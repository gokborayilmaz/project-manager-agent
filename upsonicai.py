import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from upsonic import Agent, Task, ObjectResponse

# Load environment variables
load_dotenv()

app = FastAPI(title="Project Management Assistant")

# Initialize the AI agent
project_management_agent = Agent("Project Management Assistant", model="azure/gpt-4o", reflection=True)

# MCP Server Configurations
class GitHubMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-github"]
    env = {"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}

# Define response format
class ProjectDetailsResponse(ObjectResponse):
    latest_commits: list[str]
    open_pull_requests: list[str]
    open_issues: list[str]

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Management Assistant</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            #result {
                max-height: 300px;
                overflow-y: auto;
                white-space: pre-wrap;
                word-wrap: break-word;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 8px;
                background-color: #f9f9f9;
                width: 100%;
                font-size: 14px;
            }
            pre {
                white-space: pre-wrap;
                word-wrap: break-word;
            }
        </style>
    </head>
    <body class="bg-gray-100 flex justify-center items-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-lg w-96">
            <h1 class="text-2xl font-bold text-center mb-4">🚀 Project Management Assistant</h1>
            <input id="repo" type="text" placeholder="GitHub Repository (owner/repo)" class="w-full p-2 border rounded mb-4">
            <button onclick="getProjectDetails()" class="bg-blue-500 text-white px-4 py-2 rounded w-full">Get Project Details</button>
            <div id="result" class="mt-4 text-sm"></div>
        </div>
        <script>
            async function getProjectDetails() {
                const repo = document.getElementById("repo").value;
                if (!repo) {
                    alert("Please enter a repository in the format 'owner/repo'.");
                    return;
                }
                const response = await fetch(`/project_details?repo=${repo}`);
                const data = await response.json();
                document.getElementById("result").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            }
        </script>
    </body>
    </html>
    """

@app.get("/project_details")
async def project_details(repo: str = Query(..., title="GitHub Repository (owner/repo)")):
    """Fetch project details using GitHub MCP server."""
    try:
        project_task = Task(
            f"Retrieve the latest commits, open pull requests, and unresolved issues for the repository {repo}.",
            tools=[GitHubMCP],
            response_format=ProjectDetailsResponse
        )
        project_management_agent.do(project_task)
        response = project_task.response

        if not response:
            return {"error": "Failed to retrieve project details."}

        return {
            "latest_commits": response.latest_commits,
            "open_pull_requests": response.open_pull_requests,
            "open_issues": response.open_issues
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

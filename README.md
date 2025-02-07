## 21-Day Agent Series: Day 12 AGENT : Project Management Assistant

### Project Management Assistant

This agent is part of the "A New AI Agent Every Day!" Series - Day 12/21 - Project Management Assistant 🚀🎯. This AI agent tracks progress in GitHub repositories, analyzes project activity, and provides details about:

- Recent commits.
- Open pull requests.
- Unresolved issues.

The agent leverages **GitHub MCP** for seamless integration with GitHub projects.

---

### 🛠 Installation

#### Prerequisites

- Python 3.9 or higher
- Git
- Node.js (for MCP GitHub server)
- Virtual environment (recommended)

#### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables by creating a `.env` file in the root directory:

   ```env
   GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
   ```

4. Start the MCP GitHub server:

   ```bash
   npx -y @modelcontextprotocol/server-github
   ```

5. Run the FastAPI server:

   ```bash
   uvicorn upsonicai:app --reload
   ```

---

### 🚀 How to Use

1. Open the browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

2. Enter a GitHub repository in the format `owner/repo` (e.g., `octocat/Hello-World`).

3. Click **"Get Project Details"** to fetch:

   - Latest commits.
   - Open pull requests.
   - Open issues.

4. View the results dynamically rendered on the page.

---

### 🛠 Technical Details

#### GitHub MCP Configuration

The agent integrates with GitHub through the MCP server, allowing seamless interaction with repositories. The following command is used to start the GitHub MCP server:

```bash
npx -y @modelcontextprotocol/server-github
```

#### API Endpoints

- `/`: Returns the user interface.
- `/project_details?repo=<owner/repo>`: Fetches project details using GitHub MCP.

---

### 🔮 Future Improvements

- Add support for GitLab projects.
- Visualize commit and PR activity with graphs.
- Integrate with task management tools like Jira or Trello.

---

### 📜 License

MIT License © 2025


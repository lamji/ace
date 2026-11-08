# G016: An AI Agent in the Terminal That Reads Code and Runs gcloud/git With Permission (Gemini CLI)

**Topic:** AI-assisted tooling (Gemini CLI)
**Exam guide section:** 2.4 Planning and implementing resources using tooling: AI-assisted planning and implementation (Gemini CLI)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> A developer wants an AI assistant that runs in the terminal, can read the project's source files, suggest and make code changes, and run commands such as gcloud and git after asking for permission. Which tool should the developer use?
>
> **A.** Gemini Cloud Assist in the Google Cloud console
>
> **B.** Application Design Center
>
> **C.** Gemini CLI
>
> **D.** Cloud Shell without any AI tools

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A developer works mostly in the terminal (the text window where you type commands).
- **What you must achieve:** Get an AI helper right there that can read the project's files, change code, and run commands like gcloud (Google Cloud's command-line tool) and git (version control), after asking first.
- **The limits:** It must run in the terminal, not in a web console.
- **What they're really asking:** Which Google AI tool is an agent that lives in your terminal?

**Clues in the question:**
- "**runs in the terminal**": a command-line tool.
- "**read the project's source files … run commands … after asking for permission**": an AI **agent** that acts locally. That's **Gemini CLI**.

**Exam topic:** AI-assisted tooling (exam guide section 2.4).

---

## 📚 Key Terms Explained

### 1. Gemini CLI 🔑
- **What it is:** An open-source AI agent from Google that runs in your terminal. It reads and edits files in your project, runs shell commands (gcloud, git, tests) with your approval, and can connect to extra tools through MCP servers.
- **Looks like:** `$ gemini` → "add a health check endpoint and deploy it to Cloud Run"
- **Not to be confused with:** Gemini Cloud Assist, which is the AI help **inside the Google Cloud console** for your cloud resources.
- **Analogy:** 🧑‍💻 A helper sitting next to you at your desk who can type for you when you say yes.
- **In the online store:** Writing a new Cloud Run handler and running `gcloud run deploy`.

### 2. Google Antigravity
- **What it is:** Google's agent-first code editor (IDE), where AI agents plan and carry out coding tasks across the editor, terminal and browser.
- **Looks like:** Agent Manager view: "Build the checkout page tests" → plan → changes → review
- **Not to be confused with:** Gemini CLI. Antigravity is a full editor application, while Gemini CLI is a terminal tool.
- **Analogy:** 🏗️ A whole workshop with robot assistants, vs one helper at your desk.
- **In the online store:** Larger feature work by the storefront team.

### 🔗 How they fit together
```
 Terminal ─► Gemini CLI ─► reads repo files
                          ─► proposes edits / runs gcloud, git (asks first) ✅
 Console  ─► Gemini Cloud Assist (cloud resources, not your local repo)
```

---

## 🌍 Real-World Scenario

A developer on call needs to add a feature flag and redeploy fast. In the terminal, **Gemini CLI** reads the code, edits two files, runs the tests, and after approval runs `gcloud run deploy`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Gemini Cloud Assist in the Google Cloud console

**Wrong words:**
- ❌ "**in the Google Cloud console**": Cloud Assist works with your **cloud resources** in the console, not your local terminal and code files.

📌 **When to use it:** Use it when you want AI help understanding or fixing things in your Google Cloud projects from the console.
🏢 **Office example:** The help desk inside the building's management office.

### ❌ B
> **B.** Application Design Center

**Wrong words:**
- ❌ "**Application Design Center**": a visual architecture designer in the console, not a terminal coding agent.

📌 **When to use it:** Use it to design new apps from approved templates.
🏢 **Office example:** The architect's drawing board, not your desk helper.

### ✅ C
> **C.** Gemini CLI

**Why it's correct:**
- ✔️ "**Gemini CLI**" matches "**runs in the terminal**".
- ✔️ It reads and edits project files and runs commands with approval, matching "**read the project's source files … run commands such as gcloud and git after asking for permission**".

📌 **When to use it:** Use it when you want an AI helper right in your command window that can read your files and do tasks after you agree.
🏢 **Office example:** A helper at your desk who reads the file with you and types only when you say "go ahead".

### ❌ D
> **D.** Cloud Shell without any AI tools

**Wrong words:**
- ✔️ It's a terminal.
- ❌ "**without any AI tools**": no AI assistant to read or change code.

📌 **When to use it:** Use it for quick commands in the browser.
🏢 **Office example:** A plain notepad with no assistant.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** dev: `gemini` → "add a /healthz route to orders-api and redeploy to staging" → reviews diff → approves `gcloud run deploy orders-api --region=us-central1`.

---

## 🧠 Key Takeaways / Memory Tips

- **AI agent in the terminal → Gemini CLI. AI in the console for your cloud → Gemini Cloud Assist. Agent-first IDE → Antigravity.**
  🧠 *"**CLI = command line.**"*
- Related: **G015**, **G017**, **G023**.

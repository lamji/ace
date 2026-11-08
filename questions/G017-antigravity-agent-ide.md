# G017: An Agent-First Code Editor Where AI Agents Plan and Build Features Across Editor, Terminal and Browser (Google Antigravity)

**Topic:** AI-assisted tooling (Google Antigravity)
**Exam guide section:** 2.4 Planning and implementing resources using tooling: AI-assisted planning and implementation (Google Antigravity)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your development team wants a code editor in which AI agents can take a task such as "add a checkout page with tests," plan the work, write code across files, run commands in the terminal, and test the result in a browser, while developers review the agents' plans and changes. Which tool should the team use?
>
> **A.** Cloud Shell Editor
>
> **B.** Gemini Cloud Assist
>
> **C.** Cloud Workstations without any AI tools
>
> **D.** Google Antigravity

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A development team wants AI to do larger coding jobs, not just suggest single lines.
- **What you must achieve:** Hand an AI agent a whole task (like "build the checkout page with tests") and have it plan, write code across many files, run commands, and check the result in a browser.
- **The limits:** Developers stay in control by reviewing the agent's plan and changes. It should be a code editor (IDE).
- **What they're really asking:** Which Google tool is an agent-first code editor?

**Clues in the question:**
- "**code editor in which AI agents … plan the work, write code across files, run commands … test the result in a browser**": an **agent-first IDE**. That's **Google Antigravity**.
- "**developers review the agents' plans and changes**": the developer is a reviewer or manager of agents.

**Exam topic:** AI-assisted tooling (exam guide section 2.4).

---

## 📚 Key Terms Explained

### 1. Google Antigravity 🔑
- **What it is:** Google's agent-first development platform (an IDE). Developers give tasks to AI agents that plan and carry them out across the editor, terminal and a browser, then report back with plans and results to review.
- **Looks like:** Task: "Add checkout page + tests" → agent plan → code diffs → browser test screenshots
- **Not to be confused with:** Gemini CLI (a terminal agent) or Gemini Cloud Assist (AI help in the Cloud console).
- **Analogy:** 🏗️ A workshop where robot assistants build a piece while you inspect each step.
- **In the online store:** Building the new checkout page.

### 2. IDE
- **What it is:** Integrated development environment: an app for writing, running and debugging code.
- **Looks like:** VS Code-style editor with file tree, editor, terminal
- **Not to be confused with:** A plain text editor.
- **Analogy:** 🛠️ A fully equipped workbench.
- **In the online store:** Where developers work on the storefront.

### 🔗 How they fit together
```
 Developer ─task─► Antigravity agent ─► plan → edit files → run terminal → test in browser
            ◄──── review plan & changes ✅
```

---

## 🌍 Real-World Scenario

A storefront team gives an **Antigravity** agent the task "add gift-card support to checkout with tests". The agent proposes a plan, edits the frontend and API, runs the tests, and shows browser screenshots. A developer reviews and merges.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Cloud Shell Editor

**Wrong words:**
- ✔️ It's a code editor.
- ❌ "**Cloud Shell Editor**": a basic browser editor with no agents that plan and carry out multi-step tasks.

📌 **When to use it:** Use it for quick edits in the browser.
🏢 **Office example:** A notepad on the reception desk.

### ❌ B
> **B.** Gemini Cloud Assist

**Wrong words:**
- ❌ "**Gemini Cloud Assist**": AI help for your Google Cloud resources in the console, not a code editor where agents build features.

📌 **When to use it:** Use it to understand, troubleshoot or optimize cloud resources.
🏢 **Office example:** The building manager's help desk, not a workshop.

### ❌ C
> **C.** Cloud Workstations without any AI tools

**Wrong words:**
- ✔️ A managed developer environment.
- ❌ "**without any AI tools**": no agents to plan or build anything.

📌 **When to use it:** Use it for secure, standard developer machines.
🏢 **Office example:** A clean desk, but no assistant.

### ✅ D
> **D.** Google Antigravity

**Why it's correct:**
- ✔️ "**Google Antigravity**" matches "**code editor in which AI agents**": an agent-first IDE.
- ✔️ Its agents plan, edit files, use the terminal and test in a browser, matching "**plan the work, write code across files, run commands … test the result in a browser**".
- ✔️ Developers review the agents' plans and results, matching "**developers review**".

📌 **When to use it:** Use it when you want AI assistants to take on whole coding tasks while you check their work.
🏢 **Office example:** A workshop where assistants build the piece and you inspect it before it ships.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** storefront team: an Antigravity task builds `CheckoutGiftCard.tsx` plus API changes and Playwright tests. A human reviews and merges.

---

## 🧠 Key Takeaways / Memory Tips

- **Agent-first IDE → Antigravity. Terminal agent → Gemini CLI. Console cloud helper → Gemini Cloud Assist.**
  🧠 *"**Antigravity lifts whole tasks.**"*
- Related: **G016**, **G023**.

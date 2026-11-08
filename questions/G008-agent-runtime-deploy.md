# G008: Host an ADK AI Agent With Managed Sessions and Memory, No Servers (Agent Runtime, Formerly Vertex AI Agent Engine)

**Topic:** AI agents (Agent Runtime)
**Exam guide section:** 2.1 Selecting compute (Agent Runtime on Gemini Enterprise Agent Platform); 3.1 Deploying an agent to Agent Runtime

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your team built a customer-support AI agent with the Agent Development Kit (ADK). You want Google to host and scale the agent and manage conversation sessions and memory. You do not want to manage servers, containers, or Kubernetes clusters. What should you do?
>
> **A.** Deploy the agent to Agent Runtime on Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine).
>
> **B.** Create a GKE Standard cluster, deploy the agent as a Deployment, and build your own session database.
>
> **C.** Run the agent on a Compute Engine VM created from a custom image.
>
> **D.** Upload the agent code to a Cloud Storage bucket configured for static website hosting.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team wrote an AI agent (a program that chats with customers and can take actions) using ADK, Google's Agent Development Kit, a code library for building agents.
- **What you must achieve:** Put it online so Google runs and scales it, and remembers each customer's conversation (sessions) and long-term facts (memory).
- **The limits:** You do not want to run servers, build containers, or manage Kubernetes.
- **What they're really asking:** Which Google Cloud service is built to host AI agents with sessions and memory already handled?

**Clues in the question:**
- "**built … with the Agent Development Kit**" + "**manage conversation sessions and memory**": features of **Agent Runtime** (formerly Vertex AI Agent Engine).
- "**do not want to manage servers, containers, or Kubernetes clusters**" rules out GKE and VMs.

**Exam topic:** Compute choice for AI agents (exam guide sections 2.1 and 3.1).

---

## 📚 Key Terms Explained

### 1. AI agent
- **What it is:** A program built around an AI model that can hold a conversation, remember context, and call tools (APIs) to do tasks.
- **Looks like:** "Where's my order?" → agent calls `getOrderStatus(1234)` → replies
- **Not to be confused with:** A plain chatbot script with fixed answers.
- **Analogy:** 🧑‍💼 A support rep who can look things up and act.
- **In the online store:** ShopNow's order-help assistant.

### 2. Agent Development Kit (ADK)
- **What it is:** Google's open-source framework for writing agents in code (Python and others).
- **Looks like:** `from google.adk.agents import Agent`
- **Not to be confused with:** The hosting service. ADK is how you **build** an agent, not where it runs.
- **Analogy:** 📘 The training manual for the support rep.
- **In the online store:** The `order_helper` agent code.

### 3. Agent Runtime (formerly Vertex AI Agent Engine) 🔑
- **What it is:** A fully managed service in Gemini Enterprise Agent Platform for **deploying, scaling and running agents**, with managed **sessions** and **memory**. You deploy from code and Google handles the infrastructure.
- **Looks like:** `agent_engines.create(agent, requirements=[...])` → endpoint `projects/p/locations/us-central1/reasoningEngines/123`
- **Not to be confused with:** Cloud Run, which can run a container you build. Agent Runtime adds agent-specific sessions and memory and needs no container.
- **Analogy:** 🏢 A staffing agency office that houses, schedules and supports your reps.
- **In the online store:** Deployed `order_helper` answering storefront chat.

### 🔗 How they fit together
```
 ADK code ──deploy──► Agent Runtime (managed scale + sessions + memory) ✅
 Storefront chat ──► agent endpoint ──► tools (Orders API)
```

---

## 🌍 Real-World Scenario

An online store adds an AI helper that answers order questions. The team writes it in ADK and deploys to **Agent Runtime**. Google keeps each shopper's conversation, scales up during sales, and the team never touches a server.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the agent to Agent Runtime on Gemini Enterprise Agent Platform (formerly Vertex AI Agent Engine).

**Why it's correct:**
- ✔️ "**Agent Runtime**" matches "**Google to host and scale the agent**".
- ✔️ It has built-in sessions and memory, matching "**manage conversation sessions and memory**".
- ✔️ It is fully managed, matching "**do not want to manage servers, containers, or Kubernetes**".

📌 **When to use it:** Use it when you've built an AI helper and want Google to run it and remember conversations for you.
🏢 **Office example:** Placing your trained support staff with an agency that provides the desks, phones and call records.

### ❌ B
> **B.** Create a GKE Standard cluster, deploy the agent as a Deployment, and build your own session database.

**Wrong words:**
- ❌ "**GKE Standard cluster**": you'd manage nodes and Kubernetes, which the question rejects.
- ❌ "**build your own session database**": extra work that Agent Runtime already does.

📌 **When to use it:** Use it when you need full control of a container platform and have a team to run it.
🏢 **Office example:** Building your own call centre from scratch.

### ❌ C
> **C.** Run the agent on a Compute Engine VM created from a custom image.

**Wrong words:**
- ❌ "**Compute Engine VM**": a server to patch and scale yourself, with no built-in agent sessions.

📌 **When to use it:** Use it when software needs a full computer you control.
🏢 **Office example:** Renting an empty office and hiring IT to run it.

### ❌ D
> **D.** Upload the agent code to a Cloud Storage bucket configured for static website hosting.

**Wrong words:**
- ❌ "**static website hosting**": serves fixed files like HTML and images. It can't run agent code.

📌 **When to use it:** Use it for simple fixed web pages.
🏢 **Office example:** Pinning a printed FAQ on the wall. It can't answer questions.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** support agent:
- `order_helper` (ADK) is deployed to Agent Runtime in `us-central1`.
- Its tool calls go to the Orders API on Cloud Run through a service account with least privilege.
- Sessions keep the cart context during a chat.

---

## 🧠 Key Takeaways / Memory Tips

- **Built an agent (ADK etc.) + want managed hosting with sessions and memory → Agent Runtime (formerly Vertex AI Agent Engine).**
  🧠 *"**Agent? Agent Runtime.**"*
- Related: **G006**, **G007**.

# G023: AI-Assisted Troubleshooting of a Cloud Run Error Spike in the Console (Gemini Cloud Assist Investigation)

**Topic:** Troubleshooting (Gemini Cloud Assist)
**Exam guide section:** 3.4 Monitoring and logging: Using Gemini Cloud Assist for Cloud Monitoring; 1.1 Using Gemini Cloud Assist to analyze resources

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> After a new deployment, your Cloud Run service started returning many HTTP 500 errors. You are new to the team and want an AI-assisted way, inside the Google Cloud console, to examine related logs, metrics, and recent configuration changes and suggest likely causes and next steps. What should you do?
>
> **A.** Delete the Cloud Run service and redeploy it with a new name.
>
> **B.** Start an investigation of the issue with Gemini Cloud Assist in the Google Cloud console.
>
> **C.** Use Application Design Center to redesign the application's architecture.
>
> **D.** Use the Pricing Calculator to estimate the cost of a larger service.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Right after a new release, your Cloud Run service (Google's serverless container service) is returning lots of server errors (HTTP 500).
- **What you must achieve:** Find the likely cause and what to do next, quickly, even though you're new to the team.
- **The limits:** Use an AI helper inside the Google Cloud console that looks at logs, metrics and recent changes together.
- **What they're really asking:** Which Google Cloud console AI feature helps troubleshoot an incident?

**Clues in the question:**
- "**AI-assisted way, inside the Google Cloud console**": **Gemini Cloud Assist**.
- "**examine related logs, metrics, and recent configuration changes and suggest likely causes**": a Cloud Assist **investigation**.

**Exam topic:** Troubleshooting with AI (exam guide sections 3.4 and 1.1).

---

## 📚 Key Terms Explained

### 1. Gemini Cloud Assist 🔑
- **What it is:** The AI assistant built into the Google Cloud console. It answers questions about your resources, helps design and deploy, analyzes cost, and runs **investigations** that look across logs, metrics, configuration and changes to suggest root causes and fixes.
- **Looks like:** Console → Gemini → "Investigate 500 errors on orders-api since 10:05" → findings: "new revision missing env var DB_HOST"
- **Not to be confused with:** Gemini CLI, which is a terminal agent for your local code.
- **Analogy:** 🩺 A senior engineer who reads all the charts with you and points at the likely problem.
- **In the online store:** Diagnosing checkout 500s after a release.

### 2. HTTP 500
- **What it is:** A server-side error: the app crashed or failed to handle the request.
- **Looks like:** `500 Internal Server Error`
- **Not to be confused with:** 404 (not found) or 403 (forbidden).
- **Analogy:** 🚫 "Sorry, the kitchen broke your order."
- **In the online store:** Checkout failures after a deploy.

### 🔗 How they fit together
```
 500 errors ─► Gemini Cloud Assist investigation
     ├─ logs: "DB_HOST not set"
     ├─ metrics: errors rose at 10:05
     └─ changes: revision orders-api-00042 deployed 10:04 → likely cause ✅
```

---

## 🌍 Real-World Scenario

During a Monday release, checkout starts failing. A junior engineer opens a **Gemini Cloud Assist** investigation. In minutes it connects the 10:04 revision deployment, the error logs, and a missing environment variable, and suggests rolling traffic back to the previous revision.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Delete the Cloud Run service and redeploy it with a new name.

**Wrong words:**
- ❌ "**Delete … redeploy it with a new name**": destroys the service and its URL without learning the cause. The bug comes back with the same code.

📌 **When to use it:** Never use this as troubleshooting. Roll back traffic or fix the config.
🏢 **Office example:** Demolishing the shop because the till jammed.

### ✅ B
> **B.** Start an investigation of the issue with Gemini Cloud Assist in the Google Cloud console.

**Why it's correct:**
- ✔️ "**Gemini Cloud Assist**" matches "**AI-assisted way, inside the Google Cloud console**".
- ✔️ "**investigation of the issue**" matches "**examine related logs, metrics, and recent configuration changes and suggest likely causes and next steps**".

📌 **When to use it:** Use it when something breaks and you want an AI helper to look at all the evidence and suggest causes.
🏢 **Office example:** Asking an experienced colleague to look over the reports with you and point out what changed.

### ❌ C
> **C.** Use Application Design Center to redesign the application's architecture.

**Wrong words:**
- ❌ "**Application Design Center**": designs new architectures. It doesn't troubleshoot a live error spike.

📌 **When to use it:** Use it to design and deploy new apps from templates.
🏢 **Office example:** Redrawing the office plan because a printer jammed.

### ❌ D
> **D.** Use the Pricing Calculator to estimate the cost of a larger service.

**Wrong words:**
- ❌ "**Pricing Calculator**": estimates cost. It has nothing to do with finding the cause of errors.

📌 **When to use it:** Use it to estimate costs before building.
🏢 **Office example:** Getting a quote when the machine is broken.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: the investigation on `orders-api` finds that revision 42 lacks the `DB_HOST` secret mapping. Fix: `gcloud run services update-traffic orders-api --to-revisions=orders-api-00041=100`, then repair the config.

---

## 🧠 Key Takeaways / Memory Tips

- **AI help in the console to troubleshoot or analyze cloud resources → Gemini Cloud Assist (investigations).**
  🧠 *"**Cloud Assist = console copilot.**"*
- Related: **G016**, **G024**, **Q343** (Explain log entry).

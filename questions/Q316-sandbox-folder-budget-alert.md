# Q316: Notify Engineers as a $1,000 Sandbox Budget Nears, Automated (Folder + Budget Scoped to Folder)

**Topic:** Billing (budgets, folders)

## ❓ Question
> Your company wants to provide engineers with access to explore Google Cloud freely in a sandbox environment. The total budget for testing across your organization is $1,000. You need to ensure that engineers are notified when the budget is about to be reached. You want to automate your solution as much as possible. What should you do?
>
> **A.** Create a separate Cloud Billing account for all sandbox projects. Link a credit card with a limit of $1,000 to this billing account. Ensure all sandbox projects are linked to this new Cloud Billing account.
>
> **B.** Create a Google Cloud Folder and ensure that all sandbox projects are located under that Folder. Create a Budget Alert for $1,000 and scope it to the Folder. Configure an email alert to billing administrators and users once the budget is 90% reached.
>
> **C.** Create an email template reminding people to regularly check their Google Cloud spend. Create a Cloud Function that sends the email to all the project owners. Create a daily job in Cloud Scheduler that triggers the Cloud Function. Deploy this solution for each sandbox.
>
> **D.** Configure a billing data export to a BigQuery dataset on the Cloud Billing account. Create a dashboard for all costs related to the sandbox experiments. Share the dashboard with all engineers.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Total sandbox budget $1,000; **notify** near the limit; **automate**.

**Clues in the question:**
- "**notified when the budget is about to be reached**" → **budget alert** (e.g., 90%).
- Group all sandbox projects in a **folder** and scope the budget to it.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Budget scoped to a folder 🔑
- **What it is:** A budget can filter by projects, folders, services or labels; threshold rules send emails.
- **Looks like:** Budget `$1000`, scope: folder `sandbox`, thresholds 50/90/100%
- **Not to be confused with:** a spending cap (budgets don't stop spending).
- **Analogy:** 🔔 A warning bell for one department's spending.
- **In the online store:** ShopNow sandbox folder.

### 🔗 How they fit together
```
 folder sandbox/ (all projects) → budget $1000 → 90% email ✅
```

---

## 🌍 Real-World Scenario

All sandbox projects live in `sandbox/`; a **$1,000 budget** scoped to that folder emails engineers at 90%.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a separate Cloud Billing account for all sandbox projects. Link a credit card with a limit of $1,000 to this billing account. Ensure all sandbox projects are linked to this new Cloud Billing account.

**Wrong words:**
- ❌ "**credit card with a limit**": no notification; services break when payments fail.

📌 **When to use it:** **Never use this** as cost control.
🏢 **Office example:** Letting the card decline as your only warning.

### ✅ B
> **B.** Create a Google Cloud Folder and ensure that all sandbox projects are located under that Folder. Create a Budget Alert for $1,000 and scope it to the Folder. Configure an email alert to billing administrators and users once the budget is 90% reached.

**Why it's correct:**
- ✔️ "**Budget Alert for $1,000 … scope it to the Folder**" matches "**total budget for testing across your organization is $1,000**".
- ✔️ "**email alert … once the budget is 90% reached**" matches "**notified when the budget is about to be reached**" and "**automate**".

📌 **When to use it:** Use it when a group of work areas shares one spending limit and people should be warned before it's hit.
🏢 **Office example:** The finance office emails the test team when they've used 90% of their shared allowance.

### ❌ C
> **C.** Create an email template reminding people to regularly check their Google Cloud spend. Create a Cloud Function that sends the email to all the project owners. Create a daily job in Cloud Scheduler that triggers the Cloud Function. Deploy this solution for each sandbox.

**Wrong words:**
- ❌ "**email template … Cloud Function … daily job … for each sandbox**": custom code, and it only reminds rather than measuring spend.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Daily reminder notes instead of a real meter.

### ❌ D
> **D.** Configure a billing data export to a BigQuery dataset on the Cloud Billing account. Create a dashboard for all costs related to the sandbox experiments. Share the dashboard with all engineers.

**Wrong words:**
- ❌ "**dashboard**": people must check it; no automatic alert.

📌 **When to use it:** Use dashboards for analysis.
🏢 **Office example:** A chart on the wall that nobody watches.

---

## 🛒 E-Commerce Full-Stack Example

Budget `sandbox-1k` scoped to folder `sandbox`, alerts at 50/90/100% to `eng@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Notify near a shared limit → budget alert scoped to a folder.**
  🧠 *"**Folder groups, budget warns.**"*
- Related: **Q374**, **Q335**.

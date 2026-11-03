# Q374: Near-Real-Time Budget Threshold Notifications to Slack, Low Maintenance (Budget → Pub/Sub → Cloud Run Function → Slack)

**Topic:** Billing (programmatic budget notifications)

## ❓ Question
> You are a Cloud Billing administrator for your company. Your company uses numerous Google Cloud projects and needs to implement a cost-control mechanism. Project teams must be notified promptly when their spending approaches its limit. You need to send near real-time notifications to a team’s Slack channel when their project’s spending reaches a predefined budget threshold. Your solution must be easy to support and require minimal maintenance. What should you do?
>
> **A.** Create a detailed billing export to BigQuery. Create a Cloud Composer directed acyclic graph (DAG) that runs on a schedule to analyze the BigQuery data and post notifications to Slack.
>
> **B.** Create a programmatic budget notification to send messages to a Pub/Sub topic. Create a Cloud Run function that is triggered by messages on the topic and posts the notifications to Slack.
>
> **C.** Create a programmatic budget notification to send messages to a Pub/Sub topic. Create a Compute Engine managed instance group to pull messages from the Pub/Sub subscription and post them to Slack.
>
> **D.** Create a detailed billing export to BigQuery. Create a Cloud Scheduler job that triggers a Cloud Run function to analyze the BigQuery data and post notifications to Slack.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Post to Slack when a budget threshold is hit; **minimal maintenance**.

**Clues in the question:**
- Budget threshold → **programmatic notification to Pub/Sub**.
- Serverless handler → **Cloud Run function** posts to Slack.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Budget Pub/Sub → function 🔑 (review from Q370)
- **What it is:** Budget publishes to a topic; a function reacts.
- **Looks like:** function reads `costAmount`, `budgetAmount` → POST Slack webhook
- **Not to be confused with:** scheduled BigQuery analysis.
- **Analogy:** 📟 Automatic page to the team chat.
- **In the online store:** —

### 🔗 How they fit together
```
 budget → Pub/Sub → Cloud Run function → Slack ✅
```

---

## 🌍 Real-World Scenario

Each team's budget publishes to Pub/Sub; a **function** posts threshold messages to their Slack channel.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a detailed billing export to BigQuery. Create a Cloud Composer directed acyclic graph (DAG) that runs on a schedule to analyze the BigQuery data and post notifications to Slack.

**Wrong words:**
- ❌ "**Cloud Composer DAG**": heavy, costly, scheduled (not near real time).

📌 **When to use it:** Use Composer for complex data workflows.
🏢 **Office example:** A full scheduling department for a doorbell.

### ✅ B
> **B.** Create a programmatic budget notification to send messages to a Pub/Sub topic. Create a Cloud Run function that is triggered by messages on the topic and posts the notifications to Slack.

**Why it's correct:**
- ✔️ "**programmatic budget notification … Pub/Sub**" matches "**spending reaches a predefined budget threshold**" + "**near real-time**".
- ✔️ "**Cloud Run function … posts the notifications to Slack**" matches "**team's Slack channel**" + "**minimal maintenance**".

📌 **When to use it:** Use it when you want an automatic chat message the moment spending hits a set level.
🏢 **Office example:** An automatic note to the team chat when the allowance hits a mark.

### ❌ C
> **C.** Create a programmatic budget notification to send messages to a Pub/Sub topic. Create a Compute Engine managed instance group to pull messages from the Pub/Sub subscription and post them to Slack.

**Wrong words:**
- ✔️ Pub/Sub notification is right.
- ❌ "**Compute Engine managed instance group**": servers to maintain.

📌 **When to use it:** Use MIGs for heavy steady processing.
🏢 **Office example:** Hiring full-time staff to forward notes.

### ❌ D
> **D.** Create a detailed billing export to BigQuery. Create a Cloud Scheduler job that triggers a Cloud Run function to analyze the BigQuery data and post notifications to Slack.

**Wrong words:**
- ❌ "**billing export … Cloud Scheduler**": export has delay; polling isn't near real time; more code.

📌 **When to use it:** Use export for analysis.
🏢 **Office example:** Checking the ledger every hour.

---

## 🛒 E-Commerce Full-Stack Example

Budget per project → `budget-alerts` → function `budget-to-slack`.

---

## 🧠 Key Takeaways / Memory Tips

- **Budget alert to chat/automation → Pub/Sub + Cloud Run function.**
  🧠 *"**Budget → Pub/Sub → function → Slack.**"*
- Related: **Q370**.

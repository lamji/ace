# Q172: Get Notified if a Specific Error Comes Back (Log-Based Metric + Alerting Policy)

**Topic:** Monitoring (log-based metrics, alerting policies)

## ❓ Question
> You are monitoring an application and receive user feedback that a specific error is spiking. You notice that the error is caused by a Service Account having insufficient permissions. You are able to solve the problem but want to be notified if the problem recurs. What should you do?
>
> **A.** In the Log Viewer, filter the logs on severity 'Error' and the name of the Service Account.
>
> **B.** Create a sink to BigQuery to export all the logs. Create a Data Studio dashboard on the exported logs.
>
> **C.** Create a custom log-based metric for the specific error to be used in an Alerting Policy.
>
> **D.** Grant Project Owner access to the Service Account.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Users report a spike in one error. You found it was caused by a service account missing a permission, and you fixed it.
- **What you must achieve:** Be notified if the same problem happens again.
- **The limits:** None stated.
- **What they're really asking:** How do you get an alert when that error shows up again?

**Clues in the question:**
- "**want to be notified if the problem recurs**" → an **alerting policy**.
- The error lives in **logs**, so first turn it into a number with a **log-based metric**.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Log-based metric 🔑
- **What it is:** A **counter** that goes up each time a log line matches your filter.
- **Looks like:** filter: `severity=ERROR AND protoPayload.status.code=7 AND protoPayload.authenticationInfo.principalEmail="orders-sa@…"`
- **Not to be confused with:** the logs themselves.
- **Analogy:** 🧮 A tally clicker for one kind of complaint.
- **In the online store:** Count of PERMISSION_DENIED errors.

### 2. Alerting policy
- **What it is:** A rule that **notifies you** (email, SMS, Slack) when a metric crosses a threshold.
- **Looks like:** "if metric > 0 for 1 min → email oncall@"
- **Not to be confused with:** a dashboard.
- **Analogy:** 🚨 A smoke alarm.
- **In the online store:** Pages on-call.

### 🔗 How they fit together
```
 logs ─filter─► log-based metric (count) ─► alerting policy (>0) ─► email/Slack ✅
```

---

## 🌍 Real-World Scenario

After fixing a permission error, the engineer creates a **log-based metric** that counts that exact error and an **alert** that emails the team if it is ever above zero.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In the Log Viewer, filter the logs on severity 'Error' and the name of the Service Account.

**Wrong words:**
- ❌ "**In the Log Viewer, filter the logs**": you'd have to keep checking by hand. No notification.

📌 **When to use it:** Use it to investigate an error right now.
🏢 **Office example:** Reading the complaint book yourself every day.

### ❌ B
> **B.** Create a sink to BigQuery to export all the logs. Create a Data Studio dashboard on the exported logs.

**Wrong words:**
- ❌ "**sink to BigQuery … Data Studio dashboard**": a dashboard shows data but **doesn't notify** anyone.

📌 **When to use it:** Use it for long-term log analysis and reports.
🏢 **Office example:** Making a wall chart that nobody looks at at night.

### ✅ C
> **C.** Create a custom log-based metric for the specific error to be used in an Alerting Policy.

**Why it's correct:**
- ✔️ "**custom log-based metric for the specific error**" matches "**a specific error**": it counts just that error.
- ✔️ "**used in an Alerting Policy**" matches "**want to be notified if the problem recurs**".

📌 **When to use it:** Use it when you want to be told automatically the moment a problem happens again.
🏢 **Office example:** A tally clicker for one complaint type, wired to ring the manager's phone.

### ❌ D
> **D.** Grant Project Owner access to the Service Account.

**Wrong words:**
- ❌ "**Grant Project Owner**": far too much power, and it doesn't notify you of anything.

📌 **When to use it:** **Never use this.** Grant only the missing role.
🏢 **Office example:** Giving the intern master keys because one door was locked.

---

## 🛒 E-Commerce Full-Stack Example

Metric `orders_sa_permission_denied` (filter on `status.code=7` + `orders-sa`). Alert: count > 0 in 5 min → Slack #oncall.

---

## 🧠 Key Takeaways / Memory Tips

- **Notify when a log error recurs → log-based metric + alerting policy.**
  🧠 *"**Count it, then alarm it.**"*
- Related: **Q117**, **Q113**.

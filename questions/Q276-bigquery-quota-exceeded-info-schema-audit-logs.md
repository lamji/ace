# Q276: BigQuery quotaExceeded Error: Diagnose It (INFORMATION_SCHEMA Views + Cloud Audit Logs)

**Topic:** BigQuery (troubleshooting quotas)

## ❓ Question
> Your company uses BigQuery to store and analyze data. Upon submitting your query in BigQuery, the query fails with a quotaExceeded error. You need to diagnose the issue causing the error. What should you do? (Choose two.)
>
> **A.** Use BigQuery BI Engine to analyze the issue.
>
> **B.** Use the INFORMATION_SCHEMA views to analyze the underlying issue.
>
> **C.** Configure Cloud Trace to analyze the issue.
>
> **D.** Search errors in Cloud Audit Logs to analyze the issue.
>
> **E.** View errors in Cloud Monitoring to analyze the issue.

**My answer:** — (didn't know)
**Correct answer:** B, D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** A query failed with **quotaExceeded**. Where do you look?

**Clues in the question:**
- Google's troubleshooting guide for quota errors: query **INFORMATION_SCHEMA** (e.g. `JOBS` views) and search **Cloud Audit Logs** for the error details.

**Exam topic:** BigQuery.

---

## 📚 Key Terms Explained

### 1. INFORMATION_SCHEMA 🔑
- **What it is:** Built-in BigQuery views with metadata about jobs, tables and reservations.
- **Looks like:** `SELECT * FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT WHERE error_result.reason='quotaExceeded'`
- **Not to be confused with:** BI Engine.
- **Analogy:** 📋 The library's own record book.
- **In the online store:** Who ran heavy queries.

### 2. Cloud Audit Logs for BigQuery
- **What it is:** Logs each job with status and error message.
- **Looks like:** `protoPayload.status.message:"quotaExceeded"`
- **Not to be confused with:** —
- **Analogy:** 📓 Logbook.
- **In the online store:** —

### 🔗 How they fit together
```
 quotaExceeded → INFORMATION_SCHEMA.JOBS (which jobs, how many) ✅ + Audit Logs (error details) ✅
```

---

## 🌍 Real-World Scenario

An analyst's query fails with quotaExceeded. The admin checks **INFORMATION_SCHEMA.JOBS** for concurrent/large jobs and filters **audit logs** for the error.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use BigQuery BI Engine to analyze the issue.

**Wrong words:**
- ❌ "**BI Engine**": an in-memory accelerator for dashboards, not a diagnostic tool.

📌 **When to use it:** Use BI Engine to speed up dashboards.
🏢 **Office example:** Buying a faster car to find out why you got a ticket.

### ✅ B
> **B.** Use the INFORMATION_SCHEMA views to analyze the underlying issue.

**Why it's correct:**
- ✔️ "**INFORMATION_SCHEMA views**" matches "**diagnose the issue causing the error**": shows jobs, bytes, concurrency that hit the quota.

📌 **When to use it:** Use it when you need the system's own records about what ran.
🏢 **Office example:** Reading the library's records of who borrowed what and how much.

### ❌ C
> **C.** Configure Cloud Trace to analyze the issue.

**Wrong words:**
- ❌ "**Cloud Trace**": traces latency in your own applications, not BigQuery quotas.

📌 **When to use it:** Use Trace to find slow parts of your app.
🏢 **Office example:** Timing the walk to the library to see why you were refused.

### ✅ D
> **D.** Search errors in Cloud Audit Logs to analyze the issue.

**Why it's correct:**
- ✔️ "**Search errors in Cloud Audit Logs**" matches "**query fails with a quotaExceeded error**": the log entry shows which quota and when.

📌 **When to use it:** Use it to find the exact error message and when it happened.
🏢 **Office example:** Checking the front-desk logbook for the refusal note.

### ❌ E
> **E.** View errors in Cloud Monitoring to analyze the issue.

**Wrong words:**
- ❌ "**Cloud Monitoring**": shows metrics, not the detailed quota error for your job.

📌 **When to use it:** Use Monitoring for usage trends and alerts.
🏢 **Office example:** Looking at a visitor count chart for the reason you were refused.

---

## 🛒 E-Commerce Full-Stack Example

`SELECT user_email, COUNT(*) FROM region-us.INFORMATION_SCHEMA.JOBS_BY_PROJECT WHERE creation_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) AND error_result.reason='quotaExceeded' GROUP BY 1`

---

## 🧠 Key Takeaways / Memory Tips

- **BigQuery quota errors → INFORMATION_SCHEMA + Cloud Audit Logs.**
  🧠 *"**Schema for what ran, audit logs for why it failed.**"*
- Related: **Q193**, **Q227**.

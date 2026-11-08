# Q193: Data Studio Charts Broke After the Nightly Table Overwrite (Review the Nightly Job in BigQuery)

**Topic:** BigQuery (job history, troubleshooting)

## ❓ Question
> You are using Data Studio to visualize a table from your data warehouse that is built on top of BigQuery. Data is appended to the data warehouse during the day. At night, the daily summary is recalculated by overwriting the table. You just noticed that the charts in Data Studio are broken, and you want to analyze the problem. What should you do?
>
> **A.** Review the Error Reporting page in the Cloud Console to find any errors.
>
> **B.** Use the BigQuery interface to review the nightly job and look for any errors.
>
> **C.** Use Cloud Debugger to find out why the data was not refreshed correctly.
>
> **D.** In Cloud Logging, create a filter for your Data Studio report.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Data Studio (now Looker Studio, a chart tool) shows a BigQuery table. Data is added during the day, and each night the summary table is rebuilt by overwriting it. The charts are now broken.
- **What you must achieve:** Analyze what went wrong.
- **The limits:** None stated.
- **What they're really asking:** Where do you look to understand what happened to the table?

**Clues in the question:**
- "**At night, the daily summary is recalculated by overwriting the table**" → the likely culprit is the **nightly BigQuery job** → check its **job history** in BigQuery.

**Exam topic:** BigQuery.

---

## 📚 Key Terms Explained

### 1. BigQuery job history 🔑
- **What it is:** A list of every query/load job with status and **error messages**.
- **Looks like:** BigQuery console → Job history → failed job → "Table schema changed"
- **Not to be confused with:** Error Reporting (app crashes).
- **Analogy:** 📋 The night shift's work log.
- **In the online store:** Nightly sales summary job.

### 2. Data Studio / Looker Studio
- **What it is:** Google's free dashboard tool that reads BigQuery tables.
- **Looks like:** —
- **Not to be confused with:** BigQuery itself.
- **Analogy:** 📊 The wall chart.
- **In the online store:** Sales dashboard.

### 🔗 How they fit together
```
 nightly job overwrites table ─✗─► Data Studio charts break
 → BigQuery Job history shows the error ✅
```

---

## 🌍 Real-World Scenario

A morning dashboard is broken. The analyst opens **BigQuery job history**, finds last night's overwrite failed (or changed a column name), and fixes the job.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Review the Error Reporting page in the Cloud Console to find any errors.

**Wrong words:**
- ❌ "**Error Reporting**": collects crashes from your application code, not BigQuery job failures.

📌 **When to use it:** Use it to see app exceptions grouped together.
🏢 **Office example:** Checking the IT crash log for an accounting mistake.

### ✅ B
> **B.** Use the BigQuery interface to review the nightly job and look for any errors.

**Why it's correct:**
- ✔️ "**Use the BigQuery interface to review the nightly job**" matches "**At night, the daily summary is recalculated by overwriting the table**": that job is where things broke.
- ✔️ "**look for any errors**" matches "**analyze the problem**".

📌 **When to use it:** Use it when a report breaks right after a scheduled update.
🏢 **Office example:** Reading the night shift's log to see what went wrong with last night's update.

### ❌ C
> **C.** Use Cloud Debugger to find out why the data was not refreshed correctly.

**Wrong words:**
- ❌ "**Cloud Debugger**": inspected running app code (now retired). Not for BigQuery jobs.

📌 **When to use it:** **Never use this** today (retired).
🏢 **Office example:** Using a microscope on the wrong desk.

### ❌ D
> **D.** In Cloud Logging, create a filter for your Data Studio report.

**Wrong words:**
- ❌ "**filter for your Data Studio report**": Data Studio reports don't write logs to your Cloud Logging.

📌 **When to use it:** Use Logging for your own services' logs.
🏢 **Office example:** Searching the building log for a visitor who never signed in.

---

## 🛒 E-Commerce Full-Stack Example

BigQuery → Job history → `summary_nightly` job failed: "Field `revenue` changed type". Fix the query; dashboard recovers.

---

## 🧠 Key Takeaways / Memory Tips

- **Broken after a nightly BigQuery job → check BigQuery job history.**
  🧠 *"**Broke at night? Read the night job.**"*
- Related: **Q227** (same, Looker Studio).

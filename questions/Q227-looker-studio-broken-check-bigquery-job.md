# Q227: Looker Studio Charts Broke After the Nightly Table Overwrite (Review the Nightly Job in BigQuery)

**Topic:** BigQuery (job history)

## ❓ Question
> You are using Looker Studio to visualize a table from your data warehouse that is built on top of BigQuery. Data is appended to the data warehouse during the day. At night, the daily summary is recalculated by overwriting the table. You just noticed that the charts in Looker Studio are broken, and you want to analyze the problem. What should you do?
>
> **A.** In Cloud Logging, create a filter for your Looker Studio report.
>
> **B.** Use the open source CLI tool, Snapshot Debugger, to find out why the data was not refreshed correctly.
>
> **C.** Review the Error Reporting page in the Google Cloud console to find any errors.
>
> **D.** Use the BigQuery interface to review the nightly job and look for any errors.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Looker Studio (a chart tool) shows a BigQuery table. Data is added during the day, and each night the summary table is rebuilt by overwriting it. The charts are now broken.
- **What you must achieve:** Analyze what went wrong.
- **The limits:** None stated.
- **What they're really asking:** Where do you look to understand what happened to the table?

**Clues in the question:**
- "**At night … overwriting the table**" → check the **nightly BigQuery job** in job history.

**Exam topic:** BigQuery.

---

## 📚 Key Terms Explained

### 1. BigQuery job history 🔑 (review from Q193)
- **What it is:** Every job's status and error.
- **Looks like:** —
- **Not to be confused with:** Error Reporting.
- **Analogy:** 📋 Night shift log.
- **In the online store:** —

### 2. Snapshot Debugger
- **What it is:** Open-source successor of Cloud Debugger for inspecting **running app code**.
- **Looks like:** —
- **Not to be confused with:** BigQuery tools.
- **Analogy:** 🔬 A microscope for app code.
- **In the online store:** —

### 🔗 How they fit together
```
 nightly overwrite job ✗ → BigQuery job history ✅
```

---

## 🌍 Real-World Scenario

The morning dashboard is broken; the analyst checks **BigQuery job history** for last night's overwrite job.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In Cloud Logging, create a filter for your Looker Studio report.

**Wrong words:**
- ❌ "**filter for your Looker Studio report**" in Cloud Logging: Looker Studio reports don't log to your project.

📌 **When to use it:** Use Logging for your own services.
🏢 **Office example:** Searching the building log for a visitor who never signed in.

### ❌ B
> **B.** Use the open source CLI tool, Snapshot Debugger, to find out why the data was not refreshed correctly.

**Wrong words:**
- ❌ "**Snapshot Debugger**": inspects running application code, not BigQuery jobs.

📌 **When to use it:** Use it to debug live app code.
🏢 **Office example:** A microscope on the wrong desk.

### ❌ C
> **C.** Review the Error Reporting page in the Google Cloud console to find any errors.

**Wrong words:**
- ❌ "**Error Reporting**": collects app crashes, not BigQuery job errors.

📌 **When to use it:** Use it for app exceptions.
🏢 **Office example:** The IT crash log for an accounting mistake.

### ✅ D
> **D.** Use the BigQuery interface to review the nightly job and look for any errors.

**Why it's correct:**
- ✔️ "**Use the BigQuery interface to review the nightly job**" matches "**At night, the daily summary is recalculated by overwriting the table**".
- ✔️ "**look for any errors**" matches "**analyze the problem**".

📌 **When to use it:** Use it when a report breaks right after a scheduled update.
🏢 **Office example:** Reading the night shift's log.

---

## 🛒 E-Commerce Full-Stack Example

BigQuery → Job history → `summary_nightly` failed → fix and rerun.

---

## 🧠 Key Takeaways / Memory Tips

- **Broken after nightly BigQuery job → BigQuery job history.**
  🧠 *"**Broke at night? Read the night job.**"*
- Related: **Q193**.

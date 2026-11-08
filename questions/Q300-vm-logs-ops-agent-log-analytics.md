# Q300: Retain and Explore Compute Engine App Logs With SQL and Charts (Ops Agent + Log Analytics)

**Topic:** Logging (Ops Agent, Log Analytics)

## ❓ Question
> Your company is seeking a scalable solution to retain and explore application logs hosted on Compute Engine. You must be able to analyze your logs with SQL queries, and you want to be able to create charts to identify patterns and trends in your logs over time. You want to follow Google-recommended practices and minimize your operational costs. What should you do?
>
> **A.** Use a custom script to push your application logs to BigQuery for exploration.
>
> **B.** Ingest your application logs to Cloud Logging by using Ops Agent, and explore your logs in Logs Explorer.
>
> **C.** Ingest your application logs to Cloud Logging by using Ops Agent, and explore your logs with Log Analytics.
>
> **D.** Use a custom script to push your application logs to Cloud SQL for exploration.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your apps run on Compute Engine and write logs.
- **What you must achieve:** Keep and explore the logs: analyze them with SQL and build charts of patterns over time.
- **The limits:** Scalable, recommended practice, and low running cost.
- **What they're really asking:** How do you collect the VM logs and analyze them with SQL and charts?

**Clues in the question:**
- Get logs off the VM → **Ops Agent** (Q231).
- "**SQL queries**" + "**charts**" → **Log Analytics** (Q280). Logs Explorer doesn't do SQL.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Log Analytics 🔑 (review from Q280)
- **What it is:** SQL queries and charts on Cloud Logging buckets.
- **Looks like:** —
- **Not to be confused with:** Logs Explorer (filters).
- **Analogy:** 🔎 SQL search desk.
- **In the online store:** —

### 🔗 How they fit together
```
 VM logs ─ Ops Agent ─► Cloud Logging ─ Log Analytics (SQL + charts) ✅
```

---

## 🌍 Real-World Scenario

A team installs the **Ops Agent** on VMs and uses **Log Analytics** to chart error trends with SQL.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use a custom script to push your application logs to BigQuery for exploration.

**Wrong words:**
- ❌ "**custom script to push … to BigQuery**": code to maintain.

📌 **When to use it:** **Avoid** custom shipping when agents exist.
🏢 **Office example:** Hand-carrying logbooks to the library.

### ❌ B
> **B.** Ingest your application logs to Cloud Logging by using Ops Agent, and explore your logs in Logs Explorer.

**Wrong words:**
- ✔️ Ops Agent is right.
- ❌ "**Logs Explorer**": filter-based, not SQL.

📌 **When to use it:** Use Logs Explorer for quick searches.
🏢 **Office example:** Flipping pages instead of querying.

### ✅ C
> **C.** Ingest your application logs to Cloud Logging by using Ops Agent, and explore your logs with Log Analytics.

**Why it's correct:**
- ✔️ "**Ops Agent**" matches "**application logs hosted on Compute Engine**".
- ✔️ "**Log Analytics**" matches "**analyze your logs with SQL queries**" + "**create charts**".

📌 **When to use it:** Use it when you want to search and chart your machines' logs with a query language.
🏢 **Office example:** A courier brings logbooks to a library where you can run searches and draw charts.

### ❌ D
> **D.** Use a custom script to push your application logs to Cloud SQL for exploration.

**Wrong words:**
- ❌ "**custom script … Cloud SQL**": wrong store for logs, plus code.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Filing logs in the customer ledger.

---

## 🛒 E-Commerce Full-Stack Example

Ops Agent on `legacy-api` VMs → bucket `app-logs` (Log Analytics on) → chart of 5xx per hour.

---

## 🧠 Key Takeaways / Memory Tips

- **VM logs + SQL + charts → Ops Agent + Log Analytics.**
  🧠 *"**Agent ships, Analytics queries.**"*
- Related: **Q280**, **Q231**.

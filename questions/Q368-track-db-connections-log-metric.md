# Q368: Track How Many DB Connections a Cloud Run App Creates (Log Each Connection + Log-Based Metric)

**Topic:** Monitoring (log-based metrics)

## ❓ Question
> You are creating and deploying an application on Cloud Run that uses Cloud SQL for data storage. You need to track the number of database connections created by the application to ensure that database connections are reused. What should you do?
>
> **A.** In Cloud Monitoring, create a custom metric that tracks the creation of Cloud Run instances, and display the metric on a dashboard.
>
> **B.** Log each new database connection in the application. In Cloud Monitoring, create a custom metric for these logs, and display the metric on a dashboard.
>
> **C.** In the Google Cloud console, navigate to the Cloud SQL instance, and review the instance logs.
>
> **D.** In Cloud Trace, enable trace storage for your project, and use a filter to check for new database connections.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app on Cloud Run uses Cloud SQL.
- **What you must achieve:** Track how many database connections the app creates, to check that connections are reused.
- **The limits:** None stated.
- **What they're really asking:** How do you measure and chart the number of new connections?

**Clues in the question:**
- App-specific event → **log it** in the app, make a **log-based (custom) metric**, chart it.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Log-based metric 🔑
- **What it is:** A Cloud Monitoring metric that counts log entries matching a filter.
- **Looks like:** `gcloud logging metrics create db_conn_new --log-filter='jsonPayload.event="db_connection_created"'`
- **Not to be confused with:** built-in metrics.
- **Analogy:** 🧮 A tally of a certain line in the logbook.
- **In the online store:** —

### 🔗 How they fit together
```
 app logs "db_connection_created" → log-based metric → dashboard ✅
```

---

## 🌍 Real-World Scenario

The checkout app logs each new DB connection; a **log-based metric** shows whether pooling works.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In Cloud Monitoring, create a custom metric that tracks the creation of Cloud Run instances, and display the metric on a dashboard.

**Wrong words:**
- ❌ "**creation of Cloud Run instances**": instances ≠ DB connections.

📌 **When to use it:** Use instance counts for scaling insight.
🏢 **Office example:** Counting employees to know how many phone calls they made.

### ✅ B
> **B.** Log each new database connection in the application. In Cloud Monitoring, create a custom metric for these logs, and display the metric on a dashboard.

**Why it's correct:**
- ✔️ "**Log each new database connection in the application**" matches "**track the number of database connections created by the application**".
- ✔️ "**custom metric for these logs … dashboard**" matches "**ensure that database connections are reused**" (a flat count means reuse).

📌 **When to use it:** Use it when you want to count a specific thing your program does over time.
🏢 **Office example:** Writing a line in the logbook each time a new phone line is opened, then charting the tally.

### ❌ C
> **C.** In the Google Cloud console, navigate to the Cloud SQL instance, and review the instance logs.

**Wrong words:**
- ❌ "**review the instance logs**": manual and not a tracked metric.

📌 **When to use it:** Use it for ad hoc troubleshooting.
🏢 **Office example:** Reading the switchboard log by hand.

### ❌ D
> **D.** In Cloud Trace, enable trace storage for your project, and use a filter to check for new database connections.

**Wrong words:**
- ❌ "**Cloud Trace**": latency traces, not a connection count metric.

📌 **When to use it:** Use Trace for request latency.
🏢 **Office example:** A stopwatch, not a counter.

---

## 🛒 E-Commerce Full-Stack Example

`checkout-api` logs `db_connection_created`; metric `db_conn_new` per minute.

---

## 🧠 Key Takeaways / Memory Tips

- **Count app events → log them + log-based metric.**
  🧠 *"**Log it, count it.**"*
- Related: **Q300**.

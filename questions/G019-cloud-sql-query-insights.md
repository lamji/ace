# G019: Find the SQL Queries Slowing Cloud SQL and Get Index Suggestions (Query Insights + Index Advisor)

**Topic:** Cloud SQL (Query Insights)
**Exam guide section:** 3.4 Monitoring and logging: Using cloud diagnostic tools (Query Insights, index advisor)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Users report that the order history page has become slow. The data is stored in Cloud SQL for PostgreSQL. You need to identify which SQL queries create the most database load, view their execution plans, and get recommendations for missing indexes, with minimal setup. What should you do?
>
> **A.** Increase the Cloud SQL instance's machine type to the largest available size.
>
> **B.** Enable Query Insights on the Cloud SQL instance, review the top queries and their query plans, and use index advisor recommendations.
>
> **C.** Export the database to BigQuery every night and analyze the tables there.
>
> **D.** Use Cloud Trace to view request latency without examining the database.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

> ℹ️ **Note:** Some features, such as index advisor and longer retention, may depend on the Cloud SQL edition (Enterprise Plus has the most).

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A web page that reads order history is slow. Its data lives in Cloud SQL for PostgreSQL (Google's managed relational database).
- **What you must achieve:** Find which SQL queries put the most load on the database, see how the database runs them (execution plans), and get advice on missing indexes (lookup shortcuts that speed up searches).
- **The limits:** Do it with minimal setup.
- **What they're really asking:** Which built-in Cloud SQL feature diagnoses slow queries?

**Clues in the question:**
- "**which SQL queries create the most database load**" + "**execution plans**": **Query Insights**.
- "**recommendations for missing indexes**": **index advisor**.
- "**minimal setup**": built into Cloud SQL, you just turn it on.

**Exam topic:** Diagnostics (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Query Insights 🔑
- **What it is:** A Cloud SQL (and AlloyDB) feature that shows database load by query, user and app tag, with query plans and latency over time.
- **Looks like:** Console → Cloud SQL → `orders-db` → Query insights → top query: `SELECT … FROM orders WHERE customer_id=$1 ORDER BY created_at`
- **Not to be confused with:** Cloud Trace (request timing across services) or Cloud Logging.
- **Analogy:** 🕵️ A dashboard that shows which clerk is causing the queue at the counter.
- **In the online store:** Finds the slow order-history query.

### 2. Index advisor / index
- **What it is:** An index is a lookup structure that lets the database find rows without scanning the whole table. Index advisor analyzes your queries and recommends indexes to create.
- **Looks like:** `CREATE INDEX idx_orders_cust_created ON orders(customer_id, created_at);`
- **Not to be confused with:** Adding CPU or memory.
- **Analogy:** 📇 The index at the back of a book.
- **In the online store:** Recommended index on `orders(customer_id, created_at)`.

### 🔗 How they fit together
```
 Slow page ─► Cloud SQL Query Insights ─► top query + plan (Seq Scan on orders 🐢)
           ─► index advisor: CREATE INDEX … ✅ ─► fast lookup
```

---

## 🌍 Real-World Scenario

After a year of growth, the `orders` table holds 40 million rows. **Query Insights** shows one query doing full table scans. Index advisor suggests a composite index, and the page goes from 4 seconds to 80 milliseconds without a bigger machine.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Increase the Cloud SQL instance's machine type to the largest available size.

**Wrong words:**
- ❌ "**largest available size**": costly guessing. It doesn't tell you which query is slow, and a missing index stays missing.

📌 **When to use it:** Use a bigger machine when you've confirmed the database is truly out of CPU or memory.
🏢 **Office example:** Hiring more clerks without finding out why the line is slow.

### ✅ B
> **B.** Enable Query Insights on the Cloud SQL instance, review the top queries and their query plans, and use index advisor recommendations.

**Why it's correct:**
- ✔️ "**Enable Query Insights**" matches "**minimal setup**".
- ✔️ "**review the top queries and their query plans**" matches "**which SQL queries create the most database load, view their execution plans**".
- ✔️ "**index advisor recommendations**" matches "**recommendations for missing indexes**".

📌 **When to use it:** Use it when a database feels slow and you want it to show you which requests are the problem and how to fix them.
🏢 **Office example:** Watching the counter to see which request holds up the line, then adding a quick-lookup index card.

### ❌ C
> **C.** Export the database to BigQuery every night and analyze the tables there.

**Wrong words:**
- ❌ "**Export … every night and analyze the tables**": analyzes the data, not how live queries perform. No plans and no index advice.

📌 **When to use it:** Use BigQuery exports for business reporting.
🏢 **Office example:** Analyzing sales reports when the problem is the slow counter.

### ❌ D
> **D.** Use Cloud Trace to view request latency without examining the database.

**Wrong words:**
- ✔️ Trace can show the request is slow.
- ❌ "**without examining the database**": you won't learn which SQL query is the problem or get index advice.

📌 **When to use it:** Use Cloud Trace to see which service in a chain slows a request.
🏢 **Office example:** Timing the whole visit without looking inside the records room.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `orders-db` (Cloud SQL PostgreSQL): Query Insights flags `GET /orders/history`. Index advisor adds `idx_orders_cust_created`. p95 latency drops from 4s to 80ms.

---

## 🧠 Key Takeaways / Memory Tips

- **Slow Cloud SQL/AlloyDB queries → Query Insights (top queries, plans) + index advisor.**
  🧠 *"**Slow SQL? Ask Query Insights.**"*
- Related: **Q269**, **G048** (Profiler).

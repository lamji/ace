# Q015: Estimating BigQuery Query Cost with a Dry Run

**Topic:** BigQuery (on-demand pricing, bytes processed, dry run, Pricing Calculator)

## ❓ Question
> You need to run an important query in BigQuery but expect it to return a lot of records. You want to find out how much it will cost to run the query. You are using on-demand pricing. What should you do?
>
> **A.** Arrange to switch to Flat-Rate pricing for this query, then move back to on-demand.
>
> **B.** Use the command line to run a dry run query to estimate the number of bytes read. Then convert that bytes estimate to dollars using the Pricing Calculator.
>
> **C.** Use the command line to run a dry run query to estimate the number of bytes returned. Then convert that bytes estimate to dollars using the Pricing Calculator.
>
> **D.** Run a select count (*) to get an idea of how many records your query will look through. Then convert that number of rows to dollars using the Pricing Calculator.

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are about to run a large BigQuery query (BigQuery is Google's data warehouse; with on-demand pricing you pay for how much data each query reads).
- **What you must achieve:** Know what the query will cost before you run it.
- **The limits:** You are on on-demand pricing.
- **What they're really asking:** How do you find out how much data the query will read, so you can work out its cost first?

| Keyword | What it hints at |
|---|---|
| "**on-demand pricing**" | You pay per **bytes processed (read/scanned)** |
| "**find out how much it will cost**" | Estimate **before** running, so use a **dry run** |
| "**return a lot of records**" | ⚠️ **Distractor.** Cost does **not** depend on how much data comes back |

**Exam topic:** BigQuery, specifically **cost estimation**.

⚠️ **Update:** "Flat-Rate pricing" has been replaced by **BigQuery editions** (capacity-based pricing using slots). The idea is the same: you pay for **reserved capacity** instead of per query.

---

## 📚 Key Terms Explained

### 1️⃣ BigQuery
- **What it is:** Google's **serverless data warehouse** for analyzing **huge amounts of data** (gigabytes to petabytes) with **SQL**. There are no servers to manage.
- **Analogy:** 📚 A **giant company archive** with a super-fast research team. You ask a question, and they search millions of records in seconds.
- **In the online store:** All of ShopNow's order history (years of orders) lives in BigQuery for sales reports.

### 2️⃣ Query
- **What it is:** A **question written in SQL**, e.g., "total sales per month."
- **Analogy:** 📝 A **research request form** you give to the archive team.

### 3️⃣ On-demand Pricing vs Flat-Rate (now Editions / Capacity) Pricing
| | **On-demand** | **Flat-rate → Editions (capacity)** |
|---|---|---|
| **You pay for** | **Bytes processed** by each query | **Reserved capacity (slots)** over time |
| **Price** | About **$6.25 per TiB** read (first 1 TiB per month free; check the pricing page) | A fixed/committed amount, whatever the number of queries |
| **Good for** | Occasional or unpredictable queries | Heavy, steady query use with a predictable bill |
- **Analogy:** 🧾 On-demand = paying a researcher **per page they read**. Flat-rate/editions = paying an **in-house researcher a monthly salary**.

### 4️⃣ Bytes Read (Processed / Scanned) vs Bytes Returned
- **Bytes read / processed:** How much data BigQuery **has to go through** to answer the query. **This is what you pay for.**
- **Bytes returned:** How big the **result** is (the rows you get back). **This does NOT affect on-demand cost.**
- **Analogy:** 📚 The researcher reads **500 books** (bytes read) to answer your question, but hands you a **one-page summary** (bytes returned). You pay for the **500 books**.

### 5️⃣ Columnar Storage (why bytes read depends on columns)
- **What it is:** BigQuery stores data **by column**, not by row. A query only reads the **columns it uses**, across **all rows** (unless the table is partitioned or clustered).
- So `SELECT *` reads **every column**, which is expensive. Choosing only the needed columns is cheaper.
- ⚠️ **`LIMIT 10` does NOT reduce cost.** BigQuery still reads the full columns, then shows you 10 rows.
- **Analogy:** 🗂️ The archive keeps **one drawer per type of information** (all dates in one drawer, all prices in another). For "total sales by month," the team opens **only** the "date" and "price" drawers.

### 6️⃣ Dry Run
- **What it is:** A **"pretend" run**. BigQuery **checks** the query and tells you **how many bytes it would process**, **without running it**. It's **free**.
- **Command:** `bq query --use_legacy_sql=false --dry_run 'SELECT ...'`
- The Console shows the same estimate before you click Run: *"This query will process X GB when run."*
- **Analogy:** 📋 Asking the researcher, *"How many pages will you need to read?"* **before** hiring them.

### 7️⃣ Pricing Calculator
- **What it is:** Google's **online calculator** that turns usage (like "40 GB processed") into an **estimated price in dollars**.
- **Analogy:** 🧮 The **price list and calculator** at the print shop.

### 8️⃣ `SELECT COUNT(*)`
- **What it is:** A query that **counts rows** in a table.
- Cost is based on **bytes**, not **rows**. A table with 1 million small rows and one with 1 million huge rows cost very different amounts to scan.

### 🔗 How They Fit Together
```
📝 Your query
   │
   │  bq query --dry_run   (free, nothing is actually run)
   ▼
📏 "This query will process 40 GB"   ← BYTES READ (what you pay for on-demand)
   │
   │  Pricing Calculator: 40 GB × ~$6.25/TiB
   ▼
💲 ≈ $0.24

(Bytes RETURNED, the size of the result, is NOT part of the on-demand price,
 and a dry run doesn't even report it.)
```

---

## 🌍 Real-World Scenario

BigQuery is very fast, but a careless query over a huge table can **cost hundreds of dollars in seconds**. Before running a big or important query, especially on production data, analysts and engineers **check the cost first** with a **dry run**, then convert bytes to dollars.

Many teams also set **`--maximum_bytes_billed`** so a query **fails instead of running** if it would read more than an allowed amount.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Arrange to switch to Flat-Rate pricing for this query, then move back to on-demand.

**Why it's wrong:**
- ❌ Switching pricing models **doesn't tell you what the query costs**. It just changes **how** you're billed.
- ❌ Flat-rate/capacity pricing requires **reserving capacity** (with commitments). That's a lot of work and possibly expensive, all for one query.

**📌 When to use it:** Use flat-rate/capacity pricing when your company **runs lots of queries every day** and wants a **fixed, predictable bill**. (Switching it on and off for one query is never right.)
🏢 **Office example:** Hiring an **in-house researcher on a monthly salary** because there's research work every single day, instead of paying per job.

### ✅ B
> **B.** Use the command line to run a dry run query to estimate the number of bytes read. Then convert that bytes estimate to dollars using the Pricing Calculator.

**Why it's correct:**
- ✔️ On-demand pricing charges by **bytes read (processed)**, and a **dry run** reports exactly that number.
- ✔️ A dry run is **free**, because it doesn't actually run the query.
- ✔️ The **Pricing Calculator** turns bytes into dollars.

**📌 When to use it:** Use it when you want to **know the cost before you run a query**.
🏢 **Office example:** Asking the researcher, *"**How many pages will you need to read?**"* before hiring them, because they **charge per page read**.

### ❌ C
> **C.** Use the command line to run a dry run query to estimate the number of bytes returned. Then convert that bytes estimate to dollars using the Pricing Calculator.

**Why it's wrong:**
- ❌ On-demand cost is based on **bytes read**, **not** bytes returned. A tiny result can come from a huge, expensive scan.
- ❌ A dry run **doesn't report bytes returned** anyway. It can't know the result size without actually running the query.
- ⚠️ **Trap option:** it's **one word different** from B. The question's "return a lot of records" is there to make you pick this.

**📌 When to use it:** Thinking about **bytes returned** is useful when you care about **how big the result is** (for example, whether it fits in a spreadsheet or how long a download takes), not the query cost.
🏢 **Office example:** Asking **how many pages the final summary will be**, to see if it fits in your folder. It doesn't tell you what the research will **cost**.

### ❌ D
> **D.** Run a select count (*) to get an idea of how many records your query will look through. Then convert that number of rows to dollars using the Pricing Calculator.

**Why it's wrong:**
- ❌ BigQuery on-demand pricing is per **byte**, not per **row**. You can't convert a row count to dollars, because rows can be tiny or huge.
- ❌ It counts the **whole table**, not what **your** query will read. Your query might use only 2 of 30 columns.
- ❌ It **runs a real query**, while a dry run is the proper (and free) way to estimate.

**📌 When to use it:** Use `COUNT(*)` when you simply want to know **how many records a table has**.
🏢 **Office example:** **Counting how many folders are in the filing cabinet**. Useful, but it doesn't tell you how much reading a research job will need.

---

## 🆚 B vs C: Bytes READ vs Bytes RETURNED

This is the **most important** point in the question. The two options are the same except for **one word**:

| | **B: bytes READ** ✅ | **C: bytes RETURNED** ❌ |
|---|---|---|
| **What it measures** | How much data BigQuery **goes through** to answer | How big the **answer** is |
| **Does on-demand charge for it?** | ✅ **Yes**, this is the bill | ❌ **No** |
| **Does a dry run report it?** | ✅ Yes ("will process X bytes") | ❌ No, it can't know the result size without running |
| **What makes it bigger** | More **columns** used, more **rows scanned** (bigger table, no partition filter) | More rows/columns in the **result** |
| **Does `LIMIT` reduce it?** | ❌ No, the full columns are still read | ✅ Yes |

**🏢 Office example:**
> You ask the archive team: *"What were our total sales each month for the last 2 years?"*
> - They **read through 2 years of invoices** (500 boxes) → **bytes READ** → **this is what you pay for** 💲
> - They hand you **one page with 24 numbers** → **bytes RETURNED** → tiny, and not what you pay for

**🛒 Online store example: two queries on `shopnow_analytics.orders` (2 TB, 30 columns):**

| Query | Bytes **read** (you pay) | Bytes **returned** | Cost (on-demand) |
|---|---|---|---|
| ① Monthly sales: `SELECT month, SUM(total) ... GROUP BY month` (uses only 2 columns) | **~40 GB** | 24 rows (~1 KB) | **~$0.24** |
| ② Peek at data: `SELECT * FROM orders LIMIT 10` (all 30 columns) | **~2 TiB** 😱 | 10 rows (~5 KB) | **~$12.50** |

→ Both queries return only a few KB, yet query ② **costs about 50× more**, because it **reads** every column. **Bytes returned tell you nothing about cost.** That's why **B** is right and **C** is wrong.

🧠 *"You pay for what BigQuery **READS**, not what it **RETURNS**. Like paying a researcher for the books they read, not the length of their summary."*

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's marketing team wants a **"top customers by total spending"** report from the `shopnow_analytics.orders` table in BigQuery (about **2 TB**, years of orders). The manager asks, *"How much will this cost?"*

```
🛍️ Orders (Cloud SQL) ──nightly export──► 📊 BigQuery: shopnow_analytics.orders (2 TB)
                                                 │
                       👩‍💼 Analyst: dry run first ──► 📏 bytes read ──► 🧮 Pricing Calculator ──► 💲
```

**1. Dry run (free), option B:**
```bash
bq query --use_legacy_sql=false --dry_run \
'SELECT customer_id, SUM(total) AS spent
 FROM shopnow_analytics.orders
 WHERE created_at >= "2026-01-01"
 GROUP BY customer_id
 ORDER BY spent DESC'
```
```
Query successfully validated. Assuming the tables are not modified,
running this query will process 42949672960 bytes of data.     ← 40 GiB READ
```

**2. Convert to dollars:** 40 GiB ≈ 0.039 TiB × ~$6.25/TiB ≈ **$0.24** (Pricing Calculator). ✅ Approved.

**3. Run it for real, with a safety limit:**
```bash
bq query --use_legacy_sql=false --maximum_bytes_billed=50000000000 \
'SELECT customer_id, SUM(total) AS spent ...'
# fails instead of running if it would read more than 50 GB
```

**💡 Cost-saving tips for ShopNow:**
- Select **only needed columns** (avoid `SELECT *`).
- **Partition** the table by `created_at`, so a date filter reads only the needed days.
- Remember that **`LIMIT` doesn't save money** on a normal table.

---

## 🧠 Key Takeaways / Memory Tips

- **BigQuery on-demand = you pay for BYTES READ (processed/scanned).**
- **Estimate cost → `bq query --dry_run` (free) → bytes read → Pricing Calculator → dollars.**
- **Bytes returned ≠ cost.** A tiny result can come from a huge, expensive scan.
- **Rows ≠ bytes.** You can't price a query from `COUNT(*)`.
- **`SELECT *` is expensive. `LIMIT` doesn't reduce cost.** Pick only the columns you need.
- **Flat-rate → now "editions" (capacity/slots):** a fixed bill for heavy, steady use. Not for checking one query's cost.
- 🧠 *"**Dry run = free price check.** Pay for what it **reads**, not what it **returns**."*

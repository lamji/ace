# Q017: Analyzing and Forecasting Costs with Billing Export to BigQuery

**Topic:** Billing (Cloud Billing export to BigQuery, SQL cost analysis) vs Cloud Storage / Bigtable / Sheets

## ❓ Question
> You are analyzing Google Cloud Platform service costs from three separate projects. You want to use this information to create service cost estimates by service type, daily and monthly, for the next six months using standard query syntax. What should you do?
>
> **A.** Export your bill to a Cloud Storage bucket, and then import into Cloud Bigtable for analysis.
>
> **B.** Export your bill to a Cloud Storage bucket, and then import into Google Sheets for analysis.
>
> **C.** Export your transactions to a local file, and perform analysis with a desktop tool.
>
> **D.** Export your bill to a BigQuery dataset, and then write time window-based SQL queries for analysis.

**My answer:** D
**Correct answer:** D
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You want to study your Google Cloud **spending** across **3 projects**, grouped **by service** (Compute Engine, Cloud SQL, BigQuery, ...) and **by day and month**, to **estimate the next 6 months**. You want to do it with **standard query syntax**, meaning **SQL**. Where should the billing data go?

| Keyword | What it hints at |
|---|---|
| "**service costs from three separate projects**" | Billing data from one **billing account** (covers all its projects) |
| "**by service type, daily and monthly**" | Grouping and filtering by **time windows** |
| "**standard query syntax**" | **Standard SQL**, which means **BigQuery** |
| "**next six months**" | Lots of history to analyze, plus forecasting |

**Exam topic:** Billing, specifically **exporting Cloud Billing data to BigQuery**.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Billing Account and Projects (review from Q007)
- **What it is:** One **billing account** pays for many **projects**. Billing data includes **every project** linked to it.
- **Analogy:** 💳 The **company credit account** that receives the bills from every department.
- **In the online store:** `ShopNow Corporate Billing` pays for `shopnow-prod`, `shopnow-dev`, and `shopnow-analytics`.

### 2️⃣ Cloud Billing Export to BigQuery
- **What it is:** A setting (Console → **Billing → Billing export → BigQuery export**) that **automatically and continuously** sends detailed cost data to a **BigQuery dataset**: cost per service, per project, per SKU, per hour.
- It starts collecting **from when you turn it on**, so enable it early.
- *(The old CSV/JSON "file export" to Cloud Storage has been **retired**. BigQuery export is Google's recommended method.)*
- **Analogy:** 📥 Having every receipt **automatically filed** into the accounting department's records system, every day, with no manual work.

### 3️⃣ BigQuery Dataset and Table (review from Q015)
- **Dataset:** A **folder** in BigQuery that holds tables (e.g., `billing_export`).
- **Table:** The actual data (e.g., `gcp_billing_export_v1_<BILLING_ACCOUNT_ID>`), with one row per usage item.
- **Analogy:** 🗂️ Dataset = a **filing cabinet**. Table = a **drawer** full of receipts.

### 4️⃣ Standard SQL (GoogleSQL)
- **What it is:** The normal, widely used **SQL query language** (`SELECT ... FROM ... WHERE ... GROUP BY ...`). BigQuery's dialect is called **GoogleSQL** (it used to be called "standard SQL").
- **Analogy:** 🗣️ A **common business language** every analyst already speaks.

### 5️⃣ Time Window-Based Queries
- **What it is:** SQL that **groups or filters by time periods**: per day, per month, last 30 days, last 6 months.
- **Example:** `WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 180 DAY)`
- **Analogy:** 📅 Sorting receipts into **daily piles** and **monthly folders**.

### 6️⃣ Cloud Storage Bucket (review from Q006)
- **What it is:** Storage for **files**. It can **hold** data, but it **can't analyze** it.
- **Analogy:** 📦 A **storage room**: it holds boxes but doesn't do any accounting.

### 7️⃣ Cloud Bigtable
- **What it is:** A **NoSQL** database for **huge amounts of data** with **very fast lookups by key**, e.g., IoT sensor readings or user activity. It's built for **speed at massive scale**, **not** for reports and analysis.
- **Analogy:** 📬 A giant **automated mailroom** with millions of numbered pigeonholes. You can grab any one box instantly, but it's not where you **make reports**.

### 8️⃣ Google Sheets
- **What it is:** Google's **online spreadsheet**. It's great for **small** data and sharing. It has a **cell limit** (about 10 million cells) and isn't standard SQL.
- **Analogy:** 📊 A **shared team spreadsheet** for tracking small expenses.

### 9️⃣ Local File + Desktop Tool
- **What it is:** Downloading data to **your laptop** and analyzing it in a desktop program.
- **Problems:** manual, not automatic, hard to share, limited by your computer's power, and not standard SQL.
- **Analogy:** 🖍️ **Printing a bank statement** and highlighting items with a pen at your desk.

### 🔗 How They Fit Together
```
📁 shopnow-prod ──┐
📁 shopnow-dev ───┼──► 💳 Billing account: ShopNow Corporate Billing
📁 shopnow-analytics ┘          │
                                │  Billing export → BigQuery (automatic, continuous)
                                ▼
                 📊 BigQuery dataset: billing_export
                    └── table: gcp_billing_export_v1_XXXXXX
                                │
                                │  Standard SQL, time-window queries
                                ▼
                 📈 Cost per service, per day / month → 6-month forecast
                    (+ optional: Looker Studio dashboard, BigQuery ML forecast)
```

---

## 🌍 Real-World Scenario

Finance asks the cloud team, *"How much will we spend on Google Cloud in the next 6 months, broken down by service?"* The team needs **detailed history**, **across all projects**, that's **updated automatically**, and they want to answer it with **SQL**.

Google's recommended pattern: **turn on Billing export to BigQuery**, then **query it with SQL** (and optionally build a **Looker Studio** dashboard or a **BigQuery ML** forecast on top).

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Export your bill to a Cloud Storage bucket, and then import into Cloud Bigtable for analysis.

**Why it's wrong:**
- ❌ **Bigtable** is a **NoSQL** database built for **fast key lookups** at massive scale, **not** for analysis and reports with standard SQL.
- ❌ Two extra steps (export to a bucket, then import), so it's slow and manual. (Billing file export to Cloud Storage has also been retired.)

**📌 When to use it:** Use Bigtable when you need to **store a huge amount of data** and **find single items super fast**.
🏢 **Office example:** A giant **automated mailroom** with millions of numbered pigeonholes. You can grab any one box instantly, but you don't write reports there.

### ❌ B
> **B.** Export your bill to a Cloud Storage bucket, and then import into Google Sheets for analysis.

**Why it's wrong:**
- ❌ **Sheets isn't standard SQL**, and it has a **size limit**. Months of detailed billing rows from 3 projects can be **too big**.
- ❌ It's a **manual** export and import each time, not automatic.

**📌 When to use it:** Use Sheets when the data is **small** and you want to **share a simple table** with your team.
🏢 **Office example:** The **shared team spreadsheet** for tracking small monthly office expenses.

### ❌ C
> **C.** Export your transactions to a local file, and perform analysis with a desktop tool.

**Why it's wrong:**
- ❌ **Manual**, stuck on **one laptop**, hard to share, and must be repeated every time.
- ❌ "Transactions" (payments) don't contain the **detailed usage per service per day** you need.
- ❌ It isn't **standard SQL** and doesn't scale.

**📌 When to use it:** Use it for a **small, one-time check** that only you need.
🏢 **Office example:** **Printing a bank statement** and highlighting items with a pen at your desk.

### ✅ D
> **D.** Export your bill to a BigQuery dataset, and then write time window-based SQL queries for analysis.

**Why it's correct:**
- ✔️ **Billing export to BigQuery** is Google's **built-in, automatic** way to get detailed cost data for **all projects** on a billing account.
- ✔️ **BigQuery uses standard SQL**, which matches "**standard query syntax**."
- ✔️ **Time window-based SQL** gives you exactly **daily and monthly cost by service**, the basis for a **6-month estimate**.
- ✔️ It handles **large data easily** and stays **up to date** automatically.

**📌 When to use it:** Use it when you want to **study lots of cost data over time** and **ask questions with SQL**.
🏢 **Office example:** Having **every receipt automatically filed** into the **accounting department's records system**, where analysts can pull any report: daily, monthly, or by department.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow has **3 projects** on one billing account (from Q007). Finance wants: *"Cost per service, daily and monthly, and a 6-month forecast."*

**1. Create a dataset to receive the billing data:**
```bash
bq mk --dataset --location=US shopnow-billing:billing_export
```

**2. Turn on the export (Console):** **Billing → Billing export → BigQuery export → Standard usage cost → Edit settings →** choose project `shopnow-billing`, dataset `billing_export` → **Save**.

**3. Daily cost by service, last 6 months (time window SQL):**
```sql
SELECT
  DATE(usage_start_time)  AS day,
  service.description     AS service,
  SUM(cost)               AS daily_cost
FROM `shopnow-billing.billing_export.gcp_billing_export_v1_01A2B3_C4D5E6_F7G8H9`
WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 180 DAY)
GROUP BY day, service
ORDER BY day, service;
```

**4. Monthly cost by service and project:**
```sql
SELECT
  invoice.month         AS month,      -- e.g. "202610"
  project.id            AS project,
  service.description   AS service,
  ROUND(SUM(cost), 2)   AS monthly_cost
FROM `shopnow-billing.billing_export.gcp_billing_export_v1_01A2B3_C4D5E6_F7G8H9`
GROUP BY month, project, service
ORDER BY month, monthly_cost DESC;
```
| month | project | service | monthly_cost |
|---|---|---|---|
| 202610 | shopnow-prod | Compute Engine | 1,240.50 |
| 202610 | shopnow-prod | Cloud SQL | 410.20 |
| 202610 | shopnow-analytics | BigQuery | 96.75 |

**5. (Bonus) Forecast the next 6 months with BigQuery ML, still in SQL:**
```sql
CREATE OR REPLACE MODEL `shopnow-billing.billing_export.cost_forecast`
OPTIONS (
  model_type = 'ARIMA_PLUS',
  time_series_timestamp_col = 'day',
  time_series_data_col = 'daily_cost',
  time_series_id_col = 'service'
) AS
SELECT DATE(usage_start_time) AS day, service.description AS service, SUM(cost) AS daily_cost
FROM `shopnow-billing.billing_export.gcp_billing_export_v1_01A2B3_C4D5E6_F7G8H9`
GROUP BY day, service;

SELECT * FROM ML.FORECAST(MODEL `shopnow-billing.billing_export.cost_forecast`,
                          STRUCT(180 AS horizon));   -- next ~6 months
```

**🎬 Result:** Finance gets a **Looker Studio dashboard** connected to these queries. It updates **automatically every day**, and they see that Compute Engine spikes every Black Friday. ✅

**With the other options:**
- **B (Sheets):** Hundreds of thousands of billing rows hit Sheets' size limit, and someone has to re-import them manually every week. ❌
- **C (laptop):** The analyst goes on vacation and nobody else has the file. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Analyze GCP costs" + "SQL" / "standard query syntax" → Billing export to BigQuery.**
- **Billing export works at the billing account level**, so it covers **all projects** linked to that account.
- **Enable it early.** It only collects data **from when you turn it on**.
- **BigQuery = analytics with SQL. Bigtable = fast NoSQL lookups. Sheets = small data. Local tools = manual one-offs.**
- 🧠 *"**Big**Query for **big questions** (analysis). **Big**table for **big lookups** (speed)."*
- Bonus: **Looker Studio** for dashboards, **BigQuery ML (`ARIMA_PLUS`)** for forecasts, **budgets & alerts** (from Q007) to get warned before overspending.

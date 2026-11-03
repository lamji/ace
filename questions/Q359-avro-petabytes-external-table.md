# Q359: Petabytes of Avro Data for BigQuery Analysis Without Loading (Cloud Storage + Partitioned External Table)

**Topic:** BigQuery (external tables)

## ❓ Question
> Your team manages several petabytes of historical, structured transaction data stored in Apache Avro format on-premises. You are migrating this data to Google Cloud for a machine learning project. You must ensure that the data is accessible for large-scale analysis and model training using BigQuery. You must also minimize storage costs and avoid the overhead of loading data into BigQuery’s managed storage. What should you do?
>
> **A.** Use the BigQuery Data Transfer Service to ingest all Avro files into a BigQuery native table.
>
> **B.** Migrate the data to a Cloud SQL for PostgreSQL instance, and use BigQuery federated queries to access the data.
>
> **C.** Store the data in a Cloud Storage bucket, and define a BigQuery external table partitioned by a relevant column.
>
> **D.** Store the data in a Cloud Storage bucket, define a schema, and then use the bq load command to upload files individually.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Analyze PBs of Avro in BigQuery; **cheap storage**; **don't load** into BigQuery storage.

**Clues in the question:**
- "**avoid the overhead of loading data into BigQuery's managed storage**" → **external table** on Cloud Storage.
- "**minimize storage costs**" → Cloud Storage; **partitioned** keeps queries efficient.

**Exam topic:** BigQuery.

---

## 📚 Key Terms Explained

### 1. BigQuery external table 🔑
- **What it is:** A table definition pointing to files in Cloud Storage; queries read the files directly.
- **Looks like:** `bq mk --external_table_definition=@AVRO=gs://txn/*.avro txn.history` (hive partitioning by date)
- **Not to be confused with:** native table (data loaded).
- **Analogy:** 📚 A library index pointing to books in another building.
- **In the online store:** —

### 🔗 How they fit together
```
 gs://txn/dt=.../*.avro ← BigQuery external table (partitioned) ✅
```

---

## 🌍 Real-World Scenario

An ML team keeps Avro files in **Cloud Storage** and defines a **partitioned external table** for BigQuery.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the BigQuery Data Transfer Service to ingest all Avro files into a BigQuery native table.

**Wrong words:**
- ❌ "**ingest all Avro files into a BigQuery native table**": that's loading — the thing to avoid.

📌 **When to use it:** Use native tables for heavy repeated queries.
🏢 **Office example:** Moving every book into the library.

### ❌ B
> **B.** Migrate the data to a Cloud SQL for PostgreSQL instance, and use BigQuery federated queries to access the data.

**Wrong words:**
- ❌ "**Cloud SQL for PostgreSQL**": can't hold petabytes; federated queries slow.

📌 **When to use it:** Use federated queries for small operational lookups.
🏢 **Office example:** Storing a warehouse in a filing cabinet.

### ✅ C
> **C.** Store the data in a Cloud Storage bucket, and define a BigQuery external table partitioned by a relevant column.

**Why it's correct:**
- ✔️ "**Store the data in a Cloud Storage bucket**" matches "**minimize storage costs**".
- ✔️ "**BigQuery external table partitioned by a relevant column**" matches "**accessible for large-scale analysis … using BigQuery**" + "**avoid the overhead of loading**".

📌 **When to use it:** Use it when you want to query huge files where they sit, without copying them in.
🏢 **Office example:** A library index that points to boxes in the cheap warehouse.

### ❌ D
> **D.** Store the data in a Cloud Storage bucket, define a schema, and then use the bq load command to upload files individually.

**Wrong words:**
- ❌ "**bq load … upload files individually**": loading, and manual.

📌 **When to use it:** Use bq load for normal loads.
🏢 **Office example:** Carrying every box in by hand.

---

## 🛒 E-Commerce Full-Stack Example

`gs://shopnow-txn-archive/dt=*/*.avro` → external table `ml.txn_history`.

---

## 🧠 Key Takeaways / Memory Tips

- **Query without loading → external table on Cloud Storage.**
  🧠 *"**Leave it in the bucket; point BigQuery at it.**"*
- Related: **Q292**.

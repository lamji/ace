# Q146: Ad Hoc Join of Spanner Backup and Bigtable Data (BigQuery External Tables)

**Topic:** BigQuery (external tables on Cloud Storage and Bigtable), Dataflow, Dataproc

## ❓ Question
> You have an application that uses Cloud Spanner as a database backend to keep current state information about users. Cloud Bigtable logs all events triggered by users. You export Cloud Spanner data to Cloud Storage during daily backups. One of your analysts asks you to join data from Cloud Spanner and Cloud Bigtable for specific users. You want to complete this ad hoc request as efficiently as possible. What should you do?
>
> **A.** Create a dataflow job that copies data from Cloud Bigtable and Cloud Storage for specific users.
>
> **B.** Create a dataflow job that copies data from Cloud Bigtable and Cloud Spanner for specific users.
>
> **C.** Create a Cloud Dataproc cluster that runs a Spark job to extract data from Cloud Bigtable and Cloud Storage for specific users.
>
> **D.** Create two separate BigQuery external tables on Cloud Storage and Cloud Bigtable. Use the BigQuery console to join these tables through user fields, and apply appropriate filters.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Spanner holds current user data, Bigtable logs every user event, and Spanner is exported to Cloud Storage daily. An analyst wants Spanner and Bigtable data joined for certain users.
- **What you must achieve:** Handle this one-time request.
- **The limits:** As efficiently as possible.
- **What they're really asking:** Where can you join data from both sources quickly?

**Clues in the question:**
- "**ad hoc request**" + "**as efficiently as possible**": no pipelines or clusters, just a SQL query.
- "**export Cloud Spanner data to Cloud Storage**" + "**Cloud Bigtable**": BigQuery can read **both** through **external tables** and join them with SQL.

**Exam topic:** BigQuery / data.

---

## 📚 Key Terms Explained

### 1. BigQuery external table (review from Q085) 🔑
- **What it is:** A BigQuery table that **reads data where it lives**: Cloud Storage files, Bigtable, and more. No copying.
- **Looks like:** `CREATE EXTERNAL TABLE ds.events OPTIONS(format='CLOUD_BIGTABLE', uris=['https://googleapis.com/bigtable/projects/p/instances/i/tables/events'])`
- **Not to be confused with:** a loaded table.
- **Analogy:** 📇 Catalog cards pointing to books in other buildings.
- **In the online store:** Join backups with events in one query.

### 2. Dataflow / Dataproc
- **What it is:** Dataflow = managed pipelines (Beam). Dataproc = managed Spark/Hadoop clusters. Both are **heavier** than one SQL query.
- **Looks like:** `gcloud dataflow jobs run …` / `gcloud dataproc clusters create …`
- **Not to be confused with:** a quick query.
- **Analogy:** 🏭 Building an assembly line for one question.
- **In the online store:** Nightly ETL jobs.

### 🔗 How they fit together
```
 gs://spanner-backup/users/*  ─ external table users ┐
 Bigtable events              ─ external table events ┴─► BigQuery SQL JOIN ON user_id ✅
```

---

## 🌍 Real-World Scenario

An analyst wants "profile + last 30 days of events" for 50 users. The engineer creates two **BigQuery external tables**: one on the Spanner export in Cloud Storage, one on the Bigtable events table. The analyst writes one JOIN query.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a dataflow job that copies data from Cloud Bigtable and Cloud Storage for specific users.

**Wrong words:**
- ❌ "**Create a dataflow job that copies data**": you'd write, deploy and run a pipeline for a one-off question. Not efficient.

📌 **When to use it:** Use Dataflow for repeating ETL pipelines.
🏢 **Office example:** Building an assembly line to answer one question.

### ❌ B
> **B.** Create a dataflow job that copies data from Cloud Bigtable and Cloud Spanner for specific users.

**Wrong words:**
- ❌ "**dataflow job … Cloud Spanner**": a pipeline (too heavy), and it reads live Spanner instead of the existing export.

📌 **When to use it:** Use it for regular pipelines that need live Spanner data.
🏢 **Office example:** An assembly line that also bothers the live front desk.

### ❌ C
> **C.** Create a Cloud Dataproc cluster that runs a Spark job to extract data from Cloud Bigtable and Cloud Storage for specific users.

**Wrong words:**
- ❌ "**Create a Cloud Dataproc cluster that runs a Spark job**": a cluster plus Spark code for an ad hoc request.

📌 **When to use it:** Use Dataproc when you already have Spark/Hadoop jobs.
🏢 **Office example:** Renting a factory for one question.

### ✅ D
> **D.** Create two separate BigQuery external tables on Cloud Storage and Cloud Bigtable. Use the BigQuery console to join these tables through user fields, and apply appropriate filters.

**Why it's correct:**
- ✔️ "**external tables on Cloud Storage and Cloud Bigtable**" matches "**export Cloud Spanner data to Cloud Storage**" + "**Cloud Bigtable logs all events**": BigQuery reads both where they are.
- ✔️ "**join these tables through user fields, and apply appropriate filters**" matches "**join data … for specific users**".
- ✔️ "**BigQuery console**" (one SQL query) matches "**ad hoc … as efficiently as possible**".

📌 **When to use it:** Use it when you need a quick, one-time answer combining data from different places.
🏢 **Office example:** Using catalog cards to read two archives side by side, without moving any books.

---

## 🛒 E-Commerce Full-Stack Example

```sql
SELECT u.user_id, u.tier, e.event_type, e.ts
FROM analytics.users_ext u            -- gs://shopnow-spanner-backup/users/*
JOIN analytics.events_bt e            -- Bigtable shopnow-events
  ON u.user_id = e.user_id
WHERE u.user_id IN ('u123','u456');
```

---

## 🧠 Key Takeaways / Memory Tips

- **Ad hoc SQL across Cloud Storage / Bigtable → BigQuery external tables.**
- Pipelines and clusters are for repeated jobs.
  🧠 *"**Ad hoc join? Point BigQuery at both.**"*
- Related: **Q085** (external tables), **Q139** (Bigtable).

# Q085: SQL on a 5-TB AVRO File in Cloud Storage (BigQuery External Table)

**Topic:** BigQuery (external tables / federated queries, loading data, Cloud Storage)

## ❓ Question
> You have a large 5-TB AVRO file stored in a Cloud Storage bucket. Your analysts are proficient only in SQL and need access to the data stored in this file. You want to find a cost-effective way to complete their request as soon as possible. What should you do?
>
> **A.** Load data in Cloud Datastore and run a SQL query against it.
>
> **B.** Create a BigQuery table and load data in BigQuery. Run a SQL query on this table and drop this table after you complete your request.
>
> **C.** Create external tables in BigQuery that point to Cloud Storage buckets and run a SQL query on these external tables to complete your request.
>
> **D.** Create a Hadoop cluster and copy the AVRO file to NDFS by compressing it. Load the file in a hive table and provide access to your analysts so that they can run SQL queries.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** Some people argue for B, because loaded tables query faster. But loading 5 TB takes time and you pay to store a copy. "**As soon as possible**" + "**cost-effective**" → query the file **where it already is** (C). This is the accepted answer.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A 5 TB AVRO file (a data file format) is in a Cloud Storage bucket. The analysts only know SQL.
- **What you must achieve:** Let the analysts query the data.
- **The limits:** Cheap and as soon as possible.
- **What they're really asking:** How can the analysts query this file with SQL quickly and cheaply?

**Clues in the question:**
- "**stored in a Cloud Storage bucket**": the data is already there, so don't move it.
- "**proficient only in SQL**": use **BigQuery** (SQL).
- "**cost-effective**" + "**as soon as possible**": no copying 5 TB, no new clusters. An **external table** lets BigQuery read the file directly.

**Exam topic:** BigQuery / data analytics.

---

## 📚 Key Terms Explained

### 1️⃣ AVRO file
- **What it is:** A **data file format** that stores rows of records along with a description of the columns (the schema). Common for big data exports.
- **Looks like:** `gs://shopnow-exports/orders-2026.avro` (binary, not readable as text)
- **Not to be confused with:** CSV. AVRO carries its own column names and types, so BigQuery can read it without you defining columns.
- **Analogy:** 📦 A **sealed box with a packing list taped on top**.

### 2️⃣ BigQuery external table 🔑
- **What it is:** A **BigQuery table definition that points to files in Cloud Storage** instead of storing the data inside BigQuery. You run normal SQL; BigQuery reads the files on the fly.
- **Looks like:**
  ```sql
  CREATE EXTERNAL TABLE analytics.orders_ext
  OPTIONS (format = 'AVRO', uris = ['gs://shopnow-exports/orders-2026.avro']);
  SELECT country, SUM(total) FROM analytics.orders_ext GROUP BY country;
  ```
- **Not to be confused with:** a normal (native) BigQuery table, which holds its own copy of the data.
- **Analogy:** 📇 A **library catalog card** that points to a book in the basement. You read it where it is, without photocopying it.
- **In the online store:** Analysts query last year's order export without loading it.

### 3️⃣ Loading data into BigQuery
- **What it is:** **Copying** the data into BigQuery's own storage. Faster queries later, but the load takes time and you pay to store the copy.
- **Looks like:** `bq load --source_format=AVRO analytics.orders gs://shopnow-exports/orders-2026.avro`

### 4️⃣ Datastore / Hadoop (Hive)
- **Datastore:** a **NoSQL** document database, no real SQL (only the limited GQL).
- **Hadoop + Hive:** a cluster you build and run yourself to process big data with SQL-like queries (on Google Cloud, that's Dataproc). Slow to set up and costly.

### 🔗 How they fit together
```
 gs://shopnow-exports/orders-2026.avro (5 TB)  ← stays here
            ▲
            │ reads on the fly
 BigQuery external table orders_ext  ◄── analysts write SQL ✅
```

---

## 🌍 Real-World Scenario

A partner drops a huge AVRO export into a bucket and the business wants answers today. Instead of building a pipeline, the engineer creates an **external table** in BigQuery pointing at the file. Analysts start writing SQL within minutes, and nothing is copied.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Load data in Cloud Datastore and run a SQL query against it.

**Wrong words:**
- ❌ "**Load data in Cloud Datastore**": moving 5 TB into a NoSQL database is slow and costly.
- ❌ "**run a SQL query against it**": Datastore doesn't support full SQL.

📌 **When to use it:** Use Datastore/Firestore for app data like user profiles or shopping carts.
🏢 **Office example:** Moving the whole archive into the receptionist's card file just to answer one report question.

### ❌ B
> **B.** Create a BigQuery table and load data in BigQuery. Run a SQL query on this table and drop this table after you complete your request.

**Wrong words:**
- ✔️ "Run a SQL query" in BigQuery fits analysts who know SQL.
- ❌ "**Create a BigQuery table and load data in BigQuery**": copying 5 TB takes time and you pay to store the copy. Less "as soon as possible" and less "cost-effective" than reading the file directly.

📌 **When to use it:** Use it when analysts will query the data often for a long time and need the fastest queries.
🏢 **Office example:** Photocopying the whole archive into your office because you'll read it every day.

### ✅ C
> **C.** Create external tables in BigQuery that point to Cloud Storage buckets and run a SQL query on these external tables to complete your request.

**Why it's correct:**
- ✔️ "**external tables in BigQuery that point to Cloud Storage buckets**" matches "**stored in a Cloud Storage bucket**": BigQuery reads the AVRO file right where it is.
- ✔️ "**run a SQL query**" matches "**analysts are proficient only in SQL**": analysts write normal BigQuery SQL.
- ✔️ "**point to Cloud Storage**" (no copy) matches "**cost-effective … as soon as possible**": no loading time and no second copy to pay for.

📌 **When to use it:** Use it when you need quick answers from a file that already sits in storage, without moving it.
🏢 **Office example:** Reading the archive box right where it sits in the storage room, using the catalog card.

### ❌ D
> **D.** Create a Hadoop cluster and copy the AVRO file to NDFS by compressing it. Load the file in a hive table and provide access to your analysts so that they can run SQL queries.

**Wrong words:**
- ❌ "**Create a Hadoop cluster**": machines to set up, run and pay for. Not "as soon as possible".
- ❌ "**copy the AVRO file to NDFS by compressing it**": more copying of 5 TB (and "NDFS" is a typo for HDFS).
- ❌ "**Load the file in a hive table**": yet another load step.

📌 **When to use it:** Use Hadoop/Spark (Dataproc) when you already have Hadoop jobs to move to the cloud.
🏢 **Office example:** Building a whole new records department to answer one question.

---

## 🛒 E-Commerce Full-Stack Example

A marketplace partner exports 5 TB of ShopNow order history as `gs://shopnow-exports/orders-2026.avro`. The marketing analysts want "revenue by country" today.

```sql
CREATE EXTERNAL TABLE marketing.orders_ext
OPTIONS (format = 'AVRO', uris = ['gs://shopnow-exports/orders-2026.avro']);

SELECT country, SUM(total) AS revenue
FROM marketing.orders_ext
GROUP BY country ORDER BY revenue DESC;
```
Answers in minutes. ShopNow pays only for the bytes the query scans, and nothing is copied.

---

## 🧠 Key Takeaways / Memory Tips

- **SQL on files in Cloud Storage, quickly and cheaply → BigQuery external table.**
- Load into BigQuery when you'll query a lot over time.
- Datastore isn't SQL; Hadoop is heavy.
  🧠 *"**Leave it in the bucket, point BigQuery at it.**"*
- Related: **Q068** (logs into BigQuery), **Q058** (choosing a database).

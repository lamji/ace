# Q119: Unstructured Files in Many Formats for a Dataflow ETL Job (Upload to Cloud Storage With gsutil)

**Topic:** Data (Cloud Storage as a data lake, Dataflow, BigQuery, Cloud SQL, Spanner)

## ❓ Question
> Your company has a large quantity of unstructured data in different file formats. You want to perform ETL transformations on the data. You need to make the data accessible on Google Cloud so it can be processed by a Dataflow job. What should you do?
>
> **A.** Upload the data to BigQuery using the bq command line tool.
>
> **B.** Upload the data to Cloud Storage using the gsutil command line tool.
>
> **C.** Upload the data into Cloud SQL using the import function in the console.
>
> **D.** Upload the data into Cloud Spanner using the import function in the console.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Lots of **unstructured files** in **different formats** must be available to a **Dataflow** job. Where do you put them?

**Clues in the question:**
- "**unstructured data in different file formats**": files, not tables → **Cloud Storage** (object storage for any file).
- "**processed by a Dataflow job**": Dataflow reads files from Cloud Storage easily (`gs://…`).
- BigQuery, Cloud SQL and Spanner need **structured** data with a schema.

**Exam topic:** Data / Storage.

---

## 📚 Key Terms Explained

### 1. Cloud Storage 🔑
- **What it is:** **Object storage for any file** (images, logs, PDFs, JSON, CSV, video), in buckets. The usual landing zone for raw data.
- **Looks like:** `gsutil -m cp -r ./raw-data gs://shopnow-raw/`
- **Not to be confused with:** a database.
- **Analogy:** 📦 A huge **storage room** that takes boxes of any shape.
- **In the online store:** Raw clickstream files and product feeds.

### 2. Dataflow / ETL
- **What it is:** Dataflow runs **data pipelines** (Apache Beam). ETL = **Extract, Transform, Load**: read raw data, clean and reshape it, write it somewhere useful.
- **Looks like:** `ReadFromText('gs://shopnow-raw/*.json') | Map(clean) | WriteToBigQuery(...)`
- **Not to be confused with:** a storage service.
- **Analogy:** 🏭 A **sorting line** that unpacks, cleans and labels boxes.
- **In the online store:** Turns raw clicks into tidy BigQuery tables.

### 3. gsutil
- **What it is:** The command-line tool for Cloud Storage (now also `gcloud storage`).
- **Looks like:** `gsutil cp file gs://bucket/`
- **Not to be confused with:** bq (for BigQuery).
- **Analogy:** 🚚 The delivery van to the storage room.
- **In the online store:** Uploads nightly exports.

### 🔗 How they fit together
```
 raw files (json, csv, pdf, images…) ─ gsutil ─► gs://shopnow-raw ✅ ─► Dataflow (ETL) ─► BigQuery / Cloud SQL
```

---

## 🌍 Real-World Scenario

A retailer has years of mixed-format files: CSV exports, JSON logs, XML feeds. They upload everything to a **Cloud Storage** bucket with gsutil. A **Dataflow** pipeline reads the bucket, cleans the data, and loads it into BigQuery.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Upload the data to BigQuery using the bq command line tool.

**Wrong words:**
- ❌ "**Upload the data to BigQuery**": BigQuery needs structured data with a schema. Unstructured files in many formats don't load cleanly, and ETL usually happens **before** BigQuery.

📌 **When to use it:** Use bq load for structured data (CSV, JSON, Avro, Parquet) ready to analyze.
🏢 **Office example:** Putting unsorted boxes straight onto the library's catalog shelves.

### ✅ B
> **B.** Upload the data to Cloud Storage using the gsutil command line tool.

**Why it's correct:**
- ✔️ "**Cloud Storage**" matches "**unstructured data in different file formats**": it stores any file type as-is.
- ✔️ "**Upload … using the gsutil command line tool**" matches "**make the data accessible on Google Cloud**": gsutil copies large amounts of files into a bucket.
- ✔️ "**Cloud Storage**" matches "**processed by a Dataflow job**": Dataflow reads directly from `gs://` paths.

📌 **When to use it:** Use it when you have lots of mixed files to keep before sorting and processing them.
🏢 **Office example:** Bringing every box, whatever its shape, to the big storage room before the sorting team processes it.

### ❌ C
> **C.** Upload the data into Cloud SQL using the import function in the console.

**Wrong words:**
- ❌ "**into Cloud SQL**": a relational database needs tables with columns. Unstructured files don't fit, and it isn't built for huge raw data.

📌 **When to use it:** Use Cloud SQL for app data like orders and users.
🏢 **Office example:** Forcing odd-shaped boxes into a filing cabinet with fixed drawers.

### ❌ D
> **D.** Upload the data into Cloud Spanner using the import function in the console.

**Wrong words:**
- ❌ "**into Cloud Spanner**": also a relational database, and expensive for raw files.

📌 **When to use it:** Use Spanner for global, strongly consistent relational data.
🏢 **Office example:** Storing loose boxes in the bank vault.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gsutil -m cp -r ./supplier-feeds gs://shopnow-raw/feeds/   # CSV, XML, JSON from 40 suppliers
```
A Dataflow job reads `gs://shopnow-raw/feeds/**`, converts every format into one product schema, and writes to `bigquery:catalog.products`.

---

## 🧠 Key Takeaways / Memory Tips

- **Raw / unstructured files → Cloud Storage** (the data lake), then Dataflow, then BigQuery.
- Databases need structure.
  🧠 *"**Any file, any format → a bucket.**"*
- Related: **Q085** (BigQuery external tables), **Q093** (Data Catalog).

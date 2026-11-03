# Q230: Unstructured Files for a Dataflow ETL Job (Upload to Cloud Storage With gcloud storage)

**Topic:** Cloud Storage (data for Dataflow)

## ❓ Question
> Your company has a large quantity of unstructured data in different file formats. You want to perform ETL transformations on the data. You need to make the data accessible on Google Cloud so it can be processed by a Dataflow job. What should you do?
>
> **A.** Upload the data to BigQuery using the bq command line tool.
>
> **B.** Upload the data to Cloud Storage using the gcloud storage command.
>
> **C.** Upload the data into Cloud SQL using the import function in the Google Cloud console.
>
> **D.** Upload the data into Cloud Spanner using the import function in the Google Cloud console.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Lots of **unstructured files** must be available to **Dataflow**.

**Clues in the question:**
- "**unstructured data in different file formats**" → **Cloud Storage** (stores any file).
- Dataflow reads files from Cloud Storage easily.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. ETL 🔑
- **What it is:** **Extract, Transform, Load**: read raw data, clean/reshape it, write it somewhere useful.
- **Looks like:** Dataflow reads `gs://raw/*`, writes BigQuery
- **Not to be confused with:** —
- **Analogy:** 🏭 Unpack, sort, shelve.
- **In the online store:** Clean product feeds.

### 2. gcloud storage cp
- **What it is:** Uploads files to a bucket.
- **Looks like:** `gcloud storage cp -r ./raw gs://co-raw-data/`
- **Not to be confused with:** bq load.
- **Analogy:** 📦 Shipping boxes to the warehouse.
- **In the online store:** —

### 🔗 How they fit together
```
 files (json, csv, images, pdf) ─► gs://raw-data ─► Dataflow ETL ✅
```

---

## 🌍 Real-World Scenario

A company uploads mixed raw files to **Cloud Storage** with `gcloud storage cp`, then a Dataflow job cleans and loads them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Upload the data to BigQuery using the bq command line tool.

**Wrong words:**
- ❌ "**BigQuery**": needs structured, table-shaped data; can't hold arbitrary file formats.

📌 **When to use it:** Use BigQuery for structured analytics data.
🏢 **Office example:** Putting loose boxes into a spreadsheet.

### ✅ B
> **B.** Upload the data to Cloud Storage using the gcloud storage command.

**Why it's correct:**
- ✔️ "**Upload the data to Cloud Storage**" matches "**unstructured data in different file formats**": a bucket holds any file.
- ✔️ It makes the data "**accessible … so it can be processed by a Dataflow job**".

📌 **When to use it:** Use it when you have all kinds of files that need to be processed later.
🏢 **Office example:** Shipping all the mixed boxes to one warehouse where the sorting crew can work on them.

### ❌ C
> **C.** Upload the data into Cloud SQL using the import function in the Google Cloud console.

**Wrong words:**
- ❌ "**Cloud SQL**": relational tables, not unstructured files.

📌 **When to use it:** Use Cloud SQL for app databases.
🏢 **Office example:** Filing loose photos into a ledger.

### ❌ D
> **D.** Upload the data into Cloud Spanner using the import function in the Google Cloud console.

**Wrong words:**
- ❌ "**Cloud Spanner**": relational, structured, and expensive for raw files.

📌 **When to use it:** Use Spanner for global relational data.
🏢 **Office example:** A worldwide ledger for loose boxes.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud storage cp -r ./supplier-feeds gs://shopnow-raw/feeds/` → Dataflow job normalizes into BigQuery `catalog.products`.

---

## 🧠 Key Takeaways / Memory Tips

- **Unstructured files for processing → Cloud Storage.**
  🧠 *"**Any file? A bucket.**"*
- Related: **Q213**, **Q216**.

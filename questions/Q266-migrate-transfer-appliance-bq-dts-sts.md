# Q266: 200 TB Videos, Redshift Warehouse, 20 GB S3 PNGs, No Code (Transfer Appliance, BigQuery Data Transfer Service, Storage Transfer Service)

**Topic:** Migration (transfer services)

## ❓ Question
> You are planning to migrate your on-premises data to Google Cloud. The data includes: • 200 TB of video files in SAN storage • Data warehouse data stored on Amazon Redshift • 20 GB of PNG files stored on an S3 bucket. You need to load the video files into a Cloud Storage bucket, transfer the data warehouse data into BigQuery, and load the PNG files into a second Cloud Storage bucket. You want to follow Google-recommended practices and avoid writing any code for the migration. What should you do?
>
> **A.** Use gcloud storage for the video files, Dataflow for the data warehouse data, and Storage Transfer Service for the PNG files.
>
> **B.** Use Transfer Appliance for the videos, BigQuery Data Transfer Service for the data warehouse data, and Storage Transfer Service for the PNG files.
>
> **C.** Use Storage Transfer Service for the video files, BigQuery Data Transfer Service for the data warehouse data, and Storage Transfer Service for the PNG files.
>
> **D.** Use Cloud Data Fusion for the video files, Dataflow for the data warehouse data, and Storage Transfer Service for the PNG files.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are moving 200 TB of video files from SAN storage (on-premises disk storage), a data warehouse on Amazon Redshift, and 20 GB of PNG images from an Amazon S3 bucket.
- **What you must achieve:** Put the videos in one bucket, the warehouse data in BigQuery, and the PNGs in a second bucket.
- **The limits:** Follow recommended practice and write no code.
- **What they're really asking:** Which transfer tool fits each of the three data sets?

**Clues in the question:**
- "**200 TB … on-premises**" → **Transfer Appliance** (ship a physical device).
- "**Amazon Redshift**" → **BigQuery Data Transfer Service** (has a Redshift connector).
- "**S3 bucket**" → **Storage Transfer Service**.
- "**avoid writing any code**" → not Dataflow.

**Exam topic:** Migration.

---

## 📚 Key Terms Explained

### 1. Transfer Appliance 🔑
- **What it is:** A physical storage box Google ships to you; you load data and ship it back. For very large data (≈20 TB+) or slow links.
- **Looks like:** Order → copy 200 TB → ship
- **Not to be confused with:** online transfer.
- **Analogy:** 🚚 A moving truck.
- **In the online store:** Video archive.

### 2. BigQuery Data Transfer Service
- **What it is:** Managed, no-code loads into BigQuery from sources like Redshift, Teradata, S3, SaaS.
- **Looks like:** Transfer config: Amazon Redshift → dataset `dw`
- **Not to be confused with:** Dataflow.
- **Analogy:** 🔁 A scheduled delivery service for tables.
- **In the online store:** —

### 3. Storage Transfer Service
- **What it is:** Managed copying into Cloud Storage from S3, Azure, HTTP, other buckets (and on-prem with agents).
- **Looks like:** S3 → gs://pngs
- **Not to be confused with:** —
- **Analogy:** 📦 A courier for files.
- **In the online store:** —

### 🔗 How they fit together
```
 SAN 200 TB ─ Transfer Appliance ─► gs://videos ✅
 Redshift ─ BigQuery DTS ─► BigQuery ✅
 S3 20 GB ─ Storage Transfer Service ─► gs://pngs ✅
```

---

## 🌍 Real-World Scenario

A media company ships 200 TB of video on a **Transfer Appliance**, moves its Redshift warehouse with **BigQuery Data Transfer Service**, and copies S3 images with **Storage Transfer Service**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use gcloud storage for the video files, Dataflow for the data warehouse data, and Storage Transfer Service for the PNG files.

**Wrong words:**
- ❌ "**gcloud storage for the video files**": 200 TB over the network could take weeks.
- ❌ "**Dataflow for the data warehouse data**": requires writing pipelines.

📌 **When to use it:** Use gcloud storage for smaller uploads; Dataflow for custom processing.
🏢 **Office example:** Carrying 200 TB by hand, and hiring programmers to move tables.

### ✅ B
> **B.** Use Transfer Appliance for the videos, BigQuery Data Transfer Service for the data warehouse data, and Storage Transfer Service for the PNG files.

**Why it's correct:**
- ✔️ "**Transfer Appliance for the videos**" matches "**200 TB of video files in SAN storage**".
- ✔️ "**BigQuery Data Transfer Service for the data warehouse data**" matches "**Amazon Redshift**" → "**into BigQuery**".
- ✔️ "**Storage Transfer Service for the PNG files**" matches "**PNG files stored on an S3 bucket**"; all no-code, which matches "**avoid writing any code**".

📌 **When to use it:** Use it when each kind of data has a ready-made moving service and you don't want to write anything.
🏢 **Office example:** A moving truck for the huge archive, a table-delivery service for the ledgers, and a courier for the small box of photos.

### ❌ C
> **C.** Use Storage Transfer Service for the video files, BigQuery Data Transfer Service for the data warehouse data, and Storage Transfer Service for the PNG files.

**Wrong words:**
- ✔️ BigQuery DTS and STS for PNGs are right.
- ❌ "**Storage Transfer Service for the video files**": 200 TB on-prem is better suited to Transfer Appliance.

📌 **When to use it:** Use STS on-prem agents when your network is fast enough.
🏢 **Office example:** Sending a huge archive by courier van, trip after trip.

### ❌ D
> **D.** Use Cloud Data Fusion for the video files, Dataflow for the data warehouse data, and Storage Transfer Service for the PNG files.

**Wrong words:**
- ❌ "**Cloud Data Fusion for the video files**": a data-integration tool, not for bulk video files.
- ❌ "**Dataflow**": code.

📌 **When to use it:** Use Data Fusion for visual ETL pipelines.
🏢 **Office example:** Hiring a data analyst to move boxes.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow migration: product video archive → Transfer Appliance; Redshift sales DW → BigQuery DTS; S3 thumbnails → Storage Transfer Service.

---

## 🧠 Key Takeaways / Memory Tips

- **Huge on-prem → Transfer Appliance. Warehouse → BigQuery DTS. Other clouds' buckets → Storage Transfer Service.**
  🧠 *"**Truck, table service, courier.**"*
- Related: **Q230**, **Q216**.

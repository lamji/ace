# Q114: Combined Logs From All Projects for 60 Days, Quick Analysis (Sink to BigQuery + Table Expiration)

**Topic:** Logging (log sinks / exports, BigQuery, table expiration)

## ❓ Question
> You are managing several Google Cloud Platform (GCP) projects and need access to all logs for the past 60 days. You want to be able to explore and quickly analyze the log contents. You want to follow Google-recommended practices to obtain the combined logs for all projects. What should you do?
>
> **A.** Navigate to Stackdriver Logging and select resource.labels.project_id="*"
>
> **B.** Create a Stackdriver Logging Export with a Sink destination to a BigQuery dataset. Configure the table expiration to 60 days.
>
> **C.** Create a Stackdriver Logging Export with a Sink destination to Cloud Storage. Create a lifecycle rule to delete objects after 60 days.
>
> **D.** Configure a Cloud Scheduler job to read from Stackdriver and store the logs in BigQuery. Configure the table expiration to 60 days.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You manage several projects.
- **What you must achieve:** Get all logs from the last 60 days in one place to explore and analyze quickly.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** Where should the combined logs be sent?

**Clues in the question:**
- "**combined logs for all projects**": send each project's logs (or an aggregated org/folder sink) to **one destination**.
- "**explore and quickly analyze**": **BigQuery** lets you run SQL on logs.
- "**past 60 days**": BigQuery **table expiration = 60 days** deletes old data automatically.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Log sink / export 🔑 (review from Q061, Q068)
- **What it is:** A **rule that copies matching log entries to a destination** (BigQuery, Cloud Storage, Pub/Sub, a log bucket). It can be created per project or at **folder/org level** to collect all projects.
- **Looks like:** `gcloud logging sinks create all-logs bigquery.googleapis.com/projects/shopnow-ops/datasets/all_logs --organization=123 --include-children`
- **Not to be confused with:** Logs Explorer, which only views logs.
- **Analogy:** 📬 A **mail-forwarding rule**: copies of all mail go to one inbox.
- **In the online store:** All ShopNow projects' logs flow into `shopnow-ops`.

### 2. BigQuery table expiration
- **What it is:** A setting that **automatically deletes tables (or partitions) after N days**.
- **Looks like:** `bq update --default_table_expiration 5184000 shopnow-ops:all_logs`  (60 days in seconds)
- **Not to be confused with:** a Cloud Storage lifecycle rule.
- **Analogy:** 🗑️ "Shred reports older than 60 days".
- **In the online store:** Logs older than 60 days disappear automatically.

### 3. Cloud Storage for logs
- **What it is:** Cheap long-term storage of log **files**. Great for archives, but you can't run SQL directly on the files.
- **Looks like:** `gs://shopnow-logs/2026/11/03/...json`
- **Not to be confused with:** an analysis tool.
- **Analogy:** 📦 Boxes in the storage room.
- **In the online store:** 3-year audit log archive (Q061).

### 🔗 How they fit together
```
 project A ┐
 project B ├─ log sink(s) ─► BigQuery dataset all_logs (table expiration 60 days) ✅
 project C ┘                     └─ SQL: SELECT severity, COUNT(*) ... (quick analysis)
```

---

## 🌍 Real-World Scenario

An ops team runs 12 projects and wants one place to investigate incidents across all of them. They create an **aggregated log sink** at the folder level, sending to a **BigQuery** dataset with **60-day table expiration**. Investigations become SQL queries.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Navigate to Stackdriver Logging and select resource.labels.project_id="*"

**Wrong words:**
- ❌ "**select resource.labels.project_id="*"**": this isn't a real way to combine projects in Logs Explorer, and it doesn't store or analyze 60 days of logs together.

📌 **When to use it:** Use the Logs Explorer to look at one project's logs quickly.
🏢 **Office example:** Walking from office to office reading each logbook.

### ✅ B
> **B.** Create a Stackdriver Logging Export with a Sink destination to a BigQuery dataset. Configure the table expiration to 60 days.

**Why it's correct:**
- ✔️ "**Logging Export with a Sink destination to a BigQuery dataset**" matches "**obtain the combined logs for all projects**": all projects' logs land in one dataset.
- ✔️ "**BigQuery**" matches "**explore and quickly analyze the log contents**": you query the logs with SQL.
- ✔️ "**table expiration to 60 days**" matches "**logs for the past 60 days**": older data is removed automatically.

📌 **When to use it:** Use it when you want copies of everyone's records in one place where you can search and count them quickly.
🏢 **Office example:** Forwarding every branch's logbook to head office's searchable records system, shredded after 60 days.

### ❌ C
> **C.** Create a Stackdriver Logging Export with a Sink destination to Cloud Storage. Create a lifecycle rule to delete objects after 60 days.

**Wrong words:**
- ✔️ "Sink" and "delete objects after 60 days" handle collection and retention.
- ❌ "**Sink destination to Cloud Storage**": files in a bucket can't be explored and analyzed quickly with SQL.

📌 **When to use it:** Use Cloud Storage sinks for cheap long-term archives.
🏢 **Office example:** Boxing all the logbooks in the storage room: kept, but hard to search.

### ❌ D
> **D.** Configure a Cloud Scheduler job to read from Stackdriver and store the logs in BigQuery. Configure the table expiration to 60 days.

**Wrong words:**
- ❌ "**Configure a Cloud Scheduler job to read from Stackdriver**": a homemade copy job instead of a built-in sink. More work, and it can miss logs.

📌 **When to use it:** **Never use this** when a log sink can do it.
🏢 **Office example:** Sending an intern every hour to copy logbooks by hand.

---

## 🛒 E-Commerce Full-Stack Example

```bash
bq mk --dataset --default_table_expiration 5184000 shopnow-ops:all_logs
gcloud logging sinks create shopnow-all bigquery.googleapis.com/projects/shopnow-ops/datasets/all_logs \
  --folder=RETAIL_FOLDER_ID --include-children --use-partitioned-tables
```
```sql
SELECT resource.labels.project_id, COUNT(*) AS errors
FROM `shopnow-ops.all_logs.*` WHERE severity='ERROR' GROUP BY 1;
```

---

## 🧠 Key Takeaways / Memory Tips

- **Combine and analyze logs → sink to BigQuery.** Keep N days → table expiration.
- Cloud Storage sink = archive, not quick analysis.
  🧠 *"**Analyze logs? Sink to BigQuery.**"*
- Related: **Q068** (sink to BigQuery), **Q061** (sink to Coldline), **Q086** (audit log categories).

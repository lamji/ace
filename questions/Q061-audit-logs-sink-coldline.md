# Q061: Keeping Audit Logs for 3 Years Cheaply (Log Sink → Coldline Bucket)

**Topic:** Cloud Logging + Cloud Storage (log sinks / exports, aggregated org sink, Coldline vs BigQuery vs Cloud SQL, log retention)

## ❓ Question
> Your organization is a financial company that needs to store audit log files for 3 years. Your organization has hundreds of Google Cloud projects. You need to implement a cost-effective approach for log file retention. What should you do?
>
> **A.** Create an export to the sink that saves logs from Cloud Audit to BigQuery.
>
> **B.** Create an export to the sink that saves logs from Cloud Audit to a Coldline Storage bucket.
>
> **C.** Write a custom script that uses logging API to copy the logs from Stackdriver logs to BigQuery.
>
> **D.** Export these logs to Cloud Pub/Sub and write a Cloud Dataflow pipeline to store logs to Cloud SQL.

**My answer:** — (didn't know; asked "why B?")
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** A bank-like company must **keep audit logs for 3 years** (rules require it), across **hundreds of projects**. Nobody will read them unless an auditor or investigator asks. What's the **cheapest** way to keep them?

| Question words | What they point to |
|---|---|
| "**store audit log files for 3 years**" | Long-term **storage**, rarely opened → cold storage class |
| "**financial company**" | Kept for **compliance/audits**, not daily analysis |
| "**hundreds of Google Cloud projects**" | Use a built-in **sink** (one at the organization level covers all projects), not custom scripts |
| "**cost-effective**" | **Coldline** bucket: very cheap per GB for data opened rarely |
| "**log file retention**" | Just **keep** the files; no querying requirement |

**Exam topic:** Cloud Logging + Cloud Storage.

---

## 📚 Key Terms Explained

### 1️⃣ Audit logs (Cloud Audit Logs)
- **What it is:** Records of **who did what, where and when** in Google Cloud (e.g., "ana@ changed a firewall rule at 10:02").
- **Looks like:** `protoPayload.methodName: "v1.compute.firewalls.patch"  principalEmail: "ana@shopnow.com"`
- **Not to be confused with:** app logs (your code's output). Audit logs track **people and admin actions**.
- **Analogy:** 📒 The **visitor sign-in book** at the front desk.
- **In the online store:** Proof of who changed the payment service's settings.

### 2️⃣ Log sink (export) 🔑
- **What it is:** A **rule in Cloud Logging** that **automatically copies matching logs** to a destination: a Cloud Storage bucket, BigQuery, Pub/Sub, or another log bucket. An **aggregated sink** at the **organization** level covers **all projects** at once.
- **Looks like:**
  ```bash
  gcloud logging sinks create audit-archive \
    storage.googleapis.com/shopnow-audit-archive \
    --organization=123456789 --include-children \
    --log-filter='logName:"cloudaudit.googleapis.com"'
  ```
- **Not to be confused with:** a script you write. A sink is built in and runs automatically, forever.
- **Analogy:** 📮 A **standing order to the mailroom**: "Send a copy of every sign-in page to the archive warehouse."
- **In the online store:** Every project's audit logs flow into one archive bucket.

### 3️⃣ Coldline Storage (review from Q006)
- **What it is:** A Cloud Storage **class** for files you open **about once a year or less**. Very cheap to store; you pay a bit more when you read them. Minimum storage time: 90 days.
- **Looks like:** `gsutil mb -c coldline -l us gs://shopnow-audit-archive`
- **Not to be confused with:** Nearline (opened ~once a month) or Archive (even cheaper, opened less than once a year).
- **Analogy:** 📦 Boxes in the **storage room**, opened only when auditors come.
- **In the online store:** 3 years of audit logs, opened only during an audit.

### 4️⃣ BigQuery
- **What it is:** A **data warehouse** for running **SQL analysis** on huge data. It costs more to store than Coldline and is built for frequent querying.
- **Not to be confused with:** cheap long-term storage. It's for **analyzing**, not just keeping.
- **Analogy:** 📊 An **analyst's desk** with every report open for crunching numbers.

### 5️⃣ Pub/Sub + Dataflow + Cloud SQL
- **What it is:** Pub/Sub = message queue, Dataflow = data-processing pipeline, Cloud SQL = relational database. Together: a **custom pipeline** that you build and run.
- **Not to be confused with:** a storage solution. Cloud SQL isn't designed for 3 years of logs from hundreds of projects; it's expensive and has size limits.
- **Analogy:** 🏭 Building a **conveyor belt and a custom filing cabinet** just to store sign-in books.

### 🔗 How they fit together
```
 Hundreds of projects ──► Cloud Logging
                             │  aggregated org sink (filter: audit logs)
                             ▼
                    🪣 Coldline bucket  ← cheap, kept 3 years ✅
                       (+ retention policy / lifecycle rule to delete after 3 years)
```

---

## 🌍 Real-World Scenario

Financial regulators require companies to keep audit records for years. Cloud Logging's default log buckets keep most logs for only **30 days** (Admin Activity audit logs: 400 days), so you must **export** them. The standard pattern: one **organization-level sink** sends all audit logs into a **Coldline** (or Archive) bucket, optionally with a **bucket retention policy** so nobody can delete them early. It costs very little, and the logs are there if an auditor asks.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an export to the sink that saves logs from Cloud Audit to BigQuery.

**Wrong words:**
- ✔️ "Create an export to the sink that saves logs from Cloud Audit" is the right method (built-in sink).
- ❌ "**to BigQuery**": BigQuery is for **analyzing** data with SQL, and storing 3 years of logs there costs more than Coldline. The question asks for **cost-effective retention**, not analysis.

📌 **When to use it:** Use it when you need to search and analyze logs often with SQL (security investigations, reports).
🏢 **Office example:** Keeping every sign-in book on an analyst's desk so they can count visitors every week.

### ✅ B
> **B.** Create an export to the sink that saves logs from Cloud Audit to a Coldline Storage bucket.

**Why it's correct:**

- ✔️ "**Create an export to the sink**" matches "**hundreds of Google Cloud projects**": A built-in sink copies logs automatically. One aggregated sink at the org level covers all projects. No code.
- ✔️ "**saves logs from Cloud Audit**" matches "**store audit log files**": Exactly the logs the company must keep.
- ✔️ "**Coldline Storage bucket**" matches "**cost-effective**", "**for 3 years**", "**log file retention**": Very cheap storage for files that are kept long and opened rarely (only during audits).

📌 **When to use it:** Use it when you must keep records for years and only open them if someone asks.
🏢 **Office example:** Sending a copy of every sign-in book to the storage room, opened only when auditors come.

### ❌ C
> **C.** Write a custom script that uses logging API to copy the logs from Stackdriver logs to BigQuery.

**Wrong words:**
- ❌ "**Write a custom script**": you must build, run and fix it yourself for **hundreds of projects**, when a sink does it automatically.
- ❌ "**to BigQuery**": more expensive than Coldline for just keeping files (same problem as A).

📌 **When to use it:** **Never use this.** A sink does the copying for you. Use B.
🏢 **Office example:** Hiring someone to photocopy every sign-in book by hand, when the mailroom already sends copies automatically.

### ❌ D
> **D.** Export these logs to Cloud Pub/Sub and write a Cloud Dataflow pipeline to store logs to Cloud SQL.

**Wrong words:**
- ❌ "**Cloud Pub/Sub and write a Cloud Dataflow pipeline**": a streaming pipeline is for **real-time processing**. Here it's extra services to build and pay for, just to store files.
- ❌ "**store logs to Cloud SQL**": a database is expensive per GB and has size limits. It's the wrong place for 3 years of logs from hundreds of projects.

📌 **When to use it:** Use Pub/Sub + Dataflow when logs must be processed in real time, like sending them to an outside security tool.
🏢 **Office example:** Building a conveyor belt and a custom filing cabinet just to store old sign-in books.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow (now handling payments) has 200 projects and must keep audit logs for 3 years.

```bash
# 1. Cheap bucket, locked for 3 years
gsutil mb -c coldline -l us gs://shopnow-audit-archive
gsutil retention set 3y gs://shopnow-audit-archive

# 2. One sink for the whole organization
gcloud logging sinks create audit-archive \
  storage.googleapis.com/shopnow-audit-archive \
  --organization=123456789 --include-children \
  --log-filter='logName:"cloudaudit.googleapis.com"'

# 3. Let the sink's service account write to the bucket (the command above prints it)
gsutil iam ch serviceAccount:<sink-writer-identity>:objectCreator gs://shopnow-audit-archive
```

| Destination | Good for | Cost for 3 years of keeping |
|---|---|---|
| **Coldline bucket** | Keeping, rarely opened | 💲 low ✅ |
| BigQuery | Frequent SQL analysis | 💲💲 higher |
| Cloud SQL | App data (orders, users) | 💲💲💲 and size limits |

---

## 🧠 Key Takeaways / Memory Tips

- **"Keep logs for years" + "cost-effective" → log sink → Coldline (or Archive) bucket.**
- **"Analyze logs with SQL" → sink → BigQuery.** **"Real-time processing" → sink → Pub/Sub.**
- **Many projects → one aggregated sink at the org/folder level**, never custom scripts.
  🧠 *"**Keep = Storage. Query = BigQuery. Stream = Pub/Sub.**"*
- Related: **Q006** (storage classes), **Q027** (audit logs in Cloud Logging), **Q017** (export to BigQuery for analysis).

# Q068: Sending All Compute Engine Logs to BigQuery Cheaply (Filtered Log Sink)

**Topic:** Cloud Logging (log sinks / exports with filters, BigQuery as sink destination, sink writer identity) vs custom pipelines

## ❓ Question
> For analysis purposes, you need to send all the logs from all of your Compute Engine instances to a BigQuery dataset called platform-logs. You have already installed the Cloud Logging agent on all the instances. You want to minimize cost. What should you do?
>
> **A.** 1. Give the BigQuery Data Editor role on the platform-logs dataset to the service accounts used by your instances. 2. Update your instances' metadata to add the following value: logs-destination: bq://platform-logs.
>
> **B.** 1. In Cloud Logging, create a logs export with a Cloud Pub/Sub topic called logs as a sink. 2. Create a Cloud Function that is triggered by messages in the logs topic. 3. Configure that Cloud Function to drop logs that are not from Compute Engine and to insert Compute Engine logs in the platform-logs dataset.
>
> **C.** 1. In Cloud Logging, create a filter to view only Compute Engine logs. 2. Click Create Export. 3. Choose BigQuery as Sink Service, and the platform-logs dataset as Sink Destination.
>
> **D.** 1. Create a Cloud Function that has the BigQuery User role on the platform-logs dataset. 2. Configure this Cloud Function to create a BigQuery Job that executes this query: INSERT INTO dataset.platform-logs (timestamp, log) SELECT timestamp, log FROM compute.logs WHERE timestamp > DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) 3. Use Cloud Scheduler to trigger this Cloud Function once a day.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Every VM already has the Cloud Logging agent installed (a program that sends logs to Google).
- **What you must achieve:** Send all VM logs to a BigQuery dataset named platform-logs.
- **The limits:** Keep costs low.
- **What they're really asking:** How do you route the logs into BigQuery?

**Clues in the question:**
- "**For analysis purposes**" + "**BigQuery dataset**": the destination is BigQuery (a sink can send there directly).
- "**all the logs from all of your Compute Engine instances**": you need a **filter** that keeps only Compute Engine logs.
- "**already installed the Cloud Logging agent**": the logs are **already in Cloud Logging**, so you just route them onward.
- "**minimize cost**": use the **built-in sink** (no charge for routing), not extra Pub/Sub topics, Cloud Functions or schedulers.

**Exam topic:** Cloud Logging.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Logging agent
- **What it is:** A small program installed on each VM that **sends the VM's logs** (system logs, app logs) to Cloud Logging. Today it's part of the **Ops Agent**.
- **Looks like:** `sudo systemctl status google-cloud-ops-agent` → active (running)
- **Not to be confused with:** a sink. The agent gets logs **into** Cloud Logging; a sink sends them **out** to somewhere else.
- **Analogy:** 📮 Each office's **outbox** that sends its paperwork to the central mailroom.
- **In the online store:** Every web server's Nginx and app logs land in Cloud Logging.

### 2️⃣ Log sink (export) 🔑 (review from Q061)
- **What it is:** A **rule in Cloud Logging** with a **filter** and a **destination**. Every new log entry that matches the filter is **automatically copied** to the destination (BigQuery, Cloud Storage, Pub/Sub, or a log bucket).
- **Looks like:**
  ```bash
  gcloud logging sinks create gce-to-bq \
    bigquery.googleapis.com/projects/shopnow-prod/datasets/platform_logs \
    --log-filter='resource.type="gce_instance"'
  ```
- **Not to be confused with:** a script or function you write. A sink is built in and needs no code.
- **Analogy:** 📮 A **standing order to the mailroom**: "Send a copy of every letter from the branch offices to the analysis team."
- **In the online store:** Every Compute Engine log goes straight into BigQuery for reports.

### 3️⃣ Log filter
- **What it is:** A query that selects which logs you want, for example only logs from Compute Engine VMs.
- **Looks like:** `resource.type="gce_instance"`
- **Not to be confused with:** deleting logs. The filter only chooses what the sink copies.
- **Analogy:** 🔎 "Only letters **stamped 'Branch Office'**."

### 4️⃣ BigQuery dataset
- **What it is:** A **folder of tables** in BigQuery where you run SQL analysis. A sink to BigQuery creates tables in it automatically.
- **Looks like:** `shopnow-prod:platform_logs.syslog_20261030`
- **Not to be confused with:** a bucket. A dataset holds **tables** you query with SQL.
- **Analogy:** 📊 The **analysis team's binder of spreadsheets**.
- **In the online store:** `SELECT COUNT(*) ... WHERE severity="ERROR"` per web server.

### 5️⃣ Pub/Sub + Cloud Function (custom pipeline)
- **What it is:** Pub/Sub carries messages; a Cloud Function is a small piece of code that runs on each message. Together they make a **custom pipeline** you build and pay for.
- **Not to be confused with:** a sink to BigQuery, which does the same delivery **without code**.
- **Analogy:** 🏭 Hiring a courier and a sorter to deliver mail the mailroom already delivers for free.

### 🔗 How they fit together
```
 🖥️ VMs + Logging agent ──► 📜 Cloud Logging
                               │ sink: filter resource.type="gce_instance"
                               ▼
                         📊 BigQuery: platform-logs  ✅ no code, no extra services
```

---

## 🌍 Real-World Scenario

Ops teams want to answer questions like "which servers threw the most errors last week?" with SQL. The logs are already in Cloud Logging, so the engineer creates a **sink** with a filter for Compute Engine logs and BigQuery as the destination. From then on, every new log is streamed into BigQuery automatically, and analysts query it like any other table.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Give the BigQuery Data Editor role on the platform-logs dataset to the service accounts used by your instances. 2. Update your instances' metadata to add the following value: logs-destination: bq://platform-logs.

**Wrong words:**
- ❌ "**Update your instances' metadata to add the following value: logs-destination: bq://platform-logs**": there's **no such setting**. Metadata like this doesn't send logs anywhere; this option is made up.
- ❌ "**Give the BigQuery Data Editor role … to the service accounts used by your instances**": gives every VM write access to the dataset, which isn't needed, since Cloud Logging (not the VMs) does the exporting.

📌 **When to use it:** **Never use this.** That metadata key doesn't exist. Use a log sink (C).
🏢 **Office example:** Writing "send copies to Analysis" on each desk's sticky note and hoping the mailroom notices.

### ❌ B
> **B.** 1. In Cloud Logging, create a logs export with a Cloud Pub/Sub topic called logs as a sink. 2. Create a Cloud Function that is triggered by messages in the logs topic. 3. Configure that Cloud Function to drop logs that are not from Compute Engine and to insert Compute Engine logs in the platform-logs dataset.

**Wrong words:**
- ✔️ "In Cloud Logging, create a logs export … as a sink" is the right idea.
- ❌ "**with a Cloud Pub/Sub topic called logs**": an extra hop. A sink can send **straight to BigQuery**.
- ❌ "**Create a Cloud Function that is triggered by messages**": you pay for a function call **on every single log**. That's expensive and the opposite of "minimize cost".
- ❌ "**drop logs that are not from Compute Engine**": filtering in code, when a sink filter does it for free.

📌 **When to use it:** Use Pub/Sub + a function when logs must be changed or sent to a tool that a sink can't reach directly.
🏢 **Office example:** Hiring a courier and a sorter to deliver mail that the mailroom would deliver directly for free.

### ✅ C (your answer)
> **C.** 1. In Cloud Logging, create a filter to view only Compute Engine logs. 2. Click Create Export. 3. Choose BigQuery as Sink Service, and the platform-logs dataset as Sink Destination.

**Why it's correct:**
- ✔️ "**create a filter to view only Compute Engine logs**" matches "**all the logs from all of your Compute Engine instances**": the filter keeps exactly the Compute Engine logs and nothing else.
- ✔️ "**Choose BigQuery as Sink Service, and the platform-logs dataset as Sink Destination**" matches "**to a BigQuery dataset called platform-logs**": the sink delivers straight into that dataset.
- ✔️ "**Click Create Export**" (a built-in sink) matches "**minimize cost**": no Pub/Sub, no functions, no scheduler. Cloud Logging routes the logs with no extra services to pay for.
- ✔️ "**In Cloud Logging**" matches "**already installed the Cloud Logging agent**": the logs are already there, so you just route them.

📌 **When to use it:** Use it when you want certain logs copied automatically into BigQuery to analyze them.
🏢 **Office example:** Telling the mailroom once: "Send a copy of every branch-office letter to the analysis team."

### ❌ D
> **D.** 1. Create a Cloud Function that has the BigQuery User role on the platform-logs dataset. 2. Configure this Cloud Function to create a BigQuery Job that executes this query: INSERT INTO dataset.platform-logs (timestamp, log) SELECT timestamp, log FROM compute.logs WHERE timestamp > DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY) 3. Use Cloud Scheduler to trigger this Cloud Function once a day.

**Wrong words:**
- ❌ "**SELECT timestamp, log FROM compute.logs**": there's **no BigQuery table called `compute.logs`**. The logs live in Cloud Logging, not in BigQuery, so this query has nothing to read.
- ❌ "**Create a Cloud Function**" + "**Use Cloud Scheduler … once a day**": extra services to build and pay for, and the logs only arrive once a day.

📌 **When to use it:** Use a scheduled function + query when you need to copy or summarize data that's **already in BigQuery** on a schedule.
🏢 **Office example:** Each morning, copying yesterday's pages from a binder that doesn't exist.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's web servers (Compute Engine) already send logs via the Ops Agent. The ops team wants error reports in BigQuery.

```bash
# 1. One sink, filtered to Compute Engine, straight to BigQuery
gcloud logging sinks create gce-to-bq \
  bigquery.googleapis.com/projects/shopnow-prod/datasets/platform_logs \
  --log-filter='resource.type="gce_instance"'

# 2. Let the sink's writer identity (printed above) write to the dataset
#    → grant it BigQuery Data Editor on platform_logs
```

Then the analysts run:
```sql
SELECT resource.labels.instance_id, COUNT(*) AS errors
FROM `shopnow-prod.platform_logs.*`
WHERE severity = "ERROR"
GROUP BY 1 ORDER BY errors DESC;
```

*(Note: BigQuery dataset names can't contain hyphens, so in real life it would be `platform_logs`.)*

---

## 🧠 Key Takeaways / Memory Tips

- **Logs → BigQuery (or Storage, Pub/Sub) = a log sink with a filter.** No code needed.
- **Filter in the sink, not in a Cloud Function.** Cheaper and simpler.
- **Watch for made-up settings** (like `logs-destination` metadata) and tables that don't exist (`compute.logs`).
  🧠 *"**Filter + sink = logs delivered. No functions, no schedulers.**"*
- Related: **Q061** (sink → Coldline for cheap retention), **Q055** (exclude noisy logs), **Q017** (billing export to BigQuery).

# G047: Run a Standard SQL Query Against BigQuery From the Command Line (bq query --use_legacy_sql=false)

**Topic:** BigQuery (executing queries)
**Exam guide section:** 3.2 Managing storage and data solutions: Executing queries to retrieve data from data instances (BigQuery)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You need to run a GoogleSQL query against the BigQuery table shop.orders from a shell script to count today's orders. What should you do?
>
> **A.** Run gcloud sql connect, and then type the query.
>
> **B.** Run bq query --use_legacy_sql=false with the SQL statement.
>
> **C.** Run gsutil cat on the table.
>
> **D.** Run kubectl exec into a BigQuery Pod.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You want a shell script (a file of terminal commands) to run a query in BigQuery (Google's data warehouse) on the table `shop.orders`.
- **What you must achieve:** Count today's orders using a GoogleSQL query (BigQuery's standard SQL dialect).
- **The limits:** It must run from the command line.
- **What they're really asking:** Which command-line tool and command run a BigQuery query?

**Clues in the question:**
- "**BigQuery**" + "**from a shell script**": the **bq** command-line tool.
- "**GoogleSQL**": add `--use_legacy_sql=false` (or put `#standardSQL` in the query).

**Exam topic:** Data querying (exam guide section 3.2).

---

## 📚 Key Terms Explained

### 1. bq CLI 🔑
- **What it is:** BigQuery's command-line tool (part of the Google Cloud CLI) for queries, loads, datasets and jobs.
- **Looks like:** `bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM shop.orders WHERE DATE(created_at)=CURRENT_DATE()'`
- **Not to be confused with:** `gcloud sql`, which is for Cloud SQL instances.
- **Analogy:** ⌨️ A direct phone line to the data warehouse.
- **In the online store:** Nightly count script.

### 2. GoogleSQL (standard SQL)
- **What it is:** BigQuery's ANSI-compatible SQL dialect. Legacy SQL is the old dialect.
- **Looks like:** `` `project.dataset.table` `` naming, `CURRENT_DATE()`
- **Not to be confused with:** Legacy SQL (`[project:dataset.table]`).
- **Analogy:** 📘 The modern rulebook vs the old one.
- **In the online store:** All ShopNow queries.

### 🔗 How they fit together
```
 script.sh ─► bq query --use_legacy_sql=false 'SELECT COUNT(*) …' ─► BigQuery ─► result ✅
```

---

## 🌍 Real-World Scenario

A nightly cron job posts the day's order count to Slack. It calls `bq query --use_legacy_sql=false` and parses the output.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Run gcloud sql connect, and then type the query.

**Wrong words:**
- ❌ "**gcloud sql connect**": connects to Cloud SQL databases, not BigQuery.

📌 **When to use it:** Use it to open a SQL shell to a Cloud SQL instance.
🏢 **Office example:** Calling the wrong department.

### ✅ B
> **B.** Run bq query --use_legacy_sql=false with the SQL statement.

**Why it's correct:**
- ✔️ "**bq query**" matches "**run a … query against the BigQuery table … from a shell script**".
- ✔️ "**--use_legacy_sql=false**" matches "**GoogleSQL query**".

📌 **When to use it:** Use it when a script needs to ask the data warehouse a question.
🏢 **Office example:** Calling the warehouse's direct line with a clear question.

### ❌ C
> **C.** Run gsutil cat on the table.

**Wrong words:**
- ❌ "**gsutil cat**": prints Cloud Storage objects. BigQuery tables aren't files in a bucket.

📌 **When to use it:** Use it to view a file stored in Cloud Storage.
🏢 **Office example:** Reading a file in the storeroom to answer a warehouse question.

### ❌ D
> **D.** Run kubectl exec into a BigQuery Pod.

**Wrong words:**
- ❌ "**kubectl exec into a BigQuery Pod**": BigQuery is serverless. There are no Pods of yours to enter.

📌 **When to use it:** Use kubectl exec to debug your own containers in GKE.
🏢 **Office example:** Knocking on a door that doesn't exist.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** cron: `bq query --use_legacy_sql=false --format=csv 'SELECT COUNT(*) FROM shop.orders WHERE DATE(created_at)=CURRENT_DATE()'` → post to Slack.

---

## 🧠 Key Takeaways / Memory Tips

- **BigQuery from the CLI → `bq query --use_legacy_sql=false`.** Cloud SQL → `gcloud sql connect`.
  🧠 *"**bq for BigQuery.**"*
- Related: **Q015**, **Q085**, **Q146**.

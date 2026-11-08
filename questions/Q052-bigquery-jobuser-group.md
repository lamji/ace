# Q052: Letting a Changing Data Science Team Run BigQuery Queries (Group + jobUser)

**Topic:** IAM + BigQuery (Google groups in Cloud Identity, `roles/bigquery.jobUser` vs `roles/bigquery.dataViewer`)

## ❓ Question
> Your company has a Google Cloud Platform project that uses BigQuery for data warehousing. Your data science team changes frequently and has few members. You need to allow members of this team to perform queries. You want to follow Google-recommended practices. What should you do?
>
> **A.** 1. Create an IAM entry for each data scientist's user account. 2. Assign the BigQuery jobUser role to the group.
>
> **B.** 1. Create an IAM entry for each data scientist's user account. 2. Assign the BigQuery dataViewer user role to the group.
>
> **C.** 1. Create a dedicated Google group in Cloud Identity. 2. Add each data scientist's user account to the group. 3. Assign the BigQuery jobUser role to the group.
>
> **D.** 1. Create a dedicated Google group in Cloud Identity. 2. Add each data scientist's user account to the group. 3. Assign the BigQuery dataViewer user role to the group.

**My answer:** D
**Correct answer:** C
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** BigQuery is used as the company data warehouse. The data science team is small and its members change often.
- **What you must achieve:** Let team members run queries.
- **The limits:** Follow Google's recommended practice, keeping in mind people join and leave often.
- **What they're really asking:** How should you grant query access so it stays easy to manage as people come and go?

The question tests **two choices at once**, just like Q025:

| Choice | Options | Google's answer |
|---|---|---|
| **Who** gets the role? | Individual users (A, B) vs **group** (C, D) | ✅ **Group** |
| **Which** role? | **jobUser** (A, C) vs **dataViewer** (B, D) | ✅ **jobUser**, because the task is "**perform queries**" |

**Group + jobUser = C.**

| Keyword | What it hints at |
|---|---|
| "**changes frequently**" | Use a **group**, so membership changes don't touch IAM |
| "**perform queries**" | A query in BigQuery is a **job**. Running jobs needs **`bigquery.jobs.create`**, which is in **jobUser**, not dataViewer |
| "**Google-recommended practices**" | Groups over individual users. Least privilege |

**Exam topic:** IAM / BigQuery access.

> 🎯 **The one-sentence answer to "why C and not D?":** Both use a group, so the difference is only the role. **dataViewer** lets you **see** datasets and tables, but it **doesn't let you run a query**. Every BigQuery query is a **job**, and only a role with `bigquery.jobs.create` (like **jobUser**) can start one.

---

## 📚 Key Terms Explained

### 1️⃣ BigQuery Job 🔑
- **What it is:** **Any piece of work** BigQuery runs for you: a **query**, a data load, an export, a copy. When you click **Run** on a query, BigQuery creates a **query job** and **bills the project** for it.
- **Looks like:**
  ```
  Job ID: shopnow-analytics:US.bquxjob_5f2a91c
  Type: QUERY · User: ana@shopnow.com · Bytes processed: 1.2 GB · Status: DONE
  ```
- **Not to be confused with:** **reading** a table's details. Opening a table's schema or preview isn't a query job.
- **Analogy:** 🧾 A **work order** sent to the records department ("pull all orders from March and total them"). You need permission to **submit work orders**.
- **In the online store:** `SELECT SUM(total) FROM orders WHERE month='2026-10'` is a query job.

### 2️⃣ `roles/bigquery.jobUser` (BigQuery Job User) ✅
- **What it is:** Lets a user **create and run jobs** (including queries) **in the project**, and see/cancel their own jobs. It does **not** by itself give access to any dataset's data.
- **Looks like:** permission `bigquery.jobs.create`
- **Not to be confused with:** dataViewer. jobUser = "**may submit work orders**". It's the role named after the action "perform queries".
- **Analogy:** 🎫 Permission to **use the records department's copy machine and calculators**.

### 3️⃣ `roles/bigquery.dataViewer` (BigQuery Data Viewer)
- **What it is:** **Read-only access** to datasets and tables: list them, see schemas, **preview rows**, read table data. It **doesn't include `bigquery.jobs.create`**, so you **can't run a query** with it alone.
- **Looks like:** permissions `bigquery.tables.get`, `bigquery.tables.getData`, … (no `jobs.create`)
- **Not to be confused with:** "can query". Viewing a table ≠ running SQL on it.
- **Analogy:** 👀 Permission to **walk into the records room and look at the files**, but not to submit work orders.

### 4️⃣ Google Group in Cloud Identity (review from Q001, Q025)
- **What it is:** A **named list of email addresses**. Give a role **to the group**, and everyone on the list gets it. **Cloud Identity** is Google's service for managing users and groups (like Google Workspace without Gmail and Docs).
- **Looks like:** `data-science@shopnow.com = [ana@shopnow.com, raj@shopnow.com, mei@shopnow.com]`
- **Not to be confused with:** a shared account. Nobody logs in as the group. Each person uses their **own** account.
- **Analogy:** 👥 The **"Data Science Team" list at the front desk**. Each person uses their own ID card.

### 5️⃣ "IAM entry for each user account" (options A and B)
- **What it is:** Granting roles **person by person** in IAM.
- **Not to be confused with:** the group method. Note that A and B then say "assign the role **to the group**", but **no group was ever created**. Those options contradict themselves.

### 🔗 How They Fit Together
```
👥 data-science@shopnow.com  (Cloud Identity group)
     ├── ana@shopnow.com
     ├── raj@shopnow.com
     └── mei@shopnow.com
            │  roles granted ONCE, to the group
            ▼
🎫 roles/bigquery.jobUser    → may RUN queries (create jobs)   ✅ what the question asks
👀 roles/bigquery.dataViewer → may READ tables' data            (real life: usually given too)

  Run a query = jobs.create (jobUser)  +  read the tables it touches (dataViewer)
```

> ⚠️ **Honest note (real life):** To query a table **successfully**, a user needs **both**: permission to **run the job** (`jobUser`) **and** permission to **read the data** (`dataViewer`, often granted on specific datasets). The exam only asks about "**perform queries**", which points at the missing piece: **jobUser**. Think of it as: "dataViewer alone can never run a query. jobUser is the role *named* for querying."

---

## 🌍 Real-World Scenario

Data scientists come and go: interns, contractors, people moving teams. If you grant roles to each person, you'll forget to remove someone who left (a security finding), and every new joiner means an IAM change. The standard setup is a **group per team**: grant **jobUser** (to run queries, often on the project) plus **dataViewer** (on the datasets they may read) **to the group once**, and from then on HR or the team lead **only edits the group membership**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Create an IAM entry for each data scientist's user account. 2. Assign the BigQuery jobUser role to the group.

**Why it's wrong:**
- ✔️ jobUser is the right role…
- ❌ …but granting **per user** goes against "team changes frequently". Every change means editing IAM.
- ❌ It says "assign to **the group**", but no group was created. The steps don't fit together.

**📌 When to use it:** Grant roles to individual users only for a one-off person with temporary access.
🏢 **Office example:** Writing one visitor's name on the records-room door for a single day.

### ❌ B
> **B.** 1. Create an IAM entry for each data scientist's user account. 2. Assign the BigQuery dataViewer user role to the group.

**Why it's wrong:**
- ❌ **Both choices are wrong**: individual users instead of a group, and dataViewer can't run queries.
- ❌ It has the same "which group?" contradiction as A.

**📌 When to use it:** **Never use this** for a changing team. Use a group with the role that matches the task (C).
🏢 **Office example:** Writing each new analyst's name on the door, and they still can't submit work orders.

### ✅ C
> **C.** 1. Create a dedicated Google group in Cloud Identity. 2. Add each data scientist's user account to the group. 3. Assign the BigQuery jobUser role to the group.

**Why it's correct:**
- ✔️ **Group**: team changes = edit the group, with no IAM changes. Google-recommended.
- ✔️ **jobUser**: grants `bigquery.jobs.create`, the permission to **run queries**, exactly what "perform queries" needs.
- ✔️ Least privilege: it doesn't give admin or edit rights.

**📌 When to use it:** Use it when a team whose members change needs to run reports on the company's data.
🏢 **Office example:** Giving the "Data Science Team" list permission to submit work orders to the records department. HR just updates the list.

### ❌ D (your answer)
> **D.** 1. Create a dedicated Google group in Cloud Identity. 2. Add each data scientist's user account to the group. 3. Assign the BigQuery dataViewer user role to the group.

**Why it's wrong:**
- ✔️ The **group** part is perfect…
- ❌ …but **dataViewer can't run queries**. It has no `bigquery.jobs.create`. The team could **look** at tables and preview rows, but clicking **Run** would fail with *"User does not have bigquery.jobs.create permission in project …"*.
- 💡 **Likely mix-up:** In Q025, auditors got **dataViewer**, because they needed to **view** data. Here the task word is "**perform queries**", which means running **jobs**, so the role is **jobUser**. **Match the role to the verb.**

**📌 When to use it:** Use dataViewer when people only need to look at tables and their contents, not run their own queries.
🏢 **Office example:** Letting the team walk into the records room and read files, without permission to submit work orders.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's analytics live in BigQuery in **`shopnow-analytics`**. The data science team (`data-science@shopnow.com`) needs to run queries like "revenue per product this month".

```bash
# Run queries in the project (the answer to this question)
gcloud projects add-iam-policy-binding shopnow-analytics \
  --member="group:data-science@shopnow.com" \
  --role="roles/bigquery.jobUser"

# Real life: also let them READ the sales dataset the queries touch
bq add-iam-policy-binding \
  --member="group:data-science@shopnow.com" \
  --role="roles/bigquery.dataViewer" \
  shopnow-analytics:sales
```

**What Ana sees with each setup when she runs `SELECT product, SUM(total) FROM sales.orders GROUP BY product`:**
| Setup | Result |
|---|---|
| **dataViewer only (D)** | ❌ *"Access Denied: User does not have bigquery.jobs.create permission in project shopnow-analytics."* |
| **jobUser** (C) + read access to `sales` | ✅ Results in 3 seconds |

**Next month:** Raj leaves, and Lea joins. The admin edits `data-science@shopnow.com` only. **IAM stays untouched.** ✅

---

## 🧠 Key Takeaways / Memory Tips

- **"Team changes frequently" → Google group.** (Same as Q001, Q025.)
- **"Perform queries / run queries" → `bigquery.jobUser`.** A query is a **job**.
  🧠 *"**Viewer views, JobUser runs.**"*
- **dataViewer** = read tables, **can't run queries** alone. **jobUser** = run jobs, no data access by itself. Real-life querying needs **both**.
- **Match the role to the verb** in the question: "view/audit data" → dataViewer (Q025). "Perform queries" → jobUser.
- Related: **Q025** (auditors: group + logging.viewer + dataViewer), **Q015** (BigQuery dry run shows bytes a query job would read).

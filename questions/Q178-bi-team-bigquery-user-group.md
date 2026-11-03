# Q178: BI Team Runs Custom SQL on the Latest Data (BigQuery User Role to a Google Group)

**Topic:** IAM (BigQuery roles, groups)

## ❓ Question
> You are managing a project for the Business Intelligence (BI) department in your company. A data pipeline ingests data into BigQuery via streaming. You want the users in the BI department to be able to run the custom SQL queries against the latest data in BigQuery. What should you do?
>
> **A.** Create a Data Studio dashboard that uses the related BigQuery tables as a source and give the BI team view access to the Data Studio dashboard.
>
> **B.** Create a Service Account for the BI team and distribute a new private key to each member of the BI team.
>
> **C.** Use Cloud Scheduler to schedule a batch Dataflow job to copy the data from BigQuery to the BI team's internal data warehouse.
>
> **D.** Assign the IAM role of BigQuery User to a Google Group that contains the members of the BI team.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** BI users must **run their own SQL** on **live** data in BigQuery.

**Clues in the question:**
- "**run the custom SQL queries**" → they need to **run jobs** → **BigQuery User** (can run queries, create datasets).
- "**users in the BI department**" → grant to a **Google Group**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. BigQuery User role 🔑
- **What it is:** `roles/bigquery.user`: can **run queries/jobs** and create datasets in the project.
- **Looks like:** `gcloud projects add-iam-policy-binding bi-proj --member=group:bi@co.com --role=roles/bigquery.user`
- **Not to be confused with:** Data Viewer (read only).
- **Analogy:** 🧑‍💻 A pass to use the query terminal.
- **In the online store:** Analysts query sales.

### 2. Google Group (review)
- **What it is:** A named list of people's accounts. Grant once, everyone on the list gets it.
- **Looks like:** bi@co.com = [ana, ben]
- **Not to be confused with:** a shared login.
- **Analogy:** 📋 Department roster.
- **In the online store:** —

### 🔗 How they fit together
```
 group bi@ → roles/bigquery.user → run SQL on streaming tables ✅
```

---

## 🌍 Real-World Scenario

The BI team wants to write their own SQL on fresh streaming data. The admin grants **BigQuery User** to `bi-team@company.com`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Data Studio dashboard that uses the related BigQuery tables as a source and give the BI team view access to the Data Studio dashboard.

**Wrong words:**
- ❌ "**Data Studio dashboard … view access**": viewers see fixed charts but can't run **custom SQL**.

📌 **When to use it:** Use it for sharing ready-made reports.
🏢 **Office example:** Giving staff a printed report when they asked to query the database.

### ❌ B
> **B.** Create a Service Account for the BI team and distribute a new private key to each member of the BI team.

**Wrong words:**
- ❌ "**distribute a new private key to each member**": shared keys are insecure and hide who did what.

📌 **When to use it:** **Never use this.** Grant roles to people/groups.
🏢 **Office example:** Copying one master key for the whole department.

### ❌ C
> **C.** Use Cloud Scheduler to schedule a batch Dataflow job to copy the data from BigQuery to the BI team's internal data warehouse.

**Wrong words:**
- ❌ "**copy the data … to the BI team's internal data warehouse**": batch copies aren't the **latest** data and add cost.

📌 **When to use it:** Use it only if data must move to another system.
🏢 **Office example:** Photocopying the ledger nightly when they want today's numbers.

### ✅ D
> **D.** Assign the IAM role of BigQuery User to a Google Group that contains the members of the BI team.

**Why it's correct:**
- ✔️ "**BigQuery User**" matches "**run the custom SQL queries**".
- ✔️ "**Google Group that contains the members of the BI team**" matches "**users in the BI department**".
- ✔️ Querying BigQuery directly matches "**against the latest data**".

📌 **When to use it:** Use it when a whole department needs to search the records themselves.
🏢 **Office example:** Adding the analytics department roster to the query-terminal access list.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud projects add-iam-policy-binding shopnow-analytics --member=group:bi-team@shopnow.com --role=roles/bigquery.user` (+ dataViewer on the sales dataset).

---

## 🧠 Key Takeaways / Memory Tips

- **Users run queries → BigQuery User (jobs). Grant to a group.**
  🧠 *"**Run SQL? BigQuery User.**"*
- Related: **Q121**, **Q165**.

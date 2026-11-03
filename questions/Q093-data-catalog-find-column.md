# Q093: Finding a Column Across 1000+ BigQuery Datasets (Data Catalog Search)

**Topic:** Data governance (Data Catalog / Dataplex search, BigQuery INFORMATION_SCHEMA)

## ❓ Question
> Your company uses BigQuery for data warehousing. Over time, many different business units in your company have created 1000+ datasets across hundreds of projects. Your CIO wants you to examine all datasets to find tables that contain an employee_ssn column. You want to minimize effort in performing this task. What should you do?
>
> **A.** Go to Data Catalog and search for employee_ssn in the search box.
>
> **B.** Write a shell script that uses the bq command line tool to loop through all the projects in your organization.
>
> **C.** Write a script that loops through all the projects in your organization and runs a query on INFORMATION_SCHEMA.COLUMNS view to find the employee_ssn column.
>
> **D.** Write a Cloud Dataflow job that loops through all the projects in your organization and runs a query on INFORMATION_SCHEMA.COLUMNS view to find employee_ssn column.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Thousands of datasets in hundreds of projects. Find every table with a column named `employee_ssn`, with the **least effort**.

**Clues in the question:**
- "**1000+ datasets across hundreds of projects**": too many to check one by one.
- "**minimize effort**": no scripts to write. **Data Catalog** already indexes every BigQuery table and column, so you just **search**.

**Exam topic:** Data management / BigQuery.

---

## 📚 Key Terms Explained

### 1️⃣ Data Catalog 🔑
- **What it is:** Google's **searchable inventory of your data**. It automatically indexes BigQuery datasets, tables and **column names** across all projects you can see. (It's now part of **Dataplex**.)
- **Looks like:** search box → `column:employee_ssn` → list of tables in every project
- **Not to be confused with:** BigQuery itself. Data Catalog stores **descriptions of data**, not the data.
- **Analogy:** 📇 The **company-wide file index**: type a word and see every folder that has it.
- **In the online store:** Find every table with `customer_email` before a privacy review.

### 2️⃣ INFORMATION_SCHEMA.COLUMNS
- **What it is:** A built-in BigQuery view that lists the columns of tables, **one dataset or region per project at a time**.
- **Looks like:** `SELECT table_name FROM proj.region-us.INFORMATION_SCHEMA.COLUMNS WHERE column_name='employee_ssn'`
- **Not to be confused with:** an organization-wide search. You'd still loop over hundreds of projects.

### 3️⃣ bq command-line tool / Dataflow
- **bq:** the command-line tool for BigQuery. Looping it over hundreds of projects = writing and running a script.
- **Dataflow:** a service for running big data **pipelines**. Far too heavy for a search.

### 🔗 How they fit together
```
 Data Catalog (already indexes all projects) → search "employee_ssn" → done ✅
 Scripts with bq / INFORMATION_SCHEMA → loop 100s of projects → more effort ❌
```

---

## 🌍 Real-World Scenario

A privacy audit asks: "Where do we store social security numbers?" Instead of writing a script, the data engineer opens **Data Catalog** (Dataplex search), types `column:employee_ssn`, and gets every matching table across the organization in seconds.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Go to Data Catalog and search for employee_ssn in the search box.

**Why it's correct:**
- ✔️ "**Go to Data Catalog**" matches "**1000+ datasets across hundreds of projects**": Data Catalog already indexes all of them in one place.
- ✔️ "**search for employee_ssn in the search box**" matches "**find tables that contain an employee_ssn column**": it searches column names directly.
- ✔️ "**search box**" matches "**minimize effort**": no code to write or run.

📌 **When to use it:** Use it when you need to find where something is stored across many places, fast.
🏢 **Office example:** Typing a word into the company's file index instead of opening every cabinet.

### ❌ B
> **B.** Write a shell script that uses the bq command line tool to loop through all the projects in your organization.

**Wrong words:**
- ❌ "**Write a shell script … loop through all the projects**": you have to write, test and run a script over hundreds of projects. Much more effort than a search.

📌 **When to use it:** Use a bq script when you must **change** or export many datasets automatically.
🏢 **Office example:** Writing a checklist and visiting every office yourself.

### ❌ C
> **C.** Write a script that loops through all the projects in your organization and runs a query on INFORMATION_SCHEMA.COLUMNS view to find the employee_ssn column.

**Wrong words:**
- ✔️ "INFORMATION_SCHEMA.COLUMNS" can find column names.
- ❌ "**Write a script that loops through all the projects**": still a custom script over hundreds of projects. Not "minimize effort".

📌 **When to use it:** Use INFORMATION_SCHEMA when checking columns in one project or dataset.
🏢 **Office example:** Reading each office's own folder list, one office at a time.

### ❌ D
> **D.** Write a Cloud Dataflow job that loops through all the projects in your organization and runs a query on INFORMATION_SCHEMA.COLUMNS view to find employee_ssn column.

**Wrong words:**
- ❌ "**Write a Cloud Dataflow job**": a data-processing pipeline is far heavier than a search, and you still loop over every project.

📌 **When to use it:** Use Dataflow to process large streams or batches of data.
🏢 **Office example:** Hiring a moving company to find one word in the files.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's legal team asks where `customer_card_last4` is stored. The data engineer opens **Dataplex → Search**, types `column:customer_card_last4`, and finds it in `orders.payments` and an old `marketing.export_2023` table, which is then cleaned up.

---

## 🧠 Key Takeaways / Memory Tips

- **"Find a column/table across many projects, least effort" → Data Catalog search.**
- Scripts with bq or INFORMATION_SCHEMA = more effort.
  🧠 *"**Looking for data? Search the catalog.**"*
- Related: **Q085** (BigQuery external tables), **Q068** (logs into BigQuery).

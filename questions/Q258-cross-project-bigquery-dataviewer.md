# Q258: VMs in web-applications Need BigQuery in crm-databases (bigquery.dataViewer on crm-databases)

**Topic:** IAM (cross-project service account access)

## ❓ Question
> You are configuring service accounts for an application that spans multiple projects. Virtual machines (VMs) running in the web-applications project need access to BigQuery datasets in the crm-databases project. You want to follow Google-recommended practices to grant access to the service account in the web-applications project. What should you do?
>
> **A.** Grant "project owner" for web-applications appropriate roles to crm-databases.
>
> **B.** Grant "project owner" role to crm-databases and the web-applications project.
>
> **C.** Grant "project owner" role to crm-databases and roles/bigquery.dataViewer role to web-applications.
>
> **D.** Grant roles/bigquery.dataViewer role to crm-databases and appropriate roles to web-applications.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** The options are worded oddly (this question is a garbled copy of a well-known one). Read D as: give the **web-applications service account** `roles/bigquery.dataViewer` **in crm-databases**, and only the roles it needs in its own project. Every other option grants **Project Owner**, which breaks least privilege.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** VMs in project web-applications need BigQuery data in project crm-databases.
- **What you must achieve:** Give the VMs' service account access.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** In which project and with which role do you grant access?

**Clues in the question:**
- "**Google-recommended practices**" → least privilege → **BigQuery Data Viewer** in crm-databases, not Owner.
- Grant it to the **web-applications VMs' service account**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Cross-project grant 🔑 (review from Q133/Q165)
- **What it is:** A service account from one project can be given roles in another.
- **Looks like:** `gcloud projects add-iam-policy-binding crm-databases --member=serviceAccount:web-sa@web-applications.iam.gserviceaccount.com --role=roles/bigquery.dataViewer`
- **Not to be confused with:** Owner.
- **Analogy:** 🪪 A visitor badge for one archive in another building.
- **In the online store:** Storefront reads CRM.

### 🔗 How they fit together
```
 web-applications: VM (web-sa) ──read──► crm-databases: BigQuery (web-sa = dataViewer) ✅
```

---

## 🌍 Real-World Scenario

The storefront VMs need customer segments from the CRM project. The admin grants their service account **BigQuery Data Viewer** on crm-databases.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant "project owner" for web-applications appropriate roles to crm-databases.

**Wrong words:**
- ❌ "**project owner**": far more than reading data.

📌 **When to use it:** **Never** grant Owner for data access.
🏢 **Office example:** Giving a visitor the building deed.

### ❌ B
> **B.** Grant "project owner" role to crm-databases and the web-applications project.

**Wrong words:**
- ❌ "**project owner role to crm-databases and the web-applications project**": Owner in both projects.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** The deed to two buildings.

### ❌ C
> **C.** Grant "project owner" role to crm-databases and roles/bigquery.dataViewer role to web-applications.

**Wrong words:**
- ❌ "**project owner role to crm-databases**": Owner where only read is needed.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** The deed to the archive building.

### ✅ D
> **D.** Grant roles/bigquery.dataViewer role to crm-databases and appropriate roles to web-applications.

**Why it's correct:**
- ✔️ "**roles/bigquery.dataViewer role to crm-databases**" matches "**need access to BigQuery datasets in the crm-databases project**" with least privilege.
- ✔️ "**appropriate roles to web-applications**" matches "**Google-recommended practices**": only what's needed there too.

📌 **When to use it:** Use it when a program in one team's area needs to read records kept by another team.
🏢 **Office example:** Giving the visiting clerk a read-only pass to the other building's archive.

---

## 🛒 E-Commerce Full-Stack Example

`serviceAccount:storefront-sa@shopnow-web.iam.gserviceaccount.com` → `roles/bigquery.dataViewer` on `shopnow-crm` (+ `roles/bigquery.jobUser` in `shopnow-web` to run queries).

---

## 🧠 Key Takeaways / Memory Tips

- **Cross-project read → grant the SA a viewer role in the data project. Never Owner.**
  🧠 *"**Read access, not the deed.**"*
- Related: **Q165**, **Q133**.

# Q355: One View of Health and Downtime Risk Across Bigtable, Cloud SQL, Memorystore, Spanner (Database Center)

**Topic:** Databases (Database Center)

## ❓ Question
> You are managing a fleet of data storage solutions for your company on Google Cloud, including Bigtable, Cloud SQL, Memorystore, and Spanner. You need a single, unified view to monitor the health of all data storage solutions and identify any that are at risk for downtime. What should you do?
>
> **A.** Use Dataplex Universal Catalog to search the metadata of the data storage solutions to obtain the required insights.
>
> **B.** Use the terraform state list command in the directory used to deploy the data storage solutions.
>
> **C.** In the Google Cloud Console, use Cloud Asset Inventory to see an overview of the data storage solutions.
>
> **D.** In the Google Cloud Console, navigate to Database Center to find an overview of the data storage solutions.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You manage many databases: Bigtable, Cloud SQL, Memorystore and Spanner.
- **What you must achieve:** One unified view of the health of all of them, showing which are at risk of downtime.
- **The limits:** None stated.
- **What they're really asking:** Which console tool shows the health of all your databases in one place?

**Clues in the question:**
- "**single, unified view**" + "**health**" + "**at risk for downtime**" across many DB products → **Database Center**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Database Center 🔑
- **What it is:** A console dashboard showing all your database instances across products, with health issues and recommendations (e.g., no backups, no HA).
- **Looks like:** Console → Database Center → issues: 'Cloud SQL instance without automated backups'
- **Not to be confused with:** Cloud Asset Inventory (lists, no health).
- **Analogy:** 🩺 One health board for all your vehicles.
- **In the online store:** ShopNow DB fleet.

### 🔗 How they fit together
```
 Bigtable + Cloud SQL + Memorystore + Spanner → Database Center (health) ✅
```

---

## 🌍 Real-World Scenario

The DB team opens **Database Center** to spot instances without HA or backups.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Dataplex Universal Catalog to search the metadata of the data storage solutions to obtain the required insights.

**Wrong words:**
- ❌ "**Dataplex Universal Catalog**": data catalog/metadata, not health.

📌 **When to use it:** Use Dataplex to discover and govern data.
🏢 **Office example:** The library catalog, not the health board.

### ❌ B
> **B.** Use the terraform state list command in the directory used to deploy the data storage solutions.

**Wrong words:**
- ❌ "**terraform state list**": lists resources Terraform made; no health.

📌 **When to use it:** Use it to see Terraform-managed resources.
🏢 **Office example:** A purchase list, not a health check.

### ❌ C
> **C.** In the Google Cloud Console, use Cloud Asset Inventory to see an overview of the data storage solutions.

**Wrong words:**
- ❌ "**Cloud Asset Inventory**": lists resources; no health risk analysis.

📌 **When to use it:** Use it for inventory audits.
🏢 **Office example:** An inventory list without checkups.

### ✅ D
> **D.** In the Google Cloud Console, navigate to Database Center to find an overview of the data storage solutions.

**Why it's correct:**
- ✔️ "**Database Center**" matches "**single, unified view to monitor the health of all data storage solutions and identify any that are at risk for downtime**".

📌 **When to use it:** Use it when you want one screen showing which of your record systems need attention.
🏢 **Office example:** One health board showing which company vehicles are overdue for service.

---

## 🛒 E-Commerce Full-Stack Example

Database Center flags `orders-replica` without HA.

---

## 🧠 Key Takeaways / Memory Tips

- **Health of all databases in one place → Database Center.**
  🧠 *"**Database health? Database Center.**"*
- Related: —

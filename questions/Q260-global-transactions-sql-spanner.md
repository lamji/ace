# Q260: Global E-Commerce Transactions, SQL Analytics, Highly Available and Scalable (Multi-Region Cloud Spanner)

**Topic:** Databases (Spanner)

## ❓ Question
> You are building a backend service for an ecommerce platform that will persist transaction data from mobile and web clients. After the platform is launched, you expect a large volume of global transactions. Your business team wants to run SQL queries to analyze the data. You need to build a highly available and scalable data store for the platform. What should you do?
>
> **A.** Create a multi-region Cloud Spanner instance with an optimized schema.
>
> **B.** Create a multi-region Firestore database with aggregation query enabled.
>
> **C.** Create a multi-region Cloud SQL for PostgreSQL database with optimized indexes.
>
> **D.** Create a multi-region BigQuery dataset with optimized tables.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Global transactions**, **SQL**, **highly available**, **scalable**.

**Clues in the question:**
- "**persist transaction data**" + "**large volume of global transactions**" + "**SQL**" + "**highly available and scalable**" → **multi-region Spanner**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Spanner multi-region 🔑 (review from Q173)
- **What it is:** Relational, SQL, strongly consistent across regions, 99.999% SLA.
- **Looks like:** `--config=nam-eur-asia1`
- **Not to be confused with:** Cloud SQL (regional).
- **Analogy:** 🏦 One ledger in every branch.
- **In the online store:** ShopNow global orders.

### 🔗 How they fit together
```
 mobile/web worldwide → Spanner multi-region (transactions + SQL) ✅
```

---

## 🌍 Real-World Scenario

A global marketplace stores orders in **multi-region Spanner**; analysts query it with SQL.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a multi-region Cloud Spanner instance with an optimized schema.

**Why it's correct:**
- ✔️ "**multi-region Cloud Spanner**" matches "**large volume of global transactions**" + "**highly available and scalable**".
- ✔️ Spanner supports SQL, which matches "**run SQL queries**".

📌 **When to use it:** Use it when people worldwide record transactions that must be safe, consistent and searchable.
🏢 **Office example:** One shared ledger that's always identical in every branch and easy to search.

### ❌ B
> **B.** Create a multi-region Firestore database with aggregation query enabled.

**Wrong words:**
- ❌ "**Firestore**": NoSQL documents; limited SQL-style analysis.

📌 **When to use it:** Use Firestore for app documents and mobile sync.
🏢 **Office example:** Index cards instead of a ledger.

### ❌ C
> **C.** Create a multi-region Cloud SQL for PostgreSQL database with optimized indexes.

**Wrong words:**
- ❌ "**multi-region Cloud SQL**": Cloud SQL is regional (replicas only); doesn't scale writes globally.

📌 **When to use it:** Use Cloud SQL for regional apps.
🏢 **Office example:** One branch's ledger with photocopies.

### ❌ D
> **D.** Create a multi-region BigQuery dataset with optimized tables.

**Wrong words:**
- ❌ "**BigQuery**": analytics warehouse, not for an app's transactional writes.

📌 **When to use it:** Use BigQuery to analyze exported data.
🏢 **Office example:** The archive isn't the cash register.

---

## 🛒 E-Commerce Full-Stack Example

Orders in Spanner `nam-eur-asia1`; nightly export to BigQuery for heavy analytics.

---

## 🧠 Key Takeaways / Memory Tips

- **Global transactions + SQL + HA → Spanner multi-region.**
  🧠 *"**Global transactions? Spanner.**"*
- Related: **Q173**, **Q199**, **Q200**.

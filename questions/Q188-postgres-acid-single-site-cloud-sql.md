# Q188: Internal Orders App on PostgreSQL, One Location, ACID, Minimal Code Changes (Cloud SQL)

**Topic:** Databases (Cloud SQL vs Spanner vs BigQuery vs Datastore)

## ❓ Question
> Your company has an internal application for managing transactional orders. The application is used exclusively by employees in a single physical location. The application requires strong consistency, fast queries, and ACID guarantees for multi-table transactional updates. The first version of the application is implemented in PostgreSQL, and you want to deploy it to the cloud with minimal code changes. Which database is most appropriate for this application?
>
> **A.** BigQuery
>
> **B.** Cloud SQL
>
> **C.** Cloud Spanner
>
> **D.** Cloud Datastore

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Orders app, **one location**, **ACID**, already **PostgreSQL**, **minimal code changes**.

**Clues in the question:**
- "**implemented in PostgreSQL**" + "**minimal code changes**" → **Cloud SQL for PostgreSQL**.
- "**single physical location**" → no need for global Spanner.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Cloud SQL 🔑
- **What it is:** Managed **MySQL, PostgreSQL, SQL Server**. Same engine, so apps move with little change. ACID, regional.
- **Looks like:** `gcloud sql instances create orders --database-version=POSTGRES_15 --region=us-east1`
- **Not to be confused with:** Spanner (global).
- **Analogy:** 🏪 Moving your ledger to a managed office, same format.
- **In the online store:** ShopNow orders DB.

### 2. ACID
- **What it is:** Transactions are all-or-nothing, consistent, isolated and durable.
- **Looks like:** order + payment rows saved together or not at all
- **Not to be confused with:** eventual consistency.
- **Analogy:** 🧾 A receipt that's either fully written or not at all.
- **In the online store:** Checkout.

### 🔗 How they fit together
```
 PostgreSQL app → Cloud SQL for PostgreSQL ✅ (same SQL, ACID, one region)
```

---

## 🌍 Real-World Scenario

A warehouse's internal order system runs on PostgreSQL. It moves to **Cloud SQL for PostgreSQL** with just a connection string change.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** BigQuery

**Wrong words:**
- ❌ "**BigQuery**": an analytics warehouse, not for transactional order updates.

📌 **When to use it:** Use BigQuery for reports over huge data.
🏢 **Office example:** Using the annual-report archive as your daily order book.

### ✅ B
> **B.** Cloud SQL

**Why it's correct:**
- ✔️ "**Cloud SQL**" matches "**implemented in PostgreSQL**" + "**minimal code changes**" (same engine).
- ✔️ It provides "**ACID guarantees for multi-table transactional updates**" and fits "**single physical location**".

📌 **When to use it:** Use it when one office's existing records system needs a managed home without changing how it works.
🏢 **Office example:** Moving the office ledger into a managed records room, same format and same forms.

### ❌ C
> **C.** Cloud Spanner

**Wrong words:**
- ✔️ Spanner is relational and ACID.
- ❌ "**Cloud Spanner**": built for global scale. It's overkill and needs code changes (different SQL dialect/driver details).

📌 **When to use it:** Use Spanner for global apps needing identical data everywhere.
🏢 **Office example:** Building a worldwide ledger system for one small office.

### ❌ D
> **D.** Cloud Datastore

**Wrong words:**
- ❌ "**Cloud Datastore**": NoSQL, so the PostgreSQL code would need rewriting.

📌 **When to use it:** Use Datastore/Firestore for app documents.
🏢 **Office example:** Switching from a ledger to loose index cards.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's internal warehouse order tool: `orders-pg` (Cloud SQL PostgreSQL 15, us-east1) with HA enabled.

---

## 🧠 Key Takeaways / Memory Tips

- **Existing MySQL/PostgreSQL, one region → Cloud SQL.** Global → Spanner.
  🧠 *"**Same engine, same region: Cloud SQL.**"*
- Related: **Q173**, **Q141**.

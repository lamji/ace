# Q217: Internal Orders App on PostgreSQL, One Location, ACID, Minimal Code Changes (Cloud SQL)

**Topic:** Databases (Cloud SQL)

## ❓ Question
> Your company has an internal application for managing transactional orders. The application is used exclusively by employees in a single physical location. The application requires strong consistency, fast queries, and ACID guarantees for multi-table transactional updates. The first version of the application is implemented in PostgreSQL, and you want to deploy it to the cloud with minimal code changes. Which database is most appropriate for this application?
>
> **A.** Bigtable
>
> **B.** BigQuery
>
> **C.** Cloud SQL
>
> **D.** Firestore

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An internal orders app is used by employees in one location. It needs strong consistency, fast queries and ACID transactions (all-or-nothing updates across tables). It is built on PostgreSQL.
- **What you must achieve:** Move it to the cloud.
- **The limits:** Minimal code changes.
- **What they're really asking:** Which database fits a single-location PostgreSQL transactional app?

**Clues in the question:**
- "**implemented in PostgreSQL**" + "**minimal code changes**" → **Cloud SQL for PostgreSQL**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Cloud SQL 🔑 (review from Q188)
- **What it is:** Managed MySQL/PostgreSQL/SQL Server, ACID, regional.
- **Looks like:** `--database-version=POSTGRES_15`
- **Not to be confused with:** Spanner.
- **Analogy:** 🏪 Same ledger format, managed office.
- **In the online store:** ShopNow orders DB.

### 🔗 How they fit together
```
 PostgreSQL app → Cloud SQL for PostgreSQL ✅
```

---

## 🌍 Real-World Scenario

A warehouse's PostgreSQL order system moves to **Cloud SQL for PostgreSQL** with just a new connection string.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Bigtable

**Wrong words:**
- ❌ "**Bigtable**": NoSQL, no multi-table ACID transactions.

📌 **When to use it:** Use Bigtable for huge time-series data.
🏢 **Office example:** A tally sheet instead of a ledger.

### ❌ B
> **B.** BigQuery

**Wrong words:**
- ❌ "**BigQuery**": analytics warehouse, not transactional updates.

📌 **When to use it:** Use BigQuery for reports.
🏢 **Office example:** Using the archive as the daily order book.

### ✅ C
> **C.** Cloud SQL

**Why it's correct:**
- ✔️ "**Cloud SQL**" matches "**implemented in PostgreSQL**" + "**minimal code changes**".
- ✔️ It gives "**ACID guarantees for multi-table transactional updates**" in "**a single physical location**".

📌 **When to use it:** Use it when one office's existing records system needs a managed home without changing how it works.
🏢 **Office example:** Moving the office ledger to a managed records room, same format.

### ❌ D
> **D.** Firestore

**Wrong words:**
- ❌ "**Firestore**": NoSQL documents; the PostgreSQL code would need rewriting.

📌 **When to use it:** Use Firestore for app documents.
🏢 **Office example:** Index cards instead of a ledger.

---

## 🛒 E-Commerce Full-Stack Example

`orders-pg` (Cloud SQL PostgreSQL 15, HA) for the warehouse order tool.

---

## 🧠 Key Takeaways / Memory Tips

- **Existing PostgreSQL/MySQL, one region → Cloud SQL.**
  🧠 *"**Same engine, same region: Cloud SQL.**"*
- Related: **Q188**.

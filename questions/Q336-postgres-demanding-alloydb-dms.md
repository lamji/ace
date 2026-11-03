# Q336: Fully Managed PostgreSQL With Fast Transactions and Analytics, Synchronous Replication (AlloyDB via Database Migration Service)

**Topic:** Databases (AlloyDB, DMS)

## ❓ Question
> Your company plans to migrate its on-premises PostgreSQL database to Google Cloud. The workloads are demanding, requiring fast transactional and analytical performance. You need to select a fully managed database service on Google Cloud. Your solution must also be able to synchronously replicate and optimize the storage layer. What should you do?
>
> **A.** Migrate the database to Cloud SQL for PostgreSQL by using Database Migration Service.
>
> **B.** Use the psql client installed on a Compute Engine instance. Connect to the Cloud SQL instance to perform the database migration.
>
> **C.** Migrate the database to AlloyDB for PostgreSQL by using Database Migration Service.
>
> **D.** Create a Compute Engine instance. Install and configure PostgreSQL on the instance, and migrate the database.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Demanding PostgreSQL: **fast transactional + analytical**, fully managed, sync replication & optimized storage.

**Clues in the question:**
- "**fast transactional and analytical performance**" + "**optimize the storage layer**" → **AlloyDB** (columnar engine, disaggregated storage with sync replication).
- Migrate with **Database Migration Service**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. AlloyDB 🔑 (review from Q311)
- **What it is:** PostgreSQL-compatible; columnar engine for analytics; storage layer replicates synchronously across zones.
- **Looks like:** —
- **Not to be confused with:** Cloud SQL.
- **Analogy:** 🏎️ Turbo Postgres.
- **In the online store:** —

### 2. Database Migration Service (DMS)
- **What it is:** Managed tool to migrate databases (continuous replication, minimal downtime).
- **Looks like:** DMS job: source on-prem PG → AlloyDB
- **Not to be confused with:** manual dumps.
- **Analogy:** 🚚 Moving company that keeps both offices in sync.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem PG ─DMS─► AlloyDB (OLTP + analytics, sync storage) ✅
```

---

## 🌍 Real-World Scenario

A team migrates to **AlloyDB** via **DMS** for fast transactions and built-in analytics.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate the database to Cloud SQL for PostgreSQL by using Database Migration Service.

**Wrong words:**
- ✔️ DMS is right.
- ❌ "**Cloud SQL for PostgreSQL**": no columnar analytics engine or AlloyDB's optimized storage.

📌 **When to use it:** Use Cloud SQL for standard Postgres needs.
🏢 **Office example:** A good cabinet, but not the turbo one.

### ❌ B
> **B.** Use the psql client installed on a Compute Engine instance. Connect to the Cloud SQL instance to perform the database migration.

**Wrong words:**
- ❌ "**psql client … Compute Engine**": manual migration to Cloud SQL.

📌 **When to use it:** Use psql for small manual tasks.
🏢 **Office example:** Carrying files by hand.

### ✅ C
> **C.** Migrate the database to AlloyDB for PostgreSQL by using Database Migration Service.

**Why it's correct:**
- ✔️ "**AlloyDB for PostgreSQL**" matches "**fast transactional and analytical performance**" + "**synchronously replicate and optimize the storage layer**".
- ✔️ "**Database Migration Service**" matches "**migrate … on-premises PostgreSQL**"; AlloyDB is "**fully managed**".

📌 **When to use it:** Use it when a busy PostgreSQL system needs to be much faster for both everyday work and reports.
🏢 **Office example:** Moving the ledger into a turbo cabinet with a moving company that keeps both in sync.

### ❌ D
> **D.** Create a Compute Engine instance. Install and configure PostgreSQL on the instance, and migrate the database.

**Wrong words:**
- ❌ "**Install and configure PostgreSQL**" on a VM: not fully managed.

📌 **When to use it:** Use self-managed DBs for unsupported extensions.
🏢 **Office example:** Running your own records room.

---

## 🛒 E-Commerce Full-Stack Example

DMS: on-prem `orders` PG → AlloyDB `shopnow-orders`.

---

## 🧠 Key Takeaways / Memory Tips

- **PostgreSQL + transactions + analytics + managed → AlloyDB (migrate with DMS).**
  🧠 *"**Alloy does both.**"*
- Related: **Q311**.

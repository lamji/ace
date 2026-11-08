# G045: Recover an AlloyDB Database to Just Before an Accidental DELETE (Point-in-Time Recovery From Continuous Backup)

**Topic:** Databases (AlloyDB backup and restore)
**Exam guide section:** 3.2 Managing storage and data solutions: Backing up and restoring database instances (AlloyDB)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> At 14:32 today, a developer accidentally ran a DELETE statement without a WHERE clause on the orders table in your AlloyDB for PostgreSQL cluster. Continuous backup and recovery is enabled with the default retention. You need to recover the data as it was at 14:30 without overwriting the current cluster. What should you do?
>
> **A.** Use point-in-time recovery to restore the cluster to 14:30 into a new cluster, and copy the needed data back.
>
> **B.** Ask Google Cloud Support to undo the DELETE statement.
>
> **C.** Create a read pool instance and read the deleted rows from it.
>
> **D.** Restore the most recent daily backup over the current cluster.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** At 14:32, someone ran a command that deleted every row in the orders table of an AlloyDB database (Google's high-performance PostgreSQL-compatible database).
- **What you must achieve:** Get the data back exactly as it was at 14:30.
- **The limits:** Don't overwrite the current cluster. Continuous backup (which keeps a running log of changes) is turned on.
- **What they're really asking:** Which AlloyDB recovery feature restores to an exact minute, and where does the restored data go?

**Clues in the question:**
- "**as it was at 14:30**": **point-in-time recovery** (PITR) from continuous backup.
- "**without overwriting the current cluster**": AlloyDB restores into a **new cluster**.

**Exam topic:** Database backup and restore (exam guide section 3.2).

---

## 📚 Key Terms Explained

### 1. Continuous backup and recovery 🔑
- **What it is:** AlloyDB keeps continuous backups and logs so you can restore to any point in the retention window (14 days by default, configurable). Restores create a **new cluster**.
- **Looks like:** `gcloud alloydb clusters restore orders-recovered --region=us-central1 --source-cluster=orders --point-in-time=2026-11-08T14:30:00Z --network=shop-vpc`
- **Not to be confused with:** Read pools (read-only scaling) or exports.
- **Analogy:** ⏪ A security camera recording you can rewind to an exact minute.
- **In the online store:** Recovering deleted orders.

### 2. Read pool
- **What it is:** Read-only AlloyDB instances that serve read traffic, kept in sync with the primary.
- **Looks like:** `orders-read-pool` (2 nodes)
- **Not to be confused with:** A backup. Read pools copy the current state, including the delete.
- **Analogy:** 📚 Extra reading desks showing the same current book.
- **In the online store:** Analytics reads.

### 🔗 How they fit together
```
 14:30 ✅ data ─ 14:32 DELETE ✗
 PITR to 14:30 ─► new cluster orders-recovered ─► copy rows back to orders ✅
```

---

## 🌍 Real-World Scenario

A rushed hotfix wipes the orders table. Because AlloyDB **continuous backup** is on, the team restores to 14:30 into `orders-recovered`, exports the missing rows, and re-imports them into production within the hour.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use point-in-time recovery to restore the cluster to 14:30 into a new cluster, and copy the needed data back.

**Why it's correct:**
- ✔️ "**point-in-time recovery to restore the cluster to 14:30**" matches "**recover the data as it was at 14:30**".
- ✔️ "**into a new cluster**" matches "**without overwriting the current cluster**".
- ✔️ "**copy the needed data back**" brings the rows back to production.

📌 **When to use it:** Use it when you need the data exactly as it was a few minutes before a mistake.
🏢 **Office example:** Rewinding the security recording to just before the mistake and copying what you need.

### ❌ B
> **B.** Ask Google Cloud Support to undo the DELETE statement.

**Wrong words:**
- ❌ "**Ask … Support to undo**": Support can't undo your SQL. Recovery is self-service with PITR.

📌 **When to use it:** Use Support for platform problems, not your own data mistakes.
🏢 **Office example:** Asking the landlord to undo shredded files.

### ❌ C
> **C.** Create a read pool instance and read the deleted rows from it.

**Wrong words:**
- ❌ "**read pool**": read pools mirror the current data, which already has the delete.

📌 **When to use it:** Use read pools to scale read traffic.
🏢 **Office example:** Reading the same empty book at another desk.

### ❌ D
> **D.** Restore the most recent daily backup over the current cluster.

**Wrong words:**
- ❌ "**most recent daily backup**": loses everything since the backup ran.
- ❌ "**over the current cluster**": breaks "**without overwriting the current cluster**".

📌 **When to use it:** Use a daily backup when you don't have continuous backup.
🏢 **Office example:** Restoring last night's copy and losing today's work.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: AlloyDB `orders` (continuous backup, 14 days) → restore to `orders-recovered` at 14:30 → `pg_dump -t orders` → reload the missing rows into prod.

---

## 🧠 Key Takeaways / Memory Tips

- **AlloyDB "undo to an exact minute" → PITR from continuous backup → new cluster.**
  🧠 *"**Rewind to a minute, into a new cluster.**"*
- Related: **Q311**, **Q336**, **G044**, **Q003**.

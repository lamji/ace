# Q171: Keep a Month-End Copy of a Cloud SQL Database for 3 Years (Export to an Archive Bucket)

**Topic:** Cloud SQL (exports vs backups, Archive storage)

## ❓ Question
> You are working with a Cloud SQL MySQL database at your company. You need to retain a month-end copy of the database for three years for audit purposes. What should you do?
>
> **A.** Set up an export job for the first of the month. Write the export file to an Archive class Cloud Storage bucket.
>
> **B.** Save the automatic first-of-the-month backup for three years. Store the backup file in an Archive class Cloud Storage bucket.
>
> **C.** Set up an on-demand backup for the first of the month. Write the backup to an Archive class Cloud Storage bucket.
>
> **D.** Convert the automatic first-of-the-month backup to an export file. Write the export file to a Coldline class Cloud Storage bucket.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **A**. Cloud SQL backups are managed by Cloud SQL itself. You can't pick a bucket for them or move them into one, so only an **export** produces a file you can put in an Archive bucket.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company uses a Cloud SQL MySQL database.
- **What you must achieve:** Keep a month-end copy of the database for three years for audits.
- **The limits:** Each month-end copy must last three years.
- **What they're really asking:** How do you create and keep those monthly copies?

**Clues in the question:**
- "**retain … for three years**" + "**audit**" (rarely opened) → **Archive** class.
- Cloud SQL **backups live inside Cloud SQL**. You can't write them to your own bucket. An **export** (SQL dump file) can go to any bucket.

**Exam topic:** Cloud SQL.

---

## 📚 Key Terms Explained

### 1. Cloud SQL export 🔑
- **What it is:** A **file** (SQL dump or CSV) of the database, written to a Cloud Storage bucket **you choose**.
- **Looks like:** `gcloud sql export sql shop-db gs://shop-audit/2026-11-01.sql.gz --database=orders`
- **Not to be confused with:** a backup.
- **Analogy:** 📦 Photocopying the ledger and filing the copy in the archive room.
- **In the online store:** Monthly order DB dump for auditors.

### 2. Cloud SQL backup
- **What it is:** A snapshot **managed by Cloud SQL**, used to restore the instance. It isn't a file you can move into your own bucket.
- **Looks like:** Automatic daily backups (kept 7 by default)
- **Not to be confused with:** an export file.
- **Analogy:** 🔒 The building's own safe. You can't carry it out.
- **In the online store:** Restore after a bad deploy.

### 3. Archive storage class
- **What it is:** The cheapest class for data kept **a year or more** and almost never read. 365-day minimum storage.
- **Looks like:** `gsutil mb -c archive gs://shop-audit`
- **Not to be confused with:** Coldline (90 days).
- **Analogy:** 🗄️ Deep storage room.
- **In the online store:** 3-year audit copies.

### 🔗 How they fit together
```
 1st of month → Cloud Scheduler → gcloud sql export → gs://shop-audit (Archive) ✅ (kept 3 years)
```

---

## 🌍 Real-World Scenario

Auditors require a month-end copy of the orders DB for 3 years. A scheduled job **exports** the DB on the 1st of each month to an **Archive** bucket, with a lifecycle rule that deletes files after 3 years.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set up an export job for the first of the month. Write the export file to an Archive class Cloud Storage bucket.

**Why it's correct:**
- ✔️ "**export job for the first of the month**" matches "**month-end copy of the database**": an export is a file you control.
- ✔️ "**Archive class Cloud Storage bucket**" matches "**retain … for three years for audit purposes**": the cheapest class for files you rarely open.

📌 **When to use it:** Use it when you must keep a copy of records for years and almost never look at it.
🏢 **Office example:** Photocopying the ledger every month-end and filing the copy in the deep storage room.

### ❌ B
> **B.** Save the automatic first-of-the-month backup for three years. Store the backup file in an Archive class Cloud Storage bucket.

**Wrong words:**
- ❌ "**Store the backup file in an Archive class Cloud Storage bucket**": Cloud SQL backups can't be stored in your own bucket.

📌 **When to use it:** Use automatic backups to restore the database after a mistake.
🏢 **Office example:** Trying to carry the building's safe to your storage unit.

### ❌ C
> **C.** Set up an on-demand backup for the first of the month. Write the backup to an Archive class Cloud Storage bucket.

**Wrong words:**
- ❌ "**Write the backup to an Archive class Cloud Storage bucket**": on-demand backups also stay inside Cloud SQL.

📌 **When to use it:** Use an on-demand backup right before a risky change.
🏢 **Office example:** Asking the safe to file itself in the archive room.

### ❌ D
> **D.** Convert the automatic first-of-the-month backup to an export file. Write the export file to a Coldline class Cloud Storage bucket.

**Wrong words:**
- ❌ "**Convert the automatic … backup to an export file**": there's no such conversion.
- ❌ "**Coldline**": Archive is cheaper for 3-year storage.

📌 **When to use it:** Use Coldline for data opened about once a quarter.
🏢 **Office example:** A quarterly cabinet for files you keep for years.

---

## 🛒 E-Commerce Full-Stack Example

Cloud Scheduler on the 1st → Cloud Function runs:
```bash
gcloud sql export sql shopnow-orders gs://shopnow-audit-archive/orders-$(date +%Y-%m).sql.gz --database=orders
```
Bucket class **Archive**, lifecycle `delete` at age 1095 days.

---

## 🧠 Key Takeaways / Memory Tips

- **Keep DB copies for years in your own bucket → Cloud SQL export to Archive.**
- Backups stay inside Cloud SQL.
  🧠 *"**Export to keep; backup to restore.**"*
- Related: **Q154** (Archive), **Q102**.

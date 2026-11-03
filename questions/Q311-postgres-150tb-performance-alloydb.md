# Q311: Migrate PostgreSQL With Big Performance Gains, Few Changes, 150+ TB per Region (AlloyDB)

**Topic:** Databases (AlloyDB for PostgreSQL)

## ❓ Question
> You need to migrate multiple PostgreSQL databases from your on-premises data center to Google Cloud. You want to significantly improve the performance of your databases while minimizing changes to your data schema and application code. You expect to exceed 150 TB of data per geographical region. You want to follow Google-recommended practices and minimize your operational costs. What should you do?
>
> **A.** Migrate your data to AlloyDB.
>
> **B.** Migrate your data to Spanner.
>
> **C.** Migrate your data to Firebase.
>
> **D.** Migrate your data to Bigtable.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** PostgreSQL → faster, **minimal schema/code changes**, very large.

**Clues in the question:**
- "**PostgreSQL**" + "**significantly improve the performance**" + "**minimizing changes**" → **AlloyDB** (fully PostgreSQL-compatible, much faster than standard PostgreSQL).
- "**150 TB**" is beyond Cloud SQL's 64 TB limit; AlloyDB handles it.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. AlloyDB for PostgreSQL 🔑
- **What it is:** Google's managed, PostgreSQL-compatible database built for high performance (faster transactions and analytics) and large sizes.
- **Looks like:** `gcloud alloydb clusters create orders --region=us-central1 --password=...`
- **Not to be confused with:** Cloud SQL for PostgreSQL (standard engine, smaller max size); Spanner (different SQL engine).
- **Analogy:** 🏎️ Same car model, much more powerful engine.
- **In the online store:** ShopNow order history DB.

### 🔗 How they fit together
```
 PostgreSQL (on-prem) → AlloyDB (same Postgres, faster, huge) ✅
```

---

## 🌍 Real-World Scenario

A company with huge PostgreSQL databases moves to **AlloyDB** for speed without rewriting apps.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Migrate your data to AlloyDB.

**Why it's correct:**
- ✔️ "**AlloyDB**" matches "**PostgreSQL**" + "**minimizing changes to your data schema and application code**" + "**significantly improve the performance**".

📌 **When to use it:** Use it when you run PostgreSQL and want it much faster and bigger without rewriting your programs.
🏢 **Office example:** Same filing system, but a far faster and bigger cabinet.

### ❌ B
> **B.** Migrate your data to Spanner.

**Wrong words:**
- ❌ "**Spanner**": would need schema and code changes (keys, interleaving, dialect differences).

📌 **When to use it:** Use Spanner for global relational scale.
🏢 **Office example:** Moving to a new filing system.

### ❌ C
> **C.** Migrate your data to Firebase.

**Wrong words:**
- ❌ "**Firebase**": a mobile/app platform; not a PostgreSQL target.

📌 **When to use it:** Use Firebase for mobile app backends.
🏢 **Office example:** Index cards for a ledger.

### ❌ D
> **D.** Migrate your data to Bigtable.

**Wrong words:**
- ❌ "**Bigtable**": NoSQL; full rewrite.

📌 **When to use it:** Use Bigtable for key-value streams.
🏢 **Office example:** A tally sheet for a ledger.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow 180 TB order archive DB → AlloyDB via Database Migration Service.

---

## 🧠 Key Takeaways / Memory Tips

- **PostgreSQL + much faster + minimal change → AlloyDB.**
  🧠 *"**Alloy = Postgres with a turbo.**"*
- Related: **Q336**.

# Q308: Social Platform Outgrowing PostgreSQL, Needs Auto Scaling and Multi-Region (Spanner)

**Topic:** Databases (Spanner)

## ❓ Question
> Your company has a rapidly growing social media platform and a user base primarily located in North America. Due to increasing demand, your current on-premises PostgreSQL database, hosted in your United States headquarters data center, no longer meets your needs. You need to identify a cloud-based database solution that offers automatic scaling, multi-region support for future expansion, and maintains low latency. What should you do?
>
> **A.** Use BigQuery.
>
> **B.** Use Spanner.
>
> **C.** Use Cloud SQL for PostgreSQL.
>
> **D.** Use Bigtable.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Relational, **automatic scaling**, **multi-region**, low latency.

**Clues in the question:**
- "**automatic scaling**" + "**multi-region support**" + relational (PostgreSQL) → **Spanner** (supports a PostgreSQL interface).

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Spanner 🔑 (review)
- **What it is:** Google's globally distributed relational database; scales horizontally; multi-region configs; PostgreSQL dialect available.
- **Looks like:** `gcloud spanner instances create social --config=nam6 --processing-units=1000`
- **Not to be confused with:** Cloud SQL (single region primary, vertical scaling).
- **Analogy:** 🏦 A bank ledger synced across branches.
- **In the online store:** —

### 🔗 How they fit together
```
 relational + auto scale + multi-region → Spanner ✅
```

---

## 🌍 Real-World Scenario

A social app moves from on-prem PostgreSQL to **Spanner** (PostgreSQL dialect) in a North America multi-region config.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use BigQuery.

**Wrong words:**
- ❌ "**BigQuery**": an analytics warehouse, not an app database.

📌 **When to use it:** Use BigQuery for analytics.
🏢 **Office example:** The reports library, not the live ledger.

### ✅ B
> **B.** Use Spanner.

**Why it's correct:**
- ✔️ "**Spanner**" matches "**automatic scaling, multi-region support … low latency**" for a relational workload.

📌 **When to use it:** Use it when a growing app needs one database that grows by itself and works across many regions.
🏢 **Office example:** One ledger kept perfectly in sync across every branch, adding pages as needed.

### ❌ C
> **C.** Use Cloud SQL for PostgreSQL.

**Wrong words:**
- ❌ "**Cloud SQL for PostgreSQL**": scales up a single primary; multi-region writes aren't supported.

📌 **When to use it:** Use Cloud SQL for regional relational apps.
🏢 **Office example:** One branch's ledger with photocopies elsewhere.

### ❌ D
> **D.** Use Bigtable.

**Wrong words:**
- ❌ "**Bigtable**": NoSQL; not relational SQL.

📌 **When to use it:** Use Bigtable for huge key-value streams.
🏢 **Office example:** A giant tally sheet.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow global loyalty service on Spanner `nam-eur-asia1`.

---

## 🧠 Key Takeaways / Memory Tips

- **Relational + horizontal scale + multi-region → Spanner.**
  🧠 *"**Grows and spans regions: Spanner.**"*
- Related: **Q327**, **Q188**.

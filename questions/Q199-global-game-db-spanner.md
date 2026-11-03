# Q199: Consistent Global Game Performance Without More Management (Cloud Spanner)

**Topic:** Databases (Spanner for global apps)

## ❓ Question
> You are building a multi-player gaming application that will store game information in a database. As the popularity of the application increases, you are concerned about delivering consistent performance. You need to ensure an optimal gaming performance for global users, without increasing the management complexity. What should you do?
>
> **A.** Use Cloud SQL database with cross-region replication to store game statistics in the EU, US, and APAC regions.
>
> **B.** Use Cloud Spanner to store user data mapped to the game statistics.
>
> **C.** Use BigQuery to store game statistics with a Redis on Memorystore instance in the front to provide global consistency.
>
> **D.** Store game statistics in a Bigtable database partitioned by username.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Global** players, **consistent** performance as it grows, **no extra management**.

**Clues in the question:**
- "**global users**" + "**consistent performance**" + "**without increasing the management complexity**" → **Cloud Spanner** (global, scales by adding nodes, fully managed).

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Cloud Spanner 🔑 (review from Q173)
- **What it is:** A managed relational database that spans regions with strong consistency and scales horizontally.
- **Looks like:** `--config=nam-eur-asia1`
- **Not to be confused with:** Cloud SQL (one primary region).
- **Analogy:** 🏦 One ledger identical in every branch.
- **In the online store:** Global player profiles.

### 2. Cross-region read replica
- **What it is:** A read-only copy of Cloud SQL in another region. Writes still go to one primary.
- **Looks like:** —
- **Not to be confused with:** multi-master.
- **Analogy:** 📠 Faxed copies of the ledger.
- **In the online store:** —

### 🔗 How they fit together
```
 players EU/US/APAC ─► Spanner multi-region (one managed DB) ✅
```

---

## 🌍 Real-World Scenario

A game studio's player base explodes worldwide. They store players and stats in **Spanner multi-region** so everyone gets fast, consistent reads and writes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Cloud SQL database with cross-region replication to store game statistics in the EU, US, and APAC regions.

**Wrong words:**
- ❌ "**Cloud SQL … cross-region replication**": replicas are read-only, writes go to one region, and you manage several instances.

📌 **When to use it:** Use Cloud SQL with replicas for mostly-read regional apps.
🏢 **Office example:** Faxing copies of one ledger to three branches.

### ✅ B
> **B.** Use Cloud Spanner to store user data mapped to the game statistics.

**Why it's correct:**
- ✔️ "**Cloud Spanner**" matches "**optimal gaming performance for global users**" + "**consistent performance**".
- ✔️ It's fully managed and scales by adding nodes, which matches "**without increasing the management complexity**".

📌 **When to use it:** Use it when people all over the world must read and update the same records quickly.
🏢 **Office example:** One shared ledger that's instantly the same in every branch, run by the landlord.

### ❌ C
> **C.** Use BigQuery to store game statistics with a Redis on Memorystore instance in the front to provide global consistency.

**Wrong words:**
- ❌ "**BigQuery**": analytics, not real-time game reads/writes.
- ❌ "**Redis … to provide global consistency**": a cache doesn't give global consistency, and it adds parts to manage.

📌 **When to use it:** Use BigQuery for analyzing game stats later.
🏢 **Office example:** Using the yearly archive as the scoreboard.

### ❌ D
> **D.** Store game statistics in a Bigtable database partitioned by username.

**Wrong words:**
- ❌ "**Bigtable … partitioned by username**": regional NoSQL, and multi-region needs replication setup; not the simple global answer.

📌 **When to use it:** Use Bigtable for huge time-series data.
🏢 **Office example:** A giant tally sheet in one building.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's global loyalty points live in **Spanner** `nam-eur-asia1`, so a reward earned in Tokyo shows up in Paris immediately.

---

## 🧠 Key Takeaways / Memory Tips

- **Global + consistent + low management → Spanner.**
  🧠 *"**Global game? Spanner.**"*
- Related: **Q173**, **Q200**.

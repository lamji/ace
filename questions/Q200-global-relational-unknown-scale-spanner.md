# Q200: Global Relational App With Unknown Growth, Minimal Config Changes (Cloud Spanner)

**Topic:** Databases (Spanner horizontal scaling)

## ❓ Question
> You are building an application that stores relational data from users. Users across the globe will use this application. Your CTO is concerned about the scaling requirements because the size of the user base is unknown. You need to implement a database solution that can scale with your user growth with minimum configuration changes. Which storage solution should you use?
>
> **A.** Cloud SQL
>
> **B.** Firestore
>
> **C.** Cloud Spanner
>
> **D.** Bigtable

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app stores relational data for users all over the world, and nobody knows how big the user base will become.
- **What you must achieve:** Use a database that grows along with the users.
- **The limits:** Users are global, and growth should need very few configuration changes.
- **What they're really asking:** Which database can scale with unknown worldwide growth easily?

**Clues in the question:**
- "**relational**" + "**across the globe**" + "**scale with your user growth**" → **Spanner** (horizontal scaling, can autoscale).

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Horizontal scaling 🔑
- **What it is:** Adding **more machines** (nodes) instead of a bigger one. Spanner does this without downtime.
- **Looks like:** `gcloud spanner instances update app --nodes=10` or autoscaler
- **Not to be confused with:** vertical scaling (Cloud SQL).
- **Analogy:** 👥 Hiring more clerks vs buying one bigger desk.
- **In the online store:** Grow with shoppers.

### 🔗 How they fit together
```
 users ↑↑↑ → Spanner nodes 3 → 10 → 30 ✅ (same schema, no redesign)
```

---

## 🌍 Real-World Scenario

A startup doesn't know if it'll have 1,000 or 10 million users worldwide. It picks **Spanner** so it can add capacity without re-architecting.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Cloud SQL

**Wrong words:**
- ✔️ Cloud SQL is relational.
- ❌ "**Cloud SQL**": scales up to one machine's limit in one region; global growth needs redesign.

📌 **When to use it:** Use Cloud SQL for regional apps with known size.
🏢 **Office example:** One desk that can only get so big.

### ❌ B
> **B.** Firestore

**Wrong words:**
- ❌ "**Firestore**": NoSQL documents, not relational.

📌 **When to use it:** Use Firestore for mobile/web app documents.
🏢 **Office example:** Index cards instead of a ledger.

### ✅ C
> **C.** Cloud Spanner

**Why it's correct:**
- ✔️ "**Cloud Spanner**" matches "**relational data**" + "**across the globe**".
- ✔️ It adds nodes without downtime, which matches "**scale with your user growth with minimum configuration changes**".

📌 **When to use it:** Use it when a worldwide records system must keep growing without being rebuilt.
🏢 **Office example:** Hiring more clerks for the same shared ledger whenever customers grow.

### ❌ D
> **D.** Bigtable

**Wrong words:**
- ❌ "**Bigtable**": NoSQL wide-column, not relational.

📌 **When to use it:** Use Bigtable for huge time-series data.
🏢 **Office example:** A tally sheet, not a ledger.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow global accounts in **Spanner** with the managed autoscaler (min 1, max 20 nodes).

---

## 🧠 Key Takeaways / Memory Tips

- **Relational + global + unknown scale → Spanner.**
  🧠 *"**Unknown growth, global SQL: Spanner.**"*
- Related: **Q173**, **Q199**, **Q188**.

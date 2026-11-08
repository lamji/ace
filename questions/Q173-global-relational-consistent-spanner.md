# Q173: Global Trading App: Relational, Identical Data Everywhere, Multi-Region (Cloud Spanner)

**Topic:** Databases (Spanner vs Cloud SQL vs Bigtable vs Firestore)

## ❓ Question
> You are developing a financial trading application that will be used globally. Data is stored and queried using a relational structure, and clients from all over the world should get the exact identical state of the data. The application will be deployed in multiple regions to provide the lowest latency to end users. You need to select a storage option for the application data while minimizing latency. What should you do?
>
> **A.** Use Cloud Bigtable for data storage.
>
> **B.** Use Cloud SQL for data storage.
>
> **C.** Use Cloud Spanner for data storage.
>
> **D.** Use Firestore for data storage.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are building a global trading app. Data is relational (tables queried with SQL), and every client worldwide must see exactly the same data. The app runs in several regions.
- **What you must achieve:** Choose where to store the data.
- **The limits:** Keep delay (latency) as low as possible for users everywhere.
- **What they're really asking:** Which database gives one identical, relational view of data worldwide with low delay?

**Clues in the question:**
- "**relational**" + "**globally**" + "**exact identical state**" + "**multiple regions**" → **Cloud Spanner**.
- Cloud SQL is relational but **regional**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Cloud Spanner 🔑
- **What it is:** A **relational SQL database** that spans **regions** with **strong consistency** (everyone sees the same data).
- **Looks like:** `gcloud spanner instances create trade --config=nam-eur-asia1 --nodes=3`
- **Not to be confused with:** Cloud SQL (one region).
- **Analogy:** 🏦 One ledger magically identical in every branch worldwide.
- **In the online store:** Global inventory counts.

### 2. Strong consistency
- **What it is:** After a write, **every** reader everywhere sees the new value.
- **Looks like:** Buy in Tokyo → London sees it instantly
- **Not to be confused with:** eventual consistency.
- **Analogy:** 📖 Everyone reads the same page.
- **In the online store:** Stock levels.

### 🔗 How they fit together
```
 users US / EU / Asia ─► Spanner multi-region (one relational DB, same data) ✅
```

---

## 🌍 Real-World Scenario

A trading platform serves traders worldwide. Every trader must see the **same** order book, and the data is relational. They choose **Spanner multi-region**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Cloud Bigtable for data storage.

**Wrong words:**
- ❌ "**Cloud Bigtable**": NoSQL (not relational).

📌 **When to use it:** Use Bigtable for huge time-series or IoT data.
🏢 **Office example:** A giant tally sheet, not a ledger with linked tables.

### ❌ B
> **B.** Use Cloud SQL for data storage.

**Wrong words:**
- ✔️ Cloud SQL is relational.
- ❌ "**Cloud SQL**": it runs in **one region**, so it can't serve global users with low latency.

📌 **When to use it:** Use Cloud SQL for a relational app in one region.
🏢 **Office example:** One branch's ledger. Other countries must call in.

### ✅ C
> **C.** Use Cloud Spanner for data storage.

**Why it's correct:**
- ✔️ "**Cloud Spanner**" matches "**relational structure**" + "**exact identical state of the data**" (strong consistency) + "**multiple regions**".

📌 **When to use it:** Use it when offices around the world must share one always-identical set of records.
🏢 **Office example:** One ledger that's instantly identical in every branch worldwide.

### ❌ D
> **D.** Use Firestore for data storage.

**Wrong words:**
- ❌ "**Firestore**": document (NoSQL) database, not relational.

📌 **When to use it:** Use Firestore for mobile/web app documents.
🏢 **Office example:** Folders of loose notes instead of a ledger.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow going global: inventory and orders in **Spanner** `nam-eur-asia1` so a sale in Paris immediately reduces stock seen in New York.

---

## 🧠 Key Takeaways / Memory Tips

- **Relational + global + strongly consistent → Spanner.**
- Relational + one region → Cloud SQL.
  🧠 *"**Spanner spans the globe.**"*
- Related: **Q188**, **Q180**, **Q187**.

# Q292: Customer Data, Rarely Read Historical Logs, High-Velocity Sensor Data (Cloud SQL, Cloud Storage Archive, Bigtable)

**Topic:** Storage choice (Cloud SQL, Cloud Storage classes, Bigtable)

## ❓ Question
> Your company stores data from multiple sources that have different data storage requirements. These data include: 1. Customer data that is structured and read with complex queries 2. Historical log data that is large in volume and accessed infrequently 3. Real-time sensor data with high-velocity writes, which needs to be available for analysis but can tolerate some data loss You need to design the most cost-effective storage solution that fulfills all data storage requirements. What should you do?
>
> **A.** Use Firestore for customer data, Cloud Storage (Nearline) for historical logs, and Bigtable for sensor data.
>
> **B.** Use Cloud SQL for customer data. Cloud Storage (Coldline) for historical logs, and BigQuery for sensor data.
>
> **C.** Use Cloud SQL for customer data. Cloud Storage (Archive) for historical logs, and Bigtable for sensor data.
>
> **D.** Use Spanner for all data.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **C**. Some argue Coldline or Nearline for the logs, but "accessed infrequently" + "most cost-effective" points to the cheapest class, Archive.

---

## 📖 What the Question Is Asking

**In plain words:** Pick the cheapest correct store for each of three data types.

**Clues in the question:**
- "**structured and read with complex queries**" → **Cloud SQL** (relational SQL).
- "**large in volume and accessed infrequently**" + "**most cost-effective**" → **Archive** storage.
- "**high-velocity writes**" sensor data → **Bigtable**.

**Exam topic:** Storage choice.

---

## 📚 Key Terms Explained

### 1. Matching data to stores 🔑
- **What it is:** Relational + queries → Cloud SQL; files rarely read → Cloud Storage cold class; huge write streams → Bigtable.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🗄️ Ledger, basement boxes, tally sheet.
- **In the online store:** Orders / old logs / clickstream.

### 🔗 How they fit together
```
 customers → Cloud SQL ✅   old logs → Archive ✅   sensors → Bigtable ✅
```

---

## 🌍 Real-World Scenario

A company keeps customers in **Cloud SQL**, old logs in an **Archive** bucket, and sensor streams in **Bigtable**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Firestore for customer data, Cloud Storage (Nearline) for historical logs, and Bigtable for sensor data.

**Wrong words:**
- ❌ "**Firestore for customer data**": NoSQL; weaker for complex relational queries.
- ❌ "**Nearline**": costs more than Archive for rarely read data.

📌 **When to use it:** Use Firestore for app documents; Nearline for monthly-read data.
🏢 **Office example:** Index cards for the ledger.

### ❌ B
> **B.** Use Cloud SQL for customer data. Cloud Storage (Coldline) for historical logs, and BigQuery for sensor data.

**Wrong words:**
- ✔️ Cloud SQL is right.
- ❌ "**BigQuery for sensor data**": streaming inserts at high velocity cost more and BigQuery isn't built as a write-heavy store.

📌 **When to use it:** Use BigQuery for analytics on loaded data.
🏢 **Office example:** Writing every sensor tick into the reports library.

### ✅ C
> **C.** Use Cloud SQL for customer data. Cloud Storage (Archive) for historical logs, and Bigtable for sensor data.

**Why it's correct:**
- ✔️ "**Cloud SQL for customer data**" matches "**structured and read with complex queries**".
- ✔️ "**Cloud Storage (Archive) for historical logs**" matches "**large in volume and accessed infrequently**" + "**most cost-effective**".
- ✔️ "**Bigtable for sensor data**" matches "**high-velocity writes**".

📌 **When to use it:** Use it when different kinds of records each need a store built for them, at the lowest cost.
🏢 **Office example:** Customer ledger in the office, old logs in the cheapest basement, sensor tallies on a giant fast sheet.

### ❌ D
> **D.** Use Spanner for all data.

**Wrong words:**
- ❌ "**Spanner for all data**": expensive, and wrong for cold logs.

📌 **When to use it:** Use Spanner for global relational data.
🏢 **Office example:** Putting everything in the most expensive vault.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow: customers → Cloud SQL; 2020–2024 logs → `gs://shopnow-log-archive` (Archive); delivery-van telemetry → Bigtable.

---

## 🧠 Key Takeaways / Memory Tips

- **Relational → Cloud SQL. Rarely read files → Archive. High-velocity writes → Bigtable.**
  🧠 *"**Ledger, basement, tally sheet.**"*
- Related: **Q139**, **Q154**, **Q188**.

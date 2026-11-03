# Q219: Migrate MySQL, Kafka and Reporting PostgreSQL With Global Scale and Little Management (Spanner, Pub/Sub, BigQuery)

**Topic:** Migration (choosing managed services)

## ❓ Question
> You are planning to migrate the following on-premises data management solutions to Google Cloud: • One MySQL cluster for your main database • Apache Kafka for your event streaming platform • One Cloud SQL for PostgreSQL database for your analytical and reporting needs. You want to implement Google-recommended solutions for the migration. You need to ensure that the new solutions provide global scalability and require minimal operational and infrastructure management. What should you do?
>
> **A.** Migrate from MySQL to Cloud SQL, from Kafka to Pub/Sub, and from Cloud SQL for PostgreSQL to BigQuery.
>
> **B.** Migrate from MySQL to Cloud Spanner, from Kafka to Pub/Sub, and from Cloud SQL for PostgreSQL to BigQuery.
>
> **C.** Migrate from MySQL to Cloud Spanner, from Kafka to Memorystore, and from Cloud SQL for PostgreSQL to Cloud SQL.
>
> **D.** Migrate from MySQL to Cloud SQL, from Kafka to Memorystore, and from Cloud SQL for PostgreSQL to Cloud SQL.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Main DB, event streaming, analytics → **global scale**, **minimal management**.

**Clues in the question:**
- Main relational DB + "**global scalability**" → **Spanner**.
- Kafka (event streaming) → **Pub/Sub**.
- "**analytical and reporting**" → **BigQuery**.

**Exam topic:** Migration.

---

## 📚 Key Terms Explained

### 1. Pub/Sub 🔑
- **What it is:** Google's managed, global messaging service; the usual Kafka replacement.
- **Looks like:** topic `orders-events`
- **Not to be confused with:** Memorystore (cache).
- **Analogy:** 📬 A global mail sorting center.
- **In the online store:** Order events.

### 2. Memorystore
- **What it is:** Managed **Redis/Memcached** cache. Not a streaming platform.
- **Looks like:** —
- **Not to be confused with:** Pub/Sub.
- **Analogy:** 🗒️ A sticky-note board.
- **In the online store:** Session cache.

### 3. BigQuery
- **What it is:** Serverless analytics data warehouse.
- **Looks like:** —
- **Not to be confused with:** Cloud SQL.
- **Analogy:** 📊 The analysis library.
- **In the online store:** Sales reports.

### 🔗 How they fit together
```
 MySQL → Spanner ✅   Kafka → Pub/Sub ✅   reporting PostgreSQL → BigQuery ✅
```

---

## 🌍 Real-World Scenario

A retailer modernizes: the main DB moves to **Spanner** (global), Kafka to **Pub/Sub**, and reporting to **BigQuery**, all fully managed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate from MySQL to Cloud SQL, from Kafka to Pub/Sub, and from Cloud SQL for PostgreSQL to BigQuery.

**Wrong words:**
- ✔️ "Kafka to Pub/Sub" and "PostgreSQL to BigQuery" are right.
- ❌ "**MySQL to Cloud SQL**": regional, not **global scalability**.

📌 **When to use it:** Use Cloud SQL for regional relational apps.
🏢 **Office example:** A single-branch ledger for a worldwide business.

### ✅ B
> **B.** Migrate from MySQL to Cloud Spanner, from Kafka to Pub/Sub, and from Cloud SQL for PostgreSQL to BigQuery.

**Why it's correct:**
- ✔️ "**MySQL to Cloud Spanner**" matches "**main database**" + "**global scalability**".
- ✔️ "**Kafka to Pub/Sub**" matches "**event streaming platform**" + "**minimal operational … management**".
- ✔️ "**Cloud SQL for PostgreSQL to BigQuery**" matches "**analytical and reporting needs**".

📌 **When to use it:** Use it when moving to fully managed services that grow worldwide without you running servers.
🏢 **Office example:** Moving the ledger, mailroom and reports library into services run by the landlord, sized for every branch.

### ❌ C
> **C.** Migrate from MySQL to Cloud Spanner, from Kafka to Memorystore, and from Cloud SQL for PostgreSQL to Cloud SQL.

**Wrong words:**
- ✔️ "MySQL to Cloud Spanner" is right.
- ❌ "**Kafka to Memorystore**": a cache, not a streaming platform.
- ❌ "**to Cloud SQL**" for analytics: not built for large-scale reporting.

📌 **When to use it:** Use Memorystore for caching.
🏢 **Office example:** Using a sticky-note board as a mailroom.

### ❌ D
> **D.** Migrate from MySQL to Cloud SQL, from Kafka to Memorystore, and from Cloud SQL for PostgreSQL to Cloud SQL.

**Wrong words:**
- ❌ "**Cloud SQL**", ❌ "**Memorystore**", ❌ "**Cloud SQL**": none give global scale or proper streaming/analytics.

📌 **When to use it:** **Never use this** combination for these needs.
🏢 **Office example:** Every department in the wrong room.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow: catalog/orders → **Spanner**; order events → **Pub/Sub**; reporting → **BigQuery**.

---

## 🧠 Key Takeaways / Memory Tips

- **Kafka → Pub/Sub. Global relational → Spanner. Analytics → BigQuery.**
  🧠 *"**Spanner, Pub/Sub, BigQuery: the managed trio.**"*
- Related: **Q173**, **Q213**.

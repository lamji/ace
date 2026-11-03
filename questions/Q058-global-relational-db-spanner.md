# Q058: Global Relational Database That Scales With Unknown User Growth (Cloud Spanner)

**Topic:** Databases (Cloud Spanner vs Cloud SQL vs Firestore vs Datastore; relational vs NoSQL; global horizontal scaling)

## ❓ Question
> You are building an application that stores relational data from users. Users across the globe will use this application. Your CTO is concerned about the scaling requirements because the size of the user base is unknown. You need to implement a database solution that can scale with your user growth with minimum configuration changes. Which storage solution should you use?
>
> **A.** Cloud SQL
>
> **B.** Cloud Spanner
>
> **C.** Cloud Firestore
>
> **D.** Cloud Datastore

**My answer:** D
**Correct answer:** B
**Result:** ❌ Incorrect

> Why D was tempting: Datastore scales automatically with no setup, which matches "minimum configuration changes". But it is **NoSQL**, and the question says **relational data**.

---

## 📖 What the Question Is Asking

**In plain words:** Your app stores data in **tables with relationships** (users, orders, ...). Users are **all over the world**, and you don't know how big it will get. Which database grows with you without lots of reconfiguring?

| Question words | What they point to |
|---|---|
| "**relational data**" | Tables, rows, SQL, joins → only **Cloud SQL** or **Cloud Spanner** qualify. Firestore/Datastore are out |
| "**across the globe**" | Must work across **many regions** → Spanner (Cloud SQL is one region) |
| "**size of the user base is unknown**" + "**scale with your user growth**" | Must grow **without limit** by adding capacity → Spanner scales horizontally |
| "**minimum configuration changes**" | Add nodes / turn on autoscaling, no re-architecting → Spanner |

**Exam topic:** Databases / choosing a storage service.

---

## 📚 Key Terms Explained

### 1️⃣ Relational data 🔑
- **What it is:** Data stored in **tables** (rows and columns) that **link to each other** with keys, queried with **SQL**.
- **Looks like:**
  ```
  users(user_id, name)        orders(order_id, user_id, total)
  SELECT * FROM orders JOIN users USING (user_id);
  ```
- **Not to be confused with:** NoSQL **documents** (JSON-like records with no fixed tables or joins).
- **Analogy:** 🗂️ A **spreadsheet workbook** where the "Orders" sheet points to rows in the "Customers" sheet.
- **In the online store:** Users, orders, order items, payments.

### 2️⃣ Cloud SQL
- **What it is:** Managed **MySQL / PostgreSQL / SQL Server**. Relational, but it runs in **one region** and grows mostly by using a **bigger machine** (vertical scaling).
- **Looks like:** `gcloud sql instances create shop-db --database-version=POSTGRES_15 --tier=db-custom-4-16384 --region=us-central1`
- **Not to be confused with:** Spanner. Cloud SQL has a size ceiling and isn't built to serve the whole globe from one database.
- **Analogy:** 🏢 One **big filing room** in one office. You can buy bigger cabinets, but only so big.
- **In the online store:** Perfect for a store with customers in one country.

### 3️⃣ Cloud Spanner 🔑
- **What it is:** Google's **relational SQL database** that **scales horizontally** (add more nodes) and can be **multi-region / global**, with strong consistency.
- **Looks like:** `gcloud spanner instances create shop-global --config=nam-eur-asia1 --nodes=3` (later: more nodes, or autoscaling)
- **Not to be confused with:** NoSQL. Spanner **is relational** (tables, SQL, joins), but it scales like NoSQL.
- **Analogy:** 🌍 A **filing system with synced branches in every country**. Need more room? Add another cabinet, and it stays one system.
- **In the online store:** One orders database that shoppers in the US, Europe and Asia all use.

### 4️⃣ Cloud Firestore
- **What it is:** A **NoSQL document database**. It stores JSON-like documents in collections, scales automatically and is great for mobile/web apps.
- **Looks like:** `carts/{userId}` → `{ items: [{sku: "red-sneaker", qty: 1}] }`
- **Not to be confused with:** a relational database. There are no tables or SQL joins.
- **Analogy:** 📁 A **folder of separate index cards**, one per customer, each written however you like.
- **In the online store:** Shopping carts and user sessions.

### 5️⃣ Cloud Datastore
- **What it is:** The **older NoSQL** database. Today it is **Firestore in Datastore mode**. It scales automatically, but it's **not relational**.
- **Looks like:** Entity `Kind: Product, key: 123, properties: {name: "Red Sneaker", price: 49}`
- **Not to be confused with:** Cloud SQL or Spanner. No tables with relationships, no SQL joins.
- **Analogy:** 📁 The **older version** of the index-card folder.
- **In the online store:** Product catalog entries in an older App Engine app.

### 🔗 How they fit together
```
                 Relational (tables + SQL)?
                 ├── YES ─┬─ one region, normal size ───► Cloud SQL
                 │        └─ global / unknown huge size ► Cloud Spanner ✅
                 └── NO (documents, NoSQL) ─────────────► Firestore (Datastore = older mode)
```

---

## 🌍 Real-World Scenario

A startup launches an app worldwide and has no idea whether it will get 1,000 or 100 million users. The data is relational (users, accounts, transactions), and correctness matters. Cloud SQL would work at first, but it lives in one region and hits a ceiling. Then you'd have to split the database (sharding), which is a big re-architecture. Spanner avoids that: you **add nodes** (or let autoscaling do it), and the same SQL database keeps growing across regions.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Cloud SQL

**Wrong words:**
- ✔️ "Cloud **SQL**" is relational, which fits "relational data".
- ❌ It fails "**across the globe**": a Cloud SQL instance lives in **one region** (read replicas elsewhere can only read).
- ❌ It fails "**scale with your user growth with minimum configuration changes**": it grows by a bigger machine up to a limit. Beyond that you need sharding, which is big changes.

📌 **When to use it:** Use it when your data is in tables and your users are mostly in one region at a normal size.
🏢 **Office example:** One filing room at head office that serves the whole company in one city.

### ✅ B (correct answer)
> **B.** Cloud Spanner

**Why it's correct:**

- ✔️ Relational SQL database matches "**relational data**": Tables, SQL, joins, transactions.
- ✔️ Multi-region / global configurations matches "**users across the globe**": One database replicated across continents.
- ✔️ Horizontal scaling (add nodes / autoscaler) matches "**size of the user base is unknown**", "**scale with your user growth**": No size ceiling. Just add capacity as users grow.
- ✔️ Same schema and SQL as you grow matches "**minimum configuration changes**": No sharding or re-architecting. Change the node count and that's it.

📌 **When to use it:** Use it when your data is in tables, users are worldwide, and you need it to keep growing without limits.
🏢 **Office example:** One shared filing system with synced branches in every country, where you just add cabinets as the company grows.

### ❌ C
> **C.** Cloud Firestore

**Wrong words:**
- ✔️ Scales automatically and globally, which fits "scale with your user growth".
- ❌ It fails "**relational data**": Firestore is a **NoSQL document** database, with no tables or SQL joins.

📌 **When to use it:** Use it for app data stored as separate records per user, like carts or profiles, that must sync to phones and web pages.
🏢 **Office example:** A folder of index cards, one per customer, each written in its own way.

### ❌ D (your answer)
> **D.** Cloud Datastore

**Wrong words:**
- ✔️ Scales automatically with no setup, which fits "minimum configuration changes". That's why it was tempting.
- ❌ It fails "**relational data**": Datastore is **NoSQL** (now Firestore in Datastore mode), with no tables, relationships or SQL joins.
- ❌ It's also the **older** product. New apps should use Firestore anyway.

📌 **When to use it:** Use it only for older App Engine apps that already use it. New NoSQL apps use Firestore.
🏢 **Office example:** The old index-card cabinet kept running only because old departments still use it.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow goes global: shoppers in the US, Europe and Asia.

| Data | Shape | Database |
|---|---|---|
| Users, orders, order items, payments | **Relational** (orders link to users and products) | **Cloud Spanner** (multi-region) ✅ |
| Shopping carts, sessions | Documents per user | Firestore |
| Product images | Files | Cloud Storage |

```bash
gcloud spanner instances create shopnow-global \
  --config=nam-eur-asia1 --processing-units=1000 --description="ShopNow orders"
# Black Friday: more shoppers → raise capacity, same database, same SQL
gcloud spanner instances update shopnow-global --processing-units=3000
```

---

## 🧠 Key Takeaways / Memory Tips

- **"Relational" + "global" / "unknown huge scale" → Cloud Spanner.**
- **"Relational" + one region / normal size → Cloud SQL.**
- **No "relational" (documents, mobile app data) → Firestore** (Datastore = older mode).
  🧠 *"**First ask: tables or documents? Then ask: one region or the whole world?**"*
- Related: **Q003** (Cloud SQL vs Spanner), **Q038** (Spanner IAM).

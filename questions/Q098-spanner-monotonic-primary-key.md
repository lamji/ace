# Q098: Cloud Spanner Read Latency on One Table (Avoid Monotonically Increasing Primary Keys)

**Topic:** Cloud Spanner (primary key design, hotspots, secondary indexes)

## ❓ Question
> Your customer has implemented a solution that uses Cloud Spanner and notices some read latency-related performance issues on one table. This table is accessed only by their users using a primary key. The table schema is shown below.
>
> *(schema image not included in the paste; in the original, the table is keyed on `person_id`, an increasing number, and has a `profile_picture` column)*
>
> You want to resolve the issue. What should you do?
>
> **A.** Remove the profile_picture field from the table.
>
> **B.** Add a secondary index on the person_id column.
>
> **C.** Change the primary key to not have monotonically increasing values.
>
> **D.** Create a secondary index using the following Data Definition Language (DDL): *(image not included)*

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** The schema image is missing, and this question is debated. Some people pick A (a big picture field slows reads). The accepted exam answer is **C**, assuming the missing schema shows an increasing primary key and the table receives frequent inserts. An increasing key concentrates **new writes** on one server; work, including reads, on that overloaded server can then slow down. Increasing keys alone do not prove that every read is slow.

---

## 📖 What the Question Is Asking

**In plain words:** One Spanner table is slow to read. Users always look rows up **by primary key**. What fixes it?

**Clues in the question:**
- "**accessed only … using a primary key**": lookups already use the key, so **extra indexes won't help** (rules out B and D).
- The missing schema reportedly shows an increasing `person_id`. For a **busy insert workload**, new IDs like 1001, 1002, 1003 all go to the **last key range**. That server may become overloaded. A read of a row on that server may then wait longer.
- Fix that particular bottleneck with keys that spread **new writes** among key ranges, such as UUIDv4 values or a hash prefix.
- **Limit:** If there are few inserts or reads are slow for some other reason, the question does not give enough evidence to prove this is the cause. C is the intended exam answer, not a diagnosis confirmed by the text alone.

**Exam topic:** Cloud Spanner / databases.

---

## 📚 Key Terms Explained

### 1️⃣ Primary key
- **What it is:** The **column (or columns) that uniquely identifies each row**. Spanner stores rows **sorted by primary key** and splits them across servers by key range.
- **Looks like:** `CREATE TABLE Persons (person_id INT64, name STRING(100), profile_picture BYTES(MAX)) PRIMARY KEY (person_id)`
- **Analogy:** 🗂️ The **folder number** on each file in the cabinet.

### 2️⃣ Monotonically increasing key / hotspot 🔑
- **What it is:** A key that **always goes up** (1, 2, 3… or a timestamp). Because rows are sorted by key, **new inserts** all go to the last key range. If inserts arrive quickly, the server handling that range can become overloaded. Reads handled there can then become slower too. That overloaded range is a **hotspot**.
- **Looks like:** bad: `person_id = 1001, 1002, 1003…` · better: `person_id = "3f9a1c2e-…"` (UUID v4)
- **Not to be confused with:** a missing index.
- **Analogy:** 🗄️ Filing every new folder in the **same last drawer**. One clerk is swamped while others sit idle.
- **In the online store:** Order IDs 1, 2, 3… all hit one Spanner split on Black Friday.

### 3️⃣ Secondary index
- **What it is:** An extra sorted copy of some columns, so you can look rows up **by a column other than the primary key**.
- **Not to be confused with:** the primary key itself, which is already indexed.
- **Analogy:** 📇 An **extra index card box** sorted by name. Useless if you always look up by folder number.

### 🔗 How they fit together
```
 Key 1001,1002,1003… → new writes → last split → busy server → reads there may wait 🔥
 Key UUIDv4 (random) → new writes spread among splits → servers share the work ✅
 Secondary index on the primary key → already exists, no help ❌
```

---

## 🌍 Real-World Scenario

A social app stores users in Spanner with `person_id` values 1001, 1002, 1003, and so on. During a signup surge, Spanner puts each new user at the end of the sorted table, so the same server receives the new writes. If the app also looks up those recently created users, that busy server must handle the reads too. Their read latency can rise even though the lookups already use the primary key. Spreading new IDs across the key space removes this particular bottleneck.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Remove the profile_picture field from the table.

**Wrong words:**
- ❌ "**Remove the profile_picture field**": it deletes data users need, and doesn't fix the root cause of uneven load across servers. (Better practice: store big pictures in Cloud Storage and keep only a link, but that's not the main issue here.)

📌 **When to use it:** Move large files out of the database when rows are huge and reads pull data you don't need.
🏢 **Office example:** Throwing away the photos in employee files because one drawer is slow.

### ❌ B
> **B.** Add a secondary index on the person_id column.

**Wrong words:**
- ❌ "**Add a secondary index on the person_id column**": `person_id` is already the primary key, so it's already indexed. An extra index adds write cost and doesn't fix the hotspot.

📌 **When to use it:** Add a secondary index when you look rows up by a column that **isn't** the primary key.
🏢 **Office example:** Making a second index by folder number when the folders are already sorted by number.

### ✅ C
> **C.** Change the primary key to not have monotonically increasing values.

**Why it's correct:**
- ✔️ Spanner keeps rows in **primary-key order** and assigns ranges of keys to different servers. With an increasing key, each new row goes to the **end range**. At a high insert rate, that one server receives too much work.
- ✔️ The server handling the end range also serves reads for rows in that range. If users read newly created rows, those reads can wait behind the concentrated work. That explains **read latency** without assuming that the primary-key lookup needs another index.
- ✔️ Non-increasing keys, such as UUIDv4 values, place new rows across different ranges so servers can share the inserts. This addresses the hotspot behind the intended answer.
- **Important qualification:** C is the best exam choice given the implied increasing-key schema. The question as pasted does not show insert rate or which keys users read, so it does not establish that the hotspot is the real cause in every workload.

📌 **When to use it:** Use it when new records keep piling onto one place and that one place gets overloaded.
🏢 **Office example:** Spreading new folders across all drawers instead of always the last one, so every clerk shares the work.

### ❌ D
> **D.** Create a secondary index using the following Data Definition Language (DDL): *(image not included)*

**Wrong words:**
- ❌ "**Create a secondary index**": users only read **by primary key**, so another index won't be used and doesn't fix the hotspot.

📌 **When to use it:** Add a secondary index when queries filter on other columns.
🏢 **Office example:** Making another card box nobody uses because everyone looks up by folder number.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `Orders` table in Spanner used `order_id = 1, 2, 3…`. On Black Friday, many checkouts insert new orders into the last key range. The checkout page then reads those new orders to show confirmations. The server serving that range is busy with inserts, so those reads may be slow.

```sql
CREATE TABLE Orders (
  order_id STRING(36) NOT NULL,   -- GENERATE_UUID()
  customer_id STRING(36),
  total NUMERIC
) PRIMARY KEY (order_id);
```
New orders can now land in different key ranges. If the concentrated writes caused the slow reads, this reduces that contention.

---

## 🧠 Key Takeaways / Memory Tips

- **Spanner + many inserts + increasing key → one busy end range → reads there may slow down.** Spread new keys with UUIDv4 or a hash prefix.
- Don't add secondary indexes for primary-key lookups.
  🧠 *"**Counting keys pile up. Random keys spread out.**"*
- Related: **Q058** (why Spanner), **Q067** (Spanner monitoring), **Q095** (Spanner IAM history).

**Google Cloud guidance:** [Schema design best practices](https://docs.cloud.google.com/spanner/docs/schema-design) explains that increasing keys concentrate inserts on one server and that other work on that server may slow. [Primary key migration overview](https://docs.cloud.google.com/spanner/docs/primary-keys-overview) describes the resulting latency and recommends UUIDv4 keys.

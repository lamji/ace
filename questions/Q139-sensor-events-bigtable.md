# Q139: Thousands of Sensor Events per Device, Time-Based Reads, Atomic Rows (Cloud Bigtable)

**Topic:** Databases (Cloud Bigtable for time series, row keys, Datastore, Filestore)

## ❓ Question
> The core business of your company is to rent out construction equipment at large scale. All the equipment that is being rented out has been equipped with multiple sensors that send event information every few seconds. These signals can vary from engine status, distance traveled, fuel level, and more. Customers are billed based on the consumption monitored by these sensors. You expect high throughput — up to thousands of events per hour per device — and need to retrieve consistent data based on the time of the event. Storing and retrieving individual signals should be atomic. What should you do?
>
> **A.** Create a file in Cloud Storage per device and append new data to that file.
>
> **B.** Create a file in Cloud Filestore per device and append new data to that file.
>
> **C.** Ingest the data into Datastore. Store data in an entity group based on the device.
>
> **D.** Ingest the data into Cloud Bigtable. Create a row key based on the event timestamp.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** D is the accepted answer (Bigtable for high-throughput time-series data). Real-world tip: a row key that **starts** with a timestamp causes hotspots; Google recommends `deviceId#timestamp`. For the exam, the point is **Bigtable + time-based row key**.

---

## 📖 What the Question Is Asking

**In plain words:** Huge numbers of sensor events, read back **by time**, and each write and read must be **atomic**. Which database?

**Clues in the question:**
- "**high throughput … thousands of events per hour per device**" + sensors = **time-series IoT data** → **Bigtable**.
- "**retrieve consistent data based on the time of the event**": the row key includes the **timestamp**, so time-range reads are fast.
- "**Storing and retrieving individual signals should be atomic**": Bigtable writes and reads of a **single row** are atomic.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Cloud Bigtable 🔑
- **What it is:** A **NoSQL wide-column database** for huge volumes of fast reads and writes (time series, IoT, analytics). Rows are sorted by **row key**, and single-row operations are atomic.
- **Looks like:** row key `excavator-17#2026-11-03T10:15:02` → columns `fuel`, `engine`, `km`
- **Not to be confused with:** a relational database or file storage.
- **Analogy:** 📇 A giant, super-fast **card index** sorted by label.
- **In the online store:** Clickstream events per user.

### 2. Row key
- **What it is:** The **one index** in Bigtable. Rows are stored and scanned in key order, so design it for your queries.
- **Looks like:** `deviceId#reverseTimestamp`
- **Not to be confused with:** a secondary index.
- **Analogy:** 🏷️ The label that decides where a card is filed.
- **In the online store:** `user123#20261103`

### 🔗 How they fit together
```
 sensors ─► Bigtable table events
   row key: device#timestamp → fuel | engine | km   (single-row writes atomic ✅)
   read: scan prefix device-17#2026-11 → this month's events ✅
```

---

## 🌍 Real-World Scenario

A rental company's machines send readings every few seconds. Billing needs usage per machine per time period. Readings stream into **Bigtable**, with row keys built from the device and event time, and billing jobs scan time ranges per device.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a file in Cloud Storage per device and append new data to that file.

**Wrong words:**
- ❌ "**file in Cloud Storage per device and append**": Cloud Storage objects can't be appended to. You'd rewrite the whole file each time, and there's no time-based querying.

📌 **When to use it:** Use Cloud Storage for files and archives.
🏢 **Office example:** Rewriting a whole notebook every time you add one line.

### ❌ B
> **B.** Create a file in Cloud Filestore per device and append new data to that file.

**Wrong words:**
- ❌ "**file in Cloud Filestore … append**": a shared file system isn't built for thousands of writes per device per hour, or for querying by time.

📌 **When to use it:** Use Filestore when apps need a shared network drive.
🏢 **Office example:** One shared notebook that everyone scribbles in.

### ❌ C
> **C.** Ingest the data into Datastore. Store data in an entity group based on the device.

**Wrong words:**
- ❌ "**Datastore … entity group based on the device**": entity groups are limited to about 1 write per second, which is far below this throughput.

📌 **When to use it:** Use Datastore/Firestore for app data like profiles and carts.
🏢 **Office example:** A tidy filing cabinet that can only take one new card per second.

### ✅ D
> **D.** Ingest the data into Cloud Bigtable. Create a row key based on the event timestamp.

**Why it's correct:**
- ✔️ "**Cloud Bigtable**" matches "**high throughput … thousands of events per hour per device**": built for massive streams of writes.
- ✔️ "**row key based on the event timestamp**" matches "**retrieve consistent data based on the time of the event**": rows are sorted by time for fast range reads.
- ✔️ "**Bigtable**" matches "**individual signals should be atomic**": single-row reads and writes are atomic.

📌 **When to use it:** Use it when you collect a constant flood of readings and look them up by time.
🏢 **Office example:** A huge, fast card index where every reading is filed by machine and time.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's delivery vans send GPS and fuel every 5 seconds into Bigtable table `van_events`, with row key `van-042#20261103T101502`. The billing job scans `van-042#202611*` for November usage.

---

## 🧠 Key Takeaways / Memory Tips

- **High-throughput time series / IoT → Bigtable.**
- Single-row operations are atomic; design the row key for your reads.
- Datastore entity groups ≈ 1 write/s.
  🧠 *"**Sensors firehose? Bigtable.**"*
- Related: **Q058** (Spanner), **Q098** (key design), **Q146**.

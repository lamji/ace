# Q264: Construction Equipment Sensors, Thousands of Events per Device, Time-Based Reads (Bigtable, Timestamp Row Key)

**Topic:** Databases (Bigtable)

## ❓ Question
> The core business of your company is to rent out construction equipment at large scale. All the equipment that is being rented out has been equipped with multiple sensors that send event information every few seconds. These signals can vary from engine status, distance traveled, fuel level, and more. Customers are billed based on the consumption monitored by these sensors. You expect high throughput – up to thousands of events per hour per device – and need to retrieve consistent data based on the time of the event. Storing and retrieving individual signals should be atomic. What should you do?
>
> **A.** Create files in Cloud Storage as data comes in.
>
> **B.** Create a file in Filestore per device, and append new data to that file.
>
> **C.** Ingest the data into Cloud SQL. Use multiple read replicas to match the throughput.
>
> **D.** Ingest the data into Bigtable. Create a row key based on the event timestamp.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** Same as Q139. In real Bigtable design, a row key that **starts** with the timestamp causes hotspots; Google recommends something like `deviceId#timestamp`. The exam's voted answer is still D.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Rented construction equipment has sensors that send events every few seconds, and customers are billed from these readings.
- **What you must achieve:** Store events and read them back by time.
- **The limits:** Up to thousands of events per hour per device, consistent reads by event time, and each signal stored all-or-nothing (atomically).
- **What they're really asking:** Which database fits huge streams of timestamped readings?

**Clues in the question:**
- "**high throughput – up to thousands of events per hour per device**" + "**time of the event**" + "**atomic**" → **Bigtable** (single-row operations are atomic).

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Bigtable 🔑 (review from Q139)
- **What it is:** NoSQL wide-column DB for huge volumes of time-series data; rows sorted by key; single-row ops are atomic.
- **Looks like:** row key `excavator42#20261103T101500`
- **Not to be confused with:** Cloud SQL.
- **Analogy:** 📜 A giant sorted ledger.
- **In the online store:** Clickstream.

### 🔗 How they fit together
```
 sensors → Bigtable (row key by time) → range scans by time ✅
```

---

## 🌍 Real-World Scenario

An equipment rental firm streams sensor readings into **Bigtable** and bills customers by scanning each device's rows for the billing period.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create files in Cloud Storage as data comes in.

**Wrong words:**
- ❌ "**files in Cloud Storage**": no per-signal atomic reads/writes or fast time queries.

📌 **When to use it:** Use Cloud Storage for files and archives.
🏢 **Office example:** Writing each reading on a separate sheet in a warehouse.

### ❌ B
> **B.** Create a file in Filestore per device, and append new data to that file.

**Wrong words:**
- ❌ "**file in Filestore per device … append**": file shares don't give atomic per-signal access at this scale.

📌 **When to use it:** Use Filestore for shared file systems.
🏢 **Office example:** One notebook per machine that everyone scribbles in.

### ❌ C
> **C.** Ingest the data into Cloud SQL. Use multiple read replicas to match the throughput.

**Wrong words:**
- ❌ "**Cloud SQL … read replicas to match the throughput**": replicas help reads, not this write volume.

📌 **When to use it:** Use Cloud SQL for transactional apps.
🏢 **Office example:** Photocopying a ledger to handle more writing.

### ✅ D
> **D.** Ingest the data into Bigtable. Create a row key based on the event timestamp.

**Why it's correct:**
- ✔️ "**Bigtable**" matches "**high throughput … thousands of events per hour per device**" + "**atomic**".
- ✔️ "**row key based on the event timestamp**" matches "**retrieve consistent data based on the time of the event**".

📌 **When to use it:** Use it when machines send endless readings that you later look up by time.
🏢 **Office example:** A giant ledger sorted by time where each reading is one complete line.

---

## 🛒 E-Commerce Full-Stack Example

Delivery-van telemetry in Bigtable `fleet-events`, row key `vanId#timestamp`.

---

## 🧠 Key Takeaways / Memory Tips

- **High-volume time series → Bigtable.**
  🧠 *"**Sensors + time = Bigtable.**"*
- Related: **Q139**, **Q213**.

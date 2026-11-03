# Q324: Global IoT Sensor Storage With Sub-Millisecond Latency (Bigtable)

**Topic:** Databases (Bigtable)

## ❓ Question
> You are developing an internet of things (IoT) application that captures sensor data from multiple devices that have already been set up. You need to identify the global data storage product your company should use to store this data. You must ensure that the storage solution you choose meets your requirements of sub-millisecond latency. What should you do?
>
> **A.** Store the IoT data in Spanner. Use caches to speed up the process and avoid latencies.
>
> **B.** Store the IoT data in Bigtable.
>
> **C.** Capture IoT data in BigQuery datasets.
>
> **D.** Store the IoT data in Cloud Storage. Implement caching by using Cloud CDN.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** IoT sensor data, **sub-millisecond latency**.

**Clues in the question:**
- IoT time series + "**sub-millisecond latency**" → **Bigtable** (low single-digit ms or better, huge write throughput).

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Bigtable 🔑 (review)
- **What it is:** Wide-column NoSQL for massive time-series/IoT data at very low latency; replication across regions.
- **Looks like:** row key `device#20261103T1200`
- **Not to be confused with:** BigQuery (analytics).
- **Analogy:** 📋 A giant, fast tally sheet.
- **In the online store:** —

### 🔗 How they fit together
```
 sensors → Bigtable (low latency, high writes) ✅
```

---

## 🌍 Real-World Scenario

An IoT app writes device readings to **Bigtable** with replicated clusters.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Store the IoT data in Spanner. Use caches to speed up the process and avoid latencies.

**Wrong words:**
- ❌ "**Spanner … Use caches**": relational and pricier; caches add complexity.

📌 **When to use it:** Use Spanner for global relational data.
🏢 **Office example:** A bank vault for sensor ticks.

### ✅ B
> **B.** Store the IoT data in Bigtable.

**Why it's correct:**
- ✔️ "**Bigtable**" matches "**IoT application that captures sensor data**" + "**sub-millisecond latency**".

📌 **When to use it:** Use it when huge streams of readings must be stored and read back almost instantly.
🏢 **Office example:** A giant tally sheet where every machine writes its readings and you look them up in a blink.

### ❌ C
> **C.** Capture IoT data in BigQuery datasets.

**Wrong words:**
- ❌ "**BigQuery**": analytics with seconds of latency.

📌 **When to use it:** Use BigQuery for reporting.
🏢 **Office example:** The reports library.

### ❌ D
> **D.** Store the IoT data in Cloud Storage. Implement caching by using Cloud CDN.

**Wrong words:**
- ❌ "**Cloud Storage … Cloud CDN**": object storage; CDN caches public content, not IoT writes.

📌 **When to use it:** Use it for files and media.
🏢 **Office example:** Filing each reading as a separate document.

---

## 🛒 E-Commerce Full-Stack Example

Delivery-van telemetry → Bigtable `fleet` (us-central1 + europe-west1).

---

## 🧠 Key Takeaways / Memory Tips

- **IoT + very low latency + high writes → Bigtable.**
  🧠 *"**Sensors → Bigtable.**"*
- Related: **Q292**, **Q139**.

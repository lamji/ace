# Q375: SAP HANA Needing 200,000+ IOPS and Persistent Data (Hyperdisk Extreme)

**Topic:** Compute Engine (disk types)

## ❓ Question
> You want to deploy SAP HANA workloads on Compute Engine. The installation requires high-performance data storage, with input/output operations per second (IOPS) frequently exceeding 200,000. Your solution must also ensure the data persists through instance restarts. What should you do?
>
> **A.** Use Hyperdisk Extreme disks for the application data.
>
> **B.** Use in-memory RAM disks for the application data.
>
> **C.** Use Local SSD disks for the application data.
>
> **D.** Use Hyperdisk Throughput disks for the application data.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will run SAP HANA (a large in-memory business database) on Compute Engine.
- **What you must achieve:** Give it very fast storage, often above 200,000 IOPS (disk operations per second).
- **The limits:** Data must survive VM restarts.
- **What they're really asking:** Which disk type gives that speed and keeps the data?

**Clues in the question:**
- Highest-IOPS **persistent** block storage → **Hyperdisk Extreme** (up to 350,000 IOPS), recommended for SAP HANA.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Hyperdisk Extreme 🔑
- **What it is:** Network block storage with provisioned, very high IOPS; persistent.
- **Looks like:** `gcloud compute disks create hana-data --type=hyperdisk-extreme --size=2TB --provisioned-iops=250000`
- **Not to be confused with:** Local SSD (data lost when VM stops).
- **Analogy:** 🏎️ The fastest permanent drive.
- **In the online store:** —

### 2. Hyperdisk Throughput
- **What it is:** Optimized for MB/s (big sequential reads), lower IOPS.
- **Looks like:** —
- **Not to be confused with:** Extreme (IOPS).
- **Analogy:** 🚚 Wide truck, not fast car.
- **In the online store:** —

### 🔗 How they fit together
```
 >200k IOPS + persistent → Hyperdisk Extreme ✅
```

---

## 🌍 Real-World Scenario

An SAP team puts HANA data on **Hyperdisk Extreme** with 250k provisioned IOPS.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use Hyperdisk Extreme disks for the application data.

**Why it's correct:**
- ✔️ "**Hyperdisk Extreme**" matches "**IOPS frequently exceeding 200,000**" + "**data persists through instance restarts**".

📌 **When to use it:** Use it when a demanding database needs the fastest permanent storage.
🏢 **Office example:** The fastest permanent filing cabinet for the busiest records.

### ❌ B
> **B.** Use in-memory RAM disks for the application data.

**Wrong words:**
- ❌ "**in-memory RAM disks**": lost on restart.

📌 **When to use it:** Use RAM disks for temporary scratch data.
🏢 **Office example:** Notes on a whiteboard wiped each night.

### ❌ C
> **C.** Use Local SSD disks for the application data.

**Wrong words:**
- ❌ "**Local SSD**": fast, but data doesn't persist when the VM stops.

📌 **When to use it:** Use Local SSD for caches/scratch.
🏢 **Office example:** A desk drawer emptied when you leave.

### ❌ D
> **D.** Use Hyperdisk Throughput disks for the application data.

**Wrong words:**
- ❌ "**Hyperdisk Throughput**": optimized for throughput, not 200k+ IOPS.

📌 **When to use it:** Use it for big sequential workloads (analytics, logs).
🏢 **Office example:** A wide truck for a sprint.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow ERP (SAP HANA) on M3 VM with Hyperdisk Extreme.

---

## 🧠 Key Takeaways / Memory Tips

- **Highest IOPS + persistent → Hyperdisk Extreme. Local SSD isn't persistent.**
  🧠 *"**Extreme IOPS, Extreme disk.**"*
- Related: **Q226**.

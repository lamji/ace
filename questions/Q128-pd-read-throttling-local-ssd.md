# Q128: Disk Read Throttling on a 350 GB SSD Persistent Disk, Max Throughput at Low Cost (Local SSD)

**Topic:** Compute Engine storage (persistent disk performance scaling, Local SSD, regional PD)

## ❓ Question
> You have an application on a general-purpose Compute Engine instance that is experiencing excessive disk read throttling on its Zonal SSD Persistent Disk. The application primarily reads large files from disk. The disk size is currently 350 GB. You want to provide the maximum amount of throughput while minimizing costs. What should you do?
>
> **A.** Increase the size of the disk to 1 TB.
>
> **B.** Increase the allocated CPU to the instance.
>
> **C.** Migrate to use a Local SSD on the instance.
>
> **D.** Migrate to use a Regional SSD on the instance.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** This question is debated. Many pick **A**, because persistent disk speed grows with size. The more common (most voted) answer is **C**: Local SSD gives far more throughput and is cheaper per GB than SSD PD. The catch is that Local SSD data is lost if the VM stops, so it suits files you can re-copy. **If your site shows a different "Most Voted" answer, tell me and I'll update it.**

---

## 📖 What the Question Is Asking

**In plain words:** The app reads big files and the disk is too slow (throttled). You want the **most throughput** for the **least money**.

**Clues in the question:**
- "**excessive disk read throttling**": the disk hits its speed limit. SSD PD speed depends on **size**, so a 350 GB disk has a lowish limit.
- "**maximum amount of throughput**": **Local SSD** is physically attached and much faster than any persistent disk.
- "**minimizing costs**": Local SSD costs less per GB than SSD persistent disk, and a 1 TB SSD PD costs much more.

**Exam topic:** Compute Engine / storage.

---

## 📚 Key Terms Explained

### 1. Persistent disk performance 🔑
- **What it is:** Persistent disk **IOPS and throughput grow with disk size** (and the VM's vCPU count), up to a cap. A small disk = low limit = throttling.
- **Looks like:** pd-ssd ≈ 0.48 MB/s read per GB → 350 GB ≈ 168 MB/s; 1 TB ≈ 480 MB/s
- **Not to be confused with:** Local SSD, which is much faster regardless.
- **Analogy:** 🚰 A **pipe whose width grows with the tank size**.
- **In the online store:** A bigger PD for the reporting DB.

### 2. Local SSD (review from Q077)
- **What it is:** An SSD **physically attached** to the host server. Very high throughput and IOPS, cheap per GB, but **temporary**: data is lost if the VM is stopped or deleted.
- **Looks like:** `--local-ssd=interface=NVME` (375 GB each)
- **Not to be confused with:** persistent disk (survives restarts).
- **Analogy:** 📝 Papers on your desk: fastest, but cleared at night.
- **In the online store:** A cache of product videos re-copied from Cloud Storage.

### 3. Regional SSD PD
- **What it is:** An SSD persistent disk **copied to two zones** for high availability. It costs about **twice** as much and isn't faster.
- **Looks like:** `--type=pd-ssd --replica-zones=us-central1-a,us-central1-b`
- **Not to be confused with:** a faster disk.
- **Analogy:** 🗄️ Two copies of the cabinet in two buildings.
- **In the online store:** The orders DB disk.

### 🔗 How they fit together
```
 350 GB pd-ssd  → ~168 MB/s read (throttled) ❌
 1 TB pd-ssd    → ~480 MB/s, ~3x the cost of 350 GB (A)
 Local SSD NVMe → GB/s range, cheaper per GB, data temporary (C) ✅ max throughput, low cost
 Regional SSD   → same speed, ~2x cost ❌
```

---

## 🌍 Real-World Scenario

A media app reads large video files and keeps hitting the disk's read limit. Moving the working files to **Local SSD**, and re-copying them from Cloud Storage at startup, gives many times more throughput at a lower price per GB.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Increase the size of the disk to 1 TB.

**Wrong words:**
- ✔️ A bigger SSD PD does raise throughput.
- ❌ "**Increase the size of the disk to 1 TB**": you pay for about 3× the storage, and it's still far slower than Local SSD. Not the "maximum" at "minimum cost".

📌 **When to use it:** Use it when the data must survive restarts and you need a moderate speed boost.
🏢 **Office example:** Buying a much bigger filing cabinet just to get a wider drawer.

### ❌ B
> **B.** Increase the allocated CPU to the instance.

**Wrong words:**
- ❌ "**Increase the allocated CPU**": more vCPUs raise the cap a little, but the **350 GB size** is the limit here. It also adds CPU cost without fixing the bottleneck.

📌 **When to use it:** Use it when the app itself is short on processing power.
🏢 **Office example:** Hiring more clerks when the problem is the narrow drawer.

### ✅ C
> **C.** Migrate to use a Local SSD on the instance.

**Why it's correct:**
- ✔️ "**Local SSD**" matches "**maximum amount of throughput**": attached directly to the host, it is much faster than persistent disk.
- ✔️ "**Local SSD**" matches "**minimizing costs**": cheaper per GB than SSD persistent disk.
- ✔️ "**Migrate to use a Local SSD**" matches "**primarily reads large files**": heavy reads of files that can be re-copied fit Local SSD's speed (its data is temporary).

📌 **When to use it:** Use it when a job needs the fastest workspace and the files can be brought back if lost.
🏢 **Office example:** Working on papers spread on your desk instead of fetching them from the cabinet each time.

### ❌ D
> **D.** Migrate to use a Regional SSD on the instance.

**Wrong words:**
- ❌ "**Regional SSD**": it copies the disk to two zones for availability, which costs about **twice** as much and isn't faster.

📌 **When to use it:** Use it when the disk must survive a whole zone failing.
🏢 **Office example:** Keeping two copies of the cabinet in two buildings to make reading faster: it doesn't.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's video transcoder reads 2–5 GB source files. On a 350 GB pd-ssd it's throttled at about 170 MB/s. ShopNow moves the working set to **2× Local SSD (NVMe)**, copies sources from `gs://shopnow-media` at start, and reads at multiple GB/s. Results are written back to Cloud Storage.

---

## 🧠 Key Takeaways / Memory Tips

- **PD speed grows with size** (bigger disk = faster).
- **Maximum throughput, cheap per GB → Local SSD** (temporary data).
- Regional PD = availability, not speed.
  🧠 *"**Fastest and cheapest per GB: Local SSD. Just don't keep the only copy there.**"*
- Related: **Q077** (local SSD vs PD in the calculator), **Q112** (snapshots).

# Q322: Move Old Video Files On-Prem to Cloud Storage While Controlling Bandwidth (Storage Transfer Service)

**Topic:** Data transfer (Storage Transfer Service vs Transfer Appliance)

## ❓ Question
> Your digital media company stores a large number of video files on-premises. Each video file ranges from 100 MB to 100 GB. You are currently storing 150 TB of video data in your on-premises network, with no room for expansion. You need to migrate all infrequently accessed video files older than one year to Cloud Storage to ensure that on-premises storage remains available for new files. You must also minimize costs and control bandwidth usage. What should you do?
>
> **A.** Use Storage Transfer Service to move the data from the selected on-premises file storage systems to a Cloud Storage bucket.
>
> **B.** Use Transfer Appliance to request an appliance. Load the data locally, and ship the appliance back to Google for ingestion into Cloud Storage.
>
> **C.** Set up a Cloud Interconnect connection between the on-premises network and Google Cloud. Establish a private endpoint for Filestore access. Transfer the data from the existing Network File System (NFS) to Filestore.
>
> **D.** Create a Cloud Storage bucket. Establish an Identity and Access Management (IAM) role with write permissions to the bucket. Use the gsutil tool to directly copy files over the network to Cloud Storage.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **A**. Some pick **B** (Transfer Appliance) because 150 TB is large. The deciding clues are "**control bandwidth usage**" (Storage Transfer Service lets you set bandwidth limits) and "**selected**" files older than a year. Without a known slow link, A fits best.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A media company stores 150 TB of video files on-premises (each 100 MB to 100 GB), and local storage is full.
- **What you must achieve:** Move rarely used videos older than one year to Cloud Storage.
- **The limits:** Keep costs low and control how much network bandwidth the transfer uses.
- **What they're really asking:** Which transfer method moves the files while letting you limit bandwidth?

**Clues in the question:**
- "**control bandwidth usage**" → **Storage Transfer Service for on-premises data** (agents, bandwidth limits, filters, scheduling).

**Exam topic:** Data transfer.

---

## 📚 Key Terms Explained

### 1. Storage Transfer Service (on-premises) 🔑
- **What it is:** Managed transfers from on-prem file systems to Cloud Storage via agents you run; supports bandwidth caps, filters and schedules.
- **Looks like:** `gcloud transfer jobs create posix:///videos/archive gs://media-archive --source-agent-pool=pool1` + bandwidth limit 500 Mbps
- **Not to be confused with:** Transfer Appliance (physical device).
- **Analogy:** 🚚 A scheduled moving service that drives slowly at night.
- **In the online store:** Old product videos to Archive.

### 2. Transfer Appliance
- **What it is:** A rugged storage device Google ships to you; you load data and ship it back.
- **Looks like:** Order 300 TB appliance → copy → ship
- **Not to be confused with:** online transfer.
- **Analogy:** 📦 A shipping container you fill and send.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem NFS → STS agents (bandwidth cap) → gs://archive ✅
```

---

## 🌍 Real-World Scenario

A media company runs **Storage Transfer Service** agents to move videos older than a year, capping bandwidth so editors aren't affected.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use Storage Transfer Service to move the data from the selected on-premises file storage systems to a Cloud Storage bucket.

**Why it's correct:**
- ✔️ "**Storage Transfer Service**" matches "**control bandwidth usage**" + "**minimize costs**" (managed, no custom tooling).
- ✔️ "**from the selected on-premises file storage systems**" matches "**infrequently accessed video files older than one year**".

📌 **When to use it:** Use it when you move lots of files over your own line and need to keep the line usable for others.
🏢 **Office example:** A moving company that works at night and keeps one lane open for daily traffic.

### ❌ B
> **B.** Use Transfer Appliance to request an appliance. Load the data locally, and ship the appliance back to Google for ingestion into Cloud Storage.

**Wrong words:**
- ✔️ Good for very large data on slow links.
- ❌ No bandwidth control is needed or offered; shipping takes weeks and costs appliance fees.

📌 **When to use it:** Use it when the internet line is too slow to move the data in reasonable time.
🏢 **Office example:** Filling a shipping container and mailing it.

### ❌ C
> **C.** Set up a Cloud Interconnect connection between the on-premises network and Google Cloud. Establish a private endpoint for Filestore access. Transfer the data from the existing Network File System (NFS) to Filestore.

**Wrong words:**
- ❌ "**Cloud Interconnect … Filestore**": expensive, and the goal is Cloud Storage, not Filestore.

📌 **When to use it:** Use Interconnect for ongoing high-bandwidth hybrid needs.
🏢 **Office example:** Building a private highway to move boxes once.

### ❌ D
> **D.** Create a Cloud Storage bucket. Establish an Identity and Access Management (IAM) role with write permissions to the bucket. Use the gsutil tool to directly copy files over the network to Cloud Storage.

**Wrong words:**
- ❌ "**gsutil tool to directly copy**": manual, hard to resume/monitor at 150 TB.

📌 **When to use it:** Use gsutil/gcloud storage for small, one-off copies.
🏢 **Office example:** Carrying boxes yourself.

---

## 🛒 E-Commerce Full-Stack Example

STS job: `/mnt/videos/` (mtime > 365 days) → `gs://shopnow-video-archive`, bandwidth 300 Mbps.

---

## 🧠 Key Takeaways / Memory Tips

- **Online on-prem transfer with bandwidth control → Storage Transfer Service.** Too slow online → Transfer Appliance.
  🧠 *"**Throttle with STS; ship with Appliance.**"*
- Related: **Q196**, **Q140**.

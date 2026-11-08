# Q271: Back Up the Whole Disk Daily, Keep 7 Days, Minimal Setup (Scheduled Snapshots With 7-Day Retention)

**Topic:** Compute Engine (snapshot schedules)

## ❓ Question
> Your company is running a critical workload on a single Compute Engine VM instance. Your company's disaster recovery policies require you to back up the entire instance's disk data every day. The backups must be retained for 7 days. You must configure a backup solution that complies with your company's security policies and requires minimal setup and configuration. What should you do?
>
> **A.** Configure the instance to use persistent disk asynchronous replication.
>
> **B.** Configure daily scheduled persistent disk snapshots with a retention period of 7 days.
>
> **C.** Configure Cloud Scheduler to trigger a Cloud Function each day that creates a new machine image and deletes machine images that are older than 7 days.
>
> **D.** Configure a bash script using gsutil to run daily through a cron job. Copy the disk's files to a Cloud Storage bucket with archive storage class and an object lifecycle rule to delete the objects after 7 days.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A critical workload runs on one Compute Engine VM.
- **What you must achieve:** Back up all the VM's disk data every day and keep backups 7 days.
- **The limits:** Must meet security policies with minimal setup.
- **What they're really asking:** What is the simplest way to schedule daily backups kept for 7 days?

**Clues in the question:**
- "**back up … disk data every day**" + "**retained for 7 days**" + "**minimal setup**" → **snapshot schedule** with 7-day retention.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Snapshot schedule 🔑 (review from Q144)
- **What it is:** A resource policy that snapshots a disk on a schedule and auto-deletes old ones.
- **Looks like:** `gcloud compute resource-policies create snapshot-schedule daily7 --daily-schedule --start-time=02:00 --max-retention-days=7`
- **Not to be confused with:** async replication.
- **Analogy:** 📸 Automatic daily photocopy, shredded after a week.
- **In the online store:** Orders VM disk.

### 2. PD asynchronous replication
- **What it is:** Continuously copies a disk to another region for disaster recovery. Not daily backups with retention.
- **Looks like:** —
- **Not to be confused with:** snapshots.
- **Analogy:** 📡 A live mirror in another city.
- **In the online store:** —

### 🔗 How they fit together
```
 disk ─ daily snapshot 02:00 ─► keep 7 → oldest auto-deleted ✅
```

---

## 🌍 Real-World Scenario

A critical single VM gets a **snapshot schedule**: one snapshot every night, each kept for 7 days.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure the instance to use persistent disk asynchronous replication.

**Wrong words:**
- ❌ "**persistent disk asynchronous replication**": a live copy in another region, not daily point-in-time backups kept 7 days.

📌 **When to use it:** Use it for cross-region disaster recovery with low data loss.
🏢 **Office example:** A live mirror office instead of daily photocopies.

### ✅ B
> **B.** Configure daily scheduled persistent disk snapshots with a retention period of 7 days.

**Why it's correct:**
- ✔️ "**daily scheduled persistent disk snapshots**" matches "**back up the entire instance's disk data every day**".
- ✔️ "**retention period of 7 days**" matches "**retained for 7 days**"; built in, which matches "**minimal setup**".

📌 **When to use it:** Use it when you need automatic daily copies kept for a fixed time.
🏢 **Office example:** An automatic nightly photocopy of the ledger, with copies older than a week shredded.

### ❌ C
> **C.** Configure Cloud Scheduler to trigger a Cloud Function each day that creates a new machine image and deletes machine images that are older than 7 days.

**Wrong words:**
- ❌ "**Cloud Scheduler … Cloud Function … machine image**": custom code to maintain.

📌 **When to use it:** Use machine images to clone a whole VM config.
🏢 **Office example:** Hiring a clerk to do what the copier does automatically.

### ❌ D
> **D.** Configure a bash script using gsutil to run daily through a cron job. Copy the disk's files to a Cloud Storage bucket with archive storage class and an object lifecycle rule to delete the objects after 7 days.

**Wrong words:**
- ❌ "**bash script using gsutil … cron**": copies files, not a consistent disk backup; custom work.

📌 **When to use it:** Use file-level copies for specific folders.
🏢 **Office example:** Copying a few papers by hand instead of photocopying the whole binder.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute disks add-resource-policies orders-disk --resource-policies=daily7 --zone=us-central1-a`

---

## 🧠 Key Takeaways / Memory Tips

- **Daily disk backups with retention → snapshot schedule.**
  🧠 *"**Schedule it, keep 7.**"*
- Related: **Q144**, **Q234**.

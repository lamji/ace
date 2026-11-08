# Q112: Regular Boot Disk Backups With Fast Restore and Auto-Cleanup (Snapshot Schedule)

**Topic:** Compute Engine (snapshot schedules, retention, images, instance templates)

## ❓ Question
> You have a workload running on Compute Engine that is critical to your business. You want to ensure that the data on the boot disk of this workload is backed up regularly. You need to be able to restore a backup as quickly as possible in case of disaster. You also want older backups to be cleaned automatically to save on cost. You want to follow Google-recommended practices. What should you do?
>
> **A.** Create a Cloud Function to create an instance template.
>
> **B.** Create a snapshot schedule for the disk using the desired interval.
>
> **C.** Create a cron job to create a new disk from the disk using gcloud.
>
> **D.** Create a Cloud Task to create an image and export it to Cloud Storage.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A business-critical VM's boot disk (the disk holding the operating system) must be backed up regularly.
- **What you must achieve:** Regular backups that can be restored quickly.
- **The limits:** Old backups must be deleted automatically; follow recommended practice.
- **What they're really asking:** How do you schedule boot-disk backups with automatic cleanup?

**Clues in the question:**
- "**backed up regularly**": a **schedule**.
- "**restore … quickly**": a disk snapshot can be turned into a new disk in minutes.
- "**older backups to be cleaned automatically**": snapshot schedules have a **retention policy** (e.g., keep 14 days).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Snapshot
- **What it is:** A **backup copy of a persistent disk** at a point in time. Incremental: only changed blocks are stored after the first one.
- **Looks like:** `gcloud compute disks snapshot orders-vm --zone=us-central1-a`
- **Not to be confused with:** an image (made for creating many VMs).
- **Analogy:** 📸 A **photocopy** of the filing cabinet.
- **In the online store:** Nightly copy of the orders VM disk.

### 2. Snapshot schedule 🔑
- **What it is:** A **resource policy** attached to a disk that **takes snapshots automatically** at an interval and **deletes old ones** after a retention period.
- **Looks like:** `gcloud compute resource-policies create snapshot-schedule daily-14 --region=us-central1 --daily-schedule --start-time=02:00 --max-retention-days=14`
- **Not to be confused with:** a cron job you run yourself.
- **Analogy:** 🗓️ An office policy: **photocopy the cabinet every night, shred copies older than 2 weeks**.
- **In the online store:** The orders VM is backed up daily, keeping 14 days.

### 3. Instance template / image
- **What it is:** A template = **settings for creating VMs** (no data backup). An image = a disk copy mainly for **creating new VMs**.
- **Looks like:** `gcloud compute instance-templates create ...`
- **Not to be confused with:** a regular backup.
- **Analogy:** 📝 A form for setting up new desks.
- **In the online store:** Used for the web MIG.

### 🔗 How they fit together
```
 boot disk ── attached policy: daily 02:00, keep 14 days ✅
   snapshots: day1 … day14 → day15 created, day1 auto-deleted
   disaster → gcloud compute disks create --source-snapshot=… → new VM in minutes
```

---

## 🌍 Real-World Scenario

A company's billing server runs on one VM. The admin attaches a **snapshot schedule** to its boot disk: every 4 hours, keep 7 days. When a bad update corrupts the disk, they create a new disk from the latest snapshot and are back online in minutes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Function to create an instance template.

**Wrong words:**
- ❌ "**create an instance template**": a template stores VM **settings**, not the disk's **data**. It's no backup.
- ❌ "**Cloud Function**": custom code you'd have to maintain.

📌 **When to use it:** Use instance templates to create identical VMs, for example in a managed instance group.
🏢 **Office example:** Saving the form for setting up a desk, but not copying the files in it.

### ✅ B
> **B.** Create a snapshot schedule for the disk using the desired interval.

**Why it's correct:**
- ✔️ "**snapshot schedule**" matches "**backed up regularly**": snapshots are taken automatically at the interval.
- ✔️ "**snapshot**" matches "**restore a backup as quickly as possible**": a new disk is created from a snapshot in minutes.
- ✔️ "**schedule**" (with retention) matches "**older backups to be cleaned automatically**": old snapshots are deleted after the retention period.
- ✔️ It's built into Compute Engine, which matches "**Google-recommended practices**".

📌 **When to use it:** Use it when something important must be copied on a timetable and old copies thrown away automatically.
🏢 **Office example:** A nightly photocopy of the cabinet, with copies older than two weeks shredded automatically.

### ❌ C
> **C.** Create a cron job to create a new disk from the disk using gcloud.

**Wrong words:**
- ❌ "**cron job … create a new disk from the disk**": full disk copies cost more than incremental snapshots, there's no automatic cleanup, and you maintain the cron yourself.

📌 **When to use it:** Use a disk clone when you need a one-off copy for testing.
🏢 **Office example:** Photocopying the whole cabinet by hand every night and never throwing old copies away.

### ❌ D
> **D.** Create a Cloud Task to create an image and export it to Cloud Storage.

**Wrong words:**
- ❌ "**create an image and export it to Cloud Storage**": exported images are slow to restore (they must be imported again) and aren't cleaned up automatically.
- ❌ "**Cloud Task**": custom work.

📌 **When to use it:** Use image export when moving a disk to another system or keeping a long-term archive.
🏢 **Office example:** Shipping a copy to a far-away warehouse: safe, but slow to get back.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute resource-policies create snapshot-schedule orders-daily \
  --region=us-central1 --daily-schedule --start-time=02:00 --max-retention-days=14
gcloud compute disks add-resource-policies orders-vm --zone=us-central1-a --resource-policies=orders-daily
```
On Friday the orders VM's disk breaks. The team runs `gcloud compute disks create orders-restore --source-snapshot=<Friday 02:00 snapshot>` and attaches it to a new VM. They're back in about 5 minutes.

---

## 🧠 Key Takeaways / Memory Tips

- **Regular disk backups + auto-cleanup → snapshot schedule with retention.**
- Templates aren't backups. Image export is slow to restore.
  🧠 *"**Schedule the snapshots, let retention clean up.**"*
- Related: **Q077** (snapshot storage costs), **Q057** (instance templates).

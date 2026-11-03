# Q144: Daily Backups Kept 30 Days With the Least Overhead (Snapshot Schedule on the Disk)

**Topic:** Compute Engine (snapshot schedules, retention)

## ❓ Question
> You have a Compute Engine instance hosting an application used between 9 AM and 6 PM on weekdays. You want to back up this instance daily for disaster recovery purposes. You want to keep the backups for 30 days. You want the Google-recommended solution with the least management overhead and the least number of services. What should you do?
>
> **A.** 1. Update your instances' metadata to add the following value: snapshot-schedule: 0 1 * * * 2. Update your instances' metadata to add the following value: snapshot-retention: 30
>
> **B.** 1. In the Cloud Console, go to the Compute Engine Disks page and select your instance's disk. 2. In the Snapshot Schedule section, select Create Schedule and configure the following parameters: - Schedule frequency: Daily - Start time: 1:00 AM - 2:00 AM - Autodelete snapshots after: 30 days
>
> **C.** 1. Create a Cloud Function that creates a snapshot of your instance's disk. 2. Create a Cloud Function that deletes snapshots that are older than 30 days. 3. Use Cloud Scheduler to trigger both Cloud Functions daily at 1:00 AM.
>
> **D.** 1. Create a bash script in the instance that copies the content of the disk to Cloud Storage. 2. Create a bash script in the instance that deletes data older than 30 days in the backup Cloud Storage bucket. 3. Configure the instance's crontab to execute these scripts daily at 1:00 AM.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Daily backups, kept **30 days**, with the **least work** and **fewest services**.

**Clues in the question:**
- "**daily**" + "**keep … 30 days**": a **snapshot schedule** with daily frequency and **autodelete after 30 days**.
- "**least management overhead … least number of services**": built into Compute Engine, with no functions or scripts.
- Start at **1–2 AM**, outside the 9–6 usage hours.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Snapshot schedule (review from Q112) 🔑
- **What it is:** A disk policy that **takes snapshots automatically** and **deletes old ones** after the retention period.
- **Looks like:** Disks → disk → Snapshot schedule → Daily, 1–2 AM, autodelete after 30 days
- **Not to be confused with:** metadata keys.
- **Analogy:** 🗓️ Office policy: photocopy every night, shred copies after 30 days.
- **In the online store:** The orders VM is backed up nightly.

### 2. Instance metadata
- **What it is:** Key-value settings on a VM, read by scripts and the guest OS. There's **no** `snapshot-schedule` metadata key.
- **Looks like:** `startup-script`, `enable-oslogin`
- **Not to be confused with:** a snapshot policy.
- **Analogy:** 📝 A note stuck on the computer.
- **In the online store:** OS Login settings.

### 🔗 How they fit together
```
 disk ── snapshot schedule: daily 01:00–02:00, autodelete 30 days ✅
 (no Cloud Functions, no Scheduler, no cron scripts)
```

---

## 🌍 Real-World Scenario

An office app runs weekdays 9–6. The admin opens the disk in the console, creates a **daily snapshot schedule** at 1 AM with **30-day autodelete**, and is done.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Update your instances' metadata to add the following value: snapshot-schedule: 0 1 * * * 2. Update your instances' metadata to add the following value: snapshot-retention: 30

**Wrong words:**
- ❌ "**metadata … snapshot-schedule: 0 1 * * ***": no such metadata key exists. Compute Engine ignores it.

📌 **When to use it:** Use metadata for things like startup scripts and OS Login.
🏢 **Office example:** Writing "back me up at 1 AM" on a sticky note nobody reads.

### ✅ B
> **B.** 1. In the Cloud Console, go to the Compute Engine Disks page and select your instance's disk. 2. In the Snapshot Schedule section, select Create Schedule and configure the following parameters: - Schedule frequency: Daily - Start time: 1:00 AM - 2:00 AM - Autodelete snapshots after: 30 days

**Why it's correct:**
- ✔️ "**Snapshot Schedule … Schedule frequency: Daily**" matches "**back up this instance daily**".
- ✔️ "**Autodelete snapshots after: 30 days**" matches "**keep the backups for 30 days**".
- ✔️ It's built into Compute Engine, which matches "**least management overhead and the least number of services**".
- ✔️ "**1:00 AM - 2:00 AM**" is outside "**9 AM and 6 PM**" usage.

📌 **When to use it:** Use it when something needs copying every night, with old copies cleared out automatically.
🏢 **Office example:** A nightly photocopy policy that shreds copies after 30 days.

### ❌ C
> **C.** 1. Create a Cloud Function that creates a snapshot of your instance's disk. 2. Create a Cloud Function that deletes snapshots that are older than 30 days. 3. Use Cloud Scheduler to trigger both Cloud Functions daily at 1:00 AM.

**Wrong words:**
- ❌ "**Cloud Function … Cloud Function … Cloud Scheduler**": three extra services and custom code to maintain.

📌 **When to use it:** Use it only when you need custom backup logic.
🏢 **Office example:** Hiring two robots and an alarm clock to do what a policy already does.

### ❌ D
> **D.** 1. Create a bash script in the instance that copies the content of the disk to Cloud Storage. 2. Create a bash script in the instance that deletes data older than 30 days in the backup Cloud Storage bucket. 3. Configure the instance's crontab to execute these scripts daily at 1:00 AM.

**Wrong words:**
- ❌ "**bash script … copies the content of the disk to Cloud Storage … crontab**": homemade, slow to restore, and it runs on the VM itself (if the VM dies, so do the backups).

📌 **When to use it:** Use file-level copies for specific folders you want in a bucket.
🏢 **Office example:** An employee photocopying files by hand every night.

---

## 🛒 E-Commerce Full-Stack Example

Console: **Compute Engine → Disks → shop-office-1 → Create snapshot schedule** → Daily, 01:00–02:00, delete after 30 days. Restore: create a disk from the snapshot of the day you need.

---

## 🧠 Key Takeaways / Memory Tips

- **Daily backups + retention, least effort → snapshot schedule** (built in).
- No metadata key for snapshots.
  🧠 *"**Schedule it, autodelete it.**"*
- Related: **Q112** (snapshot schedule), **Q131** (images).

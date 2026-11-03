# Q234: Data Immediately Available After a Zone Failure (Regional Persistent Disk, Attach to an Instance in the Other Zone)

**Topic:** Compute Engine (regional persistent disks)

## ❓ Question
> You are migrating a business critical application from your local data center into Google Cloud. As part of your high-availability strategy, you want to ensure that any data used by the application will be immediately available if a zonal failure occurs. What should you do?
>
> **A.** Store the application data on a zonal persistent disk. Create a snapshot schedule for the disk. If an outage occurs, create a new disk from the most recent snapshot and attach it to a new VM in another zone.
>
> **B.** Store the application data on a zonal persistent disk. If an outage occurs, create an instance in another zone with this disk attached.
>
> **C.** Store the application data on a regional persistent disk. Create a snapshot schedule for the disk. If an outage occurs, create a new disk from the most recent snapshot and attach it to a new VM in another zone.
>
> **D.** Store the application data on a regional persistent disk. If an outage occurs, create an instance in another zone with this disk attached.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Data must be **immediately available** if a **zone** fails.

**Clues in the question:**
- "**immediately available if a zonal failure occurs**" → **regional persistent disk** (synchronously copied to two zones).
- Attach that same disk to a VM in the **other zone**: no restore, no data loss.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Regional persistent disk 🔑
- **What it is:** A disk whose data is **synchronously copied to two zones** in a region. If one zone fails, attach it in the other.
- **Looks like:** `gcloud compute disks create data --region=us-central1 --replica-zones=us-central1-a,us-central1-b`
- **Not to be confused with:** zonal disk; snapshot.
- **Analogy:** 📑 Every page written in two filing cabinets in two buildings at once.
- **In the online store:** Order DB disk.

### 2. Snapshot
- **What it is:** A point-in-time backup. Restoring takes time and loses changes since it was taken.
- **Looks like:** —
- **Not to be confused with:** live replica.
- **Analogy:** 📸 Yesterday's photocopy.
- **In the online store:** —

### 🔗 How they fit together
```
 regional PD (zone a + zone b) ── zone a fails ── force-attach to VM in zone b ✅ (no data loss)
```

---

## 🌍 Real-World Scenario

A critical app stores data on a **regional PD**. When zone A goes down, the team starts a VM in zone B and attaches the same disk. Data is current.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Store the application data on a zonal persistent disk. Create a snapshot schedule for the disk. If an outage occurs, create a new disk from the most recent snapshot and attach it to a new VM in another zone.

**Wrong words:**
- ❌ "**zonal persistent disk**": lives in one zone.
- ❌ "**create a new disk from the most recent snapshot**": takes time and loses recent data. Not immediate.

📌 **When to use it:** Use snapshots for backups and recovery from mistakes.
🏢 **Office example:** Rebuilding the files from yesterday's photocopy.

### ❌ B
> **B.** Store the application data on a zonal persistent disk. If an outage occurs, create an instance in another zone with this disk attached.

**Wrong words:**
- ❌ "**zonal persistent disk … create an instance in another zone with this disk attached**": a zonal disk can't be attached in another zone, and it's unreachable during the outage.

📌 **When to use it:** Use zonal disks for normal, non-critical data.
🏢 **Office example:** Trying to open a cabinet locked inside a closed building.

### ❌ C
> **C.** Store the application data on a regional persistent disk. Create a snapshot schedule for the disk. If an outage occurs, create a new disk from the most recent snapshot and attach it to a new VM in another zone.

**Wrong words:**
- ✔️ "regional persistent disk" is right.
- ❌ "**create a new disk from the most recent snapshot**": unnecessary and slower; you lose recent data.

📌 **When to use it:** Use snapshots as an extra backup, not for failover.
🏢 **Office example:** Owning a twin cabinet but restoring from yesterday's photocopy.

### ✅ D
> **D.** Store the application data on a regional persistent disk. If an outage occurs, create an instance in another zone with this disk attached.

**Why it's correct:**
- ✔️ "**regional persistent disk**" matches "**immediately available if a zonal failure occurs**": data is already in the second zone.
- ✔️ "**create an instance in another zone with this disk attached**": the same, up-to-date disk is used.

📌 **When to use it:** Use it when important records must survive one building going dark with nothing lost.
🏢 **Office example:** Every page written in two buildings at once, so if one closes you keep working in the other.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instances attach-disk orders-vm-b --disk=orders-data --disk-scope=regional --force-attach --zone=us-central1-b`

---

## 🧠 Key Takeaways / Memory Tips

- **Immediate data after zone failure → regional persistent disk.** Snapshots = slower, lose recent data.
  🧠 *"**Two zones, one disk.**"*
- Related: **Q147**, **Q144**.

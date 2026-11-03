# Q281: Single VM Needs the Fastest Disk and Must Recover on Failure (Hyperdisk Extreme in a Stateful MIG)

**Topic:** Compute Engine (Hyperdisk, stateful MIGs)

## ❓ Question
> You need to deploy a third-party software application onto a single Compute Engine VM instance. The application requires the highest speed read and write disk access for the internal database. You need to ensure the instance will recover on failure. What should you do?
>
> **A.** Create an instance template. Set the disk type to be an SSD Persistent Disk. Launch the instance template as part of a stateful managed instance group.
>
> **B.** Create an instance template. Set the disk type to be an SSD Persistent Disk. Launch the instance template as part of a stateless managed instance group.
>
> **C.** Create an instance template. Set the disk type to be Hyperdisk Extreme. Launch the instance template as part of a stateful managed instance group.
>
> **D.** Create an instance template. Set the disk type to be Hyperdisk Extreme. Launch the instance template as part of a stateless managed instance group.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Fastest** disk, one VM with a database, **recovers** if it fails.

**Clues in the question:**
- "**highest speed read and write disk access**" → **Hyperdisk Extreme** (higher IOPS than SSD PD).
- "**internal database**" + "**recover on failure**" → **stateful MIG** (autohealing recreates the VM and **keeps its disk**).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Hyperdisk Extreme 🔑
- **What it is:** Google's highest-performance block storage, with very high IOPS/throughput you can set.
- **Looks like:** `--create-disk=type=hyperdisk-extreme,size=500GB,provisioned-iops=100000`
- **Not to be confused with:** pd-ssd.
- **Analogy:** 🏎️ The fastest filing cabinet.
- **In the online store:** Busy DB.

### 2. Stateful MIG
- **What it is:** A MIG that preserves disks, names and IPs when it recreates a VM (autohealing).
- **Looks like:** `--stateful-disk=device-name=data,auto-delete=never`
- **Not to be confused with:** stateless MIG.
- **Analogy:** 🔁 Replacing a worker but keeping their desk and files.
- **In the online store:** —

### 🔗 How they fit together
```
 MIG size 1 (stateful, autohealing) → VM + Hyperdisk Extreme (kept on recreate) ✅
```

---

## 🌍 Real-World Scenario

A vendor database needs top disk speed. The team runs it on **Hyperdisk Extreme** in a **stateful MIG of size 1** so a failed VM is recreated with the same disk.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an instance template. Set the disk type to be an SSD Persistent Disk. Launch the instance template as part of a stateful managed instance group.

**Wrong words:**
- ✔️ Stateful MIG is right.
- ❌ "**SSD Persistent Disk**": fast, but not the highest speed.

📌 **When to use it:** Use pd-ssd for fast disks at lower cost.
🏢 **Office example:** A good cabinet, but not the fastest.

### ❌ B
> **B.** Create an instance template. Set the disk type to be an SSD Persistent Disk. Launch the instance template as part of a stateless managed instance group.

**Wrong words:**
- ❌ "**SSD Persistent Disk**" and ❌ "**stateless**": the DB disk could be lost on recreate.

📌 **When to use it:** Use stateless MIGs for web servers.
🏢 **Office example:** A replacement worker gets an empty desk.

### ✅ C
> **C.** Create an instance template. Set the disk type to be Hyperdisk Extreme. Launch the instance template as part of a stateful managed instance group.

**Why it's correct:**
- ✔️ "**Hyperdisk Extreme**" matches "**highest speed read and write disk access**".
- ✔️ "**stateful managed instance group**" matches "**recover on failure**" + "**internal database**": the VM is recreated with its data disk.

📌 **When to use it:** Use it when one important machine needs the fastest storage and must come back automatically with its data.
🏢 **Office example:** The fastest filing cabinet, and if the worker leaves, a replacement sits at the same desk with the same files.

### ❌ D
> **D.** Create an instance template. Set the disk type to be Hyperdisk Extreme. Launch the instance template as part of a stateless managed instance group.

**Wrong words:**
- ✔️ Hyperdisk Extreme is right.
- ❌ "**stateless**": recreated VMs don't keep the database disk.

📌 **When to use it:** Use stateless MIGs for apps with no local data.
🏢 **Office example:** Fast cabinet, but emptied every time someone leaves.

---

## 🛒 E-Commerce Full-Stack Example

Template `erp-db-v1` (Hyperdisk Extreme 1 TB, 150k IOPS) → stateful MIG `erp-db` size 1, autohealing health check on TCP 5432.

---

## 🧠 Key Takeaways / Memory Tips

- **Fastest disk → Hyperdisk Extreme. Recover with data → stateful MIG.**
  🧠 *"**Extreme disk, stateful group.**"*
- Related: **Q234**, **Q225**.

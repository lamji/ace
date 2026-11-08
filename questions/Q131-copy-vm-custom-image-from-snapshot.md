# Q131: Copying a Custom VM for More Traffic (Custom Image From a Snapshot, Instances From the Image)

**Topic:** Compute Engine (snapshots, custom images, creating instances)

## ❓ Question
> You need to create a copy of a custom Compute Engine virtual machine (VM) to facilitate an expected increase in application traffic due to a business acquisition. What should you do?
>
> **A.** Create a Compute Engine snapshot of your base VM. Create your images from that snapshot.
>
> **B.** Create a Compute Engine snapshot of your base VM. Create your instances from that snapshot.
>
> **C.** Create a custom Compute Engine image from a snapshot. Create your images from that image.
>
> **D.** Create a custom Compute Engine image from a snapshot. Create your instances from that image.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You have a custom VM, and traffic will increase after an acquisition.
- **What you must achieve:** Create a copy of that VM.
- **The limits:** None stated.
- **What they're really asking:** How do you duplicate the VM?

**Clues in the question:**
- "**create a copy of a custom … VM**": the goal is **new instances** (VMs), not more images.
- Google's recommended path is snapshot → **custom image** → **instances** (images are made for creating many VMs, and can go into instance templates).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Snapshot
- **What it is:** A **backup copy of one disk** at a point in time.
- **Looks like:** `gcloud compute disks snapshot base-vm`
- **Not to be confused with:** an image (made for creating many VMs).
- **Analogy:** 📸 A photocopy of one desk's papers.
- **In the online store:** Nightly backup of the API VM.

### 2. Custom image 🔑
- **What it is:** A **reusable boot-disk template** made from a disk or snapshot. Many VMs (and instance templates) can be created from it.
- **Looks like:** `gcloud compute images create shop-api-v1 --source-snapshot=base-snap`
- **Not to be confused with:** a snapshot (backup).
- **Analogy:** 🖨️ A **master copy** you print new desks from.
- **In the online store:** Every new API VM starts from `shop-api-v1`.

### 🔗 How they fit together
```
 base VM disk → snapshot → custom image ✅ → instance 1, instance 2, instance 3 … (or instance template → MIG)
```

---

## 🌍 Real-World Scenario

After an acquisition, traffic will double. The engineer snapshots the tuned VM's disk, creates a **custom image** from the snapshot, and launches new instances (or a managed instance group) from that image.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Compute Engine snapshot of your base VM. Create your images from that snapshot.

**Wrong words:**
- ✔️ "Create a Compute Engine snapshot of your base VM" is fine.
- ❌ "**Create your images from that snapshot**": the question needs **VM copies** (instances), not more images.

📌 **When to use it:** Use it when you want to make a reusable image from a backup.
🏢 **Office example:** Making a master copy but never setting up the new desks.

### ❌ B
> **B.** Create a Compute Engine snapshot of your base VM. Create your instances from that snapshot.

**Wrong words:**
- ✔️ A snapshot can create a disk for one VM.
- ❌ "**Create your instances from that snapshot**": snapshots are backups. For many identical VMs, Google recommends **images** (and they're needed for instance templates).

📌 **When to use it:** Use it to restore or clone a single VM from a backup.
🏢 **Office example:** Rebuilding each new desk from a photocopy of the old one.

### ❌ C
> **C.** Create a custom Compute Engine image from a snapshot. Create your images from that image.

**Wrong words:**
- ✔️ "custom … image from a snapshot" is right.
- ❌ "**Create your images from that image**": an image of an image gives you no running VMs.

📌 **When to use it:** Use it to copy an image to another project or family.
🏢 **Office example:** Copying the master copy again instead of setting up desks.

### ✅ D
> **D.** Create a custom Compute Engine image from a snapshot. Create your instances from that image.

**Why it's correct:**
- ✔️ "**Create a custom Compute Engine image from a snapshot**" matches "**copy of a custom … VM**": the image holds the VM's custom setup.
- ✔️ "**Create your instances from that image**" matches "**facilitate an expected increase in application traffic**": you launch as many identical VMs as you need.

📌 **When to use it:** Use it when you need many identical copies of a carefully set-up machine.
🏢 **Office example:** Making a master copy of the perfect desk setup and using it to set up every new desk.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute disks snapshot shop-api-1 --zone=us-central1-a --snapshot-names=shop-api-base
gcloud compute images create shop-api-v1 --source-snapshot=shop-api-base
gcloud compute instances create shop-api-2 shop-api-3 --image=shop-api-v1 --zone=us-central1-a
```

---

## 🧠 Key Takeaways / Memory Tips

- **Many copies of a VM → custom image → instances** (or a template + MIG).
- Snapshots = backups; images = blueprints.
  🧠 *"**Snapshot → image → instances.**"*
- Related: **Q112** (snapshot schedule), **Q057** (MIG).

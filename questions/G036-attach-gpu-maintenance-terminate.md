# G036: Add a GPU to an Existing VM: Stop It and Set Host Maintenance to Terminate (Attaching GPUs)

**Topic:** Compute Engine (attaching GPUs)
**Exam guide section:** 3.1 Managing compute resources: Attaching GPUs and TPUs

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You want to add an NVIDIA T4 GPU to an existing N1 VM that is currently running. The VM's host maintenance policy is set to live migrate. What should you do?
>
> **A.** Attach the GPU while the VM is running; no other changes are needed.
>
> **B.** Stop the VM, set its host maintenance policy to terminate, add the GPU to the VM's configuration, and start the VM.
>
> **C.** Keep the live migrate policy, and attach the GPU through a Persistent Disk.
>
> **D.** Create a snapshot of the boot disk, and attach the snapshot to a Cloud TPU.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You have a running VM (a rented computer) on the N1 machine family, and you want to add a T4 GPU (a graphics chip for AI) to it.
- **What you must achieve:** Attach the GPU to this existing VM.
- **The limits:** The VM is currently set to live migrate, meaning Google moves it to another host during maintenance without stopping it.
- **What they're really asking:** What steps must you take for a VM to have a GPU?

**Clues in the question:**
- VMs with GPUs **can't live migrate**, so the host maintenance policy must be **Terminate**.
- Changing accelerators on an existing VM requires the VM to be **stopped**.

**Exam topic:** Compute Engine operations (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. Host maintenance policy 🔑
- **What it is:** What Compute Engine does when the physical host needs maintenance: **MIGRATE** (live-move the VM, the default) or **TERMINATE** (stop it and optionally restart it). VMs with GPUs must use TERMINATE.
- **Looks like:** `gcloud compute instances set-scheduling vm-1 --maintenance-policy=TERMINATE --restart-on-failure`
- **Not to be confused with:** Spot or preemptible settings.
- **Analogy:** 🚚 "During building repairs, move my desk" vs "close my office for the day".
- **In the online store:** GPU VMs restart after host maintenance.

### 2. Attaching a GPU
- **What it is:** Adding an accelerator to a VM's configuration. On N1 you add a GPU type and count. Some families (A2, A3, G2) come with GPUs built into the machine type.
- **Looks like:** Console: stop VM → Edit → GPUs: 1× NVIDIA T4 → Save → Start
- **Not to be confused with:** Attaching a disk.
- **Analogy:** 🔌 Installing a new graphics card, which needs the computer turned off.
- **In the online store:** Adding a T4 to the image-tagging VM.

### 🔗 How they fit together
```
 Running VM (MIGRATE) ─stop─► set TERMINATE ─► add 1× T4 ─► start ✅
```

---

## 🌍 Real-World Scenario

An image-tagging service runs too slowly on CPUs. The engineer stops the VM in a quiet hour, switches maintenance to **terminate**, adds a T4, and starts it again. Tagging is 10× faster, and the VM now restarts after host maintenance instead of live-migrating.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Attach the GPU while the VM is running; no other changes are needed.

**Wrong words:**
- ❌ "**while the VM is running; no other changes**": GPUs can't be added to a running VM, and GPU VMs can't keep the live-migrate policy.

📌 **When to use it:** Never expected to work. Stop the VM first.
🏢 **Office example:** Installing a graphics card while the computer is on.

### ✅ B
> **B.** Stop the VM, set its host maintenance policy to terminate, add the GPU to the VM's configuration, and start the VM.

**Why it's correct:**
- ✔️ "**Stop the VM**": needed to change its hardware.
- ✔️ "**set its host maintenance policy to terminate**" fixes "**set to live migrate**", since GPU VMs can't live migrate.
- ✔️ "**add the GPU … and start the VM**" matches "**add an NVIDIA T4 GPU to an existing N1 VM**".

📌 **When to use it:** Use it when an existing machine needs a special chip added.
🏢 **Office example:** Turning the computer off, installing the card, setting "close office during repairs", then turning it back on.

### ❌ C
> **C.** Keep the live migrate policy, and attach the GPU through a Persistent Disk.

**Wrong words:**
- ❌ "**Keep the live migrate policy**": not allowed with GPUs.
- ❌ "**attach the GPU through a Persistent Disk**": disks store data. They can't carry a GPU.

📌 **When to use it:** Never expected to work.
🏢 **Office example:** Trying to plug a graphics card into a filing cabinet.

### ❌ D
> **D.** Create a snapshot of the boot disk, and attach the snapshot to a Cloud TPU.

**Wrong words:**
- ❌ "**attach the snapshot to a Cloud TPU**": snapshots are disk backups, and a TPU isn't a T4 GPU on your VM.

📌 **When to use it:** Use snapshots to back up or copy disks.
🏢 **Office example:** Photocopying the hard drive to a different machine.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `img-tagger` (n1-standard-8): stop → `--maintenance-policy=TERMINATE` → add 1× `nvidia-tesla-t4` → start. The NVIDIA driver is installed on first boot.

---

## 🧠 Key Takeaways / Memory Tips

- **GPU VM → stop to change, host maintenance = TERMINATE (no live migration).**
  🧠 *"**GPUs don't migrate; they terminate.**"*
- Related: **G034**, **G035**, **G006**.

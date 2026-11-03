# Q089: Migrating an App That Needs 96 vCPUs (Machine Type n1-standard-96)

**Topic:** Compute Engine (machine types, vCPUs, CPU platform, rightsizing)

## ❓ Question
> You are migrating a production-critical on-premises application that requires 96 vCPUs to perform its task. You want to make sure the application runs in a similar environment on GCP. What should you do?
>
> **A.** When creating the VM, use machine type n1-standard-96.
>
> **B.** When creating the VM, use Intel Skylake as the CPU platform.
>
> **C.** Create the VM using Compute Engine default settings. Use gcloud to modify the running instance to have 96 vCPUs.
>
> **D.** Start the VM using Compute Engine default settings, and adjust as you go based on Rightsizing Recommendations.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The app **needs 96 vCPUs** and is **production-critical**. How do you make sure the new VM has that from day one?

**Clues in the question:**
- "**requires 96 vCPUs**": pick a **machine type with 96 vCPUs**. The number at the end of `n1-standard-96` is the vCPU count.
- "**production-critical**" + "**similar environment**": get it right **at creation**. Don't start small and fix it later.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1️⃣ vCPU
- **What it is:** A **virtual CPU**, one processing thread a VM can use. More vCPUs = more work done at the same time.
- **Looks like:** `n1-standard-96` → 96 vCPUs, 360 GB memory
- **Analogy:** 👷 The **number of workers** at a desk.

### 2️⃣ Machine type 🔑
- **What it is:** A **named VM size**: family + type + vCPU count. `n1-standard-96` = N1 family, standard memory ratio (3.75 GB per vCPU), **96 vCPUs**.
- **Looks like:** `gcloud compute instances create erp-1 --machine-type=n1-standard-96 --zone=us-central1-a`
- **Not to be confused with:** the CPU platform (which chip generation runs it).
- **Analogy:** 🏢 Choosing an **office with 96 desks**.
- **In the online store:** A big batch reporting server.

### 3️⃣ CPU platform (e.g., Intel Skylake)
- **What it is:** The **minimum processor generation** for the VM. It changes **which chip** you get, not **how many** vCPUs.
- **Looks like:** `--min-cpu-platform="Intel Skylake"`
- **Not to be confused with:** the machine type. Skylake doesn't mean 96 vCPUs.
- **Analogy:** 🖥️ Asking for **newer-model computers**, without saying how many desks.

### 4️⃣ Default settings / Rightsizing recommendations
- **Default settings:** the console's default is a small VM (e.g., `e2-medium`, 2 vCPUs).
- **Rightsizing recommendations:** Google's **suggestions after watching usage** for a while (e.g., "this VM could be smaller"). They come later, not on day one.
- **Changing machine type:** needs the VM to be **stopped** first; you can't change it while running.

### 🔗 How they fit together
```
 need: 96 vCPUs, production-critical
   ✅ create with --machine-type=n1-standard-96 (96 vCPUs from day one)
   ❌ Skylake platform (chip model, not count)
   ❌ default (2 vCPUs) then change while running (must stop it)
   ❌ default, wait for recommendations (too slow, prod suffers)
```

---

## 🌍 Real-World Scenario

A company moves its main ERP server, which runs on a 96-core machine, to Google Cloud. To avoid slowdowns on launch day, the engineer creates the VM with a **96-vCPU machine type** right away, so the app gets the same power it had on-premises.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** When creating the VM, use machine type n1-standard-96.

**Why it's correct:**
- ✔️ "**n1-standard-96**" matches "**requires 96 vCPUs**": the "96" means 96 vCPUs.
- ✔️ "**When creating the VM**" matches "**production-critical**": the VM has the right size from the start, with no restart or resize later.
- ✔️ "**machine type**" matches "**runs in a similar environment**": the same CPU count as on-premises.

📌 **When to use it:** Use it when you know exactly how much power a job needs and it must be ready on day one.
🏢 **Office example:** Renting an office with 96 desks because the team has 96 people starting Monday.

### ❌ B
> **B.** When creating the VM, use Intel Skylake as the CPU platform.

**Wrong words:**
- ❌ "**use Intel Skylake as the CPU platform**": this picks the processor **model**, not the **number** of vCPUs. The VM could still have 2 vCPUs.

📌 **When to use it:** Use it when the app needs features of a newer processor generation.
🏢 **Office example:** Asking for newer computers without saying you need 96 desks.

### ❌ C
> **C.** Create the VM using Compute Engine default settings. Use gcloud to modify the running instance to have 96 vCPUs.

**Wrong words:**
- ❌ "**Compute Engine default settings**": a small VM (about 2 vCPUs) at first.
- ❌ "**modify the running instance**": you can't change the machine type while the VM is running. You must stop it first, which means downtime for a production app.

📌 **When to use it:** Resize (after stopping) when a VM turns out to be too small or too big.
🏢 **Office example:** Renting a 2-desk office for 96 people, then trying to knock down walls while everyone works.

### ❌ D
> **D.** Start the VM using Compute Engine default settings, and adjust as you go based on Rightsizing Recommendations.

**Wrong words:**
- ❌ "**default settings**": too small for a 96-vCPU app.
- ❌ "**adjust as you go based on Rightsizing Recommendations**": recommendations need days of usage data. Meanwhile the production app is slow.

📌 **When to use it:** Use rightsizing to fine-tune VMs that are already running and whose needs you're not sure about.
🏢 **Office example:** Letting facilities suggest a better office size after a month of watching how many desks are used.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow moves its nightly inventory-forecast job from a 96-core server in its data center.

```bash
gcloud compute instances create forecast-1 \
  --zone=us-central1-a --machine-type=n1-standard-96
```
The job finishes in the same 2 hours it took on-premises. (Today you might pick `n2-standard-96` or `c3-standard-88`, but the idea is the same: choose a machine type with the needed vCPUs at creation.)

---

## 🧠 Key Takeaways / Memory Tips

- **"Needs N vCPUs" → machine type ending in N** (e.g., `n1-standard-96`), set when creating the VM.
- **CPU platform = which chip, not how many.**
- Changing machine type requires **stopping** the VM.
  🧠 *"**The number at the end is the number of vCPUs.**"*
- Related: **Q049** (machine sizes), **Q062** (custom machine types).

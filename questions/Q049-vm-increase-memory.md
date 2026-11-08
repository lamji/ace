# Q049: Giving a VM More Memory (Stop → Increase Memory → Start)

**Topic:** Compute Engine (machine types, custom machine types, changing memory, live migration, metadata)

## ❓ Question
> You have a virtual machine that is currently configured with 2 vCPUs and 4 GB of memory. It is running out of memory. You want to upgrade the virtual machine to have 8 GB of memory. What should you do?
>
> **A.** Rely on live migration to move the workload to a machine with more memory.
>
> **B.** Use gcloud to add metadata to the VM. Set the key to required-memory-size and the value to 8 GB.
>
> **C.** Stop the VM, change the machine type to n1-standard-8, and start the VM.
>
> **D.** Stop the VM, increase the memory to 8 GB, and start the VM.

**My answer:** D
**Correct answer:** D
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A VM has 2 vCPUs (virtual processors) and 4 GB of memory, and it is running out of memory.
- **What you must achieve:** Give the VM 8 GB of memory.
- **The limits:** None stated.
- **What they're really asking:** How do you increase the VM's memory?

| Keyword | What it hints at |
|---|---|
| "**2 vCPUs and 4 GB**" | Only the **memory** is the problem. The CPUs are fine |
| "**upgrade … to have 8 GB**" | Change the VM's size, which in Compute Engine **requires the VM to be stopped** |
| "**8 GB**" exactly | A **custom** memory size (2 vCPUs + 8 GB) fits exactly. A bigger preset type wastes money |

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1️⃣ vCPU and Memory (RAM)
- **What it is:** **vCPU** = a virtual processor core (how much **thinking** the VM can do at once). **Memory/RAM** = the VM's **working space** for running programs. When it's full, apps slow down or crash ("out of memory").
- **Looks like:** `2 vCPUs, 4 GB memory`
- **Not to be confused with:** **disk** storage (where files are kept). Adding disk doesn't add memory.
- **Analogy:** 🧑‍💼 vCPUs = **how many workers** in the office. Memory = **the size of their desks**. A small desk means papers fall on the floor.
- **In the online store:** The checkout API caches product prices in memory, and on sale days the 4 GB desk overflows.

### 2️⃣ Machine Type 🔑
- **What it is:** The **size of the VM**: how many vCPUs and how much memory. Google sells **predefined** sizes and also lets you build a **custom** size.
- **Looks like:**
  | Machine type | vCPUs | Memory |
  |---|---|---|
  | `n1-standard-1` | 1 | 3.75 GB |
  | `n1-standard-2` | 2 | 7.5 GB |
  | `n1-standard-8` | **8** | **30 GB** |
  | `custom-2-8192` (custom) | 2 | **8 GB** ✅ |
- **Not to be confused with:** the disk or the OS. The machine type is only **CPU + memory**.
- **Analogy:** 🏢 **Office size options**: standard small/medium/large, or a **custom-built** office with exactly the desks you need.

### 3️⃣ Custom Machine Type (how "increase memory to 8 GB" works)
- **What it is:** A VM size where **you choose the vCPUs and memory yourself**, within limits (for example N1 allows up to 6.5 GB per vCPU, so 2 vCPUs can have up to 13 GB). In the Console, you **stop** the VM, click **Edit**, choose **Custom**, and set the memory.
- **Looks like:**
  ```bash
  gcloud compute instances set-machine-type api-orders-03 \
    --zone=us-central1-a --custom-cpu=2 --custom-memory=8GB
  ```
- **Not to be confused with:** a predefined type. Custom = **pay for exactly what you need**.
- **Analogy:** 🪑 Ordering **bigger desks** for the same 2 workers.

### 4️⃣ Live Migration
- **What it is:** Google **moves your running VM to another physical server** during Google's own maintenance, **without stopping it**. The VM keeps the **same size**.
- **Looks like:** VM setting `onHostMaintenance: MIGRATE` (the default)
- **Not to be confused with:** resizing. Live migration **never changes** CPU or memory, and **you don't trigger it**.
- **Analogy:** 🚚 The building manager **moves your office to an identical room** overnight while you keep working. Same desk size.

### 5️⃣ VM Metadata (review from Q001)
- **What it is:** **Key-value notes** attached to a VM, read by startup scripts or tools (like `enable-oslogin=TRUE`).
- **Looks like:** `startup-script=…`, `enable-oslogin=TRUE`
- **Not to be confused with:** hardware settings. A metadata key like `required-memory-size` is just a **note**. It doesn't change the hardware.
- **Analogy:** 📝 A **sticky note on the office door** saying "needs bigger desks". Nobody builds them.

### 🔗 How They Fit Together
```
VM api-orders-03: 2 vCPU / 4 GB  ⚠️ out of memory
        │
        ├─ A: live migration     → same size on another host       ❌ still 4 GB
        ├─ B: metadata note      → just a label                    ❌ still 4 GB
        ├─ C: n1-standard-8      → 8 vCPU / 30 GB                  ⚠️ way more than needed ($$$)
        └─ D: stop → custom 2 vCPU / 8 GB → start                   ✅ exactly what's needed
```

---

## 🌍 Real-World Scenario

An app's traffic or data grows and it starts **crashing with "out of memory"** errors. Monitoring shows memory at 100% but CPU at 30%. The fix is **"vertical scaling"**: give the same VM more memory. In Compute Engine this means a **short planned stop** (change the size, then start again), done during a quiet time. You **only add memory**, because CPUs cost money and aren't the problem.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Rely on live migration to move the workload to a machine with more memory.

**Why it's wrong:**
- ❌ Live migration is **Google's maintenance tool**. It moves the VM to another host with the **same size**, and **you can't use it to resize**.

**📌 When to use it:** You don't trigger it. It keeps VMs running while Google maintains its servers.
🏢 **Office example:** The building manager moves you to an identical office overnight so you aren't disturbed by repairs.

### ❌ B
> **B.** Use gcloud to add metadata to the VM. Set the key to required-memory-size and the value to 8 GB.

**Why it's wrong:**
- ❌ Metadata is just **notes** for scripts. There's **no** `required-memory-size` key that changes hardware.

**📌 When to use it:** Use metadata to pass settings to a VM, like a startup script or turning on OS Login.
🏢 **Office example:** Putting a note on the door with instructions for the cleaning staff.

### ❌ C
> **C.** Stop the VM, change the machine type to n1-standard-8, and start the VM.

**Why it's wrong:**
- ✔️ The process (stop → change → start) is right…
- ❌ …but `n1-standard-8` = **8 vCPUs and 30 GB**, far more than "8 GB". You'd pay for **6 extra CPUs and 22 GB** you don't need.
- 💡 The "8" in the name means **8 vCPUs**, not 8 GB. That's the trap.

**📌 When to use it:** Use a bigger predefined type when the app needs a lot more CPU **and** memory together.
🏢 **Office example:** Moving a 2-person team into a 30-desk office just because they needed bigger desks.

### ✅ D (your answer)
> **D.** Stop the VM, increase the memory to 8 GB, and start the VM.

**Why it's correct:**
- ✔️ Compute Engine needs the VM **stopped** to change its size.
- ✔️ Increasing memory to **8 GB** (custom machine type: 2 vCPUs + 8 GB) gives **exactly** what's needed.
- ✔️ Cheapest correct fix: you don't pay for CPUs you don't need.

**📌 When to use it:** Use it when a server only needs more working space and its speed is already fine.
🏢 **Office example:** Swapping the same two workers' small desks for bigger ones over the weekend.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's checkout VM **`api-orders-03`** (2 vCPU / 4 GB) crashes during the 11.11 sale with "out of memory". Monitoring shows **memory 100%, CPU 35%**.

```bash
# Do it at 3 AM, when traffic is low (other VMs behind the load balancer handle requests)
gcloud compute instances stop api-orders-03 --zone=us-central1-a

gcloud compute instances set-machine-type api-orders-03 --zone=us-central1-a \
  --custom-cpu=2 --custom-memory=8GB

gcloud compute instances start api-orders-03 --zone=us-central1-a
```

| Choice | Size after | Rough monthly cost* | Result |
|---|---|---|---|
| **D: custom 2 vCPU / 8 GB** | 2 / 8 GB | ~$60 | ✅ Fixed, small cost increase |
| C: `n1-standard-8` | 8 / 30 GB | ~$240 | ✅ Fixed, but ~4× the bill ❌ |
| A / B | 2 / 4 GB | same | ❌ Still crashing |

*Illustrative numbers, just to show the size of the difference.

**Bonus:** If the checkout servers run in a **MIG** (Q004/Q033), you'd make a **new instance template** with the bigger size and roll it out instead of editing VMs one by one.

---

## 🧠 Key Takeaways / Memory Tips

- **Change a VM's CPU/memory → stop it → change the machine type (or custom memory) → start it.**
  🧠 *"**Stop, resize, start.**"*
- **Need only more memory → increase memory (custom type).** Don't jump to a big preset type.
- **`n1-standard-8` = 8 vCPUs** (and 30 GB), not 8 GB. The number is **CPUs**.
- **Live migration** = Google moving your VM for maintenance, **same size**. **Metadata** = notes, not hardware.

# Q307: Nightly CPU/Memory-Heavy Batch That Tolerates Interruptions, Cost-Effective (Spot VMs)

**Topic:** Compute Engine (Spot VMs)

## ❓ Question
> You are migrating your company’s on-premises compute resources to Google Cloud. You need to deploy batch processing jobs that run every night. The jobs require significant CPU and memory for several hours but can tolerate interruptions. You must ensure that the deployment is cost-effective. What should you do?
>
> **A.** Use the M1 machine series on Compute Engine.
>
> **B.** Containerize the batch processing jobs and deploy them on Compute Engine.
>
> **C.** Use Spot VMs on Compute Engine.
>
> **D.** Use custom machine types on Compute Engine.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Nightly batch, **can tolerate interruptions**, **cost-effective**.

**Clues in the question:**
- "**can tolerate interruptions**" + "**cost-effective**" → **Spot VMs** (60–91% cheaper, can be stopped by Google).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Spot VMs 🔑
- **What it is:** Spare Google capacity at a big discount; Google may reclaim them anytime with short notice.
- **Looks like:** `gcloud compute instances create batch-1 --provisioning-model=SPOT`
- **Not to be confused with:** standard VMs.
- **Analogy:** 🎟️ Standby airline seats.
- **In the online store:** ShopNow nightly reports.

### 🔗 How they fit together
```
 tolerate interruption + cheap → Spot ✅
```

---

## 🌍 Real-World Scenario

Nightly analytics jobs run on **Spot VMs**; if one is reclaimed, the job restarts.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the M1 machine series on Compute Engine.

**Wrong words:**
- ❌ "**M1 machine series**": memory-optimized, expensive; not about cost.

📌 **When to use it:** Use M1 for huge in-memory databases like SAP HANA.
🏢 **Office example:** Renting the biggest truck for every trip.

### ❌ B
> **B.** Containerize the batch processing jobs and deploy them on Compute Engine.

**Wrong words:**
- ❌ "**Containerize … on Compute Engine**": packaging, not a cost saving.

📌 **When to use it:** Use containers for portable deployments.
🏢 **Office example:** Repacking boxes doesn't lower the rent.

### ✅ C
> **C.** Use Spot VMs on Compute Engine.

**Why it's correct:**
- ✔️ "**Spot VMs**" matches "**can tolerate interruptions**" + "**cost-effective**".

📌 **When to use it:** Use it when the work can stop and restart without harm and you want the lowest price.
🏢 **Office example:** Standby temp staff at a big discount who might be called away.

### ❌ D
> **D.** Use custom machine types on Compute Engine.

**Wrong words:**
- ❌ "**custom machine types**": right-sizing helps a bit, but much less than Spot discounts.

📌 **When to use it:** Use custom types when standard shapes waste resources.
🏢 **Office example:** Tailored desks; still full-price rent.

---

## 🛒 E-Commerce Full-Stack Example

Nightly `recommendations-batch` MIG with `--provisioning-model=SPOT`.

---

## 🧠 Key Takeaways / Memory Tips

- **Interruptible + cheap → Spot VMs.**
  🧠 *"**Can stop? Spot.**"*
- Related: **Q226**, **Q166**.

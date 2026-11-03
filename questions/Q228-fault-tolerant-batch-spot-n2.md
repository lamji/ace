# Q228: Fault-Tolerant Nightly Batch Costs Too Much (Test With Simulated Maintenance, Then Use Spot N2 VMs)

**Topic:** Compute Engine (Spot VMs)

## ❓ Question
> You have a batch workload that runs every night and uses a large number of virtual machines (VMs). It is fault-tolerant and can tolerate some of the VMs being terminated. The current cost of VMs is too high. What should you do?
>
> **A.** Run a test using simulated maintenance events. If the test is successful, use Spot N2 Standard VMs when running future jobs.
>
> **B.** Run a test using simulated maintenance events. If the test is successful, use N2 Standard VMs when running future jobs.
>
> **C.** Run a test using a managed instance group. If the test is successful, use N2 Standard VMs in the managed instance group when running future jobs.
>
> **D.** Run a test using N1 standard VMs instead of N2. If the test is successful, use N1 Standard VMs when running future jobs.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Same as Q150, with **Spot** instead of preemptible.

**Clues in the question:**
- "**can tolerate some of the VMs being terminated**" + "**cost … too high**" → **Spot VMs** (up to ~60–91% cheaper).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Spot VM 🔑 (review from Q218)
- **What it is:** Cheap, interruptible VMs.
- **Looks like:** `--provisioning-model=SPOT`
- **Not to be confused with:** regular VMs.
- **Analogy:** 🪑 Borrowed desks at a big discount.
- **In the online store:** Nightly batch.

### 2. Simulated maintenance event
- **What it is:** A test that makes Compute Engine act as if the VM is being interrupted.
- **Looks like:** `gcloud compute instances simulate-maintenance-event vm-1`
- **Not to be confused with:** —
- **Analogy:** 🚨 A fire drill.
- **In the online store:** —

### 🔗 How they fit together
```
 test interruptions ✅ → switch batch to Spot N2 ✅ (much cheaper)
```

---

## 🌍 Real-World Scenario

A rendering farm proves its jobs survive interruptions with simulated maintenance events, then moves to **Spot N2** VMs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run a test using simulated maintenance events. If the test is successful, use Spot N2 Standard VMs when running future jobs.

**Why it's correct:**
- ✔️ "**use Spot N2 Standard VMs**" matches "**can tolerate some of the VMs being terminated**" + "**cost … too high**".
- ✔️ "**Run a test using simulated maintenance events**" checks the job survives interruptions first.

📌 **When to use it:** Use it when the work can survive losing some machines and you want to save a lot.
🏢 **Office example:** Running a fire drill, then renting cheap desks that might be reclaimed.

### ❌ B
> **B.** Run a test using simulated maintenance events. If the test is successful, use N2 Standard VMs when running future jobs.

**Wrong words:**
- ❌ "**N2 Standard VMs**" (regular): no savings.

📌 **When to use it:** Use regular VMs for work that can't be interrupted.
🏢 **Office example:** A fire drill, then paying full price anyway.

### ❌ C
> **C.** Run a test using a managed instance group. If the test is successful, use N2 Standard VMs in the managed instance group when running future jobs.

**Wrong words:**
- ❌ "**N2 Standard VMs in the managed instance group**": still full price.

📌 **When to use it:** Use MIGs to manage many identical VMs.
🏢 **Office example:** Organizing desks better but paying full rent.

### ❌ D
> **D.** Run a test using N1 standard VMs instead of N2. If the test is successful, use N1 Standard VMs when running future jobs.

**Wrong words:**
- ❌ "**N1 standard VMs instead of N2**": small or no saving; not the cost lever.

📌 **When to use it:** Use N1 only for legacy needs.
🏢 **Office example:** Switching to a slightly older desk model.

---

## 🛒 E-Commerce Full-Stack Example

Nightly report workers: instance template with `--provisioning-model=SPOT --instance-termination-action=DELETE`.

---

## 🧠 Key Takeaways / Memory Tips

- **Fault-tolerant + too expensive → Spot VMs (test interruptions first).**
  🧠 *"**Tolerates loss? Go Spot.**"*
- Related: **Q150**, **Q218**.

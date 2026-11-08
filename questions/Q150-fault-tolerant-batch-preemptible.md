# Q150: Fault-Tolerant Nightly Batch on Many VMs Costs Too Much (Test, Then Use Preemptible VMs)

**Topic:** Compute Engine (preemptible / Spot VMs, simulated maintenance events)

## ❓ Question
> You have a batch workload that runs every night and uses a large number of virtual machines (VMs). It is fault-tolerant and can tolerate some of the VMs being terminated. The current cost of VMs is too high. What should you do?
>
> **A.** Run a test using simulated maintenance events. If the test is successful, use preemptible N1 Standard VMs when running future jobs.
>
> **B.** Run a test using simulated maintenance events. If the test is successful, use N1 Standard VMs when running future jobs.
>
> **C.** Run a test using a managed instance group. If the test is successful, use N1 Standard VMs in the managed instance group when running future jobs.
>
> **D.** Run a test using N1 standard VMs instead of N2. If the test is successful, use N1 Standard VMs when running future jobs.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A nightly batch job uses many VMs. It is fault-tolerant (it copes if some VMs are stopped). Costs are too high.
- **What you must achieve:** Lower the cost.
- **The limits:** Losing some VMs during the run is acceptable.
- **What they're really asking:** How do you make these VMs cheaper?

**Clues in the question:**
- "**fault-tolerant and can tolerate some of the VMs being terminated**": exactly what **preemptible (Spot) VMs** need, and they're 60–91% cheaper.
- "**cost … too high**": switch to preemptible.
- "**simulated maintenance events**": test how the job behaves when VMs are stopped before you rely on it.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Preemptible / Spot VM 🔑
- **What it is:** Much cheaper VMs that Google can stop when it needs capacity (preemptible: max 24 h).
- **Looks like:** `gcloud compute instances create worker-1 --preemptible` (or `--provisioning-model=SPOT`)
- **Not to be confused with:** regular VMs.
- **Analogy:** 🪑 Cheap borrowed desks that may be taken back.
- **In the online store:** Nightly image processing workers.

### 2. Simulated maintenance event
- **What it is:** A command that makes Google **act as if host maintenance happened**, so you can test how your app handles it.
- **Looks like:** `gcloud compute instances simulate-maintenance-event worker-1 --zone=us-central1-a`
- **Not to be confused with:** a real outage.
- **Analogy:** 🚨 A fire drill.
- **In the online store:** Test that the batch retries lost work.

### 🔗 How they fit together
```
 test: simulate-maintenance-event on workers → job still finishes ✅
 then: switch workers to preemptible → big cost drop ✅
```

---

## 🌍 Real-World Scenario

A media company renders thumbnails nightly on 200 VMs. The job already retries failed pieces. They run a drill with **simulated maintenance events**, confirm the job still completes, and switch to **preemptible** VMs, cutting the bill by about 70%.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run a test using simulated maintenance events. If the test is successful, use preemptible N1 Standard VMs when running future jobs.

**Why it's correct:**
- ✔️ "**use preemptible N1 Standard VMs**" matches "**can tolerate some of the VMs being terminated**" + "**cost … too high**": much cheaper, and losing a few is fine.
- ✔️ "**Run a test using simulated maintenance events**" matches "**fault-tolerant**": it proves the job survives interruptions before you switch.

📌 **When to use it:** Use it when work can survive losing a few helpers and you want to cut costs a lot.
🏢 **Office example:** Running a fire drill, then moving the night shift to cheap borrowed desks.

### ❌ B
> **B.** Run a test using simulated maintenance events. If the test is successful, use N1 Standard VMs when running future jobs.

**Wrong words:**
- ✔️ The test is fine.
- ❌ "**use N1 Standard VMs**" (regular): no real cost saving.

📌 **When to use it:** Use regular VMs when interruptions aren't allowed.
🏢 **Office example:** Doing the drill, then keeping the expensive desks.

### ❌ C
> **C.** Run a test using a managed instance group. If the test is successful, use N1 Standard VMs in the managed instance group when running future jobs.

**Wrong words:**
- ❌ "**N1 Standard VMs in the managed instance group**": a MIG manages VMs but doesn't make them cheaper.

📌 **When to use it:** Use MIGs for autoscaling and self-healing.
🏢 **Office example:** Hiring an agency to manage the same expensive desks.

### ❌ D
> **D.** Run a test using N1 standard VMs instead of N2. If the test is successful, use N1 Standard VMs when running future jobs.

**Wrong words:**
- ❌ "**N1 standard VMs instead of N2**": a small difference at best, and it ignores the fault-tolerance clue.

📌 **When to use it:** Use machine families based on performance needs.
🏢 **Office example:** Swapping desk brands instead of using cheap borrowed desks.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's nightly image resizer uses 150 workers. After `gcloud compute instances simulate-maintenance-event` tests pass, the instance template uses `--provisioning-model=SPOT`. Cost drops from about $1,800 to about $450 a month.

---

## 🧠 Key Takeaways / Memory Tips

- **Fault-tolerant batch + cost too high → preemptible/Spot VMs** (test with simulated maintenance first).
- Not for long, non-restartable jobs (Q136).
  🧠 *"**Can lose a few? Go preemptible.**"*
- Related: **Q136** (30-hour job → no preemptible), **Q108**, **Q094**.

# Q136: Monthly 30-Hour Batch That Must Restart if Interrupted (Regular VM, Start and Stop as Needed)

**Topic:** Compute Engine (preemptible VM 24-hour limit, cost, start/stop)

## ❓ Question
> Your company runs one batch process in an on-premises server that takes around 30 hours to complete. The task runs monthly, can be performed offline, and must be restarted if interrupted. You want to migrate this workload to the cloud while minimizing cost. What should you do?
>
> **A.** Migrate the workload to a Compute Engine Preemptible VM.
>
> **B.** Migrate the workload to a Google Kubernetes Engine cluster with Preemptible nodes.
>
> **C.** Migrate the workload to a Compute Engine VM. Start and stop the instance as needed.
>
> **D.** Create an Instance Template with Preemptible VMs On. Create a Managed Instance Group from the template and adjust Target CPU Utilization. Migrate the workload.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A monthly batch job takes about 30 hours, can run offline, and must start over if it is interrupted.
- **What you must achieve:** Move it to the cloud.
- **The limits:** Keep costs as low as possible.
- **What they're really asking:** Which kind of VM is cheapest without risking the job being interrupted?

**Clues in the question:**
- "**around 30 hours**": preemptible VMs are **always stopped within 24 hours**, so the job could never finish.
- "**must be restarted if interrupted**": interruptions are very costly → no preemptible.
- "**runs monthly**" + "**minimizing cost**": a normal VM that you **start for the job and stop afterwards**, so you pay only while it runs.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Preemptible VM 24-hour limit 🔑
- **What it is:** Preemptible VMs are cheap but are **stopped at most 24 hours** after starting, and can be stopped earlier at any time.
- **Looks like:** `--preemptible`
- **Not to be confused with:** Spot VMs (no 24-hour limit, but still can be stopped).
- **Analogy:** 🪑 A borrowed desk you must give back within a day.
- **In the online store:** Short retryable jobs.

### 2. Start/stop a VM
- **What it is:** A stopped VM costs nothing for CPU and memory (you still pay for its disks).
- **Looks like:** `gcloud compute instances start batch-1` / `stop batch-1`
- **Not to be confused with:** deleting it.
- **Analogy:** 💡 Turning off the lights when you leave the office.
- **In the online store:** Monthly report VM runs 30 hours, then stops.

### 🔗 How they fit together
```
 preemptible: max 24 h ⏱️ → 30 h job never finishes ❌
 regular VM: start → 30 h job → stop → pay ~30 h/month ✅
```

---

## 🌍 Real-World Scenario

A finance company moves its monthly 30-hour reconciliation job to the cloud. A regular VM is **started** on the 1st, runs the job, and is **stopped** when it finishes. They pay for about 30 hours a month.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate the workload to a Compute Engine Preemptible VM.

**Wrong words:**
- ❌ "**Preemptible VM**": stopped within 24 hours (and possibly sooner), so a 30-hour job that must restart would never finish.

📌 **When to use it:** Use it for short jobs that can resume or retry.
🏢 **Office example:** Starting a 30-hour task at a desk you must give back within 24 hours.

### ❌ B
> **B.** Migrate the workload to a Google Kubernetes Engine cluster with Preemptible nodes.

**Wrong words:**
- ❌ "**GKE cluster with Preemptible nodes**": the same 24-hour problem, plus a cluster to run for a single batch job.

📌 **When to use it:** Use it for many retryable containers.
🏢 **Office example:** A whole team of borrowed desks for one long task.

### ✅ C
> **C.** Migrate the workload to a Compute Engine VM. Start and stop the instance as needed.

**Why it's correct:**
- ✔️ "**Compute Engine VM**" (regular) matches "**takes around 30 hours**" + "**must be restarted if interrupted**": it isn't preempted, so the job can finish.
- ✔️ "**Start and stop the instance as needed**" matches "**runs monthly**" + "**minimizing cost**": you pay only while it runs.

📌 **When to use it:** Use it when a long job can't be interrupted and runs only occasionally.
🏢 **Office example:** Booking a proper desk for the 30-hour job, then switching the lights off when done.

### ❌ D
> **D.** Create an Instance Template with Preemptible VMs On. Create a Managed Instance Group from the template and adjust Target CPU Utilization. Migrate the workload.

**Wrong words:**
- ❌ "**Preemptible VMs On**": same 24-hour limit.
- ❌ "**Managed Instance Group … Target CPU Utilization**": autoscaling doesn't help one long single job.

📌 **When to use it:** Use it for scalable, interruptible fleets.
🏢 **Office example:** An automatic staffing agency of borrowed desks for one 30-hour task.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's monthly inventory reconciliation takes about 30 hours.
```bash
gcloud compute instances start recon-1 --zone=us-central1-a   # 1st of month (Cloud Scheduler)
# job runs ~30 h, then the script calls:
gcloud compute instances stop recon-1 --zone=us-central1-a
```

---

## 🧠 Key Takeaways / Memory Tips

- **Preemptible = max 24 h.** Long, non-restartable jobs need regular VMs.
- Save money by **stopping** VMs when idle.
  🧠 *"**Longer than a day? Not preemptible.**"*
- Related: **Q108** (non-restartable GPU jobs), **Q094** (preemption), **Q150** (fault-tolerant batch → preemptible).

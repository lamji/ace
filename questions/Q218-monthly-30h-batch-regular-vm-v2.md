# Q218: Monthly 30-Hour Batch That Must Restart if Interrupted (Regular VM, Start and Stop as Needed)

**Topic:** Compute Engine (Spot VMs vs regular VMs)

## ❓ Question
> Your company runs one batch process in an on-premises server that takes around 30 hours to complete. The task runs monthly, can be performed offline, and must be restarted if interrupted. You want to migrate this workload to the cloud while minimizing cost. What should you do?
>
> **A.** Create an Instance Template with Spot VMs On. Create a Managed Instance Group from the template and adjust Target CPU Utilization. Migrate the workload.
>
> **B.** Migrate the workload to a Compute Engine VM. Start and stop the instance as needed.
>
> **C.** Migrate the workload to a Google Kubernetes Engine cluster with Spot nodes.
>
> **D.** Migrate the workload to a Compute Engine Spot VM.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Same idea as Q136, with **Spot** VMs in the wrong options.

**Clues in the question:**
- "**must be restarted if interrupted**" → Spot VMs can be stopped anytime, and a 30-hour job would likely restart again and again.
- "**runs monthly**" + "**minimizing cost**" → regular VM, **start and stop** it.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Spot VM 🔑
- **What it is:** Cheap VMs Google can **stop at any time** (newer version of preemptible, no 24-hour limit, but still interruptible).
- **Looks like:** `--provisioning-model=SPOT`
- **Not to be confused with:** regular VMs.
- **Analogy:** 🪑 A borrowed desk that can be taken back any minute.
- **In the online store:** Fault-tolerant batch.

### 🔗 How they fit together
```
 30 h job, restart if interrupted → regular VM ✅ (start → run → stop)
```

---

## 🌍 Real-World Scenario

A finance team's 30-hour monthly close job moves to a **regular VM** that's started on the 1st and stopped when done.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an Instance Template with Spot VMs On. Create a Managed Instance Group from the template and adjust Target CPU Utilization. Migrate the workload.

**Wrong words:**
- ❌ "**Spot VMs On**": can be interrupted, forcing a 30-hour restart.
- ❌ "**Managed Instance Group … Target CPU Utilization**": autoscaling doesn't help a single job.

📌 **When to use it:** Use Spot MIGs for fault-tolerant scalable work.
🏢 **Office example:** Renting desks that vanish, for a 30-hour task.

### ✅ B
> **B.** Migrate the workload to a Compute Engine VM. Start and stop the instance as needed.

**Why it's correct:**
- ✔️ "**Compute Engine VM**" (regular) matches "**must be restarted if interrupted**": it won't be taken away mid-job.
- ✔️ "**Start and stop the instance as needed**" matches "**runs monthly**" + "**minimizing cost**".

📌 **When to use it:** Use it when a long job can't be interrupted and only runs now and then.
🏢 **Office example:** Booking a meeting room for the full day of month-end closing, then releasing it.

### ❌ C
> **C.** Migrate the workload to a Google Kubernetes Engine cluster with Spot nodes.

**Wrong words:**
- ❌ "**GKE cluster with Spot nodes**": interruptible, plus a cluster to manage.

📌 **When to use it:** Use GKE Spot nodes for fault-tolerant containers.
🏢 **Office example:** A whole shared office of borrowed desks.

### ❌ D
> **D.** Migrate the workload to a Compute Engine Spot VM.

**Wrong words:**
- ❌ "**Spot VM**": can be interrupted at any time.

📌 **When to use it:** Use Spot VMs for jobs that can resume.
🏢 **Office example:** A desk that can be taken back mid-task.

---

## 🛒 E-Commerce Full-Stack Example

`month-end-reports` VM: started on the 1st via an instance schedule, stopped when the job finishes.

---

## 🧠 Key Takeaways / Memory Tips

- **Long job that can't resume → regular VM, start/stop.** Spot = interruptible.
  🧠 *"**Can't be interrupted? Don't rent Spot.**"*
- Related: **Q136**, **Q228**.

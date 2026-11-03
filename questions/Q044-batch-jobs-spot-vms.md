# Q044: Lower-Cost Compute for Nightly Batch Jobs

**Topic:** Compute Engine (Spot / preemptible VMs, batch processing, machine types, GKE cost)

## ❓ Question
> You need to select and configure compute resources for a set of batch processing jobs. These jobs take around 2 hours to complete and are run nightly. You want to minimize service costs. What should you do?
>
> **A.** Select Google Kubernetes Engine. Use a single-node cluster with a small instance type.
>
> **B.** Select Google Kubernetes Engine. Use a three-node cluster with micro instance types.
>
> **C.** Select Compute Engine. Use preemptible VM instances of the appropriate standard machine type.
>
> **D.** Select Compute Engine. Use VM instance types that support micro bursting.

**My answer:** A
**Correct answer:** C — Select Compute Engine. Use preemptible VM instances of the appropriate standard machine type.
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **A** is understandable because one small cluster sounds like a low-cost way to run jobs. However, Kubernetes adds cluster management and is unnecessary when the requirement is simply to run nightly batch work as cheaply as possible.

**Correct answer: C — Select Compute Engine. Use preemptible VM instances of the appropriate standard machine type.** The jobs run for only about two hours and recur nightly, so discounted interruptible VMs are a good fit if the jobs can be retried or resume after an interruption. Use enough CPU and memory for the actual job instead of choosing a micro machine just because its hourly price is low.

**Current terminology:** Google now calls the newer discounted offering **Spot VMs**. The option uses the older term **preemptible VM**; Google still supports that model, but recommends Spot VMs for new fault-tolerant batch workloads.

## 2. 📖 What the Question Is Asking

In plain words: a workload runs for about two hours each night. Which compute option can run that work at the lowest service cost without paying for a large cluster that sits unused?

- **“batch processing jobs”** means work can run as a scheduled task rather than serving every request immediately.
- **“2 hours” and “run nightly”** means the machines are needed for a limited scheduled period.
- **“minimize service costs”** points to discounted capacity and avoiding unnecessary cluster overhead.
- **Exam topic:** Compute Engine machine choices and discounted VMs for fault-tolerant batch work.

## 2.5 📚 Key Terms Explained

### Batch processing job
- **What it is:** A task that processes a collection of data and runs to completion, often on a schedule. Unlike a website, it usually doesn't need to respond instantly to every user.
- **Analogy:** An office team processing a stack of forms after the doors close.
- **In the online store:** A nightly job could generate sales reports or reconcile the day's orders.

### Compute resource
- **What it is:** The CPU, memory, and machines an application uses to do work.
- **Analogy:** Staff and workstations assigned to a task.
- **In the online store:** Compute resources run order processing, report generation, and backend services.

### Compute Engine
- **What it is:** Google Cloud's service for creating and managing virtual machines.
- **Analogy:** Renting individual office computers from a provider.
- **In the online store:** Compute Engine can run a nightly report job on a VM that is started for the job and stopped afterward.

### Virtual machine (VM) / instance
- **What it is:** A software-based computer with allocated CPU and memory. “VM instance” is the Compute Engine term used in the options.
- **Analogy:** A rented workstation.
- **In the online store:** A VM can run a data cleanup or report program.

### Preemptible VM / Spot VM
- **What it is:** A discounted VM that Google Cloud can stop when it needs the capacity back. Spot VMs are the newer model; preemptible VMs are the older version and can have a 24-hour maximum lifetime.
- **Analogy:** A low-cost spare workstation that the office can reclaim when a priority team needs it.
- **In the online store:** They can run retryable nightly analytics or image-processing jobs, where work can checkpoint and resume if interrupted.

### Standard machine type
- **What it is:** A VM configuration with a balanced amount of CPU and memory compared with small shared-core types. Choose its size based on what the job needs.
- **Analogy:** A workstation with enough regular capacity for the assigned workload.
- **In the online store:** A standard VM type can provide steady CPU and memory for processing a nightly order export.

### Google Kubernetes Engine (GKE)
- **What it is:** Google's managed Kubernetes service for deploying and operating containerized workloads.
- **Analogy:** A managed system for coordinating many workstations and the software running on them.
- **In the online store:** GKE can run the storefront and backend services, especially when the team already needs Kubernetes orchestration.

### Kubernetes cluster and nodes
- **What they are:** A cluster is the Kubernetes environment; nodes are the worker machines that run containers. A GKE cluster also has control-plane management overhead even though the control plane is managed by Google.
- **Analogy:** A coordinated office site with a manager and several work areas.
- **In the online store:** Nodes in a GKE cluster can run the order API containers.

### Instance type / machine type
- **What it is:** The selected VM size and shape, including CPU and memory. “Micro” is a very small shared-core configuration; “standard” indicates a balanced general-purpose configuration family.
- **Analogy:** Choosing the size and capability of a workstation.
- **In the online store:** A database report job may need more memory or CPU than a tiny utility task.

### Micro bursting
- **What it is:** Some small shared-core VM types can briefly use more CPU than their sustained share. Bursting is for short spikes; it is not sustained full-CPU capacity for a two-hour job.
- **Analogy:** A small office team can briefly work overtime, but cannot keep that pace for an entire shift.
- **In the online store:** A micro VM might suit a lightweight admin task, not a consistently CPU-heavy nightly report.

### Service costs
- **What it is:** The charges for the cloud resources and services used, such as running VMs, storage, and cluster resources.
- **Analogy:** The office's rental and utility bill.
- **In the online store:** Turning off job VMs after nightly processing helps avoid paying for idle compute.

### How the choices relate

```text
Nightly batch job (about 2 hours)
          │
          ├── Needs steady CPU/memory → suitable standard machine type
          ├── Can tolerate interruption → Spot/preemptible pricing
          └── Runs only when scheduled → stop/delete VMs after completion

GKE is useful when Kubernetes orchestration is needed; it adds complexity for a simple scheduled VM job.
```

## 3. 🌍 Real-World Scenario

A retailer processes the day's orders every night to create finance and inventory reports. The work takes two hours. The company can save money by running it on discounted Spot VMs with sufficient CPU and memory. If a VM is reclaimed, the job should checkpoint its progress or restart the affected task. The machines can be stopped or deleted when processing is complete so they do not sit idle all day.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A — Your answer

> **A.** Select Google Kubernetes Engine. Use a single-node cluster with a small instance type.

**Why it is wrong:** This option sounds economical because it says **single node** and **small instance**, but it misses the two cost clues in the question: the job runs only at night, and it is batch work. GKE is designed to orchestrate container workloads; it brings Kubernetes setup and management that this simple scheduled job does not need. A small VM also may not have enough sustained CPU or memory to finish the job efficiently. Finally, A does not choose discounted interruptible capacity. It could therefore spend more time and operational effort while still paying standard compute prices. The question asks for the lowest-cost suitable compute, not simply the fewest nodes.

**When it is useful:** A small GKE cluster can be useful for learning Kubernetes or running a small containerized workload when the team specifically needs Kubernetes features.

📌 When to use it: Use it when a small team needs a shared system to run a few packaged programs.  
🏢 Office example: A small office uses one shared workstation to run a few standard office tools.

### ❌ B

> **B.** Select Google Kubernetes Engine. Use a three-node cluster with micro instance types.

**Why it is wrong:** This option makes the architecture larger while making each worker very small. The question does not say the job needs Kubernetes or three separate workers, so the cluster adds setup and management without solving a stated need. The word **micro** is also misleading: a low hourly price does not mean a good cost for the completed job. Shared-core micro VMs provide limited sustained CPU, and their extra CPU burst lasts only briefly. If a two-hour job is CPU-heavy, three micro VMs can take much longer or fail to meet the deadline. Unlike C, this option also does not use discounted Spot/preemptible pricing.

**When it is useful:** A small multi-node Kubernetes cluster is useful when a team needs to learn or test how workloads behave across several nodes.

📌 When to use it: Use it when a team needs several small computers to practice coordinating shared work.  
🏢 Office example: A training room uses three small computers so staff can practice sharing tasks across stations.

### ✅ C — Correct

> **C.** Select Compute Engine. Use preemptible VM instances of the appropriate standard machine type.

**Why it is correct:** Compute Engine gives the job a VM directly, which fits scheduled batch work without requiring Kubernetes. Preemptible VMs cost less because Google Cloud can stop them when it needs the capacity back. That tradeoff is suitable for batch processing **if the job can handle interruption**: save progress, split the job into retryable pieces, or rerun it if necessary. The phrase **“appropriate standard machine type”** means choose CPU and memory based on the workload's measured needs. That avoids the mistake in B and D of choosing a tiny machine whose low hourly cost can be outweighed by a much longer run time. Since the job runs two hours nightly, schedule the VM to run only for that work and shut it down afterward; persistent disks and other attached resources can still incur charges while retained.

For a new deployment today, use Spot VMs, Google's newer recommended discounted VM offering. Spot VMs can also be reclaimed at any time, so the same fault-tolerance requirement applies. Schedule the job to start nightly and stop or delete its VM when finished to avoid paying for idle compute.

📌 When to use it: Use it when scheduled work can pause, retry, or resume if a computer is reclaimed.  
🏢 Office example: Run a nightly filing task on a discounted spare workstation, saving progress so another workstation can finish if it is reclaimed.

### ❌ D

> **D.** Select Compute Engine. Use VM instance types that support micro bursting.

**Why it is wrong:** Micro bursting is a short boost, not two hours of extra processing capacity. Common E2 micro, small, and medium shared-core VMs can burst for only dozens of seconds when fully busy. A long-running batch job—especially a CPU-heavy one—needs enough sustained CPU and memory to finish reliably. A micro VM could have a low hourly rate but take much longer, making the actual cost and completion time worse. D also overlooks the main cost clue: because this is scheduled batch work, it may be able to use interruptible discounted VMs as in C. Bursting can still be helpful for a small task that is usually idle and only needs brief bursts.

**When it is useful:** Micro bursting can suit a small workload with occasional short CPU spikes and low overall resource needs.

📌 When to use it: Use it when a small task needs extra effort only for a brief moment.  
🏢 Office example: A clerk's small computer briefly speeds up when opening a large spreadsheet, then returns to light work.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow runs a nightly job that summarizes orders and updates inventory reports. It can use a Compute Engine Spot VM with enough CPU and memory for the task. The job saves progress periodically and retries unfinished parts if the VM is reclaimed. A scheduler starts the VM at night and stops it after the report finishes. The live storefront and checkout services can remain on their normal always-available infrastructure.

## 6. 🧠 Key Takeaway / Memory Tip

For short, scheduled, fault-tolerant batch jobs, think **Compute Engine Spot VM + a machine size that fits the work**. Don't choose Kubernetes just because it can run containers, and don't mistake a brief CPU burst for two hours of sustained performance.

**Current documentation:** [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), [Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot), and [E2 shared-core machine types and bursting](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

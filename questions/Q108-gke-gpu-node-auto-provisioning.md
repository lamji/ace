# Q108: GPUs Needed Only Sometimes, Long Non-Restartable Jobs, Minimum Cost (Node Auto-Provisioning)

**Topic:** GKE (node auto-provisioning, autoscaling, preemptible VMs, GPUs)

## ❓ Question
> A team of data scientists infrequently needs to use a Google Kubernetes Engine (GKE) cluster that you manage. They require GPUs for some long-running, non- restartable jobs. You want to minimize cost. What should you do?
>
> **A.** Enable node auto-provisioning on the GKE cluster.
>
> **B.** Create a VerticalPodAutscaler for those workloads.
>
> **C.** Create a node pool with preemptible VMs and GPUs attached to those VMs.
>
> **D.** Create a node pool of instances with GPUs, and enable autoscaling on this node pool with a minimum size of 1.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** This is the site's accepted (most voted) answer. In practice, a GPU node pool that autoscales from **0** would also work, but D says a minimum of **1**.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Data scientists sometimes use a GKE cluster. They need GPUs for long-running jobs that cannot be restarted.
- **What you must achieve:** Give them GPUs.
- **The limits:** Keep costs low, and the jobs must not be interrupted.
- **What they're really asking:** How should you set up GPU nodes cheaply without risking their jobs?

**Clues in the question:**
- "**infrequently**": don't keep GPU nodes running all the time (rules out D's minimum of 1).
- "**long-running, non-restartable**": preemptible VMs can be stopped at any time → rules out C.
- "**minimize cost**": **node auto-provisioning** creates a GPU node pool only when a GPU pod needs it and deletes it afterwards.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Node auto-provisioning (NAP) 🔑
- **What it is:** A GKE feature where the cluster autoscaler **creates whole new node pools automatically** (including GPU pools) when pods need them, and **removes them** when they're no longer needed.
- **Looks like:** `gcloud container clusters update ds-cluster --enable-autoprovisioning --max-cpu=64 --max-memory=256 --max-accelerator=type=nvidia-tesla-t4,count=4`
- **Not to be confused with:** normal autoscaling, which only grows or shrinks pools you already made.
- **Analogy:** 🏢 Facilities **sets up a GPU room only when someone books it**, then clears it out.
- **In the online store:** The ML team's training job triggers a GPU pool, which disappears when done.

### 2. Preemptible VM
- **What it is:** A cheap VM Google can stop at any time.
- **Looks like:** `--preemptible`
- **Not to be confused with:** a safe home for jobs that can't restart.
- **Analogy:** 🪑 A borrowed desk.
- **In the online store:** Fine for retryable batch jobs.

### 3. VerticalPodAutoscaler (VPA)
- **What it is:** Adjusts the **CPU/memory requests of pods**. It doesn't add GPUs or nodes.
- **Looks like:** `kind: VerticalPodAutoscaler`
- **Not to be confused with:** node autoscaling.
- **Analogy:** 🪑 Resizing a desk, not adding a room.
- **In the online store:** Tunes the API pods' memory.

### 🔗 How they fit together
```
 GPU job submitted → NAP creates GPU node pool → job runs to the end
 job finishes      → GPU pool removed → $0 for GPUs while idle ✅
 (preemptible ❌ can kill the job; min size 1 ❌ pays for an idle GPU 24/7)
```

---

## 🌍 Real-World Scenario

A research team runs a 20-hour GPU training job about twice a month. The admin enables **node auto-provisioning** on the shared cluster. When a job asks for a GPU, GKE creates a GPU pool; when it finishes, the pool is deleted, so nobody pays for idle GPUs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Enable node auto-provisioning on the GKE cluster.

**Why it's correct:**
- ✔️ "**Enable node auto-provisioning**" matches "**infrequently needs**" + "**minimize cost**": GPU nodes exist only while jobs need them.
- ✔️ "**node auto-provisioning**" matches "**require GPUs**": it can create GPU node pools automatically.
- ✔️ It uses normal (not preemptible) VMs, which matches "**long-running, non-restartable jobs**": the job isn't killed midway.

📌 **When to use it:** Use it when special machines are needed only now and then, and should vanish when not in use.
🏢 **Office example:** Facilities sets up a GPU room only when someone books it, then clears it out.

### ❌ B
> **B.** Create a VerticalPodAutscaler for those workloads.

**Wrong words:**
- ❌ "**VerticalPodAutscaler**": it changes pods' CPU/memory requests. It doesn't create GPU nodes or reduce idle cost.

📌 **When to use it:** Use it when pods ask for the wrong amount of CPU or memory.
🏢 **Office example:** Resizing a desk when you needed a special room.

### ❌ C
> **C.** Create a node pool with preemptible VMs and GPUs attached to those VMs.

**Wrong words:**
- ✔️ "GPUs attached" gives GPUs.
- ❌ "**preemptible VMs**": Google can stop them at any time, which breaks "**non-restartable**" jobs.

📌 **When to use it:** Use it for GPU jobs that can safely restart.
🏢 **Office example:** Running a 20-hour task on a borrowed desk that can be taken away.

### ❌ D
> **D.** Create a node pool of instances with GPUs, and enable autoscaling on this node pool with a minimum size of 1.

**Wrong words:**
- ✔️ "node pool of instances with GPUs" gives GPUs.
- ❌ "**minimum size of 1**": one GPU node runs 24/7 even when nobody uses it. Not "minimize cost" for "infrequent" use.

📌 **When to use it:** Use it when GPU work arrives all day and must start instantly.
🏢 **Office example:** Keeping a GPU room staffed all month for two bookings.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's ML team retrains the recommendation model twice a month.

```bash
gcloud container clusters update shopnow-ml --zone=us-central1-c --enable-autoprovisioning \
  --max-cpu=64 --max-memory=256 --max-accelerator=type=nvidia-tesla-t4,count=2
```
The training pod requests `nvidia.com/gpu: 1`. GKE creates a T4 pool, the job runs for 18 hours, and the pool is removed afterwards.

---

## 🧠 Key Takeaways / Memory Tips

- **Rare GPU need + minimize cost → node auto-provisioning** (or a GPU pool that scales from 0).
- **Non-restartable → no preemptible/Spot.**
- VPA changes pod sizes, not nodes.
  🧠 *"**Need it rarely? Let GKE create it on demand.**"*
- Related: **Q081** (GPU node pool + nodeSelector), **Q094** (preemptible nodes).

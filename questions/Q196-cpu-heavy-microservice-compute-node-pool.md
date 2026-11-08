# Q196: CPU-Heavy Image Rendering Next to Standard Workloads (Compute-Optimized Node Pool for It)

**Topic:** GKE (node pools by machine family)

## ❓ Question
> You are running multiple microservices in a Kubernetes Engine cluster. One microservice is rendering images. The microservice responsible for the image rendering requires a large amount of CPU time compared to the memory it requires. The other microservices are workloads that are optimized for n1-standard machine types. You need to optimize your cluster so that all workloads are using resources as efficiently as possible. What should you do?
>
> **A.** Assign the pods of the image rendering microservice a higher pod priority than the other microservices.
>
> **B.** Create a node pool with compute-optimized machine type nodes for the image rendering microservice. Use the node pool with general-purpose machine type nodes for the other microservices.
>
> **C.** Use the node pool with general-purpose machine type nodes for the image rendering microservice. Create a node pool with compute-optimized machine type nodes for the other microservices.
>
> **D.** Configure the required amount of CPU and memory in the resource requests specification of the image rendering microservice deployment. Keep the resource requests for the other microservices at the default.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Several microservices run on a GKE cluster. One renders images and needs lots of CPU but little memory; the others suit n1-standard machines.
- **What you must achieve:** Make every workload use resources efficiently.
- **The limits:** None stated.
- **What they're really asking:** How should you arrange node machine types for the image service and the rest?

**Clues in the question:**
- "**large amount of CPU time compared to the memory**" → **compute-optimized** nodes (C2) for that service.
- "**others … optimized for n1-standard**" → keep them on the **general-purpose** pool.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Node pool by machine type 🔑
- **What it is:** Separate groups of nodes with different machine types in one cluster. Pods are steered with node selectors/affinity.
- **Looks like:** `gcloud container node-pools create render --machine-type=c2-standard-16` + `nodeSelector: cloud.google.com/gke-nodepool: render`
- **Not to be confused with:** pod priority.
- **Analogy:** 🏢 A workshop floor with heavy machines next to normal offices.
- **In the online store:** Image resizing pool.

### 2. Compute-optimized (C2/C3)
- **What it is:** VMs with **high CPU per memory** and fast cores.
- **Looks like:** `c2-standard-8`
- **Not to be confused with:** memory-optimized (M1).
- **Analogy:** 🏎️ Fast engines.
- **In the online store:** Thumbnail rendering.

### 🔗 How they fit together
```
 cluster
  ├─ pool general (n1-standard) → cart, checkout, catalog
  └─ pool render (c2) → image-renderer ✅
```

---

## 🌍 Real-World Scenario

A store's image-resizing service eats CPU. The team adds a **C2 node pool** just for it and keeps the other services on standard nodes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Assign the pods of the image rendering microservice a higher pod priority than the other microservices.

**Wrong words:**
- ❌ "**higher pod priority**": decides who gets scheduled first, not what hardware fits best.

📌 **When to use it:** Use priority so critical pods run first when space is short.
🏢 **Office example:** Letting one team jump the queue instead of giving them the right tools.

### ✅ B
> **B.** Create a node pool with compute-optimized machine type nodes for the image rendering microservice. Use the node pool with general-purpose machine type nodes for the other microservices.

**Why it's correct:**
- ✔️ "**node pool with compute-optimized machine type nodes for the image rendering microservice**" matches "**requires a large amount of CPU time compared to the memory**".
- ✔️ "**general-purpose … for the other microservices**" matches "**optimized for n1-standard machine types**".

📌 **When to use it:** Use it when one kind of work needs special equipment and the rest is normal.
🏢 **Office example:** Putting the heavy printing jobs in a print room with industrial printers, and keeping everyone else at normal desks.

### ❌ C
> **C.** Use the node pool with general-purpose machine type nodes for the image rendering microservice. Create a node pool with compute-optimized machine type nodes for the other microservices.

**Wrong words:**
- ❌ "**general-purpose … for the image rendering**" and ❌ "**compute-optimized … for the other microservices**": exactly backwards.

📌 **When to use it:** **Never use this** — it swaps the needs.
🏢 **Office example:** Giving the industrial printers to the receptionists.

### ❌ D
> **D.** Configure the required amount of CPU and memory in the resource requests specification of the image rendering microservice deployment. Keep the resource requests for the other microservices at the default.

**Wrong words:**
- ✔️ Setting requests is good practice.
- ❌ But requests don't change the **machine type**, so CPU-heavy pods still sit on standard nodes with wasted memory.

📌 **When to use it:** Use resource requests so pods are scheduled on nodes with enough room.
🏢 **Office example:** Reserving a desk size without changing the kind of desk.

---

## 🛒 E-Commerce Full-Stack Example

Node pool `render` (c2-standard-8, taint `workload=render:NoSchedule`) for `image-resizer`; `default-pool` (n2-standard-4) for cart/checkout.

---

## 🧠 Key Takeaways / Memory Tips

- **Different hardware needs in one cluster → separate node pools.** CPU-heavy → compute-optimized.
  🧠 *"**Right pool for the job.**"*
- Related: **Q237** (same, n2), **Q145**, **Q174**.

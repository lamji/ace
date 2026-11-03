# Q237: CPU-Heavy Image Rendering Next to n2-Standard Workloads (Compute-Optimized Node Pool for It)

**Topic:** GKE (node pools by machine family)

## ❓ Question
> You are running multiple microservices in a Kubernetes Engine cluster. One microservice is rendering images. The microservice responsible for the image rendering requires a large amount of CPU time compared to the memory it requires. The other microservices are workloads that are optimized for n2-standard machine types. You need to optimize your cluster so that all workloads are using resources as efficiently as possible. What should you do?
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

**In plain words:** Same as Q196 with n2 instead of n1.

**Clues in the question:**
- CPU-heavy → **compute-optimized** pool. Others → **general-purpose** pool.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Node pool by machine type 🔑 (review from Q196)
- **What it is:** Separate node groups with different machine types.
- **Looks like:** `--machine-type=c2-standard-16`
- **Not to be confused with:** pod priority.
- **Analogy:** 🏢 Workshop vs offices.
- **In the online store:** Image rendering pool.

### 🔗 How they fit together
```
 pool general (n2-standard) → others
 pool compute (c2) → image renderer ✅
```

---

## 🌍 Real-World Scenario

Same as Q196: a **C2 node pool** for the renderer, n2-standard for everything else.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Assign the pods of the image rendering microservice a higher pod priority than the other microservices.

**Wrong words:**
- ❌ "**higher pod priority**": scheduling order, not the right hardware.

📌 **When to use it:** Use priority for critical pods when space is short.
🏢 **Office example:** Letting one team jump the queue.

### ✅ B
> **B.** Create a node pool with compute-optimized machine type nodes for the image rendering microservice. Use the node pool with general-purpose machine type nodes for the other microservices.

**Why it's correct:**
- ✔️ "**compute-optimized … for the image rendering microservice**" matches "**large amount of CPU time compared to the memory**".
- ✔️ "**general-purpose … for the other microservices**" matches "**optimized for n2-standard machine types**".

📌 **When to use it:** Use it when one kind of work needs special equipment and the rest is normal.
🏢 **Office example:** Heavy printing jobs in the print room; everyone else at normal desks.

### ❌ C
> **C.** Use the node pool with general-purpose machine type nodes for the image rendering microservice. Create a node pool with compute-optimized machine type nodes for the other microservices.

**Wrong words:**
- ❌ Backwards: "**general-purpose … for the image rendering**" and "**compute-optimized … for the other microservices**".

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Industrial printers for the receptionists.

### ❌ D
> **D.** Configure the required amount of CPU and memory in the resource requests specification of the image rendering microservice deployment. Keep the resource requests for the other microservices at the default.

**Wrong words:**
- ❌ "**resource requests**" alone don't change the machine type.

📌 **When to use it:** Use requests for good scheduling.
🏢 **Office example:** Reserving desk size without changing the desk.

---

## 🛒 E-Commerce Full-Stack Example

Pool `render` (c2-standard-8) for `image-resizer`; `default-pool` (n2-standard-4) for the rest.

---

## 🧠 Key Takeaways / Memory Tips

- **Different hardware needs → separate node pools.**
  🧠 *"**Right pool for the job.**"*
- Related: **Q196**.

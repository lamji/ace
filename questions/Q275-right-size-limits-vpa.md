# Q275: Right-Size CPU/Memory Limits for Hundreds of Microservices (Vertical Pod Autoscaler per Microservice)

**Topic:** GKE (Vertical Pod Autoscaler)

## ❓ Question
> You have several hundred microservice applications running in a Google Kubernetes Engine (GKE) cluster. Each microservice is a deployment with resource limits configured for each container in the deployment. You've observed that the resource limits for memory and CPU are not appropriately set for many of the microservices. You want to ensure that each microservice has right sized limits for memory and CPU. What should you do?
>
> **A.** Configure a Vertical Pod Autoscaler for each microservice.
>
> **B.** Modify the cluster's node pool machine type and choose a machine type with more memory and CPU.
>
> **C.** Configure a Horizontal Pod Autoscaler for each microservice.
>
> **D.** Configure GKE cluster autoscaling.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Hundreds of microservices run on GKE, each with CPU and memory limits, but many limits are wrong.
- **What you must achieve:** Get correctly sized CPU and memory limits for each microservice.
- **The limits:** None stated.
- **What they're really asking:** Which GKE feature helps set the right CPU and memory for each one?

**Clues in the question:**
- "**right sized limits for memory and CPU**" → **VPA** adjusts requests/limits per pod.
- HPA changes **number** of pods; cluster autoscaler changes **nodes**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Vertical Pod Autoscaler 🔑
- **What it is:** Watches usage and sets (or recommends) each container's CPU/memory requests (limits scale proportionally).
- **Looks like:** `kind: VerticalPodAutoscaler … updateMode: "Auto"`
- **Not to be confused with:** HPA.
- **Analogy:** 🪑 Resizing each desk to fit the worker.
- **In the online store:** Right-size cart pods.

### 🔗 How they fit together
```
 VPA per Deployment → adjusts CPU/memory to real usage ✅
```

---

## 🌍 Real-World Scenario

A platform team adds a **VPA** to each Deployment; it right-sizes CPU and memory based on real usage.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Configure a Vertical Pod Autoscaler for each microservice.

**Why it's correct:**
- ✔️ "**Vertical Pod Autoscaler for each microservice**" matches "**right sized limits for memory and CPU**" for "**each microservice**".

📌 **When to use it:** Use it when you don't know how much power each program needs and want it adjusted to real use.
🏢 **Office example:** Resizing each worker's desk to fit what they actually use.

### ❌ B
> **B.** Modify the cluster's node pool machine type and choose a machine type with more memory and CPU.

**Wrong words:**
- ❌ "**machine type with more memory and CPU**": bigger nodes don't fix each pod's wrong settings.

📌 **When to use it:** Use bigger nodes when pods don't fit on current nodes.
🏢 **Office example:** Buying a bigger building when the desks are the wrong size.

### ❌ C
> **C.** Configure a Horizontal Pod Autoscaler for each microservice.

**Wrong words:**
- ❌ "**Horizontal Pod Autoscaler**": adds more pods with the same wrong sizes.

📌 **When to use it:** Use HPA for changing traffic.
🏢 **Office example:** Hiring more workers with badly sized desks.

### ❌ D
> **D.** Configure GKE cluster autoscaling.

**Wrong words:**
- ❌ "**cluster autoscaling**": adds nodes; pod sizes stay wrong.

📌 **When to use it:** Use it so there's room for new pods.
🏢 **Office example:** Renting more floors without fixing the desks.

---

## 🛒 E-Commerce Full-Stack Example

VPA `cart-vpa`, `catalog-vpa`, … with `updateMode: Auto` (or `Initial`).

---

## 🧠 Key Takeaways / Memory Tips

- **Right-size pod CPU/memory → VPA.** More pods → HPA. More nodes → cluster autoscaler.
  🧠 *"**Vertical = size of each pod.**"*
- Related: **Q249**, **Q182**.

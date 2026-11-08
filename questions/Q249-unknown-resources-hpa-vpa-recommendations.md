# Q249: Unknown Workload Needs: Stay Available and Get CPU/Memory Suggestions (HPA for Availability, VPA Recommendations for Suggestions)

**Topic:** GKE (HPA, VPA recommendation mode)

## ❓ Question
> Your manager asks you to deploy a workload to a Kubernetes cluster. You are not sure of the workload's resource requirements or how the requirements might vary depending on usage patterns, external dependencies, or other factors. You need a solution that makes cost-effective recommendations regarding CPU and memory requirements, and allows the workload to function consistently in any situation. You want to follow Google-recommended practices. What should you do?
>
> **A.** Configure the Horizontal Pod Autoscaler for availability, and configure the cluster autoscaler for suggestions.
>
> **B.** Configure the Horizontal Pod Autoscaler for availability, and configure the Vertical Pod Autoscaler recommendations for suggestions.
>
> **C.** Configure the Vertical Pod Autoscaler recommendations for availability, and configure the Cluster autoscaler for suggestions.
>
> **D.** Configure the Vertical Pod Autoscaler recommendations for availability, and configure the Horizontal Pod Autoscaler for suggestions.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your manager wants a workload on Kubernetes, but you don't know how much CPU and memory it needs or how that changes with usage.
- **What you must achieve:** Get cost-effective CPU and memory recommendations and keep the workload running well in any situation.
- **The limits:** Follow Google-recommended practices.
- **What they're really asking:** Which GKE feature figures out and adjusts the right CPU and memory for you?

**Clues in the question:**
- "**function consistently in any situation**" → **HPA** adds pods under load (availability).
- "**recommendations regarding CPU and memory**" → **VPA in recommendation mode** (`updateMode: Off`) suggests requests without changing pods.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. VPA recommendation mode 🔑
- **What it is:** VPA watches usage and **recommends** CPU/memory requests without applying them.
- **Looks like:** `updatePolicy: {updateMode: "Off"}` → `kubectl describe vpa`
- **Not to be confused with:** HPA.
- **Analogy:** 📋 A consultant's report on desk sizes.
- **In the online store:** Right-size cart pods.

### 2. HPA (review from Q182)
- **What it is:** Adds/removes pod copies by load.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 👥 More staff when busy.
- **In the online store:** —

### 🔗 How they fit together
```
 HPA → more pods when busy (availability) ✅
 VPA (Off mode) → recommended requests (suggestions) ✅
```

---

## 🌍 Real-World Scenario

A team deploys a new service with unknown needs. **HPA** keeps it up under load; **VPA in recommendation mode** reports what CPU/memory requests to set.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure the Horizontal Pod Autoscaler for availability, and configure the cluster autoscaler for suggestions.

**Wrong words:**
- ✔️ HPA for availability is right.
- ❌ "**cluster autoscaler for suggestions**": it adds nodes; it doesn't recommend pod CPU/memory.

📌 **When to use it:** Use cluster autoscaler so pods always have nodes to run on.
🏢 **Office example:** Asking the landlord for advice on desk sizes.

### ✅ B
> **B.** Configure the Horizontal Pod Autoscaler for availability, and configure the Vertical Pod Autoscaler recommendations for suggestions.

**Why it's correct:**
- ✔️ "**Horizontal Pod Autoscaler for availability**" matches "**function consistently in any situation**".
- ✔️ "**Vertical Pod Autoscaler recommendations for suggestions**" matches "**cost-effective recommendations regarding CPU and memory**".

📌 **When to use it:** Use it when you don't know how much a new system needs yet but it must keep working.
🏢 **Office example:** Calling in more staff when it's busy, and having a consultant suggest the right desk sizes.

### ❌ C
> **C.** Configure the Vertical Pod Autoscaler recommendations for availability, and configure the Cluster autoscaler for suggestions.

**Wrong words:**
- ❌ "**VPA recommendations for availability**": recommendations alone don't change anything.
- ❌ "**Cluster autoscaler for suggestions**": doesn't suggest.

📌 **When to use it:** **Never use this** mapping.
🏢 **Office example:** A report doesn't serve customers.

### ❌ D
> **D.** Configure the Vertical Pod Autoscaler recommendations for availability, and configure the Horizontal Pod Autoscaler for suggestions.

**Wrong words:**
- ❌ Roles swapped: "**VPA … for availability**" and "**HPA for suggestions**".

📌 **When to use it:** **Never use this** mapping.
🏢 **Office example:** Asking the extra staff to write the report.

---

## 🛒 E-Commerce Full-Stack Example

HPA `cart` (CPU 60%, 2–20 pods) + VPA `cart-vpa` (updateMode Off) → read recommendations weekly.

---

## 🧠 Key Takeaways / Memory Tips

- **Availability → HPA. CPU/memory suggestions → VPA recommendation mode.**
  🧠 *"**H for How many, V for How big.**"*
- Related: **Q275**, **Q182**.

# Q320: One-Replica Stateful App Needs More CPU at Peaks, Cost-Efficient Off-Peak (Vertical Pod Autoscaler)

**Topic:** GKE (VPA)

## ❓ Question
> You are managing a stateful application deployed on Google Kubernetes Engine (GKE) that can only have one replica. You recently discovered that the application becomes unstable at peak times. You have identified that the application needs more CPU than what has been configured in the manifest at these peak times. You want Kubernetes to allocate the application sufficient CPU resources during these peak times, while ensuring cost efficiency during off-peak periods. What should you do?
>
> **A.** Enable node auto-provisioning on the GKE cluster.
>
> **B.** Configure a Vertical Pod Autoscaler on the Deployment.
>
> **C.** Configure a Horizontal Pod Autoscaler on the Deployment.
>
> **D.** Enable cluster autoscaling on the GKE cluster.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A stateful app on GKE can only have one replica (one running copy). It becomes unstable at peak times because it needs more CPU than its manifest gives it.
- **What you must achieve:** Give it enough CPU at peak times.
- **The limits:** Stay cost-efficient when it's quiet, and it can still only have one copy.
- **What they're really asking:** Which feature gives the single Pod more CPU when needed?

**Clues in the question:**
- "**can only have one replica**" rules out HPA.
- "**more CPU than what has been configured**" → **VPA** adjusts requests up/down.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Vertical Pod Autoscaler (VPA) 🔑
- **What it is:** Adjusts a Pod's CPU/memory requests based on actual use.
- **Looks like:** `kind: VerticalPodAutoscaler … updatePolicy: updateMode: Auto`
- **Not to be confused with:** HPA (adds replicas).
- **Analogy:** 🪑 A bigger desk instead of more workers.
- **In the online store:** ShopNow single-writer inventory sync.

### 🔗 How they fit together
```
 1 replica + more CPU needed → VPA ✅ (HPA ✗)
```

---

## 🌍 Real-World Scenario

A single-replica stateful service gets **VPA** so its CPU request grows at peaks and shrinks off-peak.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable node auto-provisioning on the GKE cluster.

**Wrong words:**
- ❌ "**node auto-provisioning**": creates node pools, but the Pod's CPU request stays too low.

📌 **When to use it:** Use NAP when Pods can't fit on existing node types.
🏢 **Office example:** Building new rooms when the worker needs a bigger desk.

### ✅ B
> **B.** Configure a Vertical Pod Autoscaler on the Deployment.

**Why it's correct:**
- ✔️ "**Vertical Pod Autoscaler**" matches "**needs more CPU than what has been configured**" + "**can only have one replica**" + "**cost efficiency during off-peak**".

📌 **When to use it:** Use it when you can't add more workers, so the one worker needs more power at busy times.
🏢 **Office example:** Giving the one clerk a bigger desk during rush hour, then a smaller one later.

### ❌ C
> **C.** Configure a Horizontal Pod Autoscaler on the Deployment.

**Wrong words:**
- ❌ "**Horizontal Pod Autoscaler**": adds replicas, which isn't allowed.

📌 **When to use it:** Use HPA for stateless apps.
🏢 **Office example:** Hiring more clerks when only one is allowed.

### ❌ D
> **D.** Enable cluster autoscaling on the GKE cluster.

**Wrong words:**
- ❌ "**cluster autoscaling**": adds nodes; doesn't raise the Pod's CPU.

📌 **When to use it:** Use it when Pods can't be scheduled.
🏢 **Office example:** More rooms, same tiny desk.

---

## 🛒 E-Commerce Full-Stack Example

VPA `Auto` on `inventory-sync` (1 replica).

---

## 🧠 Key Takeaways / Memory Tips

- **One replica, needs more resources → VPA.**
  🧠 *"**Can't add Pods? Grow the Pod.**"*
- Related: **Q207**, **Q258**.

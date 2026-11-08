# Q252: Critical and Fault-Tolerant Parts on GKE, Cost-Optimized (Spot Pool for Fault-Tolerant, Standard Pool for Critical)

**Topic:** GKE (Spot node pools)

## ❓ Question
> Your company developed an application to deploy on Google Kubernetes Engine. Certain parts of the application are not fault-tolerant and are allowed to have downtime. Other parts of the application are critical and must always be available. You need to configure a Google Kubernetes Engine cluster while optimizing for cost. What should you do?
>
> **A.** Create a cluster with a single node-pool by using standard VMs. Label he fault-tolerant Deployments as spot_true.
>
> **B.** Create a cluster with a single node-pool by using Spot VMs. Label the critical Deployments as spot_false.
>
> **C.** Create a cluster with both a Spot VM node pool and a node pool by using standard VMs. Deploy the critical deployments on the Spot VM node pool and the fault-tolerant deployments on the node pool by using standard VMs.
>
> **D.** Create a cluster with both a Spot VM node pool and a nods pool by using standard VMs. Deploy the critical deployments on the node pool by using standard VMs and the fault-tolerant deployments on the Spot VM node pool.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app for GKE has parts that can tolerate downtime and parts that are critical and must always be up.
- **What you must achieve:** Set up a GKE cluster for both kinds of parts.
- **The limits:** Optimize for cost.
- **What they're really asking:** How do you set up node pools so the tolerant parts run cheaply and the critical parts stay up?

**Clues in the question:**
- "**allowed to have downtime**" → **Spot** pool (cheap, can be reclaimed).
- "**critical and must always be available**" → **standard** pool.
- Labels on Deployments don't change what VMs the nodes are.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Spot node pool 🔑
- **What it is:** A GKE node pool of Spot VMs: much cheaper, can be reclaimed anytime. Pods are steered with `nodeSelector: cloud.google.com/gke-spot: "true"`.
- **Looks like:** `gcloud container node-pools create spot --spot`
- **Not to be confused with:** standard pool.
- **Analogy:** 🪑 Discount desks that can be reclaimed.
- **In the online store:** Image resize jobs.

### 🔗 How they fit together
```
 pool standard → checkout, payments (critical) ✅
 pool spot     → thumbnailer, report workers (can wait) ✅
```

---

## 🌍 Real-World Scenario

An e-commerce cluster has two pools: **standard** for checkout and payments, **Spot** for thumbnail and report workers that can be interrupted.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a cluster with a single node-pool by using standard VMs. Label he fault-tolerant Deployments as spot_true.

**Wrong words:**
- ❌ "**single node-pool by using standard VMs**": no savings.
- ❌ "**Label … as spot_true**": a label doesn't make nodes Spot.

📌 **When to use it:** Use one standard pool when everything is critical.
🏢 **Office example:** Writing "discount" on a full-price desk.

### ❌ B
> **B.** Create a cluster with a single node-pool by using Spot VMs. Label the critical Deployments as spot_false.

**Wrong words:**
- ❌ "**single node-pool by using Spot VMs**": critical parts could be interrupted.
- ❌ "**Label … spot_false**": doesn't change the nodes.

📌 **When to use it:** Use an all-Spot pool only if everything tolerates interruptions.
🏢 **Office example:** Putting the cashier on a desk that may vanish.

### ❌ C
> **C.** Create a cluster with both a Spot VM node pool and a node pool by using standard VMs. Deploy the critical deployments on the Spot VM node pool and the fault-tolerant deployments on the node pool by using standard VMs.

**Wrong words:**
- ✔️ Two pools is right.
- ❌ Backwards: "**critical deployments on the Spot VM node pool**".

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Putting the cashier on the vanishing desk.

### ✅ D
> **D.** Create a cluster with both a Spot VM node pool and a nods pool by using standard VMs. Deploy the critical deployments on the node pool by using standard VMs and the fault-tolerant deployments on the Spot VM node pool.

**Why it's correct:**
- ✔️ "**both a Spot VM node pool and a … pool by using standard VMs**" matches "**optimizing for cost**".
- ✔️ "**critical deployments on the node pool by using standard VMs**" matches "**critical and must always be available**".
- ✔️ "**fault-tolerant deployments on the Spot VM node pool**" matches "**allowed to have downtime**".

📌 **When to use it:** Use it when some work can wait and some can't, and you want to save where it's safe.
🏢 **Office example:** Permanent desks for the cashiers, cheap hot-desks for tasks that can wait.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container node-pools create spot-pool --cluster=shopnow --spot`; thumbnailer `nodeSelector: cloud.google.com/gke-spot: "true"`; checkout stays on `default-pool`.

---

## 🧠 Key Takeaways / Memory Tips

- **Critical → standard pool. Can be interrupted → Spot pool.**
  🧠 *"**Spot for spare work, standard for the must-haves.**"*
- Related: **Q228**, **Q196**.

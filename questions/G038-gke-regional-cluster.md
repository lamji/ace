# G038: GKE Control Plane and Nodes Must Survive a Zone Outage (Regional Cluster)

**Topic:** GKE (regional clusters)
**Exam guide section:** 2.1 Deploying a GKE cluster with different configurations (e.g., GKE Autopilot, regional clusters, private clusters)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your production GKE Standard cluster must keep the Kubernetes control plane available and keep running workloads if an entire zone fails. What should you do?
>
> **A.** Create a zonal cluster with a large node pool in one zone.
>
> **B.** Create a regional cluster so that the control plane is replicated across zones and nodes run in multiple zones of the region.
>
> **C.** Create a zonal cluster and enable node auto-repair.
>
> **D.** Create two node pools in the same zone.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your production Kubernetes cluster (GKE Standard) runs important apps.
- **What you must achieve:** Keep both the control plane (the cluster's "brain" that manages everything) and the running apps going if a whole zone (one data center area) goes down.
- **The limits:** It must survive the loss of an entire zone.
- **What they're really asking:** Which kind of GKE cluster spreads both the brain and the workers across zones?

**Clues in the question:**
- "**control plane available … if an entire zone fails**": the control plane must be in **multiple zones**. That's a **regional cluster**.
- "**keep running workloads**": nodes in multiple zones too.

**Exam topic:** GKE (exam guide section 2.1).

---

## 📚 Key Terms Explained

### 1. Regional cluster 🔑
- **What it is:** A GKE cluster whose **control plane is replicated across three zones** in a region, with nodes spread across multiple zones. It survives a zone outage. Autopilot clusters are always regional.
- **Looks like:** `gcloud container clusters create shop-prod --region=us-central1 --num-nodes=2` (2 per zone × 3 zones)
- **Not to be confused with:** A zonal cluster, which has a single control plane in one zone.
- **Analogy:** 🏢 Three branch offices that each keep a copy of the head office's records.
- **In the online store:** ShopNow's production cluster.

### 2. Control plane
- **What it is:** The managed Kubernetes "brain" (API server, scheduler) that you talk to with kubectl.
- **Looks like:** `kubectl get pods` → the API server answers
- **Not to be confused with:** The nodes, which are the worker VMs that run Pods.
- **Analogy:** 🧠 The head office.
- **In the online store:** Upgraded by Google.

### 🔗 How they fit together
```
 Region us-central1
  zone a: control plane replica + nodes
  zone b: control plane replica + nodes   ← zone fails, others keep going ✅
  zone c: control plane replica + nodes
```

---

## 🌍 Real-World Scenario

During a zone outage, a retailer's zonal cluster API became unreachable, so they couldn't even scale. After moving to a **regional cluster**, the next zone incident passed without anyone noticing.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a zonal cluster with a large node pool in one zone.

**Wrong words:**
- ❌ "**zonal cluster … in one zone**": the control plane and all nodes sit in one zone. A zone outage takes everything down.

📌 **When to use it:** Use zonal clusters for dev or test where a short outage is acceptable.
🏢 **Office example:** One office, however big. A power cut stops it all.

### ✅ B
> **B.** Create a regional cluster so that the control plane is replicated across zones and nodes run in multiple zones of the region.

**Why it's correct:**
- ✔️ "**control plane is replicated across zones**" matches "**keep the Kubernetes control plane available … if an entire zone fails**".
- ✔️ "**nodes run in multiple zones of the region**" matches "**keep running workloads**".

📌 **When to use it:** Use it when the system must keep working even if one data center area goes down.
🏢 **Office example:** Running from three branch offices so one closure doesn't stop the business.

### ❌ C
> **C.** Create a zonal cluster and enable node auto-repair.

**Wrong words:**
- ✔️ Auto-repair fixes unhealthy nodes.
- ❌ "**zonal cluster**": auto-repair can't help when the whole zone, including the control plane, is down.

📌 **When to use it:** Use auto-repair on any cluster to replace broken nodes.
🏢 **Office example:** A handyman, but the building has no power.

### ❌ D
> **D.** Create two node pools in the same zone.

**Wrong words:**
- ❌ "**two node pools in the same zone**": still one zone, and the control plane isn't replicated.

📌 **When to use it:** Use multiple node pools for different machine types.
🏢 **Office example:** Two teams in the same office. A power cut hits both.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `shop-prod`: a regional cluster in us-central1, node pool `web` with 2 nodes per zone (6 total). PodDisruptionBudgets and topology spread keep replicas across zones.

---

## 🧠 Key Takeaways / Memory Tips

- **Survive a zone outage (control plane + nodes) → regional GKE cluster.** Zonal = single control plane.
  🧠 *"**Regional = three brains.**"*
- Related: **Q245**, **Q283** (Autopilot is regional), **Q147**.

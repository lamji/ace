# Q291: HA GKE, Prompt Node Security Updates, Pay Only for Workloads, No Node Management (Autopilot)

**Topic:** GKE (Autopilot vs Standard)

## ❓ Question
> You are planning to migrate your containerized workloads to Google Kubernetes Engine (GKE). You need to determine which GKE option to use. Your solution must have high availability, minimal downtime, and the ability to promptly apply security updates to your nodes. You also want to pay only for the compute resources that your workloads use without managing nodes. You want to follow Google-recommended practices and minimize operational costs. What should you do?
>
> **A.** Configure a Standard regional GKE duster.
>
> **B.** Configure a Standard zonal GKE duster.
>
> **C.** Configure a Standard multi-zonal GKE cluster.
>
> **D.** Configure an Autopilot GKE cluster.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** HA, quick node patching, **pay per workload**, **no node management**.

**Clues in the question:**
- "**pay only for the compute resources that your workloads use without managing nodes**" → **Autopilot** (billed per pod resources; Google manages and patches nodes).
- Autopilot is regional, which gives "**high availability**".

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. GKE Autopilot 🔑 (review from Q238)
- **What it is:** Google manages, scales and patches nodes; you pay for pod CPU/memory requests; always regional.
- **Looks like:** `gcloud container clusters create-auto prod --region=us-central1`
- **Not to be confused with:** Standard (you pay per node).
- **Analogy:** 🏨 Serviced apartment billed by the rooms you use.
- **In the online store:** ShopNow prod.

### 🔗 How they fit together
```
 Autopilot: regional ✅ + Google patches nodes ✅ + pay per pod ✅
```

---

## 🌍 Real-World Scenario

A company moving containers chooses **Autopilot**: regional HA, Google applies node security patches, and they pay only for what pods request.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure a Standard regional GKE duster.

**Wrong words:**
- ✔️ Regional gives HA.
- ❌ "**Standard**": you manage nodes and pay for whole nodes, even idle capacity.

📌 **When to use it:** Use Standard regional when you need node-level control and HA.
🏢 **Office example:** A sturdy building you must maintain and pay for fully.

### ❌ B
> **B.** Configure a Standard zonal GKE duster.

**Wrong words:**
- ❌ "**Standard zonal**": one zone, so no HA; nodes to manage.

📌 **When to use it:** Use zonal for dev/test.
🏢 **Office example:** One building, run by you.

### ❌ C
> **C.** Configure a Standard multi-zonal GKE cluster.

**Wrong words:**
- ❌ "**Standard multi-zonal**": control plane still in one zone; nodes to manage.

📌 **When to use it:** Use it when you want nodes in several zones with a cheaper control plane.
🏢 **Office example:** Desks in several buildings, one manager's office.

### ✅ D
> **D.** Configure an Autopilot GKE cluster.

**Why it's correct:**
- ✔️ "**Autopilot GKE cluster**" matches "**pay only for the compute resources that your workloads use without managing nodes**".
- ✔️ Regional + Google-managed patching matches "**high availability**" + "**promptly apply security updates to your nodes**".

📌 **When to use it:** Use it when you want Kubernetes without looking after or paying for idle machines.
🏢 **Office example:** A serviced office billed only for the desks your staff actually use.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container clusters create-auto shopnow-prod --region=us-central1 --release-channel=regular`

---

## 🧠 Key Takeaways / Memory Tips

- **No node management + pay per pod + HA → Autopilot.**
  🧠 *"**No nodes to manage? Autopilot.**"*
- Related: **Q238**, **Q267**, **Q283**.

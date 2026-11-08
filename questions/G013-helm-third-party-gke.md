# G013: Install a Vendor's App on Several GKE Clusters With Per-Cluster Settings, Easy Upgrade and Rollback (Helm)

**Topic:** Infrastructure as Code (Helm)
**Exam guide section:** 2.4 Planning and implementing resources using tooling: Infrastructure as Code tooling (Helm)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You need to install a third-party monitoring tool on several GKE clusters. The vendor publishes the tool as a Helm chart. Each cluster needs slightly different settings, such as the number of replicas and the storage size. You want simple upgrades and rollbacks. What should you do?
>
> **A.** Copy the vendor's Kubernetes YAML files into each cluster and edit them by hand for each cluster.
>
> **B.** Build a custom node image that includes the tool and use it for all GKE nodes.
>
> **C.** Use Helm with one values file per cluster, install the chart with helm install, and use helm upgrade and helm rollback to manage versions.
>
> **D.** Create Compute Engine VMs for each component of the tool with gcloud compute instances create.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You must install the same outside software (a monitoring tool) on several Kubernetes clusters (GKE: Google's managed Kubernetes). The vendor packages it as a Helm chart, a ready-made bundle of Kubernetes setup files.
- **What you must achieve:** Install it everywhere with a few different settings per cluster, and be able to update or undo updates easily.
- **The limits:** Settings differ per cluster, such as how many copies run (replicas) and how much storage it gets.
- **What they're really asking:** Which tool installs packaged Kubernetes apps with per-cluster settings and versioned upgrades and rollbacks?

**Clues in the question:**
- "**publishes the tool as a Helm chart**": use **Helm**, the Kubernetes package manager.
- "**slightly different settings**": a Helm **values file** per cluster.
- "**simple upgrades and rollbacks**": `helm upgrade` and `helm rollback` keep a release history.

**Exam topic:** Tooling and IaC (exam guide section 2.4).

---

## 📚 Key Terms Explained

### 1. Helm 🔑
- **What it is:** The package manager for Kubernetes. A **chart** is a package of templated Kubernetes YAML. You install it as a **release**, with settings from a **values file**. Helm tracks versions so you can upgrade or roll back.
- **Looks like:** `helm install mon vendor/monitor -f values-prod.yaml` / `helm rollback mon 3`
- **Not to be confused with:** kubectl, which applies plain YAML with no packaging or release history.
- **Analogy:** 📦 An app store installer with a settings screen and an undo button.
- **In the online store:** Installing the payment-fraud monitor on prod and staging.

### 2. Values file
- **What it is:** A YAML file holding the settings that fill in a chart's templates.
- **Looks like:** `replicaCount: 3\npersistence: {size: 50Gi}`
- **Not to be confused with:** The chart itself, which stays the same for every cluster.
- **Analogy:** 📝 The order form you fill out for each branch office.
- **In the online store:** `values-prod.yaml` vs `values-staging.yaml`.

### 🔗 How they fit together
```
 vendor/monitor chart ─┬─ values-prod.yaml  ─► helm install → prod cluster
                       └─ values-stage.yaml ─► helm install → staging cluster
 helm upgrade / helm rollback ✅
```

---

## 🌍 Real-World Scenario

A platform team runs prod, staging and dev GKE clusters. The vendor ships a Helm chart, so the team keeps three small values files in Git and runs `helm upgrade --install` from CI. When a bad upgrade breaks dashboards, `helm rollback` restores the previous release in seconds.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Copy the vendor's Kubernetes YAML files into each cluster and edit them by hand for each cluster.

**Wrong words:**
- ❌ "**edit them by hand for each cluster**": copies drift apart, and there's no release history for upgrades or rollbacks.

📌 **When to use it:** Use plain YAML for your own small apps when there's only one environment.
🏢 **Office example:** Retyping the same form for every branch office.

### ❌ B
> **B.** Build a custom node image that includes the tool and use it for all GKE nodes.

**Wrong words:**
- ❌ "**custom node image**": the tool runs as Kubernetes workloads, not baked into nodes, and every change would mean rebuilding nodes.

📌 **When to use it:** Use custom images for VM-level software you must preinstall.
🏢 **Office example:** Rebuilding the office to add a new printer.

### ✅ C
> **C.** Use Helm with one values file per cluster, install the chart with helm install, and use helm upgrade and helm rollback to manage versions.

**Why it's correct:**
- ✔️ "**Use Helm**" matches "**publishes the tool as a Helm chart**".
- ✔️ "**one values file per cluster**" matches "**slightly different settings**".
- ✔️ "**helm upgrade and helm rollback**" matches "**simple upgrades and rollbacks**".

📌 **When to use it:** Use it when you install a packaged app in several places with small differences and want an undo button.
🏢 **Office example:** A standard order form with a few boxes changed for each branch, and the old forms kept on file.

### ❌ D
> **D.** Create Compute Engine VMs for each component of the tool with gcloud compute instances create.

**Wrong words:**
- ❌ "**Compute Engine VMs for each component**": abandons Kubernetes and the vendor's chart entirely.

📌 **When to use it:** Use VMs for software that can't run in containers.
🏢 **Office example:** Renting separate offices for each part of one team.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**:
- `helm upgrade --install fraud-mon vendor/fraud-monitor -f values-prod.yaml -n monitoring` runs in Cloud Build for each cluster.
- Rollback: `helm rollback fraud-mon 4`.

---

## 🧠 Key Takeaways / Memory Tips

- **Packaged Kubernetes app + per-environment settings + upgrade/rollback → Helm (chart + values).**
  🧠 *"**Helm = app store for Kubernetes.**"*
- Related: **Q304**, **Q372**.

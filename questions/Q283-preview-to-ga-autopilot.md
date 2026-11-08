# Q283: From a Single-Zone Preview Cluster to Highly Available Production (Create an Autopilot Cluster)

**Topic:** GKE (regional/Autopilot clusters)

## ❓ Question
> Your preview application, deployed on a single-zone Google Kubernetes Engine (GKE) cluster in us-central1, has gained popularity. You are now ready to make the application generally available. You need to deploy the application to production while ensuring high availability and resilience. You also want to follow Google-recommended practices. What should you do?
>
> **A.** Use the gcloud container clusters create command with the options --enable-multi-networking and --enable-autoscaling to create an autoscaling zonal cluster and deploy the application to it.
>
> **B.** Use the gcloud container clusters create-auto command to create an autopilot cluster and deploy the application to it.
>
> **C.** Use the gcloud container clusters update command with the option --region us-central1 to update the cluster and deploy the application to it.
>
> **D.** Use the gcloud container clusters update command with the option --node-locations us-central1-a,us-central1-b to update the cluster and deploy the application to the nodes.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A preview app runs on a single-zone GKE cluster in us-central1 and has become popular.
- **What you must achieve:** Release it for everyone.
- **The limits:** High availability and resilience, following recommended practice.
- **What they're really asking:** What kind of cluster should production use?

**Clues in the question:**
- "**high availability and resilience**" → a **regional** cluster; **Autopilot** clusters are always regional and follow Google's best practices.
- A zonal cluster **can't be converted** to regional with `update --region`.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Regional cluster 🔑
- **What it is:** Control plane and nodes spread across 3 zones; survives a zone outage. Autopilot is always regional.
- **Looks like:** `gcloud container clusters create-auto prod --region=us-central1`
- **Not to be confused with:** zonal cluster.
- **Analogy:** 🏢🏢🏢 Offices in three buildings.
- **In the online store:** ShopNow prod.

### 2. --node-locations
- **What it is:** Adds node zones to a cluster, but a zonal cluster's control plane still lives in one zone.
- **Looks like:** —
- **Not to be confused with:** regional.
- **Analogy:** —
- **In the online store:** —

### 🔗 How they fit together
```
 preview: zonal (1 zone) → production: Autopilot (regional, 3 zones) ✅
```

---

## 🌍 Real-World Scenario

A startup's preview runs on a zonal cluster. For GA, they create a new **Autopilot** (regional) cluster and redeploy.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the gcloud container clusters create command with the options --enable-multi-networking and --enable-autoscaling to create an autoscaling zonal cluster and deploy the application to it.

**Wrong words:**
- ❌ "**create an autoscaling zonal cluster**": still one zone; a zone outage takes it down.
- ❌ "**--enable-multi-networking**": unrelated.

📌 **When to use it:** Use zonal clusters for dev/test.
🏢 **Office example:** A bigger office, still in one building.

### ✅ B
> **B.** Use the gcloud container clusters create-auto command to create an autopilot cluster and deploy the application to it.

**Why it's correct:**
- ✔️ "**create-auto … autopilot cluster**" matches "**high availability and resilience**": Autopilot is regional across zones.
- ✔️ It matches "**Google-recommended practices**": Google manages nodes and best-practice settings.

📌 **When to use it:** Use it when a growing service must keep running even if one site fails, with little upkeep.
🏢 **Office example:** Moving into a serviced office spread across three buildings.

### ❌ C
> **C.** Use the gcloud container clusters update command with the option --region us-central1 to update the cluster and deploy the application to it.

**Wrong words:**
- ❌ "**update … --region us-central1**": you can't change a zonal cluster into a regional one.

📌 **When to use it:** **Not possible** — create a new regional cluster.
🏢 **Office example:** Trying to turn one building into three by renaming it.

### ❌ D
> **D.** Use the gcloud container clusters update command with the option --node-locations us-central1-a,us-central1-b to update the cluster and deploy the application to the nodes.

**Wrong words:**
- ✔️ Nodes in more zones helps a bit.
- ❌ "**update … --node-locations**": the zonal **control plane** is still a single point of failure.

📌 **When to use it:** Use it to spread nodes of a regional cluster.
🏢 **Office example:** Desks in two buildings, but one manager's office in only one.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container clusters create-auto shopnow-prod --region=us-central1 --release-channel=stable` → redeploy manifests.

---

## 🧠 Key Takeaways / Memory Tips

- **HA production GKE → regional cluster; Autopilot is regional by default.** Zonal can't be converted.
  🧠 *"**Preview zonal, production regional.**"*
- Related: **Q238**, **Q245**.

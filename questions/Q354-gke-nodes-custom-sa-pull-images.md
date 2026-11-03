# Q354: GKE Must Pull Images From Artifact Registry Using a Prepared Service Account (Create Nodes With That Service Account)

**Topic:** GKE (node service accounts)

## ❓ Question
> You are storing your team’s container images in Artifact Registry. You need to create a new Google Kubernetes Engine (GKE) cluster and deploy these containers. You have already configured an IAM service account with the necessary permissions to pull images from Artifact Registry. You must ensure the images can be deployed on the GKE cluster. What should you do?
>
> **A.** In the Pod manifest, enter the service account name in the serviceAccountName field.
>
> **B.** Enable Workload Identity Federation for GKE on the cluster.
>
> **C.** Deploy the cluster nodes with the specified service account.
>
> **D.** After creating the cluster, store the service account JSON key in a Kubernetes Secret.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** SA already has Artifact Registry pull permission. Make GKE use it to pull images.

**Clues in the question:**
- Image pulls are done by the **node's** (kubelet's) identity → create nodes with **`--service-account`**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Node service account 🔑
- **What it is:** The IAM identity GKE nodes use for pulling images, writing logs/metrics.
- **Looks like:** `gcloud container clusters create app --service-account=gke-nodes@proj.iam.gserviceaccount.com`
- **Not to be confused with:** Pod identity (Workload Identity).
- **Analogy:** 🚚 The delivery truck's own access badge.
- **In the online store:** —

### 🔗 How they fit together
```
 node SA (artifactregistry.reader) → kubelet pulls images ✅
```

---

## 🌍 Real-World Scenario

The team creates the cluster with `--service-account=gke-nodes@…`, which has Artifact Registry Reader.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In the Pod manifest, enter the service account name in the serviceAccountName field.

**Wrong words:**
- ❌ "**serviceAccountName**": sets a Kubernetes SA for the Pod's own API calls, not image pulls.

📌 **When to use it:** Use it with Workload Identity for app API calls.
🏢 **Office example:** Giving the passenger a badge when the truck needs one.

### ❌ B
> **B.** Enable Workload Identity Federation for GKE on the cluster.

**Wrong words:**
- ❌ "**Workload Identity Federation**": for Pod API calls, not node image pulls.

📌 **When to use it:** Use it for Pods calling Google APIs.
🏢 **Office example:** Badges for workers, not the truck.

### ✅ C
> **C.** Deploy the cluster nodes with the specified service account.

**Why it's correct:**
- ✔️ "**Deploy the cluster nodes with the specified service account**" matches "**service account with the necessary permissions to pull images**" + "**images can be deployed on the GKE cluster**".

📌 **When to use it:** Use it when the machines themselves need permission to fetch your packages.
🏢 **Office example:** Giving the delivery truck the badge for the warehouse gate.

### ❌ D
> **D.** After creating the cluster, store the service account JSON key in a Kubernetes Secret.

**Wrong words:**
- ❌ "**JSON key in a Kubernetes Secret**": risky keys; unnecessary.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Taping the master key inside the truck.

---

## 🛒 E-Commerce Full-Stack Example

`gke-nodes@shopnow-prod` has `roles/artifactregistry.reader`; cluster created with it.

---

## 🧠 Key Takeaways / Memory Tips

- **Image pulls use the node SA → create nodes with the right SA.**
  🧠 *"**Nodes pull, nodes need the badge.**"*
- Related: **Q301**.

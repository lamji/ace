# Q145: New Pods Need Bigger Machines, No Downtime (Add a Node Pool With n2-highmem-16)

**Topic:** GKE (node pools, machine types, no-downtime changes)

## ❓ Question
> Your existing application running in Google Kubernetes Engine (GKE) consists of multiple pods running on four GKE n1-standard-2 nodes. You need to deploy additional pods requiring n2-highmem-16 nodes without any downtime. What should you do?
>
> **A.** Use gcloud container clusters upgrade. Deploy the new services.
>
> **B.** Create a new Node Pool and specify machine type n2-highmem-16. Deploy the new pods.
>
> **C.** Create a new cluster with n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.
>
> **D.** Create a new cluster with both n1-standard-2 and n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs as pods on four n1-standard-2 GKE nodes.
- **What you must achieve:** Deploy new pods that need bigger n2-highmem-16 nodes.
- **The limits:** No downtime.
- **What they're really asking:** How do you add the bigger machines without disrupting the current pods?

**Clues in the question:**
- "**additional pods requiring n2-highmem-16 nodes**": add a **node pool** of that machine type to the **same cluster**.
- "**without any downtime**": don't touch the existing pool or rebuild the cluster.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Node pool (review from Q081) 🔑
- **What it is:** A group of nodes in a cluster with the **same machine type**. A cluster can have pools of different types.
- **Looks like:** `gcloud container node-pools create highmem --cluster=shop --machine-type=n2-highmem-16`
- **Not to be confused with:** a new cluster.
- **Analogy:** 🏢 Adding a floor of bigger offices to the same building.
- **In the online store:** Analytics pods on highmem nodes.

### 2. cluster upgrade
- **What it is:** Updates the **Kubernetes version** of the control plane or nodes. It doesn't change machine types.
- **Looks like:** `gcloud container clusters upgrade shop --master`
- **Not to be confused with:** adding nodes.
- **Analogy:** 🔧 Renovating the building's systems.
- **In the online store:** Moving to a newer GKE version.

### 🔗 How they fit together
```
 cluster shop
   ├── default-pool: 4 × n1-standard-2 (existing pods keep running ✅)
   └── highmem-pool: n2-highmem-16 (new pods, via nodeSelector) ✅
```

---

## 🌍 Real-World Scenario

A team adds an in-memory analytics service to their GKE cluster. They create a **new node pool** with `n2-highmem-16`, then deploy the new pods with a nodeSelector for that pool. The website pods keep running the whole time.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use gcloud container clusters upgrade. Deploy the new services.

**Wrong words:**
- ❌ "**gcloud container clusters upgrade**": this changes the Kubernetes version, not machine types, and node upgrades restart nodes.

📌 **When to use it:** Use it to move the cluster to a newer GKE version.
🏢 **Office example:** Renovating the building when you needed bigger offices.

### ✅ B
> **B.** Create a new Node Pool and specify machine type n2-highmem-16. Deploy the new pods.

**Why it's correct:**
- ✔️ "**Create a new Node Pool and specify machine type n2-highmem-16**" matches "**additional pods requiring n2-highmem-16 nodes**".
- ✔️ "**Deploy the new pods**" (existing pool untouched) matches "**without any downtime**".

📌 **When to use it:** Use it when new work needs bigger machines and current work must keep running.
🏢 **Office example:** Adding a floor of big offices to the same building while everyone keeps working downstairs.

### ❌ C
> **C.** Create a new cluster with n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.

**Wrong words:**
- ❌ "**Create a new cluster … delete the old cluster**": a big migration with risk of downtime, and the old pods' n1-standard-2 nodes are gone.

📌 **When to use it:** Use a new cluster for major redesigns.
🏢 **Office example:** Moving the whole company to a new building to add one big office.

### ❌ D
> **D.** Create a new cluster with both n1-standard-2 and n2-highmem-16 nodes. Redeploy the pods and delete the old cluster.

**Wrong words:**
- ❌ "**Create a new cluster … Redeploy the pods and delete the old cluster**": the right mix of nodes, but far more work and downtime risk than adding a pool.

📌 **When to use it:** Use it only when the old cluster can't be changed.
🏢 **Office example:** Building an identical new building plus the extra floor, then moving everyone.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud container node-pools create analytics-highmem --cluster=shopnow-prod \
  --machine-type=n2-highmem-16 --num-nodes=2 --zone=us-central1-a
kubectl apply -f recommender-cache.yaml   # nodeSelector: cloud.google.com/gke-nodepool: analytics-highmem
```

---

## 🧠 Key Takeaways / Memory Tips

- **Different machine type in GKE → add a node pool** (no downtime).
- Cluster upgrade = Kubernetes version.
  🧠 *"**Need bigger nodes? Add a pool.**"*
- Related: **Q081** (GPU pool), **Q182** (autoscaling).

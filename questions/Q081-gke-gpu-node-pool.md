# Q081: Giving the ML Team GPUs in a Shared GKE Cluster (GPU Node Pool + nodeSelector)

**Topic:** GKE (node pools, GPUs, nodeSelector, cost)

## ❓ Question
> You are operating a Google Kubernetes Engine (GKE) cluster for your company where different teams can run non-production workloads. Your Machine Learning (ML) team needs access to Nvidia Tesla P100 GPUs to train their models. You want to minimize effort and cost. What should you do?
>
> **A.** Ask your ML team to add the "accelerator: gpu" annotation to their pod specification.
>
> **B.** Recreate all the nodes of the GKE cluster to enable GPUs on all of them.
>
> **C.** Create your own Kubernetes cluster on top of Compute Engine with nodes that have GPUs. Dedicate this cluster to your ML team.
>
> **D.** Add a new, GPU-enabled, node pool to the GKE cluster. Ask your ML team to add the cloud.google.com/gke -accelerator: nvidia-tesla-p100 nodeSelector to their pod specification.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A shared GKE cluster runs non-production work for many teams. The machine learning team needs Nvidia Tesla P100 GPUs (graphics chips used for fast ML training).
- **What you must achieve:** Give the ML team GPUs.
- **The limits:** Minimum effort and cost.
- **What they're really asking:** How should you add GPUs to the cluster for the ML team?

**Clues in the question:**
- "**Your Machine Learning (ML) team needs**": only **one team** needs GPUs, so don't put GPUs on every node.
- "**Nvidia Tesla P100 GPUs**": a specific GPU type, so the pods must land on nodes with **that** GPU.
- "**minimize effort and cost**": reuse the existing cluster (no new cluster to run), and pay for GPUs only on the few nodes that need them.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1️⃣ Node pool 🔑
- **What it is:** A **group of nodes (VMs) inside a GKE cluster that all have the same machine setup**. One cluster can have several node pools, for example a normal pool and a GPU pool.
- **Looks like:** `gcloud container node-pools create gpu-pool --cluster=shared --accelerator=type=nvidia-tesla-p100,count=1 --num-nodes=1`
- **Not to be confused with:** a whole new cluster. A node pool is just **extra machines added to the same cluster**.
- **Analogy:** 🏢 One office building, with **one floor of special workstations** for designers. Everyone else uses the normal floors.
- **In the online store:** ShopNow's cluster has a `default-pool` for the website and a `gpu-pool` for the recommendation model.

### 2️⃣ GPU
- **What it is:** A **graphics processor**, a chip that does huge amounts of math in parallel. Used to train machine learning models. Costly per hour.
- **Looks like:** `nvidia-tesla-p100`, `nvidia-tesla-t4`
- **Not to be confused with:** a faster CPU or disk.
- **Analogy:** 🧮 A room full of calculators.

### 3️⃣ nodeSelector
- **What it is:** A **line in the pod's YAML file** that says "only run me on nodes with this label". GKE automatically labels GPU nodes with `cloud.google.com/gke-accelerator: <gpu type>`.
- **Looks like:**
  ```yaml
  spec:
    nodeSelector:
      cloud.google.com/gke-accelerator: nvidia-tesla-p100
  ```
- **Not to be confused with:** an **annotation**, which is just a note on the pod and does **not** control where it runs.
- **Analogy:** 🪪 A note on the job ticket: "send this to the design floor only".
- **In the online store:** The training pod lands on the GPU node; the checkout pods never do.

### 4️⃣ Annotation
- **What it is:** A **free-text note** (key: value) attached to a Kubernetes object, read by tools. It does not decide which node a pod runs on.
- **Looks like:** `metadata: annotations: {owner: "ml-team"}`
- **Not to be confused with:** a nodeSelector or a resource request.

### 🔗 How they fit together
```
 GKE cluster "shared"
   ├── default-pool (normal VMs)  ← web, API, other teams' pods
   └── gpu-pool (P100 GPU VMs)    ← label cloud.google.com/gke-accelerator=nvidia-tesla-p100
                                     ▲
              ML pod with nodeSelector ┘  ✅
```

---

## 🌍 Real-World Scenario

A platform team runs one shared dev cluster. The data science team asks for GPUs. Instead of making every node expensive or building a second cluster, the engineer adds a small **GPU node pool** (it can even scale to zero when idle) and tells the ML team to add a **nodeSelector** so their training pods go to those nodes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ask your ML team to add the "accelerator: gpu" annotation to their pod specification.

**Wrong words:**
- ❌ "**add the "accelerator: gpu" annotation**": an annotation is only a note. It doesn't add GPUs to the cluster or send the pod to a GPU node. The cluster has **no GPU nodes** yet anyway.

📌 **When to use it:** Use annotations when you want to attach notes or settings that tools read, like who owns a pod.
🏢 **Office example:** Writing "needs a design workstation" on a sticky note when the office has no design workstations.

### ❌ B
> **B.** Recreate all the nodes of the GKE cluster to enable GPUs on all of them.

**Wrong words:**
- ❌ "**Recreate all the nodes**": lots of effort and disrupts every team.
- ❌ "**enable GPUs on all of them**": you pay for GPUs on every node, even though only the ML team uses them. Not "minimize cost".

📌 **When to use it:** Use it only when every workload in the cluster needs GPUs.
🏢 **Office example:** Buying expensive design workstations for every desk, including the accountants'.

### ❌ C
> **C.** Create your own Kubernetes cluster on top of Compute Engine with nodes that have GPUs. Dedicate this cluster to your ML team.

**Wrong words:**
- ❌ "**Create your own Kubernetes cluster on top of Compute Engine**": you'd install and run Kubernetes yourself, which is a lot of effort.
- ❌ "**Dedicate this cluster**": a second cluster to pay for and maintain. Not "minimize effort and cost".

📌 **When to use it:** Use it when a team must be completely separate and you need a custom Kubernetes setup GKE can't offer.
🏢 **Office example:** Building a whole new office building for one team that only needed one special room.

### ✅ D
> **D.** Add a new, GPU-enabled, node pool to the GKE cluster. Ask your ML team to add the cloud.google.com/gke -accelerator: nvidia-tesla-p100 nodeSelector to their pod specification.

**Why it's correct:**
- ✔️ "**Add a new, GPU-enabled, node pool to the GKE cluster**" matches "**minimize effort and cost**": you reuse the existing cluster and pay for GPUs only on the few new nodes.
- ✔️ "**GPU-enabled, node pool**" matches "**Your Machine Learning (ML) team needs access to Nvidia Tesla P100 GPUs**": the new pool has exactly the GPUs the ML team needs.
- ✔️ "**cloud.google.com/gke-accelerator: nvidia-tesla-p100 nodeSelector**" matches "**Nvidia Tesla P100**": the ML pods are sent only to nodes with P100 GPUs, and other teams' pods stay on the normal nodes.

📌 **When to use it:** Use it when only one team needs special, costly machines inside a shared setup.
🏢 **Office example:** Adding one floor of design workstations to the building and telling the designers to book that floor.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's shared dev cluster runs the storefront, API and tests. The ML team wants to train a "customers also bought" model.

```bash
gcloud container node-pools create gpu-pool --cluster=shopnow-dev --zone=us-central1-c \
  --accelerator=type=nvidia-tesla-p100,count=1 --num-nodes=1 \
  --enable-autoscaling --min-nodes=0 --max-nodes=2
```
```yaml
# recommender-training.yaml
spec:
  nodeSelector:
    cloud.google.com/gke-accelerator: nvidia-tesla-p100
  containers:
  - name: train
    resources: {limits: {nvidia.com/gpu: 1}}
```
The training job runs on the GPU node. When no training is running, the GPU pool shrinks to 0, so ShopNow pays nothing for GPUs.

---

## 🧠 Key Takeaways / Memory Tips

- **Special hardware for one team in GKE → add a node pool + nodeSelector.**
- Annotations are notes; they don't schedule pods.
- Don't put GPUs on every node, and don't build a second cluster.
  🧠 *"**New need? New node pool.**"*
- Related: **Q077** (GPUs vs local SSD), **Q072** (pod stuck Pending when no node fits).

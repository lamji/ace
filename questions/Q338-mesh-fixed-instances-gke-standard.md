# Q338: Micro-Frontend Containers With a Service Mesh, Control the Number of Compute Instances (GKE Standard Fixed Node Pool + Cloud Service Mesh)

**Topic:** GKE (Standard, Cloud Service Mesh)

## ❓ Question
> You are deploying a new frontend service for an online game. The service was built using a micro-frontend architecture and consists of multiple containers that interact using a service mesh. You need to control the number of compute instances that are running at a given time. What should you do?
>
> **A.** Create a Compute Engine instance template using a container-optimized virtual machine (VM) instance, and create a startup script that installs Istio service mesh. Deploy the service, and create a managed instance group with a fixed number of instances to run the service.
>
> **B.** Create a Cloud Run service specifying the minimum and maximum number of instances, and configure the service to use Cloud Service Mesh. Deploy all the containers to the service.
>
> **C.** Create a Google Kubernetes Engine (GKE) Autopilot cluster, and enable Cloud Service Mesh. Deploy the service, and use vertical and horizontal Pod autoscaling to control the cluster size.
>
> **D.** Create a Google Kubernetes Engine (GKE) Standard cluster with a node pool that has a fixed number of nodes. Enable the Cloud Service Mesh add-on, and deploy the service.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **D**. "**control the number of compute instances**" means you choose the node count, which only GKE Standard (fixed node pool) gives. Some pick B, but Cloud Run doesn't expose compute instances and mesh support there is limited.

---

## 📖 What the Question Is Asking

**In plain words:** Multiple containers + **service mesh**; **control how many compute instances run**.

**Clues in the question:**
- "**control the number of compute instances**" → **fixed node pool** (GKE Standard).
- "**service mesh**" → **Cloud Service Mesh** add-on.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Cloud Service Mesh 🔑
- **What it is:** Google's managed Istio-based mesh: traffic control, mTLS, observability between services.
- **Looks like:** `gcloud container fleet mesh enable`
- **Not to be confused with:** a load balancer.
- **Analogy:** 🛤️ Traffic controllers between departments.
- **In the online store:** —

### 2. Fixed node pool
- **What it is:** A node pool with autoscaling off and a set node count.
- **Looks like:** `--num-nodes=3 --no-enable-autoscaling`
- **Not to be confused with:** Autopilot (Google decides).
- **Analogy:** 🏢 Exactly three rented rooms.
- **In the online store:** —

### 🔗 How they fit together
```
 GKE Standard (node pool: 3 fixed) + Cloud Service Mesh ✅
```

---

## 🌍 Real-World Scenario

A game studio runs micro-frontends on **GKE Standard** with a **fixed 3-node pool** and **Cloud Service Mesh**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Compute Engine instance template using a container-optimized virtual machine (VM) instance, and create a startup script that installs Istio service mesh. Deploy the service, and create a managed instance group with a fixed number of instances to run the service.

**Wrong words:**
- ❌ "**startup script that installs Istio**" on VMs: heavy manual setup, not a managed mesh.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Building traffic controllers yourself.

### ❌ B
> **B.** Create a Cloud Run service specifying the minimum and maximum number of instances, and configure the service to use Cloud Service Mesh. Deploy all the containers to the service.

**Wrong words:**
- ❌ "**Cloud Run**": you set container instances, not compute instances; multi-container mesh support is limited.

📌 **When to use it:** Use Cloud Run for simple services.
🏢 **Office example:** Serviced desks where you can't choose the rooms.

### ❌ C
> **C.** Create a Google Kubernetes Engine (GKE) Autopilot cluster, and enable Cloud Service Mesh. Deploy the service, and use vertical and horizontal Pod autoscaling to control the cluster size.

**Wrong words:**
- ✔️ Mesh is right.
- ❌ "**Autopilot … autoscaling to control the cluster size**": Google controls nodes; you don't fix the count.

📌 **When to use it:** Use Autopilot when you don't care about node counts.
🏢 **Office example:** A serviced building deciding room count for you.

### ✅ D
> **D.** Create a Google Kubernetes Engine (GKE) Standard cluster with a node pool that has a fixed number of nodes. Enable the Cloud Service Mesh add-on, and deploy the service.

**Why it's correct:**
- ✔️ "**GKE Standard cluster with a node pool that has a fixed number of nodes**" matches "**control the number of compute instances that are running**".
- ✔️ "**Cloud Service Mesh add-on**" matches "**containers that interact using a service mesh**".

📌 **When to use it:** Use it when you must decide exactly how many machines run and your services need traffic rules between them.
🏢 **Office example:** Renting exactly three rooms and hiring traffic controllers between teams.

---

## 🛒 E-Commerce Full-Stack Example

GKE Standard `game-frontend`, pool `fixed-3`, Cloud Service Mesh enabled.

---

## 🧠 Key Takeaways / Memory Tips

- **Control node count → GKE Standard fixed pool. Mesh → Cloud Service Mesh.**
  🧠 *"**Fixed nodes = Standard.**"*
- Related: **Q291**.

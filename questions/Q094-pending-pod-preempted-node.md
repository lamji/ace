# Q094: One of Two Replicas Pending on a Preemptible Node Pool (Node Was Preempted, Pod Being Rescheduled)

**Topic:** GKE (Pod scheduling, Pending status, preemptible nodes)

## ❓ Question
> You create a Deployment with 2 replicas in a Google Kubernetes Engine cluster that has a single preemptible node pool. After a few minutes, you use kubectl to examine the status of your Pod and observe that one of them is still in Pending status:
>
> ```
> $ kubectl get pods -l app=myapp
> NAME                              READY   STATUS    RESTART   AGE
> myapp-deployment-58ddbbb995-lp86m 0/1     Pending   0         9m
> myapp-deployment-58ddbbb995-qjpkg 1/1     Running   0         9m
> ```
>
> What is the most likely cause?
>
> **A.** The pending Pod's resource requests are too large to fit on a single node of the cluster.
>
> **B.** Too many Pods are already running in the cluster, and there are not enough resources left to schedule the pending Pod.
>
> **C.** The node pool is configured with a service account that does not have permission to pull the container image used by the pending Pod.
>
> **D.** The pending Pod was originally scheduled on a node that has been preempted between the creation of the Deployment and your verification of the Pods' status. It is currently being rescheduled on a new node.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Correction:** I first marked **B**. The site's most-voted answer is **D**, and the user pointed this out. D fits the question's main clue: "**single preemptible node pool**". The question mentions preemptible nodes on purpose.
> 🔬 **Technical nuance (not needed for the exam):** in real Kubernetes, when a node disappears, its pod is usually **replaced by a new pod** with a new name and a younger AGE. Here both pods are 9m old, which some people use to argue for B. For the exam, follow the clue: **preemptible → D**.

---

## 📖 What the Question Is Asking

**In plain words:** Two identical pods. One is running, one is **Pending**. The cluster runs **only on preemptible nodes**. What most likely happened?

**Clues in the question:**
- "**single preemptible node pool**": preemptible VMs can be **taken away by Google at any time**. This detail is the main hint.
- "**2 replicas**" + "**one of them is still in Pending**": both pods are identical and one runs, so the pod **fits** on a node. That rules out A.
- "**Pending**" (not ImagePullBackOff): this isn't an image permission problem, which rules out C.
- "**between the creation of the Deployment and your verification**": in those few minutes, the node under one pod was preempted. The pod waits for a new node.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1️⃣ Preemptible node 🔑
- **What it is:** A **cheap VM that Google can stop at any time** (and always within 24 hours) when it needs the capacity back. GKE creates a new node to replace it, and the pods that were on it must be placed again.
- **Looks like:** `gcloud container node-pools create cheap-pool --cluster=dev --preemptible` (today's version is **Spot VMs**: `--spot`)
- **Not to be confused with:** a normal (on-demand) node, which Google doesn't take away.
- **Analogy:** 🪑 A **borrowed desk** the owner can take back without notice. You wait for another desk.
- **In the online store:** Cheap batch jobs, like nightly image resizing, run on preemptible nodes.

### 2️⃣ Pending status (review from Q072)
- **What it is:** A pod status meaning **"not running on any node right now"**. It's waiting for the scheduler to find a node with room.
- **Looks like:** `0/1   Pending` · `kubectl describe pod` → `Events: FailedScheduling …` or `node(s) were not ready`
- **Not to be confused with:** `ImagePullBackOff` (the pod has a node, but can't download its image).
- **Analogy:** 🪑 Standing in the lobby, **waiting for a desk**.

### 3️⃣ Rescheduling
- **What it is:** Kubernetes **placing a pod onto another node** after its node goes away. The Deployment keeps 2 replicas, so it makes sure a replacement runs as soon as a node is ready.
- **Analogy:** 🪑 Facilities finds the employee a new desk after the borrowed one is taken back.

### 🔗 How they fit together
```
 Deployment: 2 replicas, single PREEMPTIBLE node pool
   node-1 ── pod qjpkg ✅ Running
   node-2 ── pod lp86m … Google preempts node-2 ⚡
                          → pod lp86m Pending, waiting for a new node ✅ (D)
                          → GKE brings up a replacement node → pod runs again
```

---

## 🌍 Real-World Scenario

A team runs its dev cluster only on preemptible nodes to save money. Someone deploys 2 replicas, and minutes later one is Pending. Google reclaimed one node, and the pod is waiting while GKE brings up a replacement. A few minutes later both pods are Running again. This is normal with preemptible nodes, which is why production usually keeps at least one pool of regular nodes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** The pending Pod's resource requests are too large to fit on a single node of the cluster.

**Wrong words:**
- ❌ "**resource requests are too large to fit on a single node**": the other **identical** pod (same requests) is running on a node, so the size fits.

📌 **When to use it:** This is the cause when **every** replica is Pending because the pod needs more than any node has.
🏢 **Office example:** A new hire needs a desk bigger than any desk in the building.

### ❌ B
> **B.** Too many Pods are already running in the cluster, and there are not enough resources left to schedule the pending Pod.

**Wrong words:**
- ❌ "**Too many Pods are already running**": nothing in the question says other workloads fill the cluster.
- ❌ It ignores the main clue, "**single preemptible node pool**". Preemption is the more likely cause here.

📌 **When to use it:** This is the cause when `kubectl describe pod` shows `Insufficient cpu/memory` on a busy cluster with normal nodes.
🏢 **Office example:** Every desk is taken by other teams, so the new hire waits.

### ❌ C
> **C.** The node pool is configured with a service account that does not have permission to pull the container image used by the pending Pod.

**Wrong words:**
- ❌ "**does not have permission to pull the container image**": both pods use the **same image**, and one is running. An image problem also shows **ImagePullBackOff**, not Pending.

📌 **When to use it:** This is the cause when pods show `ImagePullBackOff` / `ErrImagePull` (see Q071).
🏢 **Office example:** The new hire has a desk but no key to the supply room.

### ✅ D
> **D.** The pending Pod was originally scheduled on a node that has been preempted between the creation of the Deployment and your verification of the Pods' status. It is currently being rescheduled on a new node.

**Why it's correct:**
- ✔️ "**a node that has been preempted**" matches "**a single preemptible node pool**": preemptible nodes can be taken away at any moment, which is the clue the question plants.
- ✔️ "**between the creation of the Deployment and your verification**" matches "**After a few minutes**": the node was lost during that short window.
- ✔️ "**It is currently being rescheduled on a new node**" matches "**still in Pending status**": Pending means it's waiting for a node, here the replacement node.
- ✔️ "**The pending Pod**" (only one) matches "**one of them**": only the pod on the lost node is affected. The other keeps running.

📌 **When to use it:** Think of this when you use cheap machines that can be taken away and one copy suddenly has to wait.
🏢 **Office example:** A borrowed desk was taken back, so that one employee waits in the lobby until facilities sets up another desk.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's dev cluster uses only preemptible (Spot) nodes to save about 70%.

```bash
kubectl get pods -l app=image-resizer
# image-resizer-58dd-lp86m  0/1  Pending  0  9m
# image-resizer-58dd-qjpkg  1/1  Running  0  9m
kubectl get events --sort-by=.lastTimestamp | tail -3
# Node gke-dev-spot-pool-a1b2 … Preempted / NodeNotReady
```
A few minutes later, GKE adds a fresh node and both pods run. For the **checkout** service in production, ShopNow keeps a regular node pool so preemption never takes it down.

---

## 🧠 Key Takeaways / Memory Tips

- **"Preemptible node pool" + one pod suddenly Pending → the node was preempted, and the pod is waiting for a new node.**
- One identical replica running → the pod size fits (not A). Pending ≠ image problem (not C).
- Exam rule: **if the question mentions a special detail like "preemptible", the answer usually uses it.**
  🧠 *"**Preemptible in the question? Preemption in the answer.**"*
- Related: **Q072** (describe the pending pod), **Q071** (image pull permissions), **Q081** (node pools).

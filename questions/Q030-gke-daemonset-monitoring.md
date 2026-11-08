# Q030: Running One Monitoring Pod on Every GKE Node (DaemonSet)

**Topic:** GKE / Kubernetes workloads (DaemonSet vs StatefulSet vs Deployment, cluster autoscaler)

## ❓ Question
> You are creating a Google Kubernetes Engine (GKE) cluster with a cluster autoscaler feature enabled. You need to make sure that each node of the cluster will run a monitoring pod that sends container metrics to a third-party monitoring solution. What should you do?
>
> **A.** Deploy the monitoring pod in a StatefulSet object.
>
> **B.** Deploy the monitoring pod in a DaemonSet object.
>
> **C.** Reference the monitoring pod in a Deployment object.
>
> **D.** Reference the monitoring pod in a cluster initializer at the GKE cluster creation time.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know (learned it now)

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are creating a GKE cluster (Google Kubernetes Engine) with the cluster autoscaler on (it adds and removes nodes, the machines in the cluster).
- **What you must achieve:** Every node, including nodes added later, must run one monitoring pod (a small container) that sends metrics to an outside monitoring tool.
- **The limits:** It must also cover nodes the autoscaler adds later.
- **What they're really asking:** What Kubernetes setup puts one copy of the monitoring pod on every node automatically?

| Keyword | What it hints at |
|---|---|
| "**each node**" | One copy **per node**, which is exactly what a **DaemonSet** does |
| "**cluster autoscaler**" | Nodes come and go, so new nodes must get the pod **automatically** |
| "**monitoring pod**" / "**container metrics**" | A classic **node agent** (log/metrics collector), the textbook DaemonSet use |

**Exam topic:** GKE / Kubernetes workloads.

---

## 📚 Key Terms Explained

### 1️⃣ Node
- **What it is:** **One VM (computer)** in your GKE cluster. Your containers run on nodes.
- **Looks like:** `gke-shopnow-pool-1-a1b2c3d4-xk9p` (an `e2-standard-4` VM)
- **Not to be confused with:** a pod. A node is the **machine**; pods are what run **on** it.
- **Analogy:** 🏢 **One office floor** in the building.
- **In the online store:** The cluster has 3 nodes on a normal day.

### 2️⃣ Pod
- **What it is:** The **smallest thing Kubernetes runs**: one (or a few) **containers** running together on one node.
- **Looks like:** `checkout-api-7d9f8b6c5-qwert` running the image `shopnow/checkout:1.4`
- **Not to be confused with:** a node (the machine) or a container image (the packaged app file). A pod is a **running copy** of the app.
- **Analogy:** 👤 **One worker at a desk** on a floor.

### 3️⃣ Cluster Autoscaler
- **What it is:** A GKE feature that **adds nodes** when pods don't fit and **removes nodes** when they're idle.
- **Looks like:** `gcloud container clusters create shop --enable-autoscaling --min-nodes=3 --max-nodes=10`
- **Not to be confused with:** the pod autoscaler (HPA), which adds **pods**, not **machines**.
- **Analogy:** 🏗️ The building **opens extra floors** when it's busy and **closes them** when it's quiet.
- **In the online store:** Black Friday → 3 nodes become 10 nodes.

### 4️⃣ DaemonSet ✅
- **What it is:** A Kubernetes object that runs **exactly one copy of a pod on every node**. When a **new node joins**, the pod is **added automatically**. When a node is removed, its copy goes too.
- **Looks like:**
  ```yaml
  apiVersion: apps/v1
  kind: DaemonSet
  metadata:
    name: metrics-agent
  spec:
    selector:
      matchLabels: {app: metrics-agent}
    template:
      metadata:
        labels: {app: metrics-agent}
      spec:
        containers:
        - name: agent
          image: datadog/agent:7
  ```
  *(No `replicas:` field. The number of copies = the number of nodes.)*
- **Not to be confused with:** a Deployment. A Deployment says "**N copies somewhere**". A DaemonSet says "**one on every node**".
- **Analogy:** 🧯 **One fire extinguisher per floor.** Open a new floor and it gets one automatically.
- **In the online store:** The metrics agent on every node reports CPU and memory of all ShopNow containers to Datadog.

### 5️⃣ Deployment
- **What it is:** Runs **a set number of identical pods** (`replicas: 3`) and keeps that number running. Kubernetes decides **which nodes** they land on.
- **Looks like:** `kind: Deployment` with `replicas: 3`
- **Not to be confused with:** a DaemonSet. 3 replicas could land on 2 nodes and skip the others, and new nodes don't get one.
- **Analogy:** 👥 "We need **3 receptionists** in the building", on whatever floors have space.
- **In the online store:** The checkout API runs as a Deployment with 3 replicas.

### 6️⃣ StatefulSet
- **What it is:** Like a Deployment, but each pod gets a **fixed name and its own permanent disk** (`db-0`, `db-1`). Built for **databases** and apps that store data.
- **Looks like:** `kind: StatefulSet`, pods `redis-0`, `redis-1`, each with its own disk.
- **Not to be confused with:** "one per node". It's about **stable identity + storage**, not node coverage.
- **Analogy:** 🗄️ **Numbered filing clerks**, each with their **own locked cabinet** that stays theirs.
- **In the online store:** A self-run Redis or Elasticsearch cluster.

### 🔗 How They Fit Together
```
GKE cluster (autoscaler: 3 → 5 nodes on Black Friday)
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│  Node 1    │ │  Node 2    │ │  Node 3    │ │  Node 4 🆕 │ │  Node 5 🆕 │
│ 📊 agent   │ │ 📊 agent   │ │ 📊 agent   │ │ 📊 agent   │ │ 📊 agent   │  ← DaemonSet: 1 per node, auto ✅
│ 🛒 checkout│ │ 🛒 checkout│ │            │ │ 🛒 checkout│ │            │  ← Deployment: N copies anywhere
└────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘
                     │
                     ▼
            📈 Third-party monitoring (Datadog, New Relic…)
```

---

## 🌍 Real-World Scenario

Almost every production Kubernetes cluster runs **agents on every node**: a **log collector** (Fluent Bit), a **metrics agent** (Datadog, Prometheus node-exporter), or a **security scanner**. Each agent watches **its own node**, so if a node has no agent, that node is **invisible** to monitoring. With autoscaling, nodes appear at 2 AM without anyone touching anything, so the agent must be **added automatically**. That's what DaemonSets are for. (GKE itself runs its own logging agent as a DaemonSet.)

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the monitoring pod in a StatefulSet object.

**Why it's wrong:**
- ❌ A StatefulSet gives pods **fixed names and their own disks**. It's for **databases**, and it **doesn't** place one pod per node.
- ❌ New nodes from the autoscaler **won't get** a monitoring pod.

**📌 When to use it:** Use it when each copy of an app needs its own name and its own storage that it keeps.
🏢 **Office example:** Numbered filing clerks, each with their own locked cabinet that nobody else uses.

### ✅ B
> **B.** Deploy the monitoring pod in a DaemonSet object.

**Why it's correct:**
- ✔️ Runs **one monitoring pod on every node**.
- ✔️ When the autoscaler **adds a node**, the pod is **added automatically**. When a node is removed, its pod goes away too.
- ✔️ This is the **standard Kubernetes way** to run node agents (logs, metrics, security).

**📌 When to use it:** Use it when every machine needs its own helper running on it, including new machines.
🏢 **Office example:** One fire extinguisher on every floor. When a new floor opens, it gets one too.

### ❌ C
> **C.** Reference the monitoring pod in a Deployment object.

**Why it's wrong:**
- ❌ A Deployment runs a **fixed number of copies** and **doesn't care which nodes** they're on. Some nodes may get two, others none.
- ❌ New nodes **don't** automatically get one.

**📌 When to use it:** Use it for normal apps where you just need a certain number of copies running.
🏢 **Office example:** "We need 3 receptionists in the building", without caring which floor each one sits on.

### ❌ D
> **D.** Reference the monitoring pod in a cluster initializer at the GKE cluster creation time.

**Why it's wrong:**
- ❌ There's **no "cluster initializer"** feature in GKE for this.
- ❌ Even if something ran at creation time, **nodes added later** by the autoscaler wouldn't get the pod.

**📌 When to use it:** **Never use this.** It doesn't exist. Use a DaemonSet (B).
🏢 **Office example:** Handing out fire extinguishers only on opening day, so every floor built later has none.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow runs its storefront and APIs on GKE with autoscaling (3–10 nodes). The ops team uses **Datadog** to watch container CPU, memory and errors.

```bash
kubectl apply -f metrics-agent-daemonset.yaml   # the YAML from Key Term 4
kubectl get daemonset metrics-agent
# NAME            DESIRED   CURRENT   READY   NODE SELECTOR
# metrics-agent   3         3         3       <none>
```

**Black Friday, 8 PM:** traffic spikes and the autoscaler adds 7 nodes.
```
# metrics-agent   10        10        10      ← went from 3 to 10 by itself ✅
```
Every new node is monitored within seconds. Nobody had to do anything.

| Approach | Black Friday result |
|---|---|
| **DaemonSet (B)** | 10 nodes, 10 agents. Every node monitored ✅ |
| Deployment, `replicas: 3` (C) | 3 agents on 3 nodes. **7 new nodes unmonitored**. The overloaded one crashes and nobody sees why ❌ |
| StatefulSet (A) | Same gap as C, plus unneeded disks ❌ |

---

## 🧠 Key Takeaways / Memory Tips

- **"Each node / every node" → DaemonSet.** No exceptions on the exam.
  🧠 *"**DaemonSet = one per node, like one fire extinguisher per floor.**"*
- **Quick comparison:**
  - **Deployment** → "N copies, anywhere" (web apps, APIs)
  - **StatefulSet** → "copies with fixed names + own disks" (databases)
  - **DaemonSet** → "one copy on every node" (log/metrics/security agents)
- DaemonSets **follow the autoscaler** automatically, both up and down.
- Related: **Q012** (deploying containers to GKE with `kubectl`).

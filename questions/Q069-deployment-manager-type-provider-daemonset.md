# Q069: Creating a GKE DaemonSet From the Same Deployment Manager Deployment (Type Provider)

**Topic:** Infrastructure as Code (Deployment Manager, Type Providers, Runtime Configurator, GKE DaemonSet in kube-system)

## ❓ Question
> You are using Deployment Manager to create a Google Kubernetes Engine cluster. Using the same Deployment Manager deployment, you also want to create a DaemonSet in the kube-system namespace of the cluster. You want a solution that uses the fewest possible services. What should you do?
>
> **A.** Add the cluster's API as a new Type Provider in Deployment Manager, and use the new type to create the DaemonSet.
>
> **B.** Use the Deployment Manager Runtime Configurator to create a new Config resource that contains the DaemonSet definition.
>
> **C.** With Deployment Manager, create a Compute Engine instance with a startup script that uses kubectl to create the DaemonSet.
>
> **D.** In the cluster's definition in Deployment Manager, add a metadata that has kube-system as key and the DaemonSet manifest as value.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

> ℹ️ **Real-life note:** Deployment Manager is being retired by Google (end of support in 2026). Teams now use **Terraform** (Infrastructure Manager), where the Kubernetes provider plays the same role as a Type Provider. The exam may still ask about Deployment Manager.

---

## 📖 What the Question Is Asking

**In plain words:** One Deployment Manager config already creates a GKE cluster. You want the **same** config to also create a **DaemonSet** (one pod on every node) inside the cluster, using as **few extra services** as possible.

**Clues in the question:**
- "**Using the same Deployment Manager deployment**": the DaemonSet must be a resource **inside Deployment Manager**, not something done separately.
- "**DaemonSet in the kube-system namespace**": that's a **Kubernetes** object. Deployment Manager only knows Google Cloud resources by default, so it must be taught to talk to the **cluster's Kubernetes API**.
- "**fewest possible services**": no extra VMs or scripts. Use Deployment Manager's own feature for this: a **Type Provider**.

**Exam topic:** Infrastructure as Code / GKE.

---

## 📚 Key Terms Explained

### 1️⃣ Deployment Manager (review from Q011)
- **What it is:** Google's **infrastructure-as-code** tool. You write a **YAML config** listing resources (VMs, clusters, buckets), and it creates them all as one **deployment**.
- **Looks like:**
  ```yaml
  resources:
  - name: shop-cluster
    type: container.v1.cluster
    properties: {zone: us-central1-a, cluster: {initialNodeCount: 3}}
  ```
- **Not to be confused with:** kubectl. Deployment Manager talks to **Google Cloud APIs**, not to Kubernetes, unless you add a Type Provider.
- **Analogy:** 📋 A **building contractor's order form**: list everything you want built, and the contractor builds it all.
- **In the online store:** One file creates ShopNow's cluster, network and buckets.

### 2️⃣ Type Provider 🔑
- **What it is:** A way to **teach Deployment Manager a new API**. You point it at an API's description (for GKE, the cluster's **Kubernetes API**), and then you can create that API's objects (Deployments, Services, DaemonSets) as normal Deployment Manager resources.
- **Looks like:**
  ```yaml
  - name: shop-k8s-provider
    type: deploymentmanager.v2beta.typeProvider
    properties:
      descriptorUrl: https://$(ref.shop-cluster.endpoint)/openapi/v2
  - name: log-agent
    type: my-project/shop-k8s-provider:/apis/apps/v1/namespaces/{namespace}/daemonsets
    properties: {namespace: kube-system, ...}
  ```
- **Not to be confused with:** a plug-in service you must run. It's a **built-in Deployment Manager feature**, so no extra service is added.
- **Analogy:** 📖 Giving the contractor a **new catalog** so they can also order furniture from a different supplier, on the same order form.
- **In the online store:** The same config builds the cluster **and** installs the log-collector DaemonSet.

### 3️⃣ DaemonSet in kube-system (review from Q030)
- **What it is:** A Kubernetes object that runs **one pod on every node**. `kube-system` is the namespace for **cluster-level helper tools** (log collectors, monitoring agents).
- **Looks like:** `kubectl get daemonsets -n kube-system` → `log-agent  3/3 ready`
- **Not to be confused with:** a Google Cloud resource. It lives **inside** the cluster, so Deployment Manager can't create it without a Type Provider.
- **Analogy:** 🧯 A **fire extinguisher on every floor**, managed by building maintenance.

### 4️⃣ Runtime Configurator
- **What it is:** A Deployment Manager feature that **stores key-value settings** (Config and Variable resources) and can make deployments **wait** for signals (Waiters).
- **Looks like:** `runtimeconfig.v1beta1.config` with variables like `db-host = 10.0.0.5`
- **Not to be confused with:** a tool that creates things. It only **stores settings**; storing a DaemonSet's YAML there doesn't create it in the cluster.
- **Analogy:** 📝 A **noticeboard** where you pin notes. Pinning a note saying "install extinguishers" doesn't install them.

### 5️⃣ Cluster metadata (in Deployment Manager)
- **What it is:** Key-value labels/settings passed to the cluster's **nodes (VMs)**.
- **Not to be confused with:** Kubernetes objects. Putting a manifest in metadata **doesn't apply it**; Kubernetes never reads it.
- **Analogy:** 🏷️ A **sticky note on the building**. Nobody reads it as an instruction.

### 🔗 How they fit together
```
 Deployment Manager deployment (one config)
   ├── container.v1.cluster           → 🏗️ GKE cluster
   ├── typeProvider (cluster's K8s API) → 📖 "now DM can speak Kubernetes"
   └── DaemonSet via that type         → 🧯 one pod per node in kube-system ✅
 No extra VMs, no scripts, no other services.
```

---

## 🌍 Real-World Scenario

Platform teams want **one config** that builds a ready-to-use cluster: the cluster plus required helper tools (log collectors, security agents) on every node. Rather than running a second tool after the cluster exists, they register the cluster's **Kubernetes API as a Type Provider**, so the same Deployment Manager config creates both the cluster and its DaemonSets. One deploy, one delete, everything tracked together.

---

## 🔍 Option-by-Option Breakdown

### ✅ A (your answer)
> **A.** Add the cluster's API as a new Type Provider in Deployment Manager, and use the new type to create the DaemonSet.

**Why it's correct:**
- ✔️ "**Add the cluster's API as a new Type Provider**" matches "**create a DaemonSet in the kube-system namespace of the cluster**": the Type Provider teaches Deployment Manager to talk to the cluster's Kubernetes API, where DaemonSets live.
- ✔️ "**use the new type to create the DaemonSet**" matches "**Using the same Deployment Manager deployment**": the DaemonSet becomes a normal resource in the same config, created and deleted together with the cluster.
- ✔️ "**in Deployment Manager**" matches "**fewest possible services**": it's a built-in Deployment Manager feature. No VMs, scripts or other services.

📌 **When to use it:** Use it when one setup file must build both the cloud resources and the things inside them.
🏢 **Office example:** Giving the contractor a second supplier's catalog so the same order form covers the building and its furniture.

### ❌ B
> **B.** Use the Deployment Manager Runtime Configurator to create a new Config resource that contains the DaemonSet definition.

**Wrong words:**
- ✔️ "Use the Deployment Manager Runtime Configurator" stays inside Deployment Manager.
- ❌ "**create a new Config resource that contains the DaemonSet definition**": a Config only **stores** text and settings. Nothing sends that definition to the cluster, so the DaemonSet is **never created**.

📌 **When to use it:** Use Runtime Configurator to share settings between resources or make a deployment wait until something is ready.
🏢 **Office example:** Pinning "install fire extinguishers" on the noticeboard. It's written down, but nobody installs them.

### ❌ C
> **C.** With Deployment Manager, create a Compute Engine instance with a startup script that uses kubectl to create the DaemonSet.

**Wrong words:**
- ❌ "**create a Compute Engine instance**": adds an **extra VM** just to run one command. That's another service (and cost), breaking "**fewest possible services**".
- ❌ "**startup script that uses kubectl**": the DaemonSet is created **outside** Deployment Manager, so the deployment doesn't track or delete it. You'd also have to give the VM credentials for the cluster.

📌 **When to use it:** Almost never. Use it only when no built-in way exists and you need a one-off setup task.
🏢 **Office example:** Hiring a temp just to walk in once and place the extinguishers, instead of putting them on the contractor's order.

### ❌ D
> **D.** In the cluster's definition in Deployment Manager, add a metadata that has kube-system as key and the DaemonSet manifest as value.

**Wrong words:**
- ❌ "**add a metadata that has kube-system as key and the DaemonSet manifest as value**": metadata is just labels/settings for the nodes. Kubernetes **never reads it as a manifest**, so nothing is created. This isn't a real feature.

📌 **When to use it:** **Never use this** to create Kubernetes objects. Use a Type Provider (A).
🏢 **Office example:** Sticking a note on the building saying "please install extinguishers" and expecting it to happen.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow wants every new cluster to come with a **log-collector DaemonSet** in `kube-system`.

```yaml
resources:
- name: shop-cluster                       # 1. the GKE cluster
  type: container.v1.cluster
  properties: {zone: us-central1-a, cluster: {name: shop-cluster, initialNodeCount: 3}}

- name: shop-k8s                           # 2. teach DM the cluster's Kubernetes API
  type: deploymentmanager.v2beta.typeProvider
  properties:
    descriptorUrl: https://$(ref.shop-cluster.endpoint)/openapi/v2

- name: log-agent                          # 3. the DaemonSet, same deployment
  type: shopnow-prod/shop-k8s:/apis/apps/v1/namespaces/{namespace}/daemonsets
  properties:
    namespace: kube-system
    apiVersion: apps/v1
    kind: DaemonSet
    metadata: {name: log-agent}
    spec: {...}
```

```bash
gcloud deployment-manager deployments create shop-platform --config=platform.yaml
# → cluster + log-agent on all 3 nodes, from ONE deployment
```

*(Simplified: a real Type Provider also needs authentication options for the cluster.)*

---

## 🧠 Key Takeaways / Memory Tips

- **Deployment Manager + something that isn't a Google Cloud resource (like Kubernetes objects) → Type Provider.**
- **Runtime Configurator stores settings; it doesn't create things.**
- **"Fewest services" rules out extra VMs and scripts.**
  🧠 *"**Type Provider = a new catalog for the same order form.**"*
- Related: **Q011** (Deployment Manager for infrastructure as code), **Q030** (DaemonSet = one pod per node).

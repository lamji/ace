# Q039: Keeping a GKE Cluster on a Supported Kubernetes Version

**Topic:** Google Kubernetes Engine (GKE) (node auto-upgrades, auto-repair, node images)

## ❓ Question
> You create a new Google Kubernetes Engine (GKE) cluster and want to make sure that it always runs a supported and stable version of Kubernetes. What should you do?
>
> **A.** Enable the Node Auto-Repair feature for your GKE cluster.
>
> **B.** Enable the Node Auto-Upgrades feature for your GKE cluster.
>
> **C.** Select the latest available cluster version for your GKE cluster.
>
> **D.** Select “Container-Optimized OS (COS)” as a node image for your GKE cluster.

*(The screenshot has encoding glitches around the quotation marks in D; they are shown here as normal quotation marks.)*

**My answer:** D
**Correct answer:** B — Enable the Node Auto-Upgrades feature for your GKE cluster.
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **D** is incorrect, but it is a reasonable mix-up: Container-Optimized OS is a recommended node operating system, while the question asks how to keep the **Kubernetes version** supported and stable over time.

**Correct answer: B — Enable the Node Auto-Upgrades feature for your GKE cluster.** Auto-upgrades let GKE move nodes to appropriate supported versions as the cluster is upgraded. Choosing an image or version once does not keep it current over time.

## 2. 📖 What the Question Is Asking

In plain words: after creating a Kubernetes cluster, how do you keep its software version maintained as GKE releases supported updates?

- **“always runs”** means ongoing maintenance, not a one-time selection.
- **“supported and stable version”** points to GKE’s managed upgrade process.
- **Exam topic:** GKE cluster lifecycle and node upgrades.

## 2.5 📚 Key Terms Explained

### Google Kubernetes Engine (GKE)
- **What it is:** Google Cloud's managed service for running Kubernetes clusters.
- **Analogy:** An office building where Google manages much of the building's infrastructure while your team organizes the work inside.
- **In the online store:** GKE can run the store's backend API and other containerized services.

### Kubernetes
- **What it is:** Software that runs and coordinates containerized applications across a group of machines.
- **Analogy:** An office coordinator assigning tasks to staff and replacing a worker when needed.
- **In the online store:** Kubernetes can keep the order API's application copies running.

### Cluster
- **What it is:** A Kubernetes environment made up of a control plane and worker machines called nodes.
- **Analogy:** An office site with a central manager and several work areas.
- **In the online store:** The GKE cluster is the environment where the store's backend containers run.

### Version
- **What it is:** A numbered release of Kubernetes and GKE software. Different versions include changes and fixes; versions can also reach the end of their supported period.
- **Analogy:** A dated edition of the office handbook.
- **In the online store:** The cluster and its nodes use Kubernetes versions to run the store's services.

### Supported and stable version
- **What it is:** A version still supported by Google and selected for production use based on its release status and stability. “Stable” does not mean no updates; fixes and upgrades still happen.
- **Analogy:** A current, approved edition of a handbook that the company continues to maintain.
- **In the online store:** Keeping the cluster on a supported version helps Google maintain its security and compatibility.

### Node
- **What it is:** A worker machine in a cluster that runs application containers.
- **Analogy:** A desk or workstation where office tasks get done.
- **In the online store:** Nodes run containers for the cart, inventory, or order API.

### Node auto-upgrades
- **What it is:** A GKE feature that automatically updates nodes to an appropriate Kubernetes version as upgrades are rolled out. GKE selects upgrade targets over time; it does not necessarily jump to every newest release immediately.
- **Analogy:** Automatically replacing office handbooks with the current approved edition as updates are issued.
- **In the online store:** It helps keep the machines running the store's containers aligned with supported GKE versions.

### Node auto-repair
- **What it is:** A feature that detects certain unhealthy nodes and repairs them, such as by recreating a node. It addresses node health, not keeping Kubernetes versions current.
- **Analogy:** Repairing or replacing a broken workstation.
- **In the online store:** It can restore a node that stops working so the store's containers can run elsewhere or after repair.

### Latest available cluster version
- **What it is:** The newest version available for a cluster's location at that moment. Selecting it sets a version at creation; it does not itself enable automatic future upgrades.
- **Analogy:** Choosing the newest handbook on the shelf today, without arranging future replacements.
- **In the online store:** It describes the cluster's initial Kubernetes version, not its ongoing upgrade policy.

### Node image
- **What it is:** The operating system image installed on a node. It is separate from the Kubernetes version.
- **Analogy:** The workstation's base setup, separate from the handbook used by the team.
- **In the online store:** The image is the operating system environment on machines that run the backend containers.

### Container-Optimized OS (COS)
- **What it is:** A Google-maintained operating system image designed for running containers. GKE documents it as a recommended node operating system; it does not automatically maintain the cluster's Kubernetes version.
- **Analogy:** A workstation configured for a particular kind of office work.
- **In the online store:** COS may be used as the operating system on GKE nodes running the store's application containers.

### How the terms fit together

```text
GKE cluster
├── Kubernetes version (managed over time with upgrades)
└── Worker nodes
    ├── Run application containers
    ├── Have a node image such as COS
    ├── Can be auto-upgraded to a supported Kubernetes version
    └── Can be auto-repaired if unhealthy
```

## 3. 🌍 Real-World Scenario

A team runs its online services on GKE. Kubernetes versions receive fixes and eventually leave support. The team wants GKE to handle node upgrades as supported targets become available, rather than relying on someone to remember to update every node. Auto-repair solves a different problem: recovering unhealthy nodes.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A

> **A.** Enable the Node Auto-Repair feature for your GKE cluster.

Auto-repair helps recover unhealthy nodes. It does not keep a healthy cluster's Kubernetes version current, so it does not meet the version requirement.

📌 When to use it: Use it when a workstation can fail and needs to be repaired automatically.  
🏢 Office example: Replace a broken desk computer so the employee can resume work.

### ✅ B — Correct

> **B.** Enable the Node Auto-Upgrades feature for your GKE cluster.

Node auto-upgrades keep nodes aligned with GKE's upgrade targets as the control plane is upgraded. GKE selects upgrade targets that have been assessed for stability, and rollouts are phased. Auto-upgrades do not necessarily install the newest release the moment it appears. For GKE clusters created through the console or `gcloud`, node auto-upgrade is enabled by default in supported configurations, but B is the option that directly addresses ongoing maintenance.

📌 When to use it: Use it when work machines should receive approved software updates over time.  
🏢 Office example: Automatically replace old handbook editions with the current approved one across the department.

### ❌ C

> **C.** Select the latest available cluster version for your GKE cluster.

This selects a version available at creation time, but it does not enable future automatic upgrades. Also, “latest” is not the same as “stable”: the newest available version may be in a faster release channel. Version selection alone cannot ensure the cluster stays supported and stable over time.

📌 When to use it: Use it when you need to choose a specific starting edition for a new system.  
🏢 Office example: Pick the newest approved handbook edition for a new office opening today.

### ❌ D — Your answer

> **D.** Select “Container-Optimized OS (COS)” as a node image for your GKE cluster.

COS is an operating system image for nodes, not a Kubernetes version or upgrade setting. It is a recommended node image, but choosing it does not keep Kubernetes current. GKE's own node auto-upgrade feature handles Kubernetes upgrades for nodes.

📌 When to use it: Use it when you want work machines set up with an operating system suited to running packaged applications.  
🏢 Office example: Choose a standard computer setup for the workstations in a new department.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow runs its Node.js order API in containers on GKE. Those containers run on worker nodes. Node auto-upgrades help keep the nodes aligned with supported Kubernetes versions as GKE rolls out updates. COS is a choice for the nodes' operating system; auto-repair would help recover an unhealthy node; choosing the latest cluster version sets the initial version but does not arrange future upgrades.

## 6. 🧠 Key Takeaway / Memory Tip

**Auto-repair fixes unhealthy nodes; auto-upgrade keeps node software current.** If the question says “always supported over time,” think **auto-upgrades**, not “pick latest once” or “choose an OS image.”

**Current documentation:** [Auto-upgrading nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades), [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning), [Node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images), and [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades).

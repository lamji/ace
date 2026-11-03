# Q072: Why Is a Pod Stuck in Pending? (Describe the Pod and Read Its Events)

**Topic:** GKE / Kubernetes troubleshooting (Pod status Pending, kubectl describe pod, events, logs vs events)

## ❓ Question
> You deployed a new application inside your Google Kubernetes Engine cluster using the YAML file specified below.
>
> *(YAML file shown as an image in the original: a Deployment `myapp-deployment` and a Service `myapp-service`.)*
>
> You check the status of the deployed pods and notice that one of them is still in PENDING status:
>
> *(Pod list shown as an image in the original: `myapp-deployment-58ddbbb995-lp86m` is `Pending`.)*
>
> You want to find out why the pod is stuck in pending status. What should you do?
>
> **A.** Review details of the myapp-service Service object and check for error messages.
>
> **B.** Review details of the myapp-deployment Deployment object and check for error messages.
>
> **C.** Review details of myapp-deployment-58ddbbb995-lp86m Pod and check for warning messages.
>
> **D.** View logs of the container in myapp-deployment-58ddbbb995-lp86m pod and check for warning messages.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** One pod won't start; it's stuck at **Pending**. Where do you look to find out **why**?

**Clues in the question:**
- "**PENDING status**": Pending means the pod **hasn't been placed on a node yet** (or its containers haven't started). The container never ran.
- "**one of them**": the problem is about **that specific pod**, so look at that pod.
- "**find out why**": Kubernetes records the reason as **events** on the pod, shown by `kubectl describe pod`.

**Exam topic:** GKE troubleshooting.

---

## 📚 Key Terms Explained

### 1️⃣ Pod and its status
- **What it is:** A **pod** is the smallest unit Kubernetes runs: one or more containers together. Its **status** says what stage it's in: `Pending` → `Running` → `Succeeded`/`Failed`.
- **Looks like:**
  ```
  NAME                                READY   STATUS    
  myapp-deployment-58ddbbb995-abcde   1/1     Running
  myapp-deployment-58ddbbb995-lp86m   0/1     Pending
  ```
- **Not to be confused with:** the Deployment (which creates pods) or the Service (which sends traffic to pods).
- **Analogy:** 👷 A **new hire** waiting for a desk. "Pending" = no desk assigned yet.
- **In the online store:** One of three checkout pods never starts.

### 2️⃣ Why pods stay Pending
- **What it is:** Usual reasons: **not enough CPU or memory** on any node, a **node selector or taint** that no node matches, or a **disk (volume)** that can't be attached.
- **Looks like:** `Warning  FailedScheduling  0/3 nodes are available: 3 Insufficient cpu.`
- **Analogy:** 🪑 No free desk big enough for the new hire.

### 3️⃣ `kubectl describe pod` and events 🔑
- **What it is:** A command that shows **everything about one pod**, ending with an **Events** list: Kubernetes' notes about what happened (scheduled, pulled image, failed scheduling, and why).
- **Looks like:**
  ```bash
  kubectl describe pod myapp-deployment-58ddbbb995-lp86m
  # ...
  # Events:
  #   Warning  FailedScheduling  default-scheduler  0/3 nodes are available: 3 Insufficient memory.
  ```
- **Not to be confused with:** logs. Events are Kubernetes' notes **about** the pod; logs are what **your app prints**.
- **Analogy:** 📋 The **HR file** for the new hire: "No desk available on any floor."
- **In the online store:** Shows the checkout pod asks for 4 GB of memory but no node has 4 GB free.

### 4️⃣ Container logs (`kubectl logs`)
- **What it is:** The text **your application prints** while it runs.
- **Looks like:** `kubectl logs myapp-deployment-58ddbbb995-lp86m`
- **Not to be confused with:** events. A Pending pod's container **never started**, so there are **no logs**.
- **Analogy:** 🗣️ What the employee **says at their desk**. If they never got a desk, they've said nothing.

### 5️⃣ Deployment and Service
- **What it is:** A **Deployment** keeps N copies of a pod running. A **Service** gives those pods one address and sends traffic to them.
- **Not to be confused with:** the pod. Neither one shows **why a single pod** couldn't be scheduled.
- **Analogy:** 🧑‍💼 The **hiring manager** (Deployment) and the **receptionist** (Service).

### 🔗 How they fit together
```
 Deployment myapp-deployment ──creates──► Pods (3 copies)
                                           ├── …abcde  Running
                                           ├── …fghij  Running
                                           └── …lp86m  Pending ← kubectl describe pod → Events: "Insufficient cpu" ✅
 Service myapp-service ──sends traffic──► Running pods only
```

---

## 🌍 Real-World Scenario

After a deploy, an engineer sees one pod stuck in Pending. The first command any Kubernetes admin runs is `kubectl describe pod <name>`. The Events at the bottom almost always say why: not enough CPU/memory, no node matches the pod's rules, or a disk can't attach. Then the fix is clear: lower the pod's requests, add nodes, or fix the rule.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Review details of the myapp-service Service object and check for error messages.

**Wrong words:**
- ❌ "**Review details of the myapp-service Service object**": a Service only routes traffic to pods. It has nothing to do with **scheduling** a pod onto a node, so it won't explain Pending.

📌 **When to use it:** Use it when pods are running but users can't reach the app.
🏢 **Office example:** Checking the receptionist's call log when the real problem is a new hire with no desk.

### ❌ B
> **B.** Review details of the myapp-deployment Deployment object and check for error messages.

**Wrong words:**
- ✔️ "myapp-deployment" is related: it created the pod.
- ❌ "**Review details of the myapp-deployment Deployment object**": the Deployment shows **how many** pods are ready (2/3), but not **why** one specific pod can't be scheduled. That reason is recorded on the **pod**.

📌 **When to use it:** Use it when the Deployment itself won't roll out, for example a bad image version or a stuck update.
🏢 **Office example:** Asking the hiring manager how many people started, when you need the new hire's own HR file to see why they have no desk.

### ✅ C
> **C.** Review details of myapp-deployment-58ddbbb995-lp86m Pod and check for warning messages.

**Why it's correct:**
- ✔️ "**Review details of myapp-deployment-58ddbbb995-lp86m Pod**" matches "**one of them is still in PENDING status**": it looks at exactly the pod that's stuck (`kubectl describe pod`).
- ✔️ "**check for warning messages**" matches "**find out why the pod is stuck**": the Events section shows warnings like `FailedScheduling: Insufficient cpu`, which is the reason.

📌 **When to use it:** Use it when one item is stuck and you need its own record to see the reason.
🏢 **Office example:** Opening the new hire's HR file, which says "no free desk on any floor".

### ❌ D
> **D.** View logs of the container in myapp-deployment-58ddbbb995-lp86m pod and check for warning messages.

**Wrong words:**
- ✔️ "myapp-deployment-58ddbbb995-lp86m pod" is the right pod.
- ❌ "**View logs of the container**": a Pending pod's container **has never started**, so it has **no logs**. Logs show what the app prints, not why Kubernetes couldn't place it.

📌 **When to use it:** Use logs when the pod is **Running** (or crashing) and you want to see the app's own errors.
🏢 **Office example:** Asking what the new hire said at their desk, when they never got a desk.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow deploys 3 `checkout` pods, each asking for 2 CPUs. One stays Pending.

```bash
kubectl get pods
# checkout-58ddbbb995-lp86m   0/1   Pending

kubectl describe pod checkout-58ddbbb995-lp86m
# Events:
#   Warning  FailedScheduling  0/3 nodes are available: 3 Insufficient cpu.

kubectl logs checkout-58ddbbb995-lp86m
# (nothing: the container never started)
```

Fix: lower the CPU request to 1, or let the cluster autoscaler add a node.

---

## 🧠 Key Takeaways / Memory Tips

- **Pod stuck in Pending → `kubectl describe pod <name>` → read the Events.**
- **Pending = never started = no logs.** Logs are for running or crashing pods.
- Service = traffic; Deployment = how many; **Pod = why this one failed.**
  🧠 *"**Pending? Describe it, don't log it.**"*
- Related: **Q030** (DaemonSet / workloads), **Q042** (Kubernetes objects).

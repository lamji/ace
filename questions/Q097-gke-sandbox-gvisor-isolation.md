# Q097: Isolating Customers' Pods That Run Arbitrary Code (GKE Sandbox with gVisor)

**Topic:** GKE security (GKE Sandbox / gVisor, RuntimeClass, Binary Authorization, Container Analysis)

## ❓ Question
> You are building a product on top of Google Kubernetes Engine (GKE). You have a single GKE cluster. For each of your customers, a Pod is running in that cluster, and your customers can run arbitrary code inside their Pod. You want to maximize the isolation between your customers' Pods. What should you do?
>
> **A.** Use Binary Authorization and whitelist only the container images used by your customers' Pods.
>
> **B.** Use the Container Analysis API to detect vulnerabilities in the containers used by your customers' Pods.
>
> **C.** Create a GKE node pool with a sandbox type configured to gvisor. Add the parameter runtimeClassName: gvisor to the specification of your customers' Pods.
>
> **D.** Use the cos_containerd image for your GKE nodes. Add a nodeSelector with the value cloud.google.com/gke-os-distribution: cos_containerd to the specification of your customers' Pods.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Customers can run **any code** inside their pods, all in one cluster. How do you **wall off** each customer's pod as strongly as possible?

**Clues in the question:**
- "**customers can run arbitrary code**": untrusted code that might try to break out of its container.
- "**maximize the isolation between your customers' Pods**": a **sandbox** around each pod → **GKE Sandbox (gVisor)**.
- Checking images (A, B) doesn't help, because the danger is the **code customers run**, not the image.

**Exam topic:** GKE security.

---

## 📚 Key Terms Explained

### 1️⃣ GKE Sandbox / gVisor 🔑
- **What it is:** gVisor is an **extra protective layer between a container and the node's operating system (kernel)**. GKE Sandbox turns it on for a node pool. If code escapes the container, it's still trapped in the sandbox, not on the node.
- **Looks like:** `gcloud container node-pools create sandbox-pool --cluster=saas --sandbox type=gvisor` + `runtimeClassName: gvisor` in the pod spec
- **Not to be confused with:** a normal container, which shares the node's kernel directly.
- **Analogy:** 🔒 Giving each visitor a **locked glass room** inside the office instead of an open desk.
- **In the online store:** Sellers upload custom pricing scripts that run in sandboxed pods.

### 2️⃣ runtimeClassName
- **What it is:** A **line in the pod's YAML** that picks which container runtime runs it. `gvisor` = run it in the sandbox.
- **Looks like:** `spec: runtimeClassName: gvisor`

### 3️⃣ Binary Authorization
- **What it is:** A rule that lets **only approved (signed) container images** be deployed.
- **Not to be confused with:** isolation. It controls **which images**, not **what code runs inside** them.
- **Analogy:** 🪪 Checking **visitors' ID** at the door. Doesn't stop them misbehaving inside.

### 4️⃣ Container Analysis
- **What it is:** Scans images for **known vulnerabilities** and reports them.
- **Not to be confused with:** protection at runtime. It only reports.

### 5️⃣ cos_containerd
- **What it is:** Google's **Container-Optimized OS** node image with the containerd runtime. It's now the **default**. It's a normal runtime, not a sandbox.

### 🔗 How they fit together
```
 Normal pod:   [container] → node kernel (shared)  ⚠️ escape = whole node
 Sandbox pod:  [container] → gVisor sandbox → node kernel   ✅ escape stays in sandbox
```

---

## 🌍 Real-World Scenario

A company sells an online coding platform. Each customer gets a pod and can run anything. To stop one customer from attacking the node or other customers, the team creates a **GKE Sandbox node pool (gVisor)** and sets `runtimeClassName: gvisor` on every customer pod.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Binary Authorization and whitelist only the container images used by your customers' Pods.

**Wrong words:**
- ❌ "**Use Binary Authorization and whitelist only the container images**": it controls **which images** can run, but customers run **arbitrary code** inside an allowed image. No isolation between pods.

📌 **When to use it:** Use it when only approved, signed images should ever be deployed.
🏢 **Office example:** Checking visitors' ID at the door, then letting them roam freely inside.

### ❌ B
> **B.** Use the Container Analysis API to detect vulnerabilities in the containers used by your customers' Pods.

**Wrong words:**
- ❌ "**detect vulnerabilities**": it only **reports** known weaknesses in images. It doesn't wall off pods or stop harmful code.

📌 **When to use it:** Use it to find known security holes in your images before deploying.
🏢 **Office example:** Inspecting visitors' bags for known dangerous items, but not watching what they do.

### ✅ C
> **C.** Create a GKE node pool with a sandbox type configured to gvisor. Add the parameter runtimeClassName: gvisor to the specification of your customers' Pods.

**Why it's correct:**
- ✔️ "**node pool with a sandbox type configured to gvisor**" matches "**maximize the isolation between your customers' Pods**": gVisor adds a strong wall between each pod and the node.
- ✔️ "**runtimeClassName: gvisor**" matches "**For each of your customers, a Pod**": every customer pod runs inside the sandbox.
- ✔️ "**sandbox**" matches "**customers can run arbitrary code**": even harmful code is trapped in the sandbox.

📌 **When to use it:** Use it when you run code from people you don't trust and must keep them apart.
🏢 **Office example:** Giving each outside visitor their own locked glass room instead of an open desk.

### ❌ D
> **D.** Use the cos_containerd image for your GKE nodes. Add a nodeSelector with the value cloud.google.com/gke-os-distribution: cos_containerd to the specification of your customers' Pods.

**Wrong words:**
- ❌ "**Use the cos_containerd image**": a normal (now default) node operating system. Containers still share the node's kernel, so there's no extra isolation.
- ❌ "**Add a nodeSelector … cos_containerd**": it only picks which nodes run the pods.

📌 **When to use it:** Use cos_containerd as the standard, secure node image for normal workloads.
🏢 **Office example:** Giving visitors the standard desks everyone uses. No extra walls.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow launches "Seller Scripts": each seller uploads custom code to calculate discounts, and it runs in that seller's pod.

```bash
gcloud container node-pools create seller-sandbox --cluster=shopnow-prod --sandbox type=gvisor
```
```yaml
spec:
  runtimeClassName: gvisor
  containers: [{name: seller-123, image: us-docker.pkg.dev/shopnow/sellers/runner:1.4}]
```
If one seller's script tries to attack the node, it's trapped in the gVisor sandbox.

---

## 🧠 Key Takeaways / Memory Tips

- **Untrusted / arbitrary code in GKE → GKE Sandbox (gVisor) + `runtimeClassName: gvisor`.**
- Binary Authorization = **which images**. Container Analysis = **scan images**. Neither isolates pods.
  🧠 *"**Strangers' code? Put it in a sandbox.**"*
- Related: **Q081** (node pools), **Q071** (image access).

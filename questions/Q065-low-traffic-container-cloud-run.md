# Q065: Cheapest Place to Run a Rarely-Used Container (Cloud Run Scales to Zero)

**Topic:** Choosing compute for containers (Cloud Run vs Cloud Run on GKE vs App Engine Flexible vs GKE; scale to zero; pay per request)

## ❓ Question
> You need to deploy an application, which is packaged in a container image, in a new project. The application exposes an HTTP endpoint and receives very few requests per day. You want to minimize costs. What should you do?
>
> **A.** Deploy the container on Cloud Run.
>
> **B.** Deploy the container on Cloud Run on GKE.
>
> **C.** Deploy the container on App Engine Flexible.
>
> **D.** Deploy the container on GKE with cluster autoscaling and horizontal pod autoscaling enabled.

**My answer:** D
**Correct answer:** A
**Result:** ❌ Incorrect

> Why D was tempting: "container" made you think "GKE". But a **container is just a package** for your app; it can run on **many** services (Cloud Run, GKE, App Engine Flexible, Compute Engine). GKE always keeps **nodes (VMs) running and billed**, even with 0 requests. Cloud Run can **scale to zero** and bill you **only while a request is being handled**.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app is packed as a container image and exposes an HTTP endpoint (a web address that receives requests). It receives very few requests per day.
- **What you must achieve:** Deploy it in a new project.
- **The limits:** Keep costs as low as possible.
- **What they're really asking:** Where should you run it so you pay as little as possible?

| Question words | What they point to |
|---|---|
| "**packaged in a container image**" | Any container platform works (Cloud Run, GKE, App Engine Flex). This alone doesn't pick GKE |
| "**exposes an HTTP endpoint**" | Request-driven web app → Cloud Run's sweet spot |
| "**very few requests per day**" | Idle almost all day → you want something that **scales to zero** |
| "**minimize costs**" | Pay only when used → **Cloud Run** (per-request billing) |
| "**in a new project**" | No existing cluster to reuse → don't build one just for this |

**Exam topic:** Choosing a compute service.

---

## 📚 Key Terms Explained

### 1️⃣ Container image 🔑
- **What it is:** A **package file** that holds your app plus everything it needs to run (code, libraries, settings). It runs the same way anywhere.
- **Looks like:** `us-docker.pkg.dev/shopnow/apps/receipt-api:1.0`
- **Not to be confused with:** GKE. A container is the **box**; GKE is **one of several trucks** that can carry it. Cloud Run, App Engine Flexible and Compute Engine can carry it too.
- **Analogy:** 📦 A **packed shipping box**. You can send it by courier, truck or plane.
- **In the online store:** The `receipt-api` app, packed once, can run on any container service.

### 2️⃣ Cloud Run 🔑
- **What it is:** A **fully managed** service that runs a container behind an HTTPS URL. It starts copies **when requests arrive** and goes down to **zero copies** when idle. You pay **only while requests are being handled** (and there's a monthly free tier).
- **Looks like:** `gcloud run deploy receipt-api --image=us-docker.pkg.dev/shopnow/apps/receipt-api:1.0 --region=us-central1`
- **Not to be confused with:** GKE. There's no cluster and no nodes to manage or pay for.
- **Analogy:** 🛎️ A **temp worker who's only paid for the minutes they're at the desk**, called in when the bell rings.
- **In the online store:** A tool used a few times a day by staff, costing almost nothing.

### 3️⃣ GKE (Google Kubernetes Engine)
- **What it is:** A managed **Kubernetes cluster**: a group of **VMs (nodes)** that run your containers. The nodes are **always running and billed**, and there's also a cluster management fee.
- **Looks like:** `gcloud container clusters create shop-cluster --num-nodes=3`
- **Not to be confused with:** "the place containers must run". It's the most powerful option, but also the most expensive and work-heavy for one small app.
- **Analogy:** 🏢 **Renting a whole office with full-time staff**, paid every hour whether or not visitors come.
- **In the online store:** The main storefront with many services and steady traffic.

### 4️⃣ Cluster autoscaling + Horizontal Pod Autoscaling (HPA)
- **What it is:** **Cluster autoscaling** adds/removes **nodes** (VMs). **HPA** adds/removes **pods** (copies of your app) based on load.
- **Looks like:** `--enable-autoscaling --min-nodes=1 --max-nodes=5` and `kubectl autoscale deployment receipt-api --min=1 --max=10`
- **Not to be confused with:** scaling to zero. The cluster still keeps **at least one node** (system components need it), so you still pay when there are no requests.
- **Analogy:** 📉 Sending staff home when it's quiet, but **at least one person must stay** to keep the office open.

### 5️⃣ App Engine Flexible
- **What it is:** App Engine that runs your container on **VMs it manages**. It keeps **at least one instance always running**.
- **Looks like:** `app.yaml` with `runtime: custom` and `env: flex`
- **Not to be confused with:** App Engine **Standard**, which can scale to zero (but doesn't take any container you give it).
- **Analogy:** 🧑‍💼 **One employee always at the desk**, paid all day even if nobody comes.

### 6️⃣ Cloud Run on GKE
- **What it is:** The Cloud Run developer experience, but running **inside your own GKE cluster** (now called Knative serving).
- **Not to be confused with:** Cloud Run (fully managed). You still pay for the **GKE cluster's nodes**.
- **Analogy:** 🛎️🏢 The temp-worker system, but you still **rent the whole office**.

### 🔗 How they fit together
```
 📦 container image
   ├─► Cloud Run              → 0 requests = 0 instances = ~$0  ✅ cheapest for rare traffic
   ├─► Cloud Run on GKE       → GKE nodes always on 💲💲
   ├─► App Engine Flexible    → ≥ 1 VM always on 💲💲
   └─► GKE (+ autoscaling)    → ≥ 1 node always on + cluster fee 💲💲
```

---

## 🌍 Real-World Scenario

Companies have lots of small internal tools: a webhook receiver, a report generator, an admin API. Each one gets a handful of requests per day. Running a VM or cluster for each one wastes money 24/7. Cloud Run is built for this: deploy the container, get a URL, and pay only for the seconds it's actually working. Many such apps cost **cents per month or fall within the free tier**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the container on Cloud Run.

**Why it's correct:**

- ✔️ "**Deploy the container**" matches "**packaged in a container image**": Cloud Run runs any container that listens for HTTP.
- ✔️ "**on Cloud Run**" matches "**exposes an HTTP endpoint**": Cloud Run gives the container an HTTPS URL and handles requests.
- ✔️ "**on Cloud Run**" (scales to zero) matches "**very few requests per day**", "**minimize costs**": Idle = 0 instances = no compute charge. You pay only during the few requests.
- ✔️ Fully managed, no cluster matches "**in a new project**": Nothing to set up first: no cluster, no nodes.

📌 **When to use it:** Use it when a web app is used only now and then and you want to pay only when it's actually working.
🏢 **Office example:** Calling in a temp worker only when a visitor rings the bell, and paying them only for those minutes.

### ❌ B
> **B.** Deploy the container on Cloud Run on GKE.

**Wrong words:**
- ✔️ "Deploy the container on Cloud Run" sounds right.
- ❌ "**on GKE**": it runs inside a GKE cluster, so you pay for the **cluster's nodes all day**, even with no requests. And the new project has no cluster, so you'd have to create one.

📌 **When to use it:** Use it when you already run a GKE cluster and want Cloud Run-style apps inside it.
🏢 **Office example:** Using the temp-worker system, but inside an office you rent full-time anyway.

### ❌ C
> **C.** Deploy the container on App Engine Flexible.

**Wrong words:**
- ✔️ "Deploy the container" is fine. App Engine Flexible does run containers.
- ❌ "**App Engine Flexible**": it keeps **at least one VM instance always running**, so you pay 24/7 for an app used a few times a day.

📌 **When to use it:** Use it when an app gets steady traffic all day and needs custom software that App Engine Standard doesn't support.
🏢 **Office example:** Keeping one receptionist at the desk all day, which is worth it only if visitors come all day.

### ❌ D (your answer)
> **D.** Deploy the container on GKE with cluster autoscaling and horizontal pod autoscaling enabled.

**Wrong words:**
- ✔️ "Deploy the container" is fine. GKE does run containers. *(But a container doesn't mean GKE.)*
- ❌ "**on GKE**": a cluster has **nodes (VMs) always running** plus a cluster management fee. For a few requests a day, you'd pay all day.
- ❌ "**with cluster autoscaling and horizontal pod autoscaling enabled**": this **shrinks** the cluster but **can't bring it to zero**. At least one node stays on, so costs don't go away.

📌 **When to use it:** Use it when you run many containers with steady, heavy traffic and need full control.
🏢 **Office example:** Renting a whole office that sends staff home when it's quiet, but someone must always stay to keep it open.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow has a small **"resend receipt" API** used by support staff about **20 times a day**.

```bash
gcloud run deploy receipt-api \
  --image=us-docker.pkg.dev/shopnow/apps/receipt-api:1.0 \
  --region=us-central1 --min-instances=0
```

| Option | Running when nobody calls it | Rough monthly cost for 20 requests/day |
|---|---|---|
| **A** Cloud Run | 0 instances | ~$0 (free tier) ✅ |
| B Cloud Run on GKE | GKE nodes | 💲💲 cluster + nodes |
| C App Engine Flex | ≥ 1 VM | 💲💲 a VM 24/7 |
| D GKE + autoscaling | ≥ 1 node + cluster fee | 💲💲 |

The main storefront (steady, heavy traffic) can stay on GKE. The rarely used tool goes on Cloud Run.

---

## 🧠 Key Takeaways / Memory Tips

- **Container ≠ GKE.** A container can run on Cloud Run, GKE, App Engine Flexible or Compute Engine.
- **"Container" + "HTTP" + "few requests" / "minimize cost" → Cloud Run** (scales to zero, pay per request).
- **GKE and App Engine Flexible always keep something running**, so you always pay.
  🧠 *"**Rarely used? Cloud Run: no requests, no bill.**"*
- Related: **Q012** (deploy a container to GKE), **Q064** (Cloud Run is request-driven), **Q037** (App Engine).

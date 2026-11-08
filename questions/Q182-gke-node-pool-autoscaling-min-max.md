# Q182: Cluster Must Grow as More Apps Are Deployed, No Manual Work (Node Pool Autoscaling With Min/Max)

**Topic:** GKE (cluster autoscaler vs HPA vs VPA)

## ❓ Question
> Your company has developed a new application that consists of multiple microservices. You want to deploy the application to Google Kubernetes Engine (GKE), and you want to ensure that the cluster can scale as more applications are deployed in the future. You want to avoid manual intervention when each new application is deployed. What should you do?
>
> **A.** Deploy the application on GKE, and add a HorizontalPodAutoscaler to the deployment.
>
> **B.** Deploy the application on GKE, and add a VerticalPodAutoscaler to the deployment.
>
> **C.** Create a GKE cluster with autoscaling enabled on the node pool. Set a minimum and maximum for the size of the node pool.
>
> **D.** Create a separate node pool for each application, and deploy each application to its dedicated node pool.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new app is made of several microservices, and you will deploy it to GKE.
- **What you must achieve:** The cluster must grow as more apps are added later.
- **The limits:** No manual work each time a new app is deployed.
- **What they're really asking:** How do you set up the cluster to add machines by itself?

**Clues in the question:**
- "**the cluster can scale as more applications are deployed**" → more **nodes** → **cluster autoscaler** on the node pool.
- HPA/VPA scale **pods** of one deployment, not the cluster.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Cluster autoscaler 🔑
- **What it is:** Adds or removes **nodes** in a node pool between a min and max, based on pods waiting for room.
- **Looks like:** `gcloud container clusters create shop --enable-autoscaling --min-nodes=1 --max-nodes=10`
- **Not to be confused with:** HPA (pods).
- **Analogy:** 🏢 Renting more floors when new teams arrive.
- **In the online store:** Room for new microservices.

### 2. HPA / VPA
- **What it is:** HPA = more **pod copies**. VPA = bigger **pod CPU/memory requests**. Both work inside one deployment.
- **Looks like:** `kubectl autoscale deployment cart --max=10`
- **Not to be confused with:** node scaling.
- **Analogy:** 👥 More staff / bigger desks in one team.
- **In the online store:** Scale checkout pods.

### 🔗 How they fit together
```
 new app deployed → pods Pending → cluster autoscaler adds node (≤ max) ✅
```

---

## 🌍 Real-World Scenario

A platform team expects new microservices every month. They enable **node pool autoscaling (1–20 nodes)** so deployments never wait for someone to add nodes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the application on GKE, and add a HorizontalPodAutoscaler to the deployment.

**Wrong words:**
- ❌ "**HorizontalPodAutoscaler to the deployment**": scales pods of **one** app. If the nodes are full, new apps still have nowhere to run.

📌 **When to use it:** Use HPA when one app's traffic goes up and down.
🏢 **Office example:** Adding staff to one team in a full building.

### ❌ B
> **B.** Deploy the application on GKE, and add a VerticalPodAutoscaler to the deployment.

**Wrong words:**
- ❌ "**VerticalPodAutoscaler**": resizes pods. It doesn't add nodes.

📌 **When to use it:** Use VPA to right-size pod CPU/memory.
🏢 **Office example:** Giving one person a bigger desk.

### ✅ C
> **C.** Create a GKE cluster with autoscaling enabled on the node pool. Set a minimum and maximum for the size of the node pool.

**Why it's correct:**
- ✔️ "**autoscaling enabled on the node pool**" matches "**cluster can scale as more applications are deployed**".
- ✔️ "**Set a minimum and maximum**" keeps it automatic but capped, which matches "**avoid manual intervention**".

📌 **When to use it:** Use it when more and more teams will move in and the space should grow by itself, within a limit.
🏢 **Office example:** A building lease that automatically adds floors as new teams arrive, up to a set maximum.

### ❌ D
> **D.** Create a separate node pool for each application, and deploy each application to its dedicated node pool.

**Wrong words:**
- ❌ "**separate node pool for each application**": that's manual work for every new app.

📌 **When to use it:** Use dedicated pools for apps needing special hardware.
🏢 **Office example:** Renting a new building for every new team.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container node-pools update default-pool --cluster=shopnow --enable-autoscaling --min-nodes=2 --max-nodes=15`

---

## 🧠 Key Takeaways / Memory Tips

- **Cluster must grow (more apps) → cluster autoscaler on the node pool.** HPA/VPA = pods.
  🧠 *"**More apps → more nodes → node autoscaling.**"*
- Related: **Q175**, **Q123**, **Q094**.

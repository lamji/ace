# Q267: Deploy With a Kubernetes Manifest, Full Control of the Deployment, Minimal Infrastructure Config (GKE Autopilot)

**Topic:** GKE (Autopilot vs Standard vs Cloud Run)

## ❓ Question
> You want to deploy a new containerized application into Google Cloud by using a Kubernetes manifest. You want to have full control over the Kubernetes deployment, and at the same time, you want to minimize configuring infrastructure. What should you do?
>
> **A.** Deploy the application on GKE Autopilot.
>
> **B.** Deploy the application on Cloud Run.
>
> **C.** Deploy the application on GKE Standard.
>
> **D.** Deploy the application on Cloud Functions.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will deploy a containerized app using a Kubernetes manifest (a YAML file describing what to run).
- **What you must achieve:** Have full control over the Kubernetes deployment.
- **The limits:** Do as little infrastructure setup as possible.
- **What they're really asking:** Which way of running Kubernetes gives control of deployments with the least infrastructure work?

**Clues in the question:**
- "**Kubernetes manifest**" + "**full control over the Kubernetes deployment**" → **GKE** (real Kubernetes API).
- "**minimize configuring infrastructure**" → **Autopilot** (Google manages nodes).

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. GKE Autopilot 🔑 (review from Q238)
- **What it is:** Full Kubernetes API for your workloads; Google manages nodes.
- **Looks like:** `kubectl apply -f deployment.yaml`
- **Not to be confused with:** Cloud Run.
- **Analogy:** 🏨 Serviced apartment where you arrange everything inside.
- **In the online store:** —

### 🔗 How they fit together
```
 manifest.yaml → kubectl apply → GKE Autopilot (nodes managed by Google) ✅
```

---

## 🌍 Real-World Scenario

A team with existing YAML manifests deploys to **GKE Autopilot**: they control Deployments, Services and HPAs, and never touch nodes.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the application on GKE Autopilot.

**Why it's correct:**
- ✔️ "**GKE Autopilot**" matches "**Kubernetes manifest**" + "**full control over the Kubernetes deployment**".
- ✔️ Google manages nodes, which matches "**minimize configuring infrastructure**".

📌 **When to use it:** Use it when you want Kubernetes features without looking after the machines.
🏢 **Office example:** A serviced apartment: you arrange everything inside, the landlord fixes the building.

### ❌ B
> **B.** Deploy the application on Cloud Run.

**Wrong words:**
- ❌ "**Cloud Run**": not a Kubernetes cluster; you don't get full control of Kubernetes Deployments.

📌 **When to use it:** Use Cloud Run for simple serverless containers.
🏢 **Office example:** A hotel room: you can't move the walls.

### ❌ C
> **C.** Deploy the application on GKE Standard.

**Wrong words:**
- ✔️ Full control.
- ❌ "**GKE Standard**": you configure node pools, against "**minimize configuring infrastructure**".

📌 **When to use it:** Use Standard when you need node-level control.
🏢 **Office example:** Owning and maintaining the whole building.

### ❌ D
> **D.** Deploy the application on Cloud Functions.

**Wrong words:**
- ❌ "**Cloud Functions**": source-code functions, no Kubernetes manifest.

📌 **When to use it:** Use Functions for small event handlers.
🏢 **Office example:** A vending machine, not an apartment.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container clusters create-auto shopnow-apps --region=us-central1` → `kubectl apply -f k8s/`

---

## 🧠 Key Takeaways / Memory Tips

- **Kubernetes manifests + low infra work → GKE Autopilot.**
  🧠 *"**Kubernetes control, Google's nodes.**"*
- Related: **Q238**, **Q245**.

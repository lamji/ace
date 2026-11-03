# Q233: Docker Images, No Infrastructure to Manage, Automatic Scaling (Artifact Registry + Cloud Run)

**Topic:** Serverless (Cloud Run vs GKE Standard vs MIG)

## ❓ Question
> Your application development team has created Docker images for an application that will be deployed on Google Cloud. Your team does not want to manage the infrastructure associated with this application. You need to ensure that the application can scale automatically as it gains popularity. What should you do?
>
> **A.** Create an instance template with the container image, and deploy a Managed Instance Group with Autoscaling.
>
> **B.** Upload Docker images to Artifact Registry, and deploy the application on Google Kubernetes Engine using Standard mode.
>
> **C.** Upload Docker images to the Cloud Storage, and deploy the application on Google Kubernetes Engine using Standard mode.
>
> **D.** Upload Docker images to Artifact Registry, and deploy the application on Cloud Run.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Containers, **no infrastructure to manage**, **auto-scaling**.

**Clues in the question:**
- "**does not want to manage the infrastructure**" → serverless → **Cloud Run**.
- "**scale automatically**" → Cloud Run scales per request.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run 🔑 (review from Q163)
- **What it is:** Runs containers without servers or clusters to manage; scales automatically.
- **Looks like:** `gcloud run deploy app --image=us-docker.pkg.dev/…`
- **Not to be confused with:** GKE Standard (you manage nodes).
- **Analogy:** 🚕 A taxi: you just ride.
- **In the online store:** Storefront.

### 2. GKE Standard mode
- **What it is:** You manage node pools, sizes and upgrades settings.
- **Looks like:** —
- **Not to be confused with:** Autopilot / Cloud Run.
- **Analogy:** 🚗 Owning a car.
- **In the online store:** —

### 🔗 How they fit together
```
 docker push → Artifact Registry → Cloud Run (auto-scales, no servers) ✅
```

---

## 🌍 Real-World Scenario

A startup pushes images to **Artifact Registry** and deploys to **Cloud Run**. Traffic spikes are handled automatically with no servers to look after.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an instance template with the container image, and deploy a Managed Instance Group with Autoscaling.

**Wrong words:**
- ❌ "**instance template … Managed Instance Group**": you still manage VMs, OS and updates.

📌 **When to use it:** Use MIGs when you need full VM control.
🏢 **Office example:** Leasing a fleet of cars you have to maintain.

### ❌ B
> **B.** Upload Docker images to Artifact Registry, and deploy the application on Google Kubernetes Engine using Standard mode.

**Wrong words:**
- ✔️ "Artifact Registry" is right.
- ❌ "**GKE using Standard mode**": you manage nodes and the cluster.

📌 **When to use it:** Use GKE Standard when you need detailed control of Kubernetes.
🏢 **Office example:** Buying cars and hiring mechanics.

### ❌ C
> **C.** Upload Docker images to the Cloud Storage, and deploy the application on Google Kubernetes Engine using Standard mode.

**Wrong words:**
- ❌ "**Cloud Storage**" (not a registry) and ❌ "**Standard mode**".

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Wrong garage and owning the cars.

### ✅ D
> **D.** Upload Docker images to Artifact Registry, and deploy the application on Cloud Run.

**Why it's correct:**
- ✔️ "**Upload Docker images to Artifact Registry**" matches "**created Docker images**".
- ✔️ "**deploy the application on Cloud Run**" matches "**does not want to manage the infrastructure**" + "**scale automatically**".

📌 **When to use it:** Use it when you have a packaged app and want it to grow with demand without running any servers.
🏢 **Office example:** Calling taxis: more come when more people need rides, and you never maintain a car.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy storefront --image=us-docker.pkg.dev/shopnow/apps/storefront:v5 --region=us-central1`

---

## 🧠 Key Takeaways / Memory Tips

- **Containers + no infrastructure + autoscale → Cloud Run.**
  🧠 *"**Container, no servers? Cloud Run.**"*
- Related: **Q163**, **Q236**, **Q226**.

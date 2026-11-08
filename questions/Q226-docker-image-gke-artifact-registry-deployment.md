# Q226: Deploy a Docker Image as a GKE Workload (Artifact Registry + Kubernetes Deployment)

**Topic:** GKE (Artifact Registry, Deployments)

## ❓ Question
> You have created an application that is packaged into a Docker image. You want to deploy the Docker image as a workload on Google Kubernetes Engine. What should you do?
>
> **A.** Upload the image to Cloud Storage and create a Kubernetes Service referencing the image.
>
> **B.** Upload the image to Cloud Storage and create a Kubernetes Deployment referencing the image.
>
> **C.** Upload the image to Artifact Registry and create a Kubernetes Service referencing the image.
>
> **D.** Upload the image to Artifact Registry and create a Kubernetes Deployment referencing the image.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app is packaged as a Docker image.
- **What you must achieve:** Run it as a workload on GKE.
- **The limits:** None stated.
- **What they're really asking:** What steps get the image running on GKE?

**Clues in the question:**
- Images → **Artifact Registry**. Run them → **Deployment**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Artifact Registry 🔑
- **What it is:** Google's current registry for container images and packages (replaces Container Registry).
- **Looks like:** `us-docker.pkg.dev/shopnow/apps/cart:v1`
- **Not to be confused with:** Cloud Storage.
- **Analogy:** 📚 The official image shelf.
- **In the online store:** ShopNow images.

### 2. Deployment vs Service (review from Q192)
- **What it is:** Deployment runs pods from an image; Service gives them an address.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 👥 Team vs 📞 phone number.
- **In the online store:** —

### 🔗 How they fit together
```
 docker push → Artifact Registry ─► Deployment (pods) ✅
```

---

## 🌍 Real-World Scenario

A developer pushes `cart:v2` to **Artifact Registry** and updates the **Deployment** to use it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Upload the image to Cloud Storage and create a Kubernetes Service referencing the image.

**Wrong words:**
- ❌ "**Cloud Storage**" and ❌ "**Service referencing the image**".

📌 **When to use it:** Use Cloud Storage for files; Services for networking.
🏢 **Office example:** Wrong cabinet, and a phone number with no staff.

### ❌ B
> **B.** Upload the image to Cloud Storage and create a Kubernetes Deployment referencing the image.

**Wrong words:**
- ✔️ "Deployment" is right.
- ❌ "**Cloud Storage**": not a registry.

📌 **When to use it:** Use Cloud Storage for regular files.
🏢 **Office example:** Right team, wrong cabinet.

### ❌ C
> **C.** Upload the image to Artifact Registry and create a Kubernetes Service referencing the image.

**Wrong words:**
- ✔️ "Artifact Registry" is right.
- ❌ "**Service referencing the image**": Services don't run images.

📌 **When to use it:** Use a Service to expose running pods.
🏢 **Office example:** A phone number with nobody behind it.

### ✅ D
> **D.** Upload the image to Artifact Registry and create a Kubernetes Deployment referencing the image.

**Why it's correct:**
- ✔️ "**Upload the image to Artifact Registry**" matches "**packaged into a Docker image**".
- ✔️ "**create a Kubernetes Deployment referencing the image**" matches "**deploy … as a workload**".

📌 **When to use it:** Use it whenever you want to run your packaged app on Kubernetes.
🏢 **Office example:** Putting the blueprint on the official shelf and assigning a team to build from it.

---

## 🛒 E-Commerce Full-Stack Example

`kubectl set image deployment/cart cart=us-docker.pkg.dev/shopnow/apps/cart:v2`

---

## 🧠 Key Takeaways / Memory Tips

- **Image → Artifact Registry. Run → Deployment.**
  🧠 *"**Registry stores, Deployment runs.**"*
- Related: **Q192**, **Q233**.

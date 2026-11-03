# Q192: Deploy a Docker Image as a GKE Workload (Container Registry + Kubernetes Deployment)

**Topic:** GKE (image registries, Deployments vs Services)

## ❓ Question
> You have created an application that is packaged into a Docker image. You want to deploy the Docker image as a workload on Google Kubernetes Engine. What should you do?
>
> **A.** Upload the image to Cloud Storage and create a Kubernetes Service referencing the image.
>
> **B.** Upload the image to Cloud Storage and create a Kubernetes Deployment referencing the image.
>
> **C.** Upload the image to Container Registry and create a Kubernetes Service referencing the image.
>
> **D.** Upload the image to Container Registry and create a Kubernetes Deployment referencing the image.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Where do you put the image, and which Kubernetes object runs it?

**Clues in the question:**
- Images go in a **registry** (Container Registry, today **Artifact Registry**), not Cloud Storage.
- A **workload** that runs containers is a **Deployment**. A Service only gives pods a network address.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Container Registry / Artifact Registry 🔑
- **What it is:** A storage service made for **container images**, with tags and versions. Artifact Registry is the newer replacement.
- **Looks like:** `docker push us-docker.pkg.dev/shop/apps/cart:v1`
- **Not to be confused with:** Cloud Storage buckets.
- **Analogy:** 📚 A library shelf made just for images.
- **In the online store:** ShopNow images.

### 2. Deployment vs Service
- **What it is:** **Deployment** runs and scales pods from an image. **Service** gives those pods one stable address. It doesn't reference an image.
- **Looks like:** `kind: Deployment … image: …` / `kind: Service … selector: app=cart`
- **Not to be confused with:** each other.
- **Analogy:** 👥 The team vs 📞 the team's phone number.
- **In the online store:** cart Deployment + cart Service.

### 🔗 How they fit together
```
 docker push → registry ─image─► Deployment (pods) ◄─ Service (address)
```

---

## 🌍 Real-World Scenario

A developer pushes `cart:v1` to the registry and applies a **Deployment** that references it. Later they add a Service so other pods can reach it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Upload the image to Cloud Storage and create a Kubernetes Service referencing the image.

**Wrong words:**
- ❌ "**Cloud Storage**": not an image registry.
- ❌ "**Service referencing the image**": Services don't run images.

📌 **When to use it:** Use Cloud Storage for files; Services for networking.
🏢 **Office example:** Filing the blueprint in a drawer and giving a phone number to nobody.

### ❌ B
> **B.** Upload the image to Cloud Storage and create a Kubernetes Deployment referencing the image.

**Wrong words:**
- ✔️ "Deployment" is right.
- ❌ "**Cloud Storage**": GKE pulls images from a registry, not a bucket.

📌 **When to use it:** Use Cloud Storage for regular files.
🏢 **Office example:** The right team, but the blueprint is in the wrong cabinet.

### ❌ C
> **C.** Upload the image to Container Registry and create a Kubernetes Service referencing the image.

**Wrong words:**
- ✔️ "Container Registry" is right.
- ❌ "**Service referencing the image**": a Service routes traffic. It doesn't run containers.

📌 **When to use it:** Use a Service to give running pods a stable address.
🏢 **Office example:** A phone number with no staff behind it.

### ✅ D
> **D.** Upload the image to Container Registry and create a Kubernetes Deployment referencing the image.

**Why it's correct:**
- ✔️ "**Upload the image to Container Registry**" matches "**packaged into a Docker image**": a registry stores images for GKE to pull.
- ✔️ "**create a Kubernetes Deployment referencing the image**" matches "**deploy … as a workload**".

📌 **When to use it:** Use it whenever you want to run your packaged app on Kubernetes.
🏢 **Office example:** Putting the blueprint on the official shelf and assigning a team to build from it.

---

## 🛒 E-Commerce Full-Stack Example

```bash
docker push us-docker.pkg.dev/shopnow/apps/cart:v1
kubectl create deployment cart --image=us-docker.pkg.dev/shopnow/apps/cart:v1
```

---

## 🧠 Key Takeaways / Memory Tips

- **Image → registry. Run it → Deployment.** Service = network address.
  🧠 *"**Registry stores, Deployment runs, Service connects.**"*
- Related: **Q226** (same, Artifact Registry), **Q175**.

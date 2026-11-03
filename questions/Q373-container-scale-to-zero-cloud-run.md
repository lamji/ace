# Q373: Ship a Container Image to Production Fast, Must Scale to Zero (Cloud Run)

**Topic:** Serverless (Cloud Run)

## ❓ Question
> Your development team has packaged and pushed a new container image to Artifact Registry. Due to design requirements, the application must be able to scale to zero. You need to take this image to production as quickly as possible while following the design requirements. What should you do?
>
> **A.** Create an instance template for the container, and use it to create a managed instance group behind an external Application Load Balancer.
>
> **B.** Create an app.yaml file that specifies the container images, and deploy it to the App Engine Flexible environment.
>
> **C.** Write a Kubernetes Deployment and a Service manifest (YAML), and apply them to a Google Kubernetes Engine cluster.
>
> **D.** Deploy the application directly to Cloud Run.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Container image ready; **scale to zero**; **as quickly as possible**.

**Clues in the question:**
- "**scale to zero**" + container + fastest → **Cloud Run** (deploy the image directly).

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run 🔑 (review)
- **What it is:** Deploy a container image with one command; scales to zero.
- **Looks like:** `gcloud run deploy app --image=us-docker.pkg.dev/proj/repo/app:v1`
- **Not to be confused with:** App Engine Flexible (min 1 instance).
- **Analogy:** 🏨 Serviced desk.
- **In the online store:** —

### 🔗 How they fit together
```
 Artifact Registry image → gcloud run deploy → scale 0..N ✅
```

---

## 🌍 Real-World Scenario

The team deploys the image straight to **Cloud Run**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an instance template for the container, and use it to create a managed instance group behind an external Application Load Balancer.

**Wrong words:**
- ❌ "**managed instance group**": VMs don't scale to zero behind an LB; more setup.

📌 **When to use it:** Use MIGs for VM workloads.
🏢 **Office example:** Leasing desks that stay rented.

### ❌ B
> **B.** Create an app.yaml file that specifies the container images, and deploy it to the App Engine Flexible environment.

**Wrong words:**
- ❌ "**App Engine Flexible**": at least one instance always runs; no scale to zero.

📌 **When to use it:** Use Flex for App Engine apps needing custom runtimes.
🏢 **Office example:** A desk that's always staffed.

### ❌ C
> **C.** Write a Kubernetes Deployment and a Service manifest (YAML), and apply them to a Google Kubernetes Engine cluster.

**Wrong words:**
- ❌ "**Kubernetes Deployment … GKE cluster**": cluster setup; nodes don't scale to zero easily.

📌 **When to use it:** Use GKE for complex platforms.
🏢 **Office example:** Building an office first.

### ✅ D
> **D.** Deploy the application directly to Cloud Run.

**Why it's correct:**
- ✔️ "**Deploy the application directly to Cloud Run**" matches "**scale to zero**" + "**as quickly as possible**".

📌 **When to use it:** Use it when you have a ready-packed app and want it live fast, costing nothing when idle.
🏢 **Office example:** Moving into a serviced desk the same day, billed only when used.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy promo-api --image=...:v3 --region=us-central1`

---

## 🧠 Key Takeaways / Memory Tips

- **Container + scale to zero + fast → Cloud Run.**
  🧠 *"**Zero idle? Cloud Run.**"*
- Related: **Q315**, **Q330**.

# Q315: Static Website and HTTP-Triggered Monthly Job, Multi-Location, Scale to Zero (Both on Cloud Run)

**Topic:** Serverless (Cloud Run)

## ❓ Question
> You are planning to move your company's website and a specific asynchronous background job to Google Cloud. Your website contains only static HTML content. The background job is started through an HTTP endpoint and generates monthly invoices for your customers. Your website needs to be available in multiple geographic locations and requires autoscaling. You want to have no costs when your workloads are not in use and follow recommended practices. What should you do?
>
> **A.** Move your website to Google Kubernetes Engine (GKE), and move your background job to Cloud Functions.
>
> **B.** Move both your website and background job to Compute Engine.
>
> **C.** Move both your website and background job to Cloud Run.
>
> **D.** Move your website to Google Kubernetes Engine (GKE), and move your background job to Compute Engine.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are moving a static HTML website and a monthly invoice job (started by calling an HTTP address) to Google Cloud.
- **What you must achieve:** Host both.
- **The limits:** The website must be in several locations and autoscale; pay nothing when idle; follow recommended practice.
- **What they're really asking:** Where should the website and the job run?

**Clues in the question:**
- "**no costs when your workloads are not in use**" + "**autoscaling**" → **Cloud Run** for both (deploy in multiple regions).

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run 🔑 (review)
- **What it is:** Serverless containers; scales to zero; deploy to several regions behind a load balancer.
- **Looks like:** —
- **Not to be confused with:** GKE / VMs.
- **Analogy:** 🏨 Serviced desks.
- **In the online store:** —

### 🔗 How they fit together
```
 site → Cloud Run (multi-region)   job → Cloud Run (HTTP) ✅
```

---

## 🌍 Real-World Scenario

A company runs its static site and invoice job on **Cloud Run**; both scale to zero.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Move your website to Google Kubernetes Engine (GKE), and move your background job to Cloud Functions.

**Wrong words:**
- ❌ "**GKE**" for the website: nodes cost money when idle.
- ✔️ Cloud Functions for the job would be fine alone.

📌 **When to use it:** Use GKE for steady container platforms.
🏢 **Office example:** A rented office for a brochure.

### ❌ B
> **B.** Move both your website and background job to Compute Engine.

**Wrong words:**
- ❌ "**Compute Engine**": VMs bill when idle; no automatic multi-location scaling.

📌 **When to use it:** Use VMs for full OS control.
🏢 **Office example:** Staffed desks 24/7.

### ✅ C
> **C.** Move both your website and background job to Cloud Run.

**Why it's correct:**
- ✔️ "**Cloud Run**" matches "**requires autoscaling**" + "**no costs when your workloads are not in use**".
- ✔️ Cloud Run deploys to many regions, matching "**available in multiple geographic locations**", and handles HTTP-started jobs.

📌 **When to use it:** Use it when both a simple site and a request-started task should cost nothing while idle.
🏢 **Office example:** Serviced desks in several cities that only bill when someone works.

### ❌ D
> **D.** Move your website to Google Kubernetes Engine (GKE), and move your background job to Compute Engine.

**Wrong words:**
- ❌ "**GKE**" + "**Compute Engine**": idle costs everywhere.

📌 **When to use it:** **Avoid** for scale-to-zero needs.
🏢 **Office example:** Paying rent for two always-open offices.

---

## 🛒 E-Commerce Full-Stack Example

`shopnow-landing` in us-central1 + europe-west1 behind a global LB; `invoice-runner` service.

---

## 🧠 Key Takeaways / Memory Tips

- **Scale to zero + autoscaling for HTTP workloads → Cloud Run.**
  🧠 *"**Idle = free: Cloud Run.**"*
- Related: **Q305**, **Q373**.

# Q175: Scale Each Microservice Separately on GKE (One Deployment per Microservice)

**Topic:** GKE (Deployments vs Jobs vs CRDs)

## ❓ Question
> You have developed an application that consists of multiple microservices, with each microservice packaged in its own Docker container image. You want to deploy the entire application on Google Kubernetes Engine so that each microservice can be scaled individually. What should you do?
>
> **A.** Create and deploy a Custom Resource Definition per microservice.
>
> **B.** Create and deploy a Docker Compose File.
>
> **C.** Create and deploy a Job per microservice.
>
> **D.** Create and deploy a Deployment per microservice.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app is made of several microservices (small separate services), each in its own Docker container image.
- **What you must achieve:** Run the whole app on GKE so each microservice can be scaled on its own.
- **The limits:** Each one must scale separately.
- **What they're really asking:** How should you deploy the microservices on GKE?

**Clues in the question:**
- "**each microservice can be scaled individually**" → one **Deployment** per microservice (each has its own `replicas`).

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Deployment 🔑
- **What it is:** A Kubernetes object that keeps **N copies (pods)** of one container running and lets you scale and update them.
- **Looks like:** `kubectl scale deployment cart --replicas=5`
- **Not to be confused with:** a Job (runs once).
- **Analogy:** 👥 A team with a headcount you can change.
- **In the online store:** cart, checkout, catalog each a Deployment.

### 2. Job
- **What it is:** Runs pods **until a task finishes**, then stops.
- **Looks like:** `kind: Job` for a DB migration
- **Not to be confused with:** long-running services.
- **Analogy:** 📋 A one-time task.
- **In the online store:** Nightly report.

### 🔗 How they fit together
```
 Deployment cart (3) | Deployment checkout (5) | Deployment catalog (2) ✅ each scales alone
```

---

## 🌍 Real-World Scenario

A store's services (cart, checkout, catalog) each get a **Deployment**, so checkout can scale to 10 pods on Black Friday without touching catalog.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create and deploy a Custom Resource Definition per microservice.

**Wrong words:**
- ❌ "**Custom Resource Definition**": it extends Kubernetes with new object types. It's not for running an app.

📌 **When to use it:** Use CRDs when building operators or extensions.
🏢 **Office example:** Inventing a new form type when you just need to hire staff.

### ❌ B
> **B.** Create and deploy a Docker Compose File.

**Wrong words:**
- ❌ "**Docker Compose File**": that's a Docker tool. GKE doesn't deploy Compose files.

📌 **When to use it:** Use Compose for running containers locally.
🏢 **Office example:** Using the home planner at the office.

### ❌ C
> **C.** Create and deploy a Job per microservice.

**Wrong words:**
- ❌ "**Job per microservice**": Jobs run to completion. Web services must run continuously.

📌 **When to use it:** Use a Job for a one-time task.
🏢 **Office example:** Hiring a temp for a permanent job.

### ✅ D
> **D.** Create and deploy a Deployment per microservice.

**Why it's correct:**
- ✔️ "**Deployment per microservice**" matches "**each microservice can be scaled individually**": each has its own replica count.

📌 **When to use it:** Use it when each team of workers needs its own adjustable headcount.
🏢 **Office example:** Each department sets its own staff size.

---

## 🛒 E-Commerce Full-Stack Example

`kubectl scale deployment checkout --replicas=10` (catalog stays at 3).

---

## 🧠 Key Takeaways / Memory Tips

- **Long-running service on GKE → Deployment.** One per microservice to scale individually.
- Job = run once.
  🧠 *"**Deploy each, scale each.**"*
- Related: **Q182**, **Q123**.

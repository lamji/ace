# Q236: Move Dockerized Python Microservices to Serverless (Existing CI/CD, Deploy Images to Cloud Run, Update Config)

**Topic:** Serverless (Cloud Run vs Cloud Functions)

## ❓ Question
> Your team is running an on-premises ecommerce application. The application contains a complex set of microservices written in Python, and each microservice is running on Docker containers. Configurations are injected by using environment variables. You need to deploy your current application to a serverless Google Cloud cloud solution. What should you do?
>
> **A.** Use your existing CI/CD pipeline. Use the generated Docker images and deploy them to Cloud Run. Update the configurations and the required endpoints.
>
> **B.** Use your existing continuous integration and delivery (CI/CD) pipeline. Use the generated Docker images and deploy them to Cloud Function. Use the same configuration as on-premises.
>
> **C.** Use the existing codebase and deploy each service as a separate Cloud Function. Update the configurations and the required endpoints.
>
> **D.** Use your existing codebase and deploy each service as a separate Cloud Run. Use the same configurations as on-premises.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An on-premises shop app is made of many Python microservices, each in a Docker container, with settings passed in through environment variables.
- **What you must achieve:** Move it to a serverless Google Cloud service (one where you don't manage servers).
- **The limits:** Keep the containers and the environment-variable settings working.
- **What they're really asking:** Which serverless service can run these containers as they are?

**Clues in the question:**
- "**running on Docker containers**" + "**serverless**" → **Cloud Run** runs your images as they are.
- "**Configurations are injected by using environment variables**" → set them on Cloud Run, but **endpoints change** in the cloud, so **update** them.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run env vars 🔑
- **What it is:** Configuration passed to containers at deploy time.
- **Looks like:** `gcloud run deploy cart --image=… --set-env-vars=DB_HOST=10.1.0.5,PAYMENTS_URL=https://payments-xyz.a.run.app`
- **Not to be confused with:** code changes.
- **Analogy:** 📝 Settings card handed to each worker.
- **In the online store:** Service URLs.

### 2. Cloud Functions
- **What it is:** Runs **source code functions**, not your existing multi-service container images.
- **Looks like:** —
- **Not to be confused with:** Cloud Run.
- **Analogy:** 🧩 Single-task helpers.
- **In the online store:** —

### 🔗 How they fit together
```
 CI/CD → Docker images → Artifact Registry → Cloud Run services ✅ (env vars updated to cloud endpoints)
```

---

## 🌍 Real-World Scenario

An e-commerce team keeps its CI/CD, pushes the same images, deploys each to **Cloud Run**, and updates env vars so services point to each other's new Cloud Run URLs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use your existing CI/CD pipeline. Use the generated Docker images and deploy them to Cloud Run. Update the configurations and the required endpoints.

**Why it's correct:**
- ✔️ "**Use your existing CI/CD pipeline. Use the generated Docker images**" matches "**each microservice is running on Docker containers**": nothing to rewrite.
- ✔️ "**deploy them to Cloud Run**" matches "**serverless**".
- ✔️ "**Update the configurations and the required endpoints**" matches "**Configurations are injected by using environment variables**": addresses change in the cloud.

📌 **When to use it:** Use it when your app is already packaged in containers and you want to stop managing servers.
🏢 **Office example:** Moving each packed department box into a serviced office, and updating the internal phone list with new extensions.

### ❌ B
> **B.** Use your existing continuous integration and delivery (CI/CD) pipeline. Use the generated Docker images and deploy them to Cloud Function. Use the same configuration as on-premises.

**Wrong words:**
- ❌ "**deploy them to Cloud Function**": Cloud Functions take source code, not your existing container images.
- ❌ "**Use the same configuration as on-premises**": on-prem endpoints won't work.

📌 **When to use it:** Use Cloud Functions for small event-driven code.
🏢 **Office example:** Asking a single-task helper to run a whole department.

### ❌ C
> **C.** Use the existing codebase and deploy each service as a separate Cloud Function. Update the configurations and the required endpoints.

**Wrong words:**
- ❌ "**deploy each service as a separate Cloud Function**": rewrites/re-packages a complex app; ignores the containers.

📌 **When to use it:** Use it for small, simple functions.
🏢 **Office example:** Breaking each department into one-off temp jobs.

### ❌ D
> **D.** Use your existing codebase and deploy each service as a separate Cloud Run. Use the same configurations as on-premises.

**Wrong words:**
- ✔️ "Cloud Run" is right.
- ❌ "**Use the same configurations as on-premises**": old endpoints/addresses won't work.

📌 **When to use it:** Use it only after updating configuration.
🏢 **Office example:** Moving offices but keeping the old phone list.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy cart --image=us-docker.pkg.dev/shopnow/apps/cart:v12 --set-env-vars=INVENTORY_URL=https://inventory-abc.a.run.app`

---

## 🧠 Key Takeaways / Memory Tips

- **Containers → serverless: Cloud Run. Update env-var endpoints for the cloud.**
  🧠 *"**Already in Docker? Cloud Run.**"*
- Related: **Q233**, **Q163**.

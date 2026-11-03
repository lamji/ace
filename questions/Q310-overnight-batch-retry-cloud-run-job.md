# Q310: Daily Overnight Batch, Lowest Cost, Automatic Retries (Cloud Run Job + Cloud Scheduler)

**Topic:** Serverless (Cloud Run jobs, Cloud Scheduler)

## ❓ Question
> Your company’s accounting department needs to run an overnight batch workload every day. You must implement a solution that minimizes the cost to run this workload and automatically retries the batch if an execution fails. What should you do?
>
> **A.** Develop an application that runs the batch workload, and deploy the application as a Google Kubernetes Engine (GKE) CronJob.
>
> **B.** Develop a web application that listens for incoming requests, and deploy the application as a Cloud Run service. Use Cloud Scheduler to call the HTTP endpoint.
>
> **C.** Develop an application that runs the batch workload, and deploy the application as a Cloud Run job. Use Cloud Scheduler to trigger the job.
>
> **D.** Develop a web application that listens for incoming requests, and deploy the application as a Google Kubernetes Engine (GKE) Deployment. Use Cloud Scheduler to call the HTTP endpoint.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Daily batch, **cheapest**, **automatic retry** on failure.

**Clues in the question:**
- Batch (not a web server) → **Cloud Run job** (has `--max-retries`).
- Daily → **Cloud Scheduler** triggers it. Pay only while it runs.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run job 🔑
- **What it is:** Runs a container to completion (no HTTP listener), with task retries; billed only while running.
- **Looks like:** `gcloud run jobs create ledger --image=... --max-retries=3`
- **Not to be confused with:** Cloud Run service (handles requests).
- **Analogy:** 🧾 A one-off task list worker.
- **In the online store:** Nightly report export.

### 🔗 How they fit together
```
 Cloud Scheduler (02:00) → Cloud Run job (retries=3) ✅
```

---

## 🌍 Real-World Scenario

Accounting's nightly reconciliation runs as a **Cloud Run job** triggered by **Cloud Scheduler**, with retries.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Develop an application that runs the batch workload, and deploy the application as a Google Kubernetes Engine (GKE) CronJob.

**Wrong words:**
- ✔️ CronJobs can retry.
- ❌ "**GKE CronJob**": you pay for the cluster all day for a nightly task.

📌 **When to use it:** Use it if you already run a GKE cluster.
🏢 **Office example:** Renting a whole office for a 1-hour night task.

### ❌ B
> **B.** Develop a web application that listens for incoming requests, and deploy the application as a Cloud Run service. Use Cloud Scheduler to call the HTTP endpoint.

**Wrong words:**
- ❌ "**web application that listens for incoming requests**" + "**Cloud Run service**": request timeouts and no built-in job retries.

📌 **When to use it:** Use services for HTTP traffic.
🏢 **Office example:** A receptionist doing all-night bookkeeping.

### ✅ C
> **C.** Develop an application that runs the batch workload, and deploy the application as a Cloud Run job. Use Cloud Scheduler to trigger the job.

**Why it's correct:**
- ✔️ "**Cloud Run job**" matches "**batch workload**" + "**automatically retries … if an execution fails**".
- ✔️ "**Cloud Scheduler to trigger**" matches "**overnight … every day**"; pay only while running matches "**minimizes the cost**".

📌 **When to use it:** Use it when a task should run on a schedule, finish, and try again if it fails.
🏢 **Office example:** A temp worker who comes in each night, finishes the ledger, and is called back if something went wrong.

### ❌ D
> **D.** Develop a web application that listens for incoming requests, and deploy the application as a Google Kubernetes Engine (GKE) Deployment. Use Cloud Scheduler to call the HTTP endpoint.

**Wrong words:**
- ❌ "**GKE Deployment**": always-on servers for a nightly task.

📌 **When to use it:** Use Deployments for long-running apps.
🏢 **Office example:** Full-time staff for a nightly chore.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud scheduler jobs create http nightly-recon --schedule="0 2 * * *" --uri=https://run.googleapis.com/v2/projects/shopnow/locations/us-central1/jobs/recon:run --oauth-service-account-email=sched@shopnow.iam.gserviceaccount.com`

---

## 🧠 Key Takeaways / Memory Tips

- **Scheduled batch + retries + cheap → Cloud Run job + Cloud Scheduler.**
  🧠 *"**Jobs finish, services listen.**"*
- Related: **Q211**, **Q270**.

# Q246: Serverless Migration: Flask Web App, Backend API, Long Background Job (App Engine, Cloud Run, Cloud Tasks → Cloud Run)

**Topic:** Serverless (App Engine, Cloud Run, Cloud Tasks)

## ❓ Question
> Your company wants to migrate their on-premises workloads to Google Cloud. The current on-premises workloads consist of: • A Flask web application • A backend API • A scheduled long-running background job for ETL and reporting. You need to keep operational costs low. You want to follow Google-recommended practices to migrate these workloads to serverless solutions on Google Cloud. What should you do?
>
> **A.** Migrate the web application to App Engine and the backend API to Cloud Run. Use Cloud Tasks to run your background job on Compute Engine.
>
> **B.** Migrate the web application to App Engine and the backend API to Cloud Run. Use Cloud Tasks to run your background job on Cloud Run.
>
> **C.** Run the web application on a Cloud Storage bucket and the backend API on Cloud Run. Use Cloud Tasks to run your background job on Cloud Run.
>
> **D.** Run the web application on a Cloud Storage bucket and the backend API on Cloud Run. Use Cloud Tasks to run your background job on Compute Engine.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are moving three on-premises workloads: a Flask web app, a backend API, and a scheduled long-running job for ETL (extract, transform, load) and reporting.
- **What you must achieve:** Move them to serverless services on Google Cloud.
- **The limits:** Keep operating costs low and follow recommended practice.
- **What they're really asking:** Which serverless service fits each of the three workloads?

**Clues in the question:**
- "**Flask web application**" (dynamic Python) → **App Engine** (a bucket can only host static files).
- "**backend API**" → **Cloud Run**.
- "**serverless**" → background job on **Cloud Run**, not Compute Engine.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Tasks 🔑
- **What it is:** A managed queue that sends tasks (HTTP requests) to a target like Cloud Run or App Engine, with retries and rate limits.
- **Looks like:** queue `etl` → target `https://etl-xyz.a.run.app/run`
- **Not to be confused with:** Cloud Scheduler (time trigger).
- **Analogy:** 📋 A to-do queue handed to workers.
- **In the online store:** Order report jobs.

### 2. Static site on Cloud Storage
- **What it is:** A bucket can serve **static** HTML/CSS/JS, not a Python Flask server.
- **Looks like:** —
- **Not to be confused with:** App Engine.
- **Analogy:** 📄 A printed brochure vs a live receptionist.
- **In the online store:** —

### 🔗 How they fit together
```
 Flask → App Engine ✅   API → Cloud Run ✅   job → Cloud Tasks → Cloud Run ✅
```

---

## 🌍 Real-World Scenario

A company moves its Flask site to **App Engine**, its API to **Cloud Run**, and dispatches the nightly ETL via **Cloud Tasks** to a **Cloud Run** service. Nothing runs when idle.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate the web application to App Engine and the backend API to Cloud Run. Use Cloud Tasks to run your background job on Compute Engine.

**Wrong words:**
- ✔️ App Engine + Cloud Run are right.
- ❌ "**background job on Compute Engine**": not serverless; you manage a VM.

📌 **When to use it:** Use Compute Engine for jobs that need full VM control.
🏢 **Office example:** Two serviced offices and one you must run yourself.

### ✅ B
> **B.** Migrate the web application to App Engine and the backend API to Cloud Run. Use Cloud Tasks to run your background job on Cloud Run.

**Why it's correct:**
- ✔️ "**web application to App Engine**" matches "**A Flask web application**" (dynamic Python).
- ✔️ "**backend API to Cloud Run**" matches "**A backend API**".
- ✔️ "**Cloud Tasks to run your background job on Cloud Run**" matches "**scheduled long-running background job**" + "**serverless**" + "**operational costs low**".

📌 **When to use it:** Use it when every part of a system should run without servers and cost little when idle.
🏢 **Office example:** Moving each department into a serviced office where you pay only while staff are working.

### ❌ C
> **C.** Run the web application on a Cloud Storage bucket and the backend API on Cloud Run. Use Cloud Tasks to run your background job on Cloud Run.

**Wrong words:**
- ❌ "**web application on a Cloud Storage bucket**": a bucket can't run Flask.

📌 **When to use it:** Use a bucket for static websites.
🏢 **Office example:** A brochure can't answer customer questions.

### ❌ D
> **D.** Run the web application on a Cloud Storage bucket and the backend API on Cloud Run. Use Cloud Tasks to run your background job on Compute Engine.

**Wrong words:**
- ❌ "**Cloud Storage bucket**" (can't run Flask) and ❌ "**Compute Engine**" (not serverless).

📌 **When to use it:** **Never use this** for this mix.
🏢 **Office example:** Two wrong offices.

---

## 🛒 E-Commerce Full-Stack Example

Storefront (Flask) → App Engine standard; `orders-api` → Cloud Run; nightly ETL: Cloud Scheduler → Cloud Tasks queue → Cloud Run `etl-runner`.

---

## 🧠 Key Takeaways / Memory Tips

- **Dynamic web app → App Engine/Cloud Run. Bucket = static only. Serverless jobs → Cloud Run.**
  🧠 *"**No VMs in a serverless answer.**"*
- Related: **Q236**, **Q240**.

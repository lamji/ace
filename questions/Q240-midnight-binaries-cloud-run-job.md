# Q240: 45-Minute Nightly In-Memory Job on 1–16 GB Files, Minimal Effort and Cost (Container + Cloud Scheduler → Cloud Run Job)

**Topic:** Serverless (Cloud Run jobs vs VMs vs Cloud Functions)

## ❓ Question
> You have an on-premises data analytics set of binaries that processes data files in memory for about 45 minutes every midnight. The sizes of those data files range from 1 gigabyte to 16 gigabytes. You want to migrate this application to Google Cloud with minimal effort and cost. What should you do?
>
> **A.** Create a container for the set of binaries. Use Cloud Scheduler to start a Cloud Run job for the container.
>
> **B.** Create a container for the set of binaries. Deploy the container to Google Kubernetes Engine (GKE) and use the Kubernetes scheduler to start the application.
>
> **C.** Upload the code to Cloud Functions. Use Cloud Scheduler to start the application.
>
> **D.** Lift and shift to a VM on Compute Engine. Use an instance schedule to start and stop the instance.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between A and D. Most Voted is **A**: Cloud Run **jobs** run to completion (tasks can run up to 24 h) with up to 32 GiB memory, and you pay only while it runs. Some argue D (lift and shift) is less effort for binaries. If your site differs, tell me.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** On-premises programs analyze data files in memory for about 45 minutes every midnight. Files are 1 GB to 16 GB.
- **What you must achieve:** Move this job to Google Cloud.
- **The limits:** Minimal effort and cost.
- **What they're really asking:** How should you run a short nightly job that needs up to 16 GB in memory?

**Clues in the question:**
- "**about 45 minutes every midnight**" → a scheduled **job** that runs and exits → **Cloud Run job** + **Cloud Scheduler**; pay only for 45 minutes.
- "**up to 16 gigabytes**" in memory → Cloud Run supports up to 32 GiB.
- Cloud Functions are limited in time and memory for this.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run job 🔑
- **What it is:** Runs a container **to completion** (not a web service), then stops. Can be triggered by Cloud Scheduler.
- **Looks like:** `gcloud run jobs create nightly-analytics --image=… --memory=32Gi --cpu=8 --task-timeout=2h`
- **Not to be confused with:** Cloud Run service.
- **Analogy:** 🧹 A cleaning crew that comes at midnight, finishes, and leaves.
- **In the online store:** Nightly sales rollup.

### 2. Instance schedule
- **What it is:** Starts/stops a VM at set times.
- **Looks like:** `gcloud compute resource-policies create instance-schedule …`
- **Not to be confused with:** —
- **Analogy:** ⏰ Timer switch.
- **In the online store:** —

### 🔗 How they fit together
```
 Cloud Scheduler 00:00 ─► Cloud Run job (container, 32 GiB) runs ~45 min ─► exits ✅ (pay 45 min)
```

---

## 🌍 Real-World Scenario

A retailer containerizes its nightly analytics binaries and runs them as a **Cloud Run job** triggered by **Cloud Scheduler** at midnight, paying only for the 45 minutes.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a container for the set of binaries. Use Cloud Scheduler to start a Cloud Run job for the container.

**Why it's correct:**
- ✔️ "**Create a container for the set of binaries**" matches "**set of binaries**" with "**minimal effort**": wrap them as they are.
- ✔️ "**Cloud Scheduler to start a Cloud Run job**" matches "**about 45 minutes every midnight**" + "**minimal … cost**": runs to completion and you pay only while it runs.

📌 **When to use it:** Use it when a task runs once a night for a while and nothing needs to stay running in between.
🏢 **Office example:** A cleaning crew that arrives at midnight, does the job, and leaves; you pay only for their hours.

### ❌ B
> **B.** Create a container for the set of binaries. Deploy the container to Google Kubernetes Engine (GKE) and use the Kubernetes scheduler to start the application.

**Wrong words:**
- ❌ "**Deploy the container to GKE**": a cluster to run and pay for all day, for a 45-minute job.

📌 **When to use it:** Use GKE when you already run many services on Kubernetes.
🏢 **Office example:** Renting a full-time office for a 45-minute nightly task.

### ❌ C
> **C.** Upload the code to Cloud Functions. Use Cloud Scheduler to start the application.

**Wrong words:**
- ❌ "**Upload the code to Cloud Functions**": these are binaries, not function code, and memory/time limits make 16 GB in-memory processing a poor fit.

📌 **When to use it:** Use Cloud Functions for short event-driven code.
🏢 **Office example:** Asking a quick-errand runner to do a long night shift.

### ❌ D
> **D.** Lift and shift to a VM on Compute Engine. Use an instance schedule to start and stop the instance.

**Wrong words:**
- ✔️ Lift and shift is simple.
- ❌ But you manage a VM, its OS and disks; still more effort and cost than a job that only exists while running.

📌 **When to use it:** Use a scheduled VM when the software can't be containerized.
🏢 **Office example:** Keeping a dedicated office with a timer on the lights.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud scheduler jobs create http nightly-rollup --schedule="0 0 * * *" --uri=https://run.googleapis.com/v2/projects/shopnow/locations/us-central1/jobs/sales-rollup:run --oauth-service-account-email=scheduler@shopnow.iam.gserviceaccount.com`

---

## 🧠 Key Takeaways / Memory Tips

- **Scheduled container that runs and exits → Cloud Run job + Cloud Scheduler.**
  🧠 *"**Runs and leaves? Cloud Run job.**"*
- Related: **Q136**, **Q218**, **Q233**.

# Q153: Run Code Whenever a File Is Uploaded to a Bucket (Cloud Functions With a Storage Trigger)

**Topic:** Serverless (Cloud Functions / Cloud Run functions, event triggers)

## ❓ Question
> You have created a code snippet that should be triggered whenever a new file is uploaded to a Cloud Storage bucket. You want to deploy this code snippet. What should you do?
>
> **A.** Use App Engine and configure Cloud Scheduler to trigger the application using Pub/Sub.
>
> **B.** Use Cloud Functions and configure the bucket as a trigger resource.
>
> **C.** Use Google Kubernetes Engine and configure a CronJob to trigger the application using Pub/Sub.
>
> **D.** Use Dataflow as a batch job, and configure the bucket as a data source.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You wrote a small piece of code that should run every time a new file is uploaded to a Cloud Storage bucket.
- **What you must achieve:** Deploy that code so uploads trigger it automatically.
- **The limits:** None stated.
- **What they're really asking:** Where and how do you deploy code so a file upload starts it?

**Clues in the question:**
- "**code snippet**": small code → **Cloud Functions**.
- "**triggered whenever a new file is uploaded**": an **event trigger** on the bucket (object finalize), not a schedule.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Functions storage trigger 🔑
- **What it is:** A function that runs **automatically when an object is created** (finalized) in a bucket.
- **Looks like:** `gcloud functions deploy make-thumb --runtime=python312 --trigger-bucket=shop-uploads`
- **Not to be confused with:** a scheduled job.
- **Analogy:** 🔔 A **doorbell**: rings the moment a parcel arrives.
- **In the online store:** Make a thumbnail when a product photo is uploaded.

### 2. Cloud Scheduler / CronJob
- **What it is:** Run things on a **timetable**, not when something happens.
- **Looks like:** `0 * * * *`
- **Not to be confused with:** event triggers.
- **Analogy:** ⏰ An alarm clock.
- **In the online store:** Nightly reports.

### 🔗 How they fit together
```
 upload photo.jpg → gs://shop-uploads → (object finalized event) → Cloud Function runs ✅
```

---

## 🌍 Real-World Scenario

A store lets sellers upload product photos. A **Cloud Function** with the bucket as its **trigger** resizes each photo the moment it lands.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use App Engine and configure Cloud Scheduler to trigger the application using Pub/Sub.

**Wrong words:**
- ❌ "**Cloud Scheduler to trigger**": runs on a schedule, not when a file is uploaded. Using App Engine for a snippet is also overkill.

📌 **When to use it:** Use Scheduler for timed jobs.
🏢 **Office example:** An alarm clock that checks the mailbox every hour instead of a doorbell.

### ✅ B
> **B.** Use Cloud Functions and configure the bucket as a trigger resource.

**Why it's correct:**
- ✔️ "**Use Cloud Functions**" matches "**code snippet**": small, serverless code.
- ✔️ "**configure the bucket as a trigger resource**" matches "**triggered whenever a new file is uploaded**": it runs on each upload event.

📌 **When to use it:** Use it when a small task should happen automatically every time something arrives.
🏢 **Office example:** A doorbell that calls the clerk the moment a parcel is delivered.

### ❌ C
> **C.** Use Google Kubernetes Engine and configure a CronJob to trigger the application using Pub/Sub.

**Wrong words:**
- ❌ "**GKE … CronJob**": a cluster plus a timer, which is heavy and not event-driven.

📌 **When to use it:** Use CronJobs for scheduled tasks in an existing cluster.
🏢 **Office example:** Building a mailroom with a clock to watch for one parcel.

### ❌ D
> **D.** Use Dataflow as a batch job, and configure the bucket as a data source.

**Wrong words:**
- ❌ "**Dataflow as a batch job**": a big data pipeline that runs once over data, not on each upload.

📌 **When to use it:** Use Dataflow for large ETL pipelines.
🏢 **Office example:** Hiring a factory to open each letter.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud functions deploy make-thumbnail --gen2 --runtime=python312 --region=us-central1 \
  --trigger-bucket=shopnow-uploads --entry-point=handle
```
A seller uploads `sku-123.jpg`, and a 300px thumbnail appears in `shopnow-thumbs` in seconds.

---

## 🧠 Key Takeaways / Memory Tips

- **"When a file is uploaded, run code" → Cloud Functions with a bucket trigger.**
- Scheduler and CronJob are for timetables.
  🧠 *"**File arrives, function fires.**"*
- Related: **Q124** (function from webhook), **Q064** (Pub/Sub push).

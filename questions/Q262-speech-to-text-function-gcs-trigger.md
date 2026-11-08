# Q262: Send Each New Audio File to Speech-to-Text Automatically, Serverless (Cloud Function With a Cloud Storage Trigger)

**Topic:** Serverless (Cloud Functions events)

## ❓ Question
> You need to extract text from audio files by using the Speech-to-Text API. The audio files are pushed to a Cloud Storage bucket. You need to implement a fully managed, serverless compute solution that requires authentication and aligns with Google-recommended practices. You want to automate the call to the API by submitting each file to the API as the audio file arrives in the bucket. What should you do?
>
> **A.** Create an App Engine standard environment triggered by Cloud Storage bucket events to submit the file URI to the Google Speech-to-TextAPI.
>
> **B.** Run a Kubernetes job to scan the bucket regularly for incoming files, and call the Speech-to-Text API for each unprocessed file.
>
> **C.** Run a Python script by using a Linux cron job in Compute Engine to scan the bucket regularly for incoming files, and call the Speech-to-Text API for each unprocessed file.
>
> **D.** Create a Cloud Function triggered by Cloud Storage bucket events to submit the file URI to the Google Speech-to-Text API.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Audio files arrive in a Cloud Storage bucket, and you need text from them with the Speech-to-Text API.
- **What you must achieve:** Send each file to the API automatically as soon as it arrives.
- **The limits:** Fully managed, serverless, authenticated, and following Google's recommendations.
- **What they're really asking:** What serverless setup reacts to each new file and calls the API?

**Clues in the question:**
- "**as the audio file arrives in the bucket**" + "**serverless**" → **Cloud Function** with a **Cloud Storage trigger** (Q153).
- App Engine can't be triggered directly by bucket events.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Storage trigger 🔑 (review from Q153)
- **What it is:** Runs a function when an object is finalized in a bucket.
- **Looks like:** `gcloud functions deploy transcribe --trigger-bucket=calls-audio --runtime=python312`
- **Not to be confused with:** polling.
- **Analogy:** 🔔 A doorbell on the mailbox.
- **In the online store:** Transcribe support calls.

### 🔗 How they fit together
```
 audio.wav → bucket ─event─► Cloud Function ─► Speech-to-Text (gs://… URI) ✅
```

---

## 🌍 Real-World Scenario

A call center drops recordings into a bucket. A **Cloud Function** fires on each upload and submits the file's URI to Speech-to-Text.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an App Engine standard environment triggered by Cloud Storage bucket events to submit the file URI to the Google Speech-to-TextAPI.

**Wrong words:**
- ❌ "**App Engine standard … triggered by Cloud Storage bucket events**": App Engine isn't triggered by bucket events.

📌 **When to use it:** Use App Engine for web apps.
🏢 **Office example:** Expecting the front desk to ring when mail drops in the back.

### ❌ B
> **B.** Run a Kubernetes job to scan the bucket regularly for incoming files, and call the Speech-to-Text API for each unprocessed file.

**Wrong words:**
- ❌ "**Kubernetes job to scan the bucket regularly**": polling, plus a cluster; not serverless.

📌 **When to use it:** Use Jobs for batch work on GKE.
🏢 **Office example:** Checking the mailbox every hour.

### ❌ C
> **C.** Run a Python script by using a Linux cron job in Compute Engine to scan the bucket regularly for incoming files, and call the Speech-to-Text API for each unprocessed file.

**Wrong words:**
- ❌ "**cron job in Compute Engine**": a VM to manage; polling.

📌 **When to use it:** Use cron on VMs for legacy scripts.
🏢 **Office example:** A clerk checking the mailbox on a timer.

### ✅ D
> **D.** Create a Cloud Function triggered by Cloud Storage bucket events to submit the file URI to the Google Speech-to-Text API.

**Why it's correct:**
- ✔️ "**Cloud Function triggered by Cloud Storage bucket events**" matches "**as the audio file arrives in the bucket**" + "**fully managed, serverless**".
- ✔️ "**submit the file URI to the … Speech-to-Text API**" matches "**automate the call to the API**".

📌 **When to use it:** Use it when every new file dropped in a folder should be handled right away, automatically.
🏢 **Office example:** A doorbell on the mailbox that calls the transcriber each time a tape arrives.

---

## 🛒 E-Commerce Full-Stack Example

Function `transcribe-reviews` on `--trigger-bucket=shopnow-voice-reviews` → Speech-to-Text → text stored in Firestore.

---

## 🧠 Key Takeaways / Memory Tips

- **React to each new file → Cloud Function with a Storage trigger.**
  🧠 *"**File lands, function runs.**"*
- Related: **Q153**.

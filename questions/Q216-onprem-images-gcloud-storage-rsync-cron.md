# Q216: Automatically Upload New Hospital Images From On-Prem (gcloud storage Sync Script on a Cron Schedule)

**Topic:** Data transfer (gcloud storage rsync, cron)

## ❓ Question
> You are working for a hospital that stores its medical images in an on-premises data room. The hospital wants to use Cloud Storage for archival storage of these images. The hospital wants an automated process to upload any new medical images to Cloud Storage. You need to design and implement a solution. What should you do?
>
> **A.** Create a Pub/Sub topic, and enable a Cloud Storage trigger for the Pub/Sub topic. Create an application that sends all medical images to the Pub/Sub topic.
>
> **B.** Create a script that uses the gcloud storage command to synchronize the on-premises storage with Cloud Storage, Schedule the script as a cron job.
>
> **C.** Create a Pub/Sub topic, and create a Cloud Function connected to the topic that writes data to Cloud Storage. Create an application that sends all medical images to the Pub/Sub topic.
>
> **D.** In the Google Cloud console, go to Cloud Storage. Upload the relevant images to the appropriate bucket.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A hospital keeps medical images in its own on-site data room.
- **What you must achieve:** Automatically upload every new image to Cloud Storage for archiving.
- **The limits:** It must be automated.
- **What they're really asking:** What should you set up so new images upload by themselves?

**Clues in the question:**
- "**automated process to upload any new medical images**" → `gcloud storage rsync` (copies only new/changed files) on a **cron** schedule.

**Exam topic:** Data transfer.

---

## 📚 Key Terms Explained

### 1. gcloud storage rsync 🔑
- **What it is:** The newer replacement for `gsutil rsync`: makes a bucket match a local folder.
- **Looks like:** `gcloud storage rsync /data/images gs://hospital-archive --recursive`
- **Not to be confused with:** gsutil (older).
- **Analogy:** 🔄 A clerk copying only new pages into the archive binder.
- **In the online store:** Product photo sync.

### 2. cron (review from Q168)
- **What it is:** Linux scheduler.
- **Looks like:** `0 2 * * * /opt/sync.sh`
- **Not to be confused with:** —
- **Analogy:** ⏰ Alarm clock.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem /images ── cron 02:00 ── gcloud storage rsync ──► gs://hospital-archive ✅
```

---

## 🌍 Real-World Scenario

The hospital's image server runs a nightly **cron** job with `gcloud storage rsync`, uploading only new images to an Archive bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Pub/Sub topic, and enable a Cloud Storage trigger for the Pub/Sub topic. Create an application that sends all medical images to the Pub/Sub topic.

**Wrong words:**
- ❌ "**sends all medical images to the Pub/Sub topic**": Pub/Sub is for small messages (max 10 MB), not image files.
- ❌ "**Cloud Storage trigger for the Pub/Sub topic**": backwards.

📌 **When to use it:** Use Pub/Sub for event messages.
🏢 **Office example:** Faxing X-ray films through the intercom.

### ✅ B
> **B.** Create a script that uses the gcloud storage command to synchronize the on-premises storage with Cloud Storage, Schedule the script as a cron job.

**Why it's correct:**
- ✔️ "**gcloud storage command to synchronize the on-premises storage with Cloud Storage**" matches "**upload any new medical images**".
- ✔️ "**Schedule the script as a cron job**" matches "**automated process**".

📌 **When to use it:** Use it when a local folder must be copied to the cloud regularly without anyone doing it by hand.
🏢 **Office example:** A clerk who copies only the new files to the off-site archive every night.

### ❌ C
> **C.** Create a Pub/Sub topic, and create a Cloud Function connected to the topic that writes data to Cloud Storage. Create an application that sends all medical images to the Pub/Sub topic.

**Wrong words:**
- ❌ "**sends all medical images to the Pub/Sub topic**": same size problem; extra function adds complexity.

📌 **When to use it:** Use Pub/Sub + Functions for small event processing.
🏢 **Office example:** A mail chain for something a courier should carry.

### ❌ D
> **D.** In the Google Cloud console, go to Cloud Storage. Upload the relevant images to the appropriate bucket.

**Wrong words:**
- ❌ "**In the Google Cloud console … Upload**": manual.

📌 **When to use it:** Use it for one-off uploads.
🏢 **Office example:** Carrying boxes by hand every day.

---

## 🛒 E-Commerce Full-Stack Example

`0 2 * * * gcloud storage rsync /studio/exports gs://shopnow-product-photos --recursive`

---

## 🧠 Key Takeaways / Memory Tips

- **Automated on-prem → bucket sync: `gcloud storage rsync` + cron.**
  🧠 *"**New files nightly: rsync on cron.**"*
- Related: **Q168** (gsutil version).

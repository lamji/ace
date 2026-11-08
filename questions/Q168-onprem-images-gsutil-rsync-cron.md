# Q168: Automatically Upload New Hospital Images From On-Prem (gsutil rsync Script on a Cron Schedule)

**Topic:** Data transfer (gsutil rsync, cron, Pub/Sub, Dataflow)

## ❓ Question
> You are working for a hospital that stores its medical images in an on-premises data room. The hospital wants to use Cloud Storage for archival storage of these images. The hospital wants an automated process to upload any new medical images to Cloud Storage. You need to design and implement a solution. What should you do?
>
> **A.** Create a Pub/Sub topic, and enable a Cloud Storage trigger for the Pub/Sub topic. Create an application that sends all medical images to the Pub/Sub topic.
>
> **B.** Deploy a Dataflow job from the batch template, "Datastore to Cloud Storage." Schedule the batch job on the desired interval.
>
> **C.** Create a script that uses the gsutil command line interface to synchronize the on-premises storage with Cloud Storage. Schedule the script as a cron job.
>
> **D.** In the Cloud Console, go to Cloud Storage. Upload the relevant images to the appropriate bucket.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A hospital keeps medical images in its own on-site data room.
- **What you must achieve:** Automatically upload every new image to Cloud Storage for archiving.
- **The limits:** It must be automated.
- **What they're really asking:** What should you set up so new images upload by themselves?

**Clues in the question:**
- "**automated process to upload any new medical images**": `gsutil rsync` copies **only new or changed files**, and **cron** runs it on a schedule.
- Files are on-prem disks, not in Datastore or Pub/Sub.

**Exam topic:** Data transfer.

---

## 📚 Key Terms Explained

### 1. gsutil rsync 🔑
- **What it is:** Makes a bucket **match a local folder**, copying only new and changed files.
- **Looks like:** `gsutil -m rsync -r /data/images gs://hospital-archive/images`
- **Not to be confused with:** cp (copies everything).
- **Analogy:** 🔄 A clerk who copies only the **new** pages into the archive binder.
- **In the online store:** Sync product photos nightly.

### 2. cron
- **What it is:** A Linux scheduler that runs commands at set times.
- **Looks like:** `0 2 * * * /opt/sync.sh`
- **Not to be confused with:** Cloud Scheduler.
- **Analogy:** ⏰ An alarm clock on the server.
- **In the online store:** Run sync at 2 AM.

### 🔗 How they fit together
```
 on-prem /images ── cron 02:00 ── gsutil rsync ──► gs://hospital-archive ✅ (only new files)
```

---

## 🌍 Real-World Scenario

A hospital's PACS server saves images to a local folder. A small script runs `gsutil rsync` to an Archive-class bucket every night through **cron**, so only new images are uploaded.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Pub/Sub topic, and enable a Cloud Storage trigger for the Pub/Sub topic. Create an application that sends all medical images to the Pub/Sub topic.

**Wrong words:**
- ❌ "**sends all medical images to the Pub/Sub topic**": Pub/Sub carries **messages** (max 10 MB), not large image files.
- ❌ "**Cloud Storage trigger for the Pub/Sub topic**": that's backwards (buckets send events to Pub/Sub).

📌 **When to use it:** Use Pub/Sub to send event messages between apps.
🏢 **Office example:** Faxing X-ray films page by page through the intercom.

### ❌ B
> **B.** Deploy a Dataflow job from the batch template, "Datastore to Cloud Storage." Schedule the batch job on the desired interval.

**Wrong words:**
- ❌ "**Datastore to Cloud Storage**": the images are in an on-prem data room, not in Datastore.

📌 **When to use it:** Use that template to export Datastore data.
🏢 **Office example:** A moving truck sent to the wrong building.

### ✅ C
> **C.** Create a script that uses the gsutil command line interface to synchronize the on-premises storage with Cloud Storage. Schedule the script as a cron job.

**Why it's correct:**
- ✔️ "**gsutil … synchronize the on-premises storage with Cloud Storage**" matches "**upload any new medical images**": rsync copies only new files.
- ✔️ "**Schedule the script as a cron job**" matches "**automated process**".

📌 **When to use it:** Use it when a local folder should be copied to the cloud regularly without anyone doing it by hand.
🏢 **Office example:** A clerk who, every night, copies only the new files into the off-site archive.

### ❌ D
> **D.** In the Cloud Console, go to Cloud Storage. Upload the relevant images to the appropriate bucket.

**Wrong words:**
- ❌ "**In the Cloud Console … Upload**": manual, not automated.

📌 **When to use it:** Use it for one-off uploads.
🏢 **Office example:** Carrying boxes to the warehouse by hand every day.

---

## 🛒 E-Commerce Full-Stack Example

```bash
# /etc/cron.d/photo-sync on ShopNow's studio server
0 2 * * * photo gsutil -m rsync -r /studio/exports gs://shopnow-product-photos
```

---

## 🧠 Key Takeaways / Memory Tips

- **Automatically copy new on-prem files → gsutil rsync + cron** (or Storage Transfer Service today).
- Pub/Sub is for messages, not big files.
  🧠 *"**New files nightly: rsync on cron.**"*
- Related: **Q119** (gsutil to Cloud Storage), **Q154** (archive classes).

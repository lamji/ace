# Q289: Get Notified of Every File Change in Cloud Storage With Little Overhead (Versioning + Pub/Sub Notifications for Cloud Storage)

**Topic:** Cloud Storage (Pub/Sub notifications)

## ❓ Question
> You are the Organization Administrator for your company's Google Cloud resources. Your company has strict compliance rules that require you to be notified about any modifications to files and documents hosted on Cloud Storage. In a recent incident, one of your team members was able to modify files and you did not receive any notifications, causing other production jobs to fail. You must ensure that you receive notifications for all changes to files and documents in Cloud Storage while minimizing management overhead. What should you do?
>
> **A.** View Cloud Audit logs for all Cloud Storage files in Logs Explorer. Filter by Admin Activity logs.
>
> **B.** Enable Cloud Storage object versioning on your bucket. Configure Pub/Sub notifications for your Cloud Storage buckets.
>
> **C.** Enable versioning on the Cloud Storage bucket. Set up a custom script that scans versions of Cloud Storage objects being modified and alert the admin by using the script.
>
> **D.** Configure Object change notifications on the Cloud Storage buckets. Send the events to Pub/Sub.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between B and D. B uses **Pub/Sub notifications for Cloud Storage**, the recommended feature. D mixes two things: legacy **Object change notifications** (deprecated; they send to webhooks, not Pub/Sub). If your site's Most Voted is D, tell me.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are the Organization Administrator. Compliance rules say you must be told about any change to files in Cloud Storage. A recent change went unnoticed and broke production jobs.
- **What you must achieve:** Get notified about every file change in Cloud Storage.
- **The limits:** Minimal management overhead.
- **What they're really asking:** What should you turn on so all file changes are recorded and alerted?

**Clues in the question:**
- "**notified about any modifications to files**" → **Pub/Sub notifications for Cloud Storage** (events on create/overwrite/delete).
- Versioning also keeps the old copy so a bad change can be undone.
- "**minimizing management overhead**" → no custom scripts.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Pub/Sub notifications for Cloud Storage 🔑
- **What it is:** A bucket setting that publishes a message to a topic for object events (`OBJECT_FINALIZE`, `OBJECT_DELETE`, …).
- **Looks like:** `gcloud storage buckets notifications create gs://contracts --topic=gcs-changes`
- **Not to be confused with:** Object change notifications (legacy webhooks).
- **Analogy:** 🔔 A doorbell for every file change.
- **In the online store:** Alert on price-file edits.

### 2. Object versioning (review from Q250)
- **What it is:** Keeps previous versions when objects are overwritten/deleted.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 📑 Keeps old drafts.
- **In the online store:** —

### 🔗 How they fit together
```
 bucket (versioning ON) ─ object event ─► Pub/Sub ─► email/alert/function ✅
```

---

## 🌍 Real-World Scenario

Compliance needs alerts on any change. The admin enables **versioning** and **Pub/Sub notifications** on the buckets; a subscriber emails the admin for each change.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** View Cloud Audit logs for all Cloud Storage files in Logs Explorer. Filter by Admin Activity logs.

**Wrong words:**
- ❌ "**View Cloud Audit logs … in Logs Explorer**": manual viewing, not notifications.
- ❌ "**Admin Activity logs**": object writes are Data Access logs, not Admin Activity.

📌 **When to use it:** Use audit logs to investigate after the fact.
🏢 **Office example:** Reading the logbook yourself instead of getting a call.

### ✅ B
> **B.** Enable Cloud Storage object versioning on your bucket. Configure Pub/Sub notifications for your Cloud Storage buckets.

**Why it's correct:**
- ✔️ "**Configure Pub/Sub notifications for your Cloud Storage buckets**" matches "**receive notifications for all changes to files and documents**".
- ✔️ "**Enable … object versioning**" keeps the previous copy, and both are built in, which matches "**minimizing management overhead**".

📌 **When to use it:** Use it when you must be told immediately whenever stored files change.
🏢 **Office example:** A doorbell that rings every time a file is changed, plus a copy of the old version kept in a drawer.

### ❌ C
> **C.** Enable versioning on the Cloud Storage bucket. Set up a custom script that scans versions of Cloud Storage objects being modified and alert the admin by using the script.

**Wrong words:**
- ✔️ Versioning is fine.
- ❌ "**custom script that scans versions**": code to maintain; polling delay.

📌 **When to use it:** Use scripts only when built-in events can't do it.
🏢 **Office example:** Hiring someone to check every drawer hourly.

### ❌ D
> **D.** Configure Object change notifications on the Cloud Storage buckets. Send the events to Pub/Sub.

**Wrong words:**
- ❌ "**Object change notifications**": a deprecated feature that sends to webhooks, not Pub/Sub; Pub/Sub notifications replace it.

📌 **When to use it:** **Avoid** — use Pub/Sub notifications instead.
🏢 **Office example:** An old doorbell model that's no longer supported.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud storage buckets update gs://shopnow-pricing --versioning` + `gcloud storage buckets notifications create gs://shopnow-pricing --topic=pricing-changes --event-types=OBJECT_FINALIZE,OBJECT_DELETE`

---

## 🧠 Key Takeaways / Memory Tips

- **Be notified of object changes → Pub/Sub notifications for Cloud Storage.** (Object change notifications are legacy.)
  🧠 *"**File changed? Pub/Sub rings.**"*
- Related: **Q153**, **Q262**, **Q250**.

# Q159: Suppliers Upload Their Own Data for 30 Minutes, Auto-Delete After 45 Days (Signed URLs + Lifecycle Rule)

**Topic:** Cloud Storage (signed URLs, lifecycle delete)

## ❓ Question
> You are building an application that processes data files uploaded from thousands of suppliers. Your primary goals for the application are data security and the expiration of aged data. You need to design the application to: * Restrict access so that suppliers can access only their own data. * Give suppliers write access to data only for 30 minutes. * Delete data that is over 45 days old. You have a very short development cycle, and you need to make sure that the application requires minimal maintenance. Which two strategies should you use? (Choose two.)
>
> **A.** Build a lifecycle policy to delete Cloud Storage objects after 45 days.
>
> **B.** Use signed URLs to allow suppliers limited time access to store their objects.
>
> **C.** Set up an SFTP server for your application, and create a separate user for each supplier.
>
> **D.** Build a Cloud function that triggers a timer of 45 days to delete objects that have expired.
>
> **E.** Develop a script that loops through all Cloud Storage buckets and deletes any buckets that are older than 45 days.

**My answer:** — (didn't know)
**Correct answer:** A, B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app receives data files uploaded by thousands of suppliers.
- **What you must achieve:** Each supplier can reach only their own data, gets write access for only 30 minutes, and data older than 45 days is deleted.
- **The limits:** Very short development time and minimal maintenance; pick two strategies.
- **What they're really asking:** Which two built-in features handle time-limited supplier uploads and automatic deletion of old data?

**Clues in the question:**
- "**write access … only for 30 minutes**" + "**only their own data**" → **signed URLs** (a link for one object that expires).
- "**Delete data that is over 45 days old**" + "**minimal maintenance**" → a **lifecycle rule** (age 45 → delete).

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Signed URL 🔑
- **What it is:** A **temporary link** that allows one action (e.g., upload) on **one object** until it **expires**. No Google account needed.
- **Looks like:** `gsutil signurl -m PUT -d 30m key.json gs://supplier-uploads/acme/2026-11-03.csv`
- **Not to be confused with:** making a bucket public.
- **Analogy:** 🎟️ A **one-time visitor pass** for one room, valid 30 minutes.
- **In the online store:** Each supplier gets an upload link.

### 2. Lifecycle delete rule 🔑
- **What it is:** A bucket rule that **automatically deletes** objects after a condition such as age.
- **Looks like:** `{"action":{"type":"Delete"},"condition":{"age":45}}`
- **Not to be confused with:** scripts or functions.
- **Analogy:** 🗑️ "Shred after 45 days" policy.
- **In the online store:** Supplier files auto-removed.

### 🔗 How they fit together
```
 app → signed PUT URL (30 min, one object) → supplier uploads ✅
 bucket lifecycle: age 45 → Delete ✅ (no code)
```

---

## 🌍 Real-World Scenario

A procurement platform asks each supplier to upload a daily file. The app issues a **signed URL** valid for 30 minutes for that supplier's path. A **lifecycle rule** deletes files older than 45 days. No servers, scripts or user accounts are needed.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Build a lifecycle policy to delete Cloud Storage objects after 45 days.

**Why it's correct:**
- ✔️ "**lifecycle policy to delete … after 45 days**" matches "**Delete data that is over 45 days old**".
- ✔️ It's built in with no code, which matches "**minimal maintenance**".

📌 **When to use it:** Use it when old files should disappear automatically.
🏢 **Office example:** An office rule: shred anything older than 45 days.

### ✅ B
> **B.** Use signed URLs to allow suppliers limited time access to store their objects.

**Why it's correct:**
- ✔️ "**signed URLs**" matches "**suppliers can access only their own data**": each link is for one specific object.
- ✔️ "**limited time access to store their objects**" matches "**write access … only for 30 minutes**".

📌 **When to use it:** Use it when outsiders need short, limited access to drop or fetch one file.
🏢 **Office example:** A 30-minute visitor pass for one specific room.

### ❌ C
> **C.** Set up an SFTP server for your application, and create a separate user for each supplier.

**Wrong words:**
- ❌ "**Set up an SFTP server … separate user for each supplier**": a server plus thousands of accounts to maintain, and no 30-minute limit.

📌 **When to use it:** Use SFTP when partners require that protocol.
🏢 **Office example:** Running a private post office with thousands of mailbox keys.

### ❌ D
> **D.** Build a Cloud function that triggers a timer of 45 days to delete objects that have expired.

**Wrong words:**
- ❌ "**Build a Cloud function that triggers a timer of 45 days**": custom code for something lifecycle rules already do (and functions can't wait 45 days).

📌 **When to use it:** **Never use this** when a lifecycle rule works.
🏢 **Office example:** Hiring someone to set a 45-day alarm for every file.

### ❌ E
> **E.** Develop a script that loops through all Cloud Storage buckets and deletes any buckets that are older than 45 days.

**Wrong words:**
- ❌ "**deletes any buckets that are older than 45 days**": it deletes whole **buckets**, not old objects, and it's a script to maintain.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Burning down whole cabinets that are 45 days old.

---

## 🛒 E-Commerce Full-Stack Example

```python
url = blob.generate_signed_url(version="v4", expiration=timedelta(minutes=30), method="PUT")
```
Bucket `shopnow-supplier-feeds` lifecycle: `Delete` when `age > 45`.

---

## 🧠 Key Takeaways / Memory Tips

- **Temporary, per-object access for outsiders → signed URLs.**
- **Auto-delete by age → lifecycle rule.**
  🧠 *"**Pass for 30 minutes, shredder at 45 days.**"*
- Related: **Q090**, **Q154** (lifecycle).

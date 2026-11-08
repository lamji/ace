# Q369: VM App Can Only Create Objects in One Logs Bucket (Dedicated SA + objectCreator on That Bucket)

**Topic:** IAM (Cloud Storage roles, service accounts)

## ❓ Question
> You are deploying a new application on a Compute Engine VM instance. This application needs to store operational logs in a Cloud Storage bucket named project-logs-us-central1 and have the ability to create new objects (logs) in this bucket. The application must be restricted from modifying or deleting existing objects or accessing any other buckets in the Google Cloud project. You must configure access following the principle of least privilege. What should you do?
>
> **A.** Create a dedicated service account for the application. Grant this service account the predefined roles/storage.objectCreator IAM role on the project-logs-us-central1 Cloud Storage bucket. Attach the service account to the Compute Engine VM instance.
>
> **B.** Grant the Compute Engine default service account the predefined roles/storage.objectAdmin IAM role on the Google Cloud project.
>
> **C.** Create a dedicated service account for the application. Generate a service account key, and grant the service account the predefined roles/storage.adm in IAM role on the project-logs-us-central1 Cloud Storage bucket. Store the key file on the Compute Engine VM.
>
> **D.** Grant the Compute Engine default service account the predefined roles/storage.objectCreator IAM role on the Google Cloud project. Attach the service account to the Compute Engine VM instance.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new app on a VM must write log files to the bucket project-logs-us-central1.
- **What you must achieve:** Let it create new files in that bucket.
- **The limits:** It must not change or delete existing files or reach any other bucket; least privilege.
- **What they're really asking:** Which identity and role give create-only access to that one bucket?

**Clues in the question:**
- Create-only → **`roles/storage.objectCreator`**.
- One bucket → grant **on the bucket**; dedicated SA, attached (no keys).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/storage.objectCreator 🔑
- **What it is:** Can create objects; cannot view, overwrite or delete them.
- **Looks like:** `gcloud storage buckets add-iam-policy-binding gs://project-logs-us-central1 --member=serviceAccount:logger@... --role=roles/storage.objectCreator`
- **Not to be confused with:** objectAdmin (full).
- **Analogy:** 📮 A drop box: you can put letters in, not take out.
- **In the online store:** —

### 🔗 How they fit together
```
 VM (logger SA) → objectCreator on project-logs-us-central1 ✅
```

---

## 🌍 Real-World Scenario

A VM writes logs as `logger-sa`, which only has **objectCreator** on one bucket.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a dedicated service account for the application. Grant this service account the predefined roles/storage.objectCreator IAM role on the project-logs-us-central1 Cloud Storage bucket. Attach the service account to the Compute Engine VM instance.

**Why it's correct:**
- ✔️ "**dedicated service account … Attach … to the … VM**" matches "**principle of least privilege**".
- ✔️ "**roles/storage.objectCreator … on the project-logs-us-central1 … bucket**" matches "**create new objects**" + "**restricted from modifying or deleting … or accessing any other buckets**".

📌 **When to use it:** Use it when a program should only drop new files into one place.
🏢 **Office example:** A drop box key for one mail slot: put letters in, never take them out.

### ❌ B
> **B.** Grant the Compute Engine default service account the predefined roles/storage.objectAdmin IAM role on the Google Cloud project.

**Wrong words:**
- ❌ "**default service account**" (shared) and ❌ "**objectAdmin … on the … project**": can delete everything everywhere.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Master keys to every mailbox.

### ❌ C
> **C.** Create a dedicated service account for the application. Generate a service account key, and grant the service account the predefined roles/storage.adm in IAM role on the project-logs-us-central1 Cloud Storage bucket. Store the key file on the Compute Engine VM.

**Wrong words:**
- ❌ "**Generate a service account key**" and ❌ "**storage.admin**": secrets and full control.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A copied master key.

### ❌ D
> **D.** Grant the Compute Engine default service account the predefined roles/storage.objectCreator IAM role on the Google Cloud project. Attach the service account to the Compute Engine VM instance.

**Wrong words:**
- ❌ "**default service account**" and ❌ "**on the Google Cloud project**": every bucket.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Drop-box rights to every mailbox.

---

## 🛒 E-Commerce Full-Stack Example

`order-logger@shopnow-prod` → objectCreator on `gs://shopnow-app-logs`.

---

## 🧠 Key Takeaways / Memory Tips

- **Write-only, one bucket → dedicated SA + objectCreator on that bucket.**
  🧠 *"**Drop box, one slot.**"*
- Related: **Q346**, **Q297**.

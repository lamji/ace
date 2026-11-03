# Q356: Cloud Run Reads Only Objects Under a Prefix in a Shared Bucket, Including New Ones (Uniform Access + IAM Condition on the Prefix)

**Topic:** Cloud Storage (IAM conditions)

## ❓ Question
> You are managing a web application that needs to read objects from a shared Cloud Storage bucket. You need to grant a Cloud Run service access to objects in the existing bucket that are named with the site1-data/ prefix while ensuring that the Cloud Run service has access to new objects as they are uploaded. Your solution should require minimal work to implement and maintain. What should you do?
>
> **A.** Enable fine-grained access control, and configure the uploader to set a per object access control list for the Cloud Run service identity to have the READER role when objects with the site1-data/ prefix are uploaded.
>
> **B.** Create a new bucket to store only objects with the site1-data/ prefix. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the project.
>
> **C.** Create a new bucket to store only objects with the site1-data/ prefix. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the bucket.
>
> **D.** Enable uniform bucket-level access, and configure an IAM binding on the existing bucket. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the bucket with an IAM condition for objects with the site1-data/ prefix.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Read only **`site1-data/`** objects, including **new ones**, minimal work.

**Clues in the question:**
- Prefix-scoped access that covers new objects → **IAM condition** `resource.name.startsWith(...)` (needs **uniform bucket-level access**).

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. IAM condition on object prefix 🔑
- **What it is:** A role binding that only applies when the object name starts with a prefix.
- **Looks like:** `--condition='expression=resource.name.startsWith("projects/_/buckets/shared/objects/site1-data/"),title=site1'`
- **Not to be confused with:** per-object ACLs.
- **Analogy:** 🗂️ Key that only opens drawers labeled 'site1'.
- **In the online store:** —

### 2. Uniform bucket-level access
- **What it is:** Turns off ACLs; access controlled only by IAM.
- **Looks like:** `gcloud storage buckets update gs://shared --uniform-bucket-level-access`
- **Not to be confused with:** fine-grained (ACLs).
- **Analogy:** —
- **In the online store:** —

### 🔗 How they fit together
```
 gs://shared (UBLA) + objectViewer IF name starts with site1-data/ ✅
```

---

## 🌍 Real-World Scenario

The Cloud Run service gets **objectViewer with a prefix condition**, covering new uploads automatically.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable fine-grained access control, and configure the uploader to set a per object access control list for the Cloud Run service identity to have the READER role when objects with the site1-data/ prefix are uploaded.

**Wrong words:**
- ❌ "**fine-grained … per object access control list**": every upload must set ACLs; heavy maintenance.

📌 **When to use it:** Use ACLs only for rare per-object needs.
🏢 **Office example:** Labeling each paper with who may read it.

### ❌ B
> **B.** Create a new bucket to store only objects with the site1-data/ prefix. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the project.

**Wrong words:**
- ❌ "**new bucket**" (migration work) and ❌ "**on the project**" (all buckets).

📌 **When to use it:** **Avoid.**
🏢 **Office example:** A new cabinet plus keys to every cabinet.

### ❌ C
> **C.** Create a new bucket to store only objects with the site1-data/ prefix. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the bucket.

**Wrong words:**
- ✔️ Bucket-level grant is fine.
- ❌ "**Create a new bucket**": moving data and changing uploaders is extra work.

📌 **When to use it:** Use a separate bucket when data should be separate anyway.
🏢 **Office example:** Buying a new cabinet.

### ✅ D
> **D.** Enable uniform bucket-level access, and configure an IAM binding on the existing bucket. Grant the Cloud Run service identity the roles/storage.objectViewer IAM role on the bucket with an IAM condition for objects with the site1-data/ prefix.

**Why it's correct:**
- ✔️ "**uniform bucket-level access … IAM binding on the existing bucket**" matches "**shared Cloud Storage bucket**" + "**minimal work**".
- ✔️ "**IAM condition for objects with the site1-data/ prefix**" matches "**named with the site1-data/ prefix**" + "**access to new objects as they are uploaded**".

📌 **When to use it:** Use it when someone should see only one labeled section of a shared cabinet, including new papers.
🏢 **Office example:** A key that opens only the 'site1' drawers, even new ones added later.

---

## 🛒 E-Commerce Full-Stack Example

`site1-web` SA → objectViewer on `gs://shopnow-shared` with prefix condition `site1-data/`.

---

## 🧠 Key Takeaways / Memory Tips

- **Prefix-scoped access → UBLA + IAM condition on resource.name.**
  🧠 *"**Condition the prefix.**"*
- Related: **Q346**.

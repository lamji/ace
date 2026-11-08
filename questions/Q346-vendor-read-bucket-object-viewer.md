# Q346: External Vendor Read-Only Access to One Bucket Only (Storage Object Viewer on the Bucket)

**Topic:** IAM (Cloud Storage roles)

## ❓ Question
> You manage a Google Cloud project that contains a critical marketing application. You need to grant an external vendor read-only access to the objects stored in a specific Cloud Storage bucket. The vendor must not be able to view any other resources in the project. What should you do?
>
> **A.** Create a custom IAM role with the storage.objects.get permission, and grant the vendor this role on the project.
>
> **B.** Grant the vendor the Storage Object User role on the project.
>
> **C.** Grant the vendor the Storage Object User role on the bucket.
>
> **D.** Grant the vendor the Storage Object Viewer role on the bucket.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A project holds a critical marketing app.
- **What you must achieve:** Give an outside vendor read-only access to the files in one specific bucket.
- **The limits:** The vendor must not see any other resources in the project.
- **What they're really asking:** Which role do you grant, and on what?

**Clues in the question:**
- "**read-only**" → **Storage Object Viewer**.
- "**specific … bucket**" + "**must not … view any other resources**" → grant **on the bucket**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/storage.objectViewer 🔑
- **What it is:** Read (get/list) objects; no writes.
- **Looks like:** `gcloud storage buckets add-iam-policy-binding gs://mkt-assets --member=user:vendor@agency.com --role=roles/storage.objectViewer`
- **Not to be confused with:** Storage Object User (read + write).
- **Analogy:** 👀 Look, don't touch.
- **In the online store:** —

### 🔗 How they fit together
```
 vendor → objectViewer on gs://mkt-assets only ✅
```

---

## 🌍 Real-World Scenario

A marketing agency gets **Object Viewer** on one bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a custom IAM role with the storage.objects.get permission, and grant the vendor this role on the project.

**Wrong words:**
- ✔️ Read-only permission.
- ❌ "**on the project**": all buckets readable.

📌 **When to use it:** Use custom roles when predefined don't fit.
🏢 **Office example:** A key to every cabinet's drawers.

### ❌ B
> **B.** Grant the vendor the Storage Object User role on the project.

**Wrong words:**
- ❌ "**Storage Object User**": can create/modify objects.
- ❌ "**on the project**": all buckets.

📌 **When to use it:** Use Object User for app writers.
🏢 **Office example:** Edit rights to every cabinet.

### ❌ C
> **C.** Grant the vendor the Storage Object User role on the bucket.

**Wrong words:**
- ✔️ On the bucket is right.
- ❌ "**Storage Object User**": not read-only.

📌 **When to use it:** Use it when someone should add and change files in one bucket.
🏢 **Office example:** Edit rights to one cabinet.

### ✅ D
> **D.** Grant the vendor the Storage Object Viewer role on the bucket.

**Why it's correct:**
- ✔️ "**Storage Object Viewer**" matches "**read-only access to the objects**".
- ✔️ "**on the bucket**" matches "**a specific Cloud Storage bucket**" + "**must not be able to view any other resources**".

📌 **When to use it:** Use it when an outsider should only look at files in one folder.
🏢 **Office example:** A visitor key that opens one cabinet, look-only.

---

## 🛒 E-Commerce Full-Stack Example

`agency@partner.com` → objectViewer on `gs://shopnow-campaign-assets`.

---

## 🧠 Key Takeaways / Memory Tips

- **Read-only, one bucket → Object Viewer on the bucket.**
  🧠 *"**View the bucket, not the project.**"*
- Related: **Q356**, **Q369**.

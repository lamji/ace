# Q250: Invoices: Keep 5 Years, Up to 5 Revisions, Cheaper After 365 Days (Object Versioning + Lifecycle Rules)

**Topic:** Cloud Storage (versioning, lifecycle)

## ❓ Question
> You need to migrate invoice documents stored on-premises to Cloud Storage. The documents have the following storage requirements: • Documents must be kept for five years. • Up to five revisions of the same invoice document must be stored, to allow for corrections. • Documents older than 365 days should be moved to lower cost storage tiers. You want to follow Google-recommended practices to minimize your operational and development costs. What should you do?
>
> **A.** Enable retention policies on the bucket, and use Cloud Scheduler to invoke a Cloud Function to move or delete your documents based on their metadata.
>
> **B.** Enable retention policies on the bucket, use lifecycle rules to change the storage classes of the objects, set the number of versions, and delete old files.
>
> **C.** Enable object versioning on the bucket, and use Cloud Scheduler to invoke a Cloud Functions instance to move or delete your documents based on their metadata.
>
> **D.** Enable object versioning on the bucket, use lifecycle conditions to change the storage class of the objects, set the number of versions, and delete old files.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Keep **5 revisions**, move to cheaper class after **365 days**, delete after **5 years**, no code.

**Clues in the question:**
- "**Up to five revisions**" → **object versioning** + lifecycle `numNewerVersions`.
- "**older than 365 days … lower cost**" + "**kept for five years**" → **lifecycle** SetStorageClass + Delete.
- "**minimize … development costs**" → no functions.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Object versioning 🔑
- **What it is:** Keeps older versions of an object when it's overwritten or deleted.
- **Looks like:** `gcloud storage buckets update gs://invoices --versioning`
- **Not to be confused with:** retention policy.
- **Analogy:** 📑 Keeping each corrected draft.
- **In the online store:** Invoice corrections.

### 2. Lifecycle conditions
- **What it is:** age, numNewerVersions, isLive… with actions SetStorageClass / Delete.
- **Looks like:** `numNewerVersions: 5 → Delete`; `age: 365 → COLDLINE`; `age: 1825 → Delete`
- **Not to be confused with:** —
- **Analogy:** 🗄️ Automatic filing rules.
- **In the online store:** —

### 🔗 How they fit together
```
 versioning ON → lifecycle: age>365 → Coldline/Archive; versions >5 → delete; age>1825 → delete ✅
```

---

## 🌍 Real-World Scenario

Finance moves invoices to a bucket with **versioning** and **lifecycle rules**: keep 5 versions, move to Archive after a year, delete after 5 years.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable retention policies on the bucket, and use Cloud Scheduler to invoke a Cloud Function to move or delete your documents based on their metadata.

**Wrong words:**
- ❌ "**retention policies**": block deletion but don't keep revisions.
- ❌ "**Cloud Scheduler … Cloud Function**": custom code.

📌 **When to use it:** Use retention policies for "cannot delete before" rules.
🏢 **Office example:** A "do not shred" stamp plus a hired clerk.

### ❌ B
> **B.** Enable retention policies on the bucket, use lifecycle rules to change the storage classes of the objects, set the number of versions, and delete old files.

**Wrong words:**
- ✔️ Lifecycle rules are right.
- ❌ "**retention policies**" instead of versioning: revisions aren't kept; overwrites are blocked/lost.

📌 **When to use it:** Use retention when deletion must be prevented legally.
🏢 **Office example:** No drafts kept.

### ❌ C
> **C.** Enable object versioning on the bucket, and use Cloud Scheduler to invoke a Cloud Functions instance to move or delete your documents based on their metadata.

**Wrong words:**
- ✔️ Versioning is right.
- ❌ "**Cloud Scheduler … Cloud Functions**": code to maintain, against "**minimize … development costs**".

📌 **When to use it:** Use functions only if lifecycle can't do it.
🏢 **Office example:** Hiring a clerk for an automatic rule.

### ✅ D
> **D.** Enable object versioning on the bucket, use lifecycle conditions to change the storage class of the objects, set the number of versions, and delete old files.

**Why it's correct:**
- ✔️ "**Enable object versioning**" matches "**Up to five revisions of the same invoice**".
- ✔️ "**lifecycle conditions to change the storage class**" matches "**older than 365 days … lower cost storage tiers**".
- ✔️ "**set the number of versions, and delete old files**" matches "**five revisions**" + "**kept for five years**".

📌 **When to use it:** Use it when you must keep a few corrected copies of each record, cheaply, for a set number of years.
🏢 **Office example:** Keeping the last five corrected drafts of each invoice, moving old ones to the basement after a year, and shredding after five years — all by rule.

---

## 🛒 E-Commerce Full-Stack Example

Bucket `shopnow-invoices`: versioning on; lifecycle: `numNewerVersions>=5 → Delete`, `age>=365 → ARCHIVE`, `age>=1825 → Delete`.

---

## 🧠 Key Takeaways / Memory Tips

- **Revisions → versioning. Age-based moves/deletes → lifecycle. No code.**
  🧠 *"**Versioning keeps drafts; lifecycle files them.**"*
- Related: **Q248**, **Q154**.

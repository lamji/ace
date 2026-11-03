# Q248: Only Files From the Last 30 Days Are Used; Save Cost Automatically (Lifecycle Rule → Archive After 30 Days)

**Topic:** Cloud Storage (Object Lifecycle Management)

## ❓ Question
> Your application stores files on Cloud Storage by using the Standard Storage class. The application only requires access to files created in the last 30 days. You want to automatically save costs on files that are no longer accessed by the application. What should you do?
>
> **A.** Create an object lifecycle on the storage bucket to change the storage class to Archive Storage for objects with an age over 30 days.
>
> **B.** Create a cron job in Cloud Scheduler to call a Cloud Functions instance every day to delete files older than 30 days.
>
> **C.** Create a retention policy on the storage bucket of 30 days, and lock the bucket by using a retention policy lock.
>
> **D.** Enable object versioning on the storage bucket and add lifecycle rules to expire non-current versions after 30 days.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** After 30 days files aren't used. **Save cost automatically** (not delete).

**Clues in the question:**
- "**save costs on files that are no longer accessed**" → move them to a cheaper class, **automatically** → **lifecycle rule** `age > 30` → **Archive**.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Object Lifecycle Management 🔑
- **What it is:** Bucket rules that **change class** or **delete** objects by age, version count, etc. No code.
- **Looks like:** `{"action":{"type":"SetStorageClass","storageClass":"ARCHIVE"},"condition":{"age":30}}`
- **Not to be confused with:** retention policy.
- **Analogy:** 🗄️ An automatic filing rule.
- **In the online store:** Old order PDFs.

### 2. Retention policy
- **What it is:** Prevents deletion **before** a minimum age. It doesn't save money.
- **Looks like:** —
- **Not to be confused with:** lifecycle.
- **Analogy:** 🔒 "Do not shred before" stamp.
- **In the online store:** —

### 🔗 How they fit together
```
 Standard (0–30 days, used) ─ lifecycle age>30 ─► Archive (cheap) ✅
```

---

## 🌍 Real-World Scenario

An app reads only recent uploads. A **lifecycle rule** moves objects older than 30 days to **Archive**, cutting storage cost with no code.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create an object lifecycle on the storage bucket to change the storage class to Archive Storage for objects with an age over 30 days.

**Why it's correct:**
- ✔️ "**object lifecycle on the storage bucket**" matches "**automatically**".
- ✔️ "**change the storage class to Archive Storage for objects with an age over 30 days**" matches "**save costs on files that are no longer accessed**".

📌 **When to use it:** Use it when files go cold after a while but must still be kept.
🏢 **Office example:** An automatic rule that moves month-old papers from your desk to the cheap basement archive.

### ❌ B
> **B.** Create a cron job in Cloud Scheduler to call a Cloud Functions instance every day to delete files older than 30 days.

**Wrong words:**
- ❌ "**delete files older than 30 days**": the question asks to **save cost**, not delete.
- ❌ Cron + function: custom code.

📌 **When to use it:** Use custom jobs only if lifecycle can't express the rule.
🏢 **Office example:** Shredding files you were told to keep cheaply.

### ❌ C
> **C.** Create a retention policy on the storage bucket of 30 days, and lock the bucket by using a retention policy lock.

**Wrong words:**
- ❌ "**retention policy … lock**": stops deletion; doesn't reduce cost.

📌 **When to use it:** Use retention locks for legal "must keep" rules.
🏢 **Office example:** A "do not shred" stamp; nothing gets cheaper.

### ❌ D
> **D.** Enable object versioning on the storage bucket and add lifecycle rules to expire non-current versions after 30 days.

**Wrong words:**
- ❌ "**object versioning … expire non-current versions**": deals with old **versions**, not old files.

📌 **When to use it:** Use it to clean up old versions.
🏢 **Office example:** Throwing away drafts while the old final copies stay on the expensive desk.

---

## 🛒 E-Commerce Full-Stack Example

`gsutil lifecycle set archive-30d.json gs://shopnow-uploads` (SetStorageClass ARCHIVE, age 30).

---

## 🧠 Key Takeaways / Memory Tips

- **Automatic cost savings by age → lifecycle SetStorageClass.** Retention = can't delete.
  🧠 *"**Cold after 30? Lifecycle to Archive.**"*
- Related: **Q154**, **Q250**, **Q290**.

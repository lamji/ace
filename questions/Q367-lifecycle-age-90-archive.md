# Q367: Move Records to the Cheapest Class 90 Days After Creation (Lifecycle Rule age 90 → SetStorageClass Archive)

**Topic:** Cloud Storage (lifecycle)

## ❓ Question
> You are managing your company's archival records that are stored in a Cloud Storage bucket using the Multi-Regional storage class. These objects are rarely accessed after 90 days but must be retained indefinitely to meet regulatory compliance requirements. You need to implement a cost-effective process that automatically transitions these objects to the lowest-cost storage class suitable for long-term retention immediately after the 90-day period. What should you do?
>
> **A.** Enable Object Versioning on the bucket, and create an Object Lifecycle Management rule that sets the daysSinceNoncurrentTime condition to 90 days, transitioning noncurrent versions to Archive storage.
>
> **B.** Create an Object Lifecycle Management rule on the bucket that specifies an age condition of 90 days and uses the SetStorageClass action to transition the objects to Archive storage.
>
> **C.** Create a nightly scheduled Cloud Run function that uses the Cloud Storage API to change the storage class of all objects older than 90 days to Archive storage.
>
> **D.** Create an Object Lifecycle Management rule on the bucket that specifies the createdBefore condition set to 90 days ago and uses the Delete action to remove the objects.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Archive records are in a Cloud Storage bucket using the Multi-Regional class. They are rarely read after 90 days but must be kept forever for compliance.
- **What you must achieve:** Automatically move them to the cheapest long-term class right after 90 days.
- **The limits:** Cost-effective and automatic.
- **What they're really asking:** Which bucket rule moves files at 90 days, and to which class?

**Clues in the question:**
- Automatic transition → **Object Lifecycle Management**.
- "**lowest-cost … long-term**" → **Archive**. Condition **age: 90**.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Lifecycle rule 🔑 (review)
- **What it is:** Bucket rule: when condition met, act (SetStorageClass/Delete).
- **Looks like:** `{"action":{"type":"SetStorageClass","storageClass":"ARCHIVE"},"condition":{"age":90}}`
- **Not to be confused with:** createdBefore (fixed date).
- **Analogy:** 📦 Auto-move boxes to the basement after 90 days.
- **In the online store:** —

### 🔗 How they fit together
```
 age ≥ 90 days → Archive ✅ (kept forever)
```

---

## 🌍 Real-World Scenario

A compliance bucket moves each record to **Archive** at **age 90**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Object Versioning on the bucket, and create an Object Lifecycle Management rule that sets the daysSinceNoncurrentTime condition to 90 days, transitioning noncurrent versions to Archive storage.

**Wrong words:**
- ❌ "**daysSinceNoncurrentTime … noncurrent versions**": affects old versions only, not live records.

📌 **When to use it:** Use it to tidy old versions.
🏢 **Office example:** Moving only old drafts.

### ✅ B
> **B.** Create an Object Lifecycle Management rule on the bucket that specifies an age condition of 90 days and uses the SetStorageClass action to transition the objects to Archive storage.

**Why it's correct:**
- ✔️ "**age condition of 90 days**" matches "**immediately after the 90-day period**".
- ✔️ "**SetStorageClass … Archive**" matches "**lowest-cost storage class suitable for long-term retention**" + "**automatically**".

📌 **When to use it:** Use it when files go quiet after a set time but must be kept.
🏢 **Office example:** Boxes automatically moved to the cheapest basement 90 days after filing.

### ❌ C
> **C.** Create a nightly scheduled Cloud Run function that uses the Cloud Storage API to change the storage class of all objects older than 90 days to Archive storage.

**Wrong words:**
- ❌ "**nightly scheduled Cloud Run function**": custom code; lifecycle rules do it free.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Hiring someone to move boxes nightly.

### ❌ D
> **D.** Create an Object Lifecycle Management rule on the bucket that specifies the createdBefore condition set to 90 days ago and uses the Delete action to remove the objects.

**Wrong words:**
- ❌ "**Delete action**": must be retained indefinitely.
- ❌ "**createdBefore … 90 days ago**": a fixed date, not rolling.

📌 **When to use it:** Use Delete when data can be removed.
🏢 **Office example:** Shredding records you must keep.

---

## 🛒 E-Commerce Full-Stack Example

`gs://shopnow-compliance`: age 90 → ARCHIVE.

---

## 🧠 Key Takeaways / Memory Tips

- **Rolling time-based tiering → lifecycle rule with age + SetStorageClass.**
  🧠 *"**Age moves, Archive keeps.**"*
- Related: **Q292**.

# Q155: Record Every Read of Sensitive Bucket Data (Enable Data Access Audit Logs for Cloud Storage)

**Topic:** Logging (Data Access audit logs), DLP, IAP

## ❓ Question
> You are storing sensitive information in a Cloud Storage bucket. For legal reasons, you need to be able to record all requests that read any of the stored data. You want to make sure you comply with these requirements. What should you do?
>
> **A.** Enable the Identity Aware Proxy API on the project.
>
> **B.** Scan the bucket using the Data Loss Prevention API.
>
> **C.** Allow only a single Service Account access to read the data.
>
> **D.** Enable Data Access audit logs for the Cloud Storage API.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Every **read** of the bucket's data must be **recorded**.

**Clues in the question:**
- "**record all requests that read any of the stored data**" → **Data Access audit logs** (DATA_READ).
- For Cloud Storage they're **off by default**, so you must **enable** them.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Data Access audit logs 🔑 (review from Q117)
- **What it is:** Logs of **reading and writing user data**. For most services, including Cloud Storage, you must **turn them on** (IAM & Admin → Audit Logs).
- **Looks like:** Audit Logs → Google Cloud Storage → ✓ Data Read ✓ Data Write
- **Not to be confused with:** Admin Activity (always on).
- **Analogy:** 📄 A "who opened which file" logbook.
- **In the online store:** Who downloaded customer documents.

### 2. Cloud DLP
- **What it is:** Scans data to **find sensitive content** (card numbers, IDs). It doesn't log who reads it.
- **Looks like:** `dlp.inspect` job
- **Not to be confused with:** audit logging.
- **Analogy:** 🔍 A clerk who checks files for secret info.
- **In the online store:** Find credit cards in uploads.

### 🔗 How they fit together
```
 IAM & Admin → Audit Logs → Cloud Storage: Data Read ✓ ✅
 every object GET → log entry (who, when, which object)
```

---

## 🌍 Real-World Scenario

A law firm stores client files in a bucket and must prove who accessed them. The admin enables **Data Access audit logs (Data Read)** for Cloud Storage. Every download now appears in Cloud Logging with the user and time.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable the Identity Aware Proxy API on the project.

**Wrong words:**
- ❌ "**Enable the Identity Aware Proxy API**": IAP controls access to apps and VMs. It doesn't log Cloud Storage reads.

📌 **When to use it:** Use IAP to protect web apps or SSH access by identity.
🏢 **Office example:** A guard at a different door.

### ❌ B
> **B.** Scan the bucket using the Data Loss Prevention API.

**Wrong words:**
- ❌ "**Data Loss Prevention API**": it finds sensitive data. It doesn't record who reads it.

📌 **When to use it:** Use DLP to discover or mask sensitive data.
🏢 **Office example:** Checking files for secrets instead of logging who opened them.

### ❌ C
> **C.** Allow only a single Service Account access to read the data.

**Wrong words:**
- ❌ "**single Service Account access**": it limits access, but nothing is recorded.

📌 **When to use it:** Use least privilege to limit who can read.
🏢 **Office example:** Giving one person the key, but keeping no logbook.

### ✅ D
> **D.** Enable Data Access audit logs for the Cloud Storage API.

**Why it's correct:**
- ✔️ "**Enable Data Access audit logs**" matches "**record all requests that read**": reads are logged with who and when.
- ✔️ "**for the Cloud Storage API**" matches "**Cloud Storage bucket**": they're off by default for Cloud Storage, so you must enable them.

📌 **When to use it:** Use it when the law requires a record of everyone who opened certain files.
🏢 **Office example:** Starting a logbook where everyone who opens the cabinet signs in.

---

## 🛒 E-Commerce Full-Stack Example

Console → IAM & Admin → Audit Logs → **Google Cloud Storage** → ✓ Data Read, ✓ Data Write. Logs Explorer: `logName:"data_access" resource.labels.bucket_name="shopnow-kyc-docs"`.

---

## 🧠 Key Takeaways / Memory Tips

- **Record reads → enable Data Access logs** (off by default for most services).
  🧠 *"**Who read it? Turn on Data Access logs.**"*
- Related: **Q117**, **Q113**, **Q169**.

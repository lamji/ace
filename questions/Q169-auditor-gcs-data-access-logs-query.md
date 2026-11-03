# Q169: Auditor Wants to Know Who Accessed Cloud Storage Data (Turn On Data Access Logs, Filter in Logs Viewer)

**Topic:** Logging (Data Access audit logs, Admin Activity logs)

## ❓ Question
> Your auditor wants to view your organization's use of data in Google Cloud. The auditor is most interested in auditing who accessed data in Cloud Storage buckets. You need to help the auditor access the data they need. What should you do?
>
> **A.** Turn on Data Access Logs for the buckets they want to audit, and then build a query in the log viewer that filters on Cloud Storage.
>
> **B.** Assign the appropriate permissions, and then create a Data Studio report on Admin Activity Audit Logs.
>
> **C.** Assign the appropriate permissions, and then use Cloud Monitoring to review metrics.
>
> **D.** Use the export logs API to provide the Admin Activity Audit Logs in the format they want.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** "**Who accessed data** in buckets?" Which logs?

**Clues in the question:**
- "**who accessed data in Cloud Storage buckets**" → **Data Access** logs (off by default → **turn them on**).
- Admin Activity logs show **config changes**, not reads.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Data Access logs 🔑 (review from Q155)
- **What it is:** Logs of reads and writes of data. **Off by default** for Cloud Storage.
- **Looks like:** IAM & Admin → Audit Logs → Cloud Storage → Data Read
- **Not to be confused with:** Admin Activity.
- **Analogy:** 📄 The "who opened which file" log.
- **In the online store:** Who downloaded customer exports.

### 2. Logs Explorer query
- **What it is:** Filter logs by service, log name and principal.
- **Looks like:** `resource.type="gcs_bucket" logName:"data_access"`
- **Not to be confused with:** Monitoring metrics.
- **Analogy:** 🔎 Searching the logbook.
- **In the online store:** Find reads of the KYC bucket.

### 🔗 How they fit together
```
 enable Data Access (Cloud Storage) → reads logged → Logs Explorer filter gcs_bucket ✅
```

---

## 🌍 Real-World Scenario

An auditor asks who read files in the finance buckets. The admin **turns on Data Access logs** for Cloud Storage and builds a Logs Explorer query on `gcs_bucket` + `data_access` for the auditor.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Turn on Data Access Logs for the buckets they want to audit, and then build a query in the log viewer that filters on Cloud Storage.

**Why it's correct:**
- ✔️ "**Turn on Data Access Logs**" matches "**who accessed data**": reads are recorded (they're off by default).
- ✔️ "**build a query in the log viewer that filters on Cloud Storage**" matches "**data in Cloud Storage buckets**".

📌 **When to use it:** Use it when someone needs to see who opened which stored files.
🏢 **Office example:** Starting the "who opened which file" logbook and searching it for the finance cabinets.

### ❌ B
> **B.** Assign the appropriate permissions, and then create a Data Studio report on Admin Activity Audit Logs.

**Wrong words:**
- ❌ "**Admin Activity Audit Logs**": they show configuration changes, not who read data.

📌 **When to use it:** Use Admin Activity for "who changed settings".
🏢 **Office example:** Checking the "who changed the locks" log to see who read files.

### ❌ C
> **C.** Assign the appropriate permissions, and then use Cloud Monitoring to review metrics.

**Wrong words:**
- ❌ "**Cloud Monitoring to review metrics**": metrics show counts and performance, not who accessed data.

📌 **When to use it:** Use Monitoring for performance.
🏢 **Office example:** Reading the electricity meter.

### ❌ D
> **D.** Use the export logs API to provide the Admin Activity Audit Logs in the format they want.

**Wrong words:**
- ❌ "**Admin Activity Audit Logs**": wrong log type (see B).

📌 **When to use it:** Use log exports to deliver logs elsewhere.
🏢 **Office example:** Exporting the wrong logbook nicely formatted.

---

## 🛒 E-Commerce Full-Stack Example

Enable **Cloud Storage → Data Read/Write** audit logs. Query:
```
resource.type="gcs_bucket" logName:"cloudaudit.googleapis.com%2Fdata_access"
resource.labels.bucket_name="shopnow-finance"
```

---

## 🧠 Key Takeaways / Memory Tips

- **Who accessed data → Data Access logs (enable first).**
- Admin Activity = config changes.
  🧠 *"**Accessed data? Data Access logs.**"*
- Related: **Q155**, **Q117**, **Q113**.

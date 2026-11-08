# Q113: Auditor Must Read Audit Logs Including Data Access Logs (Private Logs Viewer)

**Topic:** Logging / IAM (roles/logging.privateLogViewer, Data Access logs, Admin Activity logs)

## ❓ Question
> You need to assign a Cloud Identity and Access Management (Cloud IAM) role to an external auditor. The auditor needs to have permissions to review your Google Cloud Platform (GCP) Audit Logs and also to review your Data Access logs. What should you do?
>
> **A.** Assign the auditor the IAM role roles/logging.privateLogViewer. Perform the export of logs to Cloud Storage.
>
> **B.** Assign the auditor the IAM role roles/logging.privateLogViewer. Direct the auditor to also review the logs for changes to Cloud IAM policy.
>
> **C.** Assign the auditor's IAM user to a custom role that has logging.privateLogEntries.list permission. Perform the export of logs to Cloud Storage.
>
> **D.** Assign the auditor's IAM user to a custom role that has logging.privateLogEntries.list permission. Direct the auditor to also review the logs for changes to Cloud IAM policy.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

> ℹ️ **Note:** This is the site's accepted (most voted) answer. The key part is the role `roles/logging.privateLogViewer`. Exporting to Cloud Storage isn't needed for reviewing logs.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An external auditor needs to review Audit Logs and also Data Access logs.
- **What you must achieve:** Give the auditor the right IAM role.
- **The limits:** None stated.
- **What they're really asking:** Which role lets them read both kinds of logs?

**Clues in the question:**
- "**Data Access logs**": these are **private logs**. The normal Logs Viewer can't see them. You need **Private Logs Viewer** (`roles/logging.privateLogViewer`).
- "**review your … Audit Logs**": Private Logs Viewer includes Logs Viewer, so it covers Admin Activity logs too, which record **IAM policy changes**.
- No requirement to **export** anything, and a predefined role is better than a custom one.

**Exam topic:** Logging / IAM.

---

## 📚 Key Terms Explained

### 1. roles/logging.privateLogViewer 🔑
- **What it is:** A predefined role that can read **all logs, including private ones** like **Data Access** audit logs. It includes everything in Logs Viewer.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-prod --member=user:auditor@shopnow.com --role=roles/logging.privateLogViewer`
- **Not to be confused with:** roles/logging.viewer, which can't read Data Access logs.
- **Analogy:** 🔐 A pass to the **locked records room** plus the normal records room.
- **In the online store:** The auditor sees who read customer data.

### 2. Data Access audit logs (review from Q086, Q117)
- **What it is:** Logs of **who read or changed user data** (e.g., read a bucket object, queried a table). Considered **private**.
- **Looks like:** `cloudaudit.googleapis.com%2Fdata_access`
- **Not to be confused with:** Admin Activity logs (configuration changes).
- **Analogy:** 📄 The "who opened which file" log.
- **In the online store:** Who read the customers table.

### 3. Admin Activity logs
- **What it is:** Logs of **configuration changes**, including **IAM policy changes** (SetIamPolicy).
- **Looks like:** `methodName=SetIamPolicy`
- **Not to be confused with:** Data Access.
- **Analogy:** 🔧 The "who changed the locks" log.
- **In the online store:** Who granted roles last week.

### 🔗 How they fit together
```
 roles/logging.privateLogViewer ✅
   ├── Admin Activity logs (IAM policy changes) ← auditor reviews these too
   ├── System Event logs
   └── Data Access logs (private)               ← needs PRIVATE log viewer
```

---

## 🌍 Real-World Scenario

An external auditor must check who accessed customer data and who changed permissions. The admin grants **Private Logs Viewer** and points the auditor to the Admin Activity logs for SetIamPolicy events. Nothing needs to be exported.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Assign the auditor the IAM role roles/logging.privateLogViewer. Perform the export of logs to Cloud Storage.

**Wrong words:**
- ✔️ "roles/logging.privateLogViewer" is the right role.
- ❌ "**Perform the export of logs to Cloud Storage**": not needed. The auditor can read the logs directly, and an export adds cost and work.

📌 **When to use it:** Export logs to Cloud Storage when you must keep them for years (see Q061).
🏢 **Office example:** Photocopying the whole logbook when the auditor could just read it.

### ✅ B
> **B.** Assign the auditor the IAM role roles/logging.privateLogViewer. Direct the auditor to also review the logs for changes to Cloud IAM policy.

**Why it's correct:**
- ✔️ "**roles/logging.privateLogViewer**" matches "**review your Data Access logs**": only the private log viewer can read Data Access logs.
- ✔️ "**privateLogViewer**" (includes Logs Viewer) matches "**review your … Audit Logs**": it covers all the audit log types.
- ✔️ "**review the logs for changes to Cloud IAM policy**" matches "**Audit Logs**": IAM changes are in the Admin Activity audit logs.

📌 **When to use it:** Use it when someone must read every log, including the private ones about who touched data.
🏢 **Office example:** Giving the auditor a pass to both the normal records room and the locked one.

### ❌ C
> **C.** Assign the auditor's IAM user to a custom role that has logging.privateLogEntries.list permission. Perform the export of logs to Cloud Storage.

**Wrong words:**
- ❌ "**custom role that has logging.privateLogEntries.list**": a predefined role already does this. Custom roles are extra work.
- ❌ "**export of logs to Cloud Storage**": not needed.

📌 **When to use it:** Use a custom role only when no predefined role fits.
🏢 **Office example:** Hand-making a pass when a ready-made one exists, then photocopying the logbook anyway.

### ❌ D
> **D.** Assign the auditor's IAM user to a custom role that has logging.privateLogEntries.list permission. Direct the auditor to also review the logs for changes to Cloud IAM policy.

**Wrong words:**
- ✔️ "review the logs for changes to Cloud IAM policy" is fine.
- ❌ "**custom role**": unnecessary when `roles/logging.privateLogViewer` exists.

📌 **When to use it:** Use a custom role when you need fewer permissions than any predefined role.
🏢 **Office example:** Hand-making a pass for the locked records room when the front desk has one.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member=user:auditor-2026@shopnow.com --role=roles/logging.privateLogViewer
```
The auditor opens Logs Explorer:
- `logName:"data_access"` shows who read `customers` in BigQuery.
- `protoPayload.methodName="SetIamPolicy"` shows who changed roles.

---

## 🧠 Key Takeaways / Memory Tips

- **Data Access logs → roles/logging.privateLogViewer.** Logs Viewer can't see them.
- IAM changes live in Admin Activity logs.
- Prefer predefined roles over custom ones.
  🧠 *"**Private logs → Private Logs Viewer.**"*
- Related: **Q086** (Activity log categories), **Q095** (IAM changes in Admin Activity), **Q025** (auditors).

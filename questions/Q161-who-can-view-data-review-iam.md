# Q161: Who Has Access to View Data in the Project? (Review IAM Permissions)

**Topic:** IAM (reviewing access vs audit logs, IAP, DLP)

## ❓ Question
> You are performing a monthly security check of your Google Cloud environment and want to know who has access to view data stored in your Google Cloud Project. What should you do?
>
> **A.** Enable Audit Logs for all APIs that are related to data storage.
>
> **B.** Review the IAM permissions for any role that allows for data access.
>
> **C.** Review the Identity-Aware Proxy settings for each resource.
>
> **D.** Create a Data Loss Prevention job.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You do a monthly security check of your Google Cloud environment.
- **What you must achieve:** Find out who can view the data stored in your project.
- **The limits:** None stated.
- **What they're really asking:** Where do you look to see who has access to view data?

**Clues in the question:**
- "**who has access to view data**": that's about **permissions**, not activity → review **IAM** roles that include data access.
- Audit logs answer "who **did** read", not "who **can** read".

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. IAM permissions 🔑
- **What it is:** Roles bound to members define **who can do what**. Data-access roles include `storage.objectViewer`, `bigquery.dataViewer`, and so on.
- **Looks like:** IAM page → filter by role; or Policy Analyzer: "who can read bucket X?"
- **Not to be confused with:** audit logs.
- **Analogy:** 📋 Today's access list on the door.
- **In the online store:** Who can read customer data.

### 2. Audit logs vs IAM
- **What it is:** Logs = what **happened**. IAM = what's **allowed**.
- **Looks like:** Data Access logs / IAM policy
- **Not to be confused with:** each other.
- **Analogy:** 📓 Logbook vs access list.
- **In the online store:** Both used in audits.

### 🔗 How they fit together
```
 "who CAN view data?" → IAM roles with data access ✅
 "who DID view data?" → Data Access audit logs
```

---

## 🌍 Real-World Scenario

During a monthly review, the security lead uses the IAM page (and Policy Analyzer) to list everyone holding roles like Storage Object Viewer or BigQuery Data Viewer, and removes any that aren't needed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Audit Logs for all APIs that are related to data storage.

**Wrong words:**
- ❌ "**Enable Audit Logs**": logs record future **activity**. They don't list who **has access** today.

📌 **When to use it:** Use audit logs to see who actually read data.
🏢 **Office example:** Starting a logbook to find out who holds keys.

### ✅ B
> **B.** Review the IAM permissions for any role that allows for data access.

**Why it's correct:**
- ✔️ "**Review the IAM permissions for any role that allows for data access**" matches "**who has access to view data**": IAM shows who is allowed to read.

📌 **When to use it:** Use it when you need the current list of who is allowed in.
🏢 **Office example:** Reading the door access list for every room with files.

### ❌ C
> **C.** Review the Identity-Aware Proxy settings for each resource.

**Wrong words:**
- ❌ "**Identity-Aware Proxy settings**": IAP covers access to web apps or VMs, not who can read stored data in general.

📌 **When to use it:** Use it to review access to IAP-protected apps.
🏢 **Office example:** Checking one meeting room's guest list.

### ❌ D
> **D.** Create a Data Loss Prevention job.

**Wrong words:**
- ❌ "**Data Loss Prevention job**": it finds sensitive content. It doesn't show who has access.

📌 **When to use it:** Use DLP to find sensitive data.
🏢 **Office example:** Scanning files for secrets instead of checking who has keys.

---

## 🛒 E-Commerce Full-Stack Example

IAM → filter by `roles/storage.objectViewer`, `roles/bigquery.dataViewer`. Policy Analyzer query: "Who can access `shopnow-crm.customers`?"

---

## 🧠 Key Takeaways / Memory Tips

- **Who CAN access → IAM.** Who DID access → audit logs.
  🧠 *"**Can = IAM; did = logs.**"*
- Related: **Q148**, **Q117**.

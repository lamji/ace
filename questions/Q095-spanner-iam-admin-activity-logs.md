# Q095: When Were Users Added to Cloud Spanner IAM Roles? (Admin Activity Logs)

**Topic:** Logging (Admin Activity audit logs, IAM policy changes) vs IAM console / Monitoring

## ❓ Question
> You want to find out when users were added to Cloud Spanner Identity Access Management (IAM) roles on your Google Cloud Platform (GCP) project. What should you do in the GCP Console?
>
> **A.** Open the Cloud Spanner console to review configurations.
>
> **B.** Open the IAM & admin console to review IAM policies for Cloud Spanner roles.
>
> **C.** Go to the Stackdriver Monitoring console and review information for Cloud Spanner.
>
> **D.** Go to the Stackdriver Logging console, review admin activity logs, and filter them for Cloud Spanner IAM roles.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You use the Google Cloud console.
- **What you must achieve:** Find out when users were added to Cloud Spanner IAM roles.
- **The limits:** Do it in the console.
- **What they're really asking:** Where in the console do you see when roles were granted?

**Clues in the question:**
- "**find out when**": you need **history with timestamps** → **logs**.
- "**users were added to … IAM roles**": changing an IAM policy is an **admin activity** → **Admin Activity audit logs**.
- The IAM page shows **who has access now**, not **when** it was given.

**Exam topic:** Logging / IAM.

---

## 📚 Key Terms Explained

### 1️⃣ Admin Activity audit logs 🔑 (review from Q086)
- **What it is:** Logs of **configuration changes**: create, delete, change settings, **change IAM policies (SetIamPolicy)**. Always on and free. Each entry has a timestamp and who did it.
- **Looks like:** `protoPayload.methodName="google.spanner.admin.instance.v1.InstanceAdmin.SetIamPolicy"` · `ana@shopnow.com` · `2026-10-30 14:02`
- **Not to be confused with:** the current IAM policy (a snapshot with no dates).
- **Analogy:** 📓 The **logbook** that says "Ben was added to the server-room list on Oct 30 by Ana".

### 2️⃣ IAM & admin console
- **What it is:** The page that shows **who currently has which role**. No history.
- **Analogy:** 📋 Today's **access list** on the door. It doesn't show when names were added.

### 3️⃣ Cloud Monitoring (formerly Stackdriver Monitoring)
- **What it is:** **Metrics and charts** (CPU, latency, errors). Not a record of who changed permissions.
- **Analogy:** 📈 The building's **electricity meter**.

### 4️⃣ Cloud Logging (formerly Stackdriver Logging)
- **What it is:** The service that stores and searches logs, including audit logs. The **Logs Explorer** is its console page.

### 🔗 How they fit together
```
 "who has Spanner roles NOW?"   → IAM & admin page
 "WHEN were they added?"        → Logging → Admin Activity → filter SetIamPolicy + Spanner ✅
 "how busy is Spanner?"         → Monitoring
```

---

## 🌍 Real-World Scenario

A security team spots an unexpected user with Spanner admin rights. They need to know **when** that happened and **who** did it. The engineer opens **Logs Explorer**, filters Admin Activity logs for Spanner `SetIamPolicy` calls, and finds the exact change and time.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Open the Cloud Spanner console to review configurations.

**Wrong words:**
- ❌ "**review configurations**": the Spanner console shows instances and databases as they are now. It doesn't show when IAM roles were granted.

📌 **When to use it:** Use it to see or change Spanner instances, databases and their settings.
🏢 **Office example:** Looking at the server room's equipment to find out when someone got a key.

### ❌ B
> **B.** Open the IAM & admin console to review IAM policies for Cloud Spanner roles.

**Wrong words:**
- ✔️ It shows **who** has Spanner roles.
- ❌ "**review IAM policies**": the policy is a **current snapshot**, with **no dates**. It can't tell you **when** users were added.

📌 **When to use it:** Use it when you need to know who has which access right now.
🏢 **Office example:** Reading today's door access list, which doesn't say when each name was added.

### ❌ C
> **C.** Go to the Stackdriver Monitoring console and review information for Cloud Spanner.

**Wrong words:**
- ❌ "**Stackdriver Monitoring**": Monitoring shows **performance metrics** (CPU, latency), not permission changes.

📌 **When to use it:** Use Monitoring to check how busy or slow Spanner is.
🏢 **Office example:** Checking the electricity meter to find out who got a key.

### ✅ D
> **D.** Go to the Stackdriver Logging console, review admin activity logs, and filter them for Cloud Spanner IAM roles.

**Why it's correct:**
- ✔️ "**review admin activity logs**" matches "**users were added to … IAM roles**": adding someone to a role is an IAM policy change, recorded in Admin Activity logs.
- ✔️ "**Stackdriver Logging console**" matches "**find out when**": every log entry has a timestamp and who made the change.
- ✔️ "**filter them for Cloud Spanner IAM roles**" matches "**Cloud Spanner Identity Access Management (IAM) roles**": you see only Spanner role changes.

📌 **When to use it:** Use it when you need to know when a permission was given, and by whom.
🏢 **Office example:** Checking the logbook for "Ben added to the server-room list on Oct 30 by Ana".

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's orders database runs on Spanner. A new name shows up with `roles/spanner.databaseAdmin`.

Logs Explorer filter:
```
logName="projects/shopnow-prod/logs/cloudaudit.googleapis.com%2Factivity"
protoPayload.methodName:"SetIamPolicy"
protoPayload.serviceName="spanner.googleapis.com"
```
Result: `ana@shopnow.com added user:temp-dev@shopnow.com to roles/spanner.databaseAdmin · 2026-10-30 14:02`.

---

## 🧠 Key Takeaways / Memory Tips

- **"When was X changed / added?" → Admin Activity audit logs** in Cloud Logging.
- **IAM page = who has access now** (no dates). **Monitoring = metrics.**
  🧠 *"**When? Logs. Who now? IAM.**"*
- Related: **Q086** (service account created), **Q034** (who has which role), **Q067** (Spanner monitoring viewer).

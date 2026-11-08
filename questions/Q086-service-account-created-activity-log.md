# Q086: When Was a Service Account Created? (Activity Log, Configuration Category)

**Topic:** Logging (Activity log / Admin Activity audit logs vs Data Access logs, resource type filter)

## ❓ Question
> You need to verify that a Google Cloud Platform service account was created at a particular time. What should you do?
>
> **A.** Filter the Activity log to view the Configuration category. Filter the Resource type to Service Account.
>
> **B.** Filter the Activity log to view the Configuration category. Filter the Resource type to Google Project.
>
> **C.** Filter the Activity log to view the Data Access category. Filter the Resource type to Service Account.
>
> **D.** Filter the Activity log to view the Data Access category. Filter the Resource type to Google Project.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You need to confirm when a service account was created.
- **What you must achieve:** Find its creation time.
- **The limits:** None stated.
- **What they're really asking:** Where do you look for the record of the service account being created?

**Clues in the question:**
- "**service account was created**": creating something is a **configuration change** (Admin Activity), not reading data.
- "**service account**": filter the **resource type** to **Service Account**, so you only see service account events.

**Exam topic:** Logging / audit logs.

---

## 📚 Key Terms Explained

### 1️⃣ Activity log (project Activity page)
- **What it is:** A **page in the Cloud console (Home → Activity)** that lists who did what in the project, based on audit logs. You can filter it by **category** and **resource type**.
- **Looks like:** `ana@shopnow.com created service account checkout-sa@shopnow-prod.iam.gserviceaccount.com · Oct 31, 10:42`
- **Not to be confused with:** application logs (what your app prints).
- **Analogy:** 📓 The **building's front-desk logbook**: who came in, what they changed, and when.

### 2️⃣ Configuration category (Admin Activity) 🔑
- **What it is:** The category for **changes to settings and resources**: create, delete, update, set IAM policy. These logs are **always on and free**.
- **Looks like:** `google.iam.admin.v1.CreateServiceAccount`
- **Not to be confused with:** Data Access.
- **Analogy:** 🔧 Logbook entries like "**new desk installed**" or "**lock changed**".

### 3️⃣ Data Access category
- **What it is:** Logs of **reading or writing user data** (e.g., reading a file in a bucket, querying a table). Mostly **off by default**, because they can be huge.
- **Not to be confused with:** Configuration. Creating a service account isn't "data access".
- **Analogy:** 📄 Logbook entries like "**someone opened file #42**".

### 4️⃣ Resource type
- **What it is:** A **filter for which kind of thing** the log entry is about: Service Account, GCE VM Instance, GCS Bucket, Project, and so on.
- **Looks like:** `resource.type="service_account"`
- **Not to be confused with:** the project. Filtering on "Project" shows project-level changes, not service account ones.

### 🔗 How they fit together
```
 Activity log
   ├── Category: Configuration (Admin Activity) ← create / delete / change ✅
   │      └── Resource type: Service Account    ← CreateServiceAccount event ✅
   └── Category: Data Access                   ← reading/writing data ❌
```

---

## 🌍 Real-World Scenario

During a security review, someone asks: "Was `backup-sa` created before or after the incident?" The engineer opens the **Activity** page, picks the **Configuration** category and the **Service Account** resource type, and finds the creation event with its exact time and who created it.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Filter the Activity log to view the Configuration category. Filter the Resource type to Service Account.

**Why it's correct:**
- ✔️ "**Configuration category**" matches "**was created**": creating a resource is a configuration (admin) change.
- ✔️ "**Resource type to Service Account**" matches "**a Google Cloud Platform service account**": the filter shows only events about service accounts.
- ✔️ "**Filter the Activity log**" matches "**at a particular time**": each entry shows the exact time and who did it.

📌 **When to use it:** Use it when you need to know when something was set up or changed, and by whom.
🏢 **Office example:** Checking the front-desk logbook for "new employee badge created" to see the exact date.

### ❌ B
> **B.** Filter the Activity log to view the Configuration category. Filter the Resource type to Google Project.

**Wrong words:**
- ✔️ "Configuration category" is right.
- ❌ "**Resource type to Google Project**": that shows project-level changes (like project settings), not the service account's creation.

📌 **When to use it:** Use it when you want to see changes to the project itself, like project settings or permissions.
🏢 **Office example:** Reading logbook entries about the building, when you wanted the entry about one employee badge.

### ❌ C
> **C.** Filter the Activity log to view the Data Access category. Filter the Resource type to Service Account.

**Wrong words:**
- ❌ "**Data Access category**": creating a service account isn't reading or writing data, so the event isn't there. Data Access logs are also mostly turned off by default.
- ✔️ "Resource type to Service Account" is right.

📌 **When to use it:** Use Data Access logs when you need to know who **read or changed data**, like files or table rows.
🏢 **Office example:** Checking the "who opened which file" log to find out when a badge was made.

### ❌ D
> **D.** Filter the Activity log to view the Data Access category. Filter the Resource type to Google Project.

**Wrong words:**
- ❌ "**Data Access category**": wrong category (see C).
- ❌ "**Resource type to Google Project**": wrong resource type (see B).

📌 **When to use it:** **Never use this** to find when something was created. Use A.
🏢 **Office example:** Looking in the wrong logbook, on the wrong page.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's security team wants to know when `checkout-sa` was created.

Console: **Home → Activity → Categories: Configuration → Resource type: Service Account**.

Or in Logs Explorer:
```
logName="projects/shopnow-prod/logs/cloudaudit.googleapis.com%2Factivity"
resource.type="service_account"
protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"
```
Result: `ana@shopnow.com created checkout-sa · 2026-03-14 09:12 UTC`.

---

## 🧠 Key Takeaways / Memory Tips

- **Created / deleted / changed → Configuration (Admin Activity).** Always on, free.
- **Read / wrote data → Data Access.** Mostly off by default.
- Filter the **resource type** to the thing you care about.
  🧠 *"**Made it? Configuration. Read it? Data Access.**"*
- Related: **Q061** (keep audit logs 3 years), **Q025** (Data Access logs for auditors).

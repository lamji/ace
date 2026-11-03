# Q117: Did a Terminated Employee Read Sensitive Data? (Data Access Audit Logs by User Email)

**Topic:** Logging (Data Access vs Admin Activity vs System Event logs, principal)

## ❓ Question
> An employee was terminated, but their access to Google Cloud was not removed until 2 weeks later. You need to find out if this employee accessed any sensitive customer information after their termination. What should you do?
>
> **A.** View System Event Logs in Cloud Logging. Search for the user's email as the principal.
>
> **B.** View System Event Logs in Cloud Logging. Search for the service account associated with the user.
>
> **C.** View Data Access audit logs in Cloud Logging. Search for the user's email as the principal.
>
> **D.** View the Admin Activity log in Cloud Logging. Search for the service account associated with the user.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** A fired employee kept access for 2 weeks. Did they **read customer data**? Which logs, and what do you search for?

**Clues in the question:**
- "**accessed any sensitive customer information**": **reading data** → **Data Access** audit logs.
- "**this employee**": search by **their email** as the principal (the person who acted), not a service account.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Data Access audit logs 🔑
- **What it is:** Logs of **who read or wrote user data**: table reads, object downloads, and so on. Must be **enabled** for most services (BigQuery's are on by default).
- **Looks like:** `logName:"data_access" protoPayload.authenticationInfo.principalEmail="ex.employee@shopnow.com"`
- **Not to be confused with:** Admin Activity (config changes) or System Event (Google's own actions).
- **Analogy:** 📄 The "who opened which customer file" logbook.
- **In the online store:** Who queried the customers table.

### 2. Principal
- **What it is:** The **identity that made the request**: a user email or a service account.
- **Looks like:** `principalEmail: ex.employee@shopnow.com`
- **Not to be confused with:** a resource.
- **Analogy:** 🪪 The name on the badge that was swiped.
- **In the online store:** The analyst who ran the query.

### 3. System Event logs
- **What it is:** Logs of **actions Google systems take** on your resources (like live-migrating a VM). No user actions.
- **Looks like:** `methodName: compute.instances.migrateOnHostMaintenance`
- **Not to be confused with:** user activity.
- **Analogy:** 🔧 The building's automatic maintenance log.
- **In the online store:** VM host maintenance events.

### 🔗 How they fit together
```
 Was customer data READ by ex.employee@? → Data Access logs + principalEmail ✅
 Did they CHANGE config?                 → Admin Activity logs
 What did GOOGLE's systems do?           → System Event logs
```

---

## 🌍 Real-World Scenario

HR reports that a terminated analyst's account wasn't disabled for 2 weeks. Security filters **Data Access** logs by the analyst's email for those dates and finds two BigQuery queries on `customers`. Legal follows up.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** View System Event Logs in Cloud Logging. Search for the user's email as the principal.

**Wrong words:**
- ❌ "**System Event Logs**": these record Google's automatic actions, not users reading data.
- ✔️ "user's email as the principal" is the right filter.

📌 **When to use it:** Use System Event logs to see what Google did automatically, like host maintenance.
🏢 **Office example:** Checking the building's maintenance log to see who read a customer file.

### ❌ B
> **B.** View System Event Logs in Cloud Logging. Search for the service account associated with the user.

**Wrong words:**
- ❌ "**System Event Logs**": wrong log type (see A).
- ❌ "**service account associated with the user**": users act with their own email. There's no personal service account to search.

📌 **When to use it:** **Never use this** for user data access.
🏢 **Office example:** The maintenance log, searched for a robot's name, to find what a person read.

### ✅ C
> **C.** View Data Access audit logs in Cloud Logging. Search for the user's email as the principal.

**Why it's correct:**
- ✔️ "**Data Access audit logs**" matches "**accessed any sensitive customer information**": these logs record who read data.
- ✔️ "**Search for the user's email as the principal**" matches "**this employee**": you filter on the person who made the requests.

📌 **When to use it:** Use it when you need to know whether a specific person opened certain records.
🏢 **Office example:** Checking the "who opened which file" logbook for the former employee's name.

### ❌ D
> **D.** View the Admin Activity log in Cloud Logging. Search for the service account associated with the user.

**Wrong words:**
- ❌ "**Admin Activity log**": it records configuration changes, not reading data.
- ❌ "**service account associated with the user**": wrong principal.

📌 **When to use it:** Use Admin Activity logs to find who changed settings or permissions.
🏢 **Office example:** Checking the "who changed the locks" log to find who read a file.

---

## 🛒 E-Commerce Full-Stack Example

```
logName:"cloudaudit.googleapis.com%2Fdata_access"
protoPayload.authenticationInfo.principalEmail="ex.analyst@shopnow.com"
timestamp>="2026-10-01T00:00:00Z" timestamp<="2026-10-15T00:00:00Z"
```
Result: 2 BigQuery jobs that read `shopnow-crm.customers` on Oct 6.

---

## 🧠 Key Takeaways / Memory Tips

- **Who READ data → Data Access logs**, filter by the user's email (principal).
- Admin Activity = changes. System Event = Google's actions.
  🧠 *"**Read data? Data Access. Search the person's email.**"*
- Related: **Q086** (Configuration vs Data Access), **Q113** (Private Logs Viewer), **Q095** (Admin Activity).

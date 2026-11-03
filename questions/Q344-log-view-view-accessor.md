# Q344: Team Sees All Frontend Logs and Only Error Logs From Backend in a Central Bucket (Log View + logging.viewAccessor)

**Topic:** Logging (log views, least privilege)

## ❓ Question
> You are managing logging for your organization by aggregating logs into a centralized Google Cloud project. The aggregated logs come from two source projects: one for a frontend application and one for a backend application. You need to grant the frontend development team access to view all logs originating from the frontend project and only error-level logs from the backend project. The team must not be able to view any other logs. You want to follow the principle of least privilege and develop a cost-efficient solution. What should you do?
>
> **A.** • In the centralized logging project, craft a query that combines all logs from the frontend project and error-level logs from the backend project, and grant the logging.viewer IAM role. • Save and share this query with the frontend team for them to use in the Logs Explorer. • Request the frontend team not to use any other query.
>
> **B.** • Create two separate log sinks in the centralized project. • Configure one sink to route all frontend logs to a new, dedicated Cloud Storage bucket. • Configure a second sink to route only the error-level logs from the backend project to that same bucket. • Grant the frontend team read-only access to this bucket.
>
> **C.** • Grant the frontend team the logging.viewer IAM role on both the frontend project and the backend project. • Instruct the developers to use a specific filter in the Logs Explorer to find the logs they need.
>
> **D.** • In the centralized logging project, create a log view on the bucket that contains the aggregated logs. • Filter the view to include all logs from the frontend project and only logs with a severity level of ERROR from the backend project. • Grant the frontend team the logging.viewAccessor IAM role on this specific view.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Show the frontend team **only certain logs** from a central bucket; least privilege, cheap.

**Clues in the question:**
- "**must not be able to view any other logs**" → **log view** with a filter + **`roles/logging.viewAccessor`** on that view.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Log view 🔑
- **What it is:** A filtered window into a log bucket; IAM can grant access to just that view.
- **Looks like:** filter: `source("projects/frontend") OR (source("projects/backend") AND severity=ERROR)`
- **Not to be confused with:** a saved query (no access control).
- **Analogy:** 🪟 A window showing only part of the room.
- **In the online store:** ShopNow frontend team view.

### 2. roles/logging.viewAccessor
- **What it is:** Lets a principal read logs only through the views it's granted on.
- **Looks like:** `gcloud logging views add-iam-policy-binding frontend-view --bucket=central --location=global --member=group:fe@ --role=roles/logging.viewAccessor`
- **Not to be confused with:** logging.viewer (all logs).
- **Analogy:** 🗝️ A key to that window only.
- **In the online store:** —

### 🔗 How they fit together
```
 central bucket → log view (frontend all + backend ERROR) → viewAccessor ✅
```

---

## 🌍 Real-World Scenario

The central logging team creates a **log view** and grants the frontend group **viewAccessor** on it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** • In the centralized logging project, craft a query that combines all logs from the frontend project and error-level logs from the backend project, and grant the logging.viewer IAM role. • Save and share this query with the frontend team for them to use in the Logs Explorer. • Request the frontend team not to use any other query.

**Wrong words:**
- ❌ "**logging.viewer**" + "**Request the frontend team not to use any other query**": they can see everything; relying on a request.

📌 **When to use it:** **Never use this** for least privilege.
🏢 **Office example:** Asking people not to read other files in an open cabinet.

### ❌ B
> **B.** • Create two separate log sinks in the centralized project. • Configure one sink to route all frontend logs to a new, dedicated Cloud Storage bucket. • Configure a second sink to route only the error-level logs from the backend project to that same bucket. • Grant the frontend team read-only access to this bucket.

**Wrong words:**
- ❌ "**two separate log sinks … Cloud Storage bucket**": duplicates logs (extra cost) and loses Logs Explorer features.

📌 **When to use it:** Use sinks to archive logs.
🏢 **Office example:** Photocopying files into a new cabinet.

### ❌ C
> **C.** • Grant the frontend team the logging.viewer IAM role on both the frontend project and the backend project. • Instruct the developers to use a specific filter in the Logs Explorer to find the logs they need.

**Wrong words:**
- ❌ "**logging.viewer … on both**" projects: sees all backend logs.

📌 **When to use it:** Use it when the team may read everything.
🏢 **Office example:** A key to both whole cabinets.

### ✅ D
> **D.** • In the centralized logging project, create a log view on the bucket that contains the aggregated logs. • Filter the view to include all logs from the frontend project and only logs with a severity level of ERROR from the backend project. • Grant the frontend team the logging.viewAccessor IAM role on this specific view.

**Why it's correct:**
- ✔️ "**log view … all logs from the frontend project and only … ERROR from the backend project**" matches "**view all logs originating from the frontend project and only error-level logs from the backend**".
- ✔️ "**logging.viewAccessor … on this specific view**" matches "**must not be able to view any other logs**" + "**least privilege**" + "**cost-efficient**" (no copies).

📌 **When to use it:** Use it when a team should see only some records in a shared logbook.
🏢 **Office example:** A window into the record room that only shows the papers that team may read.

---

## 🛒 E-Commerce Full-Stack Example

View `fe-team` on `central-logs`; `group:frontend@shopnow.com` → `roles/logging.viewAccessor`.

---

## 🧠 Key Takeaways / Memory Tips

- **Restrict who sees which logs → log view + logging.viewAccessor.**
  🧠 *"**View filters, viewAccessor unlocks.**"*
- Related: **Q300**, **Q280**.

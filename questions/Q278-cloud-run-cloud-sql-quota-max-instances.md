# Q278: Cloud SQL API Quota Errors During Cloud Run Morning Spikes (Lower the Maximum Number of Cloud Run Instances)

**Topic:** Cloud Run (max instances to protect backends)

## ❓ Question
> Your web application is hosted on Cloud Run and needs to query a Cloud SQL database. Every morning during a traffic spike, you notice API quota errors in Cloud SQL logs. The project has already reached the maximum API quota. You want to make a configuration change to mitigate the issue. What should you do?
>
> **A.** Modify the minimum number of Cloud Run instances.
>
> **B.** Use traffic splitting.
>
> **C.** Modify the maximum number of Cloud Run instances.
>
> **D.** Set a minimum concurrent requests environment variable for the application.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A Cloud Run web app queries a Cloud SQL database. Each morning's traffic spike causes API quota errors in Cloud SQL logs, and the project's API quota is already at its maximum.
- **What you must achieve:** Stop the errors with a configuration change.
- **The limits:** The quota can't be raised.
- **What they're really asking:** What Cloud Run setting reduces the calls hitting the quota?

**Clues in the question:**
- Each new Cloud Run instance opens connections through the Cloud SQL connector, which calls the Cloud SQL Admin API.
- "**reached the maximum API quota**" → **cap** Cloud Run with **max instances**.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Max instances 🔑
- **What it is:** The upper limit of container instances Cloud Run will start; protects downstream services.
- **Looks like:** `gcloud run services update app --max-instances=20`
- **Not to be confused with:** min instances.
- **Analogy:** 🚧 A cap on how many staff can enter the records room.
- **In the online store:** Protect orders DB.

### 🔗 How they fit together
```
 spike → Cloud Run 200 instances → Cloud SQL API quota ✗
 max-instances=20 → fewer connections → within quota ✅
```

---

## 🌍 Real-World Scenario

A store's morning spike starts hundreds of Cloud Run instances, each hitting the Cloud SQL Admin API. The team sets **max instances** so the API stays within quota.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Modify the minimum number of Cloud Run instances.

**Wrong words:**
- ❌ "**minimum number of Cloud Run instances**": keeps instances warm; doesn't limit the spike.

📌 **When to use it:** Use min instances to avoid cold starts.
🏢 **Office example:** Keeping more staff on duty doesn't limit the crowd.

### ❌ B
> **B.** Use traffic splitting.

**Wrong words:**
- ❌ "**traffic splitting**": splits traffic between revisions; total instances stay the same.

📌 **When to use it:** Use it for canary releases.
🏢 **Office example:** Splitting the crowd between two doors into the same room.

### ✅ C
> **C.** Modify the maximum number of Cloud Run instances.

**Why it's correct:**
- ✔️ "**Modify the maximum number of Cloud Run instances**" matches "**API quota errors**" during a "**traffic spike**": fewer instances means fewer Cloud SQL API calls and connections.
- ✔️ It's a configuration change, which matches "**make a configuration change**".

📌 **When to use it:** Use it when a sudden rush overwhelms something behind your service.
🏢 **Office example:** Limiting how many clerks can go into the records room at once.

### ❌ D
> **D.** Set a minimum concurrent requests environment variable for the application.

**Wrong words:**
- ❌ "**minimum concurrent requests environment variable**": not a real Cloud Run setting (concurrency is a service setting, not an env var).

📌 **When to use it:** **Not a real fix.**
🏢 **Office example:** A sign that nobody reads.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run services update storefront --max-instances=40 --concurrency=80`

---

## 🧠 Key Takeaways / Memory Tips

- **Cloud Run overwhelming a backend/quota → set max instances.**
  🧠 *"**Cap the crowd to protect the database.**"*
- Related: **Q212**, **Q163**.

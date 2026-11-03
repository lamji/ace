# Q130: App Engine App Reads BigQuery in Another Team's Project (Other Team Grants Data Viewer to Your Service Account)

**Topic:** IAM (cross-project access, App Engine default service account, BigQuery roles)

## ❓ Question
> You manage an App Engine Service that aggregates and visualizes data from BigQuery. The application is deployed with the default App Engine Service account. The data that needs to be visualized resides in a different project managed by another team. You do not have access to this project, but you want your application to be able to read data from the BigQuery dataset. What should you do?
>
> **A.** Ask the other team to grant your default App Engine Service account the role of BigQuery Job User.
>
> **B.** Ask the other team to grant your default App Engine Service account the role of BigQuery Data Viewer.
>
> **C.** In Cloud IAM of your project, ensure that the default App Engine service account has the role of BigQuery Data Viewer.
>
> **D.** In Cloud IAM of your project, grant a newly created service account from the other team the role of BigQuery Job User in your project.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your App Engine app (running as its default service account) must **read** a BigQuery dataset in **another team's project** that you can't manage.

**Clues in the question:**
- "**read data from the BigQuery dataset**" → **BigQuery Data Viewer**.
- "**resides in a different project … You do not have access**": the role must be granted **in their project**, so you **ask the other team**.
- "**default App Engine Service account**": that's the member to grant.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. App Engine default service account
- **What it is:** The identity App Engine apps run as by default.
- **Looks like:** `shopnow-dash@appspot.gserviceaccount.com`
- **Not to be confused with:** your personal account.
- **Analogy:** 🤖 The app's robot badge.
- **In the online store:** The dashboard app calls BigQuery as this account.

### 2. BigQuery Data Viewer vs Job User 🔑
- **What it is:** **Data Viewer** = read tables and data. **Job User** = run query jobs (in the project where the job runs). Reading another project's data needs **Data Viewer on that data**.
- **Looks like:** `roles/bigquery.dataViewer` / `roles/bigquery.jobUser`
- **Not to be confused with:** each other.
- **Analogy:** 👀 A pass to read the archive vs 🧾 permission to use the reading room.
- **In the online store:** The dashboard reads `crm.segments`.

### 3. Cross-project grant (review from Q116)
- **What it is:** Roles are granted **on the project or dataset that holds the data**, with the other project's service account as the member.
- **Looks like:** `bq add-iam-policy-binding --member=serviceAccount:shopnow-dash@appspot.gserviceaccount.com --role=roles/bigquery.dataViewer crm-proj:segments`
- **Not to be confused with:** granting roles in your own project.
- **Analogy:** 🪪 HQ adds your robot to its archive list.
- **In the online store:** The CRM team grants access to the dashboard.

### 🔗 How they fit together
```
 your project (App Engine)                      other team's project
   app runs as shopnow-dash@appspot ──────────► BigQuery dataset segments
                                                IAM (set by THEM): dataViewer → shopnow-dash@appspot ✅
```

---

## 🌍 Real-World Scenario

A dashboard app on App Engine needs sales data owned by the finance team in another project. The app team asks finance to grant the app's **default service account** the **BigQuery Data Viewer** role on their dataset. The app can now read the data, and nothing else.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ask the other team to grant your default App Engine Service account the role of BigQuery Job User.

**Wrong words:**
- ✔️ "Ask the other team" and "your default App Engine Service account" are right.
- ❌ "**BigQuery Job User**": lets you run query jobs, but **not read the data** in their tables.

📌 **When to use it:** Use Job User when an account needs to run queries in a project.
🏢 **Office example:** Getting access to the reading room, but no permission to open the archive boxes.

### ✅ B
> **B.** Ask the other team to grant your default App Engine Service account the role of BigQuery Data Viewer.

**Why it's correct:**
- ✔️ "**Ask the other team to grant**" matches "**different project managed by another team. You do not have access**": only they can grant roles in their project.
- ✔️ "**your default App Engine Service account**" matches "**deployed with the default App Engine Service account**": the identity the app actually uses.
- ✔️ "**BigQuery Data Viewer**" matches "**read data from the BigQuery dataset**": read-only access to the data.

📌 **When to use it:** Use it when your program needs to read another department's records, and that department controls them.
🏢 **Office example:** Asking HQ's archive team to add your office robot to their read-only list.

### ❌ C
> **C.** In Cloud IAM of your project, ensure that the default App Engine service account has the role of BigQuery Data Viewer.

**Wrong words:**
- ❌ "**In Cloud IAM of your project**": a role in **your** project doesn't open data that lives in **their** project.

📌 **When to use it:** Use it when the data is in your own project.
🏢 **Office example:** Updating your own office's list to open HQ's archive.

### ❌ D
> **D.** In Cloud IAM of your project, grant a newly created service account from the other team the role of BigQuery Job User in your project.

**Wrong words:**
- ❌ "**grant a newly created service account from the other team**": your app doesn't run as that account.
- ❌ "**Job User in your project**": it doesn't give access to their data.

📌 **When to use it:** **Never use this.** Use B.
🏢 **Office example:** Giving a stranger's robot a pass to your own reading room.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `shopnow-dash` App Engine app needs `shopnow-crm.segments`. The CRM team runs:
```bash
bq add-iam-policy-binding \
  --member=serviceAccount:shopnow-dash@appspot.gserviceaccount.com \
  --role=roles/bigquery.dataViewer shopnow-crm:segments
```
The dashboard runs its queries (as Job User in its own project) and reads the CRM tables.

---

## 🧠 Key Takeaways / Memory Tips

- **Read another project's BigQuery data → that project grants Data Viewer to your service account.**
- Job User = run queries; Data Viewer = read data.
  🧠 *"**Their data, their grant: Data Viewer for your service account.**"*
- Related: **Q116** (cross-project service account), **Q071** (node SA in image project).

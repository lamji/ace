# Q116: VMs in One Project Need BigQuery Data in Another (Grant the Service Account Roles in the Data Project)

**Topic:** IAM (cross-project service account access, BigQuery roles)

## ❓ Question
> You are configuring service accounts for an application that spans multiple projects. Virtual machines (VMs) running in the web-applications project need access to BigQuery datasets in crm-databases-proj. You want to follow Google-recommended practices to give access to the service account in the web-applications project. What should you do?
>
> **A.** Give "project owner" for web-applications appropriate roles to crm-databases-proj.
>
> **B.** Give "project owner" role to crm-databases-proj and the web-applications project.
>
> **C.** Give "project owner" role to crm-databases-proj and bigquery.dataViewer role to web-applications.
>
> **D.** Give bigquery.dataViewer role to crm-databases-proj and appropriate roles to web-applications.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** The wording is garbled. Option A means: give **the web-applications service account** the **appropriate roles** (e.g. BigQuery Data Viewer) **in crm-databases-proj**. That's the accepted (most voted) answer.

---

## 📖 What the Question Is Asking

**In plain words:** VMs in `web-applications` use a service account. That account must read BigQuery data in `crm-databases-proj`. Where do you grant the role?

**Clues in the question:**
- "**access to BigQuery datasets in crm-databases-proj**": the permission must be granted **where the data is**, in crm-databases-proj.
- "**give access to the service account in the web-applications project**": the **member** is that service account.
- "**Google-recommended practices**": least privilege, so **appropriate** roles, never Project Owner.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Cross-project access 🔑
- **What it is:** A service account from project A can be **granted roles in project B**. Roles are always granted **on the resource's project**, with the service account as the member.
- **Looks like:** `gcloud projects add-iam-policy-binding crm-databases-proj --member=serviceAccount:web-sa@web-applications.iam.gserviceaccount.com --role=roles/bigquery.dataViewer`
- **Not to be confused with:** giving roles in the service account's own project.
- **Analogy:** 🪪 A branch employee gets added to **HQ's archive access list**.
- **In the online store:** The storefront's service account reads the CRM dataset.

### 2. roles/bigquery.dataViewer
- **What it is:** Read tables and data in BigQuery datasets.
- **Looks like:** `roles/bigquery.dataViewer`
- **Not to be confused with:** dataEditor (can change data).
- **Analogy:** 👀 Read-only archive pass.
- **In the online store:** Read customer segments.

### 3. Project Owner
- **What it is:** Full control of a project. Never the least-privilege choice.
- **Looks like:** `roles/owner`
- **Not to be confused with:** an appropriate role.
- **Analogy:** 🔑 The master key.
- **In the online store:** Never given to an app's service account.

### 🔗 How they fit together
```
 web-applications project                 crm-databases-proj
   VM ── runs as web-sa@web-applications ──► BigQuery dataset crm
                                            IAM here: web-sa → bigquery.dataViewer (+ jobUser where queries run) ✅
```

---

## 🌍 Real-World Scenario

A web app in one project must read customer segments from the CRM team's project. The CRM admin grants the web app's **service account** the **BigQuery Data Viewer** role in **crm-databases-proj**. The web project's own settings don't change.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Give "project owner" for web-applications appropriate roles to crm-databases-proj.

**Why it's correct:**
- ✔️ "**for web-applications**" (its service account) matches "**give access to the service account in the web-applications project**": the member is the web app's service account.
- ✔️ "**appropriate roles to crm-databases-proj**" matches "**need access to BigQuery datasets in crm-databases-proj**": the role is granted where the data lives.
- ✔️ "**appropriate roles**" matches "**Google-recommended practices**": least privilege, such as BigQuery Data Viewer.

📌 **When to use it:** Use it when a program in one department needs to read records kept by another department.
🏢 **Office example:** Adding the branch office's robot badge to HQ's archive read-only list.

### ❌ B
> **B.** Give "project owner" role to crm-databases-proj and the web-applications project.

**Wrong words:**
- ❌ "**project owner role to crm-databases-proj and the web-applications project**": full control of both projects. Far beyond least privilege.

📌 **When to use it:** **Never use this.** Grant appropriate roles (A).
🏢 **Office example:** Giving the robot master keys to both buildings to read one folder.

### ❌ C
> **C.** Give "project owner" role to crm-databases-proj and bigquery.dataViewer role to web-applications.

**Wrong words:**
- ❌ "**project owner role to crm-databases-proj**": far too powerful.
- ❌ "**bigquery.dataViewer role to web-applications**": the data isn't in web-applications, so this role there doesn't help.

📌 **When to use it:** **Never use this.** Use A.
🏢 **Office example:** A master key to HQ, plus a reading pass for your own empty archive.

### ❌ D
> **D.** Give bigquery.dataViewer role to crm-databases-proj and appropriate roles to web-applications.

**Wrong words:**
- ❌ "**bigquery.dataViewer role to crm-databases-proj**": as written, it gives the role to the *project*, not to the service account, which makes no sense.
- ❌ "**appropriate roles to web-applications**": roles in the web project don't open the CRM data.

📌 **When to use it:** Grant roles in the web project when the app needs resources that live there.
🏢 **Office example:** Updating your own office's access list when the files are at HQ.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects add-iam-policy-binding shopnow-crm \
  --member=serviceAccount:storefront-sa@shopnow-web.iam.gserviceaccount.com \
  --role=roles/bigquery.dataViewer
gcloud projects add-iam-policy-binding shopnow-web \
  --member=serviceAccount:storefront-sa@shopnow-web.iam.gserviceaccount.com \
  --role=roles/bigquery.jobUser    # to run query jobs from the web project
```
The storefront's VMs now read `shopnow-crm.segments.vip_customers`.

---

## 🧠 Key Takeaways / Memory Tips

- **Grant roles where the resource lives; the member is the other project's service account.**
- Never Project Owner for apps.
  🧠 *"**Grant it where the data lives.**"*
- Related: **Q071** (node SA reads images in another project), **Q130** (App Engine SA reads BigQuery in another project).

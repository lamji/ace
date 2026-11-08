# Q297: VM App Needs Short-Lived Credentials and Access to One BigQuery Dataset (Custom SA, Data Viewer on the Dataset)

**Topic:** IAM (attached service accounts, resource-level roles)

## ❓ Question
> You have an application running inside a Compute Engine instance. You want to provide the application with secure access to a BigQuery dataset. You must ensure that credentials are only valid for a short period of time, and your application will only have access to the intended BigQuery dataset. You want to follow Google-recommended practices and minimize your operational costs. What should you do?
>
> **A.** Attach a new service account to the instance every hour, and grant the service account the BigQuery Data Viewer IAM role on the project.
>
> **B.** Attach a custom service account to the instance, and grant the service account the BigQuery Data Viewer IAM role on the dataset.
>
> **C.** Attach a new service account to the instance every hour, and grant the service account the BigQuery Data Viewer IAM role on the dataset.
>
> **D.** Attach a custom service account to the instance, and grant the service account the BigQuery Data Viewer IAM role on the project.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs on a Compute Engine VM and needs to read one BigQuery dataset.
- **What you must achieve:** Give the app secure access to that dataset.
- **The limits:** Credentials must be short-lived, the app may reach only that dataset, follow recommended practice and keep costs low.
- **What they're really asking:** How do you give the VM's app short-lived access to only that one dataset?

**Clues in the question:**
- An **attached service account** gives the VM **short-lived access tokens** automatically (about 1 hour) from the metadata server — no rotation work.
- "**only have access to the intended BigQuery dataset**" → grant **on the dataset**, not the project.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Attached service account tokens 🔑
- **What it is:** Apps on a VM get OAuth tokens from the metadata server; they expire after about an hour and refresh automatically.
- **Looks like:** `curl -H 'Metadata-Flavor: Google' http://metadata/computeMetadata/v1/instance/service-accounts/default/token`
- **Not to be confused with:** keys.
- **Analogy:** 🎫 Day passes printed automatically each morning.
- **In the online store:** ShopNow report VM.

### 🔗 How they fit together
```
 VM (custom SA) → short-lived tokens ✅ → BigQuery Data Viewer on dataset only ✅
```

---

## 🌍 Real-World Scenario

A reporting VM runs as `reports-sa`, which has **Data Viewer on one dataset**. Its tokens expire hourly and refresh automatically.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Attach a new service account to the instance every hour, and grant the service account the BigQuery Data Viewer IAM role on the project.

**Wrong words:**
- ❌ "**new service account … every hour**": needless operational work (tokens are already short-lived).
- ❌ "**on the project**": access to every dataset.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Issuing a new employee badge every hour.

### ✅ B
> **B.** Attach a custom service account to the instance, and grant the service account the BigQuery Data Viewer IAM role on the dataset.

**Why it's correct:**
- ✔️ "**Attach a custom service account to the instance**" matches "**credentials are only valid for a short period of time**": attached SAs use short-lived tokens.
- ✔️ "**BigQuery Data Viewer … on the dataset**" matches "**only have access to the intended BigQuery dataset**".

📌 **When to use it:** Use it when a program on a machine should read one specific set of records with no secrets to manage.
🏢 **Office example:** Giving the robot a badge that only opens one cabinet, with a fresh day pass printed automatically.

### ❌ C
> **C.** Attach a new service account to the instance every hour, and grant the service account the BigQuery Data Viewer IAM role on the dataset.

**Wrong words:**
- ✔️ "on the dataset" is right.
- ❌ "**new service account … every hour**": unnecessary work.

📌 **When to use it:** **Avoid** — tokens already expire.
🏢 **Office example:** Changing badges hourly for no reason.

### ❌ D
> **D.** Attach a custom service account to the instance, and grant the service account the BigQuery Data Viewer IAM role on the project.

**Wrong words:**
- ✔️ Custom SA is right.
- ❌ "**on the project**": access to all datasets.

📌 **When to use it:** Use project-level only if every dataset is needed.
🏢 **Office example:** A badge that opens every cabinet.

---

## 🛒 E-Commerce Full-Stack Example

`bq add-iam-policy-binding --member=serviceAccount:reports-sa@shopnow-prod.iam.gserviceaccount.com --role=roles/bigquery.dataViewer shopnow-prod:sales`

---

## 🧠 Key Takeaways / Memory Tips

- **Attached SA = short-lived tokens. Least privilege = grant on the dataset.**
  🧠 *"**Attach once, grant narrowly.**"*
- Related: **Q134**, **Q183**.

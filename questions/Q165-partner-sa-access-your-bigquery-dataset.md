# Q165: Partner in Their Own Project Needs Your BigQuery Dataset (Their Service Account, Granted on Your Dataset)

**Topic:** IAM (cross-project / cross-organization access with service accounts)

## ❓ Question
> You are running a data warehouse on BigQuery. A partner company is offering a recommendation engine based on the data in your data warehouse. The partner company is also running their application on Google Cloud. They manage the resources in their own project, but they need access to the BigQuery dataset in your project. You want to provide the partner company with access to the dataset. What should you do?
>
> **A.** Create a Service Account in your own project, and grant this Service Account access to BigQuery in your project.
>
> **B.** Create a Service Account in your own project, and ask the partner to grant this Service Account access to BigQuery in their project.
>
> **C.** Ask the partner to create a Service Account in their project, and have them give the Service Account access to BigQuery in their project.
>
> **D.** Ask the partner to create a Service Account in their project, and grant their Service Account access to the BigQuery dataset in your project.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The partner's app (in **their** project) must read **your** dataset.

**Clues in the question:**
- "**They manage the resources in their own project**": their app runs as **their own service account**.
- "**need access to the BigQuery dataset in your project**": **you** grant that service account a role **on your dataset** (same pattern as Q116 and Q130).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Cross-project service account grant 🔑
- **What it is:** Their service account is a member in **your** IAM policy on the dataset.
- **Looks like:** `bq add-iam-policy-binding --member=serviceAccount:reco@partner-proj.iam.gserviceaccount.com --role=roles/bigquery.dataViewer shop-dw:sales`
- **Not to be confused with:** creating accounts for them.
- **Analogy:** 🪪 Adding the partner's robot badge to your archive list.
- **In the online store:** A recommendation partner reads sales.

### 2. Service account ownership
- **What it is:** Whoever owns the project owns the service account and its keys. Partners should use **their own** accounts, not keys from yours.
- **Looks like:** `…@partner-proj.iam.gserviceaccount.com`
- **Not to be confused with:** your accounts.
- **Analogy:** 🤖 Their robot, their badge.
- **In the online store:** Partner SA, not ShopNow SA.

### 🔗 How they fit together
```
 partner-proj: app runs as reco-sa@partner-proj ──read──► your project: dataset sales
                                                      IAM (you set): reco-sa → bigquery.dataViewer ✅
```

---

## 🌍 Real-World Scenario

A recommendation vendor runs in its own project. They create `reco-sa` and send you the email. You grant it **BigQuery Data Viewer on your dataset**. Their app reads your data, and you can revoke access anytime.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Service Account in your own project, and grant this Service Account access to BigQuery in your project.

**Wrong words:**
- ❌ "**Service Account in your own project**": the partner's app would need **your key**, and sharing keys is risky. They should use their own identity.

📌 **When to use it:** Use your own service accounts for your own apps.
🏢 **Office example:** Lending the partner your company robot's badge.

### ❌ B
> **B.** Create a Service Account in your own project, and ask the partner to grant this Service Account access to BigQuery in their project.

**Wrong words:**
- ❌ "**ask the partner to grant this Service Account access to BigQuery in their project**": the data is in **your** project, so a grant in theirs doesn't help.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Asking them to add your robot to their archive when the files are in yours.

### ❌ C
> **C.** Ask the partner to create a Service Account in their project, and have them give the Service Account access to BigQuery in their project.

**Wrong words:**
- ❌ "**access to BigQuery in their project**": wrong place. Your dataset is in your project.

📌 **When to use it:** Use it for access to their own data.
🏢 **Office example:** Giving their robot a pass to their own archive.

### ✅ D
> **D.** Ask the partner to create a Service Account in their project, and grant their Service Account access to the BigQuery dataset in your project.

**Why it's correct:**
- ✔️ "**Ask the partner to create a Service Account in their project**" matches "**They manage the resources in their own project**".
- ✔️ "**grant their Service Account access to the BigQuery dataset in your project**" matches "**need access to the BigQuery dataset in your project**".

📌 **When to use it:** Use it when an outside team's program needs to read your records.
🏢 **Office example:** Adding the partner's own robot badge to your archive's read-only list.

---

## 🛒 E-Commerce Full-Stack Example

```bash
bq add-iam-policy-binding --member=serviceAccount:reco-sa@partner-ai.iam.gserviceaccount.com \
  --role=roles/bigquery.dataViewer shopnow-dw:sales
```

---

## 🧠 Key Takeaways / Memory Tips

- **Outside app reads your data → their service account, granted on your resource.**
- Don't hand out your keys.
  🧠 *"**Their badge, your door list.**"*
- Related: **Q116**, **Q130**, **Q133**.

# Q365: All Company Employees Can Read a BigQuery Dataset (domain:terramearth.com Principal)

**Topic:** IAM (principals)

## ❓ Question
> Your company's Human Resources department publishes a BigQuery dataset with anonymized information about company sales and products. All employees in your company are managed in the terramearth.com Cloud Identity account and must be able to view this dataset as an authenticated user. You need to grant all employees in your company read-only access to this BigQuery dataset. What should you do?
>
> **A.** Grant the roles/bigquery.dataViewer role to the domain:terramearth.com principal on the dataset’s IAM policy.
>
> **B.** Grant the roles/bigquery.dataViewer role to the allUsers principal on the dataset’s IAM policy.
>
> **C.** Grant the roles/bigquery.dataViewer role to a new service account on the dataset’s IAM policy.
>
> **D.** Grant the roles/bigquery.dataViewer role to the allAuthenticatedUsers principal on the dataset’s IAM policy.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** HR publishes a BigQuery dataset with anonymized sales and product data. Every employee is in the terramearth.com Cloud Identity account.
- **What you must achieve:** Give all employees read-only access to the dataset.
- **The limits:** They must be signed in with their company accounts.
- **What they're really asking:** Which principal (who) should get the read role?

**Clues in the question:**
- "**All employees … in the terramearth.com Cloud Identity account**" → principal **`domain:terramearth.com`**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. domain: principal 🔑
- **What it is:** Represents every user in a Google Workspace / Cloud Identity domain.
- **Looks like:** `bq add-iam-policy-binding --member=domain:terramearth.com --role=roles/bigquery.dataViewer hr.sales_public`
- **Not to be confused with:** allAuthenticatedUsers (any Google account).
- **Analogy:** 🏢 'Everyone with a company badge.'
- **In the online store:** —

### 🔗 How they fit together
```
 domain:terramearth.com → dataViewer on dataset ✅
```

---

## 🌍 Real-World Scenario

HR shares an anonymized dataset with **`domain:terramearth.com`**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Grant the roles/bigquery.dataViewer role to the domain:terramearth.com principal on the dataset’s IAM policy.

**Why it's correct:**
- ✔️ "**domain:terramearth.com principal**" matches "**All employees … managed in the terramearth.com Cloud Identity account**".
- ✔️ "**roles/bigquery.dataViewer … on the dataset**" matches "**read-only access to this BigQuery dataset**".

📌 **When to use it:** Use it when everyone in your company should see something, and nobody outside.
🏢 **Office example:** A notice open to anyone with a company badge.

### ❌ B
> **B.** Grant the roles/bigquery.dataViewer role to the allUsers principal on the dataset’s IAM policy.

**Wrong words:**
- ❌ "**allUsers**": public internet, no login.

📌 **When to use it:** Use it for truly public data.
🏢 **Office example:** Posting it on the street.

### ❌ C
> **C.** Grant the roles/bigquery.dataViewer role to a new service account on the dataset’s IAM policy.

**Wrong words:**
- ❌ "**new service account**": employees aren't the SA.

📌 **When to use it:** Use SAs for apps.
🏢 **Office example:** Giving the badge to a robot.

### ❌ D
> **D.** Grant the roles/bigquery.dataViewer role to the allAuthenticatedUsers principal on the dataset’s IAM policy.

**Wrong words:**
- ❌ "**allAuthenticatedUsers**": any Google account worldwide.

📌 **When to use it:** **Avoid** for internal data.
🏢 **Office example:** Anyone with any ID card from anywhere.

---

## 🛒 E-Commerce Full-Stack Example

`domain:shopnow.com` → dataViewer on `public_kpis`.

---

## 🧠 Key Takeaways / Memory Tips

- **Everyone in the company → domain: principal. Not allAuthenticatedUsers.**
  🧠 *"**Company badge = domain.**"*
- Related: **Q346**.

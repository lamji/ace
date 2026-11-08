# Q353: Daily Billing Export With Resource-Level Cost Data (Standard + Detailed Usage Cost Export)

**Topic:** Billing (export types)

## ❓ Question
> You manage your company’s Google Cloud environment. Your company has a budget and wants to centralize cost management by consolidating all projects under a single Cloud Billing account. The finance team requires a daily export of all billing data to a central BigQuery dataset for analysis, including resource-level cost data. You must implement the most cost-effective solution with minimal administrative impact. What should you do?
>
> **A.** Link each project to the Cloud Billing account. Create a new Cloud Billing budget alert with Pub/Sub as the destination, and use a Cloud Run function to write the alerts to BigQuery.
>
> **B.** Link each project to the Cloud Billing account. Enable the standard and detailed usage cost exports on the billing account, specifying a BigQuery dataset as the destination.
>
> **C.** Link each project to the Cloud Billing account. Enable the standard usage cost export on the billing account, specifying a BigQuery dataset as the destination.
>
> **D.** Link each project to the Cloud Billing account. Use the gcloud billing budgets create command to set a budget for each project, and then use the cost breakdown report in the Google Cloud console to manually export the daily costs.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company wants all projects under one Cloud Billing account. Finance needs a daily export of all billing data, including per-resource costs, to a central BigQuery dataset.
- **What you must achieve:** Set this up.
- **The limits:** Most cost-effective with minimal admin impact.
- **What they're really asking:** Which export settings provide daily, resource-level billing data in BigQuery?

**Clues in the question:**
- "**resource-level cost data**" → **detailed usage cost** export (adds resource names/IDs). Enable with standard export.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Standard vs detailed usage cost export 🔑
- **What it is:** Standard: costs by project/service/SKU. Detailed: same plus resource-level data (e.g., which VM).
- **Looks like:** Billing export → BigQuery: ☑ Standard ☑ Detailed
- **Not to be confused with:** pricing export (list prices).
- **Analogy:** 🧾 Summary statement vs itemized receipt.
- **In the online store:** —

### 🔗 How they fit together
```
 billing account → standard + detailed export → BigQuery ✅
```

---

## 🌍 Real-World Scenario

Finance enables **standard + detailed** export to a central dataset to see cost per VM and bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Link each project to the Cloud Billing account. Create a new Cloud Billing budget alert with Pub/Sub as the destination, and use a Cloud Run function to write the alerts to BigQuery.

**Wrong words:**
- ❌ "**budget alert … Pub/Sub … Cloud Run function**": alerts only, not full billing data.

📌 **When to use it:** Use it for automated budget reactions.
🏢 **Office example:** Writing down warnings instead of receipts.

### ✅ B
> **B.** Link each project to the Cloud Billing account. Enable the standard and detailed usage cost exports on the billing account, specifying a BigQuery dataset as the destination.

**Why it's correct:**
- ✔️ "**Link each project to the Cloud Billing account**" matches "**consolidating all projects under a single Cloud Billing account**".
- ✔️ "**standard and detailed usage cost exports … BigQuery**" matches "**daily export of all billing data … including resource-level cost data**".

📌 **When to use it:** Use it when finance wants every cost line down to each machine.
🏢 **Office example:** Getting itemized receipts sent to the accounting spreadsheet automatically.

### ❌ C
> **C.** Link each project to the Cloud Billing account. Enable the standard usage cost export on the billing account, specifying a BigQuery dataset as the destination.

**Wrong words:**
- ❌ "**standard usage cost export**" only: no resource-level detail.

📌 **When to use it:** Use standard alone for project/service totals.
🏢 **Office example:** A summary statement only.

### ❌ D
> **D.** Link each project to the Cloud Billing account. Use the gcloud billing budgets create command to set a budget for each project, and then use the cost breakdown report in the Google Cloud console to manually export the daily costs.

**Wrong words:**
- ❌ "**manually export the daily costs**": manual work.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Copying numbers by hand daily.

---

## 🛒 E-Commerce Full-Stack Example

Export `billing_export` with standard + detailed; Looker Studio per-resource costs.

---

## 🧠 Key Takeaways / Memory Tips

- **Resource-level costs → detailed usage cost export.**
  🧠 *"**Detailed = per resource.**"*
- Related: **Q309**, **Q321**.

# Q363: Find Service Account Keys Older Than 90 Days (asset search-all-resources for ServiceAccountKey) — repeat of Q340

**Topic:** Security (Cloud Asset Inventory)

## ❓ Question
> Your organization has created hundreds of service accounts for different applications hosted on-premises and in other clouds that use Google Cloud APIs. You need to audit the service account keys that have been created and identify the keys that are older than 90 days. What should you do?
>
> **A.** Execute the gcloud kms keys list --filter=“createTime < [DATE_90_DAYS_AGO]” command.
>
> **B.** Execute the gcloud iam service-accounts list --filter=“createTime < [DATE_90_DAYS_AGO]” command.
>
> **C.** Execute the gcloud asset search-all-resources --scope=“organizations/[ORG_ID]” --query=“createTime < [DATE_90_DAYS_AGO]” --asset-types=“iam.googleapis.com/ServiceAccountKey” --order-by=“createTime” command.
>
> **D.** Execute the gcloud asset search-all-resources --scope=“organizations/[ORG_ID]” --query=“createTime < [DATE_90_DAYS_AGO]” --asset-types=“apikeys.googleapis.com/Key” --order-by=“createTime” command.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** Same question as **Q340** with options in a different order (here the right answer is **C**).

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your organization has hundreds of service accounts used by apps on-premises and in other clouds.
- **What you must achieve:** Audit service account keys and find those older than 90 days.
- **The limits:** Across the whole organization.
- **What they're really asking:** Which command finds old service account keys organization-wide?

**Clues in the question:**
- Org-wide → **asset search**; type **`iam.googleapis.com/ServiceAccountKey`**.

**Exam topic:** Security.

---

## 📚 Key Terms Explained

### 1. gcloud asset search-all-resources 🔑 (review from Q340)
- **What it is:** Org-wide resource search.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🔍 Company inventory search.
- **In the online store:** —

### 🔗 How they fit together
```
 asset search (ServiceAccountKey, createTime < 90d) ✅
```

---

## 🌍 Real-World Scenario

Same as Q340.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Execute the gcloud kms keys list --filter=“createTime < [DATE_90_DAYS_AGO]” command.

**Wrong words:**
- ❌ "**gcloud kms keys list**": Cloud KMS encryption keys, not service account keys.

📌 **When to use it:** Use it to list encryption keys.
🏢 **Office example:** Checking the safe's combination list for badges.

### ❌ B
> **B.** Execute the gcloud iam service-accounts list --filter=“createTime < [DATE_90_DAYS_AGO]” command.

**Wrong words:**
- ❌ "**iam service-accounts list**": accounts, not keys; one project.

📌 **When to use it:** Use it to list SAs in a project.
🏢 **Office example:** Listing staff, not their keys.

### ✅ C
> **C.** Execute the gcloud asset search-all-resources --scope=“organizations/[ORG_ID]” --query=“createTime < [DATE_90_DAYS_AGO]” --asset-types=“iam.googleapis.com/ServiceAccountKey” --order-by=“createTime” command.

**Why it's correct:**
- ✔️ "**asset search-all-resources --scope=“organizations/[ORG_ID]”**" matches "**hundreds of service accounts**" org-wide.
- ✔️ "**--asset-types=“iam.googleapis.com/ServiceAccountKey”**" + "**createTime < [DATE_90_DAYS_AGO]**" matches "**identify the keys that are older than 90 days**".

📌 **When to use it:** Use it when you need to find old keys anywhere in the company in one search.
🏢 **Office example:** Searching the company-wide inventory for keys issued over 90 days ago.

### ❌ D
> **D.** Execute the gcloud asset search-all-resources --scope=“organizations/[ORG_ID]” --query=“createTime < [DATE_90_DAYS_AGO]” --asset-types=“apikeys.googleapis.com/Key” --order-by=“createTime” command.

**Wrong words:**
- ❌ "**apikeys.googleapis.com/Key**": API keys, not SA keys.

📌 **When to use it:** Use it to audit API keys.
🏢 **Office example:** Searching door codes instead of badges.

---

## 🛒 E-Commerce Full-Stack Example

Same as Q340.

---

## 🧠 Key Takeaways / Memory Tips

- **SA keys = `iam.googleapis.com/ServiceAccountKey`; KMS keys and API keys are different things.**
  🧠 *"**Right type, right keys.**"*
- Related: **Q340**.

# Q340: Find Service Account Keys Older Than 90 Days Across the Org (gcloud asset search-all-resources for ServiceAccountKey)

**Topic:** Security (Cloud Asset Inventory)

## ❓ Question
> Your organization has created hundreds of service accounts for different applications hosted on-premises and in other clouds that use Google Cloud APIs. You need to audit the service account keys that have been created and identify the keys that are older than 90 days. What should you do?
>
> **A.** Execute the gcloud asset search-all-resources --scope="organizations/[ORG_ID]" --query="createTime < [DATE_90_DAYS_AGO]" --asset-types="apikeys.googleapis.com/Key" --order-by="createTime" command.
>
> **B.** Execute the gcloud iam service-accounts list --filter="createTime < [DATE_90_DAYS_AGO]" command.
>
> **C.** Execute the gcloud tans keys list --filter="createTime < [DATE_90_DAYS_AGO]" command.
>
> **D.** Execute the gcloud asset search-all-resources --scope="organizations/[ORG_ID]" --query="createTime < [DATE_90_DAYS_AGO]" --asset-types="iam.googleapis.com/ServiceAccountKey" --order-by="createTime" command.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Audit **service account keys** older than 90 days across hundreds of SAs.

**Clues in the question:**
- Org-wide search → **Cloud Asset Inventory** `search-all-resources`.
- Correct asset type: **`iam.googleapis.com/ServiceAccountKey`** (not API keys).

**Exam topic:** Security.

---

## 📚 Key Terms Explained

### 1. gcloud asset search-all-resources 🔑
- **What it is:** Searches resources across an org/folder/project by type and properties (e.g., createTime).
- **Looks like:** `gcloud asset search-all-resources --scope=organizations/123 --asset-types=iam.googleapis.com/ServiceAccountKey --query="createTime < 2026-08-05"`
- **Not to be confused with:** listing SAs one project at a time.
- **Analogy:** 🔍 The company-wide inventory search.
- **In the online store:** ShopNow key audit.

### 🔗 How they fit together
```
 org → asset search (ServiceAccountKey, createTime < 90d) → list ✅
```

---

## 🌍 Real-World Scenario

Security runs an **asset search** for `ServiceAccountKey` older than 90 days across the org, then rotates them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Execute the gcloud asset search-all-resources --scope="organizations/[ORG_ID]" --query="createTime < [DATE_90_DAYS_AGO]" --asset-types="apikeys.googleapis.com/Key" --order-by="createTime" command.

**Wrong words:**
- ✔️ Asset search across the org is right.
- ❌ "**apikeys.googleapis.com/Key**": API keys, not service account keys.

📌 **When to use it:** Use it to audit API keys.
🏢 **Office example:** Searching for door codes when you wanted badges.

### ❌ B
> **B.** Execute the gcloud iam service-accounts list --filter="createTime < [DATE_90_DAYS_AGO]" command.

**Wrong words:**
- ❌ "**iam service-accounts list**": lists accounts (not keys), one project at a time.

📌 **When to use it:** Use it to list SAs in one project.
🏢 **Office example:** Listing employees instead of their keys.

### ❌ C
> **C.** Execute the gcloud tans keys list --filter="createTime < [DATE_90_DAYS_AGO]" command.

**Wrong words:**
- ❌ "**gcloud tans keys list**": not a real command.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A form that doesn't exist.

### ✅ D
> **D.** Execute the gcloud asset search-all-resources --scope="organizations/[ORG_ID]" --query="createTime < [DATE_90_DAYS_AGO]" --asset-types="iam.googleapis.com/ServiceAccountKey" --order-by="createTime" command.

**Why it's correct:**
- ✔️ "**asset search-all-resources --scope=organizations/[ORG_ID]**" matches "**hundreds of service accounts**" across the org.
- ✔️ "**--asset-types=iam.googleapis.com/ServiceAccountKey**" + "**createTime < [DATE_90_DAYS_AGO]**" matches "**identify the keys that are older than 90 days**".

📌 **When to use it:** Use it when you need to find old keys anywhere in the company in one search.
🏢 **Office example:** Searching the company-wide inventory for every key issued over 90 days ago.

---

## 🛒 E-Commerce Full-Stack Example

Monthly key-age audit with asset search; results feed a rotation ticket.

---

## 🧠 Key Takeaways / Memory Tips

- **Org-wide resource audit → Cloud Asset Inventory search. SA keys → `iam.googleapis.com/ServiceAccountKey`.**
  🧠 *"**Search assets, pick the right type.**"*
- Related: **Q363** (same question), **Q348**.

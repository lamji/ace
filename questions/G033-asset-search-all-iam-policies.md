# G033: Find Every Principal With the Owner Role Across the Whole Organization (gcloud asset search-all-iam-policies)

**Topic:** IAM (Cloud Asset Inventory IAM search)
**Exam guide section:** 1.1 Configuring Cloud Asset Inventory; 4.1 Viewing IAM policies

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> An auditor asks for a list of every user, group, and service account that has the Owner role on any project in your organization, which contains more than 300 projects. You want to produce the list quickly with a single command. What should you do?
>
> **A.** Run gcloud asset search-all-iam-policies with the scope set to your organization and a query for roles/owner.
>
> **B.** Open the IAM page of each project in the Google Cloud console and take screenshots.
>
> **C.** Run gcloud projects get-iam-policy for each project in a loop and filter the output.
>
> **D.** Check the Billing reports page for Owner role costs.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An auditor wants to know who has Owner (full control) on any of your 300+ projects.
- **What you must achieve:** Produce a complete list of users, groups and service accounts with the Owner role, across the whole organization.
- **The limits:** Do it quickly, with a single command.
- **What they're really asking:** Which command searches IAM policies across an entire organization at once?

**Clues in the question:**
- "**every … that has the Owner role on any project in your organization**": an org-wide search of IAM policies.
- "**single command**": `gcloud asset search-all-iam-policies --scope=organizations/ID --query="policy:roles/owner"`.

**Exam topic:** IAM and inventory (exam guide sections 1.1 and 4.1).

---

## 📚 Key Terms Explained

### 1. search-all-iam-policies 🔑
- **What it is:** A Cloud Asset Inventory command that searches IAM policies in an org, folder or project scope, with a query such as a role or a member.
- **Looks like:** `gcloud asset search-all-iam-policies --scope=organizations/123456 --query="policy:roles/owner"`
- **Not to be confused with:** `get-iam-policy`, which reads one resource's policy at a time.
- **Analogy:** 🔎 Searching the master key register for everyone holding a master key.
- **In the online store:** The audit report of ShopNow owners.

### 2. Owner role
- **What it is:** The broadest basic role: full control of a project, including IAM.
- **Looks like:** `roles/owner` → `user:ceo@shopnow.com`
- **Not to be confused with:** Organization Administrator, which applies at the org level.
- **Analogy:** 🗝️ A master key.
- **In the online store:** Should be held by very few people.

### 🔗 How they fit together
```
 Org (300+ projects) ─► Cloud Asset Inventory ─search roles/owner─► list of principals + resources ✅
```

---

## 🌍 Real-World Scenario

A SOC 2 auditor requests the list of project owners by tomorrow. One `search-all-iam-policies` command returns every Owner binding across all projects, and the team removes the stale ones the same day.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run gcloud asset search-all-iam-policies with the scope set to your organization and a query for roles/owner.

**Why it's correct:**
- ✔️ "**search-all-iam-policies with the scope set to your organization**" matches "**any project in your organization**".
- ✔️ "**query for roles/owner**" matches "**has the Owner role**".
- ✔️ It's one command, matching "**quickly with a single command**".

📌 **When to use it:** Use it when you need to find who has a certain kind of access anywhere in the company.
🏢 **Office example:** Searching the central key register for every master key at once.

### ❌ B
> **B.** Open the IAM page of each project in the Google Cloud console and take screenshots.

**Wrong words:**
- ❌ "**take screenshots**" of 300+ pages: slow, error-prone and not a single command.

📌 **When to use it:** Use the IAM page to review one project.
🏢 **Office example:** Photographing every office's key cabinet.

### ❌ C
> **C.** Run gcloud projects get-iam-policy for each project in a loop and filter the output.

**Wrong words:**
- ✔️ It would work eventually.
- ❌ "**for each project in a loop**": 300+ calls and scripting. Not a single command.

📌 **When to use it:** Use get-iam-policy to read one project's policy.
🏢 **Office example:** Visiting 300 offices to read each key register.

### ❌ D
> **D.** Check the Billing reports page for Owner role costs.

**Wrong words:**
- ❌ "**Billing reports**": show spending, not who holds which role.

📌 **When to use it:** Use billing reports for costs.
🏢 **Office example:** Checking the expense report to find key holders.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** audit: `gcloud asset search-all-iam-policies --scope=organizations/123456 --query="policy:roles/owner" --format="table(resource, policy.bindings.members)"`.

---

## 🧠 Key Takeaways / Memory Tips

- **Who has role X anywhere in the org → `gcloud asset search-all-iam-policies --scope=organizations/…`.**
  🧠 *"**search-ALL for all projects.**"*
- Related: **Q148** (get-iam-policy), **Q340**, **G032**.

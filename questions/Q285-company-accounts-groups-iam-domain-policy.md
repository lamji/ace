# Q285: Only Company Accounts, Department-Level Access, Low Ops (Groups + IAM Roles + Org Policy Blocking Other Domains)

**Topic:** IAM + Organization Policy (domain restriction)

## ❓ Question
> Your organization is migrating to Google Cloud. You want only users with company-issued Google accounts to access your Google Cloud environment. You must ensure that users of the same department can only access resources within their own department. You want to minimize operational costs while following Google-recommended practices. What should you do?
>
> **A.** Assign users to the relevant Google Groups, and provide access to cloud resources through Identity and Access Management (IAM) roles. Periodically identify and remove non-company issued Google accounts.
>
> **B.** Assign users to the relevant Google Groups, and provide access to cloud resources through Identity and Access Management (IAM) roles. Use organization policies to block non-company issued emails.
>
> **C.** Create a folder for each department in Resource Manager. Grant the users of each department the Folder Admin role on the folder of their department.
>
> **D.** Create a folder for each department in Resource Manager. Grant all company users the Folder Admin role on the organization level.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Only **company accounts**, each **department sees only its own** resources, **low ops**.

**Clues in the question:**
- "**users of the same department can only access … their own department**" → **groups per department** + **IAM roles** on their resources.
- "**only … company-issued Google accounts**" + "**minimize operational costs**" → **org policy** (domain restricted sharing) instead of manual audits.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Domain restricted sharing (review from Q220) 🔑
- **What it is:** Org policy that only allows IAM grants to your company's domain.
- **Looks like:** `iam.allowedPolicyMemberDomains`
- **Not to be confused with:** manual cleanup.
- **Analogy:** 🚫 Company badges only.
- **In the online store:** Only @shopnow.com.

### 🔗 How they fit together
```
 group finance@ → roles on finance resources ✅
 org policy: only company domain ✅
```

---

## 🌍 Real-World Scenario

During migration, the admin creates **department groups**, grants roles to them, and sets the **domain restriction org policy** so outside accounts can never be granted.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Assign users to the relevant Google Groups, and provide access to cloud resources through Identity and Access Management (IAM) roles. Periodically identify and remove non-company issued Google accounts.

**Wrong words:**
- ✔️ Groups + IAM are right.
- ❌ "**Periodically identify and remove non-company issued Google accounts**": manual, ongoing work — not minimal ops.

📌 **When to use it:** Use manual reviews only as an extra check.
🏢 **Office example:** Walking the halls daily checking badges.

### ✅ B
> **B.** Assign users to the relevant Google Groups, and provide access to cloud resources through Identity and Access Management (IAM) roles. Use organization policies to block non-company issued emails.

**Why it's correct:**
- ✔️ "**Google Groups … IAM roles**" matches "**users of the same department can only access resources within their own department**".
- ✔️ "**organization policies to block non-company issued emails**" matches "**only users with company-issued Google accounts**" + "**minimize operational costs**".

📌 **When to use it:** Use it when only staff may get access and each team should only see its own things.
🏢 **Office example:** Department rosters for door access, plus a rule that only company badges can ever be added.

### ❌ C
> **C.** Create a folder for each department in Resource Manager. Grant the users of each department the Folder Admin role on the folder of their department.

**Wrong words:**
- ❌ "**Folder Admin role**": far too much power (can change IAM and create/delete projects).
- ❌ Doesn't block non-company accounts.

📌 **When to use it:** Use Folder Admin for folder administrators.
🏢 **Office example:** Giving every employee the floor's master key.

### ❌ D
> **D.** Create a folder for each department in Resource Manager. Grant all company users the Folder Admin role on the organization level.

**Wrong words:**
- ❌ "**Folder Admin role on the organization level**" for all users: everyone controls everything.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Master keys to the whole company for everyone.

---

## 🛒 E-Commerce Full-Stack Example

Groups `payments@`, `marketing@` with roles on their folders; org policy `iam.allowedPolicyMemberDomains = C0shopnow`.

---

## 🧠 Key Takeaways / Memory Tips

- **Department access → groups + IAM. Company accounts only → domain restriction org policy.**
  🧠 *"**Groups decide who; org policy decides which domain.**"*
- Related: **Q220**, **Q215**.

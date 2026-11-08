# Q111: External Auditor When Domain Restricted Sharing Is On (Temporary Cloud Identity Account + Viewer)

**Topic:** IAM / Organization Policy (Domain Restricted Sharing, Cloud Identity, Viewer vs Security Reviewer)

## ❓ Question
> Your management has asked an external auditor to review all the resources in a specific project. The security team has enabled the Organization Policy called Domain Restricted Sharing on the organization node by specifying only your Cloud Identity domain. You want the auditor to only be able to view, but not modify, the resources in that project. What should you do?
>
> **A.** Ask the auditor for their Google account, and give them the Viewer role on the project.
>
> **B.** Ask the auditor for their Google account, and give them the Security Reviewer role on the project.
>
> **C.** Create a temporary account for the auditor in Cloud Identity, and give that account the Viewer role on the project.
>
> **D.** Create a temporary account for the auditor in Cloud Identity, and give that account the Security Reviewer role on the project.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An external auditor must review the resources in one project. The organization uses Domain Restricted Sharing (only accounts from your own domain can be given roles).
- **What you must achieve:** Let the auditor view but not change anything.
- **The limits:** The policy blocks outside accounts.
- **What they're really asking:** How do you give the auditor view access while respecting that policy?

**Clues in the question:**
- "**Domain Restricted Sharing … only your Cloud Identity domain**": IAM will **reject** the auditor's outside Google account. You must give them an account **in your domain**.
- "**review all the resources**" + "**view, but not modify**" → **Viewer** role (Security Reviewer only sees IAM policies).

**Exam topic:** IAM / Organization Policy.

---

## 📚 Key Terms Explained

### 1. Domain Restricted Sharing 🔑
- **What it is:** An **organization policy** (`iam.allowedPolicyMemberDomains`) that allows IAM roles to be granted **only to accounts from listed domains**. Any other email is rejected.
- **Looks like:** `constraints/iam.allowedPolicyMemberDomains: [C0abc123 (shopnow.com)]`
- **Not to be confused with:** a firewall. It controls **who can be given roles**.
- **Analogy:** 🏢 A rule that **only employees with company badges** may enter, never visitors with outside badges.
- **In the online store:** No one can grant roles to `@gmail.com` accounts in ShopNow's org.

### 2. Temporary Cloud Identity account
- **What it is:** A **company-managed account** (e.g. `auditor-ext@shopnow.com`) that you create for the auditor and delete or suspend after the audit.
- **Looks like:** Admin console → Users → Add user `auditor-ext@shopnow.com`
- **Not to be confused with:** the auditor's personal or firm Google account.
- **Analogy:** 🪪 A **temporary company badge** for a visiting auditor.
- **In the online store:** Created for the audit, suspended afterwards.

### 3. Viewer vs Security Reviewer
- **What it is:** **Viewer** (`roles/viewer`) = read **all resources**. **Security Reviewer** (`roles/iam.securityReviewer`) = read **IAM policies only**.
- **Looks like:** `roles/viewer` / `roles/iam.securityReviewer`
- **Not to be confused with:** each other.
- **Analogy:** 👀 Visitor pass to all rooms vs only the access-list folder.
- **In the online store:** The auditor needs to see VMs, buckets and settings.

### 🔗 How they fit together
```
 Org policy: only shopnow.com accounts may get roles
   auditor@auditfirm.com → roles/viewer ❌ blocked
   auditor-ext@shopnow.com (temporary, Cloud Identity) → roles/viewer ✅
```

---

## 🌍 Real-World Scenario

A security team has locked IAM to the company domain. When an outside audit firm arrives, the admin creates `auditor-ext@company.com` in Cloud Identity, gives it **Viewer** on the project, and suspends it when the audit ends.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ask the auditor for their Google account, and give them the Viewer role on the project.

**Wrong words:**
- ❌ "**Ask the auditor for their Google account**": the outside account isn't in your domain, so Domain Restricted Sharing blocks the grant.
- ✔️ "Viewer role" is the right level.

📌 **When to use it:** Use it when there's no domain restriction policy.
🏢 **Office example:** Letting a visitor in with their outside badge, when the rules accept company badges only.

### ❌ B
> **B.** Ask the auditor for their Google account, and give them the Security Reviewer role on the project.

**Wrong words:**
- ❌ "**their Google account**": blocked by the policy (see A).
- ❌ "**Security Reviewer**": it shows only IAM policies, not "all the resources".

📌 **When to use it:** Use Security Reviewer when someone only needs to review who has which access.
🏢 **Office example:** A visitor pass to the access-list folder only, using a badge the guard won't accept.

### ✅ C
> **C.** Create a temporary account for the auditor in Cloud Identity, and give that account the Viewer role on the project.

**Why it's correct:**
- ✔️ "**Create a temporary account for the auditor in Cloud Identity**" matches "**Domain Restricted Sharing … only your Cloud Identity domain**": the new account is in your domain, so it's allowed.
- ✔️ "**Viewer role**" matches "**review all the resources**" + "**only be able to view, but not modify**": read-only access to everything in the project.
- ✔️ "**temporary**" matches "**external auditor**": you suspend or delete it after the audit.

📌 **When to use it:** Use it when only company accounts are allowed and an outsider needs read-only access for a while.
🏢 **Office example:** Giving the visiting auditor a temporary company badge that opens every room for looking only.

### ❌ D
> **D.** Create a temporary account for the auditor in Cloud Identity, and give that account the Security Reviewer role on the project.

**Wrong words:**
- ✔️ "temporary account … in Cloud Identity" is right.
- ❌ "**Security Reviewer role**": it only shows IAM policies, not all resources.

📌 **When to use it:** Use it when the auditor only reviews permissions.
🏢 **Office example:** A temporary company badge that opens only the access-list room.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's org allows only `shopnow.com` accounts.
1. Admin console → add user `auditor-2026@shopnow.com`.
2. `gcloud projects add-iam-policy-binding shopnow-prod --member=user:auditor-2026@shopnow.com --role=roles/viewer`
3. After the audit, suspend the account.

---

## 🧠 Key Takeaways / Memory Tips

- **Domain Restricted Sharing → outsiders need an account in your domain.**
- **View all resources → Viewer.** Security Reviewer = IAM policies only.
  🧠 *"**Outside badge blocked? Issue a temporary company badge.**"*
- Related: **Q080** (auditor Viewer), **Q025** (auditors group), **Q083** (Workspace users).

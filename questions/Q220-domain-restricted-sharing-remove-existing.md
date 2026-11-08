# Q220: Only Share With Your Domain and Remove Outsiders (Domain Restriction Org Policy + Remove Existing Users)

**Topic:** Organization Policy (domain restricted sharing)

## ❓ Question
> During a recent audit of your existing Google Cloud resources, you discovered several users with email addresses outside of your Google Workspace domain. You want to ensure that your resources are only shared with users whose email addresses match your domain. You need to remove any mismatched users, and you want to avoid having to audit your resources to identify mismatched users. What should you do?
>
> **A.** Create a Cloud Scheduler task to regularly scan your projects and delete mismatched users.
>
> **B.** Create a Cloud Scheduler task to regularly scan your resources and delete mismatched users.
>
> **C.** Set an organizational policy constraint to limit identities by domain to automatically remove mismatched users.
>
> **D.** Set an organizational policy constraint to limit identities by domain, and then retroactively remove the existing mismatched users

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An audit found users with email addresses outside your Google Workspace domain on your resources.
- **What you must achieve:** Only users from your domain may get access, and outsiders must be removed.
- **The limits:** You don't want to keep auditing resources by hand.
- **What they're really asking:** What setting enforces domain-only sharing automatically?

**Clues in the question:**
- "**only shared with users whose email addresses match your domain**" + "**avoid having to audit**" → org policy **`iam.allowedPolicyMemberDomains`** (domain restricted sharing).
- The policy **isn't retroactive**: existing outsiders stay until you **remove them yourself**.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. Domain restricted sharing 🔑
- **What it is:** Org policy constraint `iam.allowedPolicyMemberDomains`: IAM grants can only go to identities from allowed domains. **Existing** grants aren't removed.
- **Looks like:** allowed: `C0abc123` (your Workspace customer ID)
- **Not to be confused with:** IAM roles.
- **Analogy:** 🚫 "Company badges only" rule for new keys.
- **In the online store:** Only @shopnow.com.

### 2. Retroactive
- **What it is:** Applying to things that already exist.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** —
- **In the online store:** —

### 🔗 How they fit together
```
 org policy (allowed domain: shopnow.com) → blocks NEW outside grants ✅
 existing outsiders → remove manually once ✅
```

---

## 🌍 Real-World Scenario

An audit finds Gmail users on prod. The admin sets **domain restricted sharing**, then removes the existing outside users once. New outside grants are blocked automatically.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Scheduler task to regularly scan your projects and delete mismatched users.

**Wrong words:**
- ❌ "**Cloud Scheduler task to regularly scan your projects**": custom code and ongoing audits, which the question wants to avoid.

📌 **When to use it:** **Avoid this**; use the built-in policy.
🏢 **Office example:** Hiring someone to walk the halls daily checking badges.

### ❌ B
> **B.** Create a Cloud Scheduler task to regularly scan your resources and delete mismatched users.

**Wrong words:**
- ❌ "**regularly scan your resources**": same problem.

📌 **When to use it:** **Avoid this.**
🏢 **Office example:** Same daily badge walk.

### ❌ C
> **C.** Set an organizational policy constraint to limit identities by domain to automatically remove mismatched users.

**Wrong words:**
- ✔️ "organizational policy constraint to limit identities by domain" is right.
- ❌ "**to automatically remove mismatched users**": the policy doesn't remove existing users; it only blocks new ones.

📌 **When to use it:** Use the policy, but know you still clean up existing users.
🏢 **Office example:** A new badge rule that doesn't take back badges already handed out.

### ✅ D
> **D.** Set an organizational policy constraint to limit identities by domain, and then retroactively remove the existing mismatched users

**Why it's correct:**
- ✔️ "**organizational policy constraint to limit identities by domain**" matches "**only shared with users whose email addresses match your domain**" + "**avoid having to audit**".
- ✔️ "**retroactively remove the existing mismatched users**" matches "**remove any mismatched users**": the policy doesn't do this on its own.

📌 **When to use it:** Use it when outsiders must never get access again and the ones already in must be removed.
🏢 **Office example:** Posting a "company badges only" rule, then collecting the visitor badges already handed out.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud resource-manager org-policies allow iam.allowedPolicyMemberDomains C0shopnow --organization=SHOPNOW_ORG` → then remove `user:someone@gmail.com` bindings.

---

## 🧠 Key Takeaways / Memory Tips

- **Only your domain → domain restricted sharing org policy. It isn't retroactive: remove existing outsiders.**
  🧠 *"**Policy stops new; you clean old.**"*
- Related: **Q204**, **Q186**.

# Q118: First Version of a Custom Role for Production (Supported Permissions + ALPHA Stage)

**Topic:** IAM (custom roles: permission support levels, role launch stages)

## ❓ Question
> You need to create a custom IAM role for use with a GCP service. All permissions in the role must be suitable for production use. You also want to clearly share with your organization the status of the custom role. This will be the first version of the custom role. What should you do?
>
> **A.** Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.
>
> **B.** Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to BETA while testing the role permissions.
>
> **C.** Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.
>
> **D.** Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to BETA while testing the role permissions.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are making a custom IAM role.
- **What you must achieve:** All its permissions are fit for production, and the organization can clearly see the role's status.
- **The limits:** This is the first version of the role.
- **What they're really asking:** How do you mark the role's launch stage?

**Clues in the question:**
- "**suitable for production use**" → permissions with the **SUPPORTED** support level (TESTING ones may change or break).
- "**first version**" + "**clearly share … the status**" → set the role's **stage** to **ALPHA** while you test it. Later BETA, then GA.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Permission support level 🔑
- **What it is:** A label Google puts on each permission for custom roles: **SUPPORTED** (safe for production), **TESTING** (may change, not for production), **NOT_SUPPORTED** (can't be used).
- **Looks like:** `gcloud iam list-testable-permissions //cloudresourcemanager.googleapis.com/projects/shopnow-prod` → `customRolesSupportLevel: SUPPORTED`
- **Not to be confused with:** the role's stage.
- **Analogy:** ✅ Approved parts vs 🧪 prototype parts for building a machine.
- **In the online store:** Only SUPPORTED permissions go into ShopNow's prod roles.

### 2. Role stage 🔑
- **What it is:** A label **you** put on a custom role to show its status: **ALPHA** (first version, testing) → **BETA** (tested, being rolled out) → **GA** (stable). Also DEPRECATED / DISABLED.
- **Looks like:** `gcloud iam roles create bqAnalyst --project=shopnow-prod --stage=ALPHA --permissions=...`
- **Not to be confused with:** permission support levels.
- **Analogy:** 🏷️ A "**DRAFT v1**" sticker on a new office policy.
- **In the online store:** `bqAnalyst` starts as ALPHA, becomes GA after review.

### 🔗 How they fit together
```
 permissions: SUPPORTED ✅ (production-safe)   TESTING ❌ (may change)
 role stage:  ALPHA (first version, testing) ✅ → BETA → GA
```

---

## 🌍 Real-World Scenario

A security team builds a custom role for a new service. They include only **SUPPORTED** permissions and create the role with **stage ALPHA**, so other admins can see it's new and still being tested. After a few weeks it's promoted to GA.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.

**Why it's correct:**
- ✔️ "**'supported' support level**" matches "**All permissions in the role must be suitable for production use**": supported permissions are stable.
- ✔️ "**Set the role stage to ALPHA**" matches "**This will be the first version**": ALPHA marks a brand-new role under test.
- ✔️ "**role stage**" matches "**clearly share with your organization the status**": everyone sees the stage label.

📌 **When to use it:** Use it when you build a new set of rules from approved parts and label it as a first draft.
🏢 **Office example:** A new office policy made only from approved rules, marked "DRAFT v1" while it's tried out.

### ❌ B
> **B.** Use permissions in your role that use the 'supported' support level for role permissions. Set the role stage to BETA while testing the role permissions.

**Wrong words:**
- ✔️ "'supported' support level" is right.
- ❌ "**ALPHA → BETA**": BETA means the role has already been tested. Not the stage for a **first version**.

📌 **When to use it:** Use BETA after the ALPHA version has been tested and is being rolled out.
🏢 **Office example:** Marking a brand-new policy "almost final" before anyone has tried it.

### ❌ C
> **C.** Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to ALPHA while testing the role permissions.

**Wrong words:**
- ❌ "**'testing' support level**": testing permissions may change or break, so they aren't "suitable for production use".
- ✔️ "ALPHA" is right.

📌 **When to use it:** Use testing permissions only in non-production experiments.
🏢 **Office example:** Building a policy from prototype rules that may change next week.

### ❌ D
> **D.** Use permissions in your role that use the 'testing' support level for role permissions. Set the role stage to BETA while testing the role permissions.

**Wrong words:**
- ❌ "**'testing' support level**": not production-safe (see C).
- ❌ "**BETA**": wrong stage for a first version (see B).

📌 **When to use it:** **Never use this** for production. Use A.
🏢 **Office example:** Prototype rules, labeled almost final.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud iam roles create shopOrdersReader --project=shopnow-prod --stage=ALPHA \
  --title="Orders reader (v1)" --permissions=cloudsql.instances.get,cloudsql.databases.get
# after review:
gcloud iam roles update shopOrdersReader --project=shopnow-prod --stage=GA
```

---

## 🧠 Key Takeaways / Memory Tips

- **Production → SUPPORTED permissions.** TESTING ones may change.
- **First version → stage ALPHA**, then BETA, then GA.
  🧠 *"**Supported parts, Alpha sticker.**"*
- Related: **Q102** (custom role without delete), **Q080** (built-in vs custom roles).

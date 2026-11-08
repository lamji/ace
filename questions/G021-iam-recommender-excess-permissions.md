# G021: Remove Permissions Service Accounts Never Use, Based on Real Usage (IAM Recommender)

**Topic:** IAM (IAM recommender / Active Assist)
**Exam guide section:** 4.1 Managing IAM; 3.4 Using Active Assist to optimize resource utilization

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Several service accounts in your project were granted the Editor role years ago. You want to follow the principle of least privilege by replacing these grants with roles that match the permissions the service accounts actually used, with minimal manual analysis. What should you do?
>
> **A.** Read the application source code to guess which permissions are needed.
>
> **B.** Remove all roles from the service accounts and wait for applications to fail.
>
> **C.** Grant the Owner role instead so that all permissions are visible in one place.
>
> **D.** Review IAM role recommendations from the IAM recommender, and apply the suggested replacement roles.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Years ago, several service accounts (non-human accounts that apps use) were given Editor, a broad role that can change almost anything in a project.
- **What you must achieve:** Cut each one down to only the permissions it actually uses (least privilege: give only what's needed).
- **The limits:** Avoid lots of manual investigation.
- **What they're really asking:** Which Google Cloud feature looks at real permission usage and suggests smaller roles?

**Clues in the question:**
- "**permissions the service accounts actually used**": usage-based analysis. That's the **IAM recommender** (role recommendations).
- "**least privilege**" + "**minimal manual analysis**": apply Google's suggested replacement roles.

**Exam topic:** IAM (exam guide section 4.1).

---

## 📚 Key Terms Explained

### 1. IAM recommender 🔑
- **What it is:** Part of Active Assist / Policy Intelligence. It looks at about 90 days of permission usage and recommends removing or replacing roles with smaller ones.
- **Looks like:** "`sa-orders@` has Editor but used 6 permissions → replace with `roles/cloudsql.client` + `roles/pubsub.publisher`"
- **Not to be confused with:** Policy Troubleshooter, which explains why access was allowed or denied but doesn't suggest smaller roles.
- **Analogy:** 🔑 A locksmith who checks which doors a key actually opened and cuts a smaller key.
- **In the online store:** Shrinks the order service's account.

### 2. Basic roles (Owner / Editor / Viewer)
- **What it is:** Very broad project-wide roles from early Google Cloud. They're not recommended for production.
- **Looks like:** `roles/editor` = change almost everything
- **Not to be confused with:** Predefined roles, which are narrow and per-service.
- **Analogy:** 🗝️ A master key.
- **In the online store:** Being removed from ShopNow service accounts.

### 🔗 How they fit together
```
 sa-orders@: roles/editor ─(90 days usage)─► IAM recommender
   → replace with roles/cloudsql.client + roles/pubsub.publisher ✅
```

---

## 🌍 Real-World Scenario

A security review finds 12 service accounts with Editor. The **IAM recommender** shows each account's real usage and suggests narrow roles. The team applies them in a week, with no outages.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Read the application source code to guess which permissions are needed.

**Wrong words:**
- ❌ "**guess which permissions**": slow, error-prone manual work, which the question wants to avoid.

📌 **When to use it:** Use code review to double-check a recommendation, not as the main method.
🏢 **Office example:** Guessing door use from the job description instead of the access logs.

### ❌ B
> **B.** Remove all roles from the service accounts and wait for applications to fail.

**Wrong words:**
- ❌ "**Remove all roles … wait for applications to fail**": causes outages, and discovering needs by breaking things isn't a plan.

📌 **When to use it:** Never use this in production. Use usage-based recommendations.
🏢 **Office example:** Taking away every key and waiting for complaints.

### ❌ C
> **C.** Grant the Owner role instead so that all permissions are visible in one place.

**Wrong words:**
- ❌ "**Grant the Owner role**": even broader than Editor. The opposite of least privilege.

📌 **When to use it:** Never use this to tidy permissions.
🏢 **Office example:** Swapping a big key for the master key.

### ✅ D
> **D.** Review IAM role recommendations from the IAM recommender, and apply the suggested replacement roles.

**Why it's correct:**
- ✔️ "**IAM role recommendations from the IAM recommender**" matches "**permissions the service accounts actually used**".
- ✔️ "**apply the suggested replacement roles**" matches "**least privilege**" and "**minimal manual analysis**".

📌 **When to use it:** Use it when you want to shrink broad access to what people or apps really use.
🏢 **Office example:** A locksmith checks which doors each key actually opened and gives smaller keys.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: `sa-orders@` (Editor) → recommended `roles/cloudsql.client` + `roles/pubsub.publisher`. `sa-images@` (Editor) → `roles/storage.objectAdmin` on one bucket.

---

## 🧠 Key Takeaways / Memory Tips

- **Shrink over-broad roles based on actual use → IAM recommender (role recommendations).**
  🧠 *"**Recommender trims keys to doors used.**"*
- Related: **G020**, **Q080**, **Q211**.

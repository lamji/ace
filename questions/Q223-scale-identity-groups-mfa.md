# Q223: Grow From 100 to 1,000 Employees Simply and Securely (Cloud Identity Groups + Enforce MFA)

**Topic:** Cloud Identity (groups, MFA)

## ❓ Question
> Your company is using Google Workspace to manage employee accounts. Anticipated growth will increase the number of personnel from 100 employees to 1,000 employees within 2 years. Most employees will need access to your company's Google Cloud account. The systems and processes will need to support 10x growth without performance degradation, unnecessary complexity, or security issues. What should you do?
>
> **A.** Migrate the users to Active Directory. Connect the Human Resources system to Active Directory. Turn on Google Cloud Directory Sync (GCDS) for Cloud Identity. Turn on Identity Federation from Cloud Identity to Active Directory.
>
> **B.** Organize the users in Cloud Identity into groups. Enforce multi-factor authentication in Cloud Identity.
>
> **C.** Turn on identity federation between Cloud Identity and Google Workspace. Enforce multi-factor authentication for domain wide delegation.
>
> **D.** Use a third-party identity provider service through federation. Synchronize the users from Google Workplace to the third-party provider in real time.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company manages employee accounts in Google Workspace and will grow from 100 to 1,000 employees in 2 years. Most will need Google Cloud access.
- **What you must achieve:** Set up access that handles 10 times more people.
- **The limits:** No slowdowns, no unnecessary complexity, no security problems.
- **What they're really asking:** How should you organize access so it scales easily as staff grows?

**Clues in the question:**
- "**without … unnecessary complexity**" → keep the existing Google identity; organize with **groups** (grant roles to groups, not people).
- "**without … security issues**" → **enforce MFA**.

**Exam topic:** Cloud Identity.

---

## 📚 Key Terms Explained

### 1. Groups for access 🔑
- **What it is:** Give roles to groups; adding a new hire to a group grants everything they need.
- **Looks like:** `devs@company.com` → roles
- **Not to be confused with:** per-user grants.
- **Analogy:** 📋 Department rosters.
- **In the online store:** ShopNow teams.

### 2. MFA (2-Step Verification)
- **What it is:** Sign-in needs a second factor (phone prompt, security key).
- **Looks like:** Admin console → Security → 2SV → Enforce
- **Not to be confused with:** passwords only.
- **Analogy:** 🔐 Badge + PIN.
- **In the online store:** —

### 🔗 How they fit together
```
 Workspace/Cloud Identity users → groups (eng@, finance@) → IAM roles ✅ + MFA enforced ✅
```

---

## 🌍 Real-World Scenario

A fast-growing company keeps its Workspace identities, organizes people into **groups** that hold IAM roles, and **enforces MFA**. New hires just join a group.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate the users to Active Directory. Connect the Human Resources system to Active Directory. Turn on Google Cloud Directory Sync (GCDS) for Cloud Identity. Turn on Identity Federation from Cloud Identity to Active Directory.

**Wrong words:**
- ❌ "**Migrate the users to Active Directory … GCDS … Federation**": adds a whole new system, which is **unnecessary complexity**.

📌 **When to use it:** Use AD + GCDS when the company already runs Active Directory as its main directory.
🏢 **Office example:** Building a second HR office to manage the same staff.

### ✅ B
> **B.** Organize the users in Cloud Identity into groups. Enforce multi-factor authentication in Cloud Identity.

**Why it's correct:**
- ✔️ "**Organize the users in Cloud Identity into groups**" matches "**support 10x growth without … unnecessary complexity**".
- ✔️ "**Enforce multi-factor authentication**" matches "**without … security issues**".

📌 **When to use it:** Use it when the company will grow fast and you want access to stay simple and safe.
🏢 **Office example:** Keeping department rosters for access and requiring a badge plus PIN for everyone.

### ❌ C
> **C.** Turn on identity federation between Cloud Identity and Google Workspace. Enforce multi-factor authentication for domain wide delegation.

**Wrong words:**
- ❌ "**federation between Cloud Identity and Google Workspace**": they're the same Google identity system; nothing to federate.
- ❌ "**MFA for domain wide delegation**": delegation is for apps, not user sign-in.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Connecting the HR office to itself.

### ❌ D
> **D.** Use a third-party identity provider service through federation. Synchronize the users from Google Workplace to the third-party provider in real time.

**Wrong words:**
- ❌ "**third-party identity provider … Synchronize … in real time**": extra product, cost and complexity.

📌 **When to use it:** Use a third-party IdP if the company already standardized on one.
🏢 **Office example:** Hiring an outside firm to manage badges you already handle.

---

## 🛒 E-Commerce Full-Stack Example

Groups `eng@`, `support@`, `finance@shopnow.com` hold all IAM roles; 2-Step Verification enforced for the org.

---

## 🧠 Key Takeaways / Memory Tips

- **Scale identity simply → groups. Secure it → enforce MFA.**
  🧠 *"**Groups to grow, MFA to protect.**"*
- Related: **Q178**, **Q186**.

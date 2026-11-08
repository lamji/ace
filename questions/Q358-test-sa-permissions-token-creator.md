# Q358: Test a Service Account's Permissions From Your Workstation Without Secrets (serviceAccountTokenCreator)

**Topic:** IAM (impersonation)

## ❓ Question
> You are using your personal workstation to develop an application that will be hosted in Google Cloud. You are authenticated using a Google Account (USER). You need to test whether a specific set of permissions assigned to an existing service account (SERVICE_ACCOUNT) are sufficient for a task without handling sensitive secret information. What should you do?
>
> **A.** Grant USER the IAM role roles/iam.workloadIdentityUser on SERVICE_ACCOUNT.
>
> **B.** Grant USER the IAM role roles/iam.serviceAccountKeyAdmin on SERVICE_ACCOUNT.
>
> **C.** Grant USER the IAM role roles/iam.serviceAccountTokenCreator on SERVICE_ACCOUNT.
>
> **D.** Grant USER the IAM role roles/iam.serviceAccountUser on SERVICE_ACCOUNT.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You develop on your own workstation, signed in with your Google account (USER).
- **What you must achieve:** Test whether an existing service account's (SERVICE_ACCOUNT) permissions are enough for a task.
- **The limits:** Don't handle any sensitive secrets like key files.
- **What they're really asking:** Which role should USER get on the service account?

**Clues in the question:**
- Impersonation (short-lived tokens) requires **`roles/iam.serviceAccountTokenCreator`**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/iam.serviceAccountTokenCreator 🔑
- **What it is:** Lets a principal create short-lived tokens for a service account (impersonate it).
- **Looks like:** `gcloud iam service-accounts add-iam-policy-binding SA --member=user:me@ --role=roles/iam.serviceAccountTokenCreator` then `--impersonate-service-account=SA`
- **Not to be confused with:** serviceAccountUser (attach SA to resources).
- **Analogy:** 🎭 Permission to wear the role's badge temporarily.
- **In the online store:** —

### 🔗 How they fit together
```
 USER (TokenCreator on SA) → --impersonate-service-account → test ✅
```

---

## 🌍 Real-World Scenario

A developer gets **TokenCreator** on the SA and runs `gcloud storage ls --impersonate-service-account=...`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant USER the IAM role roles/iam.workloadIdentityUser on SERVICE_ACCOUNT.

**Wrong words:**
- ❌ "**workloadIdentityUser**": for Kubernetes/external workloads, not a user.

📌 **When to use it:** Use it to bind KSAs to GSAs.
🏢 **Office example:** A badge-link for robots, not people.

### ❌ B
> **B.** Grant USER the IAM role roles/iam.serviceAccountKeyAdmin on SERVICE_ACCOUNT.

**Wrong words:**
- ❌ "**serviceAccountKeyAdmin**": manages keys — the secrets you want to avoid.

📌 **When to use it:** Use it for key rotation admins.
🏢 **Office example:** Keys to the key cabinet.

### ✅ C
> **C.** Grant USER the IAM role roles/iam.serviceAccountTokenCreator on SERVICE_ACCOUNT.

**Why it's correct:**
- ✔️ "**serviceAccountTokenCreator**" matches "**test whether … permissions assigned to an existing service account … are sufficient**" + "**without handling sensitive secret information**".

📌 **When to use it:** Use it when you need to try things as a robot account without holding its password.
🏢 **Office example:** Permission to wear the role's badge for a short test, no key copied.

### ❌ D
> **D.** Grant USER the IAM role roles/iam.serviceAccountUser on SERVICE_ACCOUNT.

**Wrong words:**
- ❌ "**serviceAccountUser**": lets you attach the SA to resources (VMs, Cloud Run), not generate tokens to act as it locally.

📌 **When to use it:** Use it when deploying resources that run as the SA.
🏢 **Office example:** Assigning a badge to a robot, not wearing it.

---

## 🛒 E-Commerce Full-Stack Example

Dev gets TokenCreator on `checkout-sa` to test Cloud SQL access.

---

## 🧠 Key Takeaways / Memory Tips

- **Impersonate locally → serviceAccountTokenCreator.**
  🧠 *"**Token Creator = try on the badge.**"*
- Related: **Q332**, **Q345**.

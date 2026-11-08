# Q345: Gain Permission to Modify IAM Policies for Service Accounts, Least Privilege (roles/iam.serviceAccountAdmin)

**Topic:** IAM (roles)

## ❓ Question
> You are managing resources in a Google Cloud project. A new service account needs the ability to invoke a Cloud Run service. You need to gain the permissions to modify IAM policies for service accounts while adhering to the principle of least privilege. What should you do?
>
> **A.** Request the roles/iam.serviceAccountAdmin role for your user account.
>
> **B.** Request the roles/run.invoker role for your user account.
>
> **C.** Request the Editor role for your user account.
>
> **D.** Request the Owner role for your user account.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **A**. The question literally asks for permission "**to modify IAM policies for service accounts**", which Service Account Admin includes (`iam.serviceAccounts.setIamPolicy`). Strictly, granting the SA Run Invoker on a Cloud Run service needs `run.services.setIamPolicy` (e.g., Cloud Run Admin), which no option offers.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new service account must be allowed to invoke (call) a Cloud Run service.
- **What you must achieve:** Get permission to change IAM policies for service accounts.
- **The limits:** Least privilege (only what you need).
- **What they're really asking:** Which role should you request for your own account?

**Clues in the question:**
- "**modify IAM policies for service accounts**" + "**least privilege**" → **Service Account Admin**, not Editor/Owner.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/iam.serviceAccountAdmin 🔑
- **What it is:** Create/manage service accounts and their IAM policies.
- **Looks like:** `gcloud projects add-iam-policy-binding p --member=user:me@ --role=roles/iam.serviceAccountAdmin`
- **Not to be confused with:** run.invoker (calls Cloud Run).
- **Analogy:** 🧑‍💼 HR for robot staff.
- **In the online store:** —

### 🔗 How they fit together
```
 need: change SA IAM policies → serviceAccountAdmin ✅ (Editor/Owner too broad)
```

---

## 🌍 Real-World Scenario

An engineer requests **Service Account Admin** to manage the new SA's IAM policy, not Owner.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Request the roles/iam.serviceAccountAdmin role for your user account.

**Why it's correct:**
- ✔️ "**roles/iam.serviceAccountAdmin**" matches "**gain the permissions to modify IAM policies for service accounts**" + "**least privilege**".

📌 **When to use it:** Use it when your job is managing robot accounts and who can use them.
🏢 **Office example:** An HR assistant who handles robot staff records only.

### ❌ B
> **B.** Request the roles/run.invoker role for your user account.

**Wrong words:**
- ❌ "**roles/run.invoker**" for your user: lets *you* call Cloud Run; doesn't let you change IAM policies.

📌 **When to use it:** Use run.invoker for callers of a Cloud Run service.
🏢 **Office example:** A visitor pass, not HR access.

### ❌ C
> **C.** Request the Editor role for your user account.

**Wrong words:**
- ❌ "**Editor**": very broad and can't change IAM policies anyway.

📌 **When to use it:** **Avoid** basic roles.
🏢 **Office example:** Keys to almost every room.

### ❌ D
> **D.** Request the Owner role for your user account.

**Wrong words:**
- ❌ "**Owner**": far beyond least privilege.

📌 **When to use it:** Use Owner only for true project owners.
🏢 **Office example:** The master key.

---

## 🛒 E-Commerce Full-Stack Example

Platform engineer gets `roles/iam.serviceAccountAdmin` in `shopnow-prod`.

---

## 🧠 Key Takeaways / Memory Tips

- **Manage SAs and their IAM policies → Service Account Admin.**
  🧠 *"**SA policies? SA Admin.**"*
- Related: **Q358**.

# Q302: Manage Linux Account Lifecycle for Developers on VMs (OS Login + IAM Roles)

**Topic:** Compute Engine (OS Login)

## ❓ Question
> Your company’s developers use an automation that you recently built to provision Linux VMs in Compute Engine within a Google Cloud project to perform various tasks. You need to manage the Linux account lifecycle and access for these users. You want to follow Google-recommended practices to simplify access management while minimizing operational costs. What should you do?
>
> **A.** Enable OS Login for all VMs. Use IAM roles to grant user permissions.
>
> **B.** Require your developers to create public SSH keys. Write custom startup scripts to update user permissions.
>
> **C.** Require your developers to create public SSH keys. Make the owner of the public key the root user.
>
> **D.** Enable OS Login for all VMs. Write custom startup scripts to update user permissions.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Manage developers' Linux accounts on VMs simply and cheaply.

**Clues in the question:**
- "**Linux account lifecycle and access**" + "**simplify access management**" → **OS Login** with **IAM roles**.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. OS Login 🔑 (review from Q294)
- **What it is:** Linux accounts and SSH access come from Google identities and IAM roles.
- **Looks like:** `roles/compute.osLogin`
- **Not to be confused with:** metadata SSH keys.
- **Analogy:** 🪪 Badge access.
- **In the online store:** —

### 🔗 How they fit together
```
 OS Login ON + IAM roles → account created/removed with IAM ✅
```

---

## 🌍 Real-World Scenario

Developers get Linux access via `roles/compute.osLogin` granted in IAM; removing the role removes access.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Enable OS Login for all VMs. Use IAM roles to grant user permissions.

**Why it's correct:**
- ✔️ "**Enable OS Login for all VMs**" matches "**manage the Linux account lifecycle**".
- ✔️ "**Use IAM roles to grant user permissions**" matches "**simplify access management while minimizing operational costs**".

📌 **When to use it:** Use it when many people need logins to many machines and you want to control it from one place.
🏢 **Office example:** Staff badges control which rooms open; HR changes the list in one system.

### ❌ B
> **B.** Require your developers to create public SSH keys. Write custom startup scripts to update user permissions.

**Wrong words:**
- ❌ "**custom startup scripts to update user permissions**": code to maintain.

📌 **When to use it:** **Avoid** — OS Login does this.
🏢 **Office example:** Writing a new door-lock script for every hire.

### ❌ C
> **C.** Require your developers to create public SSH keys. Make the owner of the public key the root user.

**Wrong words:**
- ❌ "**Make the owner of the public key the root user**": everyone gets full admin power. Insecure.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Giving every developer the master key.

### ❌ D
> **D.** Enable OS Login for all VMs. Write custom startup scripts to update user permissions.

**Wrong words:**
- ✔️ OS Login is right.
- ❌ "**custom startup scripts**": unnecessary; IAM handles permissions.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Badge system plus hand-written lists.

---

## 🛒 E-Commerce Full-Stack Example

Developers: `roles/compute.osLogin`; SRE leads: `roles/compute.osAdminLogin`.

---

## 🧠 Key Takeaways / Memory Tips

- **Linux account lifecycle → OS Login + IAM roles.**
  🧠 *"**IAM decides who logs in.**"*
- Related: **Q294**, **Q323**.

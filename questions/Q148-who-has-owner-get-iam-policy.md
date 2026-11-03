# Q148: Who Has the Project Owner Role? (gcloud projects get-iam-policy)

**Topic:** IAM (viewing IAM policies)

## ❓ Question
> A colleague handed over a Google Cloud Platform project for you to maintain. As part of a security checkup, you want to review who has been granted the Project Owner role. What should you do?
>
> **A.** In the console, validate which SSH keys have been stored as project-wide keys.
>
> **B.** Navigate to Identity-Aware Proxy and check the permissions for these resources.
>
> **C.** Enable Audit Logs on the IAM & admin page for all resources, and validate the results.
>
> **D.** Use the command gcloud projects get-iam-policy to view the current role assignments.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** See **who currently has Owner** on the project.

**Clues in the question:**
- "**review who has been granted the Project Owner role**": the current answer is in the project's **IAM policy** → `gcloud projects get-iam-policy` (or the IAM page).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. IAM policy 🔑
- **What it is:** The list of **role → members** bindings on a resource.
- **Looks like:** `gcloud projects get-iam-policy shopnow-prod --flatten=bindings --filter=bindings.role:roles/owner --format='value(bindings.members)'`
- **Not to be confused with:** audit logs (history).
- **Analogy:** 📋 Today's **door access list**.
- **In the online store:** Who's Owner of shopnow-prod.

### 2. Project-wide SSH keys
- **What it is:** SSH keys in project metadata that let people log in to VMs. They're unrelated to IAM roles.
- **Looks like:** `ssh-keys` metadata
- **Not to be confused with:** IAM roles.
- **Analogy:** 🔑 Physical keys to the rooms, not the org chart.
- **In the online store:** Old keys to clean up.

### 🔗 How they fit together
```
 gcloud projects get-iam-policy shopnow-prod
   roles/owner → user:alice@…, user:bob@… ✅ current owners
```

---

## 🌍 Real-World Scenario

A new maintainer takes over a project and runs `gcloud projects get-iam-policy` to list everyone with `roles/owner`, then removes accounts that no longer need it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In the console, validate which SSH keys have been stored as project-wide keys.

**Wrong words:**
- ❌ "**SSH keys … stored as project-wide keys**": SSH keys give VM logins. They don't tell you who has IAM roles.

📌 **When to use it:** Use it to audit who can SSH into VMs with metadata keys.
🏢 **Office example:** Counting room keys to find out who the managers are.

### ❌ B
> **B.** Navigate to Identity-Aware Proxy and check the permissions for these resources.

**Wrong words:**
- ❌ "**Identity-Aware Proxy**": IAP permissions control access to specific apps or VMs through IAP, not project roles.

📌 **When to use it:** Use it to review who can reach apps through IAP.
🏢 **Office example:** Checking the guest list for one meeting room.

### ❌ C
> **C.** Enable Audit Logs on the IAM & admin page for all resources, and validate the results.

**Wrong words:**
- ❌ "**Enable Audit Logs … and validate**": logs show **future** activity. Admin Activity logs are already on, and they show history, not today's list of owners.

📌 **When to use it:** Use audit logs to see when roles were changed (Q095).
🏢 **Office example:** Starting a logbook today to learn who the managers already are.

### ✅ D
> **D.** Use the command gcloud projects get-iam-policy to view the current role assignments.

**Why it's correct:**
- ✔️ "**gcloud projects get-iam-policy**" matches "**review who has been granted the Project Owner role**": it prints the current role bindings, including `roles/owner`.
- ✔️ "**current role assignments**" matches "**security checkup**".

📌 **When to use it:** Use it when you need the current list of who can do what.
🏢 **Office example:** Reading today's door access list at the front desk.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects get-iam-policy shopnow-prod --flatten="bindings[].members" \
  --filter="bindings.role:roles/owner" --format="table(bindings.members)"
# user:old-contractor@gmail.com  ← remove!
```

---

## 🧠 Key Takeaways / Memory Tips

- **Who has a role now → get-iam-policy (or the IAM page).** When it changed → audit logs.
  🧠 *"**Who has it now? Read the policy.**"*
- Related: **Q095** (when roles were added), **Q034** (roles).

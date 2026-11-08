# Q326: Service Account Best Practices (Single-Purpose Service Accounts + Manage Them as Resources)

**Topic:** IAM (service account best practices)

## ❓ Question
> You need to create and manage service accounts for your workloads running on Google Cloud. You want to follow Google-recommended practices. What should you do? (Choose two.)
>
> **A.** Create as few service accounts as possible.
>
> **B.** Delete any unused service accounts immediately.
>
> **C.** Create single-purpose service accounts.
>
> **D.** Manage service accounts as resources.
>
> **E.** Use random names for the service accounts.

**My answer:** — (didn't know)
**Correct answer:** C, D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You create and manage service accounts (non-human identities for programs) for your workloads.
- **What you must achieve:** Follow Google's recommended practices.
- **The limits:** Choose two.
- **What they're really asking:** Which two service account practices does Google recommend?

**Clues in the question:**
- Google's guide: **create single-purpose service accounts** and **manage service accounts as resources** (like VMs — documented, owned, lifecycle-managed).
- Unused accounts should be **disabled first**, then deleted later — not deleted immediately.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Single-purpose service account 🔑
- **What it is:** One service account per app/task, so permissions stay narrow and audits are clear.
- **Looks like:** `checkout-sa`, `image-resizer-sa`, `reports-sa`
- **Not to be confused with:** one shared SA for everything.
- **Analogy:** 🪪 One badge per job role.
- **In the online store:** ShopNow per-service SAs.

### 2. Manage service accounts as resources
- **What it is:** Treat SAs as infrastructure: naming conventions, descriptions, owners, IaC, and lifecycle (create, rotate, disable, delete).
- **Looks like:** Terraform `google_service_account` with description and labels
- **Not to be confused with:** treating them like user accounts.
- **Analogy:** 📦 Inventory items with tags.
- **In the online store:** —

### 🔗 How they fit together
```
 ✅ one SA per purpose   ✅ managed like resources
 ❌ few shared SAs   ❌ delete immediately   ❌ random names
```

---

## 🌍 Real-World Scenario

A platform team creates a dedicated SA per service and manages them in Terraform with clear names and owners.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create as few service accounts as possible.

**Wrong words:**
- ❌ "**as few service accounts as possible**": shared SAs collect too many permissions.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** One badge for the whole company.

### ❌ B
> **B.** Delete any unused service accounts immediately.

**Wrong words:**
- ❌ "**Delete … immediately**": something might still use it; best practice is **disable first**, then delete.

📌 **When to use it:** Use it after you've disabled and confirmed nothing breaks.
🏢 **Office example:** Shredding a badge before checking if anyone still uses it.

### ✅ C
> **C.** Create single-purpose service accounts.

**Why it's correct:**
- ✔️ "**single-purpose service accounts**" matches "**Google-recommended practices**" (least privilege, clear audit).

📌 **When to use it:** Use it when each program should have its own identity and only its own permissions.
🏢 **Office example:** Each job role gets its own badge.

### ✅ D
> **D.** Manage service accounts as resources.

**Why it's correct:**
- ✔️ "**Manage service accounts as resources**" matches "**create and manage service accounts**" per Google guidance.

📌 **When to use it:** Use it when you want accounts tracked with owners, names and a full lifecycle.
🏢 **Office example:** Badges listed in the inventory with an owner and expiry.

### ❌ E
> **E.** Use random names for the service accounts.

**Wrong words:**
- ❌ "**random names**": hard to know what each does; use clear naming conventions.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Badges labeled with random codes.

---

## 🛒 E-Commerce Full-Stack Example

`checkout-sa`, `orders-worker-sa`, `reports-sa`, each in Terraform with description + owner label.

---

## 🧠 Key Takeaways / Memory Tips

- **SA best practices: one per purpose, managed as resources, clear names, disable before delete.**
  🧠 *"**One job, one badge, tracked like stock.**"*
- Related: **Q369**, **Q297**.

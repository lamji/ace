# Q366: Manage Multiple Applications Independently in Terraform (Root Directory per Application)

**Topic:** Infrastructure as Code (Terraform structure)

## ❓ Question
> You are planning to manage all of your Google Cloud resources by using Terraform. You have multiple applications that you want to manage independently of each other. You need to structure your Terraform code repository to facilitate this separation. What should you do?
>
> **A.** Create a single module for each resource type, and place all modules in the same directory.
>
> **B.** Put the Terraform configuration resources for each application in its own root directory.
>
> **C.** Create a single module for each application, and place all modules in the same directory.
>
> **D.** Put resources of the same type in their own root directory.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will manage all Google Cloud resources with Terraform, and you have several apps.
- **What you must achieve:** Manage each app separately from the others.
- **The limits:** None stated.
- **What they're really asking:** How should you structure the Terraform code repository?

**Clues in the question:**
- Independent management = separate **state** → a **root directory (root module) per application**.

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Root module / root directory 🔑
- **What it is:** The directory where you run `terraform apply`; each has its own state.
- **Looks like:** `apps/shop/`, `apps/blog/`, `apps/payments/` each with `main.tf` + backend
- **Not to be confused with:** shared module (reusable code).
- **Analogy:** 📁 Separate project folder per client.
- **In the online store:** —

### 🔗 How they fit together
```
 repo/
  ├ shop/     (own state) ✅
  ├ payments/ (own state) ✅
  └ modules/  (shared building blocks)
```

---

## 🌍 Real-World Scenario

Each app gets its own **root directory** and state, so changing one never touches another.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a single module for each resource type, and place all modules in the same directory.

**Wrong words:**
- ❌ "**module for each resource type … same directory**": one root; apps not separated.

📌 **When to use it:** Use type modules as building blocks.
🏢 **Office example:** Sorting files by paper type instead of client.

### ✅ B
> **B.** Put the Terraform configuration resources for each application in its own root directory.

**Why it's correct:**
- ✔️ "**configuration resources for each application in its own root directory**" matches "**manage independently of each other**" + "**facilitate this separation**".

📌 **When to use it:** Use it when several projects must be changed without affecting each other.
🏢 **Office example:** A separate folder per client, so updating one never mixes papers.

### ❌ C
> **C.** Create a single module for each application, and place all modules in the same directory.

**Wrong words:**
- ❌ "**all modules in the same directory**": still one root and state for all apps.

📌 **When to use it:** Use app modules inside separate roots.
🏢 **Office example:** Client folders stuffed in one binder.

### ❌ D
> **D.** Put resources of the same type in their own root directory.

**Wrong words:**
- ❌ "**same type in their own root directory**": an app spans several roots; not independent.

📌 **When to use it:** **Avoid** for app separation.
🏢 **Office example:** Filing by paper type.

---

## 🛒 E-Commerce Full-Stack Example

`infra/storefront/`, `infra/payments/`, `infra/analytics/` each with their own gcs backend prefix.

---

## 🧠 Key Takeaways / Memory Tips

- **Independent apps → separate root directories (separate state).**
  🧠 *"**One app, one root, one state.**"*
- Related: **Q341**, **Q318**.

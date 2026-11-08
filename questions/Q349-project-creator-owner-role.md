# Q349: Find Who Created Manually Made Projects (Check the Owner Role on the IAM Page)

**Topic:** Resource Manager / IAM

## ❓ Question
> You are responsible for Google Cloud governance at your company and recently implemented a new, automated process for provisioning Google Cloud projects. You have discovered several projects that were manually created before the implementation of this new process. You need to identify the creators of these projects to inform them of the new process. What should you do?
>
> **A.** Review the value of the creator label attached to the project to find the project’s creator.
>
> **B.** Use Resource Manager to identify the responsible department from the folder and project hierarchy.
>
> **C.** Review the Cloud Billing account linked to the project, and then contact the owner of that billing account.
>
> **D.** Use the IAM page in the Google Cloud console to identify the user with the Owner role.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **D**: the project creator automatically gets the **Owner** role. Caveat: owners can change later; the most reliable source is the **Admin Activity audit log** (`CreateProject` entry). A (creator label) only works if someone added that label; it's not automatic.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You introduced an automated process for creating projects, but some projects were made by hand before it existed.
- **What you must achieve:** Find who created those older projects so you can tell them about the new process.
- **The limits:** None stated.
- **What they're really asking:** Where can you see who created a project?

**Clues in the question:**
- When a user creates a project, they're automatically granted **Owner** → check the IAM page.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Project creator → Owner 🔑
- **What it is:** The account that creates a project gets `roles/owner` on it by default.
- **Looks like:** IAM page: `ana@shopnow.com — Owner`
- **Not to be confused with:** labels (only if someone set them).
- **Analogy:** 🏠 The person who signed the lease gets the keys.
- **In the online store:** —

### 🔗 How they fit together
```
 project IAM page → Owner = likely creator ✅ (audit logs = definitive)
```

---

## 🌍 Real-World Scenario

Governance checks each old project's **Owner** on the IAM page and emails them about the new process.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Review the value of the creator label attached to the project to find the project’s creator.

**Wrong words:**
- ❌ "**creator label**": not added automatically; may not exist.

📌 **When to use it:** Use labels if your process sets them.
🏢 **Office example:** Looking for a name tag nobody wrote.

### ❌ B
> **B.** Use Resource Manager to identify the responsible department from the folder and project hierarchy.

**Wrong words:**
- ❌ "**responsible department from the folder**": gives a department, not the person.

📌 **When to use it:** Use the hierarchy to see ownership by team.
🏢 **Office example:** Knowing the floor, not the person.

### ❌ C
> **C.** Review the Cloud Billing account linked to the project, and then contact the owner of that billing account.

**Wrong words:**
- ❌ "**owner of that billing account**": the billing owner may not have created the project.

📌 **When to use it:** Use it for billing questions.
🏢 **Office example:** Asking the accountant who rented the room.

### ✅ D
> **D.** Use the IAM page in the Google Cloud console to identify the user with the Owner role.

**Why it's correct:**
- ✔️ "**IAM page … user with the Owner role**" matches "**identify the creators of these projects**": creators get Owner automatically.

📌 **When to use it:** Use it when you need to know who set something up and they were given the main keys when they did.
🏢 **Office example:** Checking who holds the original lease keys to find who rented the office.

---

## 🛒 E-Commerce Full-Stack Example

Project `old-promo-2023` IAM shows `ben@shopnow.com — Owner` → email Ben.

---

## 🧠 Key Takeaways / Memory Tips

- **Project creator gets Owner automatically. Definitive: audit log CreateProject.**
  🧠 *"**Creator = first Owner.**"*
- Related: —

# Q194: Group Resources That Share Common IAM Policies (Folders)

**Topic:** Resource hierarchy (folders, IAM inheritance)

## ❓ Question
> You have been asked to set up the billing configuration for a new Google Cloud customer. Your customer wants to group resources that share common IAM policies. What should you do?
>
> **A.** Use labels to group resources that share common IAM policies.
>
> **B.** Use folders to group resources that share common IAM policies.
>
> **C.** Set up a proper billing account structure to group IAM policies.
>
> **D.** Set up a proper project naming structure to group IAM policies.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Group resources that should have the **same IAM policies**.

**Clues in the question:**
- "**group resources that share common IAM policies**" → **folders**. A policy set on a folder is **inherited** by every project inside.

**Exam topic:** Resource hierarchy.

---

## 📚 Key Terms Explained

### 1. Folder 🔑
- **What it is:** A container for projects (and other folders) in an organization. IAM policies set on it **flow down** to everything inside.
- **Looks like:** Org → Folder "Finance" → projects fin-prod, fin-dev
- **Not to be confused with:** a label.
- **Analogy:** 📁 A department drawer; whoever has the drawer key opens every file inside.
- **In the online store:** Folder "ShopNow-Prod".

### 2. Label
- **What it is:** A key/value tag for **filtering and billing**. Doesn't carry IAM.
- **Looks like:** `env=prod`
- **Not to be confused with:** folder.
- **Analogy:** 🏷️ A sticky tag.
- **In the online store:** Cost by team.

### 🔗 How they fit together
```
 Org
  └─ Folder Finance  (IAM: finance-team = viewer) ✅
       ├─ fin-prod   inherits
       └─ fin-dev    inherits
```

---

## 🌍 Real-World Scenario

A new customer has many teams. The admin creates **folders** per department and grants roles on each folder once, so all projects inside inherit them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use labels to group resources that share common IAM policies.

**Wrong words:**
- ❌ "**labels**": labels are for filtering and cost reports. They don't hold IAM policies.

📌 **When to use it:** Use labels to tag resources for cost tracking.
🏢 **Office example:** Color stickers on files; they don't lock anything.

### ✅ B
> **B.** Use folders to group resources that share common IAM policies.

**Why it's correct:**
- ✔️ "**Use folders to group resources**" matches "**group resources**".
- ✔️ Folders pass IAM down to everything inside, which matches "**share common IAM policies**".

📌 **When to use it:** Use it when several groups of work should share the same access rules.
🏢 **Office example:** A department drawer: give someone the drawer key and they can open every file inside.

### ❌ C
> **C.** Set up a proper billing account structure to group IAM policies.

**Wrong words:**
- ❌ "**billing account structure to group IAM policies**": billing accounts decide who pays, not who has access to projects.

📌 **When to use it:** Use billing accounts to separate payments.
🏢 **Office example:** Splitting invoices doesn't change who has office keys.

### ❌ D
> **D.** Set up a proper project naming structure to group IAM policies.

**Wrong words:**
- ❌ "**project naming structure**": names don't carry IAM.

📌 **When to use it:** Use naming conventions for readability.
🏢 **Office example:** Naming files neatly doesn't lock the cabinet.

---

## 🛒 E-Commerce Full-Stack Example

Org `shopnow.com` → folders `Prod`, `Dev`. `group:sre@` = Compute Admin on `Prod` folder → inherited by all prod projects.

---

## 🧠 Key Takeaways / Memory Tips

- **Shared IAM → folders (inheritance).** Labels = tags for cost/filtering.
  🧠 *"**Folders hold permissions; labels hold notes.**"*
- Related: **Q204**, **Q107**.

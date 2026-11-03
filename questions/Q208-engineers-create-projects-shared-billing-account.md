# Q208: Engineers Create Projects Without Their Own Credit Cards (One Billing Account + Billing Account User for Creators)

**Topic:** Billing (billing account permissions)

## ❓ Question
> You are working for a startup that was officially registered as a business 6 months ago. As your customer base grows, your use of Google Cloud increases. You want to allow all engineers to create new projects without asking them for their credit card information. What should you do?
>
> **A.** Create a Billing account, associate a payment method with it, and provide all project creators with permission to associate that billing account with their projects.
>
> **B.** Grant all engineers permission to create their own billing accounts for each new project.
>
> **C.** Apply for monthly invoiced billing, and have a single invoice for the project paid by the finance team.
>
> **D.** Create a billing account, associate it with a monthly purchase order (PO), and send the PO to Google Cloud.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **A**. The "6 months ago" clue rules out C: monthly invoiced billing normally requires a business that has been registered for about a year and meets spending thresholds.

---

## 📖 What the Question Is Asking

**In plain words:** Engineers should create projects **without their own cards**.

**Clues in the question:**
- "**without asking them for their credit card**" → one company **billing account** with a payment method, and give creators **Billing Account User** so they can link projects to it.
- "**registered … 6 months ago**" → too young for **invoiced billing**.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Billing Account User 🔑
- **What it is:** `roles/billing.user`: lets a person **link projects** to a billing account, without seeing or changing payment details.
- **Looks like:** `gcloud billing accounts add-iam-policy-binding ACCT --member=group:eng@ --role=roles/billing.user`
- **Not to be confused with:** Billing Admin.
- **Analogy:** 💳 Permission to charge to the company card, without holding the card.
- **In the online store:** Engineers spin up test projects.

### 2. Invoiced billing
- **What it is:** Monthly invoice paid by bank transfer, for established businesses that qualify.
- **Looks like:** —
- **Not to be confused with:** credit card billing.
- **Analogy:** 🧾 Monthly statement.
- **In the online store:** —

### 🔗 How they fit together
```
 billing account (company card) ─ Billing Account User → group:engineers ✅
 engineer creates project → links to company account
```

---

## 🌍 Real-World Scenario

A young startup sets up one **billing account** on the company card and grants the engineers group **Billing Account User**. Anyone can start a project, and charges go to the company.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a Billing account, associate a payment method with it, and provide all project creators with permission to associate that billing account with their projects.

**Why it's correct:**
- ✔️ "**Create a Billing account, associate a payment method with it**" matches "**without asking them for their credit card**": the company pays.
- ✔️ "**provide all project creators with permission to associate that billing account with their projects**" matches "**allow all engineers to create new projects**".

📌 **When to use it:** Use it when staff need to start new work that the company pays for, without using personal money.
🏢 **Office example:** Letting staff charge expenses to the company account without handing them the company card.

### ❌ B
> **B.** Grant all engineers permission to create their own billing accounts for each new project.

**Wrong words:**
- ❌ "**create their own billing accounts**": each would need a payment method, which means their own cards.

📌 **When to use it:** **Never use this** for company work.
🏢 **Office example:** Asking every employee to open their own bank account to pay for office supplies.

### ❌ C
> **C.** Apply for monthly invoiced billing, and have a single invoice for the project paid by the finance team.

**Wrong words:**
- ❌ "**Apply for monthly invoiced billing**": a 6-month-old business usually doesn't qualify.
- ❌ "**single invoice for the project**": doesn't give engineers permission to create projects.

📌 **When to use it:** Use it once the company is established and eligible.
🏢 **Office example:** Applying for a corporate credit line too early.

### ❌ D
> **D.** Create a billing account, associate it with a monthly purchase order (PO), and send the PO to Google Cloud.

**Wrong words:**
- ❌ "**monthly purchase order (PO)**": POs are part of invoiced billing, and still don't grant engineers permissions.

📌 **When to use it:** Use POs when your finance process requires them on invoices.
🏢 **Office example:** Paperwork that doesn't solve who can spend.

---

## 🛒 E-Commerce Full-Stack Example

Billing account `ShopNow Main` (company card) → `group:engineering@shopnow.com` = `roles/billing.user` + `roles/resourcemanager.projectCreator` on the Dev folder.

---

## 🧠 Key Takeaways / Memory Tips

- **Let people create billed projects → one billing account + Billing Account User (+ Project Creator).**
  🧠 *"**Company card, staff can charge.**"*
- Related: **Q164**, **Q197**.

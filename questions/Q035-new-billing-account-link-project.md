# Q035: Create a New Billing Account and Link an Existing Project

**Topic:** Billing (billing accounts, linking projects, Project Billing Manager vs Billing Account Administrator vs Billing Account Creator)

## ❓ Question
> You need to create a new billing account and then link it with an existing Google Cloud Platform project. What should you do?
>
> **A.** Verify that you are Project Billing Manager for the GCP project. Update the existing project to link it to the existing billing account.
>
> **B.** Verify that you are Project Billing Manager for the GCP project. Create a new billing account and link the new billing account to the existing project.
>
> **C.** Verify that you are Billing Administrator for the billing account. Create a new project and link the new project to the existing billing account.
>
> **D.** Verify that you are Billing Administrator for the billing account. Update the existing project to link it to the existing billing account.

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You need a new billing account.
- **What you must achieve:** Create it and link an existing project to it.
- **The limits:** None stated.
- **What they're really asking:** What are the steps to create a billing account and link the project?

| Keyword | What it hints at |
|---|---|
| "**create a new billing account**" | Any option that uses the **existing** billing account (A, C, D) is out |
| "**existing** … project" | Don't create a new project (C is out) |
| "**link it with**" a project | Changing which billing account a project uses needs permission **on the project**: **Project Billing Manager** (or Owner) |

**Exam topic:** Billing.

> 💡 **Fastest method:** Read the task words and cross out options. Only **B** says *new billing account* **and** *existing project*. The other three get one of those wrong.

---

## 📚 Key Terms Explained

### 1️⃣ Billing Account (review from Q007)
- **What it is:** The **payment profile** that pays for Google Cloud usage: a **credit card or invoice setup** with an ID. Projects are **linked** to it, and their costs land there.
- **Looks like:** `ShopNow Marketing Card · 01A2B3-C4D5E6-F7G8H9`
- **Not to be confused with:** a project. A billing account **pays**. A project **holds resources**. One billing account can pay for **many projects**, and each project has **one** billing account at a time.
- **Analogy:** 💳 The **company credit card**. Each department (project) is told which card to charge.
- **In the online store:** `shopnow-prod` charges the main company card.

### 2️⃣ Linking a Project to a Billing Account
- **What it is:** Telling a project **which billing account pays for it**. You can **switch** it later.
- **Looks like:** `gcloud billing projects link shopnow-marketing --billing-account=01A2B3-C4D5E6-F7G8H9`
- **Not to be confused with:** moving resources. Linking only changes **who pays**. Nothing inside the project moves or stops.
- **Analogy:** 🧾 Telling accounting: "Charge the Marketing department's expenses to **this** card from now on."

### 3️⃣ Project Billing Manager (`roles/billing.projectManager`) 🔑
- **What it is:** A role **on the project** that lets you **link or unlink** that project to a billing account. It **can't** see invoices or spend.
- **Looks like:** `user:maria@shopnow.com → roles/billing.projectManager (on project shopnow-marketing)`
- **Not to be confused with:** Billing Account Administrator. This role is about **the project's side** of the link.
- **Analogy:** 🗂️ The **department head** who can say "charge our expenses to card X".

### 4️⃣ Billing Account Administrator (`roles/billing.admin`)
- **What it is:** A role **on a billing account** to **manage that account**: payment methods, budgets, reports, who can use it.
- **Looks like:** `user:finance-lead@shopnow.com → roles/billing.admin (on billing account 01A2B3-…)`
- **Not to be confused with:** being able to **create** billing accounts. Admin manages an account that **already exists**.
- **Analogy:** 💼 The **finance manager** who controls one company card.

### 5️⃣ Billing Account Creator (`roles/billing.creator`) (exam detail)
- **What it is:** The role that allows **creating new** billing accounts. It's granted at the **organization** level. (In an org, it's usually given to the finance team. Without an organization, any user can create one.)
- **Not to be confused with:** Project Billing Manager. The exam's option B focuses on the **linking** permission, so you don't need to name this role.
- **Analogy:** 🏦 Permission to **open a new company card** with the bank.

### 🔗 How They Fit Together
```
① Create NEW billing account     (needs: Billing Account Creator, or no org)
      💳 "ShopNow Marketing Card" 01A2B3-…
             │  you become its Billing Account Administrator automatically
             ▼
② Link EXISTING project           (needs: Project Billing Manager / Owner on the project
      📁 shopnow-marketing               + permission to use the billing account)
             │
             ▼
   Marketing's costs now go to the new card ✅

A, D → link to the EXISTING account ❌ (no new account)
C    → creates a NEW project          ❌ (project should be existing)
```

---

## 🌍 Real-World Scenario

Finance wants a department's cloud spend **on its own card or invoice**: a new team, a client project billed separately, a startup grant, or a budget split between business units. The cloud engineer **creates a new billing account** and **re-links the existing project** to it. Nothing in the project changes, only **who pays**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Verify that you are Project Billing Manager for the GCP project. Update the existing project to link it to the existing billing account.

**Why it's wrong:**
- ✔️ Right role, right project…
- ❌ …but it links to the **existing** billing account. The task says **create a new** one.

**📌 When to use it:** Use it when a project should start charging a card the company already has.
🏢 **Office example:** A department head telling accounting to charge their expenses to an existing company card.

### ✅ B (your answer)
> **B.** Verify that you are Project Billing Manager for the GCP project. Create a new billing account and link the new billing account to the existing project.

**Why it's correct:**
- ✔️ **Creates a new billing account**, which is task 1.
- ✔️ **Links it to the existing project**, which is task 2.
- ✔️ **Project Billing Manager** is the role that allows changing a project's billing link.

**📌 When to use it:** Use it when a project that already exists needs its own new way of paying.
🏢 **Office example:** Opening a new company card for the Marketing department and telling accounting to charge Marketing's expenses to it.

### ❌ C
> **C.** Verify that you are Billing Administrator for the billing account. Create a new project and link the new project to the existing billing account.

**Why it's wrong:**
- ❌ **Backwards**: it creates a **new project** and uses the **existing** billing account. The task wants a **new billing account** and the **existing project**.

**📌 When to use it:** Use it when you're starting a brand-new project that should charge a card you already have.
🏢 **Office example:** Setting up a new department and telling it to use the company's existing card.

### ❌ D
> **D.** Verify that you are Billing Administrator for the billing account. Update the existing project to link it to the existing billing account.

**Why it's wrong:**
- ❌ **No new billing account** is created.
- ❌ Billing Administrator manages the **billing account**. Changing the **project's** link also needs permission on the **project**.

**📌 When to use it:** Use Billing Administrator to manage an existing payment account: cards, budgets, reports.
🏢 **Office example:** The finance manager updating the expiry date and spending limit on an existing company card.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **marketing site** runs in the existing project **`shopnow-marketing`**, currently charged to the main company card. Finance wants marketing on **its own card** to track the campaign budget.

```bash
# ① New billing account: created in the Console
#    Billing → Manage billing accounts → Create account → "ShopNow Marketing Card"
#    → ID 01A2B3-C4D5E6-F7G8H9

# ② Link the EXISTING project to it (you're Project Billing Manager on shopnow-marketing)
gcloud billing projects link shopnow-marketing \
  --billing-account=01A2B3-C4D5E6-F7G8H9

# Check it
gcloud billing projects describe shopnow-marketing
# billingAccountName: billingAccounts/01A2B3-C4D5E6-F7G8H9
# billingEnabled: true
```

| Project | Before | After |
|---|---|---|
| `shopnow-prod` | Main company card | Main company card |
| `shopnow-marketing` | Main company card | **ShopNow Marketing Card** ✅ |

The marketing site keeps running with **no downtime**. Only the invoice changes.

---

## 🧠 Key Takeaways / Memory Tips

- **Read the task words: "NEW billing account" + "EXISTING project" → only B matches both.**
  🧠 *"**Match the nouns:** new/existing account, new/existing project. Cross out every option that swaps them."*
- **Project Billing Manager** = link/unlink a **project** to billing. **Billing Account Administrator** = manage the **billing account** itself. **Billing Account Creator** = create **new** billing accounts.
- Linking changes **who pays**, not what runs.
- Related: **Q007** (create a billing account and link projects).

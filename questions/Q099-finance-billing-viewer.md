# Q099: Finance Must See Billing Reports Without Extra Project Permissions (Billing Account Viewer)

**Topic:** Billing / IAM (billing roles: viewer, user, admin, project manager)

## ❓ Question
> Your finance team wants to view the billing report for your projects. You want to make sure that the finance team does not get additional permissions to the project. What should you do?
>
> **A.** Add the group for the finance team to roles/billing user role.
>
> **B.** Add the group for the finance team to roles/billing admin role.
>
> **C.** Add the group for the finance team to roles/billing viewer role.
>
> **D.** Add the group for the finance team to roles/billing project/Manager role.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The finance team wants to see billing reports for your projects.
- **What you must achieve:** Let them see those reports.
- **The limits:** They must not get any extra permissions on the projects.
- **What they're really asking:** Which role lets them see billing without being able to touch projects?

**Clues in the question:**
- "**view the billing report**": read-only billing → **Billing Account Viewer** (`roles/billing.viewer`).
- "**does not get additional permissions**": least privilege. No linking projects, no changing billing.

**Exam topic:** Billing / IAM.

---

## 📚 Key Terms Explained

### 1️⃣ Billing roles 🔑 (review from Q059, Q088)
- **Billing Account Viewer** (`roles/billing.viewer`): **see** costs, reports and invoices. Read-only.
- **Billing Account User** (`roles/billing.user`): **link projects** to the billing account.
- **Billing Account Administrator** (`roles/billing.admin`): **manage everything** on the billing account (users, budgets, payment, linking).
- **Project Billing Manager** (`roles/billing.projectManager`): **link/unlink a project** to a billing account.
- **Looks like:** `gcloud billing accounts add-iam-policy-binding 01AB23-CD45EF-678901 --member=group:finance@shopnow.com --role=roles/billing.viewer`
- **Not to be confused with:** project roles like Viewer, which see the project's resources, not the bill.
- **Analogy:** 🧾 Viewer = can **read** the expense reports. User/Manager = can **add** departments to the company card. Admin = **runs** the company card.
- **In the online store:** ShopNow's accountants read monthly costs per project.

### 2️⃣ Google group
- **What it is:** A **named list of email addresses**. Granting a role to the group gives it to everyone on the list. Nobody logs in as the group.
- **Looks like:** `finance@shopnow.com = [ana@shopnow.com, ben@shopnow.com]`

### 🔗 How they fit together
```
 Billing account
   roles/billing.viewer         → 👀 read reports ✅ (finance)
   roles/billing.user           → 🔗 link projects ❌ extra
   roles/billing.projectManager → 🔗 link/unlink a project ❌ extra
   roles/billing.admin          → 🔑 everything ❌ way too much
```

---

## 🌍 Real-World Scenario

Every month, finance reviews cloud costs by project. The admin adds the `finance@` group to **Billing Account Viewer** on the billing account. Finance opens **Billing → Reports** and sees the costs, but can't change anything or touch project resources.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add the group for the finance team to roles/billing user role.

**Wrong words:**
- ❌ "**roles/billing user**": it lets finance **link projects** to the billing account, an extra permission they don't need.

📌 **When to use it:** Use it for someone who must attach new projects to the company billing account.
🏢 **Office example:** Letting accountants add new departments to the company credit card, when they only needed to read statements.

### ❌ B
> **B.** Add the group for the finance team to roles/billing admin role.

**Wrong words:**
- ❌ "**roles/billing admin**": full control of the billing account (users, budgets, payment, linking). Far more than "view".

📌 **When to use it:** Use it for the one or two people who manage the billing account.
🏢 **Office example:** Handing the accountants control of the company credit card itself.

### ✅ C
> **C.** Add the group for the finance team to roles/billing viewer role.

**Why it's correct:**
- ✔️ "**roles/billing viewer**" matches "**view the billing report**": it gives read access to costs and reports.
- ✔️ "**viewer**" (read-only) matches "**does not get additional permissions to the project**": finance can't change billing or touch project resources.
- ✔️ "**the group for the finance team**" matches "**Your finance team**": one grant covers everyone on the team.

📌 **When to use it:** Use it when someone only needs to read the bills.
🏢 **Office example:** Giving accountants read-only access to the monthly expense statements.

### ❌ D
> **D.** Add the group for the finance team to roles/billing project/Manager role.

**Wrong words:**
- ❌ "**roles/billing project/Manager**": it lets finance **link and unlink projects** to billing accounts, an extra permission on the projects.

📌 **When to use it:** Use it for someone who must move a project from one billing account to another.
🏢 **Office example:** Letting accountants switch which company card a department uses.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud billing accounts add-iam-policy-binding 01AB23-CD45EF-678901 \
  --member=group:finance@shopnow.com --role=roles/billing.viewer
```
ShopNow's accountants open **Billing → Reports**, group by project, and see that `shopnow-prod` cost $8,200 in October. They can't link projects, change payment, or touch any VM.

---

## 🧠 Key Takeaways / Memory Tips

- **Only view billing → Billing Account Viewer (`roles/billing.viewer`).**
- User / Project Manager = link projects. Admin = everything.
  🧠 *"**Read the bill → billing viewer.**"*
- Related: **Q059** (finance links projects), **Q088** (budget alerts), **Q066** (one billing account).

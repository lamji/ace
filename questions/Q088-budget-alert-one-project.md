# Q088: Budget Alert for Compute Engine in One of Three Projects (Billing Admin + Project-Scoped Budget)

**Topic:** Billing (budgets and alerts, budget scope, billing roles)

## ❓ Question
> You need to set a budget alert for use of Compute Engineer services on one of the three Google Cloud Platform projects that you manage. All three projects are linked to a single billing account. What should you do?
>
> **A.** Verify that you are the project billing administrator. Select the associated billing account and create a budget and alert for the appropriate project.
>
> **B.** Verify that you are the project billing administrator. Select the associated billing account and create a budget and a custom alert.
>
> **C.** Verify that you are the project administrator. Select the associated billing account and create a budget for the appropriate project.
>
> **D.** Verify that you are project administrator. Select the associated billing account and create a budget and a custom alert.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Three projects share one billing account.
- **What you must achieve:** Set a budget alert for Compute Engine spending on just one of those projects.
- **The limits:** None stated.
- **What they're really asking:** How do you limit the budget alert to that one project and service?

**Clues in the question:**
- "**budget alert**": budgets are created on the **billing account**, so you need a **billing** role (Billing Account Administrator or Costs Manager), not a project role.
- "**one of the three … projects**" + "**linked to a single billing account**": the budget must be **scoped to that one project**, otherwise it would count all three.
- "**alert**": the answer must include **both** a budget **and** an alert.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1️⃣ Budget and budget alert 🔑
- **What it is:** A **spending target** set on a billing account, with **alert thresholds** (e.g., email at 50%, 90%, 100%). It can be **scoped** to certain projects and services. It warns you; it doesn't stop spending.
- **Looks like:** `gcloud billing budgets create --billing-account=0X0X0X-0X0X0X-0X0X0X --display-name="prod compute" --budget-amount=1000USD --filter-projects=projects/shopnow-prod --threshold-rule=percent=0.9`
- **Not to be confused with:** a quota or a spending cap.
- **Analogy:** 💰 A **monthly department budget** where accounting emails you when you've spent 90%.
- **In the online store:** Alert when `shopnow-prod` Compute Engine spend nears $1,000.

### 2️⃣ Billing Account Administrator ("billing administrator")
- **What it is:** A **billing role** that manages the billing account: link projects, view costs, and **create budgets**. (Billing Account Costs Manager can also create budgets.)
- **Looks like:** `roles/billing.admin` on the billing account
- **Not to be confused with:** Project Owner/Administrator, which controls the project's resources, not the billing account.
- **Analogy:** 🧾 The **finance manager**, who sets the department budgets.

### 3️⃣ Budget scope
- **What it is:** The **filter** on a budget: which projects, services (e.g., Compute Engine), and labels count toward it.
- **Not to be confused with:** the whole billing account. Without a scope, all three projects count.

### 🔗 How they fit together
```
 Billing account (one) ── paid by Billing Admin ✅
   ├── project A
   ├── project B   ← budget scope: project B + service Compute Engine
   └── project C      thresholds: 50% / 90% / 100% → email alerts ✅
```

---

## 🌍 Real-World Scenario

Finance worries that the production project's VMs might overspend. The billing administrator opens **Billing → Budgets & alerts**, creates a budget, scopes it to the production project and the Compute Engine service, and sets alerts at 50%, 90% and 100%. The team gets emails before costs get out of hand.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Verify that you are the project billing administrator. Select the associated billing account and create a budget and alert for the appropriate project.

**Why it's correct:**
- ✔️ "**Verify that you are the project billing administrator**" matches "**All three projects are linked to a single billing account**": budgets live on the billing account, so you need a billing role.
- ✔️ "**create a budget and alert**" matches "**set a budget alert**": the option includes both the budget and the alert.
- ✔️ "**for the appropriate project**" matches "**on one of the three Google Cloud Platform projects**": the budget is scoped to just that one project.

📌 **When to use it:** Use it when one department's spending needs a warning, and the bills for all departments go to one account.
🏢 **Office example:** The finance manager sets a budget for the IT department only and gets an email when it's 90% spent.

### ❌ B
> **B.** Verify that you are the project billing administrator. Select the associated billing account and create a budget and a custom alert.

**Wrong words:**
- ✔️ "project billing administrator" and "create a budget" are right.
- ❌ "**create a budget and a custom alert**": it never says **which project**, so the budget would cover **all three** projects on the billing account.

📌 **When to use it:** Use it when you want one budget for everything on the billing account.
🏢 **Office example:** Setting one budget for the whole company when you only wanted to watch IT.

### ❌ C
> **C.** Verify that you are the project administrator. Select the associated billing account and create a budget for the appropriate project.

**Wrong words:**
- ❌ "**Verify that you are the project administrator**": project admin roles don't let you create budgets on the billing account.
- ❌ "**create a budget**" (no alert): the question asks for a budget **alert**.
- ✔️ "for the appropriate project" is right.

📌 **When to use it:** Be project administrator when you need to manage the project's servers and settings.
🏢 **Office example:** The IT manager trying to set the IT budget. That's finance's job.

### ❌ D
> **D.** Verify that you are project administrator. Select the associated billing account and create a budget and a custom alert.

**Wrong words:**
- ❌ "**Verify that you are project administrator**": wrong role (see C).
- ❌ "**create a budget and a custom alert**": no project scope (see B).

📌 **When to use it:** **Never use this.** Use A.
🏢 **Office example:** The wrong person setting a company-wide budget when only one department needed one.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow has `shopnow-dev`, `shopnow-staging` and `shopnow-prod`, all on one billing account. Finance wants a warning when prod's Compute Engine costs near $1,000.

```bash
gcloud billing budgets create --billing-account=01AB23-CD45EF-678901 \
  --display-name="prod compute" --budget-amount=1000USD \
  --filter-projects=projects/shopnow-prod \
  --filter-services=services/6F81-5844-456A \
  --threshold-rule=percent=0.5 --threshold-rule=percent=0.9 --threshold-rule=percent=1.0
```
(`6F81-5844-456A` is the Compute Engine service ID.) At $900, the billing admins get an email.

---

## 🧠 Key Takeaways / Memory Tips

- **Budgets are made on the billing account → you need a billing role** (Billing Account Administrator / Costs Manager), not project admin.
- **"One project" → scope the budget to that project.**
- Budgets **alert**; they don't stop spending.
  🧠 *"**Money rules? Billing role. One project? Scope it.**"*
- Related: **Q059** (billing roles for finance), **Q066** (one billing account for many projects).

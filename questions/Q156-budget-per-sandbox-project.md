# Q156: Alert if Any Developer's Sandbox Spends Over $500 (One Budget per Project)

**Topic:** Billing (budgets per project, alerts)

## ❓ Question
> You are the team lead of a group of 10 developers. You provided each developer with an individual Google Cloud Project that they can use as their personal sandbox to experiment with different Google Cloud solutions. You want to be notified if any of the developers are spending above $500 per month on their sandbox environment. What should you do?
>
> **A.** Create a single budget for all projects and configure budget alerts on this budget.
>
> **B.** Create a separate billing account per sandbox project and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per billing account.
>
> **C.** Create a budget per project and configure budget alerts on all of these budgets.
>
> **D.** Create a single billing account for all sandbox projects and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per project.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You lead 10 developers, and each has a personal sandbox project for experiments.
- **What you must achieve:** Get notified if any developer spends more than $500 a month in their sandbox.
- **The limits:** The limit applies to each developer's project separately.
- **What they're really asking:** How do you set up a $500-per-month alert for each sandbox?

**Clues in the question:**
- "**any of the developers … above $500**": the limit is **per project** → **one budget per project**, each at $500.
- "**be notified**": budget **alerts**, not a dashboard you must watch.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Budget per project 🔑 (review from Q088)
- **What it is:** A budget scoped to **one project**, with alert thresholds that email you.
- **Looks like:** `gcloud billing budgets create --display-name=dev-ana --budget-amount=500USD --filter-projects=projects/sbx-ana --threshold-rule=percent=1.0`
- **Not to be confused with:** one shared budget.
- **Analogy:** 💰 A spending limit on **each employee's card**.
- **In the online store:** One per sandbox.

### 2. Dashboard
- **What it is:** Charts you have to look at. They don't notify anyone.
- **Looks like:** Data Studio report
- **Not to be confused with:** alerts.
- **Analogy:** 📊 A chart on the wall.
- **In the online store:** Monthly cost review.

### 🔗 How they fit together
```
 sbx-ana   budget $500 → alert ✅
 sbx-ben   budget $500 → alert ✅
 … ×10 (one per project)
```

---

## 🌍 Real-World Scenario

A team lead gives 10 developers sandbox projects. They create **10 budgets** of $500, each scoped to one project and emailing the lead at 100%. When Ben's GPU experiment hits $500, the lead knows right away.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a single budget for all projects and configure budget alerts on this budget.

**Wrong words:**
- ❌ "**single budget for all projects**": it alerts on the **total** ($500 across everyone), not when **one** developer passes $500.

📌 **When to use it:** Use one budget when you care about the team's total.
🏢 **Office example:** One spending limit on the whole team's combined cards.

### ❌ B
> **B.** Create a separate billing account per sandbox project and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per billing account.

**Wrong words:**
- ❌ "**separate billing account per sandbox project**": far too much admin.
- ❌ "**Data Studio dashboard**": it doesn't notify you.

📌 **When to use it:** Use separate billing accounts when different companies pay.
🏢 **Office example:** Opening 10 bank accounts and then staring at a chart.

### ✅ C
> **C.** Create a budget per project and configure budget alerts on all of these budgets.

**Why it's correct:**
- ✔️ "**budget per project**" matches "**any of the developers … above $500**": each sandbox is tracked on its own.
- ✔️ "**configure budget alerts**" matches "**be notified**".

📌 **When to use it:** Use it when each person has their own limit and you want a warning when anyone passes theirs.
🏢 **Office example:** A spending limit on each employee's company card, with a text when anyone hits it.

### ❌ D
> **D.** Create a single billing account for all sandbox projects and enable BigQuery billing exports. Create a Data Studio dashboard to plot the spending per project.

**Wrong words:**
- ✔️ A single billing account is fine.
- ❌ "**Data Studio dashboard**": shows spending, but you aren't notified.

📌 **When to use it:** Use dashboards for regular cost reviews.
🏢 **Office example:** A wall chart nobody checks at night.

---

## 🛒 E-Commerce Full-Stack Example

```bash
for dev in ana ben cara; do
  gcloud billing budgets create --billing-account=01AB23-CD45EF-678901 --display-name="sbx-$dev" \
    --budget-amount=500USD --filter-projects=projects/shopnow-sbx-$dev --threshold-rule=percent=1.0
done
```

---

## 🧠 Key Takeaways / Memory Tips

- **Per-project limit → one budget per project with alerts.**
- Dashboards don't notify.
  🧠 *"**Each sandbox gets its own budget.**"*
- Related: **Q088**, **Q125**.

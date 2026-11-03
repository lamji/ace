# Q229: One Cost View Across Several Billing Accounts, Updated Fast (Billing Export to BigQuery + Looker Studio)

**Topic:** Billing (billing export)

## ❓ Question
> You created several resources in multiple Google Cloud projects. All projects are linked to different billing accounts. To better estimate future charges, you want to have a single visual representation of all costs incurred. You want to include new cost data as soon as possible. What should you do?
>
> **A.** Fill all resources in the Pricing Calculator to get an estimate of the monthly cost.
>
> **B.** Use the Reports view in the Cloud Billing Console to view the desired cost information.
>
> **C.** Visit the Cost Table page to get a CSV export and visualize it using Looker Studio.
>
> **D.** Configure Billing Data Export to BigQuery and visualize the data in Looker Studio.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Same as Q141, with Looker Studio.

**Clues in the question:**
- "**different billing accounts**" + "**single visual representation**" + "**as soon as possible**" → export all accounts to **BigQuery**, chart in **Looker Studio**.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Billing export to BigQuery 🔑 (review from Q201)
- **What it is:** Automatic cost feed into BigQuery.
- **Looks like:** —
- **Not to be confused with:** CSV.
- **Analogy:** 📥 Automatic receipt feed.
- **In the online store:** —

### 🔗 How they fit together
```
 billing acct 1 ┐
 billing acct 2 ├─► BigQuery ─► Looker Studio (one view) ✅
 billing acct 3 ┘
```

---

## 🌍 Real-World Scenario

An engineer with projects on three billing accounts exports all of them to one BigQuery dataset and builds one **Looker Studio** dashboard.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Fill all resources in the Pricing Calculator to get an estimate of the monthly cost.

**Wrong words:**
- ❌ "**Pricing Calculator**": estimates; doesn't show actual costs incurred.

📌 **When to use it:** Use it before building something, to estimate cost.
🏢 **Office example:** Guessing next month's bills instead of reading them.

### ❌ B
> **B.** Use the Reports view in the Cloud Billing Console to view the desired cost information.

**Wrong words:**
- ❌ "**Reports view**": one billing account at a time, not one combined view.

📌 **When to use it:** Use it for a quick look at one account.
🏢 **Office example:** Reading one bank statement at a time.

### ❌ C
> **C.** Visit the Cost Table page to get a CSV export and visualize it using Looker Studio.

**Wrong words:**
- ❌ "**CSV export**": manual, not "as soon as possible".

📌 **When to use it:** Use it for a one-off report.
🏢 **Office example:** Photocopying statements by hand.

### ✅ D
> **D.** Configure Billing Data Export to BigQuery and visualize the data in Looker Studio.

**Why it's correct:**
- ✔️ "**Billing Data Export to BigQuery**" matches "**include new cost data as soon as possible**" + "**different billing accounts**".
- ✔️ "**visualize the data in Looker Studio**" matches "**single visual representation of all costs**".

📌 **When to use it:** Use it when you want all spending in one always-current chart.
🏢 **Office example:** Every account's receipts automatically copied into one spreadsheet with one chart.

---

## 🛒 E-Commerce Full-Stack Example

Billing exports from 3 accounts → dataset `billing_all` → Looker Studio "All Cloud Spend".

---

## 🧠 Key Takeaways / Memory Tips

- **Several billing accounts, one fresh view → BigQuery export + Looker Studio.**
  🧠 *"**Many accounts, one BigQuery.**"*
- Related: **Q141**, **Q201**.

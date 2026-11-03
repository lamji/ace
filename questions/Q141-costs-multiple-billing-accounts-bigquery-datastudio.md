# Q141: One Cost View Across Several Billing Accounts, Updated Fast (Billing Export to BigQuery + Data Studio)

**Topic:** Billing (billing export to BigQuery, Looker Studio / Data Studio, billing reports)

## ❓ Question
> You created several resources in multiple Google Cloud projects. All projects are linked to different billing accounts. To better estimate future charges, you want to have a single visual representation of all costs incurred. You want to include new cost data as soon as possible. What should you do?
>
> **A.** Configure Billing Data Export to BigQuery and visualize the data in Data Studio.
>
> **B.** Visit the Cost Table page to get a CSV export and visualize it using Data Studio.
>
> **C.** Fill all resources in the Pricing Calculator to get an estimate of the monthly cost.
>
> **D.** Use the Reports view in the Cloud Billing Console to view the desired cost information.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Several projects on **different billing accounts**. You want **one chart** of all costs, with new data showing up **quickly**.

**Clues in the question:**
- "**different billing accounts**": the Billing Reports page shows **one billing account at a time**.
- "**single visual representation**": export every account into **BigQuery** and build one **Data Studio (Looker Studio)** dashboard.
- "**as soon as possible**": billing export updates **automatically through the day**, unlike a manual CSV.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Billing export to BigQuery 🔑 (review from Q125)
- **What it is:** Automatically and continuously copies detailed cost data from a billing account into a BigQuery dataset. Several accounts can export to the same dataset.
- **Looks like:** Billing → Billing export → BigQuery export → dataset `all_billing`
- **Not to be confused with:** a one-time CSV.
- **Analogy:** 🧾 Every bill line copied into one searchable spreadsheet, all day long.
- **In the online store:** All ShopNow accounts → `finance.all_billing`.

### 2. Data Studio (Looker Studio)
- **What it is:** Google's free **dashboard/report tool** that reads from BigQuery and other sources.
- **Looks like:** Bar chart: cost by billing account by month
- **Not to be confused with:** BigQuery.
- **Analogy:** 📊 A wall chart that redraws itself from the spreadsheet.
- **In the online store:** CFO's cost dashboard.

### 🔗 How they fit together
```
 billing account 1 ┐
 billing account 2 ├─► BigQuery (billing export, auto-updated) ─► Data Studio dashboard ✅ one view
 billing account 3 ┘
```

---

## 🌍 Real-World Scenario

After an acquisition, a company has three billing accounts. Finance wants one live chart. Each account's **billing export** goes to the same BigQuery dataset, and a **Data Studio** report charts the combined costs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Configure Billing Data Export to BigQuery and visualize the data in Data Studio.

**Why it's correct:**
- ✔️ "**Billing Data Export to BigQuery**" matches "**include new cost data as soon as possible**": the export updates automatically during the day.
- ✔️ Exporting all accounts into BigQuery matches "**different billing accounts**": the data is combined in one place.
- ✔️ "**visualize the data in Data Studio**" matches "**single visual representation of all costs**".

📌 **When to use it:** Use it when you need one live picture of spending from several separate accounts.
🏢 **Office example:** Every branch's bills flow into one spreadsheet, and a wall chart updates itself from it.

### ❌ B
> **B.** Visit the Cost Table page to get a CSV export and visualize it using Data Studio.

**Wrong words:**
- ❌ "**Cost Table page to get a CSV export**": a manual, one-off download per account, so new data isn't included automatically.

📌 **When to use it:** Use a CSV export for a one-time report.
🏢 **Office example:** Photocopying each branch's bill by hand once a month.

### ❌ C
> **C.** Fill all resources in the Pricing Calculator to get an estimate of the monthly cost.

**Wrong words:**
- ❌ "**Pricing Calculator**": it estimates prices you type in, not costs actually incurred.

📌 **When to use it:** Use it to estimate before building (Q126).
🏢 **Office example:** A quote calculator instead of real receipts.

### ❌ D
> **D.** Use the Reports view in the Cloud Billing Console to view the desired cost information.

**Wrong words:**
- ❌ "**Reports view in the Cloud Billing Console**": it shows one billing account at a time, not one combined view.

📌 **When to use it:** Use it to look at one billing account's costs.
🏢 **Office example:** Reading each branch's statement separately.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow (account 01AB…) and its acquired brand (account 02CD…) both export to `shopnow-finance.billing_all`. A Data Studio report shows "cost by brand, by service, this month" and refreshes during the day.

---

## 🧠 Key Takeaways / Memory Tips

- **Combine costs from multiple billing accounts → export to BigQuery → Data Studio.**
- Billing Reports = one account.
  🧠 *"**Many accounts, one dashboard: export and chart.**"*
- Related: **Q125** (billing export), **Q126** (calculator), **Q088**.

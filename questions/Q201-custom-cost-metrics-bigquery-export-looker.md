# Q201: Automated Cost Visuals With Company-Specific Calculated Metrics (Billing Export to BigQuery + Looker Studio)

**Topic:** Billing (billing export, Looker Studio)

## ❓ Question
> Your company has multiple projects linked to a single billing account in Google Cloud. You need to visualize the costs with specific metrics that should be dynamically calculated based on company-specific criteria. You want to automate the process. What should you do?
>
> **A.** In the Google Cloud console, visualize the costs related to the projects in the Reports section.
>
> **B.** In the Google Cloud console, visualize the costs related to the projects in the Cost breakdown section.
>
> **C.** In the Google Cloud console, use the export functionality of the Cost table. Create a Looker Studio dashboard on top of the CSV export.
>
> **D.** Configure Cloud Billing data export to BigQuery for the billing account. Create a Looker Studio dashboard on top of the BigQuery export.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Costs with **your own calculated metrics**, updated **automatically**.

**Clues in the question:**
- "**dynamically calculated based on company-specific criteria**" → you need **SQL** on the raw cost data → **BigQuery export**.
- "**automate the process**" → the export updates by itself; a CSV download doesn't.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Cloud Billing export to BigQuery 🔑 (review from Q141)
- **What it is:** Automatically writes detailed cost rows into a BigQuery dataset throughout the day.
- **Looks like:** table `gcp_billing_export_v1_XXXX`
- **Not to be confused with:** CSV download.
- **Analogy:** 📥 A feed that copies every receipt into your ledger automatically.
- **In the online store:** Cost per order.

### 2. Looker Studio
- **What it is:** Free dashboard tool (formerly Data Studio) that can chart BigQuery queries, including calculated fields.
- **Looks like:** calculated field `cost / orders`
- **Not to be confused with:** Cost Reports page.
- **Analogy:** 📊 Your own wall chart.
- **In the online store:** Finance dashboard.

### 🔗 How they fit together
```
 billing account ─auto export─► BigQuery (SQL: your metrics) ─► Looker Studio ✅
```

---

## 🌍 Real-World Scenario

Finance wants "cloud cost per customer order" by business unit. The admin turns on **billing export to BigQuery**, writes a view joining cost and order counts, and builds a **Looker Studio** dashboard on it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In the Google Cloud console, visualize the costs related to the projects in the Reports section.

**Wrong words:**
- ❌ "**Reports section**": fixed built-in charts. You can't add company-specific calculated metrics.

📌 **When to use it:** Use Reports for a quick look at spending trends.
🏢 **Office example:** The bank's standard statement view.

### ❌ B
> **B.** In the Google Cloud console, visualize the costs related to the projects in the Cost breakdown section.

**Wrong words:**
- ❌ "**Cost breakdown section**": also fixed. No custom calculations.

📌 **When to use it:** Use it to see how credits and discounts affect totals.
🏢 **Office example:** Another standard statement page.

### ❌ C
> **C.** In the Google Cloud console, use the export functionality of the Cost table. Create a Looker Studio dashboard on top of the CSV export.

**Wrong words:**
- ❌ "**export functionality of the Cost table … CSV**": manual downloads aren't automated.

📌 **When to use it:** Use a CSV export for a one-off report.
🏢 **Office example:** Photocopying the statement by hand each month.

### ✅ D
> **D.** Configure Cloud Billing data export to BigQuery for the billing account. Create a Looker Studio dashboard on top of the BigQuery export.

**Why it's correct:**
- ✔️ "**Cloud Billing data export to BigQuery**" matches "**automate the process**": data flows in by itself.
- ✔️ "**Looker Studio dashboard on top of the BigQuery export**" matches "**specific metrics … dynamically calculated based on company-specific criteria**": SQL and calculated fields.

📌 **When to use it:** Use it when the finance team needs its own up-to-date spending numbers, not just the standard views.
🏢 **Office example:** Having every receipt copied automatically into your own spreadsheet with your own formulas and charts.

---

## 🛒 E-Commerce Full-Stack Example

BigQuery view `cost_per_order` = billing export ⨝ `orders_daily`; Looker Studio chart "Cloud $ per order" refreshes automatically.

---

## 🧠 Key Takeaways / Memory Tips

- **Custom cost metrics + automated → billing export to BigQuery + Looker Studio.**
  🧠 *"**Your own math? Export to BigQuery.**"*
- Related: **Q141**, **Q229**.

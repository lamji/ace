# Q321: Detailed Cost Analysis With Multiple Visualizations on One Dashboard (Billing Export to BigQuery + Looker Studio)

**Topic:** Billing (export, Looker Studio)

## ❓ Question
> Your company runs a variety of applications and workloads on Google Cloud, and you are responsible for managing cloud costs. You need to identify a solution that enables you to perform detailed cost analysis. You also must be able to visualize the cost data in multiple ways on the same dashboard. What should you do?
>
> **A.** Use the cost breakdown report with the available filters from Cloud Billing to visualize the data.
>
> **B.** Enable the Cloud Billing export to BigQuery, and use Looker Studio to visualize the data.
>
> **C.** Run queries in Cloud Monitoring. Create dashboards to visualize the billing metrics.
>
> **D.** Enable Cloud Monitoring metrics export to BigQuery, and use Looker to visualize the data.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Detailed** cost analysis + **many chart types on one dashboard**.

**Clues in the question:**
- "**detailed cost analysis**" → **billing export to BigQuery**.
- "**visualize … in multiple ways on the same dashboard**" → **Looker Studio** on that dataset.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Looker Studio 🔑
- **What it is:** Google's free dashboard tool; connects to BigQuery and builds charts, tables, filters on one page.
- **Looks like:** Data source: `billing_export.gcp_billing_export_v1_*` → bar chart by project + pie by service
- **Not to be confused with:** the Billing console report (fixed views).
- **Analogy:** 📈 A custom wall of charts.
- **In the online store:** ShopNow FinOps dashboard.

### 🔗 How they fit together
```
 billing → BigQuery export → Looker Studio dashboard ✅
```

---

## 🌍 Real-World Scenario

FinOps exports billing to **BigQuery** and builds a **Looker Studio** dashboard with trends, top SKUs and per-team splits.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the cost breakdown report with the available filters from Cloud Billing to visualize the data.

**Wrong words:**
- ❌ "**cost breakdown report with the available filters**": fixed report views; not a custom multi-chart dashboard.

📌 **When to use it:** Use built-in reports for quick checks.
🏢 **Office example:** The bank's standard statement.

### ✅ B
> **B.** Enable the Cloud Billing export to BigQuery, and use Looker Studio to visualize the data.

**Why it's correct:**
- ✔️ "**Cloud Billing export to BigQuery**" matches "**perform detailed cost analysis**".
- ✔️ "**Looker Studio to visualize**" matches "**visualize the cost data in multiple ways on the same dashboard**".

📌 **When to use it:** Use it when you want to slice your spending many ways and see several charts on one screen.
🏢 **Office example:** Copy every receipt into a spreadsheet, then build a wall of charts from it.

### ❌ C
> **C.** Run queries in Cloud Monitoring. Create dashboards to visualize the billing metrics.

**Wrong words:**
- ❌ "**queries in Cloud Monitoring … billing metrics**": Monitoring doesn't hold detailed billing data.

📌 **When to use it:** Use Monitoring for performance metrics.
🏢 **Office example:** Checking the thermostat for your expenses.

### ❌ D
> **D.** Enable Cloud Monitoring metrics export to BigQuery, and use Looker to visualize the data.

**Wrong words:**
- ❌ "**Cloud Monitoring metrics export**": performance metrics, not costs.

📌 **When to use it:** Use it for long-term metric analysis.
🏢 **Office example:** Exporting temperature logs to study spending.

---

## 🛒 E-Commerce Full-Stack Example

Looker Studio `ShopNow Cloud Costs` on `shopnow-finops.billing_export`.

---

## 🧠 Key Takeaways / Memory Tips

- **Detailed cost analysis + custom dashboard → billing export to BigQuery + Looker Studio.**
  🧠 *"**Export, then visualize.**"*
- Related: **Q309**, **Q353**.

# Q335: Teams Get Spend Notifications and Build Dashboards From Detailed Billing Data (Budget Alerts + Billing Export to BigQuery)

**Topic:** Billing (budgets, export)

## ❓ Question
> Your company is closely monitoring their cloud spend. You need to allow different teams to monitor their Google Cloud costs. You must ensure that team members receive notifications when their cloud spend reaches certain thresholds and give team members the ability to create dashboards for additional insights with detailed billing data. You want to follow Google-recommended practices and minimize engineering costs. What should you do?
>
> **A.** Deploy Grafana to Compute Engine. Create a dashboard for each team that uses the data from the Cloud Billing API. Ask each team to create their own alerts in Cloud Monitoring.
>
> **B.** Set up alerts for each team based on required thresholds. Create a shell script to read data from the Cloud Billing API, and push the results to BigQuery. Grant team members access to BigQuery.
>
> **C.** Deploy Grafana to Compute Engine. Create a dashboard for each team that uses the data from the Cloud Billing Budget API. Ask each team to create their own alerts in Grafana.
>
> **D.** Set up alerts for each team based on required thresholds. Set up billing exports to BigQuery. Grant team members access to BigQuery.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Teams need **threshold notifications** and **dashboards on detailed billing data**, low engineering.

**Clues in the question:**
- Notifications → **budget alerts**.
- Detailed data for dashboards → **billing export to BigQuery** (no custom scripts).

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Budget alerts + billing export 🔑 (review)
- **What it is:** Budgets notify at thresholds; export puts detailed costs in BigQuery for any dashboard tool.
- **Looks like:** —
- **Not to be confused with:** Cloud Billing API scripts.
- **Analogy:** 🔔 + 📊
- **In the online store:** —

### 🔗 How they fit together
```
 budgets → email/PubSub   +   export → BigQuery → dashboards ✅
```

---

## 🌍 Real-World Scenario

Each team gets a budget alert, and all teams can build Looker Studio dashboards on the BigQuery export.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy Grafana to Compute Engine. Create a dashboard for each team that uses the data from the Cloud Billing API. Ask each team to create their own alerts in Cloud Monitoring.

**Wrong words:**
- ❌ "**Deploy Grafana to Compute Engine … Cloud Billing API**": servers and custom work; the Billing API doesn't give detailed usage costs.

📌 **When to use it:** Use Grafana if you already run it.
🏢 **Office example:** Building your own chart office.

### ❌ B
> **B.** Set up alerts for each team based on required thresholds. Create a shell script to read data from the Cloud Billing API, and push the results to BigQuery. Grant team members access to BigQuery.

**Wrong words:**
- ✔️ Alerts are right.
- ❌ "**shell script to read data from the Cloud Billing API**": custom code; export does this natively.

📌 **When to use it:** **Avoid** custom scripts here.
🏢 **Office example:** Copying receipts by hand.

### ❌ C
> **C.** Deploy Grafana to Compute Engine. Create a dashboard for each team that uses the data from the Cloud Billing Budget API. Ask each team to create their own alerts in Grafana.

**Wrong words:**
- ❌ "**Grafana … Budget API**": self-managed; Budget API has no detailed cost data.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** A homemade dashboard with little data.

### ✅ D
> **D.** Set up alerts for each team based on required thresholds. Set up billing exports to BigQuery. Grant team members access to BigQuery.

**Why it's correct:**
- ✔️ "**Set up alerts for each team based on required thresholds**" matches "**receive notifications when their cloud spend reaches certain thresholds**".
- ✔️ "**billing exports to BigQuery … Grant team members access**" matches "**create dashboards … with detailed billing data**" + "**minimize engineering costs**".

📌 **When to use it:** Use it when teams should be warned about spending and also dig into the numbers themselves.
🏢 **Office example:** Finance sends warnings at set amounts and shares a full spreadsheet of receipts.

---

## 🛒 E-Commerce Full-Stack Example

Budgets per team label; export `billing_export` with `roles/bigquery.dataViewer` for team groups.

---

## 🧠 Key Takeaways / Memory Tips

- **Alerts → budgets. Detailed analysis → billing export to BigQuery.**
  🧠 *"**Budgets warn, exports explain.**"*
- Related: **Q321**, **Q316**.

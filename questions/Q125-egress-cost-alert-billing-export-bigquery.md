# Q125: Email When One Server's Egress Costs Pass $100 (Billing Export to BigQuery + Scheduled Function)

**Topic:** Billing (billing export to BigQuery, budgets' limits, Cloud Functions, Cloud Scheduler)

## ❓ Question
> Your company publishes large files on an Apache web server that runs on a Compute Engine instance. The Apache web server is not the only application running in the project. You want to receive an email when the egress network costs for the server exceed 100 dollars for the current month as measured by Google Cloud. What should you do?
>
> **A.** Set up a budget alert on the project with an amount of 100 dollars, a threshold of 100%, and notification type of "email."
>
> **B.** Set up a budget alert on the billing account with an amount of 100 dollars, a threshold of 100%, and notification type of "email."
>
> **C.** Export the billing data to BigQuery. Create a Cloud Function that uses BigQuery to sum the egress network costs of the exported billing data for the Apache web server for the current month and sends an email if it is over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.
>
> **D.** Use the Cloud Logging Agent to export the Apache web server logs to Cloud Logging. Create a Cloud Function that uses BigQuery to parse the HTTP response log data in Cloud Logging for the current month and sends an email if the size of all HTTP responses, multiplied by current Google Cloud egress prices, totals over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You want an email when **only this one server's egress (outbound network) cost** passes **$100 this month**, **as Google bills it**. Other apps share the project.

**Clues in the question:**
- "**not the only application running in the project**": a project budget would include **everything**, not just this server's egress.
- "**egress network costs for the server**": you need cost **per resource and per SKU**, which the **detailed billing export to BigQuery** has.
- "**as measured by Google Cloud**": use Google's **billing data**, not your own estimate from web logs.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Billing export to BigQuery 🔑
- **What it is:** A setting that **copies detailed cost data** (per service, SKU, project, labels, and, with detailed export, per resource) into a BigQuery dataset throughout the day.
- **Looks like:** `SELECT SUM(cost) FROM billing.gcp_billing_export_resource_v1_XXXX WHERE sku.description LIKE '%Egress%' AND resource.name LIKE '%apache-1%'`
- **Not to be confused with:** a budget, which only looks at totals with simple filters.
- **Analogy:** 🧾 Getting **every line of the bill** in a spreadsheet you can search.
- **In the online store:** Finance analyzes ShopNow costs per service.

### 2. Egress
- **What it is:** Data **leaving** Google Cloud to the internet. Google charges per GB.
- **Looks like:** SKU `Network Internet Egress from Americas to Americas`
- **Not to be confused with:** ingress (incoming, usually free).
- **Analogy:** 📦 Postage for parcels you send out.
- **In the online store:** Customers downloading big product videos.

### 3. Cloud Scheduler + Cloud Function
- **What it is:** Scheduler = **cron in the cloud** (runs a job on a timetable). Function = a small piece of code that runs when called.
- **Looks like:** `gcloud scheduler jobs create http egress-check --schedule='0 * * * *' --uri=...`
- **Not to be confused with:** a budget alert.
- **Analogy:** ⏰ An alarm clock that wakes up a robot every hour.
- **In the online store:** Hourly cost check.

### 4. Budget alert (review from Q088)
- **What it is:** Alerts on **total** spend for chosen projects/services/labels. It can't isolate **one server's egress SKU** precisely.
- **Looks like:** `gcloud billing budgets create ...`
- **Not to be confused with:** a per-resource cost query.
- **Analogy:** 💰 An alert on the whole department's spend.
- **In the online store:** Total monthly budget for shopnow-prod.

### 🔗 How they fit together
```
 Billing export → BigQuery (per resource + SKU)
   Cloud Scheduler (hourly) → Cloud Function → SQL: SUM egress cost for apache-1 this month
     → if > $100 → send email ✅
```

---

## 🌍 Real-World Scenario

A media company hosts large downloads on one VM in a busy shared project. Finance wants a warning when that VM's internet egress costs pass $100. The engineer enables **detailed billing export to BigQuery** and writes a small **Cloud Function**, run **hourly by Cloud Scheduler**, that sums that VM's egress cost and emails the team when it's over $100.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Set up a budget alert on the project with an amount of 100 dollars, a threshold of 100%, and notification type of "email."

**Wrong words:**
- ❌ "**budget alert on the project**": it counts **all** costs in the project, including the other applications, not just this server's egress.

📌 **When to use it:** Use a project budget when the whole project's spending should be watched.
🏢 **Office example:** An alert on the whole department's spending when you only cared about one courier's postage.

### ❌ B
> **B.** Set up a budget alert on the billing account with an amount of 100 dollars, a threshold of 100%, and notification type of "email."

**Wrong words:**
- ❌ "**budget alert on the billing account**": even broader. It includes every project on the account.

📌 **When to use it:** Use it to watch the company's total cloud bill.
🏢 **Office example:** An alert on the entire company's spending.

### ✅ C
> **C.** Export the billing data to BigQuery. Create a Cloud Function that uses BigQuery to sum the egress network costs of the exported billing data for the Apache web server for the current month and sends an email if it is over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.

**Why it's correct:**
- ✔️ "**Export the billing data to BigQuery**" matches "**as measured by Google Cloud**": it's Google's own billing data.
- ✔️ "**sum the egress network costs … for the Apache web server**" matches "**egress network costs for the server**" + "**not the only application**": it isolates exactly that server's egress.
- ✔️ "**for the current month … sends an email if it is over 100 dollars**" matches "**receive an email when … exceed 100 dollars for the current month**".
- ✔️ "**Cloud Scheduler to run hourly**": the check runs automatically.

📌 **When to use it:** Use it when you need a warning about one specific cost line that a normal budget can't separate.
🏢 **Office example:** Searching the detailed bill every hour for one courier's postage and emailing finance when it passes $100.

### ❌ D
> **D.** Use the Cloud Logging Agent to export the Apache web server logs to Cloud Logging. Create a Cloud Function that uses BigQuery to parse the HTTP response log data in Cloud Logging for the current month and sends an email if the size of all HTTP responses, multiplied by current Google Cloud egress prices, totals over 100 dollars. Schedule the Cloud Function using Cloud Scheduler to run hourly.

**Wrong words:**
- ❌ "**size of all HTTP responses, multiplied by current Google Cloud egress prices**": your own estimate, not what Google actually bills (tiers, regions, free tiers differ).
- ❌ It also needs a logging agent and log parsing: more work, less accurate.

📌 **When to use it:** Use web logs to study traffic patterns, not to measure billed cost.
🏢 **Office example:** Estimating postage by weighing parcels yourself instead of reading the courier's bill.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow serves product videos from `media-1`. Billing export goes to `shopnow-finance.billing`.

```sql
SELECT SUM(cost) AS egress_usd
FROM `shopnow-finance.billing.gcp_billing_export_resource_v1_01AB23`
WHERE resource.name LIKE '%instances/media-1'
  AND sku.description LIKE '%Egress%'
  AND invoice.month = FORMAT_DATE('%Y%m', CURRENT_DATE())
```
Cloud Scheduler runs the function hourly. On Nov 19 it returns $101.40, and finance gets an email.

---

## 🧠 Key Takeaways / Memory Tips

- **Cost of one resource or one SKU → billing export to BigQuery + query** (scheduled function for alerts).
- Budgets cover whole projects or accounts.
- "As measured by Google Cloud" → billing data, not your own estimate.
  🧠 *"**Precise cost question? Ask the billing export.**"*
- Related: **Q088** (budget alerts), **Q096** (BigQuery cost control).

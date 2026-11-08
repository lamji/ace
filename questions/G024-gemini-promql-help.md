# G024: Write a PromQL Query for an Alert From a Plain-English Description (Gemini Cloud Assist in Cloud Monitoring)

**Topic:** Monitoring (Gemini Cloud Assist for Cloud Monitoring)
**Exam guide section:** 3.4 Monitoring and logging: Using Gemini Cloud Assist for Cloud Monitoring

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You want to create a Cloud Monitoring alert that fires when the 5-minute error rate of your checkout service exceeds 2% of requests. You are not familiar with PromQL. You want to produce the query quickly from a plain-language description and review it before saving the alerting policy. What should you do?
>
> **A.** Ask each developer to watch the dashboard and email you when errors look high.
>
> **B.** Create an uptime check on the checkout home page.
>
> **C.** Export metrics to BigQuery and write SQL instead of PromQL.
>
> **D.** In Cloud Monitoring, use Gemini Cloud Assist to generate the PromQL query from your description, review it, and use it in the alerting policy.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You want an alert (an automatic notification) when more than 2% of checkout requests fail over 5 minutes.
- **What you must achieve:** Write the PromQL query (the query language for metrics) that measures this, and save it in an alerting policy.
- **The limits:** You don't know PromQL well. You want to describe it in plain words and still review the query before saving.
- **What they're really asking:** Which Cloud Monitoring feature turns a plain description into a query?

**Clues in the question:**
- "**not familiar with PromQL**" + "**from a plain-language description**": Gemini Cloud Assist in Cloud Monitoring can **generate PromQL**.
- "**review it before saving the alerting policy**": you stay in control.

**Exam topic:** Monitoring (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Alerting policy
- **What it is:** A Cloud Monitoring rule: a condition (query + threshold + duration) and who to notify.
- **Looks like:** Condition: error ratio > 0.02 for 5 min → notify #oncall
- **Not to be confused with:** An uptime check, which tests whether a URL responds.
- **Analogy:** 🚨 A smoke alarm with a set sensitivity.
- **In the online store:** `checkout-error-rate`.

### 2. Gemini Cloud Assist in Cloud Monitoring 🔑
- **What it is:** AI help inside Cloud Monitoring that can write PromQL from natural language, explain charts and help build alerts.
- **Looks like:** "Error rate for service checkout over 5 minutes" → `sum(rate(http_requests_total{service="checkout",code=~"5.."}[5m])) / sum(rate(http_requests_total{service="checkout"}[5m]))`
- **Not to be confused with:** Writing the query yourself from scratch.
- **Analogy:** 🗣️ A translator who turns your sentence into the form's exact wording.
- **In the online store:** Creating the checkout error alert.

### 🔗 How they fit together
```
 "checkout 5xx rate over 5 min" ─► Gemini ─► PromQL ─► you review ─► alerting policy > 2% ✅
```

---

## 🌍 Real-World Scenario

A new SRE must add an error-rate alert before a sale. **Gemini Cloud Assist** in Cloud Monitoring drafts the PromQL from a sentence. The SRE checks it in the chart, sets the 2% threshold, and saves the policy.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ask each developer to watch the dashboard and email you when errors look high.

**Wrong words:**
- ❌ "**watch the dashboard and email you**": manual and unreliable, with no automatic alert.

📌 **When to use it:** Never rely on people watching charts for alerts.
🏢 **Office example:** Asking staff to sniff for smoke instead of installing an alarm.

### ❌ B
> **B.** Create an uptime check on the checkout home page.

**Wrong words:**
- ❌ "**uptime check on the checkout home page**": tells you if a page responds, not the share of failing requests.

📌 **When to use it:** Use uptime checks to know when a site stops answering.
🏢 **Office example:** Checking the door opens, not counting failed orders.

### ❌ C
> **C.** Export metrics to BigQuery and write SQL instead of PromQL.

**Wrong words:**
- ❌ "**Export metrics to BigQuery and write SQL**": not a live alert, and much more work.

📌 **When to use it:** Use BigQuery for long-term analysis.
🏢 **Office example:** Doing monthly reports when you need a smoke alarm.

### ✅ D
> **D.** In Cloud Monitoring, use Gemini Cloud Assist to generate the PromQL query from your description, review it, and use it in the alerting policy.

**Why it's correct:**
- ✔️ "**use Gemini Cloud Assist to generate the PromQL query from your description**" matches "**not familiar with PromQL**" and "**plain-language description**".
- ✔️ "**review it, and use it in the alerting policy**" matches "**review it before saving the alerting policy**".

📌 **When to use it:** Use it when you know what you want to measure but not how to write the query.
🏢 **Office example:** Telling an assistant what you need and checking the form they fill in before you sign.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** alert `checkout-error-rate`: generated PromQL (above) > 0.02 for 5 min → PagerDuty + #oncall.

---

## 🧠 Key Takeaways / Memory Tips

- **Need a metric query or alert but don't know PromQL → Gemini Cloud Assist in Cloud Monitoring, then review.**
  🧠 *"**Say it, Gemini writes PromQL.**"*
- Related: **G018**, **G023**, **Q239**.

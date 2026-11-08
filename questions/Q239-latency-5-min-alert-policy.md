# Q239: Notify Support if Latency Stays High for 5 Minutes, No Development (Cloud Monitoring Alert Policy)

**Topic:** Monitoring (alerting policies)

## ❓ Question
> You are responsible for a web application on Compute Engine. You want your support team to be notified automatically if users experience high latency for at least 5 minutes. You need a Google-recommended solution with no development cost. What should you do?
>
> **A.** Export Cloud Monitoring metrics to BigQuery and use a Looker Studio dashboard to monitor your web application's latency.
>
> **B.** Create an alert policy to send a notification when the HTTP response latency exceeds the specified threshold.
>
> **C.** Implement an App Engine service which invokes the Cloud Monitoring API and sends a notification in case of anomalies.
>
> **D.** Use the Cloud Monitoring dashboard to observe latency and take the necessary actions when the response latency exceeds the specified threshold.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You run a web app on Compute Engine.
- **What you must achieve:** Alert the support team automatically when users see high latency (slow responses) for at least 5 minutes.
- **The limits:** Google-recommended and no development cost.
- **What they're really asking:** How do you set up the alert without writing code?

**Clues in the question:**
- "**notified automatically**" + "**for at least 5 minutes**" → **alert policy** with a duration of 5 min.
- "**no development cost**" → built-in, not a custom app.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Alert policy 🔑 (review from Q172)
- **What it is:** Watches a metric and notifies when it crosses a threshold for a set **duration**.
- **Looks like:** condition: latency p95 > 1 s for 5 min → notify support@
- **Not to be confused with:** dashboards.
- **Analogy:** 🚨 A smoke alarm.
- **In the online store:** Checkout latency alert.

### 🔗 How they fit together
```
 latency metric > threshold for 5 min ─► alert policy ─► email/SMS support ✅
```

---

## 🌍 Real-World Scenario

Support wants a page if the site is slow for 5 minutes. The admin creates an **alert policy** on load balancer latency with a 5-minute window and a notification channel.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Export Cloud Monitoring metrics to BigQuery and use a Looker Studio dashboard to monitor your web application's latency.

**Wrong words:**
- ❌ "**Export … to BigQuery and use a Looker Studio dashboard**": a dashboard doesn't notify anyone.

📌 **When to use it:** Use it for long-term trend reports.
🏢 **Office example:** A wall chart nobody watches at night.

### ✅ B
> **B.** Create an alert policy to send a notification when the HTTP response latency exceeds the specified threshold.

**Why it's correct:**
- ✔️ "**alert policy to send a notification**" matches "**support team to be notified automatically**".
- ✔️ "**when the HTTP response latency exceeds the specified threshold**" matches "**high latency for at least 5 minutes**" (with a 5-minute duration).
- ✔️ Built in, which matches "**no development cost**".

📌 **When to use it:** Use it when someone should be told automatically the moment a problem lasts too long.
🏢 **Office example:** A smoke alarm that rings the support desk if smoke lasts five minutes.

### ❌ C
> **C.** Implement an App Engine service which invokes the Cloud Monitoring API and sends a notification in case of anomalies.

**Wrong words:**
- ❌ "**Implement an App Engine service**": custom development, against "**no development cost**".

📌 **When to use it:** Use custom code only if built-in alerts can't do it.
🏢 **Office example:** Building your own smoke alarm from parts.

### ❌ D
> **D.** Use the Cloud Monitoring dashboard to observe latency and take the necessary actions when the response latency exceeds the specified threshold.

**Wrong words:**
- ❌ "**observe latency and take the necessary actions**": someone has to watch. Not automatic.

📌 **When to use it:** Use dashboards for live viewing.
🏢 **Office example:** Staring at the smoke detector all day.

---

## 🛒 E-Commerce Full-Stack Example

Alert: `loadbalancing.googleapis.com/https/total_latencies` p95 > 1500 ms for 5 min → channel `support-oncall` (email + SMS).

---

## 🧠 Key Takeaways / Memory Tips

- **Automatic notification on a metric → Cloud Monitoring alert policy.**
  🧠 *"**Tell me automatically = alert policy.**"*
- Related: **Q172**, **Q187**.

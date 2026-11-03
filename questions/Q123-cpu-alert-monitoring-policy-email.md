# Q123: Email When CPU Stays Above 90% for 15 Minutes (Cloud Monitoring Alerting Policy)

**Topic:** Cloud Monitoring (workspaces/metrics scope, alerting policies, notification channels)

## ❓ Question
> You have a Compute Engine instance hosting a production application. You want to receive an email if the instance consumes more than 90% of its CPU resources for more than 15 minutes. You want to use Google services. What should you do?
>
> **A.** 1. Create a consumer Gmail account. 2. Write a script that monitors the CPU usage. 3. When the CPU usage exceeds the threshold, have that script send an email using the Gmail account and smtp.gmail.com on port 25 as SMTP server.
>
> **B.** 1. Create a Cloud Monitoring Workspace and associate your Google Cloud Platform (GCP) project with it. 2. Create a Cloud Monitoring Alerting Policy that uses the threshold as a trigger condition. 3. Configure your email address in the notification channel.
>
> **C.** 1. Create a Cloud Monitoring Workspace and associate your GCP project with it. 2. Write a script that monitors the CPU usage and sends it as a custom metric to Cloud Monitoring. 3. Create an uptime check for the instance in Cloud Monitoring.
>
> **D.** 1. In Cloud Logging, create a logs-based metric to extract the CPU usage by using this regular expression: CPU Usage: ([0-9] {1,3})% 2. In Cloud Monitoring, create an Alerting Policy based on this metric. 3. Configure your email address in the notification channel.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Send an **email** when the VM's **CPU > 90% for 15 minutes**, using Google services.

**Clues in the question:**
- "**more than 90% … for more than 15 minutes**": an **alerting policy** with a threshold condition and a 15-minute duration.
- "**receive an email**": an **email notification channel**.
- CPU usage is **already collected** by Cloud Monitoring for every VM, so no script is needed.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Alerting policy 🔑
- **What it is:** A Cloud Monitoring rule: **if a metric crosses a threshold for a duration → notify** someone.
- **Looks like:** Condition: `compute.googleapis.com/instance/cpu/utilization > 0.9 for 15 min` → notify email
- **Not to be confused with:** a dashboard.
- **Analogy:** 🚨 A **smoke alarm** that calls you if smoke lasts 15 minutes.
- **In the online store:** Alert on-call if checkout VMs run hot.

### 2. Notification channel
- **What it is:** Where alerts are sent: **email**, SMS, Slack, PagerDuty, webhook, Pub/Sub.
- **Looks like:** `ops@shopnow.com`
- **Not to be confused with:** the alert condition.
- **Analogy:** 📞 The number the alarm calls.
- **In the online store:** Ops email + Slack.

### 3. Workspace (now metrics scope)
- **What it is:** The container that lets Cloud Monitoring see one or more projects' metrics. Today every project has one automatically.
- **Looks like:** Monitoring → Settings → Metrics scope
- **Not to be confused with:** a project.
- **Analogy:** 🖥️ The control room's wall of screens.
- **In the online store:** ShopNow's ops project watches all shop projects.

### 4. Uptime check / logs-based metric
- **What it is:** Uptime check = **is the site responding?** Logs-based metric = a number counted from **log lines**. Neither is needed for CPU.
- **Looks like:** `uptime check https://shop.example.com` / `metric from log regex`
- **Not to be confused with:** the built-in CPU metric.
- **Analogy:** 🔔 A doorbell test / counting notes in the logbook.
- **In the online store:** Uptime checks on the storefront.

### 🔗 How they fit together
```
 VM CPU metric (built-in) → Alerting policy: > 90% for 15 min → Notification channel: email ✅
```

---

## 🌍 Real-World Scenario

An ops team wants to know when a production VM is overloaded. In **Cloud Monitoring → Alerting → Create policy**, they choose the VM CPU utilization metric, set threshold 90% for 15 minutes, and add their email channel. No custom code is needed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Create a consumer Gmail account. 2. Write a script that monitors the CPU usage. 3. When the CPU usage exceeds the threshold, have that script send an email using the Gmail account and smtp.gmail.com on port 25 as SMTP server.

**Wrong words:**
- ❌ "**Create a consumer Gmail account … Write a script**": homemade monitoring with a personal account.
- ❌ "**smtp.gmail.com on port 25**": Google Cloud blocks outbound port 25, so the email wouldn't even send.

📌 **When to use it:** **Never use this.** Use a Monitoring alerting policy (B).
🏢 **Office example:** Hiring someone to stare at the thermometer and post a letter.

### ✅ B
> **B.** 1. Create a Cloud Monitoring Workspace and associate your Google Cloud Platform (GCP) project with it. 2. Create a Cloud Monitoring Alerting Policy that uses the threshold as a trigger condition. 3. Configure your email address in the notification channel.

**Why it's correct:**
- ✔️ "**Create a Cloud Monitoring Workspace and associate your … project**" matches "**use Google services**": Monitoring watches the VM's built-in metrics.
- ✔️ "**Alerting Policy that uses the threshold as a trigger condition**" matches "**more than 90% of its CPU … for more than 15 minutes**": threshold 90%, duration 15 minutes.
- ✔️ "**email address in the notification channel**" matches "**receive an email**".

📌 **When to use it:** Use it when you want to be told automatically when something stays too high for too long.
🏢 **Office example:** A smoke alarm set to call the office manager if smoke lasts 15 minutes.

### ❌ C
> **C.** 1. Create a Cloud Monitoring Workspace and associate your GCP project with it. 2. Write a script that monitors the CPU usage and sends it as a custom metric to Cloud Monitoring. 3. Create an uptime check for the instance in Cloud Monitoring.

**Wrong words:**
- ❌ "**Write a script … custom metric**": CPU is already collected, so the script is unnecessary.
- ❌ "**uptime check**": it tests whether the site responds, not CPU, and sends no CPU email.

📌 **When to use it:** Use uptime checks to know when a website stops responding.
🏢 **Office example:** Ringing the doorbell to check the office temperature.

### ❌ D
> **D.** 1. In Cloud Logging, create a logs-based metric to extract the CPU usage by using this regular expression: CPU Usage: ([0-9] {1,3})% 2. In Cloud Monitoring, create an Alerting Policy based on this metric. 3. Configure your email address in the notification channel.

**Wrong words:**
- ❌ "**logs-based metric to extract the CPU usage by using this regular expression**": CPU isn't in logs by default, and parsing logs for a metric that already exists is backwards.

📌 **When to use it:** Use logs-based metrics to count things that only appear in logs, like "payment failed" lines.
🏢 **Office example:** Counting notes in the logbook to measure the room temperature.

---

## 🛒 E-Commerce Full-Stack Example

Cloud Monitoring → Alerting → Create policy:
- Metric: **VM Instance → CPU utilization**, filter `instance_name = checkout-1`
- Condition: **above 90%**, retest window **15 min**
- Notification channel: `oncall@shopnow.com`

On Black Friday at 18:05, CPU stays at 97% for 15 minutes, and on-call gets an email at 18:20.

---

## 🧠 Key Takeaways / Memory Tips

- **"Email when a metric is over X for Y minutes" → Monitoring alerting policy + email channel.**
- CPU is built in, so no scripts or log parsing are needed.
  🧠 *"**Threshold + duration + channel = alert.**"*
- Related: **Q067** (monitoring.viewer), **Q124** (alerts that trigger automation).

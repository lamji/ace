# Q371: Near-Real-Time Alert When MIG Average CPU > 75% for 5 Minutes (Monitoring Alerting Policy on cpu/utilization)

**Topic:** Monitoring (alerting policies)

## ❓ Question
> You manage a business-critical backend application running on a Compute Engine managed instance group (MIG). The operations team requires a near-real time notification if the average CPU utilization across all instances in the MIG exceeds 75% for a continuous five-minute period. You need to implement a scalable Google Cloud solution to meet this monitoring requirement. What should you do?
>
> **A.** Create a logs-based metric in Cloud Logging that filters for high CPU usage entries, and then create a Cloud Monitoring alert policy based on that custom metric.
>
> **B.** Deploy the Ops Agent to all Compute Engine VM instances to collect the CPU metric. Use a custom script running on a separate Compute Engine instance to poll this metric every five minutes, and send an email notification if the threshold is breached.
>
> **C.** Create a Cloud Monitoring alerting policy that targets the compute.googleapis.com/instance/cpu/utilization metric. Set the threshold to 75% and the duration to five minutes.
>
> **D.** Configure an autoscaling policy for the MIG to use a CPU utilization target of 75% for five minutes, and then enable a notification channel in the autoscaler settings.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A critical backend runs on a managed instance group.
- **What you must achieve:** Notify operations in near real time if average CPU across the group is above 75% for 5 minutes in a row.
- **The limits:** Scalable Google Cloud solution.
- **What they're really asking:** How do you set up that notification?

**Clues in the question:**
- Built-in metric **`compute.googleapis.com/instance/cpu/utilization`** + alert policy (threshold 75%, duration 5 min, aggregated across the MIG).

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Alerting policy 🔑
- **What it is:** Cloud Monitoring rule: when a metric crosses a threshold for a duration, notify channels.
- **Looks like:** metric `instance/cpu/utilization`, mean across group > 0.75 for 5 min → email/PagerDuty
- **Not to be confused with:** autoscaler settings.
- **Analogy:** 🚨 A temperature alarm with a 5-minute delay.
- **In the online store:** —

### 🔗 How they fit together
```
 cpu/utilization (mean over MIG) > 75% for 5m → notify ✅
```

---

## 🌍 Real-World Scenario

Ops creates an **alert policy** on MIG CPU utilization with 75% / 5 minutes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a logs-based metric in Cloud Logging that filters for high CPU usage entries, and then create a Cloud Monitoring alert policy based on that custom metric.

**Wrong words:**
- ❌ "**logs-based metric … high CPU usage entries**": CPU isn't logged; the metric already exists.

📌 **When to use it:** Use log-based metrics for events only in logs.
🏢 **Office example:** Counting complaints to measure temperature.

### ❌ B
> **B.** Deploy the Ops Agent to all Compute Engine VM instances to collect the CPU metric. Use a custom script running on a separate Compute Engine instance to poll this metric every five minutes, and send an email notification if the threshold is breached.

**Wrong words:**
- ❌ "**custom script … separate Compute Engine instance**": custom, not scalable; CPU metric needs no Ops Agent.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** A person checking the thermometer every 5 minutes.

### ✅ C
> **C.** Create a Cloud Monitoring alerting policy that targets the compute.googleapis.com/instance/cpu/utilization metric. Set the threshold to 75% and the duration to five minutes.

**Why it's correct:**
- ✔️ "**alerting policy that targets the compute.googleapis.com/instance/cpu/utilization metric**" matches "**average CPU utilization across all instances in the MIG**".
- ✔️ "**threshold to 75% and the duration to five minutes**" matches "**exceeds 75% for a continuous five-minute period**" + "**near-real time notification**".

📌 **When to use it:** Use it when you want to be told automatically if machines stay too busy for a while.
🏢 **Office example:** An alarm that rings if the office stays too hot for five minutes straight.

### ❌ D
> **D.** Configure an autoscaling policy for the MIG to use a CPU utilization target of 75% for five minutes, and then enable a notification channel in the autoscaler settings.

**Wrong words:**
- ❌ "**autoscaling policy … notification channel in the autoscaler**": autoscaler scales; it doesn't have notification channels.

📌 **When to use it:** Use autoscaling to add VMs under load.
🏢 **Office example:** Opening windows instead of calling someone.

---

## 🛒 E-Commerce Full-Stack Example

Alert `orders-mig-cpu-high`: mean CPU > 75% for 5 min → #oncall.

---

## 🧠 Key Takeaways / Memory Tips

- **Metric threshold notification → Cloud Monitoring alerting policy.**
  🧠 *"**Metric + threshold + duration = alert.**"*
- Related: **Q295**.

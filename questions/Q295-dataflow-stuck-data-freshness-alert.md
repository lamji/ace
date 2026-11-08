# Q295: Detect Stuck Dataflow Jobs With Minimal Effort (Cloud Monitoring Alert on Data Freshness)

**Topic:** Monitoring (Dataflow metrics)

## ❓ Question
> Your company was recently impacted by a service disruption that caused multiple Dataflow jobs to get stuck, resulting in significant downtime in downstream applications and revenue loss. You were able to resolve the issue by identifying and fixing an error you found in the code. You need to design a solution with minimal management effort to identify when jobs are stuck in the future to ensure that this issue does not occur again. What should you do?
>
> **A.** Update the Dataflow job configurations to send messages to a Pub/Sub topic when there are delays. Configure a backup Dataflow job to process jobs that are delayed. Use Cloud Tasks to trigger an alert when messages are pushed to the Pub/Sub topic.
>
> **B.** Set up Cloud Monitoring alerts on the data freshness metric for the Dataflow jobs to receive a notification when a certain threshold is reached.
>
> **C.** Set up Error Reporting to identify stack traces that indicate slowdowns in Dataflow jobs. Set up alerts based on these log entries.
>
> **D.** Use the Personalized Service Health dashboard to identify issues with Dataflow jobs across regions.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An outage made several Dataflow jobs (data-processing pipelines) get stuck, causing downtime and lost revenue. You fixed the code bug.
- **What you must achieve:** Find out automatically if jobs get stuck again.
- **The limits:** Very little management effort.
- **What they're really asking:** How do you detect stuck Dataflow jobs in the future?

**Clues in the question:**
- A stuck job stops moving data forward → **data freshness** (and system lag) grows.
- "**minimal management effort**" → a built-in **Monitoring alert** on that metric.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Dataflow data freshness 🔑
- **What it is:** How old the newest fully processed data is. If a job stalls, freshness keeps growing.
- **Looks like:** metric `dataflow.googleapis.com/job/data_watermark_age` > 10 min → alert
- **Not to be confused with:** error logs.
- **Analogy:** ⏱️ How stale the newest delivery is.
- **In the online store:** Order pipeline lag.

### 🔗 How they fit together
```
 job stuck → data freshness ↑ → alert > threshold ✅
```

---

## 🌍 Real-World Scenario

After an outage, the team adds a **Monitoring alert** on each Dataflow job's **data freshness**; if it lags over 10 minutes, on-call is paged.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Update the Dataflow job configurations to send messages to a Pub/Sub topic when there are delays. Configure a backup Dataflow job to process jobs that are delayed. Use Cloud Tasks to trigger an alert when messages are pushed to the Pub/Sub topic.

**Wrong words:**
- ❌ "**send messages to a Pub/Sub topic … backup Dataflow job … Cloud Tasks**": lots of custom work, and Cloud Tasks isn't an alerting tool.

📌 **When to use it:** **Avoid** — built-in metrics do this.
🏢 **Office example:** Building a whole mail system to notice a stopped conveyor.

### ✅ B
> **B.** Set up Cloud Monitoring alerts on the data freshness metric for the Dataflow jobs to receive a notification when a certain threshold is reached.

**Why it's correct:**
- ✔️ "**alerts on the data freshness metric**" matches "**identify when jobs are stuck**": stuck jobs stop updating freshness.
- ✔️ Built in, which matches "**minimal management effort**".

📌 **When to use it:** Use it when you need to know automatically if a data line stops moving.
🏢 **Office example:** An alarm that rings when the newest package on the conveyor is too old.

### ❌ C
> **C.** Set up Error Reporting to identify stack traces that indicate slowdowns in Dataflow jobs. Set up alerts based on these log entries.

**Wrong words:**
- ❌ "**Error Reporting … stack traces**": a stuck job may throw no errors at all.

📌 **When to use it:** Use Error Reporting for crashing code.
🏢 **Office example:** Waiting for a crash report from a machine that just quietly stopped.

### ❌ D
> **D.** Use the Personalized Service Health dashboard to identify issues with Dataflow jobs across regions.

**Wrong words:**
- ❌ "**Personalized Service Health**": shows Google Cloud service incidents, not your own job's code problems.

📌 **When to use it:** Use it to see if Google itself has an outage.
🏢 **Office example:** Checking the city's power status when your own machine jammed.

---

## 🛒 E-Commerce Full-Stack Example

Alert: `job/data_watermark_age` > 600 s for `orders-streaming` → PagerDuty.

---

## 🧠 Key Takeaways / Memory Tips

- **Stuck Dataflow job → alert on data freshness / system lag.**
  🧠 *"**Stale data = stuck job.**"*
- Related: **Q172**, **Q239**.

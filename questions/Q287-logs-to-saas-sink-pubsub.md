# Q287: Send Cloud Logging Logs to a Third-Party SaaS With the Least Delay (Log Sink to Pub/Sub, SaaS Subscribes)

**Topic:** Logging (sinks to Pub/Sub)

## ❓ Question
> Your company uses a multi-cloud strategy that includes Google Cloud. You want to centralize application logs in a third-party software-as-a-service (SaaS) tool from all environments. You need to integrate logs originating from Cloud Logging, and you want to ensure the export occurs with the least amount of delay possible. What should you do?
>
> **A.** Create a Cloud Logging sink and configure BigQuery as the destination. Configure the SaaS tool to query BigQuery to retrieve the logs.
>
> **B.** Create a Cloud Logging sink and configure Pub/Sub as the destination. Configure the SaaS tool to subscribe to the Pub/Sub topic to retrieve the logs.
>
> **C.** Create a Cloud Logging sink and configure Cloud Storage as the destination. Configure the SaaS tool to read the Cloud Storage bucket to retrieve the logs.
>
> **D.** Use a Cloud Scheduler cron job to trigger a Cloud Function that queries Cloud Logging and sends the logs to the SaaS tool.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Stream logs to an outside tool **as fast as possible**.

**Clues in the question:**
- "**least amount of delay**" + "**third-party**" → **sink to Pub/Sub** (streaming), tool subscribes.
- Cloud Storage sinks batch hourly; BigQuery/polling add delay.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Log sink → Pub/Sub 🔑 (review from Q244)
- **What it is:** Streams each matching log entry to a topic in near real time.
- **Looks like:** `gcloud logging sinks create to-saas pubsub.googleapis.com/projects/p/topics/logs-out`
- **Not to be confused with:** Storage sink (batched).
- **Analogy:** 📬 A chute that sends each note as it's written.
- **In the online store:** Datadog/Splunk feed.

### 🔗 How they fit together
```
 Cloud Logging ─ sink ─► Pub/Sub ─ subscription ─► SaaS tool ✅ (seconds)
```

---

## 🌍 Real-World Scenario

A multi-cloud company streams Google Cloud logs to its SaaS log tool through a **sink to Pub/Sub**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Logging sink and configure BigQuery as the destination. Configure the SaaS tool to query BigQuery to retrieve the logs.

**Wrong words:**
- ❌ "**BigQuery as the destination … query BigQuery**": the SaaS tool must poll; more delay and cost.

📌 **When to use it:** Use BigQuery sinks for log analytics.
🏢 **Office example:** Filing notes in a library and asking the tool to visit it.

### ✅ B
> **B.** Create a Cloud Logging sink and configure Pub/Sub as the destination. Configure the SaaS tool to subscribe to the Pub/Sub topic to retrieve the logs.

**Why it's correct:**
- ✔️ "**sink and configure Pub/Sub as the destination**" matches "**least amount of delay possible**": entries stream as they arrive.
- ✔️ "**SaaS tool to subscribe to the Pub/Sub topic**" matches "**centralize application logs in a third-party … tool**".

📌 **When to use it:** Use it when an outside system needs your log entries almost instantly.
🏢 **Office example:** A chute that sends each note to the outside office the moment it's written.

### ❌ C
> **C.** Create a Cloud Logging sink and configure Cloud Storage as the destination. Configure the SaaS tool to read the Cloud Storage bucket to retrieve the logs.

**Wrong words:**
- ❌ "**Cloud Storage as the destination**": logs are written in hourly batches.

📌 **When to use it:** Use Storage sinks for cheap archives.
🏢 **Office example:** Mailing the notes once an hour in a box.

### ❌ D
> **D.** Use a Cloud Scheduler cron job to trigger a Cloud Function that queries Cloud Logging and sends the logs to the SaaS tool.

**Wrong words:**
- ❌ "**Cloud Scheduler … Cloud Function that queries Cloud Logging**": custom code, polling delay, and API quotas.

📌 **When to use it:** **Avoid** custom polling when sinks exist.
🏢 **Office example:** Hiring a clerk to copy the logbook every few minutes.

---

## 🛒 E-Commerce Full-Stack Example

Sink `to-observability` (filter `severity>=INFO`) → Pub/Sub `logs-saas` → vendor's push subscription.

---

## 🧠 Key Takeaways / Memory Tips

- **Logs to a third-party tool fast → sink to Pub/Sub.**
  🧠 *"**Fastest export = Pub/Sub.**"*
- Related: **Q244**, **Q213**.

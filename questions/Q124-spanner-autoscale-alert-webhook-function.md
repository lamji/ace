# Q124: Automatically Scale Cloud Spanner Nodes Up and Down (Alert → Webhook → Cloud Function)

**Topic:** Cloud Spanner / Monitoring (alerting webhooks, Cloud Functions, autoscaling)

## ❓ Question
> You have an application that uses Cloud Spanner as a backend database. The application has a very predictable traffic pattern. You want to automatically scale up or down the number of Spanner nodes depending on traffic. What should you do?
>
> **A.** Create a cron job that runs on a scheduled basis to review Cloud Monitoring metrics, and then resize the Spanner instance accordingly.
>
> **B.** Create a Cloud Monitoring alerting policy to send an alert to oncall SRE emails when Cloud Spanner CPU exceeds the threshold. SREs would scale resources up or down accordingly.
>
> **C.** Create a Cloud Monitoring alerting policy to send an alert to Google Cloud Support email when Cloud Spanner CPU exceeds your threshold. Google support would scale resources up or down accordingly.
>
> **D.** Create a Cloud Monitoring alerting policy to send an alert to webhook when Cloud Spanner CPU is over or under your threshold. Create a Cloud Function that listens to HTTP and resizes Spanner resources accordingly.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** Today, Spanner also has **managed autoscaling** and the open-source **Spanner Autoscaler**. Among these options, D is the automatic, event-driven one.

---

## 📖 What the Question Is Asking

**In plain words:** Spanner nodes should go **up and down automatically** with traffic. Which option does it **without a person**?

**Clues in the question:**
- "**automatically scale up or down**": no humans in the loop (rules out B and C).
- "**depending on traffic**": react to the actual load, **CPU over or under** a threshold.
- Alert → **webhook** → **Cloud Function** that calls the Spanner API to change node count.

**Exam topic:** Cloud Spanner / Monitoring.

---

## 📚 Key Terms Explained

### 1. Webhook notification channel 🔑
- **What it is:** An alerting channel that sends an **HTTP request to a URL** when an alert fires, so code can react automatically.
- **Looks like:** Notification channel type **Webhook** → `https://us-central1-shop.cloudfunctions.net/scaleSpanner`
- **Not to be confused with:** an email.
- **Analogy:** 📞 The alarm **calls a robot** instead of a person.
- **In the online store:** The alert triggers the scaling function.

### 2. Cloud Function
- **What it is:** A **small piece of code that runs when an event or HTTP request arrives**. No servers to manage.
- **Looks like:** `def scale(request): instance.node_count = n; instance.update()`
- **Not to be confused with:** a VM.
- **Analogy:** 🤖 A robot that does one job when its phone rings.
- **In the online store:** Resizes Spanner from 3 to 5 nodes.

### 3. Spanner nodes / processing units
- **What it is:** Spanner's capacity. More nodes = more throughput (and more cost).
- **Looks like:** `gcloud spanner instances update orders --nodes=5`
- **Not to be confused with:** a VM.
- **Analogy:** 🧑‍💼 Clerks at the counter.
- **In the online store:** More nodes during sales.

### 🔗 How they fit together
```
 Spanner CPU > 65% ─► alert ─► webhook ─► Cloud Function ─► instances.update(nodes+1) ✅
 Spanner CPU < 30% ─► alert ─► webhook ─► Cloud Function ─► instances.update(nodes-1) ✅
```

---

## 🌍 Real-World Scenario

An app's traffic doubles every weekday at 9am. The team creates alerting policies on Spanner CPU (high and low) that send to a **webhook**. A **Cloud Function** receives each alert and adds or removes nodes. No one gets paged for routine scaling.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a cron job that runs on a scheduled basis to review Cloud Monitoring metrics, and then resize the Spanner instance accordingly.

**Wrong words:**
- ❌ "**cron job that runs on a scheduled basis**": it only checks at fixed times, so it reacts late. It's also a homemade VM job you must run and maintain.

📌 **When to use it:** Use a schedule when you scale at fixed times regardless of traffic.
🏢 **Office example:** Checking the queue only on the hour, even if it overflows at 9:10.

### ❌ B
> **B.** Create a Cloud Monitoring alerting policy to send an alert to oncall SRE emails when Cloud Spanner CPU exceeds the threshold. SREs would scale resources up or down accordingly.

**Wrong words:**
- ❌ "**send an alert to oncall SRE emails … SREs would scale**": a person does the scaling. Not automatic.

📌 **When to use it:** Use human alerts for problems that need judgment.
🏢 **Office example:** Calling the manager every time the queue grows, so they can open another counter.

### ❌ C
> **C.** Create a Cloud Monitoring alerting policy to send an alert to Google Cloud Support email when Cloud Spanner CPU exceeds your threshold. Google support would scale resources up or down accordingly.

**Wrong words:**
- ❌ "**Google support would scale resources**": Google Support doesn't resize your instances for you. Not automatic, and not their job.

📌 **When to use it:** **Never use this.** Use D.
🏢 **Office example:** Calling the building owner to open another counter in your shop.

### ✅ D
> **D.** Create a Cloud Monitoring alerting policy to send an alert to webhook when Cloud Spanner CPU is over or under your threshold. Create a Cloud Function that listens to HTTP and resizes Spanner resources accordingly.

**Why it's correct:**
- ✔️ "**alert to webhook when Cloud Spanner CPU is over or under your threshold**" matches "**scale up or down … depending on traffic**": both directions are covered by the real load.
- ✔️ "**Cloud Function that listens to HTTP and resizes Spanner**" matches "**automatically**": code makes the change, not a person.

📌 **When to use it:** Use it when a warning should automatically trigger a fix, with no person needed.
🏢 **Office example:** When the queue gets long, the alarm calls a robot that opens another counter, and closes it when the queue is short.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `orders` Spanner instance:
- Policy "Spanner high": CPU > 65% for 5 min → webhook `scaleSpanner?dir=up`
- Policy "Spanner low": CPU < 30% for 30 min → webhook `scaleSpanner?dir=down`

The Cloud Function `scaleSpanner` calls `instance.node_count += 1` (or `-= 1`) within limits of 3–10 nodes.

---

## 🧠 Key Takeaways / Memory Tips

- **Automatic reaction to a metric → alert → webhook (or Pub/Sub) → Cloud Function.**
- Email to humans or Google Support isn't automatic.
  🧠 *"**Alert calls a function, the function fixes it.**"*
- Related: **Q123** (alerting policy), **Q098** (Spanner keys), **Q058** (why Spanner).

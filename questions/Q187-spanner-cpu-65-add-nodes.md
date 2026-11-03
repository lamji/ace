# Q187: Improve Spanner Performance Fast, Single Region (Alert at 65% High-Priority CPU, Add Nodes)

**Topic:** Spanner (CPU utilization recommendations)

## ❓ Question
> You need to manage a Cloud Spanner instance for best query performance. Your instance in production runs in a single Google Cloud region. You need to improve performance in the shortest amount of time. You want to follow Google best practices for service configuration. What should you do?
>
> **A.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 45%. If you exceed this threshold, add nodes to your instance.
>
> **B.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 45%. Use database query statistics to identify queries that result in high CPU usage, and then rewrite those queries to optimize their resource usage.
>
> **C.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 65%. If you exceed this threshold, add nodes to your instance.
>
> **D.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 65%. Use database query statistics to identify queries that result in high CPU usage, and then rewrite those queries to optimize their resource usage.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Single-region** Spanner. Best practice threshold, and the **fastest** fix.

**Clues in the question:**
- "**single Google Cloud region**" → Google recommends keeping high-priority CPU **below 65%** (45% is for **multi-region**).
- "**shortest amount of time**" → **add nodes** (minutes) instead of rewriting queries (days).

**Exam topic:** Spanner.

---

## 📚 Key Terms Explained

### 1. High-priority CPU utilization 🔑
- **What it is:** The share of Spanner CPU used by user queries. Recommended max: **65% regional**, **45% multi-region**.
- **Looks like:** Monitoring metric `spanner.googleapis.com/instance/cpu/utilization_by_priority`
- **Not to be confused with:** total CPU.
- **Analogy:** 🏃 How busy the main staff are.
- **In the online store:** Inventory DB alert.

### 2. Nodes / processing units
- **What it is:** Spanner's capacity. More nodes = more CPU and throughput, added online.
- **Looks like:** `gcloud spanner instances update inv --nodes=5`
- **Not to be confused with:** VMs you manage.
- **Analogy:** 👥 Staff headcount.
- **In the online store:** Add before Black Friday.

### 🔗 How they fit together
```
 regional: alert at 65% → add nodes ✅ (fast)
 multi-region: 45%
```

---

## 🌍 Real-World Scenario

A single-region Spanner instance slows under load. The DBA sets an alert at **65%** high-priority CPU and **adds nodes** when it fires, which takes minutes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 45%. If you exceed this threshold, add nodes to your instance.

**Wrong words:**
- ❌ "**45%**": that's the multi-region recommendation. This instance is single-region.

📌 **When to use it:** Use 45% for multi-region instances.
🏢 **Office example:** Applying the head-office rule to a branch office.

### ❌ B
> **B.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 45%. Use database query statistics to identify queries that result in high CPU usage, and then rewrite those queries to optimize their resource usage.

**Wrong words:**
- ❌ "**45%**" (wrong threshold) and ❌ "**rewrite those queries**": slow, not the shortest time.

📌 **When to use it:** Use query rewrites for long-term efficiency.
🏢 **Office example:** Retraining staff when you need help today.

### ✅ C
> **C.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 65%. If you exceed this threshold, add nodes to your instance.

**Why it's correct:**
- ✔️ "**65%**" matches "**single Google Cloud region**" + "**Google best practices**".
- ✔️ "**add nodes to your instance**" matches "**improve performance in the shortest amount of time**".

📌 **When to use it:** Use it when a busy system needs more capacity right away.
🏢 **Office example:** Calling in extra temp staff the moment the team hits its workload limit.

### ❌ D
> **D.** Create an alert in Cloud Monitoring to alert when the percentage of high priority CPU utilization reaches 65%. Use database query statistics to identify queries that result in high CPU usage, and then rewrite those queries to optimize their resource usage.

**Wrong words:**
- ✔️ "65%" is right.
- ❌ "**rewrite those queries**": takes far longer than adding nodes.

📌 **When to use it:** Use it when you have time to tune slow queries.
🏢 **Office example:** Redesigning the workflow instead of adding staff today.

---

## 🛒 E-Commerce Full-Stack Example

Alert: `cpu/utilization_by_priority{priority=high} > 0.65` on `shopnow-inventory` (regional `us-central1`) → runbook: `gcloud spanner instances update shopnow-inventory --nodes=+2`.

---

## 🧠 Key Takeaways / Memory Tips

- **Spanner CPU: 65% regional, 45% multi-region. Fastest fix = add nodes.**
  🧠 *"**Single = 65, multi = 45.**"*
- Related: **Q173**, **Q180**.

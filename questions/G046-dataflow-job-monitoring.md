# G046: Streaming Pipeline Backlog Is Growing: Find the Slow Step (Dataflow Job Monitoring Interface)

**Topic:** Dataflow (reviewing job status)
**Exam guide section:** 3.2 Managing storage and data solutions: Reviewing job status (e.g., Dataflow, BigQuery)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> A streaming Dataflow pipeline reads order events from Pub/Sub and writes them to BigQuery. Users report that dashboards are 30 minutes behind, and the Pub/Sub subscription backlog is growing. You need to identify which step of the pipeline is causing the delay. What should you do?
>
> **A.** Delete the Pub/Sub subscription and create a new one.
>
> **B.** Restart the job every 30 minutes.
>
> **C.** Increase the BigQuery slot reservation without checking the pipeline.
>
> **D.** Open the job in the Dataflow monitoring interface, and review the job graph and execution details for data freshness, system lag, and the slowest stage.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A streaming pipeline in Dataflow (Google's managed data-processing service) takes order events from Pub/Sub (a message queue) and writes them into BigQuery (the data warehouse).
- **What you must achieve:** Find which step of the pipeline is causing a 30-minute delay.
- **The limits:** Messages are piling up in the queue (a growing backlog). Find the cause, don't guess.
- **What they're really asking:** Where do you look to see each pipeline step's status and lag?

**Clues in the question:**
- "**identify which step of the pipeline**": the **Dataflow monitoring interface** shows the job graph with per-stage metrics.
- "**30 minutes behind**" + "**backlog is growing**": check **data freshness** and **system lag**.

**Exam topic:** Data operations (exam guide section 3.2).

---

## 📚 Key Terms Explained

### 1. Dataflow
- **What it is:** Google's managed service for batch and streaming data pipelines (Apache Beam).
- **Looks like:** Pipeline: `ReadFromPubSub → ParseJSON → Enrich → WriteToBigQuery`
- **Not to be confused with:** Dataproc (managed Spark/Hadoop clusters).
- **Analogy:** 🏭 A conveyor-belt factory for data.
- **In the online store:** Order events into BigQuery.

### 2. Dataflow monitoring interface 🔑
- **What it is:** The console page for a job: the **job graph** (steps), **execution details** (per-stage progress), metrics like **data freshness** and **system lag**, worker logs, and autoscaling history.
- **Looks like:** Job graph: `Enrich` step: system lag 28 min 🔴
- **Not to be confused with:** Cloud Monitoring alone, without the stage view.
- **Analogy:** 🏭 The factory floor display showing which station is jammed.
- **In the online store:** Finds the slow `Enrich` call.

### 🔗 How they fit together
```
 Pub/Sub ─► Parse ─► Enrich 🔴 (system lag 28m) ─► WriteToBigQuery
 Dataflow job page → job graph + execution details → slowest stage ✅
```

---

## 🌍 Real-World Scenario

During a sale, order dashboards fall behind. In the **Dataflow job graph**, the `Enrich` step shows huge system lag because it calls a slow pricing API per record. The team adds caching and batching, and the backlog drains.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Delete the Pub/Sub subscription and create a new one.

**Wrong words:**
- ❌ "**Delete the Pub/Sub subscription**": unprocessed orders are lost, and you still don't know the cause.

📌 **When to use it:** Never do this to troubleshoot. You'd lose messages.
🏢 **Office example:** Throwing out the queue of customers instead of fixing the slow till.

### ❌ B
> **B.** Restart the job every 30 minutes.

**Wrong words:**
- ❌ "**Restart the job every 30 minutes**": hides the problem, can add more lag, and doesn't find the step.

📌 **When to use it:** Avoid it. Find and fix the slow stage.
🏢 **Office example:** Turning the conveyor off and on, hoping it helps.

### ❌ C
> **C.** Increase the BigQuery slot reservation without checking the pipeline.

**Wrong words:**
- ❌ "**without checking the pipeline**": guessing. The bottleneck may be elsewhere, like the enrichment step.

📌 **When to use it:** Use more slots when BigQuery queries themselves are slow.
🏢 **Office example:** Adding more delivery trucks when the jam is on the factory floor.

### ✅ D
> **D.** Open the job in the Dataflow monitoring interface, and review the job graph and execution details for data freshness, system lag, and the slowest stage.

**Why it's correct:**
- ✔️ "**Dataflow monitoring interface … job graph and execution details**" matches "**identify which step of the pipeline**".
- ✔️ "**data freshness, system lag, and the slowest stage**" matches "**30 minutes behind**" and "**backlog is growing**".

📌 **When to use it:** Use it when a data pipeline is behind and you need to see which step is stuck.
🏢 **Office example:** Looking at the factory display to find the jammed station.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `orders-stream`: the job graph shows `EnrichWithPrices` lagging → add a side-input cache → system lag back under 10s.

---

## 🧠 Key Takeaways / Memory Tips

- **Dataflow behind / backlog growing → Dataflow monitoring interface: job graph, execution details, data freshness, system lag.**
  🧠 *"**Find the jammed station on the job graph.**"*
- Related: **Q023**, **Q213**, **Q193** (BigQuery job review).

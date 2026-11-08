# G048: Find Which Functions Use the Most CPU in Production With Low Overhead, Continuously (Cloud Profiler)

**Topic:** Diagnostics (Cloud Profiler)
**Exam guide section:** 3.4 Monitoring and logging: Using cloud diagnostic tools (e.g., Cloud Trace, Cloud Profiler) to investigate an application issue

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your Java API running on GKE uses much more CPU than expected in production, which increases cost. You want to continuously identify which functions in the code consume the most CPU and memory, with low overhead, in the production environment. What should you do?
>
> **A.** Use Cloud Trace to measure request latency between services.
>
> **B.** Enable Cloud Profiler in the application, and review the flame graphs in the Profiler interface.
>
> **C.** Enable Data Access audit logs for the GKE cluster.
>
> **D.** Add more nodes to the cluster.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your Java API on Kubernetes (GKE) uses far more CPU than it should in production, which costs money.
- **What you must achieve:** Find which parts of the code (functions) use the most CPU and memory, all the time, in production.
- **The limits:** The overhead must be low, so the measuring itself can't slow production down.
- **What they're really asking:** Which Google Cloud tool continuously profiles code in production?

**Clues in the question:**
- "**which functions in the code consume the most CPU and memory**": a **profiler**.
- "**continuously … low overhead … production**": **Cloud Profiler** (statistical sampling).

**Exam topic:** Diagnostics (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Cloud Profiler 🔑
- **What it is:** A low-overhead, continuous profiler for production apps (Java, Go, Node.js, Python). It samples CPU time and heap usage and shows **flame graphs** by function.
- **Looks like:** Java agent: `-agentpath:/opt/cprof/profiler_java_agent.so=-cprof_service=orders-api` → flame graph: `JsonParser.parse` 38% CPU
- **Not to be confused with:** Cloud Trace, which shows time spent across requests and services, not per-function CPU inside your code.
- **Analogy:** ⏱️ A time-and-motion study that quietly samples what each worker is doing.
- **In the online store:** Finds an expensive JSON parse in orders-api.

### 2. Flame graph
- **What it is:** A chart where each bar is a function, and wider bars use more resources.
- **Looks like:** Wide bar: `PriceCalculator.applyDiscounts`
- **Not to be confused with:** A latency timeline.
- **Analogy:** 🔥 A bar chart of who's busiest.
- **In the online store:** Spotting the hottest code path.

### 🔗 How they fit together
```
 orders-api (Profiler agent, sampled) ─► Cloud Profiler ─► flame graph → hottest functions ✅
```

---

## 🌍 Real-World Scenario

An API's CPU bill doubled after a release. **Cloud Profiler** shows that 38% of CPU goes to re-parsing the same JSON config on every request. Caching it cuts CPU in half.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Cloud Trace to measure request latency between services.

**Wrong words:**
- ✔️ Trace is useful for latency.
- ❌ "**request latency between services**": it doesn't break CPU and memory down by function inside the code.

📌 **When to use it:** Use Cloud Trace to find which service in a chain makes requests slow.
🏢 **Office example:** Timing deliveries between offices, not who's busy inside one.

### ✅ B
> **B.** Enable Cloud Profiler in the application, and review the flame graphs in the Profiler interface.

**Why it's correct:**
- ✔️ "**Cloud Profiler**" matches "**continuously … low overhead … production**".
- ✔️ "**flame graphs**" show "**which functions in the code consume the most CPU and memory**".

📌 **When to use it:** Use it when you want to know which part of your program is doing the most work, in the live system.
🏢 **Office example:** A quiet efficiency study that shows which tasks take staff the most time.

### ❌ C
> **C.** Enable Data Access audit logs for the GKE cluster.

**Wrong words:**
- ❌ "**Data Access audit logs**": record who read or wrote data through APIs. Nothing about code CPU usage.

📌 **When to use it:** Use them for data access auditing.
🏢 **Office example:** The visitor log, not a work study.

### ❌ D
> **D.** Add more nodes to the cluster.

**Wrong words:**
- ❌ "**Add more nodes**": increases cost and doesn't find the inefficient code.

📌 **When to use it:** Use more nodes when the load really needs more capacity.
🏢 **Office example:** Hiring more staff instead of fixing a wasteful process.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `orders-api` (Java on GKE): Profiler agent added to the image. The flame graph shows `ConfigLoader.parse` → cache it → CPU requests lowered.

---

## 🧠 Key Takeaways / Memory Tips

- **Which code uses CPU/memory in prod → Cloud Profiler. Which service makes requests slow → Cloud Trace. Which SQL is slow → Query Insights.**
  🧠 *"**Profiler = per function; Trace = per request.**"*
- Related: **G019**, **Q343**.

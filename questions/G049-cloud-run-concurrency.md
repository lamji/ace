# G049: CPU-Heavy, Single-Threaded Cloud Run Container Slows Down Under Load (Set Concurrency to 1)

**Topic:** Cloud Run (autoscaling and concurrency)
**Exam guide section:** 3.1 Managing compute resources: Configuring autoscaling for a Cloud Run application

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your Cloud Run service generates PDF invoices. Each request is CPU-intensive, and the code can process only one request at a time efficiently. Under load, response times become very slow because many requests are sent to the same instance. You want Cloud Run to scale out so that each instance handles one request at a time. What should you do?
>
> **A.** Set the minimum number of instances to 10.
>
> **B.** Set the service's maximum concurrent requests per instance to 1.
>
> **C.** Increase the request timeout to 60 minutes.
>
> **D.** Lower the maximum number of instances to 1.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A Cloud Run service (Google's serverless container service) makes PDF invoices. Each one takes a lot of CPU, and the code can only work on one request at a time efficiently.
- **What you must achieve:** Make Cloud Run start more copies (instances) so each copy works on just one request at a time.
- **The limits:** Under heavy traffic, many requests currently pile onto the same instance and become slow.
- **What they're really asking:** Which Cloud Run setting controls how many requests one instance handles at once?

**Clues in the question:**
- "**many requests are sent to the same instance**": the **concurrency** setting (default 80).
- "**each instance handles one request at a time**": set concurrency to **1**, and Cloud Run adds instances to handle the rest.

**Exam topic:** Cloud Run operations (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. Concurrency 🔑
- **What it is:** The maximum number of requests one Cloud Run instance handles at the same time (default 80, maximum 1000). Lower concurrency means Cloud Run scales out to more instances.
- **Looks like:** `gcloud run services update invoice-pdf --concurrency=1`
- **Not to be confused with:** Max instances, which caps the total number of instances.
- **Analogy:** 🧑‍🍳 How many orders one cook works on at once.
- **In the online store:** PDF generation, one at a time per instance.

### 2. Min / max instances
- **What it is:** Min keeps instances warm (avoids cold starts). Max caps how many instances (and how much cost) can exist.
- **Looks like:** `--min-instances=1 --max-instances=50`
- **Not to be confused with:** Concurrency.
- **Analogy:** 🏪 Minimum and maximum staff on the shift.
- **In the online store:** Peak-time limits.

### 🔗 How they fit together
```
 Before: 80 requests ─► 1 instance 🐢
 After (--concurrency=1): 80 requests ─► 80 instances (1 each) ✅
```

---

## 🌍 Real-World Scenario

At month end, invoice generation slows to 40 seconds per PDF because each instance juggles dozens of CPU-heavy requests. Setting **concurrency to 1** makes Cloud Run add instances so each PDF gets its own CPU, and generation drops to 2 seconds.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Set the minimum number of instances to 10.

**Wrong words:**
- ❌ "**minimum number of instances to 10**": keeps instances warm, but each can still take many requests at once.

📌 **When to use it:** Use min instances to avoid cold-start delays.
🏢 **Office example:** Keeping cooks on standby, but still letting one cook take 80 orders.

### ✅ B
> **B.** Set the service's maximum concurrent requests per instance to 1.

**Why it's correct:**
- ✔️ "**maximum concurrent requests per instance to 1**" matches "**each instance handles one request at a time**".
- ✔️ With concurrency 1, Cloud Run scales out, matching "**want Cloud Run to scale out**" and fixing "**many requests are sent to the same instance**".

📌 **When to use it:** Use it when each job is heavy and one worker can only do one at a time well.
🏢 **Office example:** One order per cook, and more cooks are called in when it's busy.

### ❌ C
> **C.** Increase the request timeout to 60 minutes.

**Wrong words:**
- ❌ "**request timeout to 60 minutes**": requests wait longer instead of getting faster.

📌 **When to use it:** Use longer timeouts for legitimately long jobs.
🏢 **Office example:** Telling customers to wait longer rather than adding cooks.

### ❌ D
> **D.** Lower the maximum number of instances to 1.

**Wrong words:**
- ❌ "**maximum number of instances to 1**": prevents scaling out entirely, so it gets worse.

📌 **When to use it:** Use a low max to cap cost or protect a fragile backend.
🏢 **Office example:** Allowing only one cook for the whole restaurant.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `invoice-pdf`: `--concurrency=1 --cpu=2 --memory=2Gi --max-instances=100`. The storefront API keeps concurrency 80.

---

## 🧠 Key Takeaways / Memory Tips

- **CPU-heavy, one-at-a-time requests on Cloud Run → `--concurrency=1` (scale out per request).**
  🧠 *"**Concurrency = orders per cook.**"*
- Related: **Q212**, **Q278**, **Q319**.

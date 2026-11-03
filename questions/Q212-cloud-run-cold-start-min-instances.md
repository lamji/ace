# Q212: First Page Loads Slowly on Cloud Run (Cold Starts: Set Minimum Instances)

**Topic:** Cloud Run (cold starts, min instances)

## ❓ Question
> You are running a web application on Cloud Run for a few hundred users. Some of your users complain that the initial web page of the application takes much longer to load than the following pages. You want to follow Google's recommendations to mitigate the issue. What should you do?
>
> **A.** Set the minimum number of instances for your Cloud Run service to 3.
>
> **B.** Set the concurrency number to 1 for your Cloud Run service.
>
> **C.** Set the maximum number of instances for your Cloud Run service to 100.
>
> **D.** Update your web application to use the protocol HTTP/2 instead of HTTP/1.1.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The **first** page is slow, later pages are fast.

**Clues in the question:**
- "**initial web page … takes much longer**" → a **cold start** (Cloud Run starting a container from zero).
- Google's fix: **minimum instances** keep containers warm.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Cold start 🔑
- **What it is:** The delay when Cloud Run must **start a new container** before answering.
- **Looks like:** first request 4 s, next 200 ms
- **Not to be confused with:** slow code.
- **Analogy:** ☕ Waiting for the coffee machine to warm up.
- **In the online store:** Storefront first load.

### 2. Minimum instances
- **What it is:** Number of containers Cloud Run keeps **always running** (you pay for idle time).
- **Looks like:** `--min-instances=3`
- **Not to be confused with:** max instances.
- **Analogy:** ☕ Keeping the machine on.
- **In the online store:** —

### 🔗 How they fit together
```
 min-instances=0: idle → 0 → request → cold start 🐢
 min-instances=3: 3 warm → request → fast ✅
```

---

## 🌍 Real-World Scenario

An internal portal's first load is slow each morning. The team sets **min instances = 3** so containers are always warm.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set the minimum number of instances for your Cloud Run service to 3.

**Why it's correct:**
- ✔️ "**minimum number of instances … to 3**" matches "**initial web page … takes much longer**": warm containers remove cold starts.
- ✔️ It's Google's documented fix, which matches "**Google's recommendations**".

📌 **When to use it:** Use it when the first visitor of the day shouldn't wait for things to start up.
🏢 **Office example:** Keeping the coffee machine switched on so the first person in doesn't wait.

### ❌ B
> **B.** Set the concurrency number to 1 for your Cloud Run service.

**Wrong words:**
- ❌ "**concurrency number to 1**": each container handles one request, so **more** containers start, causing **more** cold starts.

📌 **When to use it:** Use concurrency 1 for code that can't handle parallel requests.
🏢 **Office example:** One customer per cashier: more cashiers have to be called in.

### ❌ C
> **C.** Set the maximum number of instances for your Cloud Run service to 100.

**Wrong words:**
- ❌ "**maximum number of instances**": a ceiling; doesn't keep any warm.

📌 **When to use it:** Use max instances to cap cost or protect a database.
🏢 **Office example:** Limiting how many staff you can hire doesn't make anyone arrive early.

### ❌ D
> **D.** Update your web application to use the protocol HTTP/2 instead of HTTP/1.1.

**Wrong words:**
- ❌ "**HTTP/2**": doesn't fix container start-up time.

📌 **When to use it:** Use HTTP/2 for streaming or many parallel requests.
🏢 **Office example:** A faster phone line while the office is still closed.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run services update storefront --min-instances=3 --region=us-central1`

---

## 🧠 Key Takeaways / Memory Tips

- **Slow first request on Cloud Run → cold start → set min instances.**
  🧠 *"**Warm instances, warm welcome.**"*
- Related: **Q163**, **Q065**.

# Q298: Serverless, Scalable Asynchronous Transaction Processing (Pub/Sub + Cloud Run)

**Topic:** Serverless (Pub/Sub, Cloud Run)

## ❓ Question
> You have an application that is currently processing transactions by using a group of managed VM instances. You need to migrate the application so that it is serverless and scalable. You want to implement an asynchronous transaction processing system, while minimizing management overhead. What should you do?
>
> **A.** Install Kafka on VM instances to acknowledge incoming transactions. Use Cloud Run to process transactions.
>
> **B.** Use Pub/Sub to acknowledge incoming transactions. Use VM instances to process transactions.
>
> **C.** Use Pub/Sub to acknowledge incoming transactions. Use Cloud Run to process transactions.
>
> **D.** Install Kafka on VM instances to acknowledge incoming transactions. Use VM instances to process transactions.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app processes transactions on a group of managed VMs.
- **What you must achieve:** Move it to a serverless setup (no servers to manage) that scales and processes transactions asynchronously (accepted now, handled shortly after).
- **The limits:** Minimal management effort.
- **What they're really asking:** Which services should accept the transactions and which should process them?

**Clues in the question:**
- "**asynchronous**" + "**serverless**" → **Pub/Sub** queues transactions.
- Processing → **Cloud Run** (serverless, scales).

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Pub/Sub + Cloud Run 🔑 (review from Q064)
- **What it is:** Pub/Sub pushes each message to a Cloud Run endpoint; both scale automatically.
- **Looks like:** push subscription → `https://process-xyz.a.run.app/`
- **Not to be confused with:** Kafka on VMs.
- **Analogy:** 📬 Mail chute → serviced office staff.
- **In the online store:** Order processing.

### 🔗 How they fit together
```
 clients → Pub/Sub (accepts) → push → Cloud Run (processes) ✅
```

---

## 🌍 Real-World Scenario

A payments team replaces VMs with **Pub/Sub** to accept transactions and **Cloud Run** to process them asynchronously.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Install Kafka on VM instances to acknowledge incoming transactions. Use Cloud Run to process transactions.

**Wrong words:**
- ❌ "**Install Kafka on VM instances**": not serverless; you manage Kafka.

📌 **When to use it:** Use Kafka on VMs only if you must keep Kafka.
🏢 **Office example:** Running your own post office.

### ❌ B
> **B.** Use Pub/Sub to acknowledge incoming transactions. Use VM instances to process transactions.

**Wrong words:**
- ✔️ Pub/Sub is right.
- ❌ "**VM instances to process**": not serverless.

📌 **When to use it:** Use VMs for processing needing full OS control.
🏢 **Office example:** A modern mailroom with staff you must manage.

### ✅ C
> **C.** Use Pub/Sub to acknowledge incoming transactions. Use Cloud Run to process transactions.

**Why it's correct:**
- ✔️ "**Pub/Sub to acknowledge incoming transactions**" matches "**asynchronous transaction processing**".
- ✔️ "**Cloud Run to process transactions**" matches "**serverless and scalable**" + "**minimizing management overhead**".

📌 **When to use it:** Use it when requests should be accepted right away and handled shortly after, without running servers.
🏢 **Office example:** A mail chute that accepts every order instantly, with serviced staff who process them as they arrive.

### ❌ D
> **D.** Install Kafka on VM instances to acknowledge incoming transactions. Use VM instances to process transactions.

**Wrong words:**
- ❌ "**Kafka on VM instances**" and ❌ "**VM instances to process**": nothing serverless.

📌 **When to use it:** **Never use this** for a serverless goal.
🏢 **Office example:** Your own post office and your own staff.

---

## 🛒 E-Commerce Full-Stack Example

Checkout publishes to `orders-new`; push subscription → Cloud Run `order-processor`.

---

## 🧠 Key Takeaways / Memory Tips

- **Serverless async → Pub/Sub + Cloud Run.**
  🧠 *"**Pub/Sub accepts, Cloud Run works.**"*
- Related: **Q064**, **Q268**, **Q219**.

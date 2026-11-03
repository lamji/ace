# Q255: Deploy New Features Safely, Affect Fewer Customers (Gradual Rollout, Split Traffic Between Revisions)

**Topic:** Cloud Run (revisions, rollback)

## ❓ Question
> You want to enable your development team to deploy new features to an existing Cloud Run service in production. To minimize the risk associated with a new revision, you want to reduce the number of customers who might be affected by an outage without introducing any development or operational costs to your customers. You want to follow Google-recommended practices for managing revisions to a service. What should you do?
>
> **A.** Ask your customers to retry access to your service with exponential backoff to mitigate any potential problems after the new revision is deployed.
>
> **B.** Gradually roll out the new revision and split customer traffic between the revisions to allow rollback in case a problem occurs.
>
> **C.** Send all customer traffic to the new revision, and roll back to a previous revision if you witness any problems in production.
>
> **D.** Deploy your application to a second Cloud Run service, and ask your customers to use the second Cloud Run service.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Limit how many customers a bad release can hurt, with **no work for customers**.

**Clues in the question:**
- "**reduce the number of customers who might be affected**" → only a **slice** of traffic on the new revision → **gradual rollout + traffic split**.
- "**without introducing any … costs to your customers**" → customers change nothing.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Rollback 🔑
- **What it is:** Sending traffic back to the previous revision.
- **Looks like:** `gcloud run services update-traffic app --to-revisions=app-v1=100`
- **Not to be confused with:** redeploying.
- **Analogy:** ↩️ Going back to the old recipe.
- **In the online store:** Undo bad checkout.

### 🔗 How they fit together
```
 v1 90% | v2 10% → problem → v1 100% ✅ (only 10% saw it)
```

---

## 🌍 Real-World Scenario

Developers ship a new revision to **10%** of users. When errors rise, they roll back instantly; 90% never noticed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ask your customers to retry access to your service with exponential backoff to mitigate any potential problems after the new revision is deployed.

**Wrong words:**
- ❌ "**Ask your customers to retry … with exponential backoff**": puts work on customers and doesn't reduce who's affected.

📌 **When to use it:** Use retries in your own clients for transient errors.
🏢 **Office example:** Telling customers to keep calling back.

### ✅ B
> **B.** Gradually roll out the new revision and split customer traffic between the revisions to allow rollback in case a problem occurs.

**Why it's correct:**
- ✔️ "**Gradually roll out the new revision and split customer traffic**" matches "**reduce the number of customers who might be affected by an outage**".
- ✔️ "**to allow rollback**" matches "**minimize the risk associated with a new revision**"; customers change nothing.

📌 **When to use it:** Use it when a change might break things and you want only a few people exposed at first.
🏢 **Office example:** Trying the new process with one in ten customers, and switching back right away if it goes wrong.

### ❌ C
> **C.** Send all customer traffic to the new revision, and roll back to a previous revision if you witness any problems in production.

**Wrong words:**
- ❌ "**Send all customer traffic to the new revision**": every customer is affected by an outage.

📌 **When to use it:** Use it only for very low-risk changes.
🏢 **Office example:** Switching every customer to an untested process at once.

### ❌ D
> **D.** Deploy your application to a second Cloud Run service, and ask your customers to use the second Cloud Run service.

**Wrong words:**
- ❌ "**ask your customers to use the second Cloud Run service**": customers must change URLs — a cost to them.

📌 **When to use it:** Use a second service for a different app.
🏢 **Office example:** Asking customers to visit a different branch.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy storefront --image=…:v8 --no-traffic --tag=v8` → `update-traffic --to-tags=v8=10` → 50 → 100.

---

## 🧠 Key Takeaways / Memory Tips

- **Limit blast radius on Cloud Run → gradual rollout with traffic split; roll back if needed.**
  🧠 *"**Small slice first.**"*
- Related: **Q253**, **Q166**.

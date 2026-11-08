# Q166: Canary on Cloud Run for Anthos (New Revision + Split Traffic)

**Topic:** Cloud Run (revisions, traffic splitting)

## ❓ Question
> Your web application has been running successfully on Cloud Run for Anthos. You want to evaluate an updated version of the application with a specific percentage of your production users (canary deployment). What should you do?
>
> **A.** Create a new service with the new version of the application. Split traffic between this version and the version that is currently running.
>
> **B.** Create a new revision with the new version of the application. Split traffic between this version and the version that is currently running.
>
> **C.** Create a new service with the new version of the application. Add an HTTP Load Balancer in front of both services.
>
> **D.** Create a new revision with the new version of the application. Add an HTTP Load Balancer in front of both revisions.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A web app runs on Cloud Run for Anthos (Cloud Run on your own Kubernetes clusters).
- **What you must achieve:** Test an updated version with a set percentage of real users first (a canary deployment).
- **The limits:** None stated.
- **What they're really asking:** How do you send a chosen percentage of traffic to the new version?

**Clues in the question:**
- "**updated version**": on Cloud Run, a new version of the same service is a **revision**.
- "**specific percentage of your production users**": Cloud Run **splits traffic between revisions** natively (like App Engine versions in Q076).

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Revision 🔑
- **What it is:** An **immutable snapshot** of a Cloud Run service (image + config). Each deploy creates one, and traffic can be split between revisions.
- **Looks like:** `gcloud run deploy shop --image=…:v2 --no-traffic --tag=canary` → `gcloud run services update-traffic shop --to-revisions=shop-v2=10`
- **Not to be confused with:** a new service.
- **Analogy:** 🍽️ A new edition of the same menu.
- **In the online store:** checkout v2 for 10% of shoppers.

### 2. Service
- **What it is:** The named app with one URL, made of revisions.
- **Looks like:** `shop`
- **Not to be confused with:** revision.
- **Analogy:** 🍽️ The restaurant.
- **In the online store:** The storefront service.

### 🔗 How they fit together
```
 service shop
   revision v1 ◄ 90%
   revision v2 ◄ 10% (canary) ✅
```

---

## 🌍 Real-World Scenario

A team releases a new checkout on Cloud Run. They deploy it as a **new revision** with no traffic, then shift **10%** of users to it, watch errors, and roll forward or back.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a new service with the new version of the application. Split traffic between this version and the version that is currently running.

**Wrong words:**
- ❌ "**Create a new service**": a different service has a different URL. Traffic splitting works **between revisions of one service**.

📌 **When to use it:** Use a new service for a different app.
🏢 **Office example:** Opening a second restaurant to test one dish.

### ✅ B
> **B.** Create a new revision with the new version of the application. Split traffic between this version and the version that is currently running.

**Why it's correct:**
- ✔️ "**Create a new revision with the new version**" matches "**evaluate an updated version**".
- ✔️ "**Split traffic between this version and the version that is currently running**" matches "**specific percentage of your production users (canary deployment)**".

📌 **When to use it:** Use it when a small share of people should try the new version first.
🏢 **Office example:** Handing the new menu edition to 1 in 10 guests in the same restaurant.

### ❌ C
> **C.** Create a new service with the new version of the application. Add an HTTP Load Balancer in front of both services.

**Wrong words:**
- ❌ "**new service … HTTP Load Balancer in front of both**": extra infrastructure for something Cloud Run does built in.

📌 **When to use it:** Use an LB for routing across different services or regions.
🏢 **Office example:** Building a new front door to choose between two restaurants.

### ❌ D
> **D.** Create a new revision with the new version of the application. Add an HTTP Load Balancer in front of both revisions.

**Wrong words:**
- ✔️ "new revision" is right.
- ❌ "**HTTP Load Balancer in front of both revisions**": not needed. Cloud Run splits traffic natively.

📌 **When to use it:** Use an LB for multi-region or custom domains.
🏢 **Office example:** Hiring a host to do what the waiter already does.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud run deploy checkout --image=…/checkout:v2 --no-traffic --tag=v2
gcloud run services update-traffic checkout --to-tags=v2=10
```

---

## 🧠 Key Takeaways / Memory Tips

- **Canary on Cloud Run → new revision + traffic split.** (App Engine: new version + split, Q076.)
  🧠 *"**Same service, new revision, split it.**"*
- Related: **Q076**, **Q056**, **Q185**.

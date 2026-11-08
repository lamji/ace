# Q253: Serverless App: Test a New Version on a Small % of Traffic (Cloud Run Gradual Rollouts)

**Topic:** Cloud Run (traffic splitting)

## ❓ Question
> You need to deploy an application in Google Cloud using serverless technology. You want to test a new version of the application with a small percentage of production traffic. What should you do?
>
> **A.** Deploy the application to Cloud Run. Use gradual rollouts for traffic splitting.
>
> **B.** Deploy the application to Google Kubernetes Engine. Use Anthos Service Mash for traffic splitting.
>
> **C.** Deploy the application to Cloud Functions. Specify the version number in the functions name.
>
> **D.** Deploy the application to App Engine. For each new version, create a new service.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will run an app with serverless technology.
- **What you must achieve:** Test a new version with a small percentage of real traffic.
- **The limits:** None stated.
- **What they're really asking:** Which serverless service lets you split traffic between versions?

**Clues in the question:**
- "**serverless**" + "**small percentage of production traffic**" → **Cloud Run** revisions with **traffic splitting / gradual rollout**.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Gradual rollout 🔑 (review from Q166)
- **What it is:** Deploy a new revision with no traffic, then shift 5% → 25% → 100%.
- **Looks like:** `gcloud run services update-traffic app --to-revisions=app-v2=5`
- **Not to be confused with:** new service.
- **Analogy:** 🍽️ New recipe for a few guests first.
- **In the online store:** Checkout v2.

### 🔗 How they fit together
```
 Cloud Run service: v1 95% | v2 5% ✅ → increase gradually
```

---

## 🌍 Real-World Scenario

A team deploys a new Cloud Run revision and sends **5%** of users to it, increasing as errors stay low.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the application to Cloud Run. Use gradual rollouts for traffic splitting.

**Why it's correct:**
- ✔️ "**Deploy the application to Cloud Run**" matches "**using serverless technology**".
- ✔️ "**Use gradual rollouts for traffic splitting**" matches "**small percentage of production traffic**".

📌 **When to use it:** Use it when a few real users should try the new version before everyone.
🏢 **Office example:** Serving the new recipe to a few tables first.

### ❌ B
> **B.** Deploy the application to Google Kubernetes Engine. Use Anthos Service Mash for traffic splitting.

**Wrong words:**
- ❌ "**Google Kubernetes Engine … Anthos Service Mesh**": not serverless, and a lot to set up.

📌 **When to use it:** Use a service mesh for complex GKE traffic control.
🏢 **Office example:** Building a control tower to test one dish.

### ❌ C
> **C.** Deploy the application to Cloud Functions. Specify the version number in the functions name.

**Wrong words:**
- ❌ "**version number in the functions name**": makes a separate function with its own URL; no traffic split.

📌 **When to use it:** Use separate function names for separate functions.
🏢 **Office example:** Opening a new restaurant for each recipe.

### ❌ D
> **D.** Deploy the application to App Engine. For each new version, create a new service.

**Wrong words:**
- ❌ "**create a new service**": App Engine splits traffic between **versions** of one service, not between services.

📌 **When to use it:** Use new versions (not services) for App Engine canaries.
🏢 **Office example:** A new department for each draft.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy checkout --image=…:v2 --no-traffic --tag=v2 && gcloud run services update-traffic checkout --to-tags=v2=5`

---

## 🧠 Key Takeaways / Memory Tips

- **Serverless canary → Cloud Run revisions + traffic split.**
  🧠 *"**Small slice, new revision.**"*
- Related: **Q166**, **Q185**, **Q255**.

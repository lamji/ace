# Q185: Test Updates on a Small Part of Real Traffic (App Engine New Version + Traffic Splitting)

**Topic:** App Engine (versions, traffic splitting)

## ❓ Question
> You are developing a new web application that will be deployed on Google Cloud Platform. As part of your release cycle, you want to test updates to your application on a small portion of real user traffic. The majority of the users should still be directed towards a stable version of your application. What should you do?
>
> **A.** Deploy the application on App Engine. For each update, create a new version of the same service. Configure traffic splitting to send a small percentage of traffic to the new version.
>
> **B.** Deploy the application on App Engine. For each update, create a new service. Configure traffic splitting to send a small percentage of traffic to the new service.
>
> **C.** Deploy the application on Kubernetes Engine. For a new release, update the deployment to use the new version.
>
> **D.** Deploy the application on Kubernetes Engine. For a new release, create a new deployment for the new version. Update the service to use the new deployment.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Send a **small part** of real users to the update; most stay on the stable version.

**Clues in the question:**
- "**small portion of real user traffic**" + "**majority … stable version**" → **App Engine versions + traffic splitting** (Q076).

**Exam topic:** App Engine.

---

## 📚 Key Terms Explained

### 1. App Engine version + traffic splitting 🔑 (review from Q076)
- **What it is:** Each deploy of a service makes a **version**. Traffic can be split by percentage between versions of the **same service**.
- **Looks like:** `gcloud app services set-traffic default --splits=v1=0.9,v2=0.1`
- **Not to be confused with:** a new service.
- **Analogy:** 🍽️ 10% of guests get the new recipe.
- **In the online store:** Test new checkout UI.

### 🔗 How they fit together
```
 service default: v1 ◄ 95% | v2 ◄ 5% ✅
```

---

## 🌍 Real-World Scenario

A team deploys `v2` of their App Engine service with `--no-promote` and sends **5%** of users to it while watching errors.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the application on App Engine. For each update, create a new version of the same service. Configure traffic splitting to send a small percentage of traffic to the new version.

**Why it's correct:**
- ✔️ "**create a new version of the same service**" matches "**test updates to your application**".
- ✔️ "**traffic splitting … small percentage of traffic to the new version**" matches "**small portion of real user traffic**" + "**majority … stable version**".

📌 **When to use it:** Use it when you want a few real customers to try something new before everyone gets it.
🏢 **Office example:** Giving the new form to one in twenty visitors at the front desk.

### ❌ B
> **B.** Deploy the application on App Engine. For each update, create a new service. Configure traffic splitting to send a small percentage of traffic to the new service.

**Wrong words:**
- ❌ "**create a new service**": traffic splitting works **between versions of one service**, not between services.

📌 **When to use it:** Use a new service for a different app part (e.g. an API).
🏢 **Office example:** Opening a new department to test one form.

### ❌ C
> **C.** Deploy the application on Kubernetes Engine. For a new release, update the deployment to use the new version.

**Wrong words:**
- ❌ "**update the deployment to use the new version**": a rolling update moves **everyone** to the new version.

📌 **When to use it:** Use it for a normal full rollout.
🏢 **Office example:** Replacing the form for everyone at once.

### ❌ D
> **D.** Deploy the application on Kubernetes Engine. For a new release, create a new deployment for the new version. Update the service to use the new deployment.

**Wrong words:**
- ❌ "**Update the service to use the new deployment**": switches **all** traffic at once, no small portion.

📌 **When to use it:** Use it for a blue/green switch-over.
🏢 **Office example:** Flipping every visitor to the new desk at once.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud app deploy --version=v2 --no-promote
gcloud app services set-traffic storefront --splits=v1=0.95,v2=0.05 --split-by=cookie
```

---

## 🧠 Key Takeaways / Memory Tips

- **Small % of real traffic on App Engine → new version + traffic splitting.** (Cloud Run: new revision, Q166.)
  🧠 *"**Same service, new version, split.**"*
- Related: **Q076**, **Q166**.

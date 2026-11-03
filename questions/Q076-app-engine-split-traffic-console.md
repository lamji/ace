# Q076: Testing a New App Engine Version With 1% of Users (Split Traffic Between Versions)

**Topic:** App Engine (versions, traffic splitting in the console, one app per project)

## ❓ Question
> You are building a new version of an application hosted in an App Engine environment. You want to test the new version with 1% of users before you completely switch your application over to the new version. What should you do?
>
> **A.** Deploy a new version of your application in Google Kubernetes Engine instead of App Engine and then use GCP Console to split traffic.
>
> **B.** Deploy a new version of your application in a Compute Engine instance instead of App Engine and then use GCP Console to split traffic.
>
> **C.** Deploy a new version as a separate app in App Engine. Then configure App Engine using GCP Console to split traffic between the two apps.
>
> **D.** Deploy a new version of your application in App Engine. Then go to App Engine settings in GCP Console and split traffic between the current version and newly deployed versions accordingly.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> 💡 This is the same idea as **Q056** (which you got right): App Engine keeps several **versions** in one app and can **split traffic** between them.

---

## 📖 What the Question Is Asking

**In plain words:** Your app runs on App Engine. You made a new version and want **1% of users** to try it before everyone gets it. How?

**Clues in the question:**
- "**new version of an application hosted in an App Engine environment**": stay on App Engine; it supports **many versions** in the same app.
- "**test the new version with 1% of users**": **traffic splitting** between versions.
- "**before you completely switch**": later you move 100% (migrate). Today: 99/1.

**Exam topic:** App Engine.

---

## 📚 Key Terms Explained

### 1️⃣ App Engine version (review from Q056)
- **What it is:** Each deploy creates a **version** of a service. Several versions can run side by side, and you choose how much traffic each gets.
- **Looks like:** service `default` → versions `v1` (live), `v2` (new)
- **Not to be confused with:** a separate App Engine **application**. Versions live **inside** the one app.
- **Analogy:** 🍽️ **Two menus** in the same restaurant.
- **In the online store:** `v1` = current checkout, `v2` = redesigned checkout.

### 2️⃣ Traffic splitting 🔑
- **What it is:** A built-in App Engine setting that sends a **percentage of users** to each version (e.g., 99% → v1, 1% → v2). In the console: **App Engine → Versions → Split traffic**.
- **Looks like:** `gcloud app services set-traffic default --splits=v1=99,v2=1`
- **Not to be confused with:** a load balancer you build yourself.
- **Analogy:** 🍽️ The host hands the **test menu to 1 in every 100 guests**.

### 3️⃣ One App Engine app per project (review from Q037)
- **What it is:** A project can have **only one** App Engine application.
- **Not to be confused with:** services and versions, which you can have many of.
- **Analogy:** 🏢 **One restaurant per building**, but many menus.

### 4️⃣ GKE / Compute Engine
- **What it is:** Other places to run apps: Kubernetes clusters and VMs.
- **Not to be confused with:** App Engine. Moving the new version there means **re-platforming**, and their traffic isn't split from the App Engine console.
- **Analogy:** 🏗️ **Opening a new restaurant elsewhere** just to test one dish.

### 🔗 How they fit together
```
 📁 project
   🏢 App Engine app (only one)
      └── service default
            ├── v1 ◄── 99% ┐
            └── v2 ◄──  1% ┘ Console → Versions → Split traffic ✅
```

---

## 🌍 Real-World Scenario

Before a big release, teams run a **canary**: a small share of users get the new version while everyone else stays on the old one. On App Engine, the engineer deploys `v2` without promoting it, opens **Versions → Split traffic**, sets 1% to v2, and watches errors. If all is well, they raise it step by step to 100%.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy a new version of your application in Google Kubernetes Engine instead of App Engine and then use GCP Console to split traffic.

**Wrong words:**
- ❌ "**in Google Kubernetes Engine instead of App Engine**": moving the app to a different platform just to test a version is a big rebuild, and App Engine can't split its traffic to a GKE app.

📌 **When to use it:** Use GKE when you're deliberately moving the whole app to Kubernetes.
🏢 **Office example:** Opening a new branch office just to test a new form with a few customers.

### ❌ B
> **B.** Deploy a new version of your application in a Compute Engine instance instead of App Engine and then use GCP Console to split traffic.

**Wrong words:**
- ❌ "**in a Compute Engine instance instead of App Engine**": same problem as A. A different platform, and the console's App Engine traffic split can't send users to a VM.

📌 **When to use it:** Use a VM when you need full control of the server and are moving the app there on purpose.
🏢 **Office example:** Renting a separate office just to test one new procedure.

### ❌ C
> **C.** Deploy a new version as a separate app in App Engine. Then configure App Engine using GCP Console to split traffic between the two apps.

**Wrong words:**
- ❌ "**Deploy a new version as a separate app**": a project can have **only one** App Engine app (Q037).
- ❌ "**split traffic between the two apps**": traffic splitting works between **versions** of one app, not between apps.

📌 **When to use it:** **Never use this.** Deploy a new **version** in the same app (D).
🏢 **Office example:** Opening a second reception desk in the same building, which the rules don't allow.

### ✅ D
> **D.** Deploy a new version of your application in App Engine. Then go to App Engine settings in GCP Console and split traffic between the current version and newly deployed versions accordingly.

**Why it's correct:**
- ✔️ "**Deploy a new version of your application in App Engine**" matches "**new version of an application hosted in an App Engine environment**": the new version lives next to the old one in the same app.
- ✔️ "**split traffic between the current version and newly deployed versions**" matches "**test the new version with 1% of users**": set 99% current, 1% new.
- ✔️ "**accordingly**" matches "**before you completely switch**": you can raise the split step by step up to 100%.

📌 **When to use it:** Use it when a small group of people should try a new version before everyone gets it.
🏢 **Office example:** Giving the new expense form to 1 in every 100 employees before rolling it out to all.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud app deploy --version=v2 --no-promote          # v2 gets 0% traffic
gcloud app services set-traffic default --splits=v1=99,v2=1 --split-by=cookie
# (same as Console → App Engine → Versions → Split traffic)
```

- Monday: 1% of shoppers see the new checkout. Errors and sales look good.
- Wednesday: 10%. Friday: 100% (`--migrate`).
- If v2 breaks: `--splits=v1=100` sends everyone back in seconds.

---

## 🧠 Key Takeaways / Memory Tips

- **"X% of users try the new version" on App Engine → new version in the same app + split traffic.**
- **One App Engine app per project.** Versions, not apps.
- Moving to GKE or Compute Engine is never the answer for an App Engine canary.
  🧠 *"**Same app, new version, split the traffic.**"*
- Related: **Q056** (--splits 99/1 vs --migrate), **Q037** (one app per project).

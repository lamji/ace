# Q056: Showing a New Version to 1% of Users (App Engine Traffic Splitting)

**Topic:** App Engine (versions, traffic splitting with `--splits`, `--migrate`, one App Engine app per project)

## ❓ Question
> You have a website hosted on App Engine standard environment. You want 1% of your users to see a new test version of the website. You want to minimize complexity. What should you do?
>
> **A.** Deploy the new version in the same application and use the --migrate option.
>
> **B.** Deploy the new version in the same application and use the --splits option to give a weight of 99 to the current version and a weight of 1 to the new version.
>
> **C.** Create a new App Engine application in the same project. Deploy the new version in that application. Use the App Engine library to proxy 1% of the requests to the new version.
>
> **D.** Create a new App Engine application in the same project. Deploy the new version in that application. Configure your network load balancer to send 1% of the traffic to that new application.

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A website runs on App Engine standard.
- **What you must achieve:** Show a new test version to 1% of users.
- **The limits:** Keep it simple.
- **What they're really asking:** How do you send 1% of visitors to the new version?

| Keyword | What it hints at |
|---|---|
| "**1% of your users**" | Send a **share** of traffic to the new version → **traffic splitting** |
| "**new test version**" | App Engine keeps **multiple versions** in the same app |
| "**minimize complexity**" | Use App Engine's **built-in** feature. No new apps, proxies or load balancers |

**Exam topic:** App Engine.

---

## 📚 Key Terms Explained

### 1️⃣ App Engine Version
- **What it is:** Every `gcloud app deploy` creates a **version** of a service. Many versions can exist side by side, and you choose **how much traffic each one gets**.
- **Looks like:** `default` service → versions `v1` (live), `v2` (new)
- **Not to be confused with:** a new **App Engine application**. Versions live **inside** the one application.
- **Analogy:** 🍽️ **Two menus** in the same restaurant: the regular one and a new test menu.
- **In the online store:** `v1` = current storefront, `v2` = new checkout design.

### 2️⃣ Traffic Splitting (`--splits`) 🔑
- **What it is:** Telling App Engine to send a **percentage of traffic** to each version, for example **99% → v1, 1% → v2**. Users can be split by **IP**, **cookie** (sticky per user) or **random**.
- **Looks like:**
  ```bash
  gcloud app services set-traffic default --splits=v1=99,v2=1 --split-by=cookie
  ```
- **Not to be confused with:** a load balancer you configure yourself. It's **built into App Engine**.
- **Analogy:** 🍽️ The host hands the **test menu to 1 in every 100 guests**.
- 💡 *Exam detail:* in real gcloud, `--splits` is on **`gcloud app services set-traffic`** (run after deploying with `--no-promote`), not on `gcloud app deploy`. The idea in option B is still the right one.

### 3️⃣ `--migrate`
- **What it is:** An option that **moves ALL traffic** from the old version to the new version (gradually), switching everyone over.
- **Looks like:** `gcloud app services set-traffic default --splits=v2=1 --migrate`
- **Not to be confused with:** a partial split. Migrate = **100%** to the new version.
- **Analogy:** 🍽️ **Replacing the menu for every guest.**

### 4️⃣ One App Engine Application per Project (review from Q037)
- **What it is:** Each project can have **only one** App Engine application. You can't create a second one in the same project.
- **Not to be confused with:** services and versions. You can have many of those inside the one app.

### 🔗 How They Fit Together
```
📁 shopnow-prod
  🏢 App Engine application (only one)
     └── service: default
           ├── v1 (current)  ◄── 99% of users
           └── v2 (new test) ◄──  1% of users     ← --splits v1=99,v2=1 ✅

❌ A: --migrate → 100% to v2
❌ C/D: a 2nd App Engine app in the same project → not allowed
```

---

## 🌍 Real-World Scenario

Teams rarely release a new version to everyone at once. They do a **canary release**: send **1–5%** of users to the new version, watch error rates and sales, then raise the percentage or roll back. App Engine has this built in, so it's a single command with no extra infrastructure.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the new version in the same application and use the --migrate option.

**Wrong words:**
- ✔️ "Deploy the new version in the same application" is right.
- ❌ "**use the --migrate option**": migrate sends **all** traffic (100%) to the new version, not 1%.

**📌 When to use it:** Use it when the new version is ready for everyone and you want to switch all traffic over.
🏢 **Office example:** Replacing the old forms with the new forms for every employee on Monday.

### ✅ B (your answer)
> **B.** Deploy the new version in the same application and use the --splits option to give a weight of 99 to the current version and a weight of 1 to the new version.

**Why it's correct:**
- ✔️ "**same application**": versions live inside the one App Engine app.
- ✔️ "**--splits … 99 … 1**": built-in traffic splitting sends exactly **1%** to the new version.
- ✔️ One command, nothing extra to build, which is minimal complexity.

**📌 When to use it:** Use it when you want a small group of users to try a new version before everyone gets it.
🏢 **Office example:** Giving the new expense form to 1 in every 100 employees to test it before rolling it out.

### ❌ C
> **C.** Create a new App Engine application in the same project. Deploy the new version in that application. Use the App Engine library to proxy 1% of the requests to the new version.

**Wrong words:**
- ❌ "**Create a new App Engine application in the same project**": only **one** App Engine app is allowed per project (Q037).
- ❌ "**Use the App Engine library to proxy 1% of the requests**": you'd have to write your own forwarding code. That's complex, and App Engine already does this for you.

**📌 When to use it:** **Never use this.** You can't have two apps in one project, and splitting is built in. Use B.
🏢 **Office example:** Opening a second reception desk in the same building (not allowed) and hand-forwarding 1 in 100 visitors.

### ❌ D
> **D.** Create a new App Engine application in the same project. Deploy the new version in that application. Configure your network load balancer to send 1% of the traffic to that new application.

**Wrong words:**
- ❌ "**Create a new App Engine application in the same project**": not allowed (one per project).
- ❌ "**Configure your network load balancer**": extra infrastructure to set up and maintain, and App Engine already splits traffic itself.

**📌 When to use it:** **Never use this** for App Engine versions. Use the built-in split (B).
🏢 **Office example:** Hiring a traffic officer to direct visitors when the receptionist already does it.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow built a **new checkout page** and wants 1% of shoppers to try it.

```bash
# Deploy v2 without sending it any traffic yet
gcloud app deploy app.yaml --version=v2 --no-promote

# Send 1% of shoppers to v2 (sticky per shopper via cookie)
gcloud app services set-traffic default --splits=v1=99,v2=1 --split-by=cookie
```

| Day | Split | What the team watches |
|---|---|---|
| Mon | v1 99% / v2 1% | Errors and checkout completion on v2 |
| Wed | v1 90% / v2 10% | Looks good, raise it |
| Fri | `--migrate` → v2 100% | Everyone gets the new checkout ✅ |

If v2 has a bug: `--splits=v1=100` returns everyone to the old version in seconds.

---

## 🧠 Key Takeaways / Memory Tips

- **"X% of users see the new version" on App Engine → traffic splitting (`--splits`).**
  🧠 *"**Splits = share. Migrate = move everyone.**"*
- **Versions live inside the one App Engine app.** Never create a second app in the same project.
- **Minimize complexity** = use the built-in feature, not proxies or load balancers.
- Related: **Q037** (one App Engine app per project), **Q024** (deploy to App Engine).

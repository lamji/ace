# Q045: Roll Back a Buggy App Engine Release (Route 100% Traffic to the Previous Version)

**Topic:** App Engine (versions and traffic splitting)

## ❓ Question
> You recently deployed a new version of an application to App Engine and then discovered a bug in the release. You need to immediately revert to the prior version of the application. What should you do?
>
> **A.** Run gcloud app restore.
>
> **B.** On the App Engine page of the GCP Console, select the application that needs to be reverted and click Revert.
>
> **C.** On the App Engine Versions page of the GCP Console, route 100% of the traffic to the previous version.
>
> **D.** Deploy the original version as a separate application. Then go to App Engine settings and split traffic between applications so that the original version serves 100% of the requests.

**My answer:** — (didn't know)
**Correct answer:** C. On the App Engine Versions page of the GCP Console, route 100% of the traffic to the previous version.
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You pushed a new release to App Engine and it has a bug. How do you switch back to the old, working release **right now**?

**Clues in the question:**
- "**new version**" + "**prior version**": App Engine keeps old **versions** after you deploy a new one, so the old one is still there.
- "**immediately revert**": you want a quick switch, not a rebuild or a redeploy.

**Exam topic:** App Engine (versions, traffic splitting, rollback).

---

## 📚 Key Terms Explained

### 1. App Engine
- **What it is:** A Google Cloud service that runs your web app for you. You upload your code, and Google runs the servers, scaling and patching.
- **Looks like:** `gcloud app deploy app.yaml` → your app is live at `https://shopnow.uc.r.appspot.com`
- **Not to be confused with:** Compute Engine, where you rent and manage the virtual machines yourself.
- **Analogy:** 🏨 A serviced office. You bring your work; the building handles power, cleaning and security.
- **In the online store:** The storefront API could run on App Engine as the `default` service.

### 2. Application (App Engine app)
- **What it is:** The single top-level App Engine container in a project. **Each project can have only one App Engine application**, and it holds all your services and versions.
- **Looks like:** Project `shopnow-prod` → App Engine app (region `us-central`) → services `default`, `checkout`
- **Not to be confused with:** a version. "Application" is the whole thing; a version is one release inside it.
- **Analogy:** 🏢 The company. There is only one company per building lease.
- **In the online store:** `shopnow-prod` has one App Engine app containing the `default` (storefront) and `checkout` services.

### 3. Version 🔑
- **What it is:** One saved, runnable copy of your code inside a service. Each deploy creates a new version (with an ID like `20261103t101500`). Old versions stay until you delete them.
- **Looks like:**
  ```
  $ gcloud app versions list
  SERVICE  VERSION.ID        TRAFFIC_SPLIT  SERVING_STATUS
  default  20261101t090000  0.00           SERVING
  default  20261103t101500  1.00           SERVING   ← new, buggy
  ```
- **Not to be confused with:** a backup you have to restore. A version is already deployed and ready to serve; it just has 0% of the traffic.
- **Analogy:** 📄 Drafts of a letter kept in the drawer. Version 2 has a typo, so you hand out version 1 again. No retyping.
- **In the online store:** Monday's storefront release is `v1`, Wednesday's is `v2`. Both exist side by side.

### 4. Traffic splitting / migrating traffic 🔑
- **What it is:** A setting that decides what **percentage of requests** each version gets. Moving 100% to one version is how you switch releases instantly, and how you roll back.
- **Looks like:** `gcloud app services set-traffic default --splits=20261101t090000=1`
- **Not to be confused with:** load balancing between different apps or projects. Traffic splitting works **between versions of one service**.
- **Analogy:** 🛎️ The receptionist who decides which desk visitors go to. Point everyone back to the old desk.
- **In the online store:** Send 100% of shoppers back to the storefront `v1` while the `v2` bug gets fixed.

### 🔗 How they fit together
```
Project (shopnow-prod)
└── App Engine application   ← only ONE per project
    └── Service: default
        ├── Version v1 (old, works)   traffic 0%  →  set to 100% ✅
        └── Version v2 (new, buggy)   traffic 100% →  set to 0%
```

---

## 🌍 Real-World Scenario

Friday afternoon, your team deploys a new release. Ten minutes later, support tickets come in: the "Add to cart" button is broken. You don't have time to find the bug, rebuild and redeploy. The previous release is still sitting in App Engine, so you open **App Engine → Versions**, select the previous version, and click **Migrate traffic** (or set its split to 100%). Users are back on the working release within seconds. Then you fix the bug calmly.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Run gcloud app restore.

**Wrong words:**
- ❌ "**gcloud app restore**": this command does not exist. The real rollback command is `gcloud app services set-traffic` (or `gcloud app versions migrate`).

📌 **When to use it:** Never use this; it's a made-up command. Move traffic back to the old version instead.
🏢 **Office example:** Asking IT for an "undo the whole week" button that was never built.

### ❌ B
> **B.** On the App Engine page of the GCP Console, select the application that needs to be reverted and click Revert.

**Wrong words:**
- ❌ "**click Revert**": the Console has no "Revert" button for App Engine. You roll back by moving traffic between versions.
- ❌ "**select the application**": a project has only one App Engine application. You choose a **version**, not an application.

📌 **When to use it:** Never use this; that button doesn't exist. Use the Versions page and move 100% of the traffic.
🏢 **Office example:** Looking for an "undo" stamp at the front desk when the fix is to hand out last week's form again.

### ✅ C
> **C.** On the App Engine Versions page of the GCP Console, route 100% of the traffic to the previous version.

**Why it's correct:**
- ✔️ "**App Engine Versions page**" matches "**prior version of the application**": old versions stay deployed and are listed there.
- ✔️ "**route 100% of the traffic to the previous version**" matches "**immediately revert**": it's one setting change, with no rebuild and no redeploy, so users are back on the working release in seconds.

The same thing from the command line:
```
gcloud app versions list --service=default
gcloud app services set-traffic default --splits=PREVIOUS_VERSION_ID=1
```
`versions list` shows which version is the old one. `set-traffic ... =1` sends 100% (written as `1`) of the `default` service's traffic to that version.

📌 **When to use it:** Use it when a new release is broken and the old one is still there to switch back to.
🏢 **Office example:** The new form has a typo, so the receptionist hands out last week's form again from the drawer.

### ❌ D
> **D.** Deploy the original version as a separate application. Then go to App Engine settings and split traffic between applications so that the original version serves 100% of the requests.

**Wrong words:**
- ❌ "**Deploy the original version as a separate application**": a project can have only one App Engine application, and redeploying is slow. The old version is already deployed.
- ❌ "**split traffic between applications**": traffic splitting works only **between versions of the same service**, not between applications.

📌 **When to use it:** Never use this; you can't split traffic between applications. Move the traffic between versions instead.
🏢 **Office example:** Opening a whole new branch office just to hand out an old form you already have in the drawer.

---

## 🛒 E-Commerce Full-Stack Example

- The ShopNow storefront API runs on App Engine as the `default` service.
- Monday's deploy created `v1` (works). Wednesday's deploy created `v2`, which breaks checkout totals.
- Rollback: `gcloud app services set-traffic default --splits=v1=1`. Shoppers are back on `v1` within seconds. Cloud SQL orders and Cloud Storage product images are untouched, because only the code version changed.
- Safer next time: deploy `v2` with `gcloud app deploy --no-promote` (it gets 0% traffic), test it at its own version URL, then send 5% of traffic to it before moving everyone over.

---

## 🧠 Key Takeaways / Memory Tips

- **App Engine rollback = move 100% of the traffic back to the previous version.** Old versions stay deployed, so nothing needs to be rebuilt.
- One project = **one** App Engine application. Traffic splits are between **versions**, never between applications.
- 🧠 *"**Don't restore, don't redeploy: re-route.**"*
- If you see "App Engine" + "revert" / "roll back" / "canary" / "A/B test" → think **traffic splitting between versions**.

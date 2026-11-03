# Q037: Moving an App Engine App to Another Region (New Project Required)

**Topic:** App Engine (region is permanent, one App Engine app per project, `gcloud app create --region`)

## ❓ Question
> You created a Google Cloud Platform project with an App Engine application inside the project. You initially configured the application to be served from the us-central region. Now you want the application to be served from the asia-northeast1 region. What should you do?
>
> **A.** Change the default region property setting in the existing GCP project to asia-northeast1.
>
> **B.** Change the region property setting in the existing App Engine application from us-central to asia-northeast1.
>
> **C.** Create a second App Engine application in the existing GCP project and specify asia-northeast1 as the region to serve your application.
>
> **D.** Create a new GCP project and create an App Engine application inside this new project. Specify asia-northeast1 as the region to serve your application.

**My answer:** B
**Correct answer:** D
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** Your App Engine app runs in **us-central**. You want it to run in **asia-northeast1 (Tokyo)** instead. How do you move it?

Two App Engine rules decide the answer:
1. **The region can't be changed** after the App Engine app is created.
2. **Each project can have only ONE App Engine app.**

So the only way is a **new project** with a **new App Engine app** in Tokyo, and then you deploy your code there.

| Keyword | What it hints at |
|---|---|
| "**initially configured** … **us-central**" | The region was chosen at creation, and **it's permanent** |
| "**Now you want** … **asia-northeast1**" | You can't edit it, so you need a **new App Engine app** |
| "**App Engine application inside the project**" | One per project, so the new app needs a **new project** |

**Exam topic:** App Engine.

---

## 📚 Key Terms Explained

### 1️⃣ App Engine Application 🔑
- **What it is:** The **one App Engine "container" per project** that holds all your App Engine services and versions. You create it **once** with `gcloud app create`, and **you pick its region then, forever**.
- **Looks like:**
  ```bash
  gcloud app create --project=shopnow-prod --region=us-central
  gcloud app describe --project=shopnow-prod
  # locationId: us-central   ← can never be edited
  ```
- **Not to be confused with:** a **service** or **version** inside it (`default`, `api`, `v20261024`). You can have many services, but **one application** per project.
- **Analogy:** 🏢 A **lease on one office building**, signed for a specific city. You can rearrange the floors, but you can't move the building to Tokyo.
- **In the online store:** ShopNow's storefront API runs on App Engine in `shopnow-prod`.

### 2️⃣ Region
- **What it is:** A **geographic area** where Google has data centers, like `us-central` (Iowa) or `asia-northeast1` (Tokyo). Serving from a region close to users makes pages load faster.
- **Looks like:** `us-central`, `europe-west`, `asia-northeast1`
- **Not to be confused with:** a **zone** (one data center inside a region, like `asia-northeast1-a`).
- **Analogy:** 🌏 The **city** where your office is.

### 3️⃣ Project Default Region (gcloud / Compute setting)
- **What it is:** A **default value** used by commands (mostly Compute Engine) **when you don't specify a region**. It's a convenience setting only.
- **Looks like:** `gcloud config set compute/region asia-northeast1`, or project metadata `google-compute-default-region`
- **Not to be confused with:** where existing resources live. Changing it **moves nothing**, and it doesn't affect an existing App Engine app.
- **Analogy:** 📝 Changing the **default city on the booking form**. It doesn't move offices you already have.

### 4️⃣ `gcloud app create` and `gcloud app deploy` (review from Q024)
- **What it is:** `app create` sets up the App Engine application **and its region** (once per project). `app deploy` **uploads your code** to it.
- **Looks like:** `gcloud app create --region=asia-northeast1 --project=shopnow-jp` then `gcloud app deploy --project=shopnow-jp`

### 🔗 How They Fit Together
```
📁 shopnow-prod                          📁 shopnow-jp  (NEW project)
   🏢 App Engine app                         🏢 App Engine app
      region: us-central (permanent 🔒)          region: asia-northeast1 ✅
      ├─ service: default                        ├─ service: default
      └─ service: api                            └─ service: api
                                              ▲
                     same source code ────────┘  gcloud app deploy --project=shopnow-jp

❌ A: project default region → just a default for new commands, moves nothing
❌ B: edit the app's region → not allowed
❌ C: second App Engine app in the same project → only one allowed
```

---

## 🌍 Real-World Scenario

A company launched its app in the US, and now **most customers are in Japan**. Pages are slow because every request travels across the Pacific. They want the app **served from Tokyo**. With App Engine, the region is fixed when the app is created. So the team **creates a new project**, sets up App Engine in **asia-northeast1**, **deploys the same code**, moves the data and DNS over, and later shuts down the old one. (That's why you should pick the App Engine region carefully on day one.)

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Change the default region property setting in the existing GCP project to asia-northeast1.

**Why it's wrong:**
- ❌ The project's **default region** is only used for **new** resources when you don't name a region (mostly Compute Engine). It **doesn't move** anything that exists, and the App Engine app stays in us-central.

**📌 When to use it:** Use it to save typing when you usually create new resources in the same region.
🏢 **Office example:** Changing the default city on the company travel booking form. Existing offices don't move.

### ❌ B (your answer)
> **B.** Change the region property setting in the existing App Engine application from us-central to asia-northeast1.

**Why it's wrong:**
- ❌ **An App Engine app's region can't be changed** after creation. There's no setting to edit it.
- 💡 **Likely mix-up:** It sounds like the most direct fix, and many services do let you change settings. But App Engine's location is **permanent**, the same "region is permanent" note from Q024.

**📌 When to use it:** **Never use this.** The region can't be edited. Create a new project with a new App Engine app (D).
🏢 **Office example:** Trying to edit the city on a signed building lease. You have to sign a new lease in the new city.

### ❌ C
> **C.** Create a second App Engine application in the existing GCP project and specify asia-northeast1 as the region to serve your application.

**Why it's wrong:**
- ❌ **Only one App Engine application per project.** `gcloud app create` fails if one already exists.
- 💡 You **can** have many **services** in one app, but they all share the **same region**.

**📌 When to use it:** **Never use this.** A project can't hold a second App Engine app. Use a new project (D).
🏢 **Office example:** Trying to sign a second lease for the same company address. The building only allows one tenant.

### ✅ D
> **D.** Create a new GCP project and create an App Engine application inside this new project. Specify asia-northeast1 as the region to serve your application.

**Why it's correct:**
- ✔️ **New project** → room for a **new App Engine app** (one per project).
- ✔️ **Pick asia-northeast1** when creating it, the only moment you can choose the region.
- ✔️ Then **deploy the same code** there (as in Q024).

**📌 When to use it:** Use it when an App Engine app must run from a different region than it was created in.
🏢 **Office example:** Signing a new lease in Tokyo and moving the team and files there.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's storefront API runs on App Engine in **`shopnow-prod` (us-central)**. A Japanese partnership means **70% of shoppers are now in Japan**, and checkout feels slow there.

```bash
# ① New project (link billing, Q035)
gcloud projects create shopnow-jp
gcloud billing projects link shopnow-jp --billing-account=01A2B3-C4D5E6-F7G8H9

# ② App Engine in Tokyo: the region is chosen now, permanently
gcloud app create --project=shopnow-jp --region=asia-northeast1

# ③ Deploy the same tested code (Q024)
gcloud app deploy app.yaml --project=shopnow-jp
```

**Then:** point `shop.jp.shopnow.com` at the new app and move the Japanese customer data.

| Try | What happens |
|---|---|
| B: edit region in `shopnow-prod` | No such setting. `locationId` stays `us-central` ❌ |
| C: `gcloud app create --region=asia-northeast1 --project=shopnow-prod` | Error: "app already exists" ❌ |
| **D** | Tokyo app live, pages load much faster for Japanese shoppers ✅ |

---

## 🧠 Key Takeaways / Memory Tips

- **App Engine region = permanent. One App Engine app per project.** → New region = **new project + new App Engine app**.
  🧠 *"**App Engine signs a lease in one city. To move cities, open a new branch (project).**"*
- **Project default region** only affects new resources when no region is named. It **moves nothing**.
- Choose the App Engine region **carefully** at `gcloud app create`.
- Related: **Q024** (create project, then deploy, and "region is permanent").

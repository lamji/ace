# Q031: Turning On the Pub/Sub API Before Your App Can Use It

**Topic:** APIs & Services (enabling APIs in the API Library), Pub/Sub, App Engine service accounts

## ❓ Question
> You want to send and consume Cloud Pub/Sub messages from your App Engine application. The Cloud Pub/Sub API is currently disabled. You will use a service account to authenticate your application to the API. You want to make sure your application can use Cloud Pub/Sub. What should you do?
>
> **A.** Enable the Cloud Pub/Sub API in the API Library on the GCP Console.
>
> **B.** Rely on the automatic enablement of the Cloud Pub/Sub API when the Service Account accesses it.
>
> **C.** Use Deployment Manager to deploy your application. Rely on the automatic enablement of all APIs used by the application being deployed.
>
> **D.** Grant the App Engine Default service account the role of Cloud Pub/Sub Admin. Have your application enable the API on the first connection to Cloud Pub/ Sub.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your App Engine app must send and receive Pub/Sub messages (Pub/Sub is Google's messaging service). The Pub/Sub API (the project's on-switch for that service) is turned off. The app signs in with a service account.
- **What you must achieve:** Make Pub/Sub work for the app.
- **The limits:** None stated.
- **What they're really asking:** What must you set up so the app can use Pub/Sub?

| Keyword | What it hints at |
|---|---|
| "**API is currently disabled**" | Nothing works until **someone turns it on**. Google Cloud **never turns APIs on by itself** |
| "**service account to authenticate**" | Identity is handled. The missing piece is the **switched-off API** |
| "**make sure your application can use**" | The reliable, simple step: **Enable it in the API Library** (or `gcloud services enable`) |

**Exam topic:** Project setup / APIs & Services.

---

## 📚 Key Terms Explained

### 1️⃣ API (Google Cloud service API)
- **What it is:** The **door your code uses to talk to a Google Cloud service**. Each service (Pub/Sub, Cloud SQL, Compute Engine…) has its own API, identified by a name.
- **Looks like:** `pubsub.googleapis.com`, `compute.googleapis.com`, `sqladmin.googleapis.com`
- **Not to be confused with:** a permission. The API being **on** means the service is **available in the project**. **IAM** decides **who** may use it.
- **Analogy:** 🚪 A **department's service window** in the office building.
- **In the online store:** The order API calls `pubsub.googleapis.com` to publish "order placed" events.

### 2️⃣ Enabling an API (API Library) 🔑
- **What it is:** A **per-project on/off switch** for each Google service. Most APIs start **off** in a new project. Until one is **enabled**, every call fails with an error like `SERVICE_DISABLED` / "API has not been used in project … or it is disabled".
- **Looks like:**
  - Console: **APIs & Services → Library → "Cloud Pub/Sub API" → Enable**
  - CLI: `gcloud services enable pubsub.googleapis.com --project=shopnow-prod`
- **Not to be confused with:** giving a role. Enabling the API **doesn't** give anyone access, and giving a role **doesn't** turn the API on. You often need **both**.
- **Analogy:** 💡 **Opening the department's service window.** Your staff badge is useless if the window is closed.
- **In the online store:** Before the first Pub/Sub event, the team enables the Pub/Sub API once in `shopnow-prod`.

### 3️⃣ Cloud Pub/Sub (review from Q023)
- **What it is:** A **messaging service**: one part of your app **publishes** messages to a **topic**, and other parts **subscribe** and receive them.
- **Looks like:** topic `order-placed` → subscriptions `send-email`, `update-inventory`
- **Not to be confused with:** a database. Messages are **delivered and then removed**, not stored long-term.
- **Analogy:** 📬 The office **internal mail room**: drop a memo in the "Orders" tray, and every department subscribed to it gets a copy.

### 4️⃣ App Engine Default Service Account
- **What it is:** The **service account App Engine apps run as** automatically, unless you choose another.
- **Looks like:** `shopnow-prod@appspot.gserviceaccount.com`
- **Not to be confused with:** a person's account. It's the app's **machine identity**, the same idea as Q019/Q026.
- **Analogy:** 🪪 The **ID badge** issued to the building's mail robot.

### 5️⃣ Roles: Pub/Sub Admin vs Publisher / Subscriber
- **What it is:** `roles/pubsub.admin` = **full control** of Pub/Sub (create/delete topics, change permissions). `roles/pubsub.publisher` / `roles/pubsub.subscriber` = **only send** / **only receive** messages.
- **Not to be confused with:** enabling the API. **No Pub/Sub role can turn on an API.** That needs `serviceusage.services.enable` (for example `roles/serviceusage.serviceUsageAdmin`), which a project admin normally does once.
- **Analogy:** 🗝️ Mail-room manager (admin) vs "can drop memos in" (publisher) vs "can pick up memos" (subscriber).

### 🔗 How They Fit Together
```
① Project switch:  APIs & Services → Enable "Cloud Pub/Sub API"   (pubsub.googleapis.com)  ← the question
        │
② Identity:        App Engine app runs as  shopnow-prod@appspot.gserviceaccount.com
        │
③ Permission:      IAM role on topic/subscription → pubsub.publisher / pubsub.subscriber
        ▼
🛒 App publishes "order-placed" → 📬 Pub/Sub → 📧 email worker, 📦 inventory worker

Miss ① → every call fails "SERVICE_DISABLED", no matter which role you grant.
```

---

## 🌍 Real-World Scenario

A developer adds Pub/Sub to the app, deploys, and the logs fill with: *"Cloud Pub/Sub API has not been used in project shopnow-prod before or it is disabled. Enable it by visiting…"*. This is one of the most common first-day errors in Google Cloud. The fix is always the same: an admin **enables the API** in that project (Console or `gcloud services enable`), usually as part of the project setup script.

---

## 🔍 Option-by-Option Breakdown

### ✅ A (your answer)
> **A.** Enable the Cloud Pub/Sub API in the API Library on the GCP Console.

**Why it's correct:**
- ✔️ APIs must be **turned on explicitly** in each project, and this is exactly where you do it.
- ✔️ One simple step, done once.
- ✔️ After that, the service account just needs a Pub/Sub role (publisher/subscriber) to send and receive.

**📌 When to use it:** Use it whenever a project is about to use a Google service for the first time.
🏢 **Office example:** Asking facilities to open the mail-room window before staff start sending memos.

### ❌ B
> **B.** Rely on the automatic enablement of the Cloud Pub/Sub API when the Service Account accesses it.

**Why it's wrong:**
- ❌ **There is no automatic enablement.** If the API is off, the call simply **fails** with `SERVICE_DISABLED`.

**📌 When to use it:** **Never use this.** APIs don't turn on by themselves. Enable the API first (A).
🏢 **Office example:** Standing at a closed service window expecting it to open just because you showed your badge.

### ❌ C
> **C.** Use Deployment Manager to deploy your application. Rely on the automatic enablement of all APIs used by the application being deployed.

**Why it's wrong:**
- ❌ Deployment Manager **doesn't scan your app and turn on APIs** for it. (It can enable an API only if you **explicitly write that resource** in the config.)
- ❌ Moving the whole deployment to Deployment Manager is a lot of extra work for a one-click task.

**📌 When to use it:** Use Deployment Manager when you want to build your infrastructure again and again from a written plan.
🏢 **Office example:** Using a floor plan to build identical branch offices. It won't open a service window you didn't draw on the plan.

### ❌ D
> **D.** Grant the App Engine Default service account the role of Cloud Pub/Sub Admin. Have your application enable the API on the first connection to Cloud Pub/ Sub.

**Why it's wrong:**
- ❌ **Pub/Sub Admin can't enable APIs.** It manages topics and subscriptions, but turning on an API needs a **Service Usage** permission.
- ❌ **Too much power**: the app only needs to send and receive, not full admin (breaks least privilege).
- ❌ Making your **app code** switch on project settings is fragile and unusual.

**📌 When to use it:** Give Pub/Sub Admin only to the people who manage all topics and subscriptions, not to an app.
🏢 **Office example:** Giving the mail-room manager key to the person who manages the whole mail room, not to every clerk who sends a memo.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's order API on App Engine should publish an `order-placed` event so the email and inventory workers react.

```bash
# ① Turn on the API once for the project (same as option A, from the CLI)
gcloud services enable pubsub.googleapis.com --project=shopnow-prod

# ② Create the topic and subscriptions
gcloud pubsub topics create order-placed
gcloud pubsub subscriptions create send-email --topic=order-placed

# ③ Least privilege for the app's service account
gcloud pubsub topics add-iam-policy-binding order-placed \
  --member="serviceAccount:shopnow-prod@appspot.gserviceaccount.com" \
  --role="roles/pubsub.publisher"
```

| Situation | What happens when a customer checks out |
|---|---|
| API **disabled** (B/C/D thinking) | `403 SERVICE_DISABLED`, no confirmation email, stock not updated ❌ |
| API **enabled** + publisher role | Event published → email sent, stock updated ✅ |

---

## 🧠 Key Takeaways / Memory Tips

- **"API is disabled" → Enable it** (API Library in the Console, or `gcloud services enable`).
  🧠 *"**No API turns itself on.** Any option that says 'rely on automatic enablement' is a trap."*
- **Enabling an API ≠ granting a role.** You need **both**: API on (project switch) + IAM role (who can use it).
- **Pub/Sub Admin can't enable APIs**, and apps should get **publisher/subscriber**, not admin.
- Related: **Q023** (Pub/Sub in a data pipeline), **Q019/Q026** (service accounts for apps and VMs).

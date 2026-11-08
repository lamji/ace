# Q064: Processing Pub/Sub Messages With Cloud Run (Push Subscription + Invoker Service Account)

**Topic:** Cloud Run + Pub/Sub (push vs pull subscriptions, Cloud Run Invoker role, service accounts, request-driven scaling)

## ❓ Question
> You want to deploy an application on Cloud Run that processes messages from a Cloud Pub/Sub topic. You want to follow Google-recommended practices. What should you do?
>
> **A.** 1. Create a Cloud Function that uses a Cloud Pub/Sub trigger on that topic. 2. Call your application on Cloud Run from the Cloud Function for every message.
>
> **B.** 1. Grant the Pub/Sub Subscriber role to the service account used by Cloud Run. 2. Create a Cloud Pub/Sub subscription for that topic. 3. Make your application pull messages from that subscription.
>
> **C.** 1. Create a service account. 2. Give the Cloud Run Invoker role to that service account for your Cloud Run application. 3. Create a Cloud Pub/Sub subscription that uses that service account and uses your Cloud Run application as the push endpoint.
>
> **D.** 1. Deploy your application on Cloud Run on GKE with the connectivity set to Internal. 2. Create a Cloud Pub/Sub subscription for that topic. 3. In the same Google Kubernetes Engine cluster as your application, deploy a container that takes the messages and sends them to your application.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will run an app on Cloud Run (Google's serverless container service) that processes messages from a Pub/Sub topic (a message channel).
- **What you must achieve:** Connect the topic to the app.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** How should Pub/Sub deliver messages to the Cloud Run app?

| Question words | What they point to |
|---|---|
| "**Cloud Run**" | Cloud Run apps wake up **when they receive a request** and can scale to zero → messages should be **pushed** to it as requests |
| "**processes messages from a Cloud Pub/Sub topic**" | You need a **subscription** on the topic |
| "**Google-recommended practices**" | Built-in **push subscription** + a **service account with only the Invoker role** (secure, no extra services) |

**Exam topic:** Cloud Run + Pub/Sub.

**The B vs C difference:** Both use a Cloud Run application and a Pub/Sub subscription. In **B, Cloud Run must ask Pub/Sub for messages**. In **C, Pub/Sub sends each message to Cloud Run as an HTTPS request**. A standard Cloud Run service is designed to handle incoming requests, so C directly starts the app when a message arrives.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Run
- **What it is:** A service that runs your **container** and gives it an HTTPS URL. It starts copies **when requests arrive** and can shut down to **zero** when there are none, so you pay only while handling requests.
- **Looks like:** `https://order-worker-abc123-uc.a.run.app`
- **Not to be confused with:** a VM that's always on. Cloud Run is **request-driven**: no request, no work.
- **Analogy:** 🛎️ A **staff member who only comes to the desk when the bell rings**.
- **In the online store:** `order-worker` sends confirmation emails.

### 2️⃣ Pub/Sub topic and subscription
- **What it is:** A **topic** is a mailbox that apps publish messages to. A **subscription** is a **delivery rule** that sends the topic's messages to one receiver.
- **Looks like:** topic `order-created` → subscription `order-worker-sub`
- **Not to be confused with:** the message itself. The subscription is the **delivery route**.
- **Analogy:** 📬 The topic is the **company mailroom**; the subscription is "**send copies of these letters to Accounting**".
- **In the online store:** Checkout publishes `order-created`, and the worker gets each order.

### 3️⃣ Push vs Pull subscription 🔑
- **What it is:**
  - **Push:** Pub/Sub **sends** each message as an HTTPS request to your URL.
  - **Pull:** your app must **keep asking** Pub/Sub "any new messages?".
- **Looks like:**
  ```bash
  # push
  gcloud pubsub subscriptions create order-worker-sub --topic=order-created \
    --push-endpoint=https://order-worker-abc123-uc.a.run.app/ \
    --push-auth-service-account=pubsub-invoker@shopnow.iam.gserviceaccount.com
  ```
- **Not to be confused with:** each other. Push = **mail delivered to your desk**. Pull = **you keep walking to the mailroom**.
- **Analogy:** 📨 Push = the mail carrier **rings your bell**. Pull = you **check the mailbox** over and over.
- **In the online store:** Each new order rings Cloud Run's bell, and Cloud Run wakes up to handle it.

### 4️⃣ Cloud Run Invoker role (`roles/run.invoker`)
- **What it is:** An IAM role that allows **calling (sending requests to)** a Cloud Run service. Without it, a private Cloud Run service rejects the request.
- **Looks like:** `gcloud run services add-iam-policy-binding order-worker --member=serviceAccount:pubsub-invoker@... --role=roles/run.invoker`
- **Not to be confused with:** Cloud Run Admin (can deploy and change services). Invoker can **only call** it.
- **Analogy:** 🎫 A **visitor pass** that lets you ring the bell, but not enter the back office.
- **In the online store:** Pub/Sub's delivery identity can call the private `order-worker` service, but cannot change its code or settings.

### 5️⃣ Service account (review from Q036)
- **What it is:** A **non-human Google account** used by apps and services. Here, Pub/Sub uses it to **prove who it is** when it pushes to Cloud Run.
- **Looks like:** `pubsub-invoker@shopnow.iam.gserviceaccount.com`
- **Not to be confused with:** a person's account. Nobody logs in with it.
- **Analogy:** 🪪 The **mail carrier's company ID badge**.
- **In the online store:** The `pubsub-invoker` badge identifies the sender of new-order requests to `order-worker`.

### 6️⃣ Pub/Sub Subscriber role (`roles/pubsub.subscriber`) and push endpoint
- **What they are:** The Subscriber role lets an identity read messages from a subscription. A **push endpoint** is the HTTPS address where Pub/Sub delivers messages for a push subscription.
- **Analogy:** Subscriber is permission to collect letters from the mailroom; the endpoint is the address where the mail carrier delivers them.
- **In the online store:** B gives the `order-worker` identity permission to collect new orders; C gives Pub/Sub the `order-worker` web address so it can deliver each order.

### 🔗 How they fit together (C)
```
 Checkout ──publish──► 📬 topic: order-created
                              │ push subscription (uses SA pubsub-invoker)
                              ▼  HTTPS POST + ID token of pubsub-invoker
                       🛎️ Cloud Run: order-worker  (checks: has run.invoker? ✅)
                              │ returns 200 = "done" → Pub/Sub deletes the message
```

---

## 🌍 Real-World Scenario

Event-driven apps are very common: an order is placed → send an email, update inventory, notify the warehouse. Teams put each step on **Cloud Run** and connect it with **Pub/Sub push**. Cloud Run sleeps (costs nothing) when there are no messages and scales up automatically when a burst arrives. A dedicated service account with **only** the Invoker role keeps the Cloud Run service private, so only Pub/Sub can call it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Create a Cloud Function that uses a Cloud Pub/Sub trigger on that topic. 2. Call your application on Cloud Run from the Cloud Function for every message.

**Wrong words:**
- ❌ "**Create a Cloud Function**": an extra service in the middle that you must deploy, pay for and maintain.
- ❌ "**Call your application on Cloud Run from the Cloud Function for every message**": a hand-made relay. Pub/Sub can deliver to Cloud Run **directly** with a push subscription.

📌 **When to use it:** Use a Cloud Function with a Pub/Sub trigger when the processing is small enough to live in the function itself.
🏢 **Office example:** Hiring a second receptionist only to walk each letter from the mailroom to Accounting, when the mail carrier could deliver it directly.

### ❌ B
> **B.** 1. Grant the Pub/Sub Subscriber role to the service account used by Cloud Run. 2. Create a Cloud Pub/Sub subscription for that topic. 3. Make your application pull messages from that subscription.

**Wrong words:**
- ✔️ "Grant the Pub/Sub Subscriber role … Create a Cloud Pub/Sub subscription" is fine for a pull app.
- ❌ "**Make your application pull messages**": With a standard Cloud Run service's default request-based billing, CPU is allocated during requests, and the service may scale to zero. If no request arrives, there may be no running app to fetch the messages. B also makes the app manage the pull loop and acknowledgments. It does not give the question's Cloud Run service a direct message-triggered request.
- **Important nuance:** Pull is possible with a deliberately configured always-running worker, such as a Cloud Run worker pool, or a Cloud Run service with instance-based billing and minimum instances. That is a different setup from the simple service described here; B omits those settings.

📌 **When to use it:** Use it when a clerk stays on duty to collect letters and control how many to handle at once.
🏢 **Office example:** A full-time accounting clerk checks the mailroom throughout the day.

### ✅ C (your answer)
> **C.** 1. Create a service account. 2. Give the Cloud Run Invoker role to that service account for your Cloud Run application. 3. Create a Cloud Pub/Sub subscription that uses that service account and uses your Cloud Run application as the push endpoint.

**Why it's correct:**

- ✔️ "**uses your Cloud Run application as the push endpoint**" matches "**application on Cloud Run that processes messages**": Pub/Sub **sends each message as a request**, which is exactly how Cloud Run wakes up and scales.
- ✔️ "**Create a Cloud Pub/Sub subscription**" matches "**from a Cloud Pub/Sub topic**": The built-in delivery route from the topic. No extra services.
- ✔️ "**Create a service account**" + "**Cloud Run Invoker role**" + "**subscription that uses that service account**" matches "**Google-recommended practices**": Cloud Run stays **private**; only Pub/Sub (with its badge) may call it, and the badge can **only invoke**: least privilege.

📌 **When to use it:** Use it when a service that only works on incoming requests must handle each new message automatically.
🏢 **Office example:** The mail carrier, with a company ID badge, rings the bell of the on-call staff member for each new letter.

### ❌ D
> **D.** 1. Deploy your application on Cloud Run on GKE with the connectivity set to Internal. 2. Create a Cloud Pub/Sub subscription for that topic. 3. In the same Google Kubernetes Engine cluster as your application, deploy a container that takes the messages and sends them to your application.

**Wrong words:**
- ❌ "**Deploy your application on Cloud Run on GKE**": the question says **Cloud Run**, the fully managed service. Running a GKE cluster adds cost and work.
- ❌ "**deploy a container that takes the messages and sends them to your application**": another hand-built relay you must maintain, while push subscriptions do this for free.

📌 **When to use it:** Use Cloud Run on GKE (now Knative serving) only when you already run GKE and need your services inside that cluster.
🏢 **Office example:** Building your own mailroom and hiring a sorter, when the post office already delivers to your door.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's checkout publishes to `order-created`. The `order-worker` on Cloud Run sends the confirmation email.

```bash
# 1. The "badge" Pub/Sub will use
gcloud iam service-accounts create pubsub-invoker

# 2. Let only that badge call the worker
gcloud run services add-iam-policy-binding order-worker --region=us-central1 \
  --member=serviceAccount:pubsub-invoker@shopnow.iam.gserviceaccount.com \
  --role=roles/run.invoker

# 3. Push each message to the worker, signed with the badge
gcloud pubsub subscriptions create order-worker-sub --topic=order-created \
  --push-endpoint=https://order-worker-abc123-uc.a.run.app/ \
  --push-auth-service-account=pubsub-invoker@shopnow.iam.gserviceaccount.com
```

| Time | Orders | Cloud Run instances |
|---|---|---|
| 3 AM | 0 | 0 (no cost) |
| Black Friday noon | 2,000/min | scales up automatically |

---

## 🧠 Key Takeaways / Memory Tips

- **Pub/Sub → Cloud Run = push subscription + service account with `run.invoker`.**
- **Pull** fits always-running apps (VMs, GKE). **Push** fits request-driven apps (Cloud Run, App Engine).
- An extra relay is unnecessary here because Pub/Sub can push directly to Cloud Run.
  🧠 *"**Cloud Run waits for the doorbell. Pub/Sub push rings it, with an Invoker badge.**"*
- Related: **Q036** (service account roles), **Q060** (no hand-built relays/proxies).

**Current Google Cloud guidance:** [Pub/Sub triggers for Cloud Run](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers) shows an authenticated push subscription with a service account authorized to invoke the service. [Cloud Run billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings) explains when background pull workers need other Cloud Run configurations.

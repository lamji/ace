# Q305: Public App Processing Google Service Events, No Cost When Idle (Cloud Run + Eventarc)

**Topic:** Serverless (Cloud Run, Eventarc)

## ❓ Question
> You are planning to deploy an application to Google Cloud. Your application processes asynchronous events from Google services and must be accessible from the public Internet. You need to identify how to deploy your application. You want to follow a standardized process while minimizing development costs. You also want to have no costs when your workloads are not in use. What should you do?
>
> **A.** Deploy your code to GKE. Use Pub/Sub for event delivery.
>
> **B.** Deploy your code to Compute Engine. Use Pub/Sub for event delivery.
>
> **C.** Deploy your code to GKE. Use Eventarc for event delivery.
>
> **D.** Deploy your code to Cloud Run. Use Eventarc for event delivery.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app processes events from Google services (like a file being uploaded) and must be reachable from the public internet.
- **What you must achieve:** Choose how to deploy it.
- **The limits:** Use a standardized process, keep development cost low, and pay nothing when it isn't being used.
- **What they're really asking:** Where should the app run and how should events be delivered to it?

**Clues in the question:**
- "**no costs when your workloads are not in use**" → **Cloud Run** (scales to zero).
- "**asynchronous events from Google services**" + "**standardized process**" → **Eventarc** (CloudEvents format).

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Eventarc 🔑
- **What it is:** Routes events from Google services (Cloud Storage, Audit Logs, Pub/Sub…) to targets like Cloud Run, in the standard CloudEvents format.
- **Looks like:** `gcloud eventarc triggers create img --destination-run-service=resizer --event-filters=type=google.cloud.storage.object.v1.finalized`
- **Not to be confused with:** Pub/Sub alone (you wire each source).
- **Analogy:** 📮 A building's central mail sorter.
- **In the online store:** New image uploaded → resize.

### 🔗 How they fit together
```
 Google service event → Eventarc → Cloud Run (scale to zero) ✅
```

---

## 🌍 Real-World Scenario

An app reacts to uploads and audit events. **Eventarc** delivers them to a public **Cloud Run** service that costs nothing when idle.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy your code to GKE. Use Pub/Sub for event delivery.

**Wrong words:**
- ❌ "**GKE**": nodes cost money even when idle.

📌 **When to use it:** Use GKE for steady container platforms.
🏢 **Office example:** A rented office paid for nights too.

### ❌ B
> **B.** Deploy your code to Compute Engine. Use Pub/Sub for event delivery.

**Wrong words:**
- ❌ "**Compute Engine**": VMs bill while running, idle or not.

📌 **When to use it:** Use VMs for full OS control.
🏢 **Office example:** A staffed desk 24/7.

### ❌ C
> **C.** Deploy your code to GKE. Use Eventarc for event delivery.

**Wrong words:**
- ✔️ Eventarc is right.
- ❌ "**GKE**": no scale-to-zero cost.

📌 **When to use it:** Use it when you already run a GKE platform.
🏢 **Office example:** A good mail sorter delivering to an always-paid office.

### ✅ D
> **D.** Deploy your code to Cloud Run. Use Eventarc for event delivery.

**Why it's correct:**
- ✔️ "**Cloud Run**" matches "**no costs when your workloads are not in use**" + "**accessible from the public Internet**".
- ✔️ "**Eventarc for event delivery**" matches "**asynchronous events from Google services**" + "**standardized process**".

📌 **When to use it:** Use it when a program should react to things happening in other services and cost nothing while waiting.
🏢 **Office example:** A central mail sorter that calls in staff only when mail arrives.

---

## 🛒 E-Commerce Full-Stack Example

Eventarc: `storage.object.finalized` on `gs://shopnow-uploads` → Cloud Run `thumbnailer`.

---

## 🧠 Key Takeaways / Memory Tips

- **Google service events + scale to zero → Eventarc + Cloud Run.**
  🧠 *"**Eventarc delivers, Cloud Run sleeps till needed.**"*
- Related: **Q298**, **Q370**.

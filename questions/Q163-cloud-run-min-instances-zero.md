# Q163: Internal Web App Used Only During Business Hours, No Cost Otherwise (Cloud Run, Min Instances 0)

**Topic:** Serverless (Cloud Run scale to zero, App Engine flexible, Cloud Run for Anthos)

## ❓ Question
> You have developed a containerized web application that will serve internal colleagues during business hours. You want to ensure that no costs are incurred outside of the hours the application is used. You have just created a new Google Cloud project and want to deploy the application. What should you do?
>
> **A.** Deploy the container on Cloud Run for Anthos, and set the minimum number of instances to zero.
>
> **B.** Deploy the container on Cloud Run (fully managed), and set the minimum number of instances to zero.
>
> **C.** Deploy the container on App Engine flexible environment with autoscaling, and set the value min_instances to zero in the app.yaml.
>
> **D.** Deploy the container on App Engine flexible environment with manual scaling, and set the value instances to zero in the app.yaml.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You built a containerized web app (an app packed as a container) for coworkers to use during business hours, and you have a brand-new project.
- **What you must achieve:** Deploy the app.
- **The limits:** No costs at all outside the hours it is used.
- **What they're really asking:** Where should you run it so it costs nothing when nobody is using it?

**Clues in the question:**
- "**containerized**" + "**no costs … outside of the hours**" → **Cloud Run (fully managed)** scales to **zero** and bills per request.
- "**just created a new Google Cloud project**": no GKE cluster exists, which rules out Cloud Run for Anthos.
- App Engine **flexible** keeps at least one instance running.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run (fully managed) 🔑 (review from Q065)
- **What it is:** Runs containers serverlessly. With **min instances 0**, it **scales to zero** and costs nothing when idle.
- **Looks like:** `gcloud run deploy intranet --image=… --min-instances=0`
- **Not to be confused with:** Cloud Run for Anthos (runs on your GKE cluster).
- **Analogy:** 💡 Lights on a motion sensor.
- **In the online store:** Internal admin tool.

### 2. App Engine flexible
- **What it is:** Runs apps on VMs. It needs **at least 1 instance**, so it can't scale to zero.
- **Looks like:** `env: flex`
- **Not to be confused with:** App Engine standard (can scale to zero).
- **Analogy:** 🏢 A small office that's always rented.
- **In the online store:** Legacy apps with custom runtimes.

### 🔗 How they fit together
```
 9:00 colleagues use app → Cloud Run starts instances
 18:00 no traffic → 0 instances → $0 ✅
```

---

## 🌍 Real-World Scenario

An HR team's internal container app is used 9–5. It's deployed on **Cloud Run** with min instances 0. At night and on weekends it scales to zero and costs nothing.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the container on Cloud Run for Anthos, and set the minimum number of instances to zero.

**Wrong words:**
- ❌ "**Cloud Run for Anthos**": it runs on a **GKE cluster** you pay for 24/7. The new project has no cluster anyway.

📌 **When to use it:** Use it when you already run GKE/Anthos and want Cloud Run on it.
🏢 **Office example:** Motion-sensor lights in a building you rent all year.

### ✅ B
> **B.** Deploy the container on Cloud Run (fully managed), and set the minimum number of instances to zero.

**Why it's correct:**
- ✔️ "**Cloud Run (fully managed)**" matches "**containerized web application**" + "**new Google Cloud project**": nothing else to set up.
- ✔️ "**minimum number of instances to zero**" matches "**no costs are incurred outside of the hours**": it scales to zero.

📌 **When to use it:** Use it when an app is only used part of the day and should cost nothing otherwise.
🏢 **Office example:** Lights on a motion sensor that switch off when everyone goes home.

### ❌ C
> **C.** Deploy the container on App Engine flexible environment with autoscaling, and set the value min_instances to zero in the app.yaml.

**Wrong words:**
- ❌ "**App Engine flexible … min_instances to zero**": flexible needs at least one instance, so it never reaches zero cost.

📌 **When to use it:** Use flexible for apps needing custom runtimes on VMs.
🏢 **Office example:** An office that's always rented, even at night.

### ❌ D
> **D.** Deploy the container on App Engine flexible environment with manual scaling, and set the value instances to zero in the app.yaml.

**Wrong words:**
- ❌ "**manual scaling … instances to zero**": not valid for flexible, and manual scaling doesn't follow usage.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Paying for a fixed number of desks no matter what.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud run deploy shop-admin --image=us-docker.pkg.dev/shopnow/apps/admin:1.3 --region=us-central1 \
  --min-instances=0 --no-allow-unauthenticated
```

---

## 🧠 Key Takeaways / Memory Tips

- **Container + zero cost when idle → Cloud Run (fully managed), min instances 0.**
- App Engine flexible can't scale to zero.
  🧠 *"**Nobody using it? Cloud Run sleeps.**"*
- Related: **Q065** (low-traffic container), **Q064**.

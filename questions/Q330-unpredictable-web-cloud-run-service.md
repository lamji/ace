# Q330: Containerized Web App With Unpredictable Traffic, Lowest Cost (Cloud Run Service)

**Topic:** Serverless (Cloud Run)

## ❓ Question
> You have developed a web application that serves traffic for a local event and are expecting unpredictable traffic. You have containerized the application, and you now want to deploy the application on Google Cloud. You also want to minimize costs. What should you do?
>
> **A.** Deploy the web application as a Cloud Run job.
>
> **B.** Deploy the web application on Google Kubernetes Engine in Standard mode.
>
> **C.** Deploy the web application as a Cloud Run service.
>
> **D.** Deploy the web application on Google Kubernetes Engine in Autopilot mode.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You built a containerized web app for a local event, and traffic will be unpredictable.
- **What you must achieve:** Deploy it on Google Cloud.
- **The limits:** Keep costs as low as possible.
- **What they're really asking:** Where should you run the containerized web app?

**Clues in the question:**
- Web app → Cloud Run **service** (not job).
- Unpredictable + cheap → scale to zero.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Cloud Run service vs job 🔑
- **What it is:** Service: handles HTTP requests, autoscaling. Job: runs to completion, no requests.
- **Looks like:** `gcloud run deploy event-site --image=...`
- **Not to be confused with:** job.
- **Analogy:** 🧑‍💼 Receptionist vs task worker.
- **In the online store:** —

### 🔗 How they fit together
```
 web traffic → Cloud Run service (0 → N) ✅
```

---

## 🌍 Real-World Scenario

A local-event site runs as a **Cloud Run service**, scaling with spikes and to zero afterwards.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the web application as a Cloud Run job.

**Wrong words:**
- ❌ "**Cloud Run job**": doesn't serve web traffic.

📌 **When to use it:** Use jobs for batch tasks.
🏢 **Office example:** A night-shift worker for the front desk.

### ❌ B
> **B.** Deploy the web application on Google Kubernetes Engine in Standard mode.

**Wrong words:**
- ❌ "**GKE … Standard**": nodes cost even when idle; you manage them.

📌 **When to use it:** Use Standard for node control.
🏢 **Office example:** Leased office paid all month.

### ✅ C
> **C.** Deploy the web application as a Cloud Run service.

**Why it's correct:**
- ✔️ "**Cloud Run service**" matches "**web application**" + "**unpredictable traffic**" + "**minimize costs**".

📌 **When to use it:** Use it when a website's visitors come in bursts and you only want to pay when they come.
🏢 **Office example:** A front desk that adds staff when the crowd arrives and closes when it leaves.

### ❌ D
> **D.** Deploy the web application on Google Kubernetes Engine in Autopilot mode.

**Wrong words:**
- ✔️ Autopilot is less work than Standard.
- ❌ Still costlier than Cloud Run for spiky, short-lived traffic (no scale to zero for the cluster).

📌 **When to use it:** Use Autopilot for many services needing Kubernetes.
🏢 **Office example:** A serviced office for a weekend pop-up.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy blackfriday-landing --image=... --max-instances=200`

---

## 🧠 Key Takeaways / Memory Tips

- **Containerized web + spiky + cheap → Cloud Run service.**
  🧠 *"**Web = service; batch = job.**"*
- Related: **Q315**, **Q373**.

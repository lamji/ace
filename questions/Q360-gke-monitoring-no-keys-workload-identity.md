# Q360: GKE App Needs Service Account Credentials, New Keys Prohibited (Workload Identity Federation)

**Topic:** GKE security (Workload Identity Federation)

## ❓ Question
> You are developing a monitoring application that runs on a Google Kubernetes Engine (GKE) cluster. The application requires credentials from a service account to collect performance data. However, your organization has a policy that prohibits the creation of new service account keys. You need to grant the application access while following Google-recommended security practices. What should you do?
>
> **A.** Use your personal user credentials to authenticate the application, ensuring your account has the necessary permissions.
>
> **B.** Create a new project, generate a service account key in the new project, and grant the service account the required IAM roles in the application project.
>
> **C.** Override the organization policy in the project, and create a long-lived service account key in the GKE cluster.
>
> **D.** Configure Workload Identity Federation to allow the application to impersonate a service account.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** GKE app needs SA access; **no new keys**.

**Clues in the question:**
- "**prohibits the creation of new service account keys**" → **Workload Identity Federation for GKE**.

**Exam topic:** GKE / IAM.

---

## 📚 Key Terms Explained

### 1. Workload Identity Federation 🔑 (review from Q301)
- **What it is:** Pods impersonate an IAM SA with short-lived tokens, no keys.
- **Looks like:** —
- **Not to be confused with:** keys.
- **Analogy:** 🪪 Linked badges.
- **In the online store:** —

### 🔗 How they fit together
```
 Pod (KSA) ─WIF─► GSA (monitoring.viewer) ✅
```

---

## 🌍 Real-World Scenario

A monitoring app on GKE uses **Workload Identity Federation** to act as `monitor-sa`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use your personal user credentials to authenticate the application, ensuring your account has the necessary permissions.

**Wrong words:**
- ❌ "**personal user credentials**": the app acts as you; insecure.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Lending your badge to a robot.

### ❌ B
> **B.** Create a new project, generate a service account key in the new project, and grant the service account the required IAM roles in the application project.

**Wrong words:**
- ❌ "**generate a service account key in the new project**": evades the policy; still a key.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Getting a master key cut in another building.

### ❌ C
> **C.** Override the organization policy in the project, and create a long-lived service account key in the GKE cluster.

**Wrong words:**
- ❌ "**Override the organization policy … long-lived … key**": breaks policy and best practice.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Disabling the rule to make a master key.

### ✅ D
> **D.** Configure Workload Identity Federation to allow the application to impersonate a service account.

**Why it's correct:**
- ✔️ "**Workload Identity Federation**" matches "**prohibits the creation of new service account keys**".
- ✔️ "**impersonate a service account**" matches "**requires credentials from a service account**" + "**Google-recommended security practices**".

📌 **When to use it:** Use it when programs in your container cluster need cloud access and keys are banned.
🏢 **Office example:** Each team's building badge is linked to a company badge; no keys copied.

---

## 🛒 E-Commerce Full-Stack Example

`metrics-collector` KSA ↔ `monitor-sa` with `roles/monitoring.viewer`.

---

## 🧠 Key Takeaways / Memory Tips

- **GKE + no keys → Workload Identity Federation.**
  🧠 *"**No keys in GKE: WIF.**"*
- Related: **Q301**.

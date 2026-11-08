# Q238: Business-Critical Kubernetes Optimized for Reliability (GKE Autopilot + Stable Release Channel)

**Topic:** GKE (Autopilot, release channels)

## ❓ Question
> You are working in a team that has developed a new application that needs to be deployed on Kubernetes. The production application is business critical and should be optimized for reliability. You need to provision a Kubernetes cluster and want to follow Google-recommended practices. What should you do?
>
> **A.** Create a GKE Autopilot cluster. Enroll the cluster in the rapid release channel.
>
> **B.** Create a GKE Autopilot cluster. Enroll the cluster in the stable release channel.
>
> **C.** Create a zonal GKE standard cluster. Enroll the cluster in the stable release channel.
>
> **D.** Create a regional GKE standard cluster. Enroll the cluster in the rapid release channel.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team built a new app that must run on Kubernetes. Production is business-critical.
- **What you must achieve:** Create the Kubernetes cluster.
- **The limits:** Optimize for reliability and follow Google-recommended practices.
- **What they're really asking:** What kind of GKE cluster should you create?

**Clues in the question:**
- "**Google-recommended practices**" → **Autopilot** (regional, Google manages nodes and best practices).
- "**optimized for reliability**" → **stable** release channel (most tested versions).

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. GKE Autopilot 🔑
- **What it is:** GKE mode where Google manages nodes, scaling and security settings. Always **regional**.
- **Looks like:** `gcloud container clusters create-auto prod --region=us-central1 --release-channel=stable`
- **Not to be confused with:** Standard mode.
- **Analogy:** 🏨 A serviced apartment.
- **In the online store:** ShopNow prod.

### 2. Release channels
- **What it is:** **Rapid** (newest, least tested), **Regular**, **Stable** (most tested, slower).
- **Looks like:** `--release-channel=stable`
- **Not to be confused with:** —
- **Analogy:** 🚦 Early adopters vs careful buyers.
- **In the online store:** —

### 🔗 How they fit together
```
 Autopilot (regional, managed) + stable channel ✅ = reliable prod
```

---

## 🌍 Real-World Scenario

A bank deploys its payments app to a **GKE Autopilot** cluster on the **stable** channel: Google manages nodes, and only well-tested versions roll out.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a GKE Autopilot cluster. Enroll the cluster in the rapid release channel.

**Wrong words:**
- ✔️ "Autopilot" is right.
- ❌ "**rapid release channel**": newest versions, least tested — not for reliability.

📌 **When to use it:** Use rapid for testing new features.
🏢 **Office example:** Buying the first batch of a brand-new car model.

### ✅ B
> **B.** Create a GKE Autopilot cluster. Enroll the cluster in the stable release channel.

**Why it's correct:**
- ✔️ "**GKE Autopilot cluster**" matches "**Google-recommended practices**": regional and managed by Google.
- ✔️ "**stable release channel**" matches "**business critical and should be optimized for reliability**".

📌 **When to use it:** Use it when an important system must run reliably with the least babysitting.
🏢 **Office example:** A serviced office that only installs equipment after it's been thoroughly tested.

### ❌ C
> **C.** Create a zonal GKE standard cluster. Enroll the cluster in the stable release channel.

**Wrong words:**
- ✔️ "stable" is right.
- ❌ "**zonal GKE standard cluster**": one zone means a zone outage takes down the control plane and nodes.

📌 **When to use it:** Use zonal clusters for dev/test.
🏢 **Office example:** One building with no backup.

### ❌ D
> **D.** Create a regional GKE standard cluster. Enroll the cluster in the rapid release channel.

**Wrong words:**
- ✔️ "regional" is good.
- ❌ "**rapid release channel**": least tested versions.

📌 **When to use it:** Use it for staging previews of new GKE features.
🏢 **Office example:** A sturdy building with untested machines.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container clusters create-auto shopnow-prod --region=us-central1 --release-channel=stable`

---

## 🧠 Key Takeaways / Memory Tips

- **Reliable production GKE → Autopilot + stable channel.** Rapid = newest, least tested.
  🧠 *"**Stable for production.**"*
- Related: **Q182**, **Q175**.

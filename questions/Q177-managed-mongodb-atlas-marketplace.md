# Q177: Managed MongoDB With a Support SLA (MongoDB Atlas From Marketplace)

**Topic:** Marketplace (partner managed services)

## ❓ Question
> You are creating an application that will run on Google Kubernetes Engine. You have identified MongoDB as the most suitable database system for your application and want to deploy a managed MongoDB environment that provides a support SLA. What should you do?
>
> **A.** Create a Cloud Bigtable cluster, and use the HBase API.
>
> **B.** Deploy MongoDB Atlas from the Google Cloud Marketplace.
>
> **C.** Download a MongoDB installation package, and run it on Compute Engine instances.
>
> **D.** Download a MongoDB installation package, and run it on a Managed Instance Group.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You want **MongoDB**, **managed**, with a **support SLA**.

**Clues in the question:**
- "**managed MongoDB environment**" + "**support SLA**" → **MongoDB Atlas** (MongoDB Inc.'s managed service) via **Marketplace**.

**Exam topic:** Marketplace.

---

## 📚 Key Terms Explained

### 1. MongoDB Atlas 🔑
- **What it is:** MongoDB's **fully managed** cloud service, run by MongoDB Inc. with an SLA, billed through Google Cloud.
- **Looks like:** Marketplace → MongoDB Atlas → Subscribe
- **Not to be confused with:** self-installed MongoDB.
- **Analogy:** 🧹 Hiring the official cleaning company with a contract.
- **In the online store:** Product reviews DB.

### 2. Google Cloud Marketplace (review from Q137)
- **What it is:** A catalog of partner software and services.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🛒 Approved vendor catalog.
- **In the online store:** —

### 🔗 How they fit together
```
 GKE app ─► MongoDB Atlas (managed, SLA) ✅
```

---

## 🌍 Real-World Scenario

A team chooses MongoDB for a catalog app and subscribes to **MongoDB Atlas** through Marketplace, getting a managed cluster with vendor support.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Bigtable cluster, and use the HBase API.

**Wrong words:**
- ❌ "**Cloud Bigtable … HBase API**": not MongoDB.

📌 **When to use it:** Use Bigtable for time-series or wide-column data.
🏢 **Office example:** Ordering a different product than the one you need.

### ✅ B
> **B.** Deploy MongoDB Atlas from the Google Cloud Marketplace.

**Why it's correct:**
- ✔️ "**MongoDB Atlas**" matches "**managed MongoDB environment**" + "**support SLA**".
- ✔️ "**Google Cloud Marketplace**" is how you get partner services billed through Google.

📌 **When to use it:** Use it when you want a product run by its maker, with a support contract.
🏢 **Office example:** Hiring the manufacturer's own service team under contract.

### ❌ C
> **C.** Download a MongoDB installation package, and run it on Compute Engine instances.

**Wrong words:**
- ❌ "**Download a MongoDB installation package … Compute Engine**": self-managed, no SLA.

📌 **When to use it:** Use it when you want full control and will run it yourself.
🏢 **Office example:** Fixing the copier yourself with no service contract.

### ❌ D
> **D.** Download a MongoDB installation package, and run it on a Managed Instance Group.

**Wrong words:**
- ❌ "**Managed Instance Group**": manages VMs, not MongoDB. Still self-managed.

📌 **When to use it:** Use a MIG for stateless app servers.
🏢 **Office example:** More DIY copiers.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow reviews service on GKE connects to a **MongoDB Atlas** cluster (GCP us-central1) via private endpoint.

---

## 🧠 Key Takeaways / Memory Tips

- **Managed third-party DB with SLA → Marketplace partner service (e.g. MongoDB Atlas).**
  🧠 *"**Want MongoDB managed? Atlas.**"*
- Related: **Q137**.

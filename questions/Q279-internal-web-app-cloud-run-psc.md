# Q279: Internal-Only Stateless Web App, Frequent Updates, Minimal Infrastructure (Cloud Run With Private Service Connect)

**Topic:** Cloud Run (private access via Private Service Connect)

## ❓ Question
> You need to deploy a single stateless web application with a web interface and multiple endpoints. For security reasons, the web application must be reachable from an internal IP address from your company's private VPC and on-premises network. You also need to update the web application multiple times per day with minimal effort and want to manage a minimal amount of cloud infrastructure. What should you do?
>
> **A.** Deploy the web application on Google Kubernetes Engine standard edition with an internal ingress.
>
> **B.** Deploy the web application on Cloud Run with Private Google Access configured.
>
> **C.** Deploy the web application on Cloud Run with Private Service Connect configured.
>
> **D.** Deploy the web application to GKE Autopilot with Private Google Access configured.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Reachable on an **internal IP** from VPC and on-prem; **minimal infrastructure**; frequent updates.

**Clues in the question:**
- "**minimal amount of cloud infrastructure**" + frequent updates → **Cloud Run**.
- "**reachable from an internal IP address from your … VPC and on-premises network**" → **Private Service Connect** endpoint (an internal IP in your VPC).
- Private Google Access is for VMs **calling out** to Google APIs, not for others **reaching** your app.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Private Service Connect 🔑
- **What it is:** Creates an **endpoint with an internal IP in your VPC** that privately reaches a Google service (like Cloud Run / Google APIs).
- **Looks like:** `gcloud compute addresses create psc-ip --global --purpose=PRIVATE_SERVICE_CONNECT --addresses=10.10.0.5`
- **Not to be confused with:** Private Google Access.
- **Analogy:** 🚪 A private door from your office straight into the service.
- **In the online store:** Internal admin tool.

### 2. Private Google Access (review from Q202)
- **What it is:** Lets internal-IP VMs call Google APIs. Doesn't give your app an internal address.
- **Looks like:** —
- **Not to be confused with:** PSC.
- **Analogy:** 🚶 Your staff walking out privately; nobody walks in.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem ─VPN─► VPC ─► PSC endpoint 10.10.0.5 ─► Cloud Run app (ingress: internal) ✅
```

---

## 🌍 Real-World Scenario

An HR portal on **Cloud Run** is exposed through a **Private Service Connect** endpoint with an internal IP; staff reach it from the office over VPN.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the web application on Google Kubernetes Engine standard edition with an internal ingress.

**Wrong words:**
- ❌ "**GKE standard edition**": a cluster and nodes to manage.

📌 **When to use it:** Use GKE when you need Kubernetes.
🏢 **Office example:** Owning a whole building for one office.

### ❌ B
> **B.** Deploy the web application on Cloud Run with Private Google Access configured.

**Wrong words:**
- ✔️ Cloud Run is right.
- ❌ "**Private Google Access**": lets VMs reach Google APIs; doesn't give your app an internal IP for others to reach.

📌 **When to use it:** Use PGA for internal VMs calling Google APIs.
🏢 **Office example:** A private exit, but no private entrance.

### ✅ C
> **C.** Deploy the web application on Cloud Run with Private Service Connect configured.

**Why it's correct:**
- ✔️ "**Cloud Run**" matches "**update … multiple times per day with minimal effort**" + "**minimal amount of cloud infrastructure**".
- ✔️ "**Private Service Connect configured**" matches "**reachable from an internal IP address from your company's private VPC and on-premises network**".

📌 **When to use it:** Use it when an internal tool must be private to your company network but you don't want to run servers.
🏢 **Office example:** A private door from the office corridor straight into a serviced office.

### ❌ D
> **D.** Deploy the web application to GKE Autopilot with Private Google Access configured.

**Wrong words:**
- ❌ "**GKE Autopilot**": still a cluster.
- ❌ "**Private Google Access**": wrong direction.

📌 **When to use it:** Use Autopilot for Kubernetes workloads.
🏢 **Office example:** A serviced building with only a private exit.

---

## 🛒 E-Commerce Full-Stack Example

Cloud Run `shop-admin` (ingress: internal) reached via PSC endpoint `10.20.0.5` in `shop-vpc`; on-prem routes over HA VPN.

---

## 🧠 Key Takeaways / Memory Tips

- **Private internal IP for a serverless app → Cloud Run + Private Service Connect.** PGA = VMs calling Google APIs.
  🧠 *"**PSC lets them in; PGA lets you out.**"*
- Related: **Q202**, **Q233**.

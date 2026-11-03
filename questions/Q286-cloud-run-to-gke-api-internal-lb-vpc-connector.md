# Q286: Cloud Run Must Privately Reach an API on GKE (Internal Application LB + Cloud DNS + Serverless VPC Access Connector)

**Topic:** Networking (serverless to VPC)

## ❓ Question
> You are deploying an application to Cloud Run. Your application requires the use of an API that runs on Google Kubernetes Engine (GKE). You need to ensure that your Cloud Run service can privately reach the API on GKE, and you want to follow Google-recommended practices. What should you do?
>
> **A.** Deploy an ingress resource on the GKE cluster to expose the API to the internet. Use Cloud Armor to filter for IP addresses that can connect to the API. On the Cloud Run service, configure the application to fetch its public IP address and update the Cloud Armor policy on startup to allow this IP address to call the API on ports 80 and 443.
>
> **B.** Create an ingress firewall rule on the VPC to allow connections from 0.0.0.0/0 on ports 80 and 443.
>
> **C.** Create an egress firewall rule on the VPC to allow connections to 0.0.0.0/ on ports 80 and 443.
>
> **D.** Deploy an internal Application Load Balancer to expose the API on GKE to the VPC. Configure Cloud DNS with the IP address of the internal Application Load Balancer. Deploy a Serverless VPC Access connector to allow the Cloud Run service to call the API through the FQDN on Cloud DNS.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Cloud Run → GKE API, **privately**.

**Clues in the question:**
- "**privately reach the API on GKE**" → expose GKE on an **internal** IP (internal Application LB).
- Cloud Run isn't in your VPC by default → **Serverless VPC Access connector** (or Direct VPC egress).
- A DNS name in **Cloud DNS** keeps it stable.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Serverless VPC Access connector 🔑
- **What it is:** Lets Cloud Run/Functions send traffic **into your VPC** to reach internal IPs.
- **Looks like:** `gcloud compute networks vpc-access connectors create run-conn --region=us-central1 --network=shop-vpc --range=10.8.0.0/28`
- **Not to be confused with:** Private Google Access.
- **Analogy:** 🚪 A side door from the serviced office into your private corridor.
- **In the online store:** Cloud Run → internal APIs.

### 2. Internal Application Load Balancer
- **What it is:** Layer-7 LB with an **internal** IP, reachable only inside the VPC (and connected networks).
- **Looks like:** GKE Ingress class `gce-internal`
- **Not to be confused with:** external LB.
- **Analogy:** 🛎️ An internal reception desk.
- **In the online store:** —

### 🔗 How they fit together
```
 Cloud Run ─ VPC connector ─► api.internal (Cloud DNS) → internal ALB → GKE API ✅
```

---

## 🌍 Real-World Scenario

A Cloud Run storefront calls an inventory API on GKE through an **internal Application LB**, a **Cloud DNS** name, and a **Serverless VPC Access connector**. Nothing is public.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy an ingress resource on the GKE cluster to expose the API to the internet. Use Cloud Armor to filter for IP addresses that can connect to the API. On the Cloud Run service, configure the application to fetch its public IP address and update the Cloud Armor policy on startup to allow this IP address to call the API on ports 80 and 443.

**Wrong words:**
- ❌ "**expose the API to the internet**": not private.
- ❌ "**fetch its public IP … update the Cloud Armor policy on startup**": Cloud Run has no fixed public IP; fragile and insecure.

📌 **When to use it:** Use Cloud Armor to protect public apps.
🏢 **Office example:** Opening the back office to the street and checking faces.

### ❌ B
> **B.** Create an ingress firewall rule on the VPC to allow connections from 0.0.0.0/0 on ports 80 and 443.

**Wrong words:**
- ❌ "**allow connections from 0.0.0.0/0**": opens the API to the whole internet.

📌 **When to use it:** **Never use this** for private APIs.
🏢 **Office example:** Unlocking the door for everyone.

### ❌ C
> **C.** Create an egress firewall rule on the VPC to allow connections to 0.0.0.0/ on ports 80 and 443.

**Wrong words:**
- ❌ "**egress firewall rule … to 0.0.0.0/**": controls outbound VPC traffic; doesn't let Cloud Run in.

📌 **When to use it:** Use egress rules to restrict outbound traffic.
🏢 **Office example:** Unlocking the exit when you need an entrance.

### ✅ D
> **D.** Deploy an internal Application Load Balancer to expose the API on GKE to the VPC. Configure Cloud DNS with the IP address of the internal Application Load Balancer. Deploy a Serverless VPC Access connector to allow the Cloud Run service to call the API through the FQDN on Cloud DNS.

**Why it's correct:**
- ✔️ "**internal Application Load Balancer to expose the API on GKE to the VPC**" matches "**privately reach the API**".
- ✔️ "**Configure Cloud DNS … FQDN**": a stable private name.
- ✔️ "**Serverless VPC Access connector**" lets Cloud Run reach the VPC, which matches "**Google-recommended practices**".

📌 **When to use it:** Use it when a serverless app must call a private service inside your network.
🏢 **Office example:** An internal reception desk, a private directory entry, and a side door from the serviced office into your corridor.

---

## 🛒 E-Commerce Full-Stack Example

GKE Ingress (internal) → `inventory.shop.internal` in Cloud DNS private zone; Cloud Run `storefront --vpc-connector=run-conn --vpc-egress=private-ranges-only`.

---

## 🧠 Key Takeaways / Memory Tips

- **Cloud Run → private VPC service → internal LB + VPC connector (or Direct VPC egress) + private DNS.**
  🧠 *"**Internal LB, private name, connector door.**"*
- Related: **Q279**, **Q162**.

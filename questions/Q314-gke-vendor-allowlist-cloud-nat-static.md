# Q314: Give an External Vendor Stable Egress IPs for GKE Traffic (Private Nodes + Cloud NAT With Static IPs)

**Topic:** Networking (Cloud NAT)

## ❓ Question
> You are deploying an application to Google Kubernetes Engine (GKE) that needs to call an external third-party API. You need to provide the external API vendor with a list of IP addresses for their firewall to allow traffic from your application. You want to follow Google-recommended practices and avoid any risk of interrupting traffic to the API due to IP address changes. What should you do?
>
> **A.** Configure your GKE cluster with one node, and set the node to have a static external IP address. Ensure that the GKE cluster autoscaler is off. Send the external IP address of the node to the vendor to be added to the allowlist.
>
> **B.** Configure your GKE cluster with private nodes. Configure a Cloud NAT instance with static IP addresses. Provide these IP addresses to the vendor to be added to the allowlist.
>
> **C.** Configure your GKE cluster with private nodes. Configure a Cloud NAT instance with dynamic IP addresses. Provide these IP addresses to the vendor to be added to the allowlist.
>
> **D.** Configure your GKE cluster with public nodes. Write a Cloud Function that pulls the public IP addresses of each node in the cluster, Trigger the function to run every day with Cloud Scheduler. Send the list to the vendor by email every day.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Vendor needs a **fixed list of IPs** that never changes.

**Clues in the question:**
- "**avoid any risk … due to IP address changes**" → **static** IPs on **Cloud NAT**; private nodes send all egress through it.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Cloud NAT with static IPs 🔑
- **What it is:** Managed outbound NAT; with manual (static) IPs, all egress comes from addresses you reserved.
- **Looks like:** `gcloud compute routers nats create gke-nat --router=r1 --nat-external-ip-pool=nat-ip-1,nat-ip-2 --nat-all-subnet-ip-ranges`
- **Not to be confused with:** auto-allocated (dynamic) NAT IPs.
- **Analogy:** 📮 All company mail leaves with the same return address.
- **In the online store:** Payment provider allowlist.

### 🔗 How they fit together
```
 private nodes → Cloud NAT (static IPs 34.x.1, 34.x.2) → vendor ✅
```

---

## 🌍 Real-World Scenario

A payment vendor allowlists two **static Cloud NAT IPs** used by private GKE nodes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure your GKE cluster with one node, and set the node to have a static external IP address. Ensure that the GKE cluster autoscaler is off. Send the external IP address of the node to the vendor to be added to the allowlist.

**Wrong words:**
- ❌ "**one node … cluster autoscaler is off**": no scaling, single point of failure.

📌 **When to use it:** **Never use this** for production.
🏢 **Office example:** One desk, one phone line, no backups.

### ✅ B
> **B.** Configure your GKE cluster with private nodes. Configure a Cloud NAT instance with static IP addresses. Provide these IP addresses to the vendor to be added to the allowlist.

**Why it's correct:**
- ✔️ "**private nodes**" + "**Cloud NAT**" matches "**call an external third-party API**" through one exit.
- ✔️ "**static IP addresses**" matches "**avoid any risk of interrupting traffic … due to IP address changes**".

📌 **When to use it:** Use it when an outside company only lets in traffic from addresses on a fixed list.
🏢 **Office example:** All company mail leaves through one mailroom with a fixed return address.

### ❌ C
> **C.** Configure your GKE cluster with private nodes. Configure a Cloud NAT instance with dynamic IP addresses. Provide these IP addresses to the vendor to be added to the allowlist.

**Wrong words:**
- ✔️ Private nodes + NAT is right.
- ❌ "**dynamic IP addresses**": can change, breaking the allowlist.

📌 **When to use it:** Use dynamic NAT IPs when nobody allowlists you.
🏢 **Office example:** A return address that may change.

### ❌ D
> **D.** Configure your GKE cluster with public nodes. Write a Cloud Function that pulls the public IP addresses of each node in the cluster, Trigger the function to run every day with Cloud Scheduler. Send the list to the vendor by email every day.

**Wrong words:**
- ❌ "**public nodes … send the list … every day**": IPs change and the vendor must keep updating. Fragile.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Emailing new phone numbers to partners daily.

---

## 🛒 E-Commerce Full-Stack Example

Cloud NAT `shopnow-egress` with `nat-ip-1`, `nat-ip-2` sent to the payment gateway.

---

## 🧠 Key Takeaways / Memory Tips

- **Fixed outbound IPs → private nodes + Cloud NAT with static IPs.**
  🧠 *"**Static NAT, steady allowlist.**"*
- Related: **Q351**, **Q158**.

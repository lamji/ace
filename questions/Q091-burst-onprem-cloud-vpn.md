# Q091: Bursting From On-Premises to Google Cloud Over Private IPs (Cloud VPN)

**Topic:** Hybrid networking (Cloud VPN, VPC peering, Shared VPC, bastion hosts)

## ❓ Question
> Your company's infrastructure is on-premises, but all machines are running at maximum capacity. You want to burst to Google Cloud. The workloads on Google Cloud must be able to directly communicate to the workloads on-premises using a private IP range. What should you do?
>
> **A.** In Google Cloud, configure the VPC as a host for Shared VPC.
>
> **B.** In Google Cloud, configure the VPC for VPC Network Peering.
>
> **C.** Create bastion hosts both in your on-premises environment and on Google Cloud. Configure both as proxy servers using their public IP addresses.
>
> **D.** Set up Cloud VPN between the infrastructure on-premises and Google Cloud.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your own data center is full. Extra work will run on Google Cloud, and those cloud machines must talk to your office machines **by private IP**. How do you connect the two places?

**Clues in the question:**
- "**on-premises**" + "**Google Cloud**": two **different places**, so you need a **link between your building and Google**.
- "**directly communicate … using a private IP range**": a private, encrypted tunnel, which is **Cloud VPN** (or Interconnect).
- Shared VPC and VPC peering only connect **Google Cloud VPCs to each other**, not to your data center.

**Exam topic:** Hybrid networking.

---

## 📚 Key Terms Explained

### 1️⃣ Bursting (cloud burst)
- **What it is:** Sending **extra work** to the cloud when your own servers are full, then scaling back down.
- **Analogy:** 🏢 Renting **temporary desks** in a co-working space when your office is full.

### 2️⃣ Cloud VPN 🔑
- **What it is:** An **encrypted tunnel over the internet** between your on-premises router and a Google Cloud VPN gateway. Machines on both sides then reach each other by **private IP**, as if on one network.
- **Looks like:** `gcloud compute vpn-tunnels create office-tunnel --peer-address=203.0.113.10 --ike-version=2 --shared-secret=... --router=office-router --vpn-gateway=gcp-gw --region=us-central1`
- **Not to be confused with:** VPC peering (cloud ↔ cloud only) or Cloud Interconnect (a dedicated physical line, faster but costlier).
- **Analogy:** 🚇 A **private tunnel** between head office and the rented desks; staff walk through without going outside.
- **In the online store:** Cloud VMs call the on-prem inventory database at `192.168.10.5`.

### 3️⃣ Private IP range
- **What it is:** Addresses like `10.x.x.x`, `172.16–31.x.x`, `192.168.x.x` that only work **inside private networks**, not on the internet.
- **Not to be confused with:** public IPs.

### 4️⃣ Shared VPC / VPC peering (review from Q079, Q060)
- **What it is:** Ways to connect **Google Cloud VPCs to each other**. Neither reaches your own data center.

### 5️⃣ Bastion host
- **What it is:** A VM used as a **jump box** to log in to other machines. Not a network link.

### 🔗 How they fit together
```
 On-premises 192.168.0.0/16 ──[ Cloud VPN encrypted tunnel ]── Google Cloud VPC 10.0.0.0/16 ✅
   inventory-db 192.168.10.5   ◄──── private IP ────►   burst VMs 10.0.1.x
```

---

## 🌍 Real-World Scenario

During peak season, a retailer's data center is maxed out. The team spins up extra workers in Google Cloud and sets up **Cloud VPN** to the office router. The cloud workers reach the on-prem database by private IP, and nothing is exposed to the internet.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In Google Cloud, configure the VPC as a host for Shared VPC.

**Wrong words:**
- ❌ "**configure the VPC as a host for Shared VPC**": Shared VPC shares a network with other **Google Cloud projects**. It doesn't connect to your data center.

📌 **When to use it:** Use it when several Google Cloud projects should use one central network.
🏢 **Office example:** Branch offices plugging into head office's phone system, but your rented desks across town are still unconnected.

### ❌ B
> **B.** In Google Cloud, configure the VPC for VPC Network Peering.

**Wrong words:**
- ❌ "**VPC Network Peering**": peering connects **two Google Cloud VPCs**. Your on-premises network isn't a VPC, so it can't peer.

📌 **When to use it:** Use it when two Google Cloud networks must talk privately.
🏢 **Office example:** Connecting two floors of the same building, when you needed a link to another city.

### ❌ C
> **C.** Create bastion hosts both in your on-premises environment and on Google Cloud. Configure both as proxy servers using their public IP addresses.

**Wrong words:**
- ❌ "**using their public IP addresses**": the question asks for a **private IP range**.
- ❌ "**bastion hosts … proxy servers**": homemade relays, not direct communication between workloads.

📌 **When to use it:** Use a bastion host as a single, guarded entry point for admins to log in.
🏢 **Office example:** Passing every message through a courier at the front door instead of building a hallway.

### ✅ D
> **D.** Set up Cloud VPN between the infrastructure on-premises and Google Cloud.

**Why it's correct:**
- ✔️ "**between the infrastructure on-premises and Google Cloud**" matches "**burst to Google Cloud**" + "**workloads on-premises**": it links your data center to Google Cloud.
- ✔️ "**Cloud VPN**" matches "**directly communicate … using a private IP range**": the tunnel carries private-IP traffic both ways, encrypted.

📌 **When to use it:** Use it when your own building and the cloud must talk privately, as one network.
🏢 **Office example:** Building a private tunnel between head office and the rented overflow desks.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's on-prem servers are full on Black Friday. Extra order-processing VMs start in Google Cloud (`10.0.1.0/24`) and connect over **HA VPN** to the data center (`192.168.0.0/16`). The cloud VMs read stock from the on-prem `inventory-db` at `192.168.10.5`, all by private IP.

---

## 🧠 Key Takeaways / Memory Tips

- **On-prem ↔ Google Cloud by private IP → Cloud VPN** (or Interconnect for big, dedicated bandwidth).
- **Peering / Shared VPC = cloud ↔ cloud only.**
  🧠 *"**Office to cloud? Tunnel it (VPN).**"*
- Related: **Q063** (on-prem Private Google Access), **Q060** (peering), **Q079** (Shared VPC).

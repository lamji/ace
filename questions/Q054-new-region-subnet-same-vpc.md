# Q054: Adding a VM in Another Region That Can Reach the App (New Subnet in the Same VPC)

**Topic:** VPC networking (global VPC, regional subnets, internal IP between regions, Cloud VPN, VPC Peering, internal load balancer)

## ❓ Question
> You are given a project with a single Virtual Private Cloud (VPC) and a single subnetwork in the us-central1 region. There is a Compute Engine instance hosting an application in this subnetwork. You need to deploy a new instance in the same project in the europe-west1 region. This new instance needs access to the application. You want to follow Google-recommended practices. What should you do?
>
> **A.** 1. Create a subnetwork in the same VPC, in europe-west1. 2. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.
>
> **B.** 1. Create a VPC and a subnetwork in europe-west1. 2. Expose the application with an internal load balancer. 3. Create the new instance in the new subnetwork and use the load balancer's address as the endpoint.
>
> **C.** 1. Create a subnetwork in the same VPC, in europe-west1. 2. Use Cloud VPN to connect the two subnetworks. 3. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.
>
> **D.** 1. Create a VPC and a subnetwork in europe-west1. 2. Peer the 2 VPCs. 3. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You have one VPC with one subnet in **us-central1**, and an app runs there. You need a new VM in **europe-west1** that can reach the app. What's the simplest Google-recommended setup?

| Keyword | What it hints at |
|---|---|
| "**single VPC**" | Reuse it. A VPC is **global**, so it can have a subnet in Europe too |
| "**europe-west1 region**" | Subnets are **regional**, so you need a **new subnet** in europe-west1 |
| "**needs access to the application**" | VMs in the **same VPC** reach each other by **private IP** automatically, in any region |
| "**Google-recommended practices**" | The simplest setup that works. No extra VPCs, VPNs or load balancers |

**Exam topic:** VPC networking.

---

## 📚 Key Terms Explained

### 1️⃣ VPC is global, subnet is regional (review from Q050)
- **What it is:** One **VPC** spans **all regions**. Each **subnet** lives in **one region**. Add a subnet per region you need, and all VMs in the VPC can talk by private IP.
- **Looks like:**
  ```
  shopnow-vpc
   ├── us-subnet   us-central1   10.0.1.0/24   🖥️ app-vm   10.0.1.5
   └── eu-subnet   europe-west1  10.0.2.0/24   🖥️ eu-vm    10.0.2.4
  ```
- **Not to be confused with:** needing a new network per region. You **don't**.
- **Analogy:** 🏢 **One company phone system** for every branch. Opening a Europe branch just means **adding a block of extensions**.
- **In the online store:** ShopNow adds a European server to the same network as its US API.

### 2️⃣ Private (internal) IP address as the endpoint
- **What it is:** The VM's **internal address** (like `10.0.1.5`), reachable only inside the network. "Endpoint" = the address the new VM calls.
- **Looks like:** `http://10.0.1.5:8080/api`
- **Not to be confused with:** a public/external IP. Private traffic stays on Google's network and costs no internet exposure.
- **Analogy:** 📞 Dialing an **internal extension** instead of the public phone number.

### 3️⃣ Cloud VPN
- **What it is:** An **encrypted tunnel over the internet** between **two different networks**, like your office network and a VPC.
- **Looks like:** `vpn-gateway-office ⇄ vpn-gateway-gcp` (IPsec tunnel)
- **Not to be confused with:** connecting subnets in the same VPC. Those are **already connected**.
- **Analogy:** 🚇 A **private tunnel** between two separate buildings.

### 4️⃣ VPC Network Peering
- **What it is:** A link between **two separate VPCs** so they can use private IPs to reach each other.
- **Looks like:** `shopnow-vpc ⇄ partner-vpc` (peering connection)
- **Not to be confused with:** something you need inside one VPC. Peering is only for **two VPCs**.
- **Analogy:** 🔗 Connecting **two companies' phone systems** so their extensions can dial each other.

### 5️⃣ Internal Load Balancer
- **What it is:** A **private address in front of a group of servers** that spreads traffic among them, reachable only inside the network.
- **Looks like:** `10.0.1.100` → app-vm-1, app-vm-2, app-vm-3
- **Not to be confused with:** a network connector. It doesn't connect **two separate VPCs**.
- **Analogy:** ☎️ A **reception desk number** that forwards calls to whichever agent is free.

### 🔗 How They Fit Together
```
✅ A: ONE VPC (global)
   ├── us-central1  10.0.1.0/24   🖥️ app  10.0.1.5
   └── europe-west1 10.0.2.0/24   🖥️ new  ──► 10.0.1.5   (works automatically)

❌ C: same VPC + Cloud VPN → VPN is for separate networks; not needed
❌ B: new VPC + internal LB → separate VPC can't reach the LB without peering/VPN
❌ D: new VPC + peering → works, but an extra VPC + peering for no reason
```

---

## 🌍 Real-World Scenario

A company expands to Europe and wants a server there that calls its existing US application. Because a VPC is **global**, the network engineer simply **adds a europe-west1 subnet** to the existing VPC. The European VM calls the US app's **private IP**, and traffic stays on Google's private network. No VPNs, no extra networks, nothing extra to maintain.

---

## 🔍 Option-by-Option Breakdown

### ✅ A (your answer)
> **A.** 1. Create a subnetwork in the same VPC, in europe-west1. 2. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.

**Why it's correct:**
- ✔️ "**same VPC**": one global VPC, so the new subnet is automatically connected to the US subnet.
- ✔️ "**in europe-west1**": subnets are regional, so you need one in the new region.
- ✔️ "**private address as the endpoint**": the new VM reaches the app directly by internal IP.

**📌 When to use it:** Use it when you need a server in a new region that must talk privately to your existing servers.
🏢 **Office example:** Opening a Europe branch on the same company phone system, so staff just dial the US office's extension.

### ❌ B
> **B.** 1. Create a VPC and a subnetwork in europe-west1. 2. Expose the application with an internal load balancer. 3. Create the new instance in the new subnetwork and use the load balancer's address as the endpoint.

**Wrong words:**
- ❌ "**Create a VPC**": a **separate** VPC can't reach the first VPC's private addresses at all (no peering or VPN is set up).
- ❌ "**Expose the application with an internal load balancer**": an internal load balancer is only reachable **inside its own VPC**, so the new VPC still can't reach it. It's also extra work for **one** app server.

**📌 When to use it:** Use an internal load balancer when several servers share the work and other servers in the same network need one address to call.
🏢 **Office example:** A reception desk number that forwards calls to whichever support agent is free.

### ❌ C
> **C.** 1. Create a subnetwork in the same VPC, in europe-west1. 2. Use Cloud VPN to connect the two subnetworks. 3. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.

**Wrong words:**
- ✔️ "**Create a subnetwork in the same VPC, in europe-west1**" is right.
- ❌ "**Use Cloud VPN to connect the two subnetworks**": subnets in the same VPC are **already connected**. A VPN is for linking **separate** networks, so this adds cost and complexity for nothing.

**📌 When to use it:** Use Cloud VPN to securely connect your office or another cloud's network to your VPC.
🏢 **Office example:** Building a private tunnel between your office and a partner company's building.

### ❌ D
> **D.** 1. Create a VPC and a subnetwork in europe-west1. 2. Peer the 2 VPCs. 3. Create the new instance in the new subnetwork and use the first instance's private address as the endpoint.

**Wrong words:**
- ❌ "**Create a VPC**": a new VPC isn't needed, because the existing VPC is global and can have a Europe subnet.
- ❌ "**Peer the 2 VPCs**": this would work, but it's an extra network plus a peering link to maintain. That isn't the simplest, Google-recommended setup.

**📌 When to use it:** Use VPC peering when two networks must stay separate (different teams or companies) but still talk privately.
🏢 **Office example:** Connecting two companies' phone systems so their staff can dial each other's extensions.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's inventory API runs on `inventory-us` (10.0.1.5) in `shopnow-vpc` (us-central1). A new **EU order-processing** VM in Belgium must call it.

```bash
# ① Add a Europe subnet to the SAME VPC
gcloud compute networks subnets create eu-subnet \
  --network=shopnow-vpc --region=europe-west1 --range=10.0.2.0/24

# ② Create the EU VM in it
gcloud compute instances create orders-eu --zone=europe-west1-b --subnet=eu-subnet

# ③ The EU VM calls the US API by private IP
curl http://10.0.1.5:8080/stock/red-sneaker
```

*(A firewall rule must still allow the traffic, e.g. ingress from 10.0.2.0/24 on tcp:8080, as in Q053.)*

| Option | Extra things to build and maintain | Works? |
|---|---|---|
| **A** | 1 subnet | ✅ |
| C | 1 subnet + VPN gateways + tunnels | ✅ but wasteful |
| D | 1 VPC + 1 subnet + peering | ✅ but wasteful |
| B | 1 VPC + 1 subnet + internal load balancer | ❌ new VPC can't reach it |

---

## 🧠 Key Takeaways / Memory Tips

- **New region, same project, needs private access → add a subnet in that region to the SAME VPC.**
  🧠 *"**VPC = global, subnet = regional.** New region? New subnet, same VPC."*
- **VPN and peering are for connecting DIFFERENT networks.** Never needed between subnets of one VPC.
- **Simplest option that works = Google-recommended.**
- Related: **Q050** (one VPC, different CIDR), **Q053** (firewall rules still needed for traffic).

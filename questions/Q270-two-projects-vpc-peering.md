# Q270: Frontend in vpc-a, Backend in vpc-b, Different Projects (VPC Network Peering)

**Topic:** Networking (VPC Network Peering)

## ❓ Question
> You have two Google Cloud projects: project-a with VPC vpc-a (10.0.0.0/16) and project-b with VPC vpc-b (10.8.0.0/16). Your frontend application resides in vpc-a and the backend API services are deployed in vpc-b. You need to efficiently and cost-effectively enable communication between these Google Cloud projects. You also want to follow Google-recommended practices. What should you do?
>
> **A.** Create an OpenVPN connection between vpc-a and vpc-b.
>
> **B.** Create VPC Network Peering between vpc-a and vpc-b.
>
> **C.** Configure a Cloud Router in vpc-a and another Cloud Router in vpc-b.
>
> **D.** Configure a Cloud Interconnect connection between vpc-a and vpc-b.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** project-a has VPC vpc-a (10.0.0.0/16) with the frontend; project-b has vpc-b (10.8.0.0/16) with the backend APIs.
- **What you must achieve:** Let the frontend talk to the backend.
- **The limits:** Efficient, low cost, and recommended practice.
- **What they're really asking:** How do you connect the two networks privately?

**Clues in the question:**
- Two Google Cloud VPCs with **non-overlapping** ranges → **VPC Network Peering** (private, Google's network, no gateways).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. VPC Network Peering 🔑
- **What it is:** Connects two VPCs (even across projects/orgs) so they use internal IPs directly. Ranges must not overlap.
- **Looks like:** `gcloud compute networks peerings create a-to-b --network=vpc-a --peer-project=project-b --peer-network=vpc-b` (and the reverse)
- **Not to be confused with:** VPN.
- **Analogy:** 🚪 A connecting door between two offices.
- **In the online store:** Storefront ↔ API.

### 🔗 How they fit together
```
 vpc-a 10.0.0.0/16 ◄═ peering ═► vpc-b 10.8.0.0/16 ✅
```

---

## 🌍 Real-World Scenario

Frontend and backend teams use separate projects. The admins create **VPC Network Peering** in both directions; services talk over internal IPs.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an OpenVPN connection between vpc-a and vpc-b.

**Wrong words:**
- ❌ "**OpenVPN connection**": self-managed VMs and encryption overhead; not needed inside Google Cloud.

📌 **When to use it:** Use VPNs to connect to on-premises or other clouds.
🏢 **Office example:** Building a tunnel between two rooms of the same building.

### ✅ B
> **B.** Create VPC Network Peering between vpc-a and vpc-b.

**Why it's correct:**
- ✔️ "**VPC Network Peering between vpc-a and vpc-b**" matches "**efficiently and cost-effectively enable communication**".
- ✔️ The ranges 10.0.0.0/16 and 10.8.0.0/16 don't overlap, so peering works, which matches "**Google-recommended practices**".

📌 **When to use it:** Use it when two teams' private networks in Google Cloud need to talk directly.
🏢 **Office example:** Putting a connecting door between two neighboring offices.

### ❌ C
> **C.** Configure a Cloud Router in vpc-a and another Cloud Router in vpc-b.

**Wrong words:**
- ❌ "**Cloud Router in vpc-a and another … in vpc-b**": Cloud Routers exchange routes for VPN/Interconnect; alone they don't connect VPCs.

📌 **When to use it:** Use Cloud Router with HA VPN or Interconnect.
🏢 **Office example:** Two receptionists with no phone line between them.

### ❌ D
> **D.** Configure a Cloud Interconnect connection between vpc-a and vpc-b.

**Wrong words:**
- ❌ "**Cloud Interconnect**": a physical link to on-premises; expensive and not for VPC-to-VPC.

📌 **When to use it:** Use Interconnect for high-bandwidth on-prem links.
🏢 **Office example:** Laying a fiber cable between two rooms in one building.

---

## 🛒 E-Commerce Full-Stack Example

`shop-frontend-vpc` (10.0.0.0/16) ⇄ peering ⇄ `shop-api-vpc` (10.8.0.0/16).

---

## 🧠 Key Takeaways / Memory Tips

- **Connect two Google Cloud VPCs, non-overlapping ranges → VPC Network Peering.**
  🧠 *"**Neighbors? Open a connecting door (peering).**"*
- Related: **Q259**, **Q179**.

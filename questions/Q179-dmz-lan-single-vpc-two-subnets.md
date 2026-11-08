# Q179: DMZ + LAN on Compute Engine (One VPC, Two Subnets, Firewall Rules, Public Ingress to the DMZ)

**Topic:** Networking (VPC design, firewall ingress vs egress)

## ❓ Question
> Your company is moving its entire workload to Compute Engine. Some servers should be accessible through the Internet, and other servers should only be accessible over the internal network. All servers need to be able to talk to each other over specific ports and protocols. The current on-premises network relies on a demilitarized zone (DMZ) for the public servers and a Local Area Network (LAN) for the private servers. You need to design the networking infrastructure on Google Cloud to match these requirements. What should you do?
>
> **A.** 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.
>
> **B.** 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.
>
> **C.** 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.
>
> **D.** 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company is moving all servers to Compute Engine. Some servers must be reachable from the internet, others only internally, and all must talk to each other on certain ports. On-premises you used a DMZ (a public zone) and a LAN (the private internal network).
- **What you must achieve:** Design the Google Cloud network to match.
- **The limits:** Keep the public/private split, and allow only specific ports between them.
- **What they're really asking:** How should you lay out the network and firewall rules?

**Clues in the question:**
- "**talk to each other**" → **one VPC** (subnets in one VPC can route to each other; separate VPCs can't without peering/VPN).
- "**accessible through the Internet**" → incoming traffic → **ingress** rule.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Ingress vs egress 🔑
- **What it is:** **Ingress** = traffic coming **in** to VMs. **Egress** = traffic going **out**.
- **Looks like:** `--direction=INGRESS --source-ranges=0.0.0.0/0 --target-tags=dmz --allow=tcp:443`
- **Not to be confused with:** —
- **Analogy:** 🚪 Front door in vs out.
- **In the online store:** Shoppers → web servers = ingress.

### 2. Subnets in one VPC
- **What it is:** All subnets in a VPC share routes, so firewall rules decide what can talk.
- **Looks like:** `dmz 10.0.1.0/24`, `lan 10.0.2.0/24`
- **Not to be confused with:** separate VPCs.
- **Analogy:** 🏢 Two floors in one building.
- **In the online store:** web tier vs DB tier.

### 3. DMZ
- **What it is:** A network zone for **public-facing** servers, separated from the internal LAN.
- **Looks like:** web, mail servers
- **Not to be confused with:** the LAN.
- **Analogy:** 🛎️ The lobby.
- **In the online store:** Storefront servers.

### 🔗 How they fit together
```
 internet ─INGRESS 443─► [dmz subnet] ◄─fw rules─► [lan subnet]   (one VPC) ✅
```

---

## 🌍 Real-World Scenario

A company lifts its DMZ/LAN design into one VPC with two subnets. Firewall rules allow specific ports between them, and one **ingress** rule lets the internet reach the DMZ servers.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.

**Why it's correct:**
- ✔️ "**single VPC with a subnet for the DMZ and a subnet for the LAN**" matches "**All servers need to be able to talk to each other**".
- ✔️ "**firewall rules to open up relevant traffic between the DMZ and the LAN**" matches "**over specific ports and protocols**".
- ✔️ "**allow public ingress traffic for the DMZ**" matches "**Some servers should be accessible through the Internet**".

📌 **When to use it:** Use it when public and private servers are in one building and only the lobby is open to visitors.
🏢 **Office example:** One office building: a public lobby open to visitors, a staff floor behind it, and set doors between them.

### ❌ B
> **B.** 1. Create a single VPC with a subnet for the DMZ and a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.

**Wrong words:**
- ❌ "**public egress traffic for the DMZ**": egress is **outgoing**. It doesn't let the internet reach the DMZ.

📌 **When to use it:** Use egress rules to control what goes out.
🏢 **Office example:** Unlocking the exit when visitors need the entrance.

### ❌ C
> **C.** 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public ingress traffic for the DMZ.

**Wrong words:**
- ❌ "**another VPC … for the LAN**": separate VPCs can't talk without peering/VPN, so firewall rules alone don't connect them.

📌 **When to use it:** Use separate VPCs for fully separate environments.
🏢 **Office example:** Two buildings with no corridor between them.

### ❌ D
> **D.** 1. Create a VPC with a subnet for the DMZ and another VPC with a subnet for the LAN. 2. Set up firewall rules to open up relevant traffic between the DMZ and the LAN subnets, and another firewall rule to allow public egress traffic for the DMZ.

**Wrong words:**
- ❌ "**another VPC**" and ❌ "**egress**": wrong on both counts.

📌 **When to use it:** **Never use this** for this need.
🏢 **Office example:** Two buildings with only the exit unlocked.

---

## 🛒 E-Commerce Full-Stack Example

`shop-vpc`: `dmz` (storefront VMs, tag `web`) + `lan` (order DB, tag `db`). Rules: allow `0.0.0.0/0 → web tcp:443` (ingress); allow `web → db tcp:5432`.

---

## 🧠 Key Takeaways / Memory Tips

- **Must talk → same VPC (subnets). Internet reaches servers → ingress rule.**
  🧠 *"**In from the internet = ingress.**"*
- Related: **Q151**, **Q098**.

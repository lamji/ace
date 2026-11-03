# Q195: Robust HA VPN With Dynamic Routing, No Over-Provisioning on Failover (Custom VPC, Cloud Router BGP, Active/Passive)

**Topic:** Networking (HA VPN, Cloud Router, BGP)

## ❓ Question
> You have been asked to create robust Virtual Private Network (VPN) connectivity between a new Virtual Private Cloud (VPC) and a remote site. Key requirements include dynamic routing, a shared address space of 10.19.0.1/22, and no overprovisioning of tunnels during a failover event. You want to follow Google-recommended practices to set up a high availability Cloud VPN. What should you do?
>
> **A.** Use a custom mode VPC network, configure static routes, and use active/passive routing.
>
> **B.** Use an automatic mode VPC network, configure static routes, and use active/active routing.
>
> **C.** Use a custom mode VPC network, use Cloud Router border gateway protocol (BGP) routes, and use active/passive routing.
>
> **D.** Use an automatic mode VPC network, use Cloud Router border gateway protocol (BGP) routes, and configure policy-based routing.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** HA VPN with **dynamic routing**, a **specific IP range**, and **no extra tunnel load** when one fails.

**Clues in the question:**
- "**dynamic routing**" → **Cloud Router + BGP** (static routes are not dynamic).
- "**shared address space of 10.19.0.1/22**" → **custom mode** VPC (auto mode picks its own 10.128.0.0/9 ranges).
- "**no overprovisioning of tunnels during a failover**" → **active/passive** (the standby tunnel takes over, total capacity is the same).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Cloud Router + BGP 🔑
- **What it is:** Cloud Router exchanges routes with your on-prem router using **BGP**, so routes update **automatically**.
- **Looks like:** `gcloud compute routers create vpn-router --asn=65001`
- **Not to be confused with:** static routes.
- **Analogy:** 📡 Two receptionists who keep updating each other's directories.
- **In the online store:** ShopNow ↔ warehouse network.

### 2. Custom vs auto mode VPC
- **What it is:** **Custom**: you choose subnets and ranges. **Auto**: one subnet per region from 10.128.0.0/9.
- **Looks like:** `--subnet-mode=custom`
- **Not to be confused with:** —
- **Analogy:** 🏗️ Designing your own floor plan vs a standard one.
- **In the online store:** —

### 3. Active/passive
- **What it is:** One tunnel carries traffic; the other waits. On failover, the standby takes the same load, so you don't need to size each tunnel for double.
- **Looks like:** —
- **Not to be confused with:** active/active.
- **Analogy:** 🚗 A spare car in the garage.
- **In the online store:** —

### 🔗 How they fit together
```
 VPC (custom, 10.19.0.0/22) ─ HA VPN gw ═ tunnel1 (active) ═╗
                     Cloud Router BGP      tunnel2 (passive)╝═ on-prem router ✅
```

---

## 🌍 Real-World Scenario

A company links a new VPC to a remote office. They use a **custom VPC** with the agreed range, **HA VPN with Cloud Router BGP**, and **active/passive** tunnels so a failover doesn't overload anything.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use a custom mode VPC network, configure static routes, and use active/passive routing.

**Wrong words:**
- ✔️ "custom mode" and "active/passive" are right.
- ❌ "**configure static routes**": not **dynamic routing**.

📌 **When to use it:** Use static routes for a simple, unchanging link.
🏢 **Office example:** A printed directory nobody updates.

### ❌ B
> **B.** Use an automatic mode VPC network, configure static routes, and use active/active routing.

**Wrong words:**
- ❌ "**automatic mode VPC**": you can't choose 10.19.0.0/22.
- ❌ "**static routes**": not dynamic.
- ❌ "**active/active**": on failover, one tunnel must carry double, so you overprovision.

📌 **When to use it:** Use auto mode for quick test networks.
🏢 **Office example:** A standard floor plan that doesn't match your address.

### ✅ C
> **C.** Use a custom mode VPC network, use Cloud Router border gateway protocol (BGP) routes, and use active/passive routing.

**Why it's correct:**
- ✔️ "**custom mode VPC network**" matches "**shared address space of 10.19.0.1/22**".
- ✔️ "**Cloud Router border gateway protocol (BGP) routes**" matches "**dynamic routing**".
- ✔️ "**active/passive routing**" matches "**no overprovisioning of tunnels during a failover event**".

📌 **When to use it:** Use it when two offices need a reliable private link with a backup line that only takes over if the main one fails.
🏢 **Office example:** Two receptionists who keep each other's directories up to date, with a backup phone line on standby.

### ❌ D
> **D.** Use an automatic mode VPC network, use Cloud Router border gateway protocol (BGP) routes, and configure policy-based routing.

**Wrong words:**
- ❌ "**automatic mode**": wrong range.
- ❌ "**policy-based routing**": HA VPN doesn't support policy-based (static selector) routing.

📌 **When to use it:** Use policy-based routing only with Classic VPN and old devices.
🏢 **Office example:** An old switchboard that the new system doesn't support.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute networks create shop-hybrid --subnet-mode=custom
gcloud compute networks subnets create core --network=shop-hybrid --range=10.19.0.0/22 --region=us-east1
gcloud compute routers create hybrid-router --network=shop-hybrid --region=us-east1 --asn=65010
gcloud compute vpn-gateways create hybrid-gw --network=shop-hybrid --region=us-east1
```

---

## 🧠 Key Takeaways / Memory Tips

- **Dynamic routing → Cloud Router BGP. Your own range → custom VPC. No overprovisioning → active/passive.**
  🧠 *"**Dynamic = BGP; custom = your range; passive = no double load.**"*
- Related: **Q091**, **Q162**.

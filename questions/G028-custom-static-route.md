# G028: Send Internet-Bound Traffic From Tagged VMs Through a Proxy Appliance VM (Custom Static Route)

**Topic:** VPC networking (custom static routes)
**Exam guide section:** 3.3 Managing networking resources: Adding custom static routes in a VPC

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your security policy requires that all internet-bound traffic from VMs with the network tag inspect go through a third-party firewall appliance running on a VM named fw-appliance in the same VPC. Other VMs must keep using the default internet route. What should you do?
>
> **A.** Create a firewall rule that allows egress to 0.0.0.0/0 from VMs with the inspect tag.
>
> **B.** Create a custom static route for destination 0.0.0.0/0 with next hop instance fw-appliance, apply it only to the inspect tag, and give it a higher priority than the default route.
>
> **C.** Assign the fw-appliance VM a static external IP address.
>
> **D.** Delete the VPC's default route to the internet.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Some VMs carry the label (network tag) `inspect`. Security wants their internet traffic checked by a firewall product running on a VM called fw-appliance.
- **What you must achieve:** Send all internet-bound traffic from the `inspect` VMs through fw-appliance first.
- **The limits:** Every other VM must keep going straight to the internet as before.
- **What they're really asking:** How do you change the path traffic takes for only some VMs?

**Clues in the question:**
- "**go through … a VM**": a route with **next hop instance**.
- "**internet-bound**": destination **0.0.0.0/0**.
- "**only VMs with the network tag inspect**" + "**others keep the default**": a **tagged** route with **higher priority** (a lower number) than the default route.

**Exam topic:** Networking (exam guide section 3.3).

---

## 📚 Key Terms Explained

### 1. Route
- **What it is:** A VPC rule that says where to send packets for a destination range. The most specific range wins, and among equally specific ranges the lowest priority number wins.
- **Looks like:** Default route: `0.0.0.0/0 → default-internet-gateway, priority 1000`
- **Not to be confused with:** A firewall rule. Routes choose the path, firewalls allow or deny.
- **Analogy:** 🗺️ A road sign: "Downtown → this way".
- **In the online store:** All ShopNow VMs reach the internet via the default route.

### 2. Custom static route 🔑
- **What it is:** A route you create yourself, with a destination, next hop (instance, IP, VPN tunnel, internal load balancer…), optional network tags and a priority.
- **Looks like:** `gcloud compute routes create inspect-egress --network=shop-vpc --destination-range=0.0.0.0/0 --next-hop-instance=fw-appliance --next-hop-instance-zone=us-central1-a --tags=inspect --priority=800`
- **Not to be confused with:** Dynamic routes learned through Cloud Router (BGP).
- **Analogy:** 🚧 A detour sign just for delivery trucks.
- **In the online store:** Payment VMs exit through the inspection appliance.

### 🔗 How they fit together
```
 VM (tag inspect) ─0.0.0.0/0, prio 800─► fw-appliance ─► internet ✅
 Other VMs        ─0.0.0.0/0, prio 1000 (default)─► internet gateway
```

---

## 🌍 Real-World Scenario

A payments company must inspect all outbound traffic from its card-processing VMs. A **custom static route** sends their internet traffic to the inspection appliance VM (which has IP forwarding enabled), while web servers keep the normal fast path.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a firewall rule that allows egress to 0.0.0.0/0 from VMs with the inspect tag.

**Wrong words:**
- ❌ "**firewall rule that allows egress**": firewalls allow or deny traffic, they don't change the path. Traffic would still go straight to the internet.

📌 **When to use it:** Use egress rules to control which outbound traffic is allowed.
🏢 **Office example:** A guard that lets trucks leave but doesn't send them through inspection.

### ✅ B
> **B.** Create a custom static route for destination 0.0.0.0/0 with next hop instance fw-appliance, apply it only to the inspect tag, and give it a higher priority than the default route.

**Why it's correct:**
- ✔️ "**custom static route for destination 0.0.0.0/0**" matches "**internet-bound traffic**".
- ✔️ "**next hop instance fw-appliance**" matches "**go through … fw-appliance**".
- ✔️ "**apply it only to the inspect tag**" + "**higher priority than the default route**" matches "**VMs with the network tag inspect**" and "**Other VMs must keep using the default**".

📌 **When to use it:** Use it when some machines' traffic must take a special path, like through an inspection checkpoint.
🏢 **Office example:** A detour sign that sends only delivery trucks through the inspection gate.

### ❌ C
> **C.** Assign the fw-appliance VM a static external IP address.

**Wrong words:**
- ❌ "**static external IP**": gives the appliance a fixed public address but doesn't send other VMs' traffic through it.

📌 **When to use it:** Use it when a server needs a public address that never changes.
🏢 **Office example:** Giving the inspection booth a street address but no detour signs.

### ❌ D
> **D.** Delete the VPC's default route to the internet.

**Wrong words:**
- ❌ "**Delete the VPC's default route**": cuts internet access for every VM, which breaks "**Other VMs must keep using the default internet route**".

📌 **When to use it:** Use it only for fully private networks that need no internet path at all.
🏢 **Office example:** Closing the main exit for everyone.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: route `pci-egress` (0.0.0.0/0 → `fw-appliance`, tags `pci`, priority 800). `fw-appliance` is created with `--can-ip-forward`. Storefront VMs keep the default route.

---

## 🧠 Key Takeaways / Memory Tips

- **Change the path for some VMs → custom static route (destination, next hop, tags, priority).** Firewalls allow or deny; routes steer.
  🧠 *"**Routes steer, firewalls filter.**"*
- Related: **Q063**, **Q195**, **Q314** (NAT).

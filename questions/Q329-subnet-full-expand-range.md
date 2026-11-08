# Q329: Subnet Running Out of IPs, No Downtime (Expand the Primary IP Range)

**Topic:** Networking (subnet expansion)

## ❓ Question
> You manage a VPC network in Google Cloud with a subnet that is rapidly approaching its private IP address capacity. You expect the number of Compute Engine VM instances in the same region to double within a week. You need to implement a Google-recommended solution that minimizes operational costs and does not require downtime. What should you do?
>
> **A.** Create a second VPC with the same subnet IP range, and connect this VPC to the existing VPC by using VPC Network Peering.
>
> **B.** Delete the existing subnet, and create a new subnet with double the IP range available.
>
> **C.** Permit additional traffic from the expected range of private IP addresses to reach your VMs by configuring firewall rules.
>
> **D.** Use the Google Cloud CLI tool to expand the primary IP range of your subnet.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A subnet is almost out of private IP addresses, and the number of VMs in that region will double within a week.
- **What you must achieve:** Make room for the new VMs.
- **The limits:** Recommended practice, low operating cost, and no downtime.
- **What they're really asking:** How do you get more addresses without downtime?

**Clues in the question:**
- "**does not require downtime**" → **expand-ip-range** (non-disruptive).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. gcloud compute networks subnets expand-ip-range 🔑
- **What it is:** Grows a subnet's primary range (smaller prefix) without disrupting VMs; can't shrink.
- **Looks like:** `gcloud compute networks subnets expand-ip-range web --region=us-central1 --prefix-length=22`
- **Not to be confused with:** recreating the subnet.
- **Analogy:** 🏠 Adding rooms without moving out.
- **In the online store:** ShopNow web subnet.

### 🔗 How they fit together
```
 10.0.0.0/24 → expand → 10.0.0.0/23 ✅ (no downtime)
```

---

## 🌍 Real-World Scenario

The web subnet is nearly full; the engineer expands `/24` to `/23` live.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a second VPC with the same subnet IP range, and connect this VPC to the existing VPC by using VPC Network Peering.

**Wrong words:**
- ❌ "**second VPC with the same subnet IP range … Peering**": overlapping ranges can't peer.

📌 **When to use it:** Use peering for non-overlapping VPCs.
🏢 **Office example:** Two buildings with the same room numbers joined by a hallway.

### ❌ B
> **B.** Delete the existing subnet, and create a new subnet with double the IP range available.

**Wrong words:**
- ❌ "**Delete the existing subnet**": requires removing all VMs, causing downtime.

📌 **When to use it:** **Avoid** for live subnets.
🏢 **Office example:** Tearing down the building to add rooms.

### ❌ C
> **C.** Permit additional traffic from the expected range of private IP addresses to reach your VMs by configuring firewall rules.

**Wrong words:**
- ❌ "**firewall rules**": controls traffic, doesn't add IPs.

📌 **When to use it:** Use firewalls for access control.
🏢 **Office example:** Changing door rules to make more rooms.

### ✅ D
> **D.** Use the Google Cloud CLI tool to expand the primary IP range of your subnet.

**Why it's correct:**
- ✔️ "**expand the primary IP range of your subnet**" matches "**approaching its private IP address capacity**" + "**does not require downtime**".

📌 **When to use it:** Use it when the room you have is filling up and you can grow it in place.
🏢 **Office example:** Knocking out a wall to add desks while staff keep working.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute networks subnets expand-ip-range shopnow-web --region=us-central1 --prefix-length=22`

---

## 🧠 Key Takeaways / Memory Tips

- **Subnet full, no downtime → expand-ip-range.**
  🧠 *"**Expand, don't recreate.**"*
- Related: **Q214**.

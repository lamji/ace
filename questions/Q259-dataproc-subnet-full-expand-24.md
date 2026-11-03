# Q259: Dataproc Subnet 172.16.20.128/25 Is Full; Add VMs With Fewest Steps (Expand the Subnet to 172.16.20.0/24)

**Topic:** Networking (expanding subnet ranges)

## ❓ Question
> Your Dataproc cluster runs in a single Virtual Private Cloud (VPC) network in a single subnetwork with range 172.16.20.128/25. There are no private IP addresses available in the subnetwork. You want to add new VMs to communicate with your cluster using the minimum number of steps. What should you do?
>
> **A.** Modify the existing subnet range to 172.16.20.0/24.
>
> **B.** Create a new Secondary IP Range in the VPC and configure the VMs to use that range.
>
> **C.** Create a new VPC network for the VMs. Enable VPC Peering between the VMs'VPC network and the Dataproc cluster VPC network.
>
> **D.** Create a new VPC network for the VMs with a subnet of 172.32.0.0/16. Enable VPC network Peering between the Dataproc VPC network and the VMs VPC network. Configure a custom Route exchange.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Subnet is full. Add VMs with the **fewest steps**.

**Clues in the question:**
- "**no private IP addresses available**" + "**minimum number of steps**" → **expand** the subnet (/25 → /24 covers 172.16.20.0–255, including the old range).
- One command, no new networks.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Expand subnet 🔑 (review from Q214)
- **What it is:** Make the primary range bigger in place; existing IPs stay.
- **Looks like:** `gcloud compute networks subnets expand-ip-range dp-subnet --region=us-central1 --prefix-length=24`
- **Not to be confused with:** new VPC.
- **Analogy:** 📞 More extensions, same numbers kept.
- **In the online store:** —

### 🔗 How they fit together
```
 172.16.20.128/25 (128 IPs) ─expand─► 172.16.20.0/24 (256 IPs) ✅ (contains old range)
```

---

## 🌍 Real-World Scenario

A Dataproc subnet runs out of IPs. The admin expands it from /25 to **/24** in one command and adds the new VMs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Modify the existing subnet range to 172.16.20.0/24.

**Why it's correct:**
- ✔️ "**Modify the existing subnet range to 172.16.20.0/24**" matches "**no private IP addresses available**": doubles the addresses and contains the old range.
- ✔️ One command matches "**minimum number of steps**".

📌 **When to use it:** Use it when a group runs out of numbers and a bigger block next door is free.
🏢 **Office example:** Expanding the phone system to more extensions while everyone keeps theirs.

### ❌ B
> **B.** Create a new Secondary IP Range in the VPC and configure the VMs to use that range.

**Wrong words:**
- ❌ "**Secondary IP Range … configure the VMs to use that range**": secondary ranges are for alias IPs; VMs' primary NICs can't use them.

📌 **When to use it:** Use secondary ranges for GKE pods/services.
🏢 **Office example:** Extension numbers only one department can dial.

### ❌ C
> **C.** Create a new VPC network for the VMs. Enable VPC Peering between the VMs'VPC network and the Dataproc cluster VPC network.

**Wrong words:**
- ❌ "**new VPC network … VPC Peering**": many more steps.

📌 **When to use it:** Use peering to connect separate networks.
🏢 **Office example:** Building a new office and a corridor.

### ❌ D
> **D.** Create a new VPC network for the VMs with a subnet of 172.32.0.0/16. Enable VPC network Peering between the Dataproc VPC network and the VMs VPC network. Configure a custom Route exchange.

**Wrong words:**
- ❌ "**new VPC … Peering … custom Route exchange**": even more steps. (Also 172.32.0.0/16 isn't private RFC 1918 space.)

📌 **When to use it:** Use it for connecting separate teams' networks.
🏢 **Office example:** A new building, a corridor, and new signs.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute networks subnets expand-ip-range analytics --region=us-central1 --prefix-length=24`

---

## 🧠 Key Takeaways / Memory Tips

- **Subnet full, fewest steps → expand the range** (smaller prefix number).
  🧠 *"**/25 → /24 = double.**"*
- Related: **Q214**, **Q149**.

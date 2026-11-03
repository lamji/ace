# Q129: No Free IPs in the Dataproc Subnet, Minimum Steps (Expand the Subnet Range)

**Topic:** VPC networking (subnet expansion, CIDR, secondary ranges, peering)

## ❓ Question
> Your Dataproc cluster runs in a single Virtual Private Cloud (VPC) network in a single subnet with range 172.16.20.128/25. There are no private IP addresses available in the VPC network. You want to add new VMs to communicate with your cluster using the minimum number of steps. What should you do?
>
> **A.** Modify the existing subnet range to 172.16.20.0/24.
>
> **B.** Create a new Secondary IP Range in the VPC and configure the VMs to use that range.
>
> **C.** Create a new VPC network for the VMs. Enable VPC Peering between the VMs' VPC network and the Dataproc cluster VPC network.
>
> **D.** Create a new VPC network for the VMs with a subnet of 172.32.0.0/16. Enable VPC network Peering between the Dataproc VPC network and the VMs VPC network. Configure a custom Route exchange.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The subnet `172.16.20.128/25` (128 addresses) is full. You need room for new VMs that talk to Dataproc, in the **fewest steps**.

**Clues in the question:**
- "**no private IP addresses available**" → make the range **bigger**.
- `172.16.20.0/24` **contains** `172.16.20.128/25` (it's the same block, doubled), so it's a valid **expansion**: one command.
- "**minimum number of steps**": one change, versus new VPCs plus peering plus routes.

**Exam topic:** VPC networking.

---

## 📚 Key Terms Explained

### 1. Subnet expansion 🔑 (review from Q082)
- **What it is:** Making a subnet's range **larger** (smaller prefix number) in place, with no downtime. The new range must **contain the old one**.
- **Looks like:** `gcloud compute networks subnets expand-ip-range dataproc-subnet --region=us-central1 --prefix-length=24`
- **Not to be confused with:** creating a new subnet.
- **Analogy:** 🔨 Knocking down a wall to double the floor space.
- **In the online store:** Grow the analytics subnet before adding workers.

### 2. CIDR /25 vs /24
- **What it is:** `/25` = 128 addresses (here .128–.255). `/24` = 256 addresses (.0–.255). The /24 includes the /25.
- **Looks like:** `172.16.20.128/25` ⊂ `172.16.20.0/24`
- **Not to be confused with:** two unrelated ranges.
- **Analogy:** 🏢 Half a floor vs the whole floor.
- **In the online store:** Room for 128 more VMs.

### 3. Secondary IP range
- **What it is:** An extra range on a subnet, used for **alias IPs** (for example, GKE pods). It doesn't give VMs their main address.
- **Looks like:** `--secondary-range pods=10.4.0.0/14`
- **Not to be confused with:** more primary addresses for VMs.
- **Analogy:** 🪑 Extra seats reserved for visitors only.
- **In the online store:** GKE pod IPs.

### 🔗 How they fit together
```
 before: 172.16.20.128/25  → .128–.255 (full) ❌
 after:  172.16.20.0/24    → .0–.255  (old IPs kept, +128 free) ✅ one command
```

---

## 🌍 Real-World Scenario

A data team's Dataproc subnet is full and new edge VMs can't be created. The engineer runs **expand-ip-range** to /24. The cluster keeps its IPs, the new VMs get addresses in the same subnet, and everything talks right away.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Modify the existing subnet range to 172.16.20.0/24.

**Why it's correct:**
- ✔️ "**Modify the existing subnet range**" matches "**minimum number of steps**": one command (`expand-ip-range`).
- ✔️ "**172.16.20.0/24**" matches "**no private IP addresses available**": it contains the old /25 and doubles the space.
- ✔️ "**existing subnet**" matches "**communicate with your cluster**": new VMs are in the same subnet, with no extra routing.

📌 **When to use it:** Use it when the space is full and you can make the same space bigger.
🏢 **Office example:** Knocking down the wall to the empty half of the floor so new staff sit with the team.

### ❌ B
> **B.** Create a new Secondary IP Range in the VPC and configure the VMs to use that range.

**Wrong words:**
- ❌ "**Secondary IP Range … configure the VMs to use that range**": secondary ranges are for alias IPs (like GKE pods). VMs still need a primary IP from the full range.

📌 **When to use it:** Use secondary ranges for GKE pods and services.
🏢 **Office example:** Reserving visitor seats when you need staff desks.

### ❌ C
> **C.** Create a new VPC network for the VMs. Enable VPC Peering between the VMs' VPC network and the Dataproc cluster VPC network.

**Wrong words:**
- ❌ "**Create a new VPC network … Enable VPC Peering**": several steps when one expansion is enough.

📌 **When to use it:** Use peering when two separately owned networks must connect.
🏢 **Office example:** Renting a new building and building a bridge, when you could use the other half of your floor.

### ❌ D
> **D.** Create a new VPC network for the VMs with a subnet of 172.32.0.0/16. Enable VPC network Peering between the Dataproc VPC network and the VMs VPC network. Configure a custom Route exchange.

**Wrong words:**
- ❌ "**new VPC … peering … custom Route exchange**": even more steps.
- ❌ "**172.32.0.0/16**": that's not even a private range (private is 172.16.0.0/12, up to 172.31.x.x).

📌 **When to use it:** **Never use this.** Expand the subnet (A).
🏢 **Office example:** A new building, a bridge, extra road signs, and an address outside your city.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute networks subnets expand-ip-range analytics-subnet \
  --region=us-central1 --prefix-length=24
# 172.16.20.128/25 → 172.16.20.0/24
gcloud compute instances create report-edge-1 --subnet=analytics-subnet --zone=us-central1-a
```

---

## 🧠 Key Takeaways / Memory Tips

- **Subnet full, minimum steps → expand the range** (the new range must contain the old one).
- Secondary ranges are alias IPs, not VM addresses.
  🧠 *"**Out of IPs? Expand.**"*
- Related: **Q082** (expand-ip-range), **Q002** (CIDR), **Q060** (peering).

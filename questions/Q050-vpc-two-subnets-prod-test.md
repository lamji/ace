# Q050: Prod and Test in Different Subnets That Can Still Talk (One VPC, Non-Overlapping CIDR)

**Topic:** VPC networking (global VPC, regional subnets, CIDR ranges must not overlap, automatic subnet routes, separate VPCs)

## ❓ Question
> You have production and test workloads that you want to deploy on Compute Engine. Production VMs need to be in a different subnet than the test VMs. All the VMs must be able to reach each other over Internal IP without creating additional routes. You need to set up VPC and the 2 subnets. Which configuration meets these requirements?
>
> **A.** Create a single custom VPC with 2 subnets. Create each subnet in a different region and with a different CIDR range.
>
> **B.** Create a single custom VPC with 2 subnets. Create each subnet in the same region and with the same CIDR range.
>
> **C.** Create 2 custom VPCs, each with a single subnet. Create each subnet in a different region and with a different CIDR range.
>
> **D.** Create 2 custom VPCs, each with a single subnet. Create each subnet in the same region and with the same CIDR range.

**My answer:** B
**Correct answer:** A
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** Prod VMs and test VMs must be in **two different subnets**, but **all VMs must reach each other by private (internal) IP** with **no extra routes**. Which setup works?

| Keyword | What it hints at |
|---|---|
| "**different subnet**" | 2 subnets |
| "**reach each other over Internal IP**" | They must be in the **same VPC**. Two separate VPCs can't talk privately without peering or VPN |
| "**without creating additional routes**" | Use the routes Google **creates automatically** inside one VPC |
| "**same CIDR range**" in B/D | 🚩 Two subnets in one VPC **can't overlap**. Google rejects it |

**Exam topic:** VPC networking.

> 🎯 **The one-sentence answer to "why A and not B?":** In one VPC, **every subnet needs its own, non-overlapping IP range**. B gives both subnets the **same** range, which Google Cloud **won't allow**, and even if it did, an IP like `10.0.1.5` would exist twice, so nobody would know which VM it means. The "different region" part of A isn't what makes it right. It's the **different CIDR range**.

---

## 📚 Key Terms Explained

### 1️⃣ VPC (review from Q002)
- **What it is:** Your **private network** in Google Cloud. A VPC is **global**: one VPC can have subnets in **many regions**, and VMs in all of them can talk privately.
- **Looks like:** `shopnow-vpc` (custom mode)
- **Not to be confused with:** a subnet. The VPC is the **whole network**. Subnets are **pieces** of it.
- **Analogy:** 🏢 The **company's internal phone system** covering every branch worldwide.
- **In the online store:** `shopnow-vpc` connects the web servers, API servers and databases.

### 2️⃣ Subnet (review from Q002)
- **What it is:** A **slice of the VPC's IP addresses** in **one region**. Every VM gets an internal IP from a subnet.
- **Looks like:** `prod-subnet  us-central1  10.0.1.0/24`, `test-subnet  us-east1  10.0.2.0/24`
- **Not to be confused with:** a separate network. Subnets in the **same VPC** can reach each other automatically.
- **Analogy:** 📞 A **block of phone extensions** for one department: Prod = 100–199, Test = 200–299.

### 3️⃣ CIDR Range (and why ranges can't overlap) 🔑
- **What it is:** The notation for a **block of IP addresses**. `10.0.1.0/24` = the 256 addresses `10.0.1.0`–`10.0.1.255`.
- **Looks like:**
  ```
  ✅ prod-subnet  10.0.1.0/24   (10.0.1.0 – 10.0.1.255)
  ✅ test-subnet  10.0.2.0/24   (10.0.2.0 – 10.0.2.255)   ← no overlap, both allowed
  ❌ test-subnet  10.0.1.0/24                              ← same range → error
  ```
- **Not to be confused with:** a label you can reuse. Inside one VPC, each IP address must point to **exactly one** place.
- **Analogy:** 📞 Two departments can't **both** use extensions 100–199. Dial 105, and which phone rings?
- **In the online store:** If prod and test both used `10.0.1.0/24`, a call to `10.0.1.5` couldn't know whether it means the prod database or the test database.

### 4️⃣ Automatic Subnet Routes ("without creating additional routes")
- **What it is:** When you create a subnet, Google **automatically adds a route** so **every VM in the same VPC** can reach it by internal IP, **in any region**.
- **Looks like:** `default-route-… destination 10.0.2.0/24 next hop: network shopnow-vpc` (created for you)
- **Not to be confused with:** connecting **different** VPCs. Those routes don't cross VPC borders, so you'd need **VPC Peering** or a **VPN**.
- **Analogy:** 📞 The phone system **automatically** knows every extension in the company.

### 5️⃣ Region (why "different region" is fine)
- **What it is:** A geographic area like `us-central1` (Iowa) or `us-east1` (South Carolina). A subnet lives in **one** region.
- **Not to be confused with:** a network border. Because the **VPC is global**, subnets in **different regions** of the same VPC still talk privately.
- 💡 Same region **would also be fine**, as long as the ranges were different. Different regions just aren't a problem.

### 🔗 How They Fit Together
```
✅ A: ONE VPC (global) — shopnow-vpc
   ├── prod-subnet  us-central1  10.0.1.0/24   🖥️ prod-api  10.0.1.5
   └── test-subnet  us-east1     10.0.2.0/24   🖥️ test-api  10.0.2.7
        ⇅ automatic subnet routes → 10.0.1.5 ↔ 10.0.2.7 works ✅

❌ B: ONE VPC, both subnets 10.0.1.0/24 → "overlaps with an existing subnet" error
❌ C: TWO VPCs → no path between them without peering/VPN (= extra setup)
❌ D: TWO VPCs + same range → no path, and can't even be peered (overlap)
```

---

## 🌍 Real-World Scenario

Teams often separate **prod and test** into different subnets so they can apply different **firewall rules** and keep things organized, while still allowing tests to call a shared service (for example, a test app reading from a staging copy of a database). A network engineer plans an **IP address map** first so that **no two subnets overlap**, because overlapping ranges cause errors now and block peering or VPN connections later.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a single custom VPC with 2 subnets. Create each subnet in a different region and with a different CIDR range.

**Why it's correct:**
- ✔️ **One VPC** → Google's automatic subnet routes let all VMs reach each other by internal IP. **No extra routes.**
- ✔️ **Different CIDR ranges** → every IP is unique, so Google allows it.
- ✔️ **Different regions** is fine because a VPC is **global**.

**📌 When to use it:** Use it when two groups of servers should be kept in separate sections but still talk privately.
🏢 **Office example:** One company phone system, with Prod on extensions 100–199 in one building and Test on 200–299 in another. Anyone can dial anyone.

### ❌ B (your answer)
> **B.** Create a single custom VPC with 2 subnets. Create each subnet in the same region and with the same CIDR range.

**Why it's wrong:**
- ✔️ One VPC is right…
- ❌ …but **two subnets in one VPC can't use the same (or overlapping) CIDR range**. Google rejects the second subnet with an "overlaps" error.
- ❌ Even in theory, `10.0.1.5` would exist **twice**, and the network couldn't know which VM you mean.
- 💡 **Likely mix-up:** "Same region, same range" *sounds* tidy and simple. But a range is like a **block of phone extensions**: two departments can't share the same numbers.

**📌 When to use it:** **Never use this.** Subnets in one network can't share IP ranges. Give each its own range (A).
🏢 **Office example:** Giving two departments the same extensions 100–199. Dial 105 and nobody knows whose phone should ring.

### ❌ C
> **C.** Create 2 custom VPCs, each with a single subnet. Create each subnet in a different region and with a different CIDR range.

**Why it's wrong:**
- ✔️ Different ranges are good…
- ❌ …but **two separate VPCs are isolated**. VMs can't reach each other by internal IP unless you add **VPC Peering** or a **VPN**, which is extra setup the question rules out.

**📌 When to use it:** Use separate VPCs when two environments must be fully cut off from each other.
🏢 **Office example:** Two companies with separate phone systems. Calling between them needs an outside line.

### ❌ D
> **D.** Create 2 custom VPCs, each with a single subnet. Create each subnet in the same region and with the same CIDR range.

**Why it's wrong:**
- ❌ **Two VPCs** → no private path between them.
- ❌ **Same range** → you couldn't even **peer** them later, because peering requires non-overlapping ranges.

**📌 When to use it:** Use it only for environments that must **never** connect, like isolated sandboxes copied from the same template.
🏢 **Office example:** Two separate branch offices that each use extensions 100–199 internally. Fine, as long as they never need to call each other's extensions.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow wants **prod** checkout servers and **test** servers separated, but the test checkout must call the **shared inventory service** on a prod VM by private IP.

```bash
gcloud compute networks create shopnow-vpc --subnet-mode=custom

gcloud compute networks subnets create prod-subnet \
  --network=shopnow-vpc --region=us-central1 --range=10.0.1.0/24

gcloud compute networks subnets create test-subnet \
  --network=shopnow-vpc --region=us-east1 --range=10.0.2.0/24
```

**What happens with option B instead:**
```bash
gcloud compute networks subnets create test-subnet \
  --network=shopnow-vpc --region=us-central1 --range=10.0.1.0/24
# ERROR: Invalid IPCidrRange: 10.0.1.0/24 conflicts with existing subnetwork 'prod-subnet'
```

| VM | Subnet | Internal IP | Can reach the other by internal IP? |
|---|---|---|---|
| `inventory-prod` | prod-subnet (us-central1) | 10.0.1.5 | ✅ |
| `checkout-test` | test-subnet (us-east1) | 10.0.2.7 | ✅ (automatic routes, firewall rule allowing it) |

*Note: routes make the path exist. A **firewall rule** still decides which traffic is allowed (for example, allow `10.0.2.0/24` → port 8080 on inventory).*

---

## 🧠 Key Takeaways / Memory Tips

- **"Different subnets" + "reach each other by internal IP" + "no extra routes" → ONE VPC, 2 subnets, DIFFERENT CIDR ranges.**
- 🧠 *"**One VPC, unique ranges.** Like phone extensions: two departments can't share the same numbers."*
- **Subnet ranges in one VPC must never overlap.** Any option with the "same CIDR range" in one VPC is wrong.
- **VPC = global, subnet = regional.** Different regions in one VPC still talk privately.
- **Two VPCs = isolated** unless you add peering or VPN.
- Related: **Q002** (VPC, subnets, CIDR basics).

---

## 🤔 Follow-up: "What if B said *same region* and a *different* CIDR range?"

> *"Create a single custom VPC with 2 subnets. Create each subnet in the same region and with a **different** CIDR range."*

**✅ That would also be correct.** It meets every requirement:

| Requirement | Same region + different CIDR |
|---|---|
| Prod and test in **different subnets** | ✅ 2 subnets |
| Reach each other by **internal IP** | ✅ same VPC |
| **No additional routes** | ✅ Google creates the subnet routes automatically |
| Allowed by Google Cloud? | ✅ the ranges don't overlap |

```
ONE VPC — shopnow-vpc
 ├── prod-subnet  us-central1  10.0.1.0/24   🖥️ 10.0.1.5
 └── test-subnet  us-central1  10.0.2.0/24   🖥️ 10.0.2.7
        ⇅ automatic routes ✅  (same region is fine)
```

**What this teaches:** The **region doesn't matter** for this question. Same region or different region, subnets in one VPC talk privately either way. The **only things that matter** are:
1. **One VPC** (not two), and
2. **Different, non-overlapping CIDR ranges.**

| Option wording | One VPC? | Different ranges? | Works? |
|---|---|---|---|
| Different region + different CIDR (**real A**) | ✅ | ✅ | ✅ |
| Same region + different CIDR (**your version**) | ✅ | ✅ | ✅ |
| Same region + same CIDR (**real B**) | ✅ | ❌ | ❌ error |
| Two VPCs (C, D) | ❌ | either | ❌ need peering/VPN |

**Same region is actually common in real life**: prod and test usually sit in the same region, close to their users and database.

**🏢 Office example:** One phone system, with Prod on extensions 100–199 and Test on 200–299. Whether both departments sit **in the same building** (same region) or **in different buildings** (different regions) doesn't matter. They can call each other because the extensions are different and it's the same phone system.

🧠 **Exam tip:** In VPC questions, **check the CIDR words first** ("same" = 🚩 in one VPC), then **count the VPCs** (two = isolated). The region is usually a distraction.

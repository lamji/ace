# Q082: Subnet Out of IP Addresses (Expand the Subnet's IP Range)

**Topic:** VPC networking (subnet mask, CIDR, expand-ip-range)

## ❓ Question
> Your VMs are running in a subnet that has a subnet mask of 255.255.255.240. The current subnet has no more free IP addresses and you require an additional 10 IP addresses for new VMs. The existing and new VMs should all be able to reach each other without additional routes. What should you do?
>
> **A.** Use gcloud to expand the IP range of the current subnet.
>
> **B.** Delete the subnet, and recreate it using a wider range of IP addresses.
>
> **C.** Create a new project. Use Shared VPC to share the current network with the new project.
>
> **D.** Create a new subnet with the same starting IP but a wider range to overwrite the current subnet.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your subnet is tiny (/28 = 16 addresses) and full. You need 10 more addresses, and the old and new VMs must stay on the same network. What's the simplest fix?

**Clues in the question:**
- "**subnet mask of 255.255.255.240**": that's a **/28**, only 16 addresses (Google keeps 4, so 12 usable).
- "**no more free IP addresses**" + "**additional 10 IP addresses**": the range must get **bigger**.
- "**without additional routes**": keep everyone in the **same subnet**, so no extra network setup is needed.
- Google Cloud lets you **expand** a subnet's range in place, with no downtime.

**Exam topic:** VPC networking.

---

## 📚 Key Terms Explained

### 1️⃣ Subnet mask / CIDR (review from Q002)
- **What it is:** A **number that says how big an IP range is**. `255.255.255.240` is the same as `/28` = 16 addresses. A smaller number after the slash = a bigger range: `/27` = 32, `/26` = 64.
- **Looks like:** `10.0.1.0/28` → 10.0.1.0 to 10.0.1.15
- **Not to be confused with:** the number of VMs. Google reserves **4 addresses** in every subnet, so a /28 has 12 usable.
- **Analogy:** 🏢 The **number of desks on one floor**.
- **In the online store:** The `checkout-subnet` holds the checkout VMs.

### 2️⃣ Expand IP range 🔑
- **What it is:** A gcloud command that **makes an existing subnet's range larger** (smaller prefix number) **without deleting it or stopping VMs**. You can only grow it, never shrink it.
- **Looks like:** `gcloud compute networks subnets expand-ip-range checkout-subnet --region=us-central1 --prefix-length=26`
- **Not to be confused with:** creating a new subnet. Same subnet, more room.
- **Analogy:** 🔨 **Knocking down a wall** to add more desks to the same floor, while people keep working.
- **In the online store:** `checkout-subnet` grows from /28 (16) to /26 (64) on Black Friday eve.

### 3️⃣ Routes
- **What it is:** Rules that tell traffic how to get from one range to another. VMs in the **same VPC** reach each other automatically through built-in subnet routes.
- **Not to be confused with:** firewall rules (which allow or block traffic).

### 4️⃣ Shared VPC (review from Q079)
- **What it is:** Sharing one project's VPC with other projects. It doesn't add IP addresses.

### 🔗 How they fit together
```
 Before: checkout-subnet 10.0.1.0/28  → 16 addresses, 12 usable, all used ❌
 gcloud compute networks subnets expand-ip-range ... --prefix-length=26
 After:  checkout-subnet 10.0.1.0/26  → 64 addresses, old VMs keep their IPs ✅
```

---

## 🌍 Real-World Scenario

A team picked a very small subnet at the start. Now the app is growing and new VMs fail to start with "no available IP addresses". The engineer runs **expand-ip-range** to grow the subnet. The existing VMs keep running with the same IPs, and new VMs get addresses from the larger range.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use gcloud to expand the IP range of the current subnet.

**Why it's correct:**
- ✔️ "**expand the IP range**" matches "**no more free IP addresses and you require an additional 10 IP addresses**": a bigger range gives room for the new VMs.
- ✔️ "**of the current subnet**" matches "**existing and new VMs should all be able to reach each other without additional routes**": everyone stays in the same subnet, so no new routes are needed.
- ✔️ "**Use gcloud**": `gcloud compute networks subnets expand-ip-range` does it in place, with no downtime.

📌 **When to use it:** Use it when a group has run out of space and you can make the same space bigger without moving anyone.
🏢 **Office example:** Knocking down a wall to add more desks on the same floor while everyone keeps working.

### ❌ B
> **B.** Delete the subnet, and recreate it using a wider range of IP addresses.

**Wrong words:**
- ❌ "**Delete the subnet**": you can't delete a subnet while VMs are using it. You'd have to delete or move all the VMs first, causing downtime.
- ✔️ "a wider range of IP addresses" is the right goal, but expanding does this without deleting anything.

📌 **When to use it:** Use it only when the subnet is empty or you need a completely different range, for example to fix an overlap.
🏢 **Office example:** Sending everyone home and tearing down the floor just to add a few desks.

### ❌ C
> **C.** Create a new project. Use Shared VPC to share the current network with the new project.

**Wrong words:**
- ❌ "**Create a new project**": a new project doesn't add IP addresses.
- ❌ "**Use Shared VPC to share the current network**": the new VMs would still use the same full subnet.

📌 **When to use it:** Use Shared VPC when several departments should use one central network.
🏢 **Office example:** Opening a new department that shares the same full floor. Still no free desks.

### ❌ D
> **D.** Create a new subnet with the same starting IP but a wider range to overwrite the current subnet.

**Wrong words:**
- ❌ "**Create a new subnet with the same starting IP**": subnet ranges in a VPC **can't overlap**, so Google rejects it.
- ❌ "**to overwrite the current subnet**": there's no "overwrite" for subnets.

📌 **When to use it:** **Never use this.** Expand the existing subnet (A).
🏢 **Office example:** Trying to build a second floor in exactly the same spot as the first.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `checkout-subnet` is `10.0.1.0/28`: 12 usable IPs, all taken by checkout VMs. Black Friday needs 10 more VMs.

```bash
gcloud compute networks subnets expand-ip-range checkout-subnet \
  --region=us-central1 --prefix-length=26
# 10.0.1.0/28 (16) → 10.0.1.0/26 (64)
```
Existing VMs keep `10.0.1.2`–`10.0.1.13`. New VMs get `10.0.1.14` and up, and everyone talks directly with no new routes.

---

## 🧠 Key Takeaways / Memory Tips

- **Subnet full → `gcloud compute networks subnets expand-ip-range`** (grow only, no downtime).
- **/28 = 16 addresses, 12 usable** (Google keeps 4).
- Subnets in one VPC can't overlap, and you can't delete a subnet that's in use.
  🧠 *"**Out of IPs? Expand, don't delete.**"*
- Related: **Q002** (CIDR), **Q054** (subnets are regional), **Q079** (Shared VPC).

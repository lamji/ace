# Q351: VM Without External IP Needs Internet for Updates (Cloud NAT)

**Topic:** Networking (Cloud NAT)

## ❓ Question
> You are creating a Compute Engine virtual machine (VM) instance for a new application. Your organization’s policy prohibits assigning external IP addresses to VM instances for security reasons. However, the application on the instance needs to access the internet to download necessary software updates and packages. What should you do?
>
> **A.** Set up a VPC Network Peering connection between your VPC network and a VPC network with internet access.
>
> **B.** Create a bastion host with an external IP address, and use it to connect to the VM using SSH.
>
> **C.** Assign an internal static IP address to the VM.
>
> **D.** Configure Cloud NAT for the subnet that the VM is in.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** No external IPs allowed, but the VM must **download updates from the internet**.

**Clues in the question:**
- Outbound internet without an external IP → **Cloud NAT**.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Cloud NAT 🔑 (review)
- **What it is:** Managed outbound NAT for private VMs; no inbound connections.
- **Looks like:** `gcloud compute routers nats create nat --router=r1 --region=us-central1 --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges`
- **Not to be confused with:** bastion host (for SSH in).
- **Analogy:** 📮 Mailroom sending letters out for staff without their own address.
- **In the online store:** —

### 🔗 How they fit together
```
 private VM → Cloud NAT → internet (apt/yum) ✅
```

---

## 🌍 Real-World Scenario

A private VM runs `apt-get update` through **Cloud NAT**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Set up a VPC Network Peering connection between your VPC network and a VPC network with internet access.

**Wrong words:**
- ❌ "**VPC Network Peering … with internet access**": peering doesn't route internet traffic through another VPC.

📌 **When to use it:** Use peering for private VPC-to-VPC traffic.
🏢 **Office example:** A hallway to the next building doesn't give you a street exit.

### ❌ B
> **B.** Create a bastion host with an external IP address, and use it to connect to the VM using SSH.

**Wrong words:**
- ❌ "**bastion host … SSH**": lets you log in; doesn't give the VM internet.

📌 **When to use it:** Use a bastion (or IAP) for admin access.
🏢 **Office example:** A reception desk for visitors, not a mailroom.

### ❌ C
> **C.** Assign an internal static IP address to the VM.

**Wrong words:**
- ❌ "**internal static IP**": internal only; no internet.

📌 **When to use it:** Use it for stable private addresses.
🏢 **Office example:** A fixed desk extension can't call outside.

### ✅ D
> **D.** Configure Cloud NAT for the subnet that the VM is in.

**Why it's correct:**
- ✔️ "**Configure Cloud NAT for the subnet**" matches "**prohibits assigning external IP addresses**" + "**needs to access the internet to download … updates**".

📌 **When to use it:** Use it when machines with no public address still need to fetch things from the internet.
🏢 **Office example:** A mailroom that sends out staff requests using the company's address.

---

## 🛒 E-Commerce Full-Stack Example

Cloud NAT `shopnow-nat` for subnet `app`.

---

## 🧠 Key Takeaways / Memory Tips

- **No external IP + outbound internet → Cloud NAT.**
  🧠 *"**Out only? Cloud NAT.**"*
- Related: **Q314**, **Q158**.

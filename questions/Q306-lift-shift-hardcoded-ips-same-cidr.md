# Q306: Lift and Shift Apps With Hard-Coded Internal IPs, Not Connected to On-Prem (Same CIDR Ranges, Same Static IPs)

**Topic:** Networking (VPC design for migration)

## ❓ Question
> Your company is migrating its workloads to Google Cloud due to an expiring data center contract. The on-premises environment and Google Cloud are not connected. You have decided to follow a lift-and-shift approach, and you plan to modernize the workloads in a future project. Several old applications connect to each other through hard-coded internal IP addresses. You want to migrate these workloads quickly without modifying the application code. You also want to maintain all functionality. What should you do?
>
> **A.** Migrate your DNS server first. Configure Cloud DNS with a forwarding zone to your migrated DNS server. Then migrate all other workloads with ephemeral internal IP addresses.
>
> **B.** Create a VPC with non-overlapping CIDR ranges compared to your on-premises network. When migrating individual workloads, assign each workload a new static internal IP address.
>
> **C.** Create a VPC with the same CIDR ranges as your on-premises network. When migrating individual workloads, assign each workload the same static internal IP address.
>
> **D.** Migrate all workloads to a single VPC subnet. Configure Cloud NAT for the subnet and manually assign a static IP address to the Cloud NAT gateway.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Apps talk via **hard-coded internal IPs**; migrate fast, no code change. Networks are **not connected**.

**Clues in the question:**
- "**hard-coded internal IP addresses**" + "**without modifying the application code**" → keep the **same IPs**.
- "**not connected**" → overlapping ranges are OK (no routing conflict).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Static internal IP 🔑
- **What it is:** A reserved private address that stays with a VM.
- **Looks like:** `gcloud compute addresses create app1 --region=us-central1 --subnet=legacy --addresses=10.20.0.15`
- **Not to be confused with:** ephemeral IP (changes).
- **Analogy:** 📞 Keeping the same extension number when you move offices.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem 10.20.0.0/16 ──(not connected)── VPC 10.20.0.0/16
 app1 10.20.0.15 → same 10.20.0.15 ✅
```

---

## 🌍 Real-World Scenario

A data center is closing. The team builds a VPC with the **same ranges** and reserves the **same internal IPs** for each app.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Migrate your DNS server first. Configure Cloud DNS with a forwarding zone to your migrated DNS server. Then migrate all other workloads with ephemeral internal IP addresses.

**Wrong words:**
- ❌ "**ephemeral internal IP addresses**": IPs change, breaking hard-coded connections; DNS doesn't help apps that use raw IPs.

📌 **When to use it:** Use DNS-based moves when apps use hostnames.
🏢 **Office example:** Giving everyone new extensions when the phone book isn't used.

### ❌ B
> **B.** Create a VPC with non-overlapping CIDR ranges compared to your on-premises network. When migrating individual workloads, assign each workload a new static internal IP address.

**Wrong words:**
- ❌ "**new static internal IP address**": apps still point at the old IPs; code must change.

📌 **When to use it:** Use non-overlapping ranges when networks will be connected.
🏢 **Office example:** New extension numbers that nobody's speed dial knows.

### ✅ C
> **C.** Create a VPC with the same CIDR ranges as your on-premises network. When migrating individual workloads, assign each workload the same static internal IP address.

**Why it's correct:**
- ✔️ "**same CIDR ranges as your on-premises network**" matches "**hard-coded internal IP addresses**" (possible because the networks are "**not connected**").
- ✔️ "**same static internal IP address**" matches "**without modifying the application code**" + "**maintain all functionality**".

📌 **When to use it:** Use it when programs call each other by fixed numbers and you're moving them to a new place that won't be linked to the old one.
🏢 **Office example:** Moving to a new building and keeping every desk's phone extension.

### ❌ D
> **D.** Migrate all workloads to a single VPC subnet. Configure Cloud NAT for the subnet and manually assign a static IP address to the Cloud NAT gateway.

**Wrong words:**
- ❌ "**Cloud NAT**": for outbound internet access; doesn't preserve internal IPs.

📌 **When to use it:** Use Cloud NAT for private VMs reaching the internet.
🏢 **Office example:** A front-desk phone line, unrelated to desk extensions.

---

## 🛒 E-Commerce Full-Stack Example

Legacy inventory/billing VMs keep `10.20.0.15` and `10.20.0.16` in VPC `legacy-lift`.

---

## 🧠 Key Takeaways / Memory Tips

- **Hard-coded IPs + not connected → same CIDR, same static IPs.**
  🧠 *"**Same numbers, new building.**"*
- Related: **Q334**.

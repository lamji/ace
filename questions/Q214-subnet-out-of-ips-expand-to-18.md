# Q214: Subnet 10.0.0.0/20 Running Out of VM IPs (Expand It to 10.0.0.0/18)

**Topic:** Networking (expanding subnet ranges)

## ❓ Question
> You are running out of primary internal IP addresses in a subnet for a custom mode VPC. The subnet has the IP range 10.0.0.0/20, and the IP addresses are primarily used by virtual machines in the project. You need to provide more IP addresses for the virtual machines. What should you do?
>
> **A.** Add a secondary IP range 10.1.0.0/20 to the subnet.
>
> **B.** Change the subnet IP range from 10.0.0.0/20 to 10.0.0.0/18.
>
> **C.** Change the subnet IP range from 10.0.0.0/20 to 10.0.0.0/22.
>
> **D.** Convert the subnet IP range from IPv4 to IPv6.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A subnet in a custom VPC uses 10.0.0.0/20, and its primary internal IPs are almost used up by VMs.
- **What you must achieve:** Give the VMs more IP addresses.
- **The limits:** None stated.
- **What they're really asking:** How do you get more addresses for the VMs?

**Clues in the question:**
- "**running out of primary internal IP addresses**" → **expand** the primary range.
- A **smaller prefix number = bigger range**: /18 (16,384 IPs) > /20 (4,096) > /22 (1,024).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. CIDR prefix 🔑
- **What it is:** The number after `/` says how many bits are fixed. **Lower number = more addresses.**
- **Looks like:** /20 = 4,096 · /18 = 16,384 · /22 = 1,024
- **Not to be confused with:** —
- **Analogy:** 📞 Fewer fixed digits in a phone number = more possible numbers.
- **In the online store:** shop subnet.

### 2. Secondary IP range
- **What it is:** Extra ranges on a subnet used for **alias IPs** (like GKE pods/services), not VM primary IPs.
- **Looks like:** `--secondary-range pods=10.4.0.0/14`
- **Not to be confused with:** primary range.
- **Analogy:** 📞 A separate extension block for one department.
- **In the online store:** GKE pods.

### 🔗 How they fit together
```
 10.0.0.0/20 (4,096) ─expand─► 10.0.0.0/18 (16,384) ✅ (existing VMs keep their IPs)
```

---

## 🌍 Real-World Scenario

A subnet fills up with VMs. The admin runs `expand-ip-range --prefix-length=18`. Existing VMs are untouched and new VMs get addresses from the bigger range.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add a secondary IP range 10.1.0.0/20 to the subnet.

**Wrong words:**
- ❌ "**secondary IP range**": secondary ranges are for alias IPs (like GKE pods), not VMs' **primary** addresses.

📌 **When to use it:** Use secondary ranges for GKE pods and services.
🏢 **Office example:** Adding extension numbers that only one department can use.

### ✅ B
> **B.** Change the subnet IP range from 10.0.0.0/20 to 10.0.0.0/18.

**Why it's correct:**
- ✔️ "**Change the subnet IP range from 10.0.0.0/20 to 10.0.0.0/18**" matches "**provide more IP addresses for the virtual machines**": /18 is four times larger.
- ✔️ It expands the **primary** range in place, which matches "**running out of primary internal IP addresses**".

📌 **When to use it:** Use it when a group runs out of numbers and needs a bigger block without renumbering anyone.
🏢 **Office example:** Expanding the phone system from 4,000 to 16,000 extensions while everyone keeps their number.

### ❌ C
> **C.** Change the subnet IP range from 10.0.0.0/20 to 10.0.0.0/22.

**Wrong words:**
- ❌ "**to 10.0.0.0/22**": /22 is **smaller**, and subnets can't shrink.

📌 **When to use it:** **Never use this** — it makes the range smaller.
🏢 **Office example:** Cutting the number of phone lines when you're short of them.

### ❌ D
> **D.** Convert the subnet IP range from IPv4 to IPv6.

**Wrong words:**
- ❌ "**Convert … from IPv4 to IPv6**": you can't convert a range type, and VMs still need IPv4.

📌 **When to use it:** Use dual-stack subnets to add IPv6.
🏢 **Office example:** Changing the whole phone system format to fix a shortage.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute networks subnets expand-ip-range backend --region=us-central1 --prefix-length=18`

---

## 🧠 Key Takeaways / Memory Tips

- **More VM IPs → expand the primary range to a smaller prefix (/20 → /18).** Can't shrink.
  🧠 *"**Smaller slash number, bigger subnet.**"*
- Related: **Q149**, **Q086**.

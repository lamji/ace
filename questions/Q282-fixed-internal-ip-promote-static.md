# Q282: Give a VM a Fixed Address for Services in the Same VPC, Cheaply (Promote Its IP to a Static Internal IP)

**Topic:** Networking (static internal IPs)

## ❓ Question
> You have a VM instance running in a VPC with single-stack subnets. You need to ensure that the VM instance has a fixed IP address so that other services hosted in the same VPC can communicate with the VM. You want to follow Google-recommended practices while minimizing cost. What should you do?
>
> **A.** Promote the existing IP address of the VM to become a static external IP address.
>
> **B.** Promote the existing IP address of the VM to become a static internal IP address.
>
> **C.** Reserve a new static external IPv6 address and assign the new IP address to the VM.
>
> **D.** Reserve a new static external IP address and assign the new IP address to the VM.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Services **in the same VPC** need a **fixed** address for this VM. Cheapest way?

**Clues in the question:**
- "**other services hosted in the same VPC**" → **internal** IP is enough.
- "**fixed**" → **static**; "**promote the existing**" keeps the current address (no reconfiguration).
- Static internal IPs are free; external IPs cost money.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Static internal IP 🔑
- **What it is:** A reserved private IP that doesn't change when the VM restarts.
- **Looks like:** `gcloud compute addresses create db-ip --region=us-central1 --subnet=backend --addresses=10.0.1.15`
- **Not to be confused with:** external IP.
- **Analogy:** 📞 A permanent internal extension.
- **In the online store:** Orders DB VM.

### 2. Single-stack subnet
- **What it is:** A subnet with IPv4 only (no IPv6).
- **Looks like:** —
- **Not to be confused with:** dual-stack.
- **Analogy:** —
- **In the online store:** —

### 🔗 How they fit together
```
 VM 10.0.1.15 (ephemeral) ─ promote ─► 10.0.1.15 (static internal) ✅ ← other VPC services
```

---

## 🌍 Real-World Scenario

An app server in a VPC must always be at the same address. The admin **promotes its ephemeral internal IP to static**, at no cost.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Promote the existing IP address of the VM to become a static external IP address.

**Wrong words:**
- ❌ "**static external IP address**": exposes the VM publicly and costs money; same-VPC services don't need it.

📌 **When to use it:** Use static external IPs for public endpoints.
🏢 **Office example:** Buying a public phone line for internal calls.

### ✅ B
> **B.** Promote the existing IP address of the VM to become a static internal IP address.

**Why it's correct:**
- ✔️ "**static internal IP address**" matches "**other services hosted in the same VPC**" + "**minimizing cost**".
- ✔️ "**Promote the existing IP address**" matches "**fixed IP address**": the current address stays, nothing else changes.

📌 **When to use it:** Use it when coworkers on the same network need a number that never changes.
🏢 **Office example:** Making someone's internal extension permanent.

### ❌ C
> **C.** Reserve a new static external IPv6 address and assign the new IP address to the VM.

**Wrong words:**
- ❌ "**external IPv6**": the subnet is single-stack (IPv4), and external isn't needed.

📌 **When to use it:** Use IPv6 on dual-stack subnets.
🏢 **Office example:** An international number for an internal call.

### ❌ D
> **D.** Reserve a new static external IP address and assign the new IP address to the VM.

**Wrong words:**
- ❌ "**new static external IP**": public, costly, and a new address to reconfigure.

📌 **When to use it:** Use it for public-facing services.
🏢 **Office example:** A new public line nobody inside needs.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute addresses create orders-db-ip --region=us-central1 --subnet=backend --addresses=10.0.1.15`

---

## 🧠 Key Takeaways / Memory Tips

- **Fixed address for same-VPC traffic → static internal IP (promote the current one).**
  🧠 *"**Internal callers, internal static.**"*
- Related: **Q214**, **Q142**.

# Q339: Internal Domain Resolvable From VPC and On-Prem, Not Public (Cloud DNS Private Zone)

**Topic:** Networking (Cloud DNS private zones)

## ❓ Question
> You are deploying a new internal web application behind an internal Application Load Balancer. The application must be accessible from both the VPC network and on-premises network using the domain name internal.altostrat.com. This name must not be resolvable from the public internet. Your on-premises network is connected to the VPC network by using Cloud VPN, and you have configured an inbound server policy. You need to resolve the domain name with the least administrative overhead. What should you do?
>
> **A.** Create an A record on the on-premises DNS server that points to the load balancer’s IP address.
>
> **B.** Create a Cloud DNS managed private zone, authorize the VPC network to use it, and add an A record that points to the load balancer’s IP address.
>
> **C.** Create a Cloud DNS managed public zone, and add an A record that points to the load balancer’s IP address.
>
> **D.** On each employee’s workstation, edit the local HOSTS file to map the domain name to the load balancer’s IP address.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Resolve `internal.altostrat.com` from **VPC and on-prem**, **not public**, least overhead.

**Clues in the question:**
- "**must not be resolvable from the public internet**" → **private zone**.
- "**inbound server policy**" already set → on-prem DNS can forward to Cloud DNS, so one record serves both.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Cloud DNS private zone 🔑
- **What it is:** DNS records visible only to authorized VPC networks (and to on-prem via inbound forwarding).
- **Looks like:** `gcloud dns managed-zones create int --dns-name=altostrat.com. --visibility=private --networks=prod-vpc` + A record `internal → 10.0.5.10`
- **Not to be confused with:** public zone.
- **Analogy:** 📒 An internal phone directory.
- **In the online store:** ShopNow `admin.internal.shopnow.com`.

### 2. Inbound server policy
- **What it is:** Gives on-prem DNS servers an IP in the VPC to forward queries to Cloud DNS.
- **Looks like:** `gcloud dns policies create inbound --networks=prod-vpc --enable-inbound-forwarding`
- **Not to be confused with:** —
- **Analogy:** 📞 A hotline into the internal directory.
- **In the online store:** —

### 🔗 How they fit together
```
 on-prem DNS ─forward─► inbound policy IP ─► private zone (A record) ✅
 VPC VMs ─────────────────────────────────► private zone ✅
```

---

## 🌍 Real-World Scenario

The team adds an **A record in a private zone**; VPC VMs resolve directly and on-prem resolves via the inbound policy.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an A record on the on-premises DNS server that points to the load balancer’s IP address.

**Wrong words:**
- ❌ "**A record on the on-premises DNS server**": works only on-prem; VPC needs another record. Two places to manage.

📌 **When to use it:** Use it if only on-prem needs the name.
🏢 **Office example:** Writing the number only in the branch directory.

### ✅ B
> **B.** Create a Cloud DNS managed private zone, authorize the VPC network to use it, and add an A record that points to the load balancer’s IP address.

**Why it's correct:**
- ✔️ "**Cloud DNS managed private zone**" matches "**must not be resolvable from the public internet**".
- ✔️ "**authorize the VPC network … A record**" matches "**accessible from both the VPC network and on-premises**" (via the inbound policy) + "**least administrative overhead**".

📌 **When to use it:** Use it when a name should work only inside the company network, from both cloud and office.
🏢 **Office example:** An internal phone directory reachable from HQ and branches, but not the public phone book.

### ❌ C
> **C.** Create a Cloud DNS managed public zone, and add an A record that points to the load balancer’s IP address.

**Wrong words:**
- ❌ "**public zone**": anyone on the internet can resolve it.

📌 **When to use it:** Use public zones for public websites.
🏢 **Office example:** Listing an internal number in the public phone book.

### ❌ D
> **D.** On each employee’s workstation, edit the local HOSTS file to map the domain name to the load balancer’s IP address.

**Wrong words:**
- ❌ "**edit the local HOSTS file**" on each workstation: manual, doesn't scale.

📌 **When to use it:** **Never use this** at scale.
🏢 **Office example:** Writing the number on every employee's hand.

---

## 🛒 E-Commerce Full-Stack Example

Private zone `internal.shopnow.com.` with `admin` → ILB `10.10.5.10`.

---

## 🧠 Key Takeaways / Memory Tips

- **Internal-only name for VPC + on-prem → Cloud DNS private zone (+ inbound policy).**
  🧠 *"**Private name, private zone.**"*
- Related: **Q264**.

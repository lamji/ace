# G030: Detect and Block Known Exploit Traffic Between VMs (Cloud NGFW Enterprise Intrusion Prevention)

**Topic:** VPC firewall (Cloud NGFW Enterprise IPS)
**Exam guide section:** 2.3 Networking: Creating and applying Cloud NGFW policies; 3.3 Managing Cloud NGFW policies

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your security team must detect and block known exploit and malware traffic, such as attempts to exploit a vulnerable web framework, in traffic reaching your web VMs. Allow and deny rules based only on IP addresses and ports are not enough. You want a Google Cloud managed solution. What should you do?
>
> **A.** Create more VPC firewall rules that deny traffic from IP ranges seen in past attacks.
>
> **B.** Use Cloud NGFW Enterprise: create a firewall endpoint and a security profile for threat prevention, associate the endpoint with the VPC, and add a firewall policy rule that applies the security profile group to traffic to the web VMs.
>
> **C.** Enable VPC Flow Logs and review them once a week.
>
> **D.** Move the web VMs to a different region.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Attackers send traffic that tries to exploit known software weaknesses in your web servers.
- **What you must achieve:** Spot and block that malicious traffic automatically.
- **The limits:** Rules that only look at IP addresses and ports can't see the attack inside the traffic. You want a Google-managed service.
- **What they're really asking:** Which Google Cloud firewall option inspects traffic contents to stop known attacks (intrusion prevention)?

**Clues in the question:**
- "**detect and block known exploit and malware traffic**": **intrusion prevention (IPS)**.
- "**rules based only on IP addresses and ports are not enough**": you need deep inspection. That's **Cloud NGFW Enterprise** (firewall endpoint + security profile).

**Exam topic:** Network security (exam guide sections 2.3 and 3.3).

---

## 📚 Key Terms Explained

### 1. Intrusion prevention service (IPS)
- **What it is:** Inspects the contents of network traffic and matches it against threat signatures (known exploits, malware) to alert on or block it.
- **Looks like:** Signature hit: "Apache Struts RCE attempt" → action: deny
- **Not to be confused with:** A normal firewall rule, which only looks at addresses and ports.
- **Analogy:** 🧳 Airport security X-raying bags, not just checking tickets.
- **In the online store:** Blocks exploit attempts on storefront VMs.

### 2. Cloud NGFW Enterprise 🔑
- **What it is:** The Cloud NGFW tier that adds Google-managed intrusion prevention. You create a zonal **firewall endpoint**, associate it with your VPC, define a **security profile** (threat prevention) inside a **security profile group**, and use a firewall policy rule with the action "apply security profile group".
- **Looks like:** Rule 200: ingress tcp:443 to tag `web` → action `apply_security_profile_group: sp-threats`
- **Not to be confused with:** Cloud Armor, which protects external HTTP(S) load balancers at the edge. NGFW Enterprise inspects traffic to VMs inside the VPC.
- **Analogy:** 🛂 A customs inspection lane every arriving package passes through.
- **In the online store:** Inspects traffic to the storefront VMs.

### 🔗 How they fit together
```
 Traffic ─► VPC ─► firewall policy rule (apply security profile group)
                    └─► firewall endpoint (IPS signatures) ─✋ exploit blocked / ✅ clean traffic → web VMs
```

---

## 🌍 Real-World Scenario

A new exploit for a popular web framework appears. A retailer using **Cloud NGFW Enterprise** has Google-managed signatures updated automatically. Exploit attempts against its web VMs are blocked and logged before engineers even finish reading the security bulletin.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create more VPC firewall rules that deny traffic from IP ranges seen in past attacks.

**Wrong words:**
- ❌ "**deny traffic from IP ranges seen in past attacks**": attackers change IPs, and IP rules can't see exploit contents.

📌 **When to use it:** Use IP deny lists for a few known bad sources as an extra layer.
🏢 **Office example:** Banning yesterday's shoplifters' cars while new ones walk in.

### ✅ B
> **B.** Use Cloud NGFW Enterprise: create a firewall endpoint and a security profile for threat prevention, associate the endpoint with the VPC, and add a firewall policy rule that applies the security profile group to traffic to the web VMs.

**Why it's correct:**
- ✔️ "**Cloud NGFW Enterprise**" matches "**Google Cloud managed solution**" and "**detect and block known exploit and malware traffic**".
- ✔️ "**firewall endpoint and a security profile for threat prevention**" provides the deep inspection that "**IP addresses and ports are not enough**" calls for.
- ✔️ "**firewall policy rule that applies the security profile group to traffic to the web VMs**" aims it at exactly the web VMs.

📌 **When to use it:** Use it when you need the firewall to look inside traffic and stop known attacks automatically.
🏢 **Office example:** An X-ray machine at the entrance that stops dangerous bags, run by a professional security company.

### ❌ C
> **C.** Enable VPC Flow Logs and review them once a week.

**Wrong words:**
- ❌ "**review them once a week**": flow logs show connections, not exploit contents, and they don't block anything.

📌 **When to use it:** Use flow logs for traffic analysis and forensics.
🏢 **Office example:** Reading last week's visitor log instead of screening bags.

### ❌ D
> **D.** Move the web VMs to a different region.

**Wrong words:**
- ❌ "**different region**": attacks reach any region. Moving fixes nothing.

📌 **When to use it:** Use other regions for latency or data-residency needs.
🏢 **Office example:** Moving the shop across town to avoid shoplifters.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: firewall endpoint in `us-central1-a`, associated with `shop-vpc`; security profile `sp-threats` (block high/critical); rule: ingress tcp:443 → tag `web` → apply `spg-web`. Cloud Armor still guards the external load balancer.

---

## 🧠 Key Takeaways / Memory Tips

- **Inspect traffic contents to stop known exploits/malware → Cloud NGFW Enterprise (IPS via firewall endpoint + security profile).**
  🧠 *"**Enterprise = X-ray the packets.**"*
- Related: **G002**, **G029**.

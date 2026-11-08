# Q334: Isolated 3-Tier App With 1,000+ IPs, Minimal Complexity (One /16 Custom VPC, Three Subnets, Subnet-Based Firewall Rules)

**Topic:** Networking (VPC design, firewall rules)

## ❓ Question
> You are deploying a large, multi-tiered application with more than 1,000 IP addresses in a Google Cloud project that needs to be securely isolated. The application includes the: 1. web tier with frontend servers for public traffic, 2. application tier with servers running core application logic that only need access from the web tier, and 3. database tier with database servers that only need access from the application tier. You want to minimize cost, complexity, and administrative overhead in the network architecture. What should you do?
>
> **A.** Create a /24 Shared VPC with separate subnets for each tier. Use firewall rules that reference network tags to control traffic.
>
> **B.** Create one custom mode /16 VPC with three subnets. Place each tier in its own subnet and use firewall rules that reference IP subnets to control traffic.
>
> **C.** Deploy each tier into a separate custom mode /16 VPC. Use VPC Network Peering to securely connect each custom mode VPC. Manage firewall rules individually in each VPC.
>
> **D.** Deploy each tier in a /24 VPC by using network tags to identify instances. Implement firewall rules for fine-grained network segmentation.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are deploying a large three-tier app (web, app and database tiers) with more than 1,000 IP addresses, and it must be securely isolated. Web takes public traffic, the app tier only accepts the web tier, and the database only accepts the app tier.
- **What you must achieve:** Design the network.
- **The limits:** Minimize cost, complexity and admin work.
- **What they're really asking:** How should you lay out the network and firewall rules?

**Clues in the question:**
- "**more than 1,000 IP addresses**" → /24 (256) is too small → **/16**.
- "**minimize cost, complexity**" → **one VPC** with a subnet per tier and firewall rules by subnet ranges.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Firewall rules by source subnet 🔑
- **What it is:** Allow traffic to the app tier only from the web subnet's range, etc.
- **Looks like:** `--source-ranges=10.10.1.0/24 --target-tags=app --allow=tcp:8080`
- **Not to be confused with:** peering many VPCs.
- **Analogy:** 🚪 Doors that only open for one department's floor.
- **In the online store:** —

### 🔗 How they fit together
```
 VPC 10.10.0.0/16
  ├ web 10.10.1.0/24 ─► app 10.10.2.0/24 ─► db 10.10.3.0/24 ✅
```

---

## 🌍 Real-World Scenario

A team builds one **/16 custom VPC** with three subnets and firewall rules: web→app, app→db only.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a /24 Shared VPC with separate subnets for each tier. Use firewall rules that reference network tags to control traffic.

**Wrong words:**
- ❌ "**/24 Shared VPC**": only 256 addresses; Shared VPC adds org complexity for one project.

📌 **When to use it:** Use Shared VPC to share a network across projects.
🏢 **Office example:** A tiny shared office for a big team.

### ✅ B
> **B.** Create one custom mode /16 VPC with three subnets. Place each tier in its own subnet and use firewall rules that reference IP subnets to control traffic.

**Why it's correct:**
- ✔️ "**one custom mode /16 VPC**" matches "**more than 1,000 IP addresses**" + "**minimize … complexity**".
- ✔️ "**three subnets … firewall rules that reference IP subnets**" matches "**only need access from the web tier**" / "**only … from the application tier**".

📌 **When to use it:** Use it when one app has layers that should only talk to the next layer, all in one simple network.
🏢 **Office example:** One building with three floors, and each floor's door only opens for the floor above.

### ❌ C
> **C.** Deploy each tier into a separate custom mode /16 VPC. Use VPC Network Peering to securely connect each custom mode VPC. Manage firewall rules individually in each VPC.

**Wrong words:**
- ❌ "**separate … VPC … Peering … individually in each VPC**": three networks to manage; complex.

📌 **When to use it:** Use separate VPCs for strong team separation.
🏢 **Office example:** Three buildings joined by hallways.

### ❌ D
> **D.** Deploy each tier in a /24 VPC by using network tags to identify instances. Implement firewall rules for fine-grained network segmentation.

**Wrong words:**
- ❌ "**/24 VPC**" per tier: small and multiple VPCs; more overhead.

📌 **When to use it:** **Avoid** here.
🏢 **Office example:** Three tiny buildings.

---

## 🛒 E-Commerce Full-Stack Example

VPC `shopnow-app` 10.10.0.0/16: web/app/db subnets; rules web→app:8080, app→db:5432.

---

## 🧠 Key Takeaways / Memory Tips

- **Simple tier isolation → one VPC, subnet per tier, firewall rules by range.**
  🧠 *"**One VPC, three floors.**"*
- Related: **Q306**, **Q215**.

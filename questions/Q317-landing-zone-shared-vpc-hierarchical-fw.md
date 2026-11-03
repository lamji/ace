# Q317: Landing Zone: Private Communication for Prod VMs, Org-Wide Allowed TCP Ports (Shared VPC + Hierarchical Firewall Policies)

**Topic:** Networking (Shared VPC, hierarchical firewall policies)

## ❓ Question
> You are planning to migrate your on-premises VMs to Google Cloud. You need to set up a landing zone in Google Cloud before migrating the VMs. You must ensure that all VM in your production environment can communicate with each other through private IP addresses. You need to allow all VMs in your Google Cloud organization to accept connections on specific TCP ports. You want to follow Google-recommended practices, and you need to minimize your operational costs. What should you do?
>
> **A.** Create individual VPCs per Google Cloud project. Peer all he VPC together. Apply organization policies on the organization level.
>
> **B.** Create individual VPCs for each Google Cloud project. Peer ail ne VPCs together. Apply hierarchical firewall policies on the organization level.
>
> **C.** Create a host VPC project with each production project as its service project. Apply organization policies on the organization level.
>
> **D.** Create a host VPC project with each production project as its service project. Apply hierarchical firewall policies on the organization level.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Prod VMs talk privately; **all VMs in the org** accept certain TCP ports; low ops.

**Clues in the question:**
- Many projects, private IPs, least ops → **Shared VPC** (host + service projects), not many peerings.
- "**all VMs in your Google Cloud organization … specific TCP ports**" → **hierarchical firewall policy** at the org. (Org policies don't control ports.)

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Hierarchical firewall policy 🔑
- **What it is:** Firewall rules attached to the org or a folder; apply to every VPC beneath.
- **Looks like:** `gcloud compute firewall-policies rules create 100 --firewall-policy=org-fw --action=allow --layer4-configs=tcp:22,tcp:443 --direction=INGRESS`
- **Not to be confused with:** organization policy (restricts services/settings, not ports).
- **Analogy:** 🏢 Company-wide building rules posted at HQ.
- **In the online store:** Allow health-check ports org-wide.

### 2. Shared VPC (review)
- **What it is:** One host project's VPC used by many service projects.
- **Looks like:** —
- **Not to be confused with:** peering.
- **Analogy:** 🏢 One shared network.
- **In the online store:** —

### 🔗 How they fit together
```
 Org ── hierarchical FW (allow tcp:443) ──► all VPCs ✅
 host project VPC ← service projects (prod) ✅
```

---

## 🌍 Real-World Scenario

The landing zone uses a **Shared VPC** for prod and an org **hierarchical firewall policy** allowing specific TCP ports.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create individual VPCs per Google Cloud project. Peer all he VPC together. Apply organization policies on the organization level.

**Wrong words:**
- ❌ "**Peer all the VPC together**": many peerings, non-transitive, heavy to manage.
- ❌ "**organization policies**": can't open TCP ports.

📌 **When to use it:** Use peering to join a few independent VPCs.
🏢 **Office example:** Phone lines between every pair of offices.

### ❌ B
> **B.** Create individual VPCs for each Google Cloud project. Peer ail ne VPCs together. Apply hierarchical firewall policies on the organization level.

**Wrong words:**
- ✔️ Hierarchical firewall is right.
- ❌ "**Peer all the VPCs together**": operationally heavy.

📌 **When to use it:** Use it when projects must keep separate networks.
🏢 **Office example:** Good company rules, messy wiring.

### ❌ C
> **C.** Create a host VPC project with each production project as its service project. Apply organization policies on the organization level.

**Wrong words:**
- ✔️ Shared VPC is right.
- ❌ "**organization policies**": not firewall rules.

📌 **When to use it:** Use org policies for guardrails like allowed regions.
🏢 **Office example:** Right building, wrong kind of rule.

### ✅ D
> **D.** Create a host VPC project with each production project as its service project. Apply hierarchical firewall policies on the organization level.

**Why it's correct:**
- ✔️ "**host VPC project with each production project as its service project**" matches "**communicate with each other through private IP addresses**" + "**minimize your operational costs**".
- ✔️ "**hierarchical firewall policies on the organization level**" matches "**all VMs in your Google Cloud organization to accept connections on specific TCP ports**".

📌 **When to use it:** Use it when many teams should share one private network and one set of company-wide door rules.
🏢 **Office example:** One shared office network, plus a rule posted at HQ that every branch follows.

---

## 🛒 E-Commerce Full-Stack Example

Host `shopnow-net-host`; service projects `shopnow-prod-*`; org FW policy allows tcp:443 and health-check ranges.

---

## 🧠 Key Takeaways / Memory Tips

- **Many projects, private comms → Shared VPC. Org-wide port rules → hierarchical firewall policy.**
  🧠 *"**Share the network, set rules at the top.**"*
- Related: **Q156**, **Q275**.

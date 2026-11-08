# Q151: Fewest Open Egress Ports (Low-Priority Deny-All + High-Priority Allow)

**Topic:** VPC firewall (rule priority, egress rules, implied rules)

## ❓ Question
> You are working with a user to set up an application in a new VPC behind a firewall. The user is concerned about data egress. You want to configure the fewest open egress ports. What should you do?
>
> **A.** Set up a low-priority (65534) rule that blocks all egress and a high-priority rule (1000) that allows only the appropriate ports.
>
> **B.** Set up a high-priority (1000) rule that pairs both ingress and egress ports.
>
> **C.** Set up a high-priority (1000) rule that blocks all egress and a low-priority (65534) rule that allows only the appropriate ports.
>
> **D.** Set up a high-priority (1000) rule to allow the appropriate ports.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are helping a user set up an app in a new VPC network behind a firewall. The user is worried about data egress (data leaving the network).
- **What you must achieve:** Set up the firewall for outgoing traffic.
- **The limits:** Open as few outgoing ports as possible.
- **What they're really asking:** How should you configure the firewall so only the outgoing ports the app needs are open?

**Clues in the question:**
- "**fewest open egress ports**": you must **block all egress** (the default implied rule allows it) and then **allow only the needed ports**.
- Firewall priority: **lower number = higher priority**, and it wins. The allow rule needs a **higher priority (1000)** than the deny-all (**65534**).

**Exam topic:** VPC firewall.

---

## 📚 Key Terms Explained

### 1. Firewall rule priority 🔑
- **What it is:** A number from 0 to 65535. **Lower number = evaluated first and wins.** The implied allow-egress rule has the lowest priority (65535).
- **Looks like:** allow tcp:443 egress priority 1000; deny all egress priority 65534
- **Not to be confused with:** bigger = stronger.
- **Analogy:** 🥇 The **rank** of a rule: #1000 beats #65534.
- **In the online store:** Allow 443 out, deny everything else.

### 2. Implied rules
- **What it is:** Every VPC has hidden rules: **allow all egress** and **deny all ingress**, both at priority 65535.
- **Looks like:** (not visible, always there)
- **Not to be confused with:** rules you create.
- **Analogy:** 🚪 The building's default: anyone can leave, nobody can enter.
- **In the online store:** Why egress is open by default.

### 🔗 How they fit together
```
 priority 1000  ALLOW egress tcp:443  ✅ checked first
 priority 65534 DENY  egress all      ✅ catches everything else
 priority 65535 (implied) allow egress — never reached
```

---

## 🌍 Real-World Scenario

A security-conscious customer wants the app to send data out **only** to HTTPS APIs. The engineer adds a **deny-all egress** rule at 65534 and an **allow tcp:443 egress** rule at 1000. Everything else outbound is blocked.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set up a low-priority (65534) rule that blocks all egress and a high-priority rule (1000) that allows only the appropriate ports.

**Why it's correct:**
- ✔️ "**low-priority (65534) rule that blocks all egress**" matches "**concerned about data egress**": it overrides the default allow-all egress.
- ✔️ "**high-priority rule (1000) that allows only the appropriate ports**" matches "**fewest open egress ports**": only these ports win over the deny.

📌 **When to use it:** Use it when only a few outbound doors should be open and everything else locked.
🏢 **Office example:** Rule #1 allows staff out through door 443; the last rule says no one leaves any other way.

### ❌ B
> **B.** Set up a high-priority (1000) rule that pairs both ingress and egress ports.

**Wrong words:**
- ❌ "**pairs both ingress and egress ports**": a firewall rule has **one direction**. There's no such pairing, and it doesn't block other egress.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** One rule for both entrances and exits doesn't exist.

### ❌ C
> **C.** Set up a high-priority (1000) rule that blocks all egress and a low-priority (65534) rule that allows only the appropriate ports.

**Wrong words:**
- ❌ "**high-priority (1000) rule that blocks all egress**" + "**low-priority (65534) rule that allows**": the deny wins first, so **nothing** gets out, not even the needed ports.

📌 **When to use it:** Use a high-priority deny when you want to block something no matter what.
🏢 **Office example:** The first rule says nobody leaves, so the later "door 443 is OK" never applies.

### ❌ D
> **D.** Set up a high-priority (1000) rule to allow the appropriate ports.

**Wrong words:**
- ❌ "**allow the appropriate ports**" only: egress is **already allowed for all ports** by the implied rule, so nothing is restricted.

📌 **When to use it:** Use allow-only rules for **ingress** (which is denied by default).
🏢 **Office example:** Saying door 443 is open while every other door is already open.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute firewall-rules create deny-all-egress --network=shop-vpc --direction=EGRESS --action=DENY --rules=all --priority=65534 --destination-ranges=0.0.0.0/0
gcloud compute firewall-rules create allow-https-egress --network=shop-vpc --direction=EGRESS --action=ALLOW --rules=tcp:443 --priority=1000 --destination-ranges=0.0.0.0/0
```

---

## 🧠 Key Takeaways / Memory Tips

- **Lower priority number wins.**
- **Egress is open by default** → deny-all (low priority) + allow specific (high priority).
  🧠 *"**Allow at 1000, deny at 65534.**"*
- Related: **Q087** (ingress rule), **Q053** (firewall parts).

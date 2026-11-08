# G027: Verify Whether a Specific Firewall Rule Is Allowing or Blocking Connections (Firewall Rules Logging)

**Topic:** VPC firewall (Firewall Rules Logging)
**Exam guide section:** 3.4 Monitoring and logging: Configuring audit logs (firewall logs); 3.3 Managing VPC firewall rules

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You created a firewall rule named deny-legacy-db that should block TCP 3306 traffic from the legacy subnet to your database VMs. You need to confirm that the rule is actually blocking connection attempts and see which source IP addresses are affected. What should you do?
>
> **A.** Enable Data Access audit logs for Compute Engine.
>
> **B.** Enable Firewall Rules Logging on the deny-legacy-db rule, and view the connection records in Cloud Logging.
>
> **C.** Change the rule's priority to 65535.
>
> **D.** Delete the rule and check whether the database receives connections.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You made a firewall rule (a network traffic rule) to stop old servers from reaching the database on port 3306 (the MySQL database port).
- **What you must achieve:** Prove the rule is really blocking those connection attempts, and see which source addresses are being blocked.
- **The limits:** Check that specific rule without breaking anything.
- **What they're really asking:** How do you get a record of the connections a particular firewall rule allows or blocks?

**Clues in the question:**
- "**confirm that the rule is actually blocking**" + "**which source IP addresses**": **Firewall Rules Logging** records each connection the rule matches.
- Logging is turned on **per rule**.

**Exam topic:** Networking and logging (exam guide sections 3.3 and 3.4).

---

## 📚 Key Terms Explained

### 1. Firewall Rules Logging 🔑
- **What it is:** A per-rule setting that writes a log entry for each TCP or UDP connection the rule allows or denies, including the rule name, action (ALLOWED or DENIED), source and destination.
- **Looks like:** `gcloud compute firewall-rules update deny-legacy-db --enable-logging` → log: `disposition: DENIED, src_ip: 10.8.0.14, dest_port: 3306`
- **Not to be confused with:** VPC Flow Logs, which record sampled traffic but not which rule decided it.
- **Analogy:** 📋 The guard's notebook at one specific door: who was turned away and when.
- **In the online store:** Proves legacy servers can't reach `orders-db`.

### 2. Rule priority
- **What it is:** A number from 0 to 65535. **Lower numbers win.** 65535 is the lowest priority.
- **Looks like:** `--priority=900` beats `--priority=1000`
- **Not to be confused with:** A rule's order in a list.
- **Analogy:** 🎖️ Rank: the lower the number, the more senior.
- **In the online store:** The deny rule at 900 beats the general allow at 1000.

### 🔗 How they fit together
```
 legacy 10.8.0.14 ──tcp:3306──► [deny-legacy-db, logging ON] ✋ DENIED
                                 └─► Cloud Logging entry (rule, src, port) ✅
```

---

## 🌍 Real-World Scenario

An auditor asks the team to prove that old servers can't reach customer data. With **Firewall Rules Logging** on, Cloud Logging shows dozens of DENIED entries from `10.8.0.0/24` on port 3306, all matched by `deny-legacy-db`. That's the evidence.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Data Access audit logs for Compute Engine.

**Wrong words:**
- ❌ "**Data Access audit logs**": record API data reads and writes, not firewall decisions.

📌 **When to use it:** Use them to see who read or changed data through Google Cloud APIs.
🏢 **Office example:** The library lending log, not the door guard's notebook.

### ✅ B
> **B.** Enable Firewall Rules Logging on the deny-legacy-db rule, and view the connection records in Cloud Logging.

**Why it's correct:**
- ✔️ "**Enable Firewall Rules Logging on the deny-legacy-db rule**" matches "**confirm that the rule is actually blocking**".
- ✔️ "**view the connection records in Cloud Logging**" matches "**see which source IP addresses are affected**".

📌 **When to use it:** Use it when you need proof of what one particular traffic rule is doing.
🏢 **Office example:** Asking the guard at one door to log everyone turned away.

### ❌ C
> **C.** Change the rule's priority to 65535.

**Wrong words:**
- ❌ "**priority to 65535**": the lowest priority, so other allow rules could win. It changes behavior and proves nothing.

📌 **When to use it:** Use a low priority for catch-all default rules.
🏢 **Office example:** Making the strict guard the most junior one.

### ❌ D
> **D.** Delete the rule and check whether the database receives connections.

**Wrong words:**
- ❌ "**Delete the rule**": opens the database to the legacy subnet. Testing by removing security is unsafe.

📌 **When to use it:** Never remove a security rule just to test it.
🏢 **Office example:** Firing the guard to see if anyone walks in.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: `deny-legacy-db` (priority 900, ingress, deny tcp:3306 from `10.8.0.0/24` to tag `db`) with logging on. Logs Explorer filter: `jsonPayload.rule_details.reference:"deny-legacy-db"`.

---

## 🧠 Key Takeaways / Memory Tips

- **Is this firewall rule allowing or denying, and for whom? → Firewall Rules Logging on that rule.**
  🧠 *"**Rule logs = the door guard's notebook.**"*
- Related: **G026**, **Q151**, **Q257**.

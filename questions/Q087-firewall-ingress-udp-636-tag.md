# Q087: Letting Clients Reach an LDAP Server on UDP 636 (Network Tag + Ingress Firewall Rule)

**Topic:** VPC networking (firewall rules, ingress vs egress, network tags, routes)

## ❓ Question
> You deployed an LDAP server on Compute Engine that is reachable via TLS through port 636 using UDP. You want to make sure it is reachable by clients over that port. What should you do?
>
> **A.** Add the network tag allow-udp-636 to the VM instance running the LDAP server.
>
> **B.** Create a route called allow-udp-636 and set the next hop to be the VM instance running the LDAP server.
>
> **C.** Add a network tag of your choice to the instance. Create a firewall rule to allow ingress on UDP port 636 for that network tag.
>
> **D.** Add a network tag of your choice to the instance running the LDAP server. Create a firewall rule to allow egress on UDP port 636 for that network tag.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An LDAP server (a directory of users) runs on a VM and is reached over TLS on port 636 using UDP.
- **What you must achieve:** Let clients reach it on that port.
- **The limits:** None stated.
- **What they're really asking:** What firewall rule do you add?

**Clues in the question:**
- "**reachable by clients**": traffic comes **into** the VM → **ingress**.
- "**port 636 using UDP**": the firewall rule must allow exactly **UDP 636**.
- By default, Google Cloud **blocks all incoming traffic**, so you need an **ingress allow rule**. A **network tag** picks which VMs the rule applies to.

**Exam topic:** VPC networking / firewall.

---

## 📚 Key Terms Explained

### 1️⃣ Firewall rule 🔑
- **What it is:** A **rule in the VPC that allows or blocks traffic** by direction (ingress/egress), protocol and port, source, and target VMs.
- **Looks like:** `gcloud compute firewall-rules create allow-ldap --direction=INGRESS --allow=udp:636 --target-tags=ldap --source-ranges=10.0.0.0/8`
- **Not to be confused with:** a network tag. The tag is only a **label**; the rule is what opens the port.
- **Analogy:** 🛡️ The **security guard's instructions**: "let visitors into rooms labeled LDAP, door 636".
- **In the online store:** a rule allows web traffic to the storefront VMs.

### 2️⃣ Ingress vs egress
- **What it is:** **Ingress** = traffic coming **into** a VM. **Egress** = traffic going **out of** a VM. By default: ingress is **denied**, egress is **allowed**.
- **Not to be confused with:** each other. Clients connecting to your server is **ingress** for the server.
- **Analogy:** 🚪 **Visitors entering** (ingress) vs **staff leaving** (egress).

### 3️⃣ Network tag
- **What it is:** A **text label on a VM** (e.g., `ldap`). Firewall rules and routes can target VMs by tag. The tag itself **does nothing**.
- **Looks like:** `gcloud compute instances add-tags ldap-1 --tags=ldap --zone=us-central1-a`
- **Not to be confused with:** a firewall rule. A tag named `allow-udp-636` still opens nothing.
- **Analogy:** 🏷️ A **sign on a room door**. The guard only cares about it if his instructions mention that sign.

### 4️⃣ Route
- **What it is:** A rule that says **where to send traffic** for a destination range (next hop). It doesn't allow or block anything.
- **Not to be confused with:** a firewall rule.
- **Analogy:** 🗺️ **Directions** to a room, not the permission to enter.

### 🔗 How they fit together
```
 client ──UDP 636──► [ firewall: INGRESS allow udp:636 target-tag=ldap ] ──► VM ldap-1 (tag: ldap) ✅
```

---

## 🌍 Real-World Scenario

A team moves its directory server (LDAP) to Compute Engine. Clients can't connect, because Google Cloud blocks incoming traffic by default. The engineer tags the VM `ldap` and creates an **ingress** firewall rule allowing **UDP 636** to that tag. Clients connect right away.

*(Note: real LDAPS normally uses TCP 636, but the question says UDP, so follow the question.)*

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add the network tag allow-udp-636 to the VM instance running the LDAP server.

**Wrong words:**
- ❌ "**Add the network tag allow-udp-636**": a tag is just a label. Its name doesn't open any port. Without a firewall rule that targets it, nothing changes.

📌 **When to use it:** Add a tag when a firewall rule already targets that tag.
🏢 **Office example:** Putting an "open to visitors" sign on a door, but never telling the guard.

### ❌ B
> **B.** Create a route called allow-udp-636 and set the next hop to be the VM instance running the LDAP server.

**Wrong words:**
- ❌ "**Create a route**": routes decide **where** traffic goes, not **whether** it's allowed. The firewall still blocks it.
- ❌ "**next hop to be the VM instance**": that's for VMs acting as routers or gateways, not for opening a port.

📌 **When to use it:** Use a route with a VM as next hop when that VM forwards traffic for others, like a NAT or firewall appliance.
🏢 **Office example:** Drawing a map to a room, when the real problem is that the guard won't let anyone in.

### ✅ C
> **C.** Add a network tag of your choice to the instance. Create a firewall rule to allow ingress on UDP port 636 for that network tag.

**Why it's correct:**
- ✔️ "**allow ingress**" matches "**reachable by clients**": clients connect **into** the server, which is ingress.
- ✔️ "**on UDP port 636**" matches "**port 636 using UDP**": exactly the protocol and port the question gives.
- ✔️ "**Add a network tag … for that network tag**" matches "**the LDAP server**": the rule applies only to the LDAP VM, not to every VM.

📌 **When to use it:** Use it when outside people must be able to reach one specific machine on one specific door.
🏢 **Office example:** Putting an "LDAP" sign on one room and telling the guard to let visitors into rooms with that sign, through door 636 only.

### ❌ D
> **D.** Add a network tag of your choice to the instance running the LDAP server. Create a firewall rule to allow egress on UDP port 636 for that network tag.

**Wrong words:**
- ✔️ "Add a network tag of your choice" is fine.
- ❌ "**allow egress**": egress is traffic **leaving** the VM. Clients connecting **in** need **ingress**. (Egress is already allowed by default anyway.)

📌 **When to use it:** Use an egress rule when you want to control what a VM can connect **out** to.
🏢 **Office example:** Telling the guard staff may leave through door 636, when visitors need to come in.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow runs an LDAP server `ldap-1` so internal tools can check staff logins.

```bash
gcloud compute instances add-tags ldap-1 --tags=ldap --zone=us-central1-a
gcloud compute firewall-rules create allow-ldap-636 \
  --network=shopnow-vpc --direction=INGRESS --allow=udp:636 \
  --target-tags=ldap --source-ranges=10.0.0.0/8
```
The admin dashboard VMs (10.0.2.x) can now reach `ldap-1` on port 636. Nothing else on `ldap-1` is opened.

---

## 🧠 Key Takeaways / Memory Tips

- **Clients reaching your VM → INGRESS allow rule** (protocol + port) **targeting a network tag**.
- **Tags are labels**; their name means nothing without a rule.
- **Routes ≠ firewall.** Routes say where, firewalls say allowed or not.
  🧠 *"**Coming IN? INgress.**"*
- Related: **Q053** (firewall rule parts), **Q050** (VPC basics).

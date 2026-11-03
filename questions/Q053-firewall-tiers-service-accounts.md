# Q053: Letting 3 Tiers Talk on Port 8080 (Firewall Rules by Service Account)

**Topic:** VPC firewall rules (ingress vs egress, targets and source filters by service account vs IP range, least privilege on ports)

## ❓ Question
> Your company has a 3-tier solution running on Compute Engine. The configuration of the current infrastructure is shown below.
>
> (Diagram: one VPC with three subnets. Subnet Tier#1 10.0.1.0/24 contains Instance Tier 1. Subnet Tier#2 10.0.2.0/24 contains Instance Tier 2. Subnet Tier#3 10.0.3.0/24 contains Instance Tier 3. All are Compute Engine instances.)
>
> Each tier has a service account that is associated with all instances within it. You need to enable communication on TCP port 8080 between tiers as follows:
> * Instances in tier #1 must communicate with tier #2.
> * Instances in tier #2 must communicate with tier #3.
>
> What should you do?
>
> **A.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.2.0/24) • Protocols: allow all 2. Create an ingress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.1.0/24) • Protocols: allow all
>
> **B.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #2 service account • Source filter: all instances with tier #1 service account • Protocols: allow TCP:8080 2. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #3 service account • Source filter: all instances with tier #2 service account • Protocols: allow TCP: 8080
>
> **C.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #2 service account • Source filter: all instances with tier #1 service account • Protocols: allow all 2. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #3 service account • Source filter: all instances with tier #2 service account • Protocols: allow all
>
> **D.** 1. Create an egress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.2.0/24) • Protocols: allow TCP: 8080 2. Create an egress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.1.0/24) • Protocols: allow TCP: 8080

*(The `ג€¢` characters in the original are broken bullet points, shown here as `•`.)*

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You have a classic 3-tier app (for example **web → API → database**), each tier in its own subnet, and **each tier has its own service account**. You must open **only TCP port 8080**, and **only in two directions**:
- Tier 1 → Tier 2
- Tier 2 → Tier 3

Which firewall rules do exactly that, and nothing more?

| Keyword | What it hints at |
|---|---|
| "**Each tier has a service account**" | Use the service account as the **firewall label** for targets and sources |
| "**TCP port 8080**" | Allow **only TCP:8080**, not "all" (least privilege) |
| "**tier #1 … with tier #2**", "**tier #2 … with tier #3**" | The **receiver** is the **target** and the **sender** is the **source**. Tier 1 must **not** reach Tier 3 directly |
| Traffic **arriving** at tier 2 / tier 3 | **Ingress** rules (incoming), on the receiving tier |

**Exam topic:** VPC firewall rules.

---

## 📚 Key Terms Explained

### 1️⃣ Firewall Rule (VPC firewall)
- **What it is:** A **rule on the VPC** that **allows or blocks traffic** to or from VMs. Each rule says: **direction**, **which VMs it applies to (targets)**, **where traffic comes from (source)**, **which ports**, and **allow/deny**. By default, a VPC **blocks all incoming** traffic and **allows all outgoing**.
- **Looks like:**
  ```
  name: allow-t1-to-t2-8080
  direction: INGRESS   action: ALLOW
  targets: serviceAccount tier2-sa@…   source: serviceAccount tier1-sa@…
  ports: tcp:8080
  ```
- **Not to be confused with:** a **route** (Q050), which decides the **path** traffic takes. The firewall decides whether traffic is **allowed**.
- **Analogy:** 🛂 The **security guard at each department's door**, with a list: "Let in people from department X, only through door 8080."
- **In the online store:** Only the web servers may call the checkout API on port 8080.

### 2️⃣ Ingress vs Egress 🔑
- **What it is:** **Ingress** = traffic **coming into** a VM. **Egress** = traffic **going out of** a VM. Since **incoming is blocked by default**, you open communication with **ingress** rules on the **receiving** VMs.
- **Looks like:** `--direction=INGRESS` (default) or `--direction=EGRESS`
- **Not to be confused with:** "who starts the conversation". The **reply** traffic is allowed automatically (firewall rules are **stateful**).
- **Analogy:** 🚪 Ingress = the guard checking **who comes in**. Egress = the guard checking **who goes out**. The doors already let everyone **out**, so you only need to fix who's let **in**.

### 3️⃣ Target and Source (by service account)
- **What it is:** **Target** = the VMs the rule **protects** (the receivers for ingress). **Source** = **who** is allowed to send. Both can be chosen by **IP range**, **network tag**, or **service account**.
- **Looks like:** `--target-service-accounts=tier2-sa@…` and `--source-service-accounts=tier1-sa@…`
- **Not to be confused with:** IAM permissions. Here the service account is just used as a **label** to pick VMs. It doesn't grant API access.
- **Analogy:** 🪪 The guard checks **department ID badges** ("Tier 1 badge? Come in through door 8080") instead of **which street the visitor came from** (IP range).
- **Why it's better than IP ranges:** IPs change when VMs are recreated or moved, but the service account stays with the tier. Google recommends **service accounts** for firewall targeting because only people allowed to **use** a service account can attach it, so it's harder to fake than a tag.

### 4️⃣ Port and Protocol (TCP:8080)
- **What it is:** A **port** is a numbered "door" on a VM for a specific app. **TCP** is the protocol. `tcp:8080` = only the app listening on door 8080.
- **Looks like:** `--allow=tcp:8080` vs `--allow=all` (every protocol and port)
- **Not to be confused with:** "allow all", which also opens SSH (22), databases, and everything else.
- **Analogy:** 🚪 Opening **one specific door** instead of **removing the walls**.

### 🔗 How They Fit Together
```
VPC
 Subnet Tier#1 10.0.1.0/24     Subnet Tier#2 10.0.2.0/24      Subnet Tier#3 10.0.3.0/24
 🖥️ web (tier1-sa)  ──8080──►  🖥️ api (tier2-sa)  ──8080──►   🖥️ db-svc (tier3-sa)
                     ▲                              ▲
        Rule 1 (INGRESS)                   Rule 2 (INGRESS)
        target: tier2-sa                   target: tier3-sa
        source: tier1-sa                   source: tier2-sa
        allow:  tcp:8080                   allow:  tcp:8080

 🚫 web → db-svc directly: no rule → blocked ✅ (good!)
```

---

## 🌍 Real-World Scenario

A typical app has a **web tier** (talks to users), an **app/API tier** (business logic), and a **data tier** (database or data services). Security teams require that **each tier can only talk to the next one, on one port**. If the web server is hacked, the attacker **can't jump straight to the database** or open an SSH session to the API servers. Firewall rules **by service account**, **ingress only**, **one port**, is the textbook way to do it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.2.0/24) • Protocols: allow all 2. Create an ingress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.1.0/24) • Protocols: allow all

**Why it's wrong:**
- ❌ **Targets: all instances** → Tier 1's subnet can reach **every** VM, including **Tier 3**, which isn't allowed.
- ❌ **Allow all** protocols and ports, not just TCP:8080. That's far too open.
- ❌ It also lets Tier 2 send to Tier 1 (backwards direction).

**📌 When to use it:** Use broad IP-range rules only in a test setup where everything in a subnet should reach everything.
🏢 **Office example:** Telling the guards "anyone from the 1st floor can enter any room on any floor through any door."

### ✅ B (your answer)
> **B.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #2 service account • Source filter: all instances with tier #1 service account • Protocols: allow TCP:8080 2. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #3 service account • Source filter: all instances with tier #2 service account • Protocols: allow TCP: 8080

**Why it's correct:**
- ✔️ **Ingress** on the **receiving** tier, the right direction (incoming is blocked by default).
- ✔️ **Targets/sources by service account**, which match the tiers exactly, even when VMs are added or their IPs change.
- ✔️ **Only TCP:8080**, which is least privilege.
- ✔️ Exactly two paths: 1 → 2 and 2 → 3. Tier 1 → Tier 3 stays **blocked**.

**📌 When to use it:** Use it when each group of servers should only be reached by one specific other group, through one door.
🏢 **Office example:** The API department's guard lets in only people with a Web department badge, and only through door 8080.

### ❌ C
> **C.** 1. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #2 service account • Source filter: all instances with tier #1 service account • Protocols: allow all 2. Create an ingress firewall rule with the following settings: • Targets: all instances with tier #3 service account • Source filter: all instances with tier #2 service account • Protocols: allow all

**Why it's wrong:**
- ✔️ Right direction, right targets and sources…
- ❌ …but **allow all** opens **every port and protocol** (SSH, databases, anything), not just TCP:8080. That breaks least privilege.

**📌 When to use it:** Use "allow all" between groups only when they truly must use many different services with each other.
🏢 **Office example:** The guard lets Web-badge holders through every door of the API department, not just the one they need.

### ❌ D
> **D.** 1. Create an egress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.2.0/24) • Protocols: allow TCP: 8080 2. Create an egress firewall rule with the following settings: • Targets: all instances • Source filter: IP ranges (with the range set to 10.0.1.0/24) • Protocols: allow TCP: 8080

**Why it's wrong:**
- ❌ **Egress** controls **outgoing** traffic, and outgoing is **already allowed** by default. The real block is on **incoming** traffic, which these rules don't open.
- ❌ Egress rules use a **destination** filter, not a **source** filter, so these settings don't even fit together.
- ❌ **Targets: all instances**, which isn't limited to the right tiers.

**📌 When to use it:** Use egress rules when you want to stop servers from sending traffic out, for example blocking a server from reaching the internet.
🏢 **Office example:** Telling the guards who's allowed to leave the building, when the problem was that nobody could get in.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's 3 tiers in `shopnow-vpc`:
| Tier | Subnet | VMs | Service account |
|---|---|---|---|
| 1. Web (Next.js storefront) | 10.0.1.0/24 | `web-01..05` | `web-sa@shopnow-prod.iam.gserviceaccount.com` |
| 2. API (checkout/orders) | 10.0.2.0/24 | `api-01..03` | `api-sa@…` |
| 3. Data service (inventory/DB proxy) | 10.0.3.0/24 | `data-01..02` | `data-sa@…` |

```bash
# Rule 1: web → api on 8080
gcloud compute firewall-rules create allow-web-to-api-8080 \
  --network=shopnow-vpc --direction=INGRESS --action=ALLOW --rules=tcp:8080 \
  --source-service-accounts=web-sa@shopnow-prod.iam.gserviceaccount.com \
  --target-service-accounts=api-sa@shopnow-prod.iam.gserviceaccount.com

# Rule 2: api → data on 8080
gcloud compute firewall-rules create allow-api-to-data-8080 \
  --network=shopnow-vpc --direction=INGRESS --action=ALLOW --rules=tcp:8080 \
  --source-service-accounts=api-sa@shopnow-prod.iam.gserviceaccount.com \
  --target-service-accounts=data-sa@shopnow-prod.iam.gserviceaccount.com
```

| Traffic | Result |
|---|---|
| `web-02` → `api-01:8080` | ✅ Allowed (rule 1) |
| `api-01` → `data-01:8080` | ✅ Allowed (rule 2) |
| `web-02` → `data-01:8080` | 🚫 Blocked. A hacked web server can't reach the data tier |
| `web-02` → `api-01:22` (SSH) | 🚫 Blocked. Only 8080 is open (C would allow this ❌) |
| New VM `api-04` added with `api-sa` | ✅ Covered automatically, no rule change |

---

## 🧠 Key Takeaways / Memory Tips

- **Tier-to-tier traffic → INGRESS rules on the receiver**, with **target = receiver**, **source = sender**.
  🧠 *"**Guard the door you walk INTO.** Ingress, on the receiving side."*
- **Use service accounts (or tags) for targets/sources**, not "all instances" or wide IP ranges.
- **Open only the needed port** (`tcp:8080`). "Allow all" is a least-privilege trap.
- **Egress is already open by default.** An egress-only answer rarely fixes "can't connect".
- Related: **Q050** (VPC, subnets, routes = path vs firewall = permission), **Q019/Q026** (service accounts on VMs).

---

## 🤔 Follow-up: "The options aren't clear. What's the difference between A and B?"

### Step 1: Read a firewall rule like a guard's instruction card

Every rule answers 4 questions:

| Field | Question it answers | Office version |
|---|---|---|
| **Direction** (ingress/egress) | Checking people coming **in** or going **out**? | Guard at the **entrance** or the **exit** |
| **Targets** | **Which rooms** does this guard protect? | "This guard stands at the API room" |
| **Source filter** | **Who** is allowed in? | "Let in people with a Web badge" |
| **Protocols/ports** | **Which door** can they use? | "Only door 8080" vs "any door" |

### Step 2: Put A and B side by side

| | **A** | **B** ✅ |
|---|---|---|
| Rule 1 targets (**which VMs are opened up**) | **All instances** (tier 1, 2 and 3) | **Only tier 2** VMs |
| Rule 1 source (**who may connect**) | Anyone in **10.0.2.0/24** = tier 2 | Only VMs with the **tier 1** service account |
| Rule 2 targets | **All instances** | **Only tier 3** VMs |
| Rule 2 source | Anyone in **10.0.1.0/24** = tier 1 | Only VMs with the **tier 2** service account |
| Ports | **Allow all** (every port) | **TCP:8080 only** |

**Notice:** In A, the source ranges are even **swapped**: rule 1 lets **tier 2** in, rule 2 lets **tier 1** in, and both open the doors of **every** VM.

### Step 3: What can actually talk? (sender → receiver)

**Required:** 1→2 on 8080, and 2→3 on 8080. Nothing else.

| Sender → Receiver | Needed? | **A** | **B** |
|---|---|---|---|
| Tier 1 → Tier 2 (8080) | ✅ yes | ✅ open | ✅ open |
| Tier 2 → Tier 3 (8080) | ✅ yes | ✅ open | ✅ open |
| Tier 1 → **Tier 3** | ❌ no | ⚠️ **open** (target = all) | 🚫 blocked |
| Tier 2 → **Tier 1** (backwards) | ❌ no | ⚠️ **open** | 🚫 blocked |
| Tier 1 → Tier 2 on **SSH port 22** | ❌ no | ⚠️ **open** (allow all) | 🚫 blocked |

**So:** A *does* make the required connections work, but it **also opens 3 doors that should stay locked**. B opens **exactly** what was asked and nothing more. On the exam, "**most secure / least privilege**" always beats "it works but opens too much".

### Step 4: All four options in one line each

| Option | Direction | Who is opened up (targets) | Who may connect (source) | Ports | Verdict |
|---|---|---|---|---|---|
| **A** | Ingress ✅ | **Everyone** ❌ | Subnet IP ranges | **All** ❌ | Works, but far too open |
| **B** | Ingress ✅ | **Tier 2 / Tier 3 only** ✅ | **Tier 1 / Tier 2 badge** ✅ | **8080** ✅ | ✅ Exactly right |
| **C** | Ingress ✅ | Tier 2 / Tier 3 only ✅ | Tier 1 / Tier 2 badge ✅ | **All** ❌ | Right people, too many doors |
| **D** | **Egress** ❌ | Everyone ❌ | (egress has no "source") ❌ | 8080 | Wrong direction, doesn't open incoming traffic |

🧠 **How to check any firewall option quickly:** Ask three questions:
1. **Ingress?** (Incoming is what's blocked by default.)
2. **Are targets and sources limited to the right tiers?** ("All instances" = 🚩)
3. **Is only the needed port open?** ("Allow all" = 🚩)

**Only B passes all three.**

### 🏢 Office version of A vs B
- **A:** "Anyone from the 2nd floor may enter **any room in the building** through **any door**. Anyone from the 1st floor may also enter **any room** through **any door**." The 1st floor can now walk into the 3rd-floor vault. 😬
- **B:** "At the **API room**, let in only **Web-badge** holders, through **door 8080**. At the **Data room**, let in only **API-badge** holders, through **door 8080**." Nobody can skip a floor.

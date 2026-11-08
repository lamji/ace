# G002: Only the Security Team Controls Which VMs a Firewall Rule Applies To (Cloud NGFW + Secure Tags)

**Topic:** VPC firewall (Cloud NGFW secure Tags)
**Exam guide section:** 2.3 Networking: Using Tags (e.g., secure Tags) and service accounts in Cloud NGFW policy rules

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your web tier VMs must reach your database tier VMs on TCP port 5432, and no other traffic to the database tier is allowed. Developers have permission to edit VM properties, and the security team is concerned that a developer could add a network tag to any VM to bypass firewall rules. You want only the security team to control which VMs a rule applies to. What should you do?
>
> **A.** Create VPC firewall rules that use the network tags web and db, and ask developers not to change network tags.
>
> **B.** Remove the developers' permission to edit VMs and grant them the Owner role on the project instead.
>
> **C.** Create a VPC firewall rule that allows TCP 5432 from 0.0.0.0/0 to all instances in the network.
>
> **D.** Create secure Tags for web and db with the firewall purpose, allow only the security team to bind them to VMs through IAM, and use them as the source and target of a Cloud NGFW network firewall policy rule that allows TCP 5432.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You have two groups of VMs (virtual machines: rented computers): web servers and database servers. A firewall rule lets the web servers talk to the database servers on port 5432 (the PostgreSQL database port).
- **What you must achieve:** Make sure that only the security team decides which VMs count as "web" or "database" for the firewall.
- **The limits:** Developers can edit VM settings, including the simple labels (network tags) that normal firewall rules use. Nothing except web → database on TCP 5432 may reach the database tier.
- **What they're really asking:** What kind of label can only the security team attach to a VM, so a firewall rule can't be bypassed by relabeling a VM?

**Clues in the question:**
- "**developer could add a network tag to any VM to bypass**": plain network tags can be changed by anyone who can edit the VM.
- "**only the security team control which VMs a rule applies to**": you need labels that are **protected by IAM**. These are **secure Tags**.
- "**TCP port 5432 … no other traffic**": one narrow allow rule from source web to target db.

**Exam topic:** Networking: Cloud NGFW firewall policies (exam guide sections 2.3 and 3.3).

---

## 📚 Key Terms Explained

### 1. Network tag
- **What it is:** A simple text label on a VM (for example `web`) that VPC firewall rules can target. Anyone who can edit the VM can add or remove it.
- **Looks like:** `gcloud compute instances add-tags vm-1 --tags=db`
- **Not to be confused with:** A secure Tag. Network tags have no access control of their own.
- **Analogy:** 🏷️ A sticky note on a desk saying "Accounting". Anyone can move it.
- **In the online store:** Old ShopNow rules used `web` and `db` network tags.

### 2. Secure Tag (Resource Manager tag) 🔑
- **What it is:** A key/value tag created in Resource Manager (for example `env-tier=db`) with the **firewall purpose**, then bound to VMs. Attaching it needs a special IAM role (Tag User) on that tag value, so you control **who** can label a VM.
- **Looks like:** Tag key `shopnow/tier` with values `web` and `db`; bind with `gcloud resource-manager tags bindings create --tag-value=tagValues/123 --parent=//compute.googleapis.com/projects/p/zones/z/instances/vm-1`
- **Not to be confused with:** A network tag (an unprotected sticker) or a label (used for billing, not firewalls).
- **Analogy:** 🔐 A badge that only the security office can issue.
- **In the online store:** Only the security team holds the Tag User role on `tier=db`.

### 3. Cloud NGFW network firewall policy
- **What it is:** Google Cloud's next-generation firewall. Its rules live in **firewall policies** (global, regional or hierarchical) attached to VPC networks, and they can match secure Tags, service accounts, IP ranges and more.
- **Looks like:** Policy `shop-fw` → rule priority 1000: ingress, allow tcp:5432, source tag `tier=web`, target tag `tier=db`
- **Not to be confused with:** Old per-network VPC firewall rules. Those still work, but they can't use secure Tags.
- **Analogy:** 📜 The building's central security rulebook.
- **In the online store:** `shop-fw` is attached to `shop-vpc`.

### 🔗 How they fit together
```
 Security team ──(Tag User role)──► binds tier=web / tier=db to VMs
 Network firewall policy shop-fw:
   allow tcp:5432  src tag tier=web ──► target tag tier=db
   (lower-priority deny all ingress to tier=db)
 Developer edits VM → cannot bind tier=db (no IAM permission) ✅
```

---

## 🌍 Real-World Scenario

At a payments company, auditors found that a developer had added the `db` network tag to a test VM, and it could suddenly reach production databases. The fix is to move these rules to a **Cloud NGFW network firewall policy** that uses **secure Tags**. Developers keep their VM admin rights, but they can't bind the `tier=db` tag because that needs IAM permission on the tag itself.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create VPC firewall rules that use the network tags web and db, and ask developers not to change network tags.

**Wrong words:**
- ✔️ A rule from web to db on port 5432 is the right idea.
- ❌ "**network tags web and db**": anyone who can edit the VM can change network tags, which is exactly the risk in the question.
- ❌ "**ask developers not to change network tags**": a request is not a control.

📌 **When to use it:** Use it when every person who can edit VMs is trusted to manage firewall targeting.
🏢 **Office example:** A sticky note on the door saying "Accounting only", which anyone can move.

### ❌ B
> **B.** Remove the developers' permission to edit VMs and grant them the Owner role on the project instead.

**Wrong words:**
- ❌ "**grant them the Owner role**": Owner gives developers far **more** power, including changing firewall rules themselves. It breaks least privilege.

📌 **When to use it:** Never use this to fix a permissions risk. Give narrower roles and protected tags.
🏢 **Office example:** Giving someone the master key because you worried about their desk key.

### ❌ C
> **C.** Create a VPC firewall rule that allows TCP 5432 from 0.0.0.0/0 to all instances in the network.

**Wrong words:**
- ❌ "**from 0.0.0.0/0**": opens the database port to the entire internet.
- ❌ "**to all instances in the network**": every VM becomes a target, not just the database tier.

📌 **When to use it:** Never use this for databases. Allow only specific sources to specific targets.
🏢 **Office example:** Leaving the records room unlocked for anyone off the street.

### ✅ D
> **D.** Create secure Tags for web and db with the firewall purpose, allow only the security team to bind them to VMs through IAM, and use them as the source and target of a Cloud NGFW network firewall policy rule that allows TCP 5432.

**Why it's correct:**
- ✔️ "**secure Tags … allow only the security team to bind them to VMs through IAM**" matches "**only the security team control which VMs a rule applies to**".
- ✔️ "**source and target of a Cloud NGFW network firewall policy rule that allows TCP 5432**" matches "**web tier VMs must reach your database tier VMs on TCP port 5432**".
- ✔️ Developers can still edit VMs, but binding a secure Tag needs separate IAM permission, so they can't bypass the rule.

📌 **When to use it:** Use it when you want only certain people to decide which machines a firewall rule covers.
🏢 **Office example:** Only the security office can issue the badge that opens the server room.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `shop-vpc`:
- Secure tag key `shopnow/tier` with values `web`, `api`, `db`.
- Network firewall policy rule: allow tcp:5432 from `tier=api` to `tier=db`. Everything else to `tier=db` is denied.
- Only `secops@shopnow.com` has `roles/resourcemanager.tagUser` on `tier=db`.

---

## 🧠 Key Takeaways / Memory Tips

- **Firewall targeting that only some people may control → secure Tags in a Cloud NGFW firewall policy.**
- Network tags = unprotected stickers. Secure Tags = IAM-protected badges.
  🧠 *"**Sticker vs badge: network tag vs secure Tag.**"*
- Related: **Q053**, **Q087**, **Q151**, **Q206** (firewall rules); **Q317** (hierarchical policies).

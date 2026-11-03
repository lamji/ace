# Q206: Allow Database Traffic Only From App Servers to DB Servers (Ingress Rule: Source SA sa-app → Target SA sa-db)

**Topic:** Networking (firewall rules with service accounts)

## ❓ Question
> You have two subnets (subnet-a and subnet-b) in the default VPC. Your database servers are running in subnet-a. Your application servers and web servers are running in subnet-b. You want to configure a firewall rule that only allows database traffic from the application servers to the database servers. What should you do?
>
> **A.** • Create service accounts sa-app and sa-db. • Associate service account sa-app with the application servers and the service account sa-db with the database servers. • Create an ingress firewall rule to allow network traffic from source service account sa-app to target service account sa-db.
>
> **B.** • Create network tags app-server and db-server. • Add the app-server tag to the application servers and the db-server tag to the database servers. • Create an egress firewall rule to allow network traffic from source network tag app-server to target network tag db-server.
>
> **C.** • Create a service account sa-app and a network tag db-server. • Associate the service account sa-app with the application servers and the network tag db-server with the database servers. • Create an ingress firewall rule to allow network traffic from source VPC IP addresses and target the subnet-a IP addresses.
>
> **D.** • Create a network tag app-server and service account sa-db. • Add the tag to the application servers and associate the service account with the database servers. • Create an egress firewall rule to allow network traffic from source network tag app-server to target service account sa-db.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Only **app servers** (not web servers in the same subnet) may reach the **DB servers**.

**Clues in the question:**
- App and web servers share subnet-b, so subnet ranges can't tell them apart → identify VMs by **service account** (or tag).
- Traffic **arriving at** the DB = **ingress**. Only ingress rules have a **source** filter by SA/tag.
- A rule can't mix **tags and service accounts** for source/target.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Firewall rule by service account 🔑
- **What it is:** Source/target chosen by the **service account** attached to VMs. Stricter than tags, because changing a VM's SA needs more permissions.
- **Looks like:** `--direction=INGRESS --source-service-accounts=sa-app@… --target-service-accounts=sa-db@… --allow=tcp:5432`
- **Not to be confused with:** network tags.
- **Analogy:** 🪪 Door opens only for staff wearing the App badge.
- **In the online store:** app → Cloud SQL proxy VMs.

### 2. Ingress vs egress (review from Q179)
- **What it is:** Ingress = traffic **coming in**. Egress = traffic **going out**. Egress rules can't filter by source tag/SA.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🚪 In vs out.
- **In the online store:** —

### 🔗 How they fit together
```
 subnet-b: web (no sa-app) ✗      app (sa-app) ──INGRESS tcp:5432──► subnet-a: db (sa-db) ✅
```

---

## 🌍 Real-World Scenario

Web and app servers share a subnet. The team gives app servers `sa-app` and DB servers `sa-db`, then creates an **ingress** rule from `sa-app` to `sa-db` on the DB port. Web servers can't reach the DB.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** • Create service accounts sa-app and sa-db. • Associate service account sa-app with the application servers and the service account sa-db with the database servers. • Create an ingress firewall rule to allow network traffic from source service account sa-app to target service account sa-db.

**Why it's correct:**
- ✔️ "**source service account sa-app**" matches "**from the application servers**" (and excludes the web servers in the same subnet).
- ✔️ "**target service account sa-db**" matches "**to the database servers**".
- ✔️ "**ingress firewall rule**": the DB servers are receiving the traffic.

📌 **When to use it:** Use it when only one specific group of machines may talk to another group.
🏢 **Office example:** The records room door opens only for staff wearing the App badge.

### ❌ B
> **B.** • Create network tags app-server and db-server. • Add the app-server tag to the application servers and the db-server tag to the database servers. • Create an egress firewall rule to allow network traffic from source network tag app-server to target network tag db-server.

**Wrong words:**
- ✔️ Tags on both sides could work.
- ❌ "**egress firewall rule … from source network tag**": egress rules can't filter on a source tag, and the DB needs an **ingress** allow.

📌 **When to use it:** Use egress rules to control what leaves VMs.
🏢 **Office example:** Checking badges at the exit instead of at the records room door.

### ❌ C
> **C.** • Create a service account sa-app and a network tag db-server. • Associate the service account sa-app with the application servers and the network tag db-server with the database servers. • Create an ingress firewall rule to allow network traffic from source VPC IP addresses and target the subnet-a IP addresses.

**Wrong words:**
- ❌ "**from source VPC IP addresses**": that lets the **web servers** in too.
- ❌ It mixes a service account and a tag but then doesn't use them.

📌 **When to use it:** Use IP ranges when whole subnets should be allowed.
🏢 **Office example:** Letting anyone from that floor into the records room.

### ❌ D
> **D.** • Create a network tag app-server and service account sa-db. • Add the tag to the application servers and associate the service account with the database servers. • Create an egress firewall rule to allow network traffic from source network tag app-server to target service account sa-db.

**Wrong words:**
- ❌ "**egress**" (wrong direction) and ❌ mixing a **tag source** with a **service account target**: not allowed in one rule.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Mixing badge types on one door rule.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute firewall-rules create app-to-db --network=default --direction=INGRESS --allow=tcp:5432 \
  --source-service-accounts=sa-app@shopnow-prod.iam.gserviceaccount.com \
  --target-service-accounts=sa-db@shopnow-prod.iam.gserviceaccount.com
```

---

## 🧠 Key Takeaways / Memory Tips

- **Same subnet, different roles → filter by service account (or tag), ingress on the receiver.** Don't mix tags and SAs in one rule.
  🧠 *"**Badge at the door you're entering.**"*
- Related: **Q179**, **Q151**.

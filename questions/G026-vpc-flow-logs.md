# G026: Record Sampled Network Connections From a Subnet for Later Analysis (VPC Flow Logs)

**Topic:** Networking logs (VPC Flow Logs)
**Exam guide section:** 3.4 Monitoring and logging: Configuring audit logs (e.g., VPC Flow Logs, audit logs, firewall logs)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> The security team wants to record a sample of the network connections made by VMs in the prod-subnet subnet, including source and destination IP addresses, ports, and bytes transferred, so they can analyze traffic later in Cloud Logging and BigQuery. What should you do?
>
> **A.** Enable Data Access audit logs for Compute Engine.
>
> **B.** Install a packet-capture tool on every VM and upload the capture files to Cloud Storage.
>
> **C.** Enable VPC Flow Logs on the prod-subnet subnet.
>
> **D.** Enable Cloud NAT logging for the VPC network.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The security team wants a record of network traffic for VMs in one subnet (a slice of the private network) named prod-subnet.
- **What you must achieve:** Capture a sample of each connection: who talked to whom (IP addresses), which ports, and how much data, then study it later in Cloud Logging and BigQuery.
- **The limits:** A sample is fine (not every packet). It must cover the VMs in that subnet.
- **What they're really asking:** Which Google Cloud feature records network connection summaries for a subnet?

**Clues in the question:**
- "**sample of the network connections … source and destination IP addresses, ports, and bytes**": exactly what **VPC Flow Logs** record.
- "**prod-subnet subnet**": flow logs are enabled per subnet.

**Exam topic:** Networking and logging (exam guide sections 3.3 and 3.4).

---

## 📚 Key Terms Explained

### 1. VPC Flow Logs 🔑
- **What it is:** Sampled records of network flows (connections) to and from VM interfaces: IPs, ports, protocol, bytes, packets and more. They go to Cloud Logging and can be routed to BigQuery.
- **Looks like:** `gcloud compute networks subnets update prod-subnet --region=us-central1 --enable-flow-logs --logging-flow-sampling=0.5`
- **Not to be confused with:** Firewall Rules Logging (which rule allowed or denied traffic) or audit logs (who changed settings).
- **Analogy:** 📞 The phone company's call records: who called whom and for how long, not the conversation.
- **In the online store:** Records traffic between the web and DB tiers.

### 2. Data Access audit logs
- **What it is:** Logs of who read or wrote data through Google Cloud APIs (for example, reading objects).
- **Looks like:** `storage.objects.get by ana@`
- **Not to be confused with:** Network traffic logs.
- **Analogy:** 📖 The library's lending log.
- **In the online store:** Who read the invoice bucket.

### 🔗 How they fit together
```
 VMs in prod-subnet ─flows─► VPC Flow Logs (sampled) ─► Cloud Logging ─sink─► BigQuery ✅
```

---

## 🌍 Real-World Scenario

After a suspicious spike in outbound traffic, security enables **VPC Flow Logs** on `prod-subnet` and sends them to BigQuery. A query shows one VM sending gigabytes to an unknown IP address, and the leak is found.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Data Access audit logs for Compute Engine.

**Wrong words:**
- ❌ "**Data Access audit logs**": record API calls that read or write data, not network connections between VMs.

📌 **When to use it:** Use them to see who read or changed data through Google Cloud APIs.
🏢 **Office example:** The library lending log, not the phone records.

### ❌ B
> **B.** Install a packet-capture tool on every VM and upload the capture files to Cloud Storage.

**Wrong words:**
- ❌ "**packet-capture tool on every VM**": heavy, manual, captures far more than needed, and isn't integrated with Cloud Logging.

📌 **When to use it:** Use packet capture only for deep, short troubleshooting of one machine.
🏢 **Office example:** Recording every phone call when you only need the call list.

### ✅ C
> **C.** Enable VPC Flow Logs on the prod-subnet subnet.

**Why it's correct:**
- ✔️ "**VPC Flow Logs**" matches "**sample of the network connections … IP addresses, ports, and bytes**".
- ✔️ "**on the prod-subnet subnet**" matches "**VMs in the prod-subnet subnet**".
- ✔️ Flow logs land in Cloud Logging and can be routed to BigQuery, matching "**analyze traffic later**".

📌 **When to use it:** Use it when you need a record of which machines talked to which, and how much.
🏢 **Office example:** The phone bill's call list showing who called whom.

### ❌ D
> **D.** Enable Cloud NAT logging for the VPC network.

**Wrong words:**
- ❌ "**Cloud NAT logging**": records NAT address translations for outbound internet traffic only, not all VM connections in the subnet.

📌 **When to use it:** Use it to see outbound connections that went through Cloud NAT.
🏢 **Office example:** Only logging calls that went through the switchboard to outside lines.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: flow logs on `prod-subnet` (sampling 0.5, 5-second aggregation) → sink to BigQuery dataset `netlogs`. Query: top destination IPs by bytes from `orders-api` VMs.

---

## 🧠 Key Takeaways / Memory Tips

- **Who talked to whom on the network (IPs, ports, bytes) → VPC Flow Logs (per subnet).**
  🧠 *"**Flow logs = phone call records.**"*
- Related: **G027** (firewall logging), **Q244**, **Q368**.

# Q162: Apps Must Survive the On-Prem Database IP Changing (Cloud DNS Private Zone + DNS Name)

**Topic:** Networking (Cloud DNS private zones, hybrid connectivity)

## ❓ Question
> Your company has embraced a hybrid cloud strategy where some of the applications are deployed on Google Cloud. A Virtual Private Network (VPN) tunnel connects your Virtual Private Cloud (VPC) in Google Cloud with your company's on-premises network. Multiple applications in Google Cloud need to connect to an on-premises database server, and you want to avoid having to change the IP configuration in all of your applications when the IP of the database changes. What should you do?
>
> **A.** Configure Cloud NAT for all subnets of your VPC to be used when egressing from the VM instances.
>
> **B.** Create a private zone on Cloud DNS, and configure the applications with the DNS name.
>
> **C.** Configure the IP of the database as custom metadata for each instance, and query the metadata server.
>
> **D.** Query the Compute Engine internal DNS from the applications to retrieve the IP of the database.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Apps connect to an **on-prem DB by IP**. When the IP changes, you don't want to edit every app.

**Clues in the question:**
- "**avoid having to change the IP configuration in all of your applications**": use a **name** instead of an IP. Change the IP in **one place** (DNS).
- A **Cloud DNS private zone** gives names visible only inside your VPC.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Cloud DNS private zone 🔑
- **What it is:** DNS names that resolve **only inside your chosen VPCs**.
- **Looks like:** zone `corp.internal` → record `db.corp.internal A 192.168.10.5`
- **Not to be confused with:** public DNS.
- **Analogy:** 📇 The **internal phone directory**: call "Accounting", not the extension.
- **In the online store:** `orders-db.shop.internal`

### 2. Compute Engine internal DNS
- **What it is:** Automatic names **for VMs** in your VPC (`vm.zone.c.project.internal`). It doesn't know on-prem servers.
- **Looks like:** `web-1.us-central1-a.c.shop.internal`
- **Not to be confused with:** custom names for on-prem hosts.
- **Analogy:** 📇 The directory of your own staff only.
- **In the online store:** Calling other VMs by name.

### 🔗 How they fit together
```
 apps → db.corp.internal (Cloud DNS private zone) → 192.168.10.5 ──VPN──► on-prem DB
 DB moves → change ONE record → apps unchanged ✅
```

---

## 🌍 Real-World Scenario

A hybrid company's apps connect to an on-prem database. Instead of hard-coding the IP, they use `db.corp.internal` from a **Cloud DNS private zone**. When the DB moves, only the DNS record is updated.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure Cloud NAT for all subnets of your VPC to be used when egressing from the VM instances.

**Wrong words:**
- ❌ "**Cloud NAT**": it lets private VMs reach the **internet**. It has nothing to do with naming an on-prem DB.

📌 **When to use it:** Use Cloud NAT for outbound internet access without public IPs.
🏢 **Office example:** A shared exit door, not a phone directory.

### ✅ B
> **B.** Create a private zone on Cloud DNS, and configure the applications with the DNS name.

**Why it's correct:**
- ✔️ "**private zone on Cloud DNS**" matches "**when the IP of the database changes**": update one DNS record.
- ✔️ "**configure the applications with the DNS name**" matches "**avoid having to change the IP configuration in all of your applications**".

📌 **When to use it:** Use it when many people need to reach something whose address may change.
🏢 **Office example:** Calling "Accounting" from the directory instead of memorizing the extension.

### ❌ C
> **C.** Configure the IP of the database as custom metadata for each instance, and query the metadata server.

**Wrong words:**
- ❌ "**custom metadata for each instance**": you'd still update **every instance** when the IP changes.

📌 **When to use it:** Use metadata for per-VM settings.
🏢 **Office example:** Writing the extension on every desk's sticky note.

### ❌ D
> **D.** Query the Compute Engine internal DNS from the applications to retrieve the IP of the database.

**Wrong words:**
- ❌ "**Compute Engine internal DNS**": it only has names for your **VMs**, not the on-prem database.

📌 **When to use it:** Use it to reach other VMs by name.
🏢 **Office example:** Looking up an outside supplier in the staff directory.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud dns managed-zones create corp-internal --dns-name=corp.internal. --visibility=private --networks=shop-vpc
gcloud dns record-sets create erp-db.corp.internal. --zone=corp-internal --type=A --ttl=300 --rrdatas=192.168.10.5
```
All ShopNow services connect to `erp-db.corp.internal:5432`.

---

## 🧠 Key Takeaways / Memory Tips

- **Address may change → use a DNS name** (Cloud DNS private zone).
  🧠 *"**Call the name, not the number.**"*
- Related: **Q091** (VPN), **Q063**.

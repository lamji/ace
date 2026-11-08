# Q202: VMs With Only Internal IPs Must Read a Cloud Storage File (Enable Private Google Access on the Subnet)

**Topic:** Networking (Private Google Access)

## ❓ Question
> You have an application that runs on Compute Engine VM instances in a custom Virtual Private Cloud (VPC). Your company's security policies only allow the use of internal IP addresses on VM instances and do not let VM instances connect to the internet. You need to ensure that the application can access a file hosted in a Cloud Storage bucket within your project. What should you do?
>
> **A.** Enable Private Service Access on the Cloud Storage Bucket.
>
> **B.** Add storage.googleapis.com to the list of restricted services in a VPC Service Controls perimeter and add your project to the list of protected projects.
>
> **C.** Enable Private Google Access on the subnet within the custom VPC.
>
> **D.** Deploy a Cloud NAT instance and route the traffic to the dedicated IP address of the Cloud Storage bucket.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs on VMs in a custom VPC. Security rules allow only internal IPs and no internet access.
- **What you must achieve:** Let the app read a file in a Cloud Storage bucket in your project.
- **The limits:** No external IPs and no internet.
- **What they're really asking:** How can VMs reach Cloud Storage without internet access?

**Clues in the question:**
- "**only allow … internal IP addresses**" + "**do not let VM instances connect to the internet**" + "**access … Cloud Storage**" → **Private Google Access** on the subnet.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Private Google Access 🔑
- **What it is:** A **subnet setting** that lets VMs with only internal IPs reach Google APIs (Cloud Storage, BigQuery…) without internet access.
- **Looks like:** `gcloud compute networks subnets update app --region=us-central1 --enable-private-ip-google-access`
- **Not to be confused with:** Cloud NAT (internet).
- **Analogy:** 🚪 A private corridor from your office to the Google building, without going outside.
- **In the online store:** Private VMs read product images.

### 2. Private Service Access
- **What it is:** A private connection to **Google-managed services in a peered network** (like Cloud SQL private IP). Not for buckets.
- **Looks like:** —
- **Not to be confused with:** Private Google Access.
- **Analogy:** 🔌 A dedicated cable to a partner's office.
- **In the online store:** Cloud SQL private IP.

### 🔗 How they fit together
```
 VM 10.0.1.5 (no external IP) ─ subnet [Private Google Access ON] ─► storage.googleapis.com ✅
```

---

## 🌍 Real-World Scenario

A bank's VMs have no internet route. The admin enables **Private Google Access** on the subnet, and the app reads its config file from Cloud Storage over Google's network.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Private Service Access on the Cloud Storage Bucket.

**Wrong words:**
- ❌ "**Private Service Access on the Cloud Storage Bucket**": that feature is for peered managed services like Cloud SQL, and it isn't set on buckets.

📌 **When to use it:** Use it to give Cloud SQL or Memorystore a private IP.
🏢 **Office example:** A cable to the wrong partner.

### ❌ B
> **B.** Add storage.googleapis.com to the list of restricted services in a VPC Service Controls perimeter and add your project to the list of protected projects.

**Wrong words:**
- ❌ "**VPC Service Controls perimeter**": restricts where data can go. It doesn't give private VMs a route to Cloud Storage.

📌 **When to use it:** Use it to stop data leaving a trusted boundary.
🏢 **Office example:** A security fence; it doesn't build the corridor.

### ✅ C
> **C.** Enable Private Google Access on the subnet within the custom VPC.

**Why it's correct:**
- ✔️ "**Enable Private Google Access on the subnet**" matches "**only allow the use of internal IP addresses**" + "**do not let VM instances connect to the internet**".
- ✔️ It reaches Google APIs, which matches "**access a file hosted in a Cloud Storage bucket**".

📌 **When to use it:** Use it when private machines must use Google services without any internet access.
🏢 **Office example:** A private corridor to the Google building so staff never step outside.

### ❌ D
> **D.** Deploy a Cloud NAT instance and route the traffic to the dedicated IP address of the Cloud Storage bucket.

**Wrong words:**
- ❌ "**Cloud NAT**": gives internet access, which the policy forbids.
- ❌ "**dedicated IP address of the Cloud Storage bucket**": buckets don't have dedicated IPs.

📌 **When to use it:** Use Cloud NAT when private VMs may reach the internet.
🏢 **Office example:** Opening a door to the street when the rules say no.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute networks subnets update backend --region=us-central1 --enable-private-ip-google-access` → private order workers read `gs://shopnow-config/app.yaml`.

---

## 🧠 Key Takeaways / Memory Tips

- **Internal-only VMs → Google APIs: Private Google Access (subnet setting).** NAT = internet.
  🧠 *"**Private VM, Google API → Private Google Access.**"*
- Related: **Q142**, **Q162**.

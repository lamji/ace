# Q063: On-Premises Servers With No Internet Reaching Cloud Storage (Private Google Access for On-Premises)

**Topic:** Hybrid networking (Cloud VPN / Interconnect, Cloud Router custom route advertisement, Private Google Access for on-premises hosts, restricted.googleapis.com, DNS CNAME)

## ❓ Question
> You are hosting an application on bare-metal servers in your own data center. The application needs access to Cloud Storage. However, security policies prevent the servers hosting the application from having public IP addresses or access to the internet. You want to follow Google-recommended practices to provide the application with access to Cloud Storage. What should you do?
>
> **A.** 1. Use nslookup to get the IP address for storage.googleapis.com. 2. Negotiate with the security team to be able to give a public IP address to the servers. 3. Only allow egress traffic from those servers to the IP addresses for storage.googleapis.com.
>
> **B.** 1. Using Cloud VPN, create a VPN tunnel to a Virtual Private Cloud (VPC) in Google Cloud. 2. In this VPC, create a Compute Engine instance and install the Squid proxy server on this instance. 3. Configure your servers to use that instance as a proxy to access Cloud Storage.
>
> **C.** 1. Use Migrate for Compute Engine (formerly known as Velostrata) to migrate those servers to Compute Engine. 2. Create an internal load balancer (ILB) that uses storage.googleapis.com as backend. 3. Configure your new instances to use this ILB as proxy.
>
> **D.** 1. Using Cloud VPN or Interconnect, create a tunnel to a VPC in Google Cloud. 2. Use Cloud Router to create a custom route advertisement for 199.36.153.4/30. Announce that network to your on-premises network through the VPN tunnel. 3. In your on-premises network, configure your DNS server to resolve *.googleapis.com as a CNAME to restricted.googleapis.com.

**My answer:** B
**Correct answer:** D
**Result:** ❌ Incorrect

> Why B was tempting: it also uses a VPN tunnel and keeps the servers off the internet, so it **works**. But it adds a **proxy VM you must build, patch and keep running**, and that VM itself needs a way out to Google APIs. Google has a **built-in** feature for exactly this case (D), so D is the "Google-recommended practice".

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs on bare-metal servers (physical machines) in your own data center and needs Cloud Storage.
- **What you must achieve:** Let the app reach Cloud Storage.
- **The limits:** The servers may not have public IP addresses or internet access; follow Google's recommended practice.
- **What they're really asking:** How do you connect your own servers to Google's services without using the internet?

| Question words | What they point to |
|---|---|
| "**bare-metal servers in your own data center**" | **On-premises** → you need a private link to Google: **Cloud VPN or Interconnect** |
| "**needs access to Cloud Storage**" | Reach the Google API `storage.googleapis.com` |
| "**prevent … public IP addresses or access to the internet**" | Must go through the **private link**, not the internet → A is out |
| "**Google-recommended practices**" | Use the built-in feature (**Private Google Access for on-premises hosts**), not a hand-built proxy (B) or a migration (C) |

**Exam topic:** Hybrid networking / Private Google Access.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud VPN / Cloud Interconnect
- **What it is:** Ways to connect **your own data center** to a **VPC** privately. **VPN** = an encrypted tunnel over the internet connection of your **router** (the servers themselves still have no internet). **Interconnect** = a dedicated physical line to Google.
- **Looks like:** `office-router ⇄ (IPsec tunnel) ⇄ Cloud VPN gateway → shop-vpc`
- **Not to be confused with:** giving the servers internet access. Only the edge router talks to Google, and the traffic is encrypted.
- **Analogy:** 🚇 A **private tunnel** from your building to Google's building.
- **In the online store:** The warehouse system in ShopNow's office reaches Google Cloud through the tunnel.

### 2️⃣ Cloud Router + custom route advertisement 🔑
- **What it is:** **Cloud Router** tells your on-premises router (using BGP) **which IP ranges are reachable through the tunnel**. A **custom advertisement** lets you add extra ranges, here **199.36.153.4/30**, the address of Google's private API endpoint.
- **Looks like:**
  ```bash
  gcloud compute routers update shop-router --region=us-central1 \
    --advertisement-mode=custom --set-advertisement-groups=all_subnets \
    --set-advertisement-ranges=199.36.153.4/30
  ```
- **Not to be confused with:** a firewall rule. It's a **directions sign**: "to reach 199.36.153.4–7, go through the tunnel."
- **Analogy:** 🪧 Posting a sign in your building: "**For Google's storage office, take the private tunnel.**"
- **In the online store:** ShopNow's office router learns that Google APIs are reachable through the VPN.

### 3️⃣ restricted.googleapis.com (199.36.153.4/30) 🔑
- **What it is:** A special Google API address range (4 IPs: 199.36.153.4–.7) that serves Google APIs like Cloud Storage **privately**, without the public internet, and works with VPC Service Controls. *(Its sibling `private.googleapis.com` is 199.36.153.8/30.)*
- **Looks like:** `restricted.googleapis.com → 199.36.153.4, .5, .6, .7`
- **Not to be confused with:** the normal public address of `storage.googleapis.com`, which is reached over the internet.
- **Analogy:** 🚪 Google's **staff-only back door** for the storage office, reachable only through the tunnel.

### 4️⃣ DNS CNAME
- **What it is:** A DNS record that says "**this name is really that other name**". Here: `*.googleapis.com` → `restricted.googleapis.com`, so when the app looks up `storage.googleapis.com` it gets the **private** 199.36.153.x address.
- **Looks like:**
  ```
  *.googleapis.com.          CNAME  restricted.googleapis.com.
  restricted.googleapis.com. A      199.36.153.4 (… .5 .6 .7)
  ```
- **Not to be confused with:** changing the app. The app still calls `storage.googleapis.com`; DNS quietly sends it to the private address.
- **Analogy:** 📇 The **office phone directory** says "for Storage Dept, dial the internal back-door extension".

### 5️⃣ Squid proxy
- **What it is:** A **proxy program** you install on a VM. Your servers send their requests to it, and it forwards them on.
- **Not to be confused with:** a managed Google feature. You build, patch, scale and monitor it yourself.
- **Analogy:** 🧍 Hiring a **runner** who carries every request to the storage office for you.

### 6️⃣ Migrate for Compute Engine
- **What it is:** A tool that **moves your servers into Google Cloud** as VMs.
- **Not to be confused with:** a networking fix. It changes **where** the app runs, which the question never asked for.

### 🔗 How they fit together (D)
```
 Your data center (no internet)                              Google Cloud
 ┌────────────────────────────────┐                          ┌─────────────────────────┐
 │ App server                      │                          │ VPC                      │
 │  1. DNS: storage.googleapis.com │                          │  Cloud Router advertises │
 │     → CNAME restricted.         │  Cloud VPN / Interconnect│  199.36.153.4/30 ────────┼──► ☁️ Cloud Storage
 │     → 199.36.153.4              │ ═══════════════════════► │                          │    (private API endpoint)
 │  2. Route: 199.36.153.4/30      │                          └─────────────────────────┘
 │     → via VPN (learned from     │
 │       Cloud Router)             │
 └────────────────────────────────┘
 No public IP. No internet. No proxy VM. ✅
```

---

## 🌍 Real-World Scenario

Banks, hospitals and government offices often have servers that are **never allowed on the internet**. When they start using Cloud Storage for backups or files, the network team sets up **Private Google Access for on-premises hosts**: a VPN or Interconnect to Google, Cloud Router advertising the private API range, and an on-prem DNS change. The servers then reach Cloud Storage as if it were inside the company network, with nothing extra to run.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Use nslookup to get the IP address for storage.googleapis.com. 2. Negotiate with the security team to be able to give a public IP address to the servers. 3. Only allow egress traffic from those servers to the IP addresses for storage.googleapis.com.

**Wrong words:**
- ❌ "**give a public IP address to the servers**": the security policy **forbids** public IPs and internet access. This breaks the main rule of the question.
- ❌ "**Use nslookup to get the IP address for storage.googleapis.com**": Google's public API IPs **change often**, so a fixed allowlist would break.

📌 **When to use it:** **Never use this** when the policy forbids internet access. Use D.
🏢 **Office example:** Asking security to let the records clerk walk out the front door, just to the storage company's address.

### ❌ B (your answer)
> **B.** 1. Using Cloud VPN, create a VPN tunnel to a Virtual Private Cloud (VPC) in Google Cloud. 2. In this VPC, create a Compute Engine instance and install the Squid proxy server on this instance. 3. Configure your servers to use that instance as a proxy to access Cloud Storage.

**Wrong words:**
- ✔️ "**Using Cloud VPN, create a VPN tunnel to a Virtual Private Cloud (VPC)**" is right. D does this too.
- ❌ "**create a Compute Engine instance and install the Squid proxy server**": an extra VM you must build, patch, monitor and scale. If it crashes, **all** Cloud Storage access stops (single point of failure).
- ❌ "**Configure your servers to use that instance as a proxy**": every server and app must be reconfigured to use a proxy. Google already offers a **built-in** private path to its APIs, so a hand-built proxy is **not** the Google-recommended practice.

📌 **When to use it:** Use a proxy only when you must inspect or log every request yourself, or when no built-in private path exists.
🏢 **Office example:** Hiring a runner to carry every document through the tunnel, when the tunnel already has a staff-only door straight into the storage office.

### ❌ C
> **C.** 1. Use Migrate for Compute Engine (formerly known as Velostrata) to migrate those servers to Compute Engine. 2. Create an internal load balancer (ILB) that uses storage.googleapis.com as backend. 3. Configure your new instances to use this ILB as proxy.

**Wrong words:**
- ❌ "**migrate those servers to Compute Engine**": the question is about servers **staying** in your data center. Moving everything is a huge project nobody asked for.
- ❌ "**internal load balancer (ILB) that uses storage.googleapis.com as backend**": an ILB's backends are your own VMs/instance groups. You can't put a Google API behind it like this.

📌 **When to use it:** Use Migrate for Compute Engine when you've decided to **move** your servers into Google Cloud.
🏢 **Office example:** Moving the whole department to a new building just because they needed access to one filing room.

### ✅ D (correct answer)
> **D.** 1. Using Cloud VPN or Interconnect, create a tunnel to a VPC in Google Cloud. 2. Use Cloud Router to create a custom route advertisement for 199.36.153.4/30. Announce that network to your on-premises network through the VPN tunnel. 3. In your on-premises network, configure your DNS server to resolve *.googleapis.com as a CNAME to restricted.googleapis.com.

**Why it's correct:**

- ✔️ "**Using Cloud VPN or Interconnect, create a tunnel to a VPC**" matches "**your own data center**", "**prevent … access to the internet**": A private, encrypted link. The servers never touch the internet.
- ✔️ "**Cloud Router … custom route advertisement for 199.36.153.4/30**" matches "**needs access to Cloud Storage**": Tells your network that Google's **private API address** is reachable **through the tunnel**.
- ✔️ "**configure your DNS server to resolve *.googleapis.com as a CNAME to restricted.googleapis.com**" matches "**application** needs access to Cloud Storage": The app keeps calling `storage.googleapis.com`; DNS sends it to the private address. **No app changes.**
- ✔️ All built-in, no extra servers matches "**Google-recommended practices**": This is Google's documented setup: **Private Google Access for on-premises hosts**.

📌 **When to use it:** Use it when servers in your own building must reach Google services but are never allowed on the internet.
🏢 **Office example:** A private tunnel to the partner building, a sign saying "Storage Dept: take the tunnel", and the phone directory pointing to the staff-only back door.

---

## ⚖️ B vs D: The Difference

| | **B** (Squid proxy) | **D** (Private Google Access) |
|---|---|---|
| Tunnel to Google | ✅ Cloud VPN | ✅ Cloud VPN or Interconnect |
| How traffic reaches Cloud Storage | Servers → **proxy VM** → Cloud Storage | Servers → **directly** to Google's private API address |
| Extra things to run | A VM + Squid software (patching, scaling, monitoring) | **Nothing.** Just a route + a DNS record |
| If something breaks | Proxy VM down = **no access** | Managed by Google, no single VM to fail |
| App changes | Every server must be set to use a proxy | None, DNS handles it |
| Google-recommended? | ❌ workaround | ✅ documented best practice |

Both keep the servers off the internet. **D does it with built-in features; B adds a server you have to babysit.**

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **warehouse inventory system** runs in its own office data center with no internet. It must upload daily stock files to `gs://shopnow-inventory`.

```bash
# 1. Tunnel already exists: office router ⇄ Cloud VPN ⇄ shop-vpc

# 2. Advertise Google's private API range to the office
gcloud compute routers update shop-router --region=us-central1 \
  --advertisement-mode=custom --set-advertisement-groups=all_subnets \
  --set-advertisement-ranges=199.36.153.4/30

# 3. Office DNS server (e.g., BIND zone for googleapis.com)
#   *.googleapis.com.          CNAME  restricted.googleapis.com.
#   restricted.googleapis.com. A      199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7
```

The warehouse app keeps running `gsutil cp stock.csv gs://shopnow-inventory/`. Unchanged, and it now travels privately through the tunnel.

---

## 🧠 Key Takeaways / Memory Tips

- **On-prem + no internet + Google APIs → VPN/Interconnect + Cloud Router advertises 199.36.153.4/30 + DNS CNAME to restricted.googleapis.com.**
- **199.36.153.4/30 = restricted.googleapis.com** (199.36.153.8/30 = private.googleapis.com).
- **Proxy VMs, public IPs and migrations are never the "Google-recommended" answer** when a built-in path exists.
  🧠 *"**Tunnel + sign + directory**: VPN (tunnel), Cloud Router (sign to 199.36.153.4), DNS CNAME (directory)."*
- Related: **Q054** (VPN connects separate networks), **Q060** (VPC peering / private access).

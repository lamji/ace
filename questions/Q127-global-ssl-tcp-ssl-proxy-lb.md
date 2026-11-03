# Q127: Global Clients, SSL-Encrypted TCP on 443, Lowest Latency (SSL Proxy Load Balancer)

**Topic:** Load balancing (SSL Proxy, HTTPS LB, Network LB, Internal TCP/UDP LB)

## ❓ Question
> You have an application that receives SSL-encrypted TCP traffic on port 443. Clients for this application are located all over the world. You want to minimize latency for the clients. Which load balancing option should you use?
>
> **A.** HTTPS Load Balancer
>
> **B.** Network Load Balancer
>
> **C.** SSL Proxy Load Balancer
>
> **D.** Internal TCP/UDP Load Balancer. Add a firewall rule allowing ingress traffic from 0.0.0.0/0 on the target instances.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** Today this is part of the **global external proxy Network Load Balancer**. The exam still uses the name "SSL Proxy Load Balancer".

---

## 📖 What the Question Is Asking

**In plain words:** Your app receives **SSL-encrypted TCP** (not HTTP) on port 443, from users **all over the world**. Which load balancer gives them the **lowest latency**?

**Clues in the question:**
- "**SSL-encrypted TCP traffic**": it's TCP with SSL, **not HTTP(S)** → the HTTPS LB doesn't fit.
- "**all over the world**" + "**minimize latency**": a **global** proxy that ends SSL at Google's edge near each user → **SSL Proxy**.
- Network LB is **regional** and passes traffic through. Internal LB is private only.

**Exam topic:** Networking / load balancing.

---

## 📚 Key Terms Explained

### 1. SSL Proxy Load Balancer 🔑
- **What it is:** A **global** external load balancer for **non-HTTP TCP traffic with SSL/TLS**. It ends the SSL connection at the **Google edge closest to the user**, then sends traffic over Google's network to the nearest healthy backend.
- **Looks like:** `gcloud compute target-ssl-proxies create ...` (frontend port 443)
- **Not to be confused with:** the HTTPS LB, which is for web (HTTP) traffic.
- **Analogy:** 🌍 A **local reception desk in every city** that receives sealed mail and forwards it fast through the company's private courier.
- **In the online store:** A secure TCP API for partner warehouses worldwide.

### 2. HTTPS Load Balancer (review from Q078)
- **What it is:** Global LB for **HTTP/HTTPS** (web) traffic, with URL rules.
- **Looks like:** Ingress / URL map
- **Not to be confused with:** TCP-only protocols.
- **Analogy:** 🛎️ A reception for web visitors.
- **In the online store:** The storefront website.

### 3. Network Load Balancer
- **What it is:** A **regional**, pass-through TCP/UDP balancer. Clients connect to one region.
- **Looks like:** forwarding rule + target pool / backend service
- **Not to be confused with:** a global proxy.
- **Analogy:** 📮 One post office in one city.
- **In the online store:** Game servers in one region.

### 4. Internal TCP/UDP LB
- **What it is:** A **private** load balancer, reachable only inside your VPC.
- **Looks like:** `--load-balancing-scheme=INTERNAL`
- **Not to be confused with:** something internet clients can reach.
- **Analogy:** ☎️ An internal extension.
- **In the online store:** Internal inventory API.

### 🔗 How they fit together
```
 client (Tokyo) ─SSL─► Google edge Tokyo (SSL ends here) ─► Google network ─► nearest backend ✅
 client (Paris) ─SSL─► Google edge Paris ─────────────────► nearest backend ✅
```

---

## 🌍 Real-World Scenario

A company runs a secure, custom TCP protocol (not a website) on port 443 for customers worldwide. They put an **SSL Proxy Load Balancer** in front. Users connect to the nearest Google edge, where SSL is handled, and traffic rides Google's fast network to backends in the US, EU and Asia.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** HTTPS Load Balancer

**Wrong words:**
- ❌ "**HTTPS Load Balancer**": built for **HTTP(S)** web requests. The question's traffic is plain **SSL-encrypted TCP**, not HTTP.

📌 **When to use it:** Use it for websites and HTTP APIs.
🏢 **Office example:** A web-visitor reception desk handling sealed courier crates.

### ❌ B
> **B.** Network Load Balancer

**Wrong words:**
- ❌ "**Network Load Balancer**": **regional** and pass-through. Faraway clients travel the public internet to one region, which means more latency.

📌 **When to use it:** Use it for TCP/UDP traffic served from one region, when you need to keep the client's IP.
🏢 **Office example:** One post office in one city serving the whole world.

### ✅ C
> **C.** SSL Proxy Load Balancer

**Why it's correct:**
- ✔️ "**SSL Proxy**" matches "**SSL-encrypted TCP traffic on port 443**": it's made for SSL over TCP (not HTTP).
- ✔️ "**SSL Proxy Load Balancer**" (global, ends SSL at the edge) matches "**Clients … all over the world**" + "**minimize latency**": users connect to the nearest Google edge.

📌 **When to use it:** Use it when secure non-web traffic comes from everywhere and should be answered close to each user.
🏢 **Office example:** A reception desk in every city that takes sealed mail and forwards it by the company's fast private courier.

### ❌ D
> **D.** Internal TCP/UDP Load Balancer. Add a firewall rule allowing ingress traffic from 0.0.0.0/0 on the target instances.

**Wrong words:**
- ❌ "**Internal TCP/UDP Load Balancer**": private, inside the VPC only. Internet clients can't reach it.
- ❌ "**firewall rule allowing ingress traffic from 0.0.0.0/0**": opening the firewall doesn't make an internal LB public.

📌 **When to use it:** Use it for private services that only your own VMs call.
🏢 **Office example:** Publishing an internal phone extension to the world and opening the doors.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's warehouse partners connect to a TLS-secured TCP inventory feed on port 443 from 30 countries. ShopNow deploys an **SSL Proxy LB** with backends in `us-central1`, `europe-west1` and `asia-east1`. A partner in Singapore connects to Google's Singapore edge and is served by `asia-east1`.

---

## 🧠 Key Takeaways / Memory Tips

- **Global + SSL TCP (not HTTP) → SSL Proxy LB.** Global + plain TCP → TCP Proxy. Web → HTTPS LB.
- Network LB = regional. Internal LB = private.
  🧠 *"**SSL but not HTTP, worldwide → SSL Proxy.**"*
- Related: **Q078** (Ingress/HTTPS LB), **Q060** (internal LB), **Q040** (HTTPS LB).

# Q274: Secure, Highly Available Web App on a MIG (HTTP(S) Load Balancing + A Record in a Public DNS Zone)

**Topic:** Load balancing + Cloud DNS

## ❓ Question
> You are deploying a web application using Compute Engine. You created a managed instance group (MIG) to host the application. You want to follow Google-recommended practices to implement a secure and highly available solution. What should you do?
>
> **A.** Use SSL proxy load balancing for the MIG and an A record in your DNS private zone with the load balancer's IP address.
>
> **B.** Use SSL proxy load balancing for the MIG and a CNAME record in your DNS public zone with the load balancer's IP address.
>
> **C.** Use HTTP(S) load balancing for the MIG and a CNAME record in your DNS private zone with the load balancer's IP address.
>
> **D.** Use HTTP(S) load balancing for the MIG and an A record in your DNS public zone with the load balancer's IP address.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A web app runs in a managed instance group on Compute Engine.
- **What you must achieve:** Make it secure and highly available.
- **The limits:** Follow Google-recommended practices.
- **What they're really asking:** What should you put in front of the group and how should the group be spread?

**Clues in the question:**
- "**web application**" + "**secure**" → **HTTP(S) load balancing**.
- Name → **IP** = **A record** (CNAME points to names).
- Public users → **public zone**.

**Exam topic:** Load balancing.

---

## 📚 Key Terms Explained

### 1. HTTP(S) LB 🔑 (review from Q263)
- **What it is:** Global layer-7 LB with TLS, URL routing, Cloud Armor and CDN.
- **Looks like:** —
- **Not to be confused with:** SSL Proxy (non-HTTP).
- **Analogy:** 🛎️ Web reception desk.
- **In the online store:** Storefront.

### 2. A record in public zone (review from Q205)
- **What it is:** Maps a public name to an IP.
- **Looks like:** `shop.com. A 34.120.10.5`
- **Not to be confused with:** CNAME, private zone.
- **Analogy:** 📇 Public directory entry.
- **In the online store:** —

### 🔗 How they fit together
```
 shop.com A 34.120.10.5 (public zone) → HTTPS LB → MIG ✅
```

---

## 🌍 Real-World Scenario

A store puts its MIG behind an **HTTPS load balancer** and adds an **A record** in its **public** Cloud DNS zone pointing to the LB's IP.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use SSL proxy load balancing for the MIG and an A record in your DNS private zone with the load balancer's IP address.

**Wrong words:**
- ❌ "**SSL proxy load balancing**": for non-HTTP TLS traffic, not web apps.
- ❌ "**DNS private zone**": internet users can't resolve it.

📌 **When to use it:** Use SSL Proxy for encrypted non-web protocols.
🏢 **Office example:** A courier desk for a web shop, listed in the internal directory.

### ❌ B
> **B.** Use SSL proxy load balancing for the MIG and a CNAME record in your DNS public zone with the load balancer's IP address.

**Wrong words:**
- ❌ "**SSL proxy**" and ❌ "**CNAME record … with the load balancer's IP address**": a CNAME can't hold an IP.

📌 **When to use it:** Use CNAMEs to alias names.
🏢 **Office example:** Writing a phone number in the "see other entry" column.

### ❌ C
> **C.** Use HTTP(S) load balancing for the MIG and a CNAME record in your DNS private zone with the load balancer's IP address.

**Wrong words:**
- ✔️ HTTP(S) LB is right.
- ❌ "**CNAME … with the load balancer's IP**" and ❌ "**private zone**".

📌 **When to use it:** Use private zones for internal names.
🏢 **Office example:** The right desk, but listed wrongly in the internal directory.

### ✅ D
> **D.** Use HTTP(S) load balancing for the MIG and an A record in your DNS public zone with the load balancer's IP address.

**Why it's correct:**
- ✔️ "**HTTP(S) load balancing for the MIG**" matches "**web application**" + "**secure and highly available**".
- ✔️ "**A record in your DNS public zone with the load balancer's IP address**": A records hold IPs and public zones are reachable by users.

📌 **When to use it:** Use it when a public website runs on a group of servers and needs a name people can type.
🏢 **Office example:** A public directory entry with the reception's number, and a receptionist who spreads visitors across staff.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud dns record-sets create shopnow.com. --zone=shopnow-public --type=A --ttl=300 --rrdatas=34.120.10.5`

---

## 🧠 Key Takeaways / Memory Tips

- **Web app → HTTP(S) LB. Name → IP → A record. Public users → public zone.**
  🧠 *"**Web LB + public A record.**"*
- Related: **Q205**, **Q263**.

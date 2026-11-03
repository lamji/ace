# Q198: Expose TCP Port 389 and Keep the Client's IP (External TCP Network Load Balancer)

**Topic:** Load balancing (pass-through vs proxy)

## ❓ Question
> You deployed an application on a managed instance group in Compute Engine. The application accepts Transmission Control Protocol (TCP) traffic on port 389 and requires you to preserve the IP address of the client who is making a request. You want to expose the application to the internet by using a load balancer. What should you do?
>
> **A.** Expose the application by using an external TCP Network Load Balancer.
>
> **B.** Expose the application by using a TCP Proxy Load Balancer.
>
> **C.** Expose the application by using an SSL Proxy Load Balancer.
>
> **D.** Expose the application by using an internal TCP Network Load Balancer.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** TCP **389** (LDAP), from the **internet**, and the app must see the **real client IP**.

**Clues in the question:**
- "**preserve the IP address of the client**" → a **pass-through** LB (Network LB). Proxy LBs replace the source IP with their own.
- "**to the internet**" → **external**.

**Exam topic:** Load balancing.

---

## 📚 Key Terms Explained

### 1. Pass-through vs proxy LB 🔑
- **What it is:** **Pass-through** (Network LB) forwards packets unchanged, so the backend sees the client IP. **Proxy** (TCP/SSL Proxy, HTTP(S)) opens a new connection, so the backend sees the proxy's IP.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 📮 Forwarding the original envelope vs re-addressing it.
- **In the online store:** Fraud checks need the real IP.

### 2. TCP port 389
- **What it is:** The standard port for **LDAP** (directory login services).
- **Looks like:** `ldap://dir.shop.com:389`
- **Not to be confused with:** —
- **Analogy:** 📇 The staff directory line.
- **In the online store:** —

### 🔗 How they fit together
```
 client 203.0.113.7 ─► External Network LB (pass-through) ─► MIG VM sees 203.0.113.7 ✅
```

---

## 🌍 Real-World Scenario

A directory service must log each client's real IP. The team uses an **external TCP Network LB** so packets arrive with the original source address.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Expose the application by using an external TCP Network Load Balancer.

**Why it's correct:**
- ✔️ "**external**" matches "**expose the application to the internet**".
- ✔️ "**TCP Network Load Balancer**" (pass-through) matches "**preserve the IP address of the client**" and supports any TCP port like 389.

📌 **When to use it:** Use it when outside users connect and the servers must know exactly who is calling.
🏢 **Office example:** Forwarding the visitor's original envelope so the department sees the real return address.

### ❌ B
> **B.** Expose the application by using a TCP Proxy Load Balancer.

**Wrong words:**
- ❌ "**TCP Proxy**": it terminates connections, so the backend sees the proxy's IP (and port 389 isn't one of its supported ports).

📌 **When to use it:** Use it for global TCP traffic when the real client IP isn't needed.
🏢 **Office example:** A mailroom that re-addresses every letter.

### ❌ C
> **C.** Expose the application by using an SSL Proxy Load Balancer.

**Wrong words:**
- ❌ "**SSL Proxy**": for SSL traffic, and also hides the client IP.

📌 **When to use it:** Use it for encrypted non-web traffic globally.
🏢 **Office example:** A courier who repacks every package.

### ❌ D
> **D.** Expose the application by using an internal TCP Network Load Balancer.

**Wrong words:**
- ❌ "**internal**": not reachable from the internet.

📌 **When to use it:** Use it for traffic between your own VMs.
🏢 **Office example:** An internal mailroom the public can't reach.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's partner LDAP endpoint: forwarding rule `ldap-fr` (EXTERNAL, TCP 389) → backend service on MIG `ldap-mig`. Logs show partner IPs.

---

## 🧠 Key Takeaways / Memory Tips

- **Keep client IP + external → External Network (pass-through) LB.** Proxies hide the client IP.
  🧠 *"**Pass-through passes the IP through.**"*
- Related: **Q167**, **Q127**.

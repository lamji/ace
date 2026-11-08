# Q167: Mobile Game Sends UDP Over the Internet to Many VMs Behind One IP (External Network Load Balancer)

**Topic:** Load balancing (UDP support, external network LB, SSL proxy, HTTP(S))

## ❓ Question
> Your company developed a mobile game that is deployed on Google Cloud. Gamers are connecting to the game with their personal phones over the Internet. The game sends UDP packets to update the servers about the gamers' actions while they are playing in multiplayer mode. Your game backend can scale over multiple virtual machines (VMs), and you want to expose the VMs over a single IP address. What should you do?
>
> **A.** Configure an SSL Proxy load balancer in front of the application servers.
>
> **B.** Configure an Internal UDP load balancer in front of the application servers.
>
> **C.** Configure an External HTTP(s) load balancer in front of the application servers.
>
> **D.** Configure an External Network load balancer in front of the application servers.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A mobile multiplayer game sends UDP packets (a fast, connectionless type of network traffic) from players' phones over the internet. The game servers run on several VMs.
- **What you must achieve:** Put all the game VMs behind one single IP address.
- **The limits:** The traffic is UDP.
- **What they're really asking:** Which load balancer can spread UDP game traffic across VMs behind one IP?

**Clues in the question:**
- "**UDP packets**": only the **network (pass-through) load balancer** handles UDP. SSL Proxy and HTTP(S) are TCP/HTTP only.
- "**over the Internet**": **external**, not internal.

**Exam topic:** Load balancing.

---

## 📚 Key Terms Explained

### 1. External Network Load Balancer 🔑
- **What it is:** A **regional, pass-through** load balancer for **TCP and UDP** with one external IP.
- **Looks like:** forwarding rule `--ip-protocol=UDP --ports=7777`
- **Not to be confused with:** proxy LBs (TCP/HTTP only).
- **Analogy:** 📮 A post office that forwards every packet type.
- **In the online store:** Real-time game or VoIP traffic.

### 2. Which LB handles what
- **What it is:** HTTP(S) → web. SSL/TCP Proxy → encrypted or plain TCP, global. Network LB → TCP/UDP, regional. Internal → private.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🗺️ A map of which door takes which visitors.
- **In the online store:** —

### 🔗 How they fit together
```
 phones ─UDP─► 34.x.x.x (External Network LB) ─► game-vm-1, game-vm-2, game-vm-3 ✅
```

---

## 🌍 Real-World Scenario

A multiplayer mobile game streams player moves over UDP. The studio puts an **External Network Load Balancer** with one public IP in front of its game server group.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure an SSL Proxy load balancer in front of the application servers.

**Wrong words:**
- ❌ "**SSL Proxy load balancer**": TCP with SSL only. It can't carry UDP.

📌 **When to use it:** Use it for global SSL/TCP traffic (Q127).
🏢 **Office example:** A courier desk that only accepts sealed envelopes, not loose packets.

### ❌ B
> **B.** Configure an Internal UDP load balancer in front of the application servers.

**Wrong words:**
- ❌ "**Internal UDP load balancer**": private only. Phones on the internet can't reach it.

📌 **When to use it:** Use it for UDP between your own VMs.
🏢 **Office example:** An internal mailroom that the public can't send to.

### ❌ C
> **C.** Configure an External HTTP(s) load balancer in front of the application servers.

**Wrong words:**
- ❌ "**External HTTP(s) load balancer**": web (HTTP) traffic only, not UDP.

📌 **When to use it:** Use it for websites and HTTP APIs.
🏢 **Office example:** A web reception desk for UDP packets.

### ✅ D
> **D.** Configure an External Network load balancer in front of the application servers.

**Why it's correct:**
- ✔️ "**External**" matches "**over the Internet**".
- ✔️ "**Network load balancer**" matches "**UDP packets**": it supports UDP.
- ✔️ It has one frontend IP, which matches "**expose the VMs over a single IP address**".

📌 **When to use it:** Use it when outside users send non-web traffic (like UDP) to a group of servers.
🏢 **Office example:** One public post office address that forwards every packet to whichever sorter is free.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's live-auction feature streams bid updates over UDP 9000: an External Network LB with IP `34.120.10.5` → MIG `auction-servers`.

---

## 🧠 Key Takeaways / Memory Tips

- **UDP from the internet → External Network LB.**
- HTTP(S)/SSL Proxy can't do UDP; internal = private.
  🧠 *"**UDP? Network LB.**"*
- Related: **Q127** (SSL Proxy), **Q078** (HTTPS LB), **Q060**.

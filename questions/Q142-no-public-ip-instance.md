# Q142: New VM Must Not Be Reachable From the Internet (Create It Without a Public IP)

**Topic:** VPC networking (external IPs, Private Google Access, firewall, VPN)

## ❓ Question
> Your company has workloads running on Compute Engine and on-premises. The Google Cloud Virtual Private Cloud (VPC) is connected to your WAN over a Virtual Private Network (VPN). You need to deploy a new Compute Engine instance and ensure that no public Internet traffic can be routed to it. What should you do?
>
> **A.** Create the instance without a public IP address.
>
> **B.** Create the instance with Private Google Access enabled.
>
> **C.** Create a deny-all egress firewall rule on the VPC network.
>
> **D.** Create a route on the VPC to route all traffic to the instance over the VPN tunnel.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The new VM must be **unreachable from the internet**, but still reachable from your offices over VPN.

**Clues in the question:**
- "**no public Internet traffic can be routed to it**": without an **external (public) IP**, the internet has no address to send traffic to.
- The VPN still reaches its **internal IP**.

**Exam topic:** VPC networking.

---

## 📚 Key Terms Explained

### 1. External (public) IP 🔑
- **What it is:** An internet-routable address on a VM. Without one, the VM has **only an internal IP**, which the internet can't reach.
- **Looks like:** `gcloud compute instances create db-2 --no-address`
- **Not to be confused with:** an internal IP.
- **Analogy:** 📞 A **public phone number** vs an internal extension only.
- **In the online store:** The orders DB VM has no public IP.

### 2. Private Google Access (review from Q063)
- **What it is:** Lets VMs **without** a public IP reach Google APIs. It doesn't block anything coming in.
- **Looks like:** `--enable-private-ip-google-access` on the subnet
- **Not to be confused with:** a security block.
- **Analogy:** 🚪 A private corridor to Google's offices.
- **In the online store:** VMs reach Cloud Storage privately.

### 🔗 How they fit together
```
 Internet ──✗── (no public IP: no address to reach)
 On-prem ──VPN──► 10.0.1.25 (internal IP) ✅
```

---

## 🌍 Real-World Scenario

A bank deploys an internal reporting server. They create it with `--no-address`. Branch offices reach it over VPN on its 10.x IP, and the internet can't reach it at all.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create the instance without a public IP address.

**Why it's correct:**
- ✔️ "**without a public IP address**" matches "**no public Internet traffic can be routed to it**": with no public address, internet traffic can't reach it.
- ✔️ It keeps an internal IP, so traffic from your WAN over the VPN still works.

📌 **When to use it:** Use it when a machine should be reachable only from inside your company network.
🏢 **Office example:** Giving a desk only an internal extension, with no public phone number.

### ❌ B
> **B.** Create the instance with Private Google Access enabled.

**Wrong words:**
- ❌ "**Private Google Access enabled**": it lets the VM **reach Google APIs** without a public IP. It doesn't block incoming internet traffic.

📌 **When to use it:** Use it so private VMs can reach Cloud Storage and other Google APIs.
🏢 **Office example:** A private corridor to Google's offices; it doesn't lock your front door.

### ❌ C
> **C.** Create a deny-all egress firewall rule on the VPC network.

**Wrong words:**
- ❌ "**deny-all egress firewall rule**": egress is **outgoing** traffic. The concern is **incoming** public traffic, and this would also break normal outbound use.

📌 **When to use it:** Use egress rules to control what VMs can connect out to.
🏢 **Office example:** Stopping staff from leaving when the worry is strangers coming in.

### ❌ D
> **D.** Create a route on the VPC to route all traffic to the instance over the VPN tunnel.

**Wrong words:**
- ❌ "**route all traffic to the instance over the VPN**": routes steer outgoing traffic. They don't stop the internet reaching a public IP.

📌 **When to use it:** Use custom routes to steer traffic to on-prem ranges.
🏢 **Office example:** Drawing a map when you need to remove the public phone number.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute instances create shop-reports-1 --zone=us-central1-a --subnet=private-subnet --no-address
```
Office staff open `http://10.0.5.12` over the VPN. From the internet, there's nothing to connect to.

---

## 🧠 Key Takeaways / Memory Tips

- **No internet traffic to a VM → no external IP.**
- Private Google Access = outgoing to Google APIs.
  🧠 *"**No public number, no public calls.**"*
- Related: **Q063** (Private Google Access), **Q091** (VPN).

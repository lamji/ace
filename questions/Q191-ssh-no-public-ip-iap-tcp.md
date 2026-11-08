# Q191: SSH to Many VMs Over the Internet Without Public IPs or Per-VM Setup (IAP for SSH and TCP)

**Topic:** Security (Identity-Aware Proxy TCP forwarding)

## ❓ Question
> You have deployed multiple Linux instances on Compute Engine. You plan on adding more instances in the coming weeks. You want to be able to access all of these instances through your SSH client over the internet without having to configure specific access on the existing and new instances. You do not want the Compute Engine instances to have a public IP. What should you do?
>
> **A.** Configure Cloud Identity-Aware Proxy for HTTPS resources.
>
> **B.** Configure Cloud Identity-Aware Proxy for SSH and TCP resources
>
> **C.** Create an SSH keypair and store the public key as a project-wide SSH Key.
>
> **D.** Create an SSH keypair and store the private key as a project-wide SSH Key.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You run several Linux VMs and will add more soon.
- **What you must achieve:** SSH into all of them from your own SSH client over the internet.
- **The limits:** No per-VM setup, and the VMs must not have public IPs.
- **What they're really asking:** How can you reach VMs without public IPs from the internet?

**Clues in the question:**
- "**do not want … a public IP**" + "**over the internet**" → **IAP TCP forwarding** tunnels SSH through Google to the VM's internal IP.
- "**without having to configure specific access on the existing and new instances**" → one firewall rule + IAM, not per-VM setup.

**Exam topic:** Security.

---

## 📚 Key Terms Explained

### 1. IAP TCP forwarding 🔑
- **What it is:** **Identity-Aware Proxy** checks who you are, then tunnels your SSH connection to a VM's **internal IP**. The VM needs no public IP.
- **Looks like:** `gcloud compute ssh web-1 --tunnel-through-iap` + firewall allow `35.235.240.0/20` tcp:22
- **Not to be confused with:** a VPN.
- **Analogy:** 🛂 A guarded entrance that walks verified visitors to internal rooms.
- **In the online store:** Engineers SSH to private ShopNow VMs.

### 2. Project-wide SSH key
- **What it is:** A **public** key stored in project metadata, so it works on all VMs. Doesn't help VMs without public IPs.
- **Looks like:** metadata `ssh-keys`
- **Not to be confused with:** IAP.
- **Analogy:** 🔑 One key that opens every door, but the doors are still unreachable.
- **In the online store:** —

### 🔗 How they fit together
```
 laptop ─SSH─► IAP (checks identity) ─► VM internal IP 10.0.0.5 ✅ (no public IP)
```

---

## 🌍 Real-World Scenario

A team removes all public IPs from its VMs. Engineers now connect with `gcloud compute ssh --tunnel-through-iap`. New VMs work automatically because the firewall rule and IAM role cover them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure Cloud Identity-Aware Proxy for HTTPS resources.

**Wrong words:**
- ❌ "**for HTTPS resources**": IAP for HTTPS protects web apps, not SSH connections.

📌 **When to use it:** Use it to put a login wall in front of an internal website.
🏢 **Office example:** A guard for the web reception, not the back corridor.

### ✅ B
> **B.** Configure Cloud Identity-Aware Proxy for SSH and TCP resources

**Why it's correct:**
- ✔️ "**Identity-Aware Proxy for SSH and TCP resources**" matches "**through your SSH client over the internet**" + "**do not want … a public IP**": IAP tunnels SSH to internal IPs.
- ✔️ Access is granted by IAM and one firewall rule, which matches "**without having to configure specific access on the existing and new instances**".

📌 **When to use it:** Use it when staff must reach internal machines from outside without exposing them publicly.
🏢 **Office example:** A guarded entrance that checks your ID and walks you to any internal room.

### ❌ C
> **C.** Create an SSH keypair and store the public key as a project-wide SSH Key.

**Wrong words:**
- ✔️ "public key as a project-wide SSH Key" works on all VMs.
- ❌ But the VMs have **no public IP**, so your SSH client can't reach them over the internet.

📌 **When to use it:** Use it when VMs are reachable and everyone should log in with the same key setup.
🏢 **Office example:** A key for every door in a building with no entrance.

### ❌ D
> **D.** Create an SSH keypair and store the private key as a project-wide SSH Key.

**Wrong words:**
- ❌ "**store the private key**": the private key must stay secret on your computer. Never upload it.

📌 **When to use it:** **Never use this.** Store only the public key.
🏢 **Office example:** Taping the master key to the front door.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute firewall-rules create allow-iap-ssh --network=shop-vpc --source-ranges=35.235.240.0/20 --allow=tcp:22
gcloud projects add-iam-policy-binding shopnow-prod --member=group:ops@shopnow.com --role=roles/iap.tunnelResourceAccessor
gcloud compute ssh orders-vm --tunnel-through-iap
```

---

## 🧠 Key Takeaways / Memory Tips

- **SSH without public IPs → IAP TCP forwarding.** (IAP for HTTPS = web apps.)
  🧠 *"**No public IP? Tunnel through IAP.**"*
- Related: **Q210**, **Q152**, **Q142**.

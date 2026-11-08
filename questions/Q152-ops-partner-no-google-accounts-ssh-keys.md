# Q152: Partner Without Google Accounts Must Maintain Linux VMs (Their Public SSH Keys on the VMs)

**Topic:** Compute Engine access (SSH keys in metadata, IAP TCP forwarding, OS Login)

## ❓ Question
> Your company runs its Linux workloads on Compute Engine instances. Your company will be working with a new operations partner that does not use Google Accounts. You need to grant access to the instances to your operations partner so they can maintain the installed tooling. What should you do?
>
> **A.** Enable Cloud IAP for the Compute Engine instances, and add the operations partner as a Cloud IAP Tunnel User.
>
> **B.** Tag all the instances with the same network tag. Create a firewall rule in the VPC to grant TCP access on port 22 for traffic from the operations partner to instances with the network tag.
>
> **C.** Set up Cloud VPN between your Google Cloud VPC and the internal network of the operations partner.
>
> **D.** Ask the operations partner to generate SSH key pairs, and add the public keys to the VM instances.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** This one is debated. Some pick **A (IAP)**, but IAP needs a **Google identity**, and the question says the partner **does not use Google Accounts**. That detail points to **D**. In practice you'd also need a firewall path for port 22. **If your site's Most Voted is A, tell me and I'll update it.**

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your Linux workloads run on Compute Engine VMs. A new operations partner will maintain the installed tools, but they do not use Google accounts.
- **What you must achieve:** Give the partner login access to the VMs.
- **The limits:** They have no Google accounts, so Google-account-based login won't work for them.
- **What they're really asking:** How do you give people without Google accounts access to your Linux VMs?

**Clues in the question:**
- "**does not use Google Accounts**": anything based on Google identity (IAP, OS Login, IAM) won't work for them.
- "**grant access to the instances**" for Linux maintenance → **SSH**. Without Google accounts, use **their own SSH key pairs**, adding the **public keys** to the VMs (metadata).

**Exam topic:** Compute Engine access.

---

## 📚 Key Terms Explained

### 1. SSH key pair 🔑
- **What it is:** A **private key** (kept secret by the user) and a **public key** (placed on the server). The server lets in whoever holds the matching private key.
- **Looks like:** `ssh-keygen -t ed25519 -f partner` → add `partner.pub` to instance metadata `ssh-keys`
- **Not to be confused with:** a password or a Google account.
- **Analogy:** 🔐 A **padlock you install** (public key) that only their key (private) opens.
- **In the online store:** Contractor access to a VM.

### 2. IAP TCP forwarding
- **What it is:** Lets users SSH to VMs **through Google** after IAM checks their **Google identity**.
- **Looks like:** `gcloud compute ssh vm-1 --tunnel-through-iap`
- **Not to be confused with:** something that works without Google accounts.
- **Analogy:** 🛂 A guard who checks Google badges.
- **In the online store:** ShopNow staff SSH without public IPs.

### 🔗 How they fit together
```
 partner generates key pair → sends PUBLIC key → you add it to VM metadata (ssh-keys) ✅
 partner: ssh -i partner_key ops@vm-ip   (no Google account needed)
```

---

## 🌍 Real-World Scenario

An outside managed-services company with no Google accounts must patch tools on Linux VMs. They generate SSH key pairs and send the **public keys**. The admin adds them to the instances' `ssh-keys` metadata, and the partner logs in with their private keys.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Cloud IAP for the Compute Engine instances, and add the operations partner as a Cloud IAP Tunnel User.

**Wrong words:**
- ❌ "**Cloud IAP … Cloud IAP Tunnel User**": IAP and IAM roles need a **Google identity**. The partner "does not use Google Accounts".

📌 **When to use it:** Use IAP when users have Google identities and VMs have no public IPs.
🏢 **Office example:** A guard who only accepts Google badges, for people who have none.

### ❌ B
> **B.** Tag all the instances with the same network tag. Create a firewall rule in the VPC to grant TCP access on port 22 for traffic from the operations partner to instances with the network tag.

**Wrong words:**
- ✔️ Port 22 must be reachable.
- ❌ "**firewall rule … port 22**" alone: opening the port doesn't give anyone a **login**. They still need credentials.

📌 **When to use it:** Use it together with SSH keys to allow the network path.
🏢 **Office example:** Unlocking the gate but giving no door key.

### ❌ C
> **C.** Set up Cloud VPN between your Google Cloud VPC and the internal network of the operations partner.

**Wrong words:**
- ❌ "**Set up Cloud VPN**": a network link only, not a way to log in. It's also heavy for this.

📌 **When to use it:** Use VPN to connect two whole networks privately.
🏢 **Office example:** Building a private road but no key to the building.

### ✅ D
> **D.** Ask the operations partner to generate SSH key pairs, and add the public keys to the VM instances.

**Why it's correct:**
- ✔️ "**Ask the operations partner to generate SSH key pairs**" matches "**does not use Google Accounts**": SSH keys don't need Google identities.
- ✔️ "**add the public keys to the VM instances**" matches "**grant access to the instances … maintain the installed tooling**": they can SSH in to do maintenance.

📌 **When to use it:** Use it when outsiders without company accounts need to log in to specific machines.
🏢 **Office example:** Installing padlocks that only the contractor's own keys open.

---

## 🛒 E-Commerce Full-Stack Example

```bash
# partner sends ops-partner.pub
gcloud compute instances add-metadata tools-vm-1 --zone=us-central1-a \
  --metadata-from-file ssh-keys=partner-keys.txt   # "opsuser:ssh-ed25519 AAAA... opsuser"
```

---

## 🧠 Key Takeaways / Memory Tips

- **No Google accounts → SSH key pairs in VM metadata.**
- IAP/OS Login need Google identities.
  🧠 *"**No Google account? Bring your own key.**"*
- Related: **Q074** (OS Login), **Q001**, **Q087**.

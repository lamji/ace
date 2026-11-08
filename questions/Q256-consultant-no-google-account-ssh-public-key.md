# Q256: External Consultant on VPN Without a Google Account Needs SSH (Their Public Key Added to the VM)

**Topic:** Compute Engine (SSH keys)

## ❓ Question
> You have deployed an application on a Compute Engine instance. An external consultant needs to access the Linux-based instance. The consultant is connected to your corporate network through a VPN connection, but the consultant has no Google account. What should you do?
>
> **A.** Instruct the external consultant to use the gcloud compute ssh command line tool by using Identity-Aware Proxy to access the instance.
>
> **B.** Instruct the external consultant to use the gcloud compute ssh command line tool by using the public IP address of the instance to access it.
>
> **C.** Instruct the external consultant to generate an SSH key pair, and request the public key from the consultant. Add the public key to the instance yourself, and have the consultant access the instance through SSH with their private key.
>
> **D.** Instruct the external consultant to generate an SSH key pair, and request the private key from the consultant. Add the private key to the instance yourself, and have the consultant access the instance through SSH with their public key.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An outside consultant needs access to a Linux VM. They connect to your company network through a VPN but have no Google account.
- **What you must achieve:** Give the consultant access to the VM.
- **The limits:** They have no Google account.
- **What they're really asking:** How do you let someone without a Google account log in to the VM?

**Clues in the question:**
- "**no Google account**" → gcloud/IAP need a Google identity → use plain **SSH keys**.
- Consultant keeps the **private** key; you add their **public** key to the VM. The VPN gives network reach.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. SSH key pair 🔑 (review from Q152)
- **What it is:** A **private** key (secret, stays with the user) and a **public** key (placed on the server).
- **Looks like:** `ssh-keygen -t ed25519` → add `id_ed25519.pub` to instance metadata
- **Not to be confused with:** password.
- **Analogy:** 🔐 Your own key + the matching lock you hand the landlord.
- **In the online store:** Contractor access.

### 🔗 How they fit together
```
 consultant: private key 🔒 ── VPN ── SSH ──► VM (has consultant's public key) ✅
```

---

## 🌍 Real-World Scenario

A contractor without a Google account generates an SSH key pair, sends the **public** key, and the admin adds it to the VM. They SSH in over the VPN.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Instruct the external consultant to use the gcloud compute ssh command line tool by using Identity-Aware Proxy to access the instance.

**Wrong words:**
- ❌ "**gcloud compute ssh … Identity-Aware Proxy**": IAP checks a **Google identity**, which the consultant doesn't have.

📌 **When to use it:** Use IAP for staff with Google accounts.
🏢 **Office example:** A guard who only accepts company badges.

### ❌ B
> **B.** Instruct the external consultant to use the gcloud compute ssh command line tool by using the public IP address of the instance to access it.

**Wrong words:**
- ❌ "**gcloud compute ssh**": needs a Google login.
- ❌ "**public IP address**": exposes the VM; the VPN already gives private access.

📌 **When to use it:** **Avoid** public SSH.
🏢 **Office example:** Opening a street door for one visitor.

### ✅ C
> **C.** Instruct the external consultant to generate an SSH key pair, and request the public key from the consultant. Add the public key to the instance yourself, and have the consultant access the instance through SSH with their private key.

**Why it's correct:**
- ✔️ "**generate an SSH key pair, and request the public key**" matches "**the consultant has no Google account**": SSH keys don't need one.
- ✔️ "**Add the public key to the instance yourself … SSH with their private key**": the private key never leaves the consultant; the VPN provides the network path.

📌 **When to use it:** Use it when an outsider without a company account needs to log in to one machine.
🏢 **Office example:** The visitor gives you a copy of their lock; you fit it to the door; they open it with their own key.

### ❌ D
> **D.** Instruct the external consultant to generate an SSH key pair, and request the private key from the consultant. Add the private key to the instance yourself, and have the consultant access the instance through SSH with their public key.

**Wrong words:**
- ❌ "**request the private key**": the private key must never be shared.
- ❌ "**SSH with their public key**": public keys can't log in.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Asking a visitor to hand over their house key.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instances add-metadata reports-vm --metadata-from-file=ssh-keys=consultant-keys.txt` (format `consultant:ssh-ed25519 AAAA… consultant`).

---

## 🧠 Key Takeaways / Memory Tips

- **No Google account → SSH keys: they keep the private key, you add the public key.**
  🧠 *"**Public goes on the server; private stays home.**"*
- Related: **Q152**, **Q191**.

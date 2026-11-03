# Q210: Most Secure and Cost-Efficient SSH Login (gcloud compute ssh --tunnel-through-iap + Allow 35.235.240.0/20)

**Topic:** Security (IAP TCP forwarding)

## ❓ Question
> Your team is using Linux instances on Google Cloud. You need to ensure that your team logs in to these instances in the most secure and cost efficient way. What should you do?
>
> **A.** Attach a public IP to the instances and allow incoming connections from the internet on port 22 for SSH.
>
> **B.** Use the gcloud compute ssh command with the --tunnel-through-iap flag. Allow ingress traffic from the IP range 35.235.240.0/20 on port 22.
>
> **C.** Use a third party tool to provide remote access to the instances.
>
> **D.** Create a bastion host with public internet access. Create the SSH tunnel to the instance through the bastion host.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Most secure** and **cheapest** way to SSH.

**Clues in the question:**
- "**most secure**" → no public IPs; identity-checked access → **IAP TCP forwarding**.
- "**cost efficient**" → no extra bastion VM to pay for.

**Exam topic:** Security.

---

## 📚 Key Terms Explained

### 1. 35.235.240.0/20 🔑
- **What it is:** The IP range IAP uses to forward TCP traffic to your VMs. You allow only this range on port 22.
- **Looks like:** `--source-ranges=35.235.240.0/20 --allow=tcp:22`
- **Not to be confused with:** the internet.
- **Analogy:** 🛂 The guard desk's own entrance.
- **In the online store:** IAP SSH rule.

### 2. Bastion host
- **What it is:** A VM with a public IP used as a jump box into private VMs. Costs money and must be patched.
- **Looks like:** `ssh -J bastion user@10.0.0.5`
- **Not to be confused with:** IAP.
- **Analogy:** 🚪 A side door with a doorman you pay full-time.
- **In the online store:** —

### 🔗 How they fit together
```
 gcloud compute ssh vm --tunnel-through-iap → IAP (35.235.240.0/20) → VM:22 ✅
```

---

## 🌍 Real-World Scenario

A team removes public IPs and bastions. Engineers connect through **IAP**, and the firewall only allows `35.235.240.0/20` on port 22.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Attach a public IP to the instances and allow incoming connections from the internet on port 22 for SSH.

**Wrong words:**
- ❌ "**public IP … allow incoming connections from the internet on port 22**": exposes SSH to the whole internet.

📌 **When to use it:** **Avoid this** for production VMs.
🏢 **Office example:** Leaving the back door open to the street.

### ✅ B
> **B.** Use the gcloud compute ssh command with the --tunnel-through-iap flag. Allow ingress traffic from the IP range 35.235.240.0/20 on port 22.

**Why it's correct:**
- ✔️ "**gcloud compute ssh … --tunnel-through-iap**" matches "**most secure**": IAP checks identity and the VM needs no public IP.
- ✔️ "**Allow ingress traffic from the IP range 35.235.240.0/20 on port 22**": only IAP can reach SSH.
- ✔️ No extra VM to run, which matches "**cost efficient**".

📌 **When to use it:** Use it when staff need to log in to internal machines safely without paying for extra infrastructure.
🏢 **Office example:** A guard desk that checks ID and escorts staff to internal rooms, no extra doorman needed.

### ❌ C
> **C.** Use a third party tool to provide remote access to the instances.

**Wrong words:**
- ❌ "**third party tool**": extra cost and another product to secure.

📌 **When to use it:** Use it only if company policy requires that tool.
🏢 **Office example:** Hiring an outside security firm for something the building already does.

### ❌ D
> **D.** Create a bastion host with public internet access. Create the SSH tunnel to the instance through the bastion host.

**Wrong words:**
- ❌ "**bastion host with public internet access**": costs a VM, needs patching, and is a public target.

📌 **When to use it:** Use a bastion when IAP isn't an option.
🏢 **Office example:** Paying a full-time doorman at a side door.

---

## 🛒 E-Commerce Full-Stack Example

Firewall `allow-iap-ssh` (35.235.240.0/20, tcp:22) + `roles/iap.tunnelResourceAccessor` for `group:ops@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Secure + cheap SSH → IAP tunnel + allow 35.235.240.0/20 on 22.**
  🧠 *"**35.235.240.0/20 = IAP's door.**"*
- Related: **Q191**, **Q152**.

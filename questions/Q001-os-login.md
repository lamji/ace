# Q001: OS Login for SSH Access to Compute Engine

**Topic:** IAM + Compute Engine access (OS Login)

## ❓ Question
> Every employee of your company has a Google account. Your operational team needs to manage a large number of instances on Compute Engine. Each member of this team needs only administrative access to the servers. Your security team wants to ensure that the deployment of credentials is operationally efficient and must be able to determine who accessed a given instance. What should you do?
>
> **A.** Generate a new SSH key pair. Give the private key to each member of your team. Configure the public key in the metadata of each instance.
>
> **B.** Ask each member of the team to generate a new SSH key pair and to send you their public key. Use a configuration management tool to deploy those keys on each instance.
>
> **C.** Ask each member of the team to generate a new SSH key pair and to add the public key to their Google account. Grant the "compute.osAdminLogin" role to the Google group corresponding to this team.
>
> **D.** Generate a new SSH key pair. Give the private key to each member of your team. Configure the public key as a project-wide public SSH key in your Cloud Platform project and allow project-wide public SSH keys on each instance.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** Your team needs admin access to many virtual machines (VMs). How do you give them that access so that:
1. It's **easy to manage**, even across lots of servers, and
2. Security can **see exactly which person** logged into which server?

| Keyword | What it hints at |
|---|---|
| "Every employee has a **Google account**" | Use their existing Google identity |
| "**large number** of instances" | Don't manage keys on each server by hand |
| "**administrative** access" | They need sudo/root, so the *admin* role |
| "**operationally efficient**" | Least manual work |
| "**determine who accessed**" | Every person must have their **own** credentials (auditing) |

---

## 📚 Key Terms Explained

### 1️⃣ Compute Engine Instance
- **What it is:** A virtual machine (VM), meaning a computer that runs in Google's data center that you rent and control.
- **Analogy:** 🏢 Renting an office in a big building. You use it as your own, but Google owns the building.
- **In the online store:** `api-orders-03` is a VM that runs the checkout API.

### 2️⃣ SSH and SSH Key Pair
- **What it is:** SSH is a secure way to log into a remote Linux server from your terminal. A **key pair** has two parts:
  - **Private key:** stays secret on your laptop.
  - **Public key:** placed on the server (or in your Google account).
  The server lets you in only if your private key matches the public key.
- **Analogy:** 🔐 The public key is a **padlock** you can give anyone. The private key is the **only key** that opens it. Never share the private key.
- **In the online store:** An engineer SSHes into `api-orders-03` to read logs during a Black Friday slowdown.

### 3️⃣ Instance Metadata / Project-wide Metadata
- **What it is:** Key-value settings attached to a VM (instance metadata) or to every VM in the project (project-wide metadata). SSH public keys can be stored here.
- **Analogy:** 📋 A **sticky note** on one office door (instance) vs a **notice posted at the building entrance** that applies to every office (project-wide).
- **In the online store:** Setting `enable-oslogin=TRUE` in project metadata turns on OS Login for all ShopNow VMs.

### 4️⃣ OS Login
- **What it is:** A Google Cloud feature that links SSH access to a person's **Google account** and controls it with **IAM**, instead of managing keys on each VM.
- **Analogy:** 🪪 An **employee ID badge** system. HR turns your badge on or off centrally, and every door swipe is logged with your name.
- **In the online store:** Maria logs in as `maria@shopnow.com`, and the logs record exactly that.

### 5️⃣ IAM Role (`compute.osLogin` vs `compute.osAdminLogin`)
- **What it is:** IAM (Identity and Access Management) decides **who** can do **what**. A role is a bundle of permissions.
  - `roles/compute.osLogin`: log in as a normal user (no sudo).
  - `roles/compute.osAdminLogin`: log in **with admin (sudo)** rights.
- **Analogy:** 🎫 A **visitor badge** (osLogin) vs a **manager master badge** (osAdminLogin).
- **In the online store:** Ops engineers get `osAdminLogin`. Developers who only read logs get `osLogin`.

### 6️⃣ Google Group
- **What it is:** A **named list of email addresses**. Each address is a person's **own** Google account. You grant IAM roles to the group, and **everyone on the list** gets them.
- **Looks like:** `ops-team@shopnow.com = [ken@shopnow.com, lea@shopnow.com, max@shopnow.com]`
- **Not to be confused with:** a shared account. The group has **no password** and **nobody logs in with it**. Ken still signs in as `ken@shopnow.com`, which is why security can see **who** accessed each VM.
- **Analogy:** 👥 A **team mailing list**. Add someone and they get every email. Remove them and they stop receiving.
- **In the online store:** When Ken leaves, you remove him from `ops-team@shopnow.com`, and his access to all VMs is gone.

### 🔗 How They Fit Together
```
👤 maria@shopnow.com  (Google account + her SSH public key)
      │ member of
      ▼
👥 Google Group: ops-team@shopnow.com
      │ granted IAM role
      ▼
🎫 roles/compute.osAdminLogin
      │ allows sudo SSH into
      ▼
🖥️ All VMs where OS Login is on (enable-oslogin=TRUE)
```

---

## 🌍 Real-World Scenario

Your company has 200 Linux VMs, and 10 ops engineers need to SSH in. One night someone runs `rm -rf` on production by mistake. Your manager asks: **"Who did this?"**

- With a shared key, you can't answer.
- When an engineer quits, you'd have to remove their key from all 200 servers.

**OS Login** fixes both problems: access is tied to each person's Google account and controlled by IAM.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Generate a new SSH key pair. Give the private key to each member of your team. Configure the public key in the metadata of each instance.

- **One shared private key:** you **cannot determine who accessed** an instance.
- **"In the metadata of each instance":** you configure VMs one by one, which is **not efficient**.
- If one person leaks the key, everyone's access is compromised.

**📌 When to use it:** **Never use this.** Giving everyone the same private key means you can't tell who logged in. Use C instead.
🏢 **Office example:** Like giving every employee a copy of the same office key. When something goes missing, you can't tell who opened the door.

### ❌ B
> **B.** Ask each member of the team to generate a new SSH key pair and to send you their public key. Use a configuration management tool to deploy those keys on each instance.

- ✔️ Individual keys, so you **can** tell who logged in.
- ❌ You must build and maintain the config tool and run it again for every join or leave, so it's **not operationally efficient**.
- It rebuilds what OS Login already does.

**📌 When to use it:** Use it when you **can't use Google accounts** for login, so someone has to set up each person's own key on every server.
🏢 **Office example:** A small office with no ID-card system, so the IT person walks to every door and installs a new lock key for each new employee.

### ✅ C
> **C.** Ask each member of the team to generate a new SSH key pair and to add the public key to their Google account. Grant the "compute.osAdminLogin" role to the Google group corresponding to this team.

- Keys are tied to **personal Google identities**, so it's **auditable**. ✔️
- The role is granted to a **Google group**, so access is managed centrally and is **efficient**. ✔️
- **osAdminLogin** gives **sudo**, matching "administrative access." ✔️

**📌 When to use it:** Use it when **many people need to get into many servers** and you **must know who got in**.
🏢 **Office example:** An employee ID card system. HR turns your card on or off from one desk, every door swipe is logged with your name, and managers get a master card.

### ❌ D
> **D.** Generate a new SSH key pair. Give the private key to each member of your team. Configure the public key as a project-wide public SSH key in your Cloud Platform project and allow project-wide public SSH keys on each instance.

- ✔️ A project-wide key is easier to set up than A.
- ❌ It's still **one shared private key**, so there's **no way to know who accessed** an instance.
- ⚠️ **Trap option:** it looks efficient but fails the auditing requirement.

**📌 When to use it:** **Never use this.** It's still one shared key for everyone, so you can't tell who logged in. Use C instead.
🏢 **Office example:** Like hanging one master key at the building entrance for anyone to use. The doors open, but nobody knows who went in.

---

## 🛒 E-Commerce Full-Stack Example

```
Shoppers ──► Load Balancer ──► [ VMs on Compute Engine ]
                                 ├─ web-frontend-01..20    (Next.js storefront)
                                 ├─ api-orders-01..10      (Node.js checkout/orders API)
                                 └─ worker-inventory-01..5 (stock updates)
                                        │
                                        ▼
                                  Cloud SQL (orders, customers)
```

During **Black Friday**, checkout slows down. Maria and Ken need to SSH into `api-orders-03`.

- **❌ A / D:** Everyone shares `shopnow-team.pem`. Ken quits and still has the key. 😱 You have to re-key 35 VMs.
- **❌ B:** You maintain an Ansible playbook and run it against 35 VMs for every staff change. If a run fails on one VM, the old key stays there.
- **✅ C (OS Login):**
  1. Create the group `ops-team@shopnow.com` and add Maria and Ken.
  2. Enable OS Login: `enable-oslogin=TRUE`.
  3. Grant the role:
     ```bash
     gcloud projects add-iam-policy-binding shopnow-prod \
       --member="group:ops-team@shopnow.com" \
       --role="roles/compute.osAdminLogin"
     ```
  4. Maria runs `gcloud compute ssh api-orders-03`, gets sudo, and the login is recorded as **maria@shopnow.com**.
  5. Ken leaves → you remove him from the group → his access is gone from all VMs. ✅

---

## 🧠 Key Takeaways / Memory Tips

- **"Google accounts" + "SSH to many VMs" + "know who accessed" → OS Login.**
- **`roles/compute.osLogin`** = normal user. **`roles/compute.osAdminLogin`** = admin (sudo) 👑
- 🚩 "Give the private key to each member of your team" → **almost always wrong** (no audit trail).
- Grant IAM roles to **Google groups**, not to individual users.

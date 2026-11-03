# Q074: SSH to Only One Instance for a Group (OS Login + compute.osLogin)

**Topic:** IAM + Compute Engine (OS Login, enable-oslogin metadata, roles/compute.osLogin on one instance, SSH keys)

## ❓ Question
> You want to configure an SSH connection to a single Compute Engine instance for users in the dev1 group. This instance is the only resource in this particular Google Cloud Platform project that the dev1 users should be able to connect to. What should you do?
>
> **A.** Set metadata to enable-oslogin=true for the instance. Grant the dev1 group the compute.osLogin role. Direct them to use the Cloud Shell to ssh to that instance.
>
> **B.** Set metadata to enable-oslogin=true for the instance. Set the service account to no service account for that instance. Direct them to use the Cloud Shell to ssh to that instance.
>
> **C.** Enable block project wide keys for the instance. Generate an SSH key for each user in the dev1 group. Distribute the keys to dev1 users and direct them to use their third-party tools to connect.
>
> **D.** Enable block project wide keys for the instance. Generate an SSH key and associate the key with that instance. Distribute the key to dev1 users and direct them to use their third-party tools to connect.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The **dev1 group** must be able to SSH into **one VM only**, and nothing else in the project. What's the clean, Google-recommended way?

**Clues in the question:**
- "**users in the dev1 group**": manage access by **group** with IAM, not by handing out keys.
- "**single Compute Engine instance**" / "**the only resource**": grant the role **on that one instance**, not on the whole project.
- "**SSH connection**": **OS Login** ties SSH access to people's Google identities and IAM roles.

**Exam topic:** IAM / Compute Engine.

---

## 📚 Key Terms Explained

### 1️⃣ OS Login (review from Q001) 🔑
- **What it is:** A feature that lets people SSH into Linux VMs **using their own Google account**, controlled by **IAM roles**. You turn it on with the metadata `enable-oslogin=TRUE`.
- **Looks like:** `gcloud compute instances add-metadata dev-box --metadata=enable-oslogin=TRUE`
- **Not to be confused with:** managing SSH keys by hand in metadata. With OS Login, Google handles the keys for each person.
- **Analogy:** 🪪 The door checks your **own employee badge** against an access list, instead of everyone sharing physical keys.
- **In the online store:** Developers SSH into `dev-box` with their own accounts; leaving the company removes access automatically.

### 2️⃣ roles/compute.osLogin
- **What it is:** The IAM role that allows **SSH login as a normal user** (no admin/sudo) through OS Login. (`compute.osAdminLogin` adds sudo.)
- **Looks like:**
  ```bash
  gcloud compute instances add-iam-policy-binding dev-box --zone=us-central1-a \
    --member=group:dev1@shopnow.com --role=roles/compute.osLogin
  ```
- **Not to be confused with:** granting it on the **project**, which would allow SSH to **every** VM there. Granting on **the instance** limits it to one VM.
- **Analogy:** ✅ Adding the team to the **access list of one specific door**.

### 3️⃣ Google group (review from Q025)
- **What it is:** A named **list of email addresses**. A role given to the group applies to everyone on the list.
- **Looks like:** `dev1@shopnow.com = [li@, sam@, kai@]`
- **Not to be confused with:** a shared login. Each person signs in as themselves.
- **Analogy:** 📇 The "Dev1 Team" list at the door.

### 4️⃣ SSH keys and "block project-wide keys"
- **What it is:** An **SSH key pair** is a private key (kept secret by the user) and a public key (placed on the VM). **Block project-wide keys** makes a VM ignore keys stored at the project level.
- **Looks like:** `ssh-keygen -t ed25519 -f ~/.ssh/dev1` → `dev1` (private), `dev1.pub` (public)
- **Not to be confused with:** OS Login. Manual keys must be created, distributed and removed by hand.
- **Analogy:** 🔑 **Physical keys** cut and handed out to each person.

### 5️⃣ Cloud Shell
- **What it is:** A free, browser-based Linux terminal in the Google Cloud console with gcloud ready to use.
- **Looks like:** `gcloud compute ssh dev-box --zone=us-central1-a`
- **Analogy:** 💻 A **company laptop at the front desk** with all the tools installed.

### 🔗 How they fit together
```
 dev-box (enable-oslogin=TRUE)
   IAM on THIS instance: dev1@ → roles/compute.osLogin
       │
 li@ (in dev1) → Cloud Shell → gcloud compute ssh dev-box ✅
 li@ → any other VM in the project ❌ (no role there)
```

---

## 🌍 Real-World Scenario

A team needs shell access to one shared dev server, but not to production VMs in the same project. With OS Login, the admin grants the team's **group** the OS Login role **on that VM only**. People log in with their own accounts, every login is audited, and when someone leaves the group, their access disappears. No keys to create, share or revoke.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set metadata to enable-oslogin=true for the instance. Grant the dev1 group the compute.osLogin role. Direct them to use the Cloud Shell to ssh to that instance.

**Why it's correct:**
- ✔️ "**Set metadata to enable-oslogin=true for the instance**" matches "**SSH connection to a single Compute Engine instance**": SSH access to that VM is now controlled by IAM.
- ✔️ "**Grant the dev1 group the compute.osLogin role**" matches "**users in the dev1 group**": one grant to the group covers every member; granted on the instance, it covers only that VM.
- ✔️ "**Direct them to use the Cloud Shell to ssh**" matches "**SSH connection**": Cloud Shell has gcloud ready, so `gcloud compute ssh` just works with their own account.

📌 **When to use it:** Use it when a team should log in to one specific computer with their own accounts, and nothing else.
🏢 **Office example:** Adding the team to the badge list for one specific room; their own badges open that door only.

### ❌ B
> **B.** Set metadata to enable-oslogin=true for the instance. Set the service account to no service account for that instance. Direct them to use the Cloud Shell to ssh to that instance.

**Wrong words:**
- ✔️ "Set metadata to enable-oslogin=true for the instance" is right.
- ❌ "**Set the service account to no service account**": the VM's service account controls what the **VM** can do with Google APIs; it has **nothing to do** with who can SSH in.
- ❌ Missing step: no role is granted to dev1, so with OS Login on, **they can't log in at all**.

📌 **When to use it:** Use "no service account" when a VM never needs to call any Google API.
🏢 **Office example:** Taking away the room's own company credit card, but never adding the team to the door's badge list.

### ❌ C
> **C.** Enable block project wide keys for the instance. Generate an SSH key for each user in the dev1 group. Distribute the keys to dev1 users and direct them to use their third-party tools to connect.

**Wrong words:**
- ✔️ "Enable block project wide keys for the instance" does limit which keys work on this VM.
- ❌ "**Generate an SSH key for each user … Distribute the keys**": you create and hand out **private keys** yourself. They can be copied or leaked, and you must remove them by hand when people leave.

📌 **When to use it:** Use manual per-user keys only when OS Login isn't available (for example, some older images).
🏢 **Office example:** Cutting a physical key for each team member and collecting them back when someone quits.

### ❌ D
> **D.** Enable block project wide keys for the instance. Generate an SSH key and associate the key with that instance. Distribute the key to dev1 users and direct them to use their third-party tools to connect.

**Wrong words:**
- ❌ "**Generate an SSH key**" + "**Distribute the key to dev1 users**": **one shared private key** for everyone. You can't tell who logged in, and removing one person means changing the key for everyone.

📌 **When to use it:** **Never use this.** Never share one private key. Use OS Login (A).
🏢 **Office example:** One door key copied for the whole team; when one person leaves, you must change the lock for everyone.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's project has `dev-box` plus production VMs. Only `dev1@shopnow.com` should reach `dev-box`.

```bash
gcloud compute instances add-metadata dev-box --zone=us-central1-a \
  --metadata=enable-oslogin=TRUE

gcloud compute instances add-iam-policy-binding dev-box --zone=us-central1-a \
  --member=group:dev1@shopnow.com --role=roles/compute.osLogin

# Li, from Cloud Shell:
gcloud compute ssh dev-box --zone=us-central1-a     # ✅
gcloud compute ssh checkout-prod-1 --zone=us-central1-a   # ❌ permission denied
```

---

## 🧠 Key Takeaways / Memory Tips

- **SSH for a group → OS Login + `compute.osLogin` granted to the group.**
- **Only one VM → grant the role on that instance, not the project.**
- **Never generate and hand out private keys, and never share one key.**
  🧠 *"**Badges, not keys: OS Login + a role on the one door.**"*
- Related: **Q001** (OS Login), **Q025** (roles to groups).

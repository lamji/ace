# Q036: Using a Service Account From Another Project to Snapshot VMs (Cross-Project IAM)

**Topic:** IAM + Compute Engine (cross-project service accounts, `roles/compute.storageAdmin`, snapshots, access scopes, service account keys)

## ❓ Question
> You have one project called proj-sa where you manage all your service accounts. You want to be able to use a service account from this project to take snapshots of VMs running in another project called proj-vm. What should you do?
>
> **A.** Download the private key from the service account, and add it to each VMs custom metadata.
>
> **B.** Download the private key from the service account, and add the private key to each VM's SSH keys.
>
> **C.** Grant the service account the IAM Role of Compute Storage Admin in the project called proj-vm.
>
> **D.** When creating the VMs, set the service account's API scope for Compute Engine to read/write.

*(The `λ€™` characters in the screenshot are broken apostrophes, shown here as `'`.)*

**My answer:** D
**Correct answer:** C
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** Your service accounts live in **`proj-sa`**. The VMs live in **`proj-vm`**. You want a service account from `proj-sa` to **take snapshots** of the VMs in `proj-vm`. How do you give it permission?

| Keyword | What it hints at |
|---|---|
| "**service account from this project**" … "**in another project**" | A service account can be granted roles **in any project**. Add it to **`proj-vm`'s IAM** |
| "**take snapshots**" | Snapshots are a **disk/storage** action in Compute Engine → **Compute Storage Admin** |
| (no "create VMs" anywhere) | Nothing about the VMs themselves needs to change |

**Exam topic:** IAM (cross-project access for service accounts).

---

## 📚 Key Terms Explained

### 1️⃣ Service Account Across Projects 🔑
- **What it is:** A service account **lives** in one project, but it's just an **identity** (an email address). You can **grant it roles in any other project**, exactly like you'd grant a role to a person.
- **Looks like:**
  ```
  Service account (lives in proj-sa):  snapshot-bot@proj-sa.iam.gserviceaccount.com
  Granted in proj-vm's IAM:            roles/compute.storageAdmin
  ```
- **Not to be confused with:** being stuck in its home project. "Lives in proj-sa" only means **where it's managed**, not **where it can work**.
- **Analogy:** 🪪 An employee badge issued by **head office HR**, which a **branch office** can also accept by adding the badge to its own door list.
- **In the online store:** One central `shopnow-identity` project holds all service accounts, used by the prod, dev and data projects.

### 2️⃣ Snapshot
- **What it is:** A **point-in-time copy of a VM's disk**. You can restore a disk or create a new VM from it.
- **Looks like:** `gcloud compute snapshots create api-orders-03-nightly --source-disk=api-orders-03 --source-disk-zone=us-central1-a`
- **Not to be confused with:** a backup of the whole VM settings, or an image. A snapshot copies **one disk's data**.
- **Analogy:** 📸 A **photocopy of a filing cabinet's contents** at 2 AM.

### 3️⃣ Compute Storage Admin (`roles/compute.storageAdmin`)
- **What it is:** A predefined role with full control of Compute Engine **storage**: **disks, images and snapshots**. It **can't** create or delete VMs.
- **Looks like:** `serviceAccount:snapshot-bot@proj-sa.iam.gserviceaccount.com → roles/compute.storageAdmin (on project proj-vm)`
- **Not to be confused with:** Storage Admin (Q028), which is for **Cloud Storage buckets**. "**Compute** Storage" = **VM disks**.
- **Analogy:** 🗄️ The **archive clerk** who can photocopy and store cabinet contents, but can't move desks or hire staff.

### 4️⃣ Access Scopes (review from Q026)
- **What it is:** A legacy **on/off switch on a VM** that limits which Google APIs **that VM** may call with **its attached service account**. It **grants nothing** by itself, and it only applies to VMs, not to service accounts used elsewhere.
- **Looks like:** `--scopes=compute-rw`, `--scopes=cloud-platform`
- **Not to be confused with:** an IAM role. Scope = "which elevator floors", IAM = "which room keys".
- **Analogy:** 🚪 The **elevator floor switch**: it doesn't unlock any room.

### 5️⃣ Service Account Private Key (JSON key)
- **What it is:** A **downloadable password file** for a service account. Whoever holds it **becomes** the service account.
- **Looks like:** `snapshot-bot-key.json` containing `"private_key": "-----BEGIN PRIVATE KEY-----…"`
- **Not to be confused with:** an **SSH key** (for logging into a VM) or **metadata** (VM settings). Pasting a key there doesn't grant any permission, and it **exposes** the key.
- **Analogy:** 🔑 A **copy of the master badge**. Lose it and anyone can act as that badge.

### 🔗 How They Fit Together
```
📁 proj-sa                                   📁 proj-vm
  🪪 snapshot-bot@proj-sa.iam…  ─────────►     IAM policy:
  (identity lives here)          granted in      snapshot-bot@proj-sa… → roles/compute.storageAdmin ✅
                                                     │
                                                     ▼
                                                 💾 disks of vm-1, vm-2 … → 📸 snapshots

❌ A/B: private key pasted into metadata/SSH → leaks the key, grants nothing
❌ D:   access scope → VM-level switch, not a permission in proj-vm
```

---

## 🌍 Real-World Scenario

Bigger companies often keep **all service accounts in one central project** (easier to audit and control), and run workloads in many other projects. A backup tool or a scheduled job uses one service account to **snapshot disks across many projects**. The pattern is always: **add that service account to each target project's IAM** with the smallest role that does the job.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Download the private key from the service account, and add it to each VMs custom metadata.

**Why it's wrong:**
- ❌ **Downloading keys is risky**, and **metadata is readable** by anything running on the VM and anyone who can view the VM. It's a key leak.
- ❌ It **grants no permission** in `proj-vm`. The service account would still be denied.

**📌 When to use it:** **Never use this.** It exposes the key and gives no access. Grant an IAM role in proj-vm (C).
🏢 **Office example:** Taping a copy of the master badge to every desk. Anyone can grab it, and it still doesn't open the archive.

### ❌ B
> **B.** Download the private key from the service account, and add the private key to each VM's SSH keys.

**Why it's wrong:**
- ❌ SSH keys are for **logging into the VM**, and they use **public** keys, not a service account's private key.
- ❌ Same leak and same lack of permission as A.

**📌 When to use it:** **Never use this.** A service account key doesn't belong in SSH keys. Grant an IAM role (C).
🏢 **Office example:** Putting a copy of the master badge into the front-door lock. Wrong lock, and now the badge is exposed.

### ✅ C
> **C.** Grant the service account the IAM Role of Compute Storage Admin in the project called proj-vm.

**Why it's correct:**
- ✔️ Service accounts can get roles **in other projects**. Add it to **`proj-vm`'s IAM**.
- ✔️ **Compute Storage Admin** covers **disks and snapshots**, exactly the job, without power over the VMs themselves.
- ✔️ No keys downloaded, nothing to change on the VMs.

**📌 When to use it:** Use it when a helper account from one project needs to do a specific job in another project.
🏢 **Office example:** The branch office adds the head-office archive clerk's badge to its archive-room door list.

### ❌ D (your answer)
> **D.** When creating the VMs, set the service account's API scope for Compute Engine to read/write.

**Why it's wrong:**
- ❌ **Access scopes grant nothing.** They only limit what a **VM's attached** service account can call. The service account would still have **no role in proj-vm**.
- ❌ "**When creating the VMs**": the VMs **already run**. You'd have to recreate them.
- ❌ It mixes things up: the snapshot tool isn't running **on** these VMs, so their scopes don't matter at all.
- 💡 **Likely mix-up:** "read/write for Compute Engine" sounds like the right permission. But since Q026 the rule is: **scopes = legacy switch, IAM roles = real permissions.**

**📌 When to use it:** Set scopes only when creating VMs, usually to `cloud-platform`, and let IAM roles control access.
🏢 **Office example:** Setting which floors a badge can reach in the elevator. It still doesn't unlock any room.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow keeps every service account in **`shopnow-identity`**. The storefront and checkout VMs run in **`shopnow-prod`**. A nightly Cloud Scheduler job runs as `snapshot-bot` to snapshot all prod disks.

```bash
# Grant the service account from shopnow-identity a role IN shopnow-prod (option C)
gcloud projects add-iam-policy-binding shopnow-prod \
  --member="serviceAccount:snapshot-bot@shopnow-identity.iam.gserviceaccount.com" \
  --role="roles/compute.storageAdmin"

# The nightly job (running as snapshot-bot) can now do:
gcloud compute snapshots create api-orders-03-$(date +%F) \
  --project=shopnow-prod \
  --source-disk=api-orders-03 --source-disk-zone=us-central1-a
```

| Action by `snapshot-bot` in `shopnow-prod` | Result |
|---|---|
| Snapshot the `api-orders-03` disk | ✅ Allowed |
| Delete old snapshots | ✅ Allowed |
| Delete the `api-orders-03` VM | ❌ Denied (Compute Storage Admin can't touch VMs) |

**🎬 With option A/B:** `snapshot-bot-key.json` sits in VM metadata. A compromised storefront VM reads it, and the attacker can act as `snapshot-bot`. Meanwhile the job **still gets "Permission denied"**. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Service account in project X needs to work in project Y → grant it a role in project Y's IAM.**
  🧠 *"**The badge is issued at head office. Each branch decides which doors it opens.**"*
- **Snapshots/disks/images → `roles/compute.storageAdmin`.** ("Compute Storage" = VM disks. "Storage Admin" = buckets, Q028.)
- 🚩 **"Download the private key"** is almost always wrong (Q001, Q019).
- 🚩 **Access scopes** never grant permissions (Q026).

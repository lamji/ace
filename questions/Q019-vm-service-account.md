# Q019: Making a VM Use a Specific Service Account (Not the Default)

**Topic:** IAM + Compute Engine (service accounts, "Identity and API access", access scopes, why not to use JSON keys)

## ❓ Question
> You have a Linux VM that must connect to Cloud SQL. You created a service account with the appropriate access rights. You want to make sure that the VM uses this service account instead of the default Compute Engine service account. What should you do?
>
> **A.** When creating the VM via the web console, specify the service account under the 'Identity and API Access' section.
>
> **B.** Download a JSON Private Key for the service account. On the Project Metadata, add that JSON as the value for the key compute-engine-service- account.
>
> **C.** Download a JSON Private Key for the service account. On the Custom Metadata of the VM, add that JSON as the value for the key compute-engine- service-account.
>
> **D.** Download a JSON Private Key for the service account. After creating the VM, ssh into the VM and save the JSON under ~/.gcloud/compute-engine-service-account.json.

*(The `λ€˜ λ€™` characters in option A are broken quote marks, shown here as `'`.)*

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know (learned it now)

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A Linux VM needs to connect to Cloud SQL (Google's managed relational database). You made a service account (a non-human Google identity that programs use) with the right access.
- **What you must achieve:** Make the VM use your service account instead of the default one every VM gets.
- **The limits:** None stated.
- **What they're really asking:** How do you switch the VM to your own service account?

| Keyword | What it hints at |
|---|---|
| "**service account with the appropriate access rights**" | The identity and its permissions already exist. You just need to **attach** it to the VM |
| "**instead of the default Compute Engine service account**" | Choose the service account in the VM's **Identity and API access** settings |
| (implied) | Google's best practice is to **attach** service accounts and **avoid downloading key files** |

**Exam topic:** IAM, specifically **service accounts on Compute Engine**.

---

## 📚 Key Terms Explained

### 1️⃣ Service Account
- **What it is:** An identity for a **program or machine**, not a person. Apps and VMs use it to prove **who they are** when calling Google Cloud services (Cloud SQL, Cloud Storage, ...). You give it IAM roles just like a user.
- **Analogy:** 🪪 An **ID badge for a robot employee**. The robot taps the badge, and the door system checks what the badge is allowed to open.
- **In the online store:** `shopnow-api-sa@shopnow-prod.iam.gserviceaccount.com` is the identity of the Orders API VM.

### 2️⃣ Default Compute Engine Service Account
- **What it is:** A service account Google **creates automatically** in every project (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`). VMs use it **unless you choose another one**. In many projects it has the very broad **Editor** role.
- **Problem:** **Every** VM shares it, and it can do **far too much**, which goes against **least privilege**.
- **Analogy:** 🔑 A **shared master badge** that every new robot gets by default, and it opens almost every door in the building.

### 3️⃣ IAM Role for Cloud SQL (`roles/cloudsql.client`)
- **What it is:** The role that lets an identity **connect to Cloud SQL instances**, and nothing more.
- **Analogy:** 🎫 A badge that opens **only the records room**.

### 4️⃣ "Identity and API access" (attaching a service account)
- **What it is:** A section in the **Create VM** page (and the `--service-account` flag in gcloud) where you **choose which service account the VM runs as**. A VM has **one** attached service account. To change it later, **stop** the VM first.
- Google then gives the VM **short-lived, auto-rotating credentials** through the **metadata server**. There are **no key files** to manage.
- **Analogy:** 🏢 **HR issuing the robot its own badge on its first day**, through the official system. The badge renews itself automatically, and nobody carries a copy.

### 5️⃣ Access Scopes
- **What it is:** An **older, extra limit** on which Google APIs a VM can call. Google's recommendation: set scope to **"Allow full access to all Cloud APIs"** (`cloud-platform`) and control access with **IAM roles** on the service account.
- ⚠️ The **default** scopes **don't include Cloud SQL**, so with default scopes the VM may be blocked even with the right IAM role.
- **Analogy:** 🚪 A **building-level door list** on top of the badge permissions. Easiest to open the building doors and let the **badge** decide.

### 6️⃣ Metadata Server
- **What it is:** A special internal address on every VM (`metadata.google.internal`) that gives the VM information about itself, including **access tokens** for its attached service account.
- **Analogy:** 🖥️ The **front desk inside each office** that hands the robot a **fresh day pass** whenever it asks.

### 7️⃣ Service Account Key (JSON Private Key)
- **What it is:** A **downloadable file** containing a **long-lived password** for a service account. Anyone who has the file **is** that service account until the key is deleted.
- ⚠️ **High security risk:** files get copied, emailed, or committed to Git. Google says **avoid keys** when you can attach a service account instead. Many companies even **block key creation** with an org policy (`iam.disableServiceAccountKeyCreation`).
- **Analogy:** 🗝️ A **physical copy of the badge** that never expires. If it's lost, anyone who finds it gets in.

### 8️⃣ Project Metadata vs Custom (Instance) Metadata
- **Project metadata:** Key-value settings shared by **all VMs** in the project (e.g., SSH keys, `enable-oslogin`, from Q001).
- **Custom / instance metadata:** Settings for **one VM** (e.g., a startup script).
- ⚠️ Metadata is **readable by anyone or any process with access to the project or VM**. It's **not a secret store**. There's also **no** special `compute-engine-service-account` key that makes a VM use a service account.
- **Analogy:** 📋 Project metadata = the **notice board in the lobby**. Instance metadata = a **note on one office door**. Everyone walking by can read both.

### 🔗 How They Fit Together
```
✅ The right way (attach the service account)
🖥️ VM: shopnow-api-vm
   └── Identity and API access → service account: shopnow-api-sa  (scope: cloud-platform)
            │
            │ app asks the metadata server for a token (automatic, short-lived)
            ▼
   🪪 shopnow-api-sa  ── IAM role: roles/cloudsql.client ──► 🗄️ Cloud SQL: shopnow-db ✅

❌ The wrong way (key files)
🗝️ JSON key downloaded ──► pasted in metadata (readable by others) / saved on disk
   → long-lived secret that can leak, and the VM still runs as the DEFAULT service account
```

---

## 🌍 Real-World Scenario

Security teams follow **least privilege**: each app gets **its own** identity with **only** the permissions it needs. The default Compute Engine service account is **shared and too powerful**, so cloud engineers create a **dedicated service account** per app and **attach** it to the VM.

They **avoid downloading keys**, because leaked service account keys are one of the most common causes of cloud security breaches.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** When creating the VM via the web console, specify the service account under the 'Identity and API Access' section.

**Why it's correct:**
- ✔️ This is **Google's official way** to make a VM run as a specific service account. You choose it in **Identity and API access** (or with `--service-account` in gcloud).
- ✔️ The VM gets **automatic, short-lived credentials** from the metadata server, so there are **no key files** to leak or rotate.
- ✔️ It follows **least privilege**: the VM gets only `roles/cloudsql.client`, not the broad default account.
- 💡 Also set access scope to **"Allow full access to all Cloud APIs"** and let IAM control permissions.

**📌 When to use it:** Use it when a **server needs its own identity** to use other Google services.
🏢 **Office example:** **HR issuing a new robot employee its own ID badge** on day one, through the official system. It only opens the doors it needs.

### ❌ B
> **B.** Download a JSON Private Key for the service account. On the Project Metadata, add that JSON as the value for the key compute-engine-service- account.

**Why it's wrong:**
- ❌ **There's no such metadata key.** Putting JSON in metadata **doesn't** change which service account the VM uses.
- ❌ **Project metadata is visible** to everyone with access to the project and to **every VM** in it. You'd be **publishing a secret key**.
- ❌ Downloading a key is **risky** and **unnecessary** when you can attach the service account.

**📌 When to use it:** **Never use this.** Don't put secret keys in metadata. Attach the service account instead (option A).
🏢 **Office example:** Like **pinning a copy of the master key on the lobby notice board**. Everyone who walks by can take it.

### ❌ C
> **C.** Download a JSON Private Key for the service account. On the Custom Metadata of the VM, add that JSON as the value for the key compute-engine- service-account.

**Why it's wrong:**
- ❌ Same problems as B, just on **one VM** instead of the whole project.
- ❌ **No such metadata key** exists, so the VM still runs as the **default** service account.
- ❌ Instance metadata is **readable by any process on the VM** and by anyone who can view the VM, so it's still a **leaked secret**.

**📌 When to use it:** **Never use this.** Metadata is not a safe place for secrets. Use option A.
🏢 **Office example:** Like **taping a copy of the key to one office door**. Anyone passing by can see it.

### ❌ D
> **D.** Download a JSON Private Key for the service account. After creating the VM, ssh into the VM and save the JSON under ~/.gcloud/compute-engine-service-account.json.

**Why it's wrong:**
- ❌ That **file path isn't special**. Google tools won't automatically use it, so the VM still uses the **default** service account.
- ❌ A **long-lived key on disk** can be copied, end up in backups, or be stolen if the VM is hacked.
- ❌ It's **manual**: you'd have to rotate (replace) the key yourself.

**📌 When to use it:** **Never use this** for a Google Cloud VM. Attach the service account instead (option A). (Key files are only a last resort for machines **outside** Google Cloud, and even then, Workload Identity Federation is preferred.)
🏢 **Office example:** Like **hiding a copy of the key in a desk drawer**. Anyone who opens the drawer can use it, and it never expires.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **Orders API** runs on a VM and saves orders in **Cloud SQL** (`shopnow-db`). Security says: *"The API VM may **only** connect to Cloud SQL. No broad default account, and no key files."*

```
🛍️ Shopper places order ──► 🖥️ shopnow-api-vm (runs as shopnow-api-sa)
                                  │ token from metadata server (auto, short-lived)
                                  ▼
                            🔌 Cloud SQL Auth Proxy
                                  │ roles/cloudsql.client ✅
                                  ▼
                            🗄️ Cloud SQL: shopnow-db (orders table)
```

**1. Create the service account and give it only the Cloud SQL role:**
```bash
gcloud iam service-accounts create shopnow-api-sa \
  --display-name="ShopNow Orders API VM"

gcloud projects add-iam-policy-binding shopnow-prod \
  --member="serviceAccount:shopnow-api-sa@shopnow-prod.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"
```

**2. Create the VM with that service account attached (option A, CLI version):**
```bash
gcloud compute instances create shopnow-api-vm \
  --zone=asia-southeast1-a \
  --machine-type=e2-medium \
  --service-account=shopnow-api-sa@shopnow-prod.iam.gserviceaccount.com \
  --scopes=cloud-platform
```

**3. (If the VM already exists) stop it, switch the service account, and start it:**
```bash
gcloud compute instances stop shopnow-api-vm --zone=asia-southeast1-a
gcloud compute instances set-service-account shopnow-api-vm \
  --zone=asia-southeast1-a \
  --service-account=shopnow-api-sa@shopnow-prod.iam.gserviceaccount.com \
  --scopes=cloud-platform
gcloud compute instances start shopnow-api-vm --zone=asia-southeast1-a
```

**4. Inside the VM, check which identity it uses, then connect with no key file:**
```bash
curl -H "Metadata-Flavor: Google" \
  http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email
# → shopnow-api-sa@shopnow-prod.iam.gserviceaccount.com ✅

./cloud-sql-proxy shopnow-prod:asia-southeast1:shopnow-db
# The proxy automatically uses the VM's attached service account
```

**🎬 Why it matters:** A developer accidentally pushes the Orders API code to a **public GitHub repo**. With option A, there's **no key in the code**, so there's nothing to steal. ✅ With B/C/D, the JSON key is copied around and could end up public, and attackers could connect to the **customer orders database**. 😱

---

## 🧠 Key Takeaways / Memory Tips

- **"VM should use a specific service account" → attach it in "Identity and API access" (or `--service-account`).**
- **Attach, don't download.** Attached service accounts get **automatic, short-lived tokens**. **JSON keys are long-lived secrets**, so avoid them.
- 🚩 Any option that says **"download a JSON private key"** for a VM **inside Google Cloud** is almost always **wrong**.
- **Metadata is not a secret store.** Anyone with access can read it.
- **Default Compute Engine service account = shared and too powerful.** Create a dedicated one per app (least privilege).
- **A VM has one attached service account.** To change it: **stop → `set-service-account` → start**.
- Set access scope to **`cloud-platform`** and control permissions with **IAM roles**.
- 🧠 *"**Give the robot its own badge (attach it). Never tape a key to the wall (metadata) or hide one in a drawer (file).**"*

---

## 🕵️ Follow-up: Debunking the "C is correct" Discussion Comments

**Comment 1:** *"A only works when creating the VM, so C is correct."* Then they posted `stop` → `set-service-account` → `start`.
- ❌ The question never says the VM already exists.
- ❌ Their commands **attach the service account**, which is the **same method as A** (on an existing VM). It's **not** option C (a JSON key in metadata). Their own commands disprove their answer.
- ✔️ The Console can also do it on an existing VM: stop → **Edit** → **Identity and API access** → change → start.

**Comment 2:** *"C is the recommended approach."*
- ❌ Compute Engine **doesn't read** any `compute-engine-service-account` metadata key. The VM keeps running as the **default** service account.
- ❌ They say B's key name is "not valid," but **C uses the same key name**. That's a contradiction.
- ❌ Google says **attach service accounts** and **avoid downloading keys**. Metadata is readable by others, so it's **not** a secret store.

| Situation | Correct method |
|---|---|
| New VM | Identity and API access / `--service-account` (option A) |
| Existing VM | Stop → change the service account (Console Edit or `set-service-account`) → Start |
| JSON key in metadata (B, C) | ❌ Doesn't work + security risk |
| JSON key file on disk (D) | ❌ Not used automatically + security risk |

🏢 *Commenter 1 is saying "HR only gives badges to new hires, so tape a key to the door." But HR can re-issue a badge to an existing employee too, if they stop by the desk for a minute (stop the VM).*

🧠 **Lesson:** "Selected Answer" and upvotes aren't proof. Check that the reasoning actually matches the option, and trust Google's best practices.

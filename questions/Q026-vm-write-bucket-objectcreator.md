# Q026: Letting VMs Write to One Bucket (Service Account + storage.objectCreator)

**Topic:** IAM + Cloud Storage (service accounts, bucket-level IAM roles `storage.objectCreator` vs `storage.objectAdmin`, legacy access scopes)

## ❓ Question
> You need to set up permissions for a set of Compute Engine instances to enable them to write data into a particular Cloud Storage bucket. You want to follow Google-recommended practices. What should you do?
>
> **A.** Create a service account with an access scope. Use the access scope 'https://www.googleapis.com/auth/devstorage.write_only'.
>
> **B.** Create a service account with an access scope. Use the access scope 'https://www.googleapis.com/auth/cloud-platform'.
>
> **C.** Create a service account and add it to the IAM role 'storage.objectCreator' for that bucket.
>
> **D.** Create a service account and add it to the IAM role 'storage.objectAdmin' for that bucket.

*(The `λ€˜ λ€™` characters in the screenshot are broken quote marks, shown here as `'`.)*

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** Some VMs need to **put files into one specific bucket**. That's all: **write**, into **that one bucket**. What's the Google-recommended way to give them that permission?

| Keyword | What it hints at |
|---|---|
| "**set of Compute Engine instances**" | Machines, not people, so use a **service account** attached to the VMs (Q019) |
| "**write data**" | Only **create objects**. They don't need to read, delete or manage anything, so use **`storage.objectCreator`** |
| "**a particular Cloud Storage bucket**" | Grant the role **on that bucket only**, not the whole project |
| "**Google-recommended practices**" | **IAM roles + least privilege**. Access scopes are a legacy method |

**Exam topic:** IAM and Cloud Storage permissions (least privilege for service accounts).

---

## 📚 Key Terms Explained

### 1️⃣ Compute Engine Instance (review)
- **What it is:** A **virtual computer** running in Google's data center.
- **Looks like:** `upload-worker-1` in `us-central1-a`, type `e2-medium`.
- **Not to be confused with:** a person. A VM can't sign in with a password, so it needs a **service account** to prove who it is.
- **Analogy:** 🖥️ A **company computer** sitting in the server room.
- **In the online store:** 3 VMs that create product thumbnails and save them.

### 2️⃣ Cloud Storage Bucket and Object (review)
- **What it is:** A **bucket** is a named container for files. Each file inside is an **object**.
- **Looks like:** `gs://shopnow-product-images/shoes/red-sneaker.jpg` (bucket = `shopnow-product-images`, object = `shoes/red-sneaker.jpg`)
- **Not to be confused with:** a disk attached to a VM. A bucket is reached **over the network** using permissions.
- **Analogy:** 📦 A **storage room** (bucket) full of **boxes** (objects).
- **In the online store:** Product photos live in `gs://shopnow-product-images`.

### 3️⃣ Service Account (review from Q019)
- **What it is:** A **Google account for a machine or app**, not a person. You **attach** it to VMs, and they use it automatically to call Google services.
- **Looks like:** `image-uploader@shopnow-prod.iam.gserviceaccount.com`
- **Not to be confused with:** a user account. It has **no password**, and nobody types it into a login screen. You also shouldn't download JSON keys for it when the code runs on Google Cloud.
- **Analogy:** 🪪 A **company ID badge issued to a machine**, like the badge clipped to the mail-sorting robot.
- **In the online store:** All 3 thumbnail VMs run as `image-uploader@…`.

### 4️⃣ IAM Role and "for that bucket" (resource-level grant)
- **What it is:** A **role** is a bundle of permissions. You can grant it on a **whole project** or on **one specific resource**, like **one bucket**. Granting on one bucket = access to **that bucket only**.
- **Looks like:**
  ```
  bucket gs://shopnow-product-images
    member: serviceAccount:image-uploader@shopnow-prod.iam.gserviceaccount.com
    role:   roles/storage.objectCreator
  ```
- **Not to be confused with:** a project-level grant, which would cover **every bucket** in the project.
- **Analogy:** 🔑 A key to **one room**, not a master key to the whole building.
- **In the online store:** The uploader can write to the images bucket but **can't touch** the `shopnow-invoices` bucket.

### 5️⃣ `roles/storage.objectCreator` vs `roles/storage.objectAdmin`
| | **objectCreator** ✅ | **objectAdmin** |
|---|---|---|
| Create (upload) new objects | ✅ | ✅ |
| Read / download objects | ❌ | ✅ |
| List objects | ❌ | ✅ |
| Delete or overwrite objects | ❌ | ✅ |
| Change object permissions | ❌ | ✅ |
- **What it is:** **objectCreator** = "can **add** new files, nothing else". **objectAdmin** = "**full control** of all files in the bucket".
- **Not to be confused with:** "write" meaning "edit". objectCreator **can't overwrite or delete** existing files. If the app must replace files with the same name, it needs more (e.g., `objectUser` or `objectAdmin`).
- **Analogy:** 📮 objectCreator = a **mail slot**: you can drop letters in, but you can't open the box. objectAdmin = **the key to the mailbox**: read, remove, replace, everything.

### 6️⃣ Access Scopes (legacy)
- **What it is:** An **older, extra on/off switch on a VM** that limits which **Google APIs** the VM may call. It is **not** a permission system: it **doesn't name a bucket**, and it **doesn't grant** anything by itself. **IAM roles** decide what the service account can actually do.
- **Looks like:** `https://www.googleapis.com/auth/devstorage.read_only`, `…/devstorage.read_write`, `…/cloud-platform`
- **Not to be confused with:** IAM roles. Google's recommendation is to set the scope to **`cloud-platform`** (allow all APIs) and control access with **IAM roles**.
- **Analogy:** 🚪 A **floor switch on the elevator** ("this badge may go to floors 2–5"). It doesn't unlock any room. The **room keys (IAM)** do that.
- **In the online store:** The thumbnail VMs use the `cloud-platform` scope, and IAM limits them to one bucket.

### 🔗 How They Fit Together
```
🖥️ VM upload-worker-1 ┐
🖥️ VM upload-worker-2 ├── run as 🪪 service account image-uploader@shopnow-prod.iam.gserviceaccount.com
🖥️ VM upload-worker-3 ┘        (access scope: cloud-platform; IAM does the real limiting)
                                   │
                                   │ IAM role granted ON THE BUCKET (not the project)
                                   ▼
        📦 gs://shopnow-product-images   ← roles/storage.objectCreator  ✅ upload only
        📦 gs://shopnow-invoices         ← (no role)                     ❌ no access
```

---

## 🌍 Real-World Scenario

Apps often have **workers that only produce files**: thumbnail generators, log shippers, nightly backup jobs, report exporters. The **security rule** is: give them **exactly** what they need. They need to **add files to one bucket**. They don't need to **read customer files, delete backups, or touch other buckets**.

If a worker is ever hacked, a minimal role means the attacker **can't read or delete** anything. They can only add files to one bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a service account with an access scope. Use the access scope 'https://www.googleapis.com/auth/devstorage.write_only'.

**Why it's wrong:**
- ❌ **Access scopes are the legacy way**. Google recommends **IAM roles** to control access.
- ❌ A scope **can't point to one bucket**. It covers Cloud Storage **in general**.
- ❌ **`devstorage.write_only` doesn't even exist.** The real storage scopes are `read_only`, `read_write` and `full_control`.

**📌 When to use it:** **Never use this.** The scope doesn't exist. Use an IAM role on the bucket (C).
🏢 **Office example:** Asking reception for a "write-only" elevator pass that the building doesn't offer.

### ❌ B
> **B.** Create a service account with an access scope. Use the access scope 'https://www.googleapis.com/auth/cloud-platform'.

**Why it's wrong:**
- ✔️ `cloud-platform` is actually the scope Google recommends setting on VMs…
- ❌ …but **only together with IAM roles**. A scope **grants nothing by itself**. Without an IAM role on the bucket, the VMs **still can't write**, and nothing limits them to **that** bucket.

**📌 When to use it:** Use the `cloud-platform` scope on VMs as the normal setting, then control access with IAM roles.
🏢 **Office example:** An elevator pass that lets you reach every floor, but you still need a room key to open any door.

### ✅ C (your answer)
> **C.** Create a service account and add it to the IAM role 'storage.objectCreator' for that bucket.

**Why it's correct:**
- ✔️ **Service account** = the right identity for VMs (attach it to the instances).
- ✔️ **IAM role** = the recommended way to grant access.
- ✔️ **`storage.objectCreator`** = can **create objects only**, exactly "write data". That's **least privilege**.
- ✔️ **"For that bucket"** = granted on **one bucket**, not every bucket in the project.

**📌 When to use it:** Use it when machines only need to drop files into one place and should not read or delete anything.
🏢 **Office example:** Giving the night courier access to the mail slot of one office. They can drop envelopes in, but they can't open the box.

### ❌ D
> **D.** Create a service account and add it to the IAM role 'storage.objectAdmin' for that bucket.

**Why it's wrong:**
- ✔️ Service account + IAM role on the bucket is the right method…
- ❌ …but **`objectAdmin` is far too much**: read, list, **delete**, **overwrite** and change permissions on every object. The VMs only need to **write**. That breaks **least privilege**.

**📌 When to use it:** Use objectAdmin when an app or person must fully manage the files in a bucket, including deleting and replacing them.
🏢 **Office example:** The records manager who holds the key to the archive room and can add, read, move or shred any file.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow has **3 thumbnail VMs**. When a seller uploads a product photo, these VMs make small versions and **save them** to `gs://shopnow-product-images`.

**1. Create the service account:**
```bash
gcloud iam service-accounts create image-uploader \
  --display-name="Thumbnail workers" --project=shopnow-prod
```

**2. Grant objectCreator on that bucket only:**
```bash
gcloud storage buckets add-iam-policy-binding gs://shopnow-product-images \
  --member="serviceAccount:image-uploader@shopnow-prod.iam.gserviceaccount.com" \
  --role="roles/storage.objectCreator"
```

**3. Attach it to the VMs** (Q019), using the recommended `cloud-platform` scope:
```bash
gcloud compute instances create upload-worker-1 --zone=us-central1-a \
  --service-account=image-uploader@shopnow-prod.iam.gserviceaccount.com \
  --scopes=cloud-platform
```

**4. What the VMs can and can't do:**
| Action | Result |
|---|---|
| Upload `thumbs/red-sneaker-200px.jpg` to `shopnow-product-images` | ✅ Allowed |
| Download a customer's invoice from `shopnow-invoices` | ❌ Denied (no role on that bucket) |
| Delete product photos | ❌ Denied (objectCreator can't delete) |
| List everything in the bucket | ❌ Denied |

**🎬 With option D:** A bug in the thumbnail code runs "clean up old files" and, because it has **objectAdmin**, **deletes every product photo**. The storefront shows broken images. With **objectCreator**, that delete would have been **blocked**. ✅

---

## 🧠 Key Takeaways / Memory Tips

- **VMs need access → service account + IAM role** (not access scopes, not JSON keys).
- **Least privilege:** "write/upload only" → **`storage.objectCreator`**. "Full control of files" → `storage.objectAdmin`.
  🧠 *"**Creator creates. Admin does everything.**"*
- **Grant on the bucket**, not the project, when the question says "**a particular bucket**".
- **Access scopes = legacy elevator switch.** Set `cloud-platform` and let **IAM** decide. And `devstorage.write_only` doesn't exist.
- Related: **Q019** (attach a service account to a VM), **Q025** (pick the smallest predefined role).

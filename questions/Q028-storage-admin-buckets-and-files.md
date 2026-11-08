# Q028: Letting Colleagues Manage Buckets AND Files (Storage Admin)

**Topic:** IAM + Cloud Storage (`roles/storage.admin` vs `roles/storage.objectAdmin` vs `roles/storage.objectCreator` vs basic `roles/editor`)

## ❓ Question
> You are the project owner of a GCP project and want to delegate control to colleagues to manage buckets and files in Cloud Storage. You want to follow Google-recommended practices. Which IAM roles should you grant your colleagues?
>
> **A.** Project Editor
>
> **B.** Storage Admin
>
> **C.** Storage Object Admin
>
> **D.** Storage Object Creator

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You own a project and want colleagues to manage buckets and the files in them in Cloud Storage.
- **What you must achieve:** Give them the right permissions.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** Which IAM roles let them manage buckets and files?

| Keyword | What it hints at |
|---|---|
| "**manage buckets**" | They need to create, delete and configure **buckets**, which only **Storage Admin** covers |
| "**and files**" | They also need full control of the **objects** (files) |
| "**in Cloud Storage**" | Only storage, not VMs, databases or the rest of the project, so **not Project Editor** |
| "**Google-recommended practices**" | **Least privilege** + **predefined roles** over broad **basic roles** (Owner/Editor/Viewer) |

**Exam topic:** IAM roles for Cloud Storage (least privilege).

---

## 📚 Key Terms Explained

### 1️⃣ Bucket vs Object (review from Q026)
- **What it is:** A **bucket** is a named **container** in Cloud Storage. An **object** is **one file** inside a bucket.
- **Looks like:** `gs://shopnow-product-images/shoes/red-sneaker.jpg` → bucket = `shopnow-product-images`, object = `shoes/red-sneaker.jpg`
- **Not to be confused with:** a folder. "Managing buckets" means creating/deleting the **containers themselves** and changing their **settings** (location, storage class, lifecycle rules, bucket permissions), which is a different job from managing the **files**.
- **Analogy:** 📦 A bucket is a **storage room**. Objects are the **boxes** on its shelves.
- **In the online store:** `shopnow-product-images`, `shopnow-invoices`, `shopnow-backups` are three buckets.

### 2️⃣ Basic Role: Project Editor (`roles/editor`)
- **What it is:** An old, **very broad** role that can **change almost everything in the whole project**: VMs, databases, networks, storage, and more.
- **Looks like:** `member: user:ken@shopnow.com  role: roles/editor  (on project shopnow-prod)`
- **Not to be confused with:** a storage role. Editor isn't "editor of storage", it's **editor of the entire project**.
- **Analogy:** 🗝️ A **master key to the whole building**, just to clean one storage room.
- **In the online store:** Someone with Editor could delete the checkout VMs or the orders database by mistake.

### 3️⃣ Storage Admin (`roles/storage.admin`) ✅
- **What it is:** A **predefined role** with **full control of Cloud Storage**: create, delete and configure **buckets**, and read, upload, delete **objects**. Nothing outside Cloud Storage.
- **Looks like:** `member: group:storage-team@shopnow.com  role: roles/storage.admin`
- **Not to be confused with:** Storage **Object** Admin. The word **"Object"** means **files only**, while plain "Storage Admin" means **buckets + files**.
- **Analogy:** 🏬 The **storage-rooms manager**: can open new storage rooms, close them, set the rules, and handle every box inside. Has no key to the offices.
- **In the online store:** The storage team creates a new bucket `shopnow-returns-labels` and sets a lifecycle rule on `shopnow-backups`.

### 4️⃣ Storage Object Admin (`roles/storage.objectAdmin`)
- **What it is:** Full control of **objects (files)**: read, upload, overwrite, delete, change file permissions. It **can't create or delete buckets** or change bucket settings.
- **Looks like:** Can run `gcloud storage rm gs://shopnow-backups/old.sql`, but `gcloud storage buckets create gs://new-bucket` is **denied**.
- **Not to be confused with:** Storage Admin. It's **files-only**, not buckets.
- **Analogy:** 📦 A **warehouse worker** who can move, add or throw away any box, but **can't build or close a storage room**.
- **In the online store:** A cleanup job that deletes old backup files.

### 5️⃣ Storage Object Creator (`roles/storage.objectCreator`) (review from Q026)
- **What it is:** Can **only upload new files**. It can't read, list, delete or overwrite them, and can't touch buckets.
- **Looks like:** Upload `thumbs/red-sneaker-200px.jpg` ✅, download it ❌
- **Not to be confused with:** "manage". It's the **smallest** storage role, an upload-only permission.
- **Analogy:** 📮 A **mail slot**: drop letters in, never take them out.
- **In the online store:** The thumbnail VMs from Q026.

### 🔗 How They Fit Together
```
Most power ▲
           │  roles/editor (basic)         → whole PROJECT: VMs, DBs, networks, storage… ❌ too much
           │  roles/storage.admin          → BUCKETS + FILES  ✅ exactly "manage buckets and files"
           │  roles/storage.objectAdmin    → FILES only (no creating/deleting buckets)
           │  roles/storage.objectCreator  → UPLOAD files only
Least power▼

"Object" in the role name = files only. No "Object" = buckets too.
```

---

## 🌍 Real-World Scenario

The project owner is busy. A **storage/data team** needs to set up buckets for new features, change retention and lifecycle rules, clean up old files, and fix file permissions. The owner wants to **hand over all of Cloud Storage** without handing over the **rest of the project** (VMs, databases, billing-heavy services). Giving **Owner** or **Editor** would be the lazy, risky shortcut. Google recommends the **predefined role that fits the job**: Storage Admin.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Project Editor

**Why it's wrong:**
- ✔️ It *would* let them manage buckets and files…
- ❌ …but it also lets them change **almost everything else in the project** (VMs, databases, networks). That breaks **least privilege**.
- ❌ Google recommends **predefined roles** over **basic roles** (Owner/Editor/Viewer) in production.

**📌 When to use it:** Use it only in a small test project where one trusted person needs to change almost everything.
🏢 **Office example:** Giving the master key to the whole office to a manager who runs every department.

### ✅ B (your answer)
> **B.** Storage Admin

**Why it's correct:**
- ✔️ Covers **buckets** (create, delete, settings, bucket permissions) **and files** (read, upload, delete), exactly what was asked.
- ✔️ Limited to **Cloud Storage only**. No access to VMs, databases, etc.
- ✔️ A **predefined role**, maintained by Google, which is the recommended practice.

**📌 When to use it:** Use it when someone must take care of all the storage rooms and everything inside them, but nothing else.
🏢 **Office example:** The records manager who can open new file rooms, set the rules, and handle every folder, but has no key to the finance office.

### ❌ C
> **C.** Storage Object Admin

**Why it's wrong:**
- ✔️ Full control of **files**…
- ❌ …but it **can't create, delete or configure buckets**. The question says "manage **buckets** and files".
- 💡 **Common trap:** "Object Admin" sounds like "admin of everything in storage". The word **Object** = **files only**.

**📌 When to use it:** Use it when someone needs to add, replace and delete files in existing storage, but should not create or remove the storage rooms themselves.
🏢 **Office example:** The filing clerk who can add, move or shred folders, but can't open a new file room.

### ❌ D
> **D.** Storage Object Creator

**Why it's wrong:**
- ❌ Can only **upload new files**. It can't read, delete, or manage files, and can't touch buckets. Far too little.

**📌 When to use it:** Use it when someone or something only needs to drop new files in and never read or remove them.
🏢 **Office example:** The night courier who can drop envelopes through the mail slot but can't open the mailbox.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's owner (you) hands Cloud Storage to the **platform team** (`storage-team@shopnow.com`, a Google group, as in Q025).

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member="group:storage-team@shopnow.com" \
  --role="roles/storage.admin"
```

**What the platform team can and can't do:**
| Action | Storage Admin (B) | Object Admin (C) | Editor (A) |
|---|---|---|---|
| Create bucket `gs://shopnow-returns-labels` | ✅ | ❌ | ✅ |
| Add a lifecycle rule to `shopnow-backups` (Q020) | ✅ | ❌ | ✅ |
| Delete an old file in `shopnow-backups` | ✅ | ✅ | ✅ |
| Delete the checkout VM `api-orders-03` | ❌ | ❌ | ⚠️ ✅ (dangerous!) |
| Drop the Cloud SQL orders database | ❌ | ❌ | ⚠️ ✅ (dangerous!) |

**🎬 With option A:** A teammate cleaning up "unused resources" deletes a VM they thought was a test machine. It was a checkout server, and Black Friday orders fail. With **Storage Admin**, that delete would have been **blocked**. ✅

---

## 🧠 Key Takeaways / Memory Tips

- **"Manage buckets AND files" → `roles/storage.admin`.**
  **"Manage files only" → `roles/storage.objectAdmin`.**
  **"Upload only" → `roles/storage.objectCreator`.**
- 🧠 *"**Object** in the name = **files only**. No 'Object' = **buckets too**."*
- **Avoid basic roles (Owner/Editor/Viewer)** when a predefined role fits. They cover the whole project.
- Ladder from small to big: **objectViewer → objectCreator → objectAdmin → storage.admin → editor**. Pick the **lowest step** that does the job.
- Related: **Q026** (objectCreator for upload-only VMs), **Q025** (predefined roles + groups).

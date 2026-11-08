# G005: Move a Windows SMB File Server With AD Permissions, Snapshots and Clones, Fully Managed (Google Cloud NetApp Volumes)

**Topic:** Storage (NetApp Volumes)
**Exam guide section:** 2.2 Planning and implementing storage: Choosing storage products (Filestore, NetApp Volumes, Managed Lustre)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You are migrating an on-premises Windows file server to Google Cloud. Employees access shared folders over the SMB protocol with Active Directory permissions, and administrators rely on fast volume snapshots and clones. You want a fully managed service and do not want to manage file server VMs. What should you use?
>
> **A.** A Compute Engine Windows Server VM with a large Persistent Disk shared as a network folder.
>
> **B.** A Cloud Storage bucket with uniform bucket-level access.
>
> **C.** Google Cloud NetApp Volumes with an SMB volume joined to Active Directory.
>
> **D.** A Filestore Basic instance.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Office staff use a Windows file server for shared folders, reached over SMB (the Windows file-sharing protocol, the thing behind mapped drives like `S:\`). Who can open what is controlled by Active Directory (the company's Windows user directory).
- **What you must achieve:** Move those shared folders to Google Cloud and keep the same Windows access, plus quick snapshots (point-in-time copies) and clones (instant writable copies).
- **The limits:** It must be fully managed. You don't want to run and patch your own file-server VMs.
- **What they're really asking:** Which managed Google Cloud file service speaks SMB, works with Active Directory, and has snapshots and clones?

**Clues in the question:**
- "**SMB protocol with Active Directory permissions**": Windows file sharing. Filestore is NFS only.
- "**fast volume snapshots and clones**": NetApp ONTAP-style features.
- "**fully managed … do not want to manage file server VMs**" rules out a self-run Windows VM.

**Exam topic:** Storage choice (exam guide section 2.2).

---

## 📚 Key Terms Explained

### 1. SMB
- **What it is:** The file-sharing protocol Windows uses for network drives.
- **Looks like:** `\\files.shopnow.local\finance` mapped as `S:`
- **Not to be confused with:** NFS, which is the Linux/Unix file-sharing protocol.
- **Analogy:** 🚪 The office's Windows-style door to the shared cabinet.
- **In the online store:** Finance staff open spreadsheets from `S:\`.

### 2. Google Cloud NetApp Volumes 🔑
- **What it is:** A fully managed file storage service built on NetApp's technology. It serves **NFS and SMB** volumes, joins Active Directory, and offers instant snapshots, clones and replication.
- **Looks like:** Storage pool `finance-pool` → volume `finance` (SMB, AD-joined), snapshot policy hourly
- **Not to be confused with:** Filestore (NFS only) and Managed Lustre (for AI/HPC speed).
- **Analogy:** 🏬 A professionally managed shared filing room that speaks Windows.
- **In the online store:** Back-office shares for finance and HR.

### 3. Snapshot / clone
- **What it is:** A snapshot is a read-only point-in-time copy. A clone is a new writable volume made instantly from a snapshot.
- **Looks like:** `snap-2026-11-08-0900` → clone `finance-test`
- **Not to be confused with:** A backup to a different location (which takes longer and is stored separately).
- **Analogy:** 📸 A photo of the cabinet, and a copy cabinet made from the photo.
- **In the online store:** Restore a deleted spreadsheet from the 09:00 snapshot.

### 🔗 How they fit together
```
 Windows PCs ──SMB (AD login)──► NetApp Volumes SMB volume "finance" ✅
                                    ├─ hourly snapshots
                                    └─ clone for testing
```

---

## 🌍 Real-World Scenario

A company's back office still uses a 10-year-old Windows file server. Moving it to Google Cloud with **NetApp Volumes** keeps the same `S:` drive and AD permissions. Admins stop patching servers, and a deleted file is restored from a snapshot in seconds.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** A Compute Engine Windows Server VM with a large Persistent Disk shared as a network folder.

**Wrong words:**
- ✔️ It would speak SMB.
- ❌ "**Compute Engine Windows Server VM**": you'd patch, back up and run the server yourself, which breaks "**do not want to manage file server VMs**".

📌 **When to use it:** Use it when you need full control of a Windows server and accept the upkeep.
🏢 **Office example:** Hiring your own file clerk instead of a managed records service.

### ❌ B
> **B.** A Cloud Storage bucket with uniform bucket-level access.

**Wrong words:**
- ❌ "**Cloud Storage bucket**": object storage. Windows users can't map it as an SMB drive with AD permissions.

📌 **When to use it:** Use it for files apps fetch by name, such as images and backups.
🏢 **Office example:** A warehouse where you order boxes by label, not a shared drawer.

### ✅ C
> **C.** Google Cloud NetApp Volumes with an SMB volume joined to Active Directory.

**Why it's correct:**
- ✔️ "**NetApp Volumes with an SMB volume**" matches "**SMB protocol**".
- ✔️ "**joined to Active Directory**" matches "**Active Directory permissions**".
- ✔️ NetApp Volumes is fully managed and has fast snapshots and clones, matching "**fully managed**" and "**snapshots and clones**".

📌 **When to use it:** Use it when Windows users need managed shared drives with their usual company logins and quick restore copies.
🏢 **Office example:** Moving the shared office cabinet into a managed records room that still uses everyone's normal staff badge.

### ❌ D
> **D.** A Filestore Basic instance.

**Wrong words:**
- ❌ "**Filestore Basic**": Filestore serves **NFS**, not SMB, so Windows AD-permissioned shares don't fit.

📌 **When to use it:** Use it for Linux servers sharing an NFS folder.
🏢 **Office example:** A shared cabinet whose lock only takes the other kind of key.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** back office:
- NetApp Volumes SMB volume `finance`, joined to `corp.shopnow.local`.
- Hourly snapshots kept 7 days. A clone `finance-uat` is used for testing new accounting software.
- Storefront containers keep using Cloud Storage for product images.

---

## 🧠 Key Takeaways / Memory Tips

- **Windows SMB + AD + snapshots/clones + managed → NetApp Volumes.**
- Filestore = NFS. Lustre = AI/HPC speed. NetApp = enterprise NFS/SMB features.
  🧠 *"**Windows share? NetApp.**"*
- Related: **Q299**, **G004**.

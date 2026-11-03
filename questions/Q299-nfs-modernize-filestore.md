# Q299: Modernize a Shared NFS Server With Least App Change (Filestore)

**Topic:** Storage (Filestore)

## ❓ Question
> Your company has many legacy third-party applications that rely on a shared NFS server for file sharing between these workloads. You want to modernize the NFS server by using a Google Cloud managed service. You need to select the solution that requires the least amount of change to the application. What should you do?
>
> **A.** Create a Compute Engine instance and configure an NFS server on the instance. Point all NFS mounts to the Compute Engine instance.
>
> **B.** Deploy a Filestore instance. Replace all NFS mounts with a Filestore mount.
>
> **C.** Configure Firestore. Configure all applications to use Firestore instead of the NFS server.
>
> **D.** Create a Cloud Storage bucket. Configure all applications to use Cloud Storage client libraries instead of the NFS server.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Replace an NFS server with a **managed** service, **no app changes**.

**Clues in the question:**
- "**NFS**" + "**managed service**" + "**least amount of change**" → **Filestore** (managed NFS; apps just mount a new path).

**Exam topic:** Storage.

---

## 📚 Key Terms Explained

### 1. Filestore 🔑
- **What it is:** Google's managed **NFS file server**; VMs/GKE mount it like any NFS share.
- **Looks like:** `sudo mount 10.0.0.2:/share /mnt/shared`
- **Not to be confused with:** Firestore (database).
- **Analogy:** 🗂️ A managed shared network drive.
- **In the online store:** Shared uploads folder.

### 🔗 How they fit together
```
 apps ─ NFS mount ─► Filestore (managed) ✅ (same protocol, no code change)
```

---

## 🌍 Real-World Scenario

Legacy apps share files over NFS. The team creates a **Filestore** share and changes the mount target; no code changes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Compute Engine instance and configure an NFS server on the instance. Point all NFS mounts to the Compute Engine instance.

**Wrong words:**
- ❌ "**Compute Engine instance … NFS server**": works, but not a managed service — you patch and run it.

📌 **When to use it:** Use self-managed NFS only for special configs.
🏢 **Office example:** Running your own file room.

### ✅ B
> **B.** Deploy a Filestore instance. Replace all NFS mounts with a Filestore mount.

**Why it's correct:**
- ✔️ "**Deploy a Filestore instance**" matches "**Google Cloud managed service**".
- ✔️ "**Replace all NFS mounts with a Filestore mount**" matches "**least amount of change to the application**": same NFS protocol.

📌 **When to use it:** Use it when programs already share files over a network drive and you want someone else to run the drive.
🏢 **Office example:** Swapping your old shared drive for a managed one with the same drive letter.

### ❌ C
> **C.** Configure Firestore. Configure all applications to use Firestore instead of the NFS server.

**Wrong words:**
- ❌ "**Firestore**": a database; apps would need rewriting.

📌 **When to use it:** Use Firestore for app documents.
🏢 **Office example:** Replacing a filing cabinet with a database form.

### ❌ D
> **D.** Create a Cloud Storage bucket. Configure all applications to use Cloud Storage client libraries instead of the NFS server.

**Wrong words:**
- ❌ "**Cloud Storage client libraries**": code changes in every app.

📌 **When to use it:** Use Cloud Storage for object storage in new apps.
🏢 **Office example:** Making every program learn a new filing system.

---

## 🛒 E-Commerce Full-Stack Example

Filestore `shared-media` (1 TiB) mounted by legacy image-processing VMs at `/mnt/media`.

---

## 🧠 Key Takeaways / Memory Tips

- **Managed NFS with no app change → Filestore.**
  🧠 *"**NFS? Filestore (not Firestore).**"*
- Related: **Q290**.

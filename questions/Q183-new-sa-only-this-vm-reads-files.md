# Q183: Only the New VM May Read the Install Files (New Service Account for It + Storage Permissions)

**Topic:** IAM (dedicated service accounts vs default service account)

## ❓ Question
> You need to manage a third-party application that will run on a Compute Engine instance. Other Compute Engine instances are already running with default configuration. Application installation files are hosted on Cloud Storage. You need to access these files from the new instance without allowing other virtual machines (VMs) to access these files. What should you do?
>
> **A.** Create the instance with the default Compute Engine service account. Grant the service account permissions on Cloud Storage.
>
> **B.** Create the instance with the default Compute Engine service account. Add metadata to the objects on Cloud Storage that matches the metadata on the new instance.
>
> **C.** Create a new service account and assign this service account to the new instance. Grant the service account permissions on Cloud Storage.
>
> **D.** Create a new service account and assign this service account to the new instance. Add metadata to the objects on Cloud Storage that matches the metadata on the new instance.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will run a third-party app on a new VM. Other VMs already run with default settings. The install files are in Cloud Storage.
- **What you must achieve:** Let only the new VM read those files.
- **The limits:** Other VMs must not be able to read them.
- **What they're really asking:** How do you give just the new VM access to the files?

**Clues in the question:**
- "**Other Compute Engine instances are already running with default configuration**" → they share the **default SA**. Granting it would give them access too.
- "**without allowing other VMs**" → a **new, dedicated SA** with the storage permission.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Default Compute Engine service account 🔑
- **What it is:** `PROJECT_NUMBER-compute@developer.gserviceaccount.com`, used by **every VM** created with defaults.
- **Looks like:** `123456789-compute@developer.gserviceaccount.com`
- **Not to be confused with:** a dedicated SA.
- **Analogy:** 🪪 One badge every new hire gets.
- **In the online store:** Old test VMs.

### 2. Dedicated service account
- **What it is:** A service account made for **one** app, so its rights apply only there.
- **Looks like:** `thirdparty-sa@proj.iam.gserviceaccount.com`
- **Not to be confused with:** the default SA.
- **Analogy:** 🪪 A special badge for one contractor.
- **In the online store:** ShopNow's ERP connector VM.

### 🔗 How they fit together
```
 other VMs → default SA (no bucket access)
 new VM → thirdparty-sa → objectViewer on gs://installers ✅
```

---

## 🌍 Real-World Scenario

A vendor's software installers sit in a bucket. The admin creates `vendor-sa`, attaches it to the new VM, and grants it **Storage Object Viewer** on that bucket. Other VMs (default SA) can't read it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create the instance with the default Compute Engine service account. Grant the service account permissions on Cloud Storage.

**Wrong words:**
- ❌ "**default Compute Engine service account … Grant … permissions**": every other VM uses that same SA, so they'd all get access.

📌 **When to use it:** Use the default SA only for quick tests.
🏢 **Office example:** Giving the storeroom key to the badge every employee has.

### ❌ B
> **B.** Create the instance with the default Compute Engine service account. Add metadata to the objects on Cloud Storage that matches the metadata on the new instance.

**Wrong words:**
- ❌ "**default … service account**" (shared) and ❌ "**Add metadata to the objects**": metadata doesn't control access.

📌 **When to use it:** **Never use this** for access control.
🏢 **Office example:** Writing "for Bob only" on a box in an unlocked room.

### ✅ C
> **C.** Create a new service account and assign this service account to the new instance. Grant the service account permissions on Cloud Storage.

**Why it's correct:**
- ✔️ "**Create a new service account and assign this service account to the new instance**" matches "**from the new instance without allowing other virtual machines**".
- ✔️ "**Grant the service account permissions on Cloud Storage**" matches "**access these files**".

📌 **When to use it:** Use it when only one machine should be allowed to open certain files.
🏢 **Office example:** A special badge just for the contractor that opens the one storeroom they need.

### ❌ D
> **D.** Create a new service account and assign this service account to the new instance. Add metadata to the objects on Cloud Storage that matches the metadata on the new instance.

**Wrong words:**
- ✔️ "new service account" is right.
- ❌ "**Add metadata to the objects**": metadata doesn't grant access, so the SA still can't read the files.

📌 **When to use it:** Use object metadata for things like content type.
🏢 **Office example:** Labels on boxes instead of an access badge.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud iam service-accounts create erp-connector-sa
gcloud compute instances create erp-connector --service-account=erp-connector-sa@shopnow-prod.iam.gserviceaccount.com --scopes=cloud-platform
gsutil iam ch serviceAccount:erp-connector-sa@shopnow-prod.iam.gserviceaccount.com:objectViewer gs://shopnow-vendor-installers
```

---

## 🧠 Key Takeaways / Memory Tips

- **Only one VM should have access → dedicated service account**, not the shared default one.
  🧠 *"**Shared badge = shared access; new badge = just you.**"*
- Related: **Q176**, **Q134**.

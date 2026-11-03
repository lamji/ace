# Q211: External Member Needs Only List Access to Images and Disks (Custom Role With Exactly Those Permissions)

**Topic:** IAM (custom roles, least privilege)

## ❓ Question
> An external member of your team needs list access to compute images and disks in one of your projects. You want to follow Google-recommended practices when you grant the required permissions to this user. What should you do?
>
> **A.** Create a custom role, and add all the required compute.disks.list and compute.images.list permissions as includedPermissions. Grant the custom role to the user at the project level.
>
> **B.** Create a custom role based on the Compute Image User role. Add the compute.disks.list to the includedPermissions field. Grant the custom role to the user at the project level.
>
> **C.** Create a custom role based on the Compute Storage Admin role. Exclude unnecessary permissions from the custom role. Grant the custom role to the user at the project level.
>
> **D.** Grant the Compute Storage Admin role at the project level.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between A and B. Most Voted is **A**: a custom role with **exactly** the two list permissions is the tightest least-privilege fit. B starts from Compute Image User, which also lets the user **use** images (`compute.images.useReadOnly`), more than "list".

---

## 📖 What the Question Is Asking

**In plain words:** An outsider should only **list** images and disks.

**Clues in the question:**
- "**list access to compute images and disks**" + "**Google-recommended practices**" (least privilege) → a **custom role with only** `compute.disks.list` and `compute.images.list`.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Custom role 🔑 (review from Q158)
- **What it is:** A role you define with exactly the permissions you list.
- **Looks like:** `gcloud iam roles create diskImageLister --project=p --permissions=compute.disks.list,compute.images.list`
- **Not to be confused with:** predefined roles.
- **Analogy:** 🔑 A key cut for exactly two drawers.
- **In the online store:** Auditor role.

### 2. includedPermissions
- **What it is:** The field in a custom role that lists its permissions.
- **Looks like:** `includedPermissions: [compute.disks.list, compute.images.list]`
- **Not to be confused with:** —
- **Analogy:** 📋 The key's list of doors.
- **In the online store:** —

### 🔗 How they fit together
```
 custom role {compute.disks.list, compute.images.list} → user@partner.com (project) ✅
```

---

## 🌍 Real-World Scenario

A contractor must inventory disks and images. The admin creates a **custom role** with just the two list permissions and grants it on the project.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a custom role, and add all the required compute.disks.list and compute.images.list permissions as includedPermissions. Grant the custom role to the user at the project level.

**Why it's correct:**
- ✔️ "**custom role … compute.disks.list and compute.images.list**" matches "**list access to compute images and disks**": nothing extra.
- ✔️ "**Grant the custom role to the user at the project level**" matches "**in one of your projects**".

📌 **When to use it:** Use it when someone needs a very specific small permission that no standard role matches.
🏢 **Office example:** Cutting a key that opens only the two cabinets the visitor needs to look into.

### ❌ B
> **B.** Create a custom role based on the Compute Image User role. Add the compute.disks.list to the includedPermissions field. Grant the custom role to the user at the project level.

**Wrong words:**
- ✔️ "custom role … compute.disks.list" is close.
- ❌ "**based on the Compute Image User role**": that role also allows **using** images, more than listing.

📌 **When to use it:** Use Compute Image User when someone must create VMs from shared images.
🏢 **Office example:** A key cut from a pattern that opens one extra drawer.

### ❌ C
> **C.** Create a custom role based on the Compute Storage Admin role. Exclude unnecessary permissions from the custom role. Grant the custom role to the user at the project level.

**Wrong words:**
- ❌ "**based on the Compute Storage Admin role**": starts from an admin role and relies on trimming; easy to leave too much.

📌 **When to use it:** Use it only if starting from admin is truly needed.
🏢 **Office example:** Copying the master key and filing it down.

### ❌ D
> **D.** Grant the Compute Storage Admin role at the project level.

**Wrong words:**
- ❌ "**Compute Storage Admin**": can create and delete disks/snapshots. Far more than list.

📌 **When to use it:** Use it for storage administrators.
🏢 **Office example:** Handing the storeroom master key to a visitor.

---

## 🛒 E-Commerce Full-Stack Example

Custom role `shopnowDiskImageViewer` (compute.disks.list, compute.images.list) → `user:auditor@partnerfirm.com` on `shopnow-prod`.

---

## 🧠 Key Takeaways / Memory Tips

- **Exact small permission set → custom role with just those permissions.**
  🧠 *"**Only what's asked, nothing more.**"*
- Related: **Q158**, **Q128**.

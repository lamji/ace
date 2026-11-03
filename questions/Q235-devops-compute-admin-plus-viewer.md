# Q235: DevOps Needs Full Compute Control, Nothing Else Writable (Viewer + Compute Admin)

**Topic:** IAM (basic vs predefined roles)

## ❓ Question
> The DevOps group in your organization needs full control of Compute Engine resources in your development project. However, they should not have permission to create or update any other resources in the project. You want to follow Google's recommendations for setting permissions for the DevOps group. What should you do?
>
> **A.** Grant the basic role roles/viewer and the predefined role roles/compute.admin to the DevOps group.
>
> **B.** Create an IAM policy and grant all compute.instanceAdmin.* permissions to the policy. Attach the policy to the DevOps group.
>
> **C.** Create a custom role at the folder level and grant all compute.instanceAdmin.* permissions to the role. Grant the custom role to the DevOps group.
>
> **D.** Grant the basic role roles/editor to the DevOps group.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Full** Compute control, **no** write access elsewhere.

**Clues in the question:**
- "**full control of Compute Engine**" → **roles/compute.admin** (predefined).
- "**should not … create or update any other resources**" → **viewer** elsewhere is read-only; Editor would be too much.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/compute.admin 🔑
- **What it is:** Predefined role with **full control** of Compute Engine resources.
- **Looks like:** `--role=roles/compute.admin`
- **Not to be confused with:** instanceAdmin (VMs only).
- **Analogy:** 🔧 Master key to the machine room.
- **In the online store:** ShopNow SRE.

### 2. roles/viewer
- **What it is:** Basic role: **read-only** across the project.
- **Looks like:** —
- **Not to be confused with:** editor.
- **Analogy:** 👀 Look, don't touch.
- **In the online store:** —

### 🔗 How they fit together
```
 group:devops → roles/viewer (read everything) + roles/compute.admin (full Compute) ✅
```

---

## 🌍 Real-World Scenario

The DevOps group gets **Compute Admin** for VMs, disks and networks, and **Viewer** so they can see other resources without changing them.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Grant the basic role roles/viewer and the predefined role roles/compute.admin to the DevOps group.

**Why it's correct:**
- ✔️ "**predefined role roles/compute.admin**" matches "**full control of Compute Engine resources**".
- ✔️ "**basic role roles/viewer**" is read-only, which matches "**should not have permission to create or update any other resources**".

📌 **When to use it:** Use it when a team must run one area fully but only look at everything else.
🏢 **Office example:** A master key to the machine room plus a visitor pass to look around the rest of the building.

### ❌ B
> **B.** Create an IAM policy and grant all compute.instanceAdmin.* permissions to the policy. Attach the policy to the DevOps group.

**Wrong words:**
- ❌ "**Create an IAM policy and grant … permissions to the policy**": permissions go into **roles**, not directly into policies.
- ❌ "**instanceAdmin**" covers instances, not all of Compute (e.g. networks/firewalls).

📌 **When to use it:** **Not how IAM works.**
🏢 **Office example:** Writing permissions on the door instead of on a badge.

### ❌ C
> **C.** Create a custom role at the folder level and grant all compute.instanceAdmin.* permissions to the role. Grant the custom role to the DevOps group.

**Wrong words:**
- ❌ "**custom role … compute.instanceAdmin.\***": not full Compute control, and custom roles add maintenance when a predefined one fits.

📌 **When to use it:** Use custom roles when no predefined role fits.
🏢 **Office example:** Cutting a custom key that still misses some rooms.

### ❌ D
> **D.** Grant the basic role roles/editor to the DevOps group.

**Wrong words:**
- ❌ "**roles/editor**": can create/update almost everything in the project.

📌 **When to use it:** Use Editor only for small trusted sandboxes.
🏢 **Office example:** A master key to the whole building.

---

## 🛒 E-Commerce Full-Stack Example

`group:devops@shopnow.com` → `roles/compute.admin` + `roles/viewer` on `shopnow-dev`.

---

## 🧠 Key Takeaways / Memory Tips

- **Full control of one service, read-only elsewhere → predefined service admin + Viewer.**
  🧠 *"**Admin where you work, viewer where you watch.**"*
- Related: **Q158**, **Q215**.

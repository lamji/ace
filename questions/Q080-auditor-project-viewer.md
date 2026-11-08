# Q080: Auditor Who Can Read Everything but Change Nothing (Project Viewer Role)

**Topic:** IAM (basic role Viewer, custom roles, predefined service viewer roles, read-only access)

## ❓ Question
> You want to add a new auditor to a Google Cloud Platform project. The auditor should be allowed to read, but not modify, all project items.
> How should you configure the auditor's permissions?
>
> **A.** Create a custom role with view-only project permissions. Add the user's account to the custom role.
>
> **B.** Create a custom role with view-only service permissions. Add the user's account to the custom role.
>
> **C.** Select the built-in IAM project Viewer role. Add the user's account to this role.
>
> **D.** Select the built-in IAM service Viewer role. Add the user's account to this role.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new auditor joins a project.
- **What you must achieve:** Let the auditor read everything in the project.
- **The limits:** The auditor must not be able to change anything.
- **What they're really asking:** Which role gives read-only access to all project items?

**Clues in the question:**
- "**read, but not modify**": a **read-only** role.
- "**all project items**": not one service, **everything** in the project → the project-wide **Viewer** role.
- "**built-in**" (in C): Google already made this role, so there's nothing to build or maintain (custom roles in A/B are extra work).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1️⃣ Basic roles: Owner, Editor, Viewer 🔑
- **What it is:** Three broad, built-in roles that apply to **every service in a project**:
  - **Viewer** (`roles/viewer`): **read-only** access to all resources.
  - **Editor**: read + change most resources.
  - **Owner**: Editor + manage permissions and billing.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-prod --member=user:ana@auditfirm.com --role=roles/viewer`
- **Not to be confused with:** predefined service roles (like `roles/compute.viewer`), which cover **one** service.
- **Analogy:** 👀 A **visitor pass to every room** in the building: look at anything, touch nothing.
- **In the online store:** The auditor can see VMs, buckets, databases and settings, but can't change them.

### 2️⃣ Custom role
- **What it is:** A role **you create yourself** by choosing individual permissions. You must keep it updated as Google adds new services and permissions.
- **Looks like:** `gcloud iam roles create shopAuditor --project=shopnow-prod --permissions=compute.instances.list,storage.buckets.list,...`
- **Not to be confused with:** built-in roles, which Google maintains for you.
- **Analogy:** ✂️ A **hand-made pass** where you list every room yourself and must update it whenever a new room opens.

### 3️⃣ Predefined service Viewer roles
- **What it is:** Built-in read-only roles for **one service**, such as `roles/compute.viewer`, `roles/storage.objectViewer`, `roles/bigquery.dataViewer`. There's **no single "service Viewer" role** that covers everything.
- **Not to be confused with:** the project Viewer role, which covers all services.
- **Analogy:** 🚪 A visitor pass for **one floor only**.

### 4️⃣ Least privilege (and the "data" caveat)
- **What it is:** Give only the access needed. Basic roles are broad, so Google usually prefers predefined roles. But here the requirement is literally "**read all project items**", which is exactly what Viewer does.
- 💡 **Detail:** Viewer sees **resources and settings**. Reading data inside some services (e.g., BigQuery table contents, Data Access logs) may need extra roles (see Q025).

### 🔗 How they fit together
```
 roles/viewer (built-in)   → 👀 read ALL services in the project ✅
 roles/compute.viewer      → 👀 Compute Engine only
 custom role               → ✂️ you pick permissions, you maintain it
 roles/editor / owner      → ✏️ can change things ❌ for an auditor
```

---

## 🌍 Real-World Scenario

An external auditor needs to review how a project is set up: VMs, firewall rules, buckets, IAM. The admin gives their account (or better, an auditors group) the **Viewer** role on the project. The auditor can browse everything in the console and run `list`/`describe` commands, but every change is denied.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a custom role with view-only project permissions. Add the user's account to the custom role.

**Wrong words:**
- ✔️ "view-only project permissions" is the right kind of access.
- ❌ "**Create a custom role**": you'd have to pick hundreds of permissions by hand and keep updating them as Google adds services. A built-in role already does this.

📌 **When to use it:** Use a custom role when no built-in role fits and you need a very specific set of permissions.
🏢 **Office example:** Hand-writing a visitor pass that lists every room, when the front desk already has a ready-made "visitor: all rooms" pass.

### ❌ B
> **B.** Create a custom role with view-only service permissions. Add the user's account to the custom role.

**Wrong words:**
- ❌ "**Create a custom role**": same extra work as A.
- ❌ "**view-only service permissions**": "service" permissions cover specific services, not "**all project items**".

📌 **When to use it:** Use it when someone should read only a few specific services and no built-in role matches.
🏢 **Office example:** A hand-made pass for a few chosen floors, when the auditor needed the whole building.

### ✅ C
> **C.** Select the built-in IAM project Viewer role. Add the user's account to this role.

**Why it's correct:**
- ✔️ "**project Viewer role**" matches "**read, but not modify**": Viewer is read-only; every change is denied.
- ✔️ "**project Viewer role**" matches "**all project items**": it covers every service in the project, not just one.
- ✔️ "**built-in IAM**" matches "**How should you configure**" (simplest correct setup): Google maintains it, so nothing to build or update.

📌 **When to use it:** Use it when someone must look at everything in a project but must not change anything.
🏢 **Office example:** Giving the auditor a "visitor: all rooms, look only" badge from the front desk.

### ❌ D
> **D.** Select the built-in IAM service Viewer role. Add the user's account to this role.

**Wrong words:**
- ✔️ "built-in" is good.
- ❌ "**service Viewer role**": service viewer roles (like `compute.viewer`) cover **one service only**, not "**all project items**". There's no single built-in "service Viewer" for everything.

📌 **When to use it:** Use a service viewer role when someone should read only one service, for example only Compute Engine.
🏢 **Office example:** A visitor pass for the IT floor only, when the auditor needs every floor.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow hires an external auditor, Ana, to review `shopnow-prod`.

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member=group:external-auditors@shopnow.com --role=roles/viewer
```

What Ana can do:
- ✅ `gcloud compute instances list`, see firewall rules, buckets, Cloud SQL settings, IAM policy.
- 🚫 `gcloud compute instances stop checkout-1` → permission denied.

*(Best practice: put Ana in an auditors **group** and grant the role to the group, as in Q025.)*

---

## 🧠 Key Takeaways / Memory Tips

- **"Read all, change nothing" in a project → built-in Viewer role (`roles/viewer`).**
- **Built-in before custom:** custom roles only when nothing built-in fits.
- Service viewer roles = **one service**. Project Viewer = **all services**.
  🧠 *"**Auditor sees all, touches nothing → Viewer.**"*
- Related: **Q025** (auditors group + predefined roles), **Q034** (who has which role), **Q067** (monitoring viewer).

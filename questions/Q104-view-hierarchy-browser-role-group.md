# Q104: Letting a Few People See the Folder/Project Tree (Group + Browser Role)

**Topic:** IAM / Resource Manager (roles/browser, groups, resource hierarchy)

## ❓ Question
> Your company set up a complex organizational structure on Google Cloud. The structure includes hundreds of folders and projects. Only a few team members should be able to view the hierarchical structure. You need to assign minimum permissions to these team members, and you want to follow Google-recommended practices. What should you do?
>
> **A.** Add the users to roles/browser role.
>
> **B.** Add the users to roles/iam.roleViewer role.
>
> **C.** Add the users to a group, and add this group to roles/browser.
>
> **D.** Add the users to a group, and add this group to roles/iam.roleViewer role.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The organization has hundreds of folders and projects.
- **What you must achieve:** Let a few team members view the hierarchy (the tree of folders and projects).
- **The limits:** Minimum permissions; follow recommended practice.
- **What they're really asking:** Which role lets them see the structure and nothing more?

**Clues in the question:**
- "**view the hierarchical structure**" + "**minimum permissions**": `roles/browser` shows folders and projects only, not what's inside them.
- "**Google-recommended practices**": grant roles to a **group**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/browser 🔑
- **What it is:** A role that lets someone **see the organization, folders and projects**, but **not** the resources inside projects (VMs, buckets).
- **Looks like:** `gcloud organizations add-iam-policy-binding 123456 --member=group:org-viewers@shopnow.com --role=roles/browser`
- **Not to be confused with:** roles/viewer, which also shows the resources inside projects.
- **Analogy:** 🗺️ A **floor plan of the building**, without keys to any room.
- **In the online store:** The platform team sees ShopNow's folder tree.

### 2. roles/iam.roleViewer
- **What it is:** A role that lets someone **read the definitions of IAM roles** (which permissions a role has).
- **Looks like:** `gcloud iam roles describe roles/editor`
- **Not to be confused with:** a role that shows folders and projects.
- **Analogy:** 📖 Reading the **badge rulebook**.
- **In the online store:** Security reviews what a custom role contains.

### 3. Resource hierarchy
- **What it is:** Organization → folders → projects → resources.
- **Looks like:** `shopnow.com → Retail → shopnow-prod → VMs`
- **Not to be confused with:** a network.
- **Analogy:** 🏢 Company → departments → teams → desks.
- **In the online store:** ShopNow has Retail, Data and Platform folders.

### 🔗 How they fit together
```
 Organization shopnow.com          ← group org-viewers@ has roles/browser ✅
   ├── folder Retail
   │     └── project shopnow-prod   (names visible, VMs NOT visible)
   └── folder Data
         └── project shopnow-data
```

---

## 🌍 Real-World Scenario

A company with hundreds of projects wants its architects to see how folders and projects are organized, without seeing any data or resources. The admin creates `architects@` and grants it **Browser** on the organization.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add the users to roles/browser role.

**Wrong words:**
- ✔️ "roles/browser" is the right role.
- ❌ "**Add the users**" one by one: Google recommends granting roles to a group.

📌 **When to use it:** Use it for one person when there's no group.
🏢 **Office example:** Writing each name on the floor-plan access list.

### ❌ B
> **B.** Add the users to roles/iam.roleViewer role.

**Wrong words:**
- ❌ "**roles/iam.roleViewer**": it shows what's inside IAM roles, not the folder and project tree.
- ❌ "**Add the users**" individually.

📌 **When to use it:** Use it when someone needs to read role definitions.
🏢 **Office example:** Giving someone the badge rulebook when they asked for the floor plan.

### ✅ C
> **C.** Add the users to a group, and add this group to roles/browser.

**Why it's correct:**
- ✔️ "**roles/browser**" matches "**view the hierarchical structure**": it shows folders and projects.
- ✔️ "**roles/browser**" matches "**minimum permissions**": it doesn't show resources inside projects.
- ✔️ "**Add the users to a group, and add this group**" matches "**Only a few team members**" + "**Google-recommended practices**": one grant to a group.

📌 **When to use it:** Use it when a few people should see how everything is organized, but touch nothing.
🏢 **Office example:** Giving the architects team a copy of the building floor plan, with no room keys.

### ❌ D
> **D.** Add the users to a group, and add this group to roles/iam.roleViewer role.

**Wrong words:**
- ✔️ "Add the users to a group" is best practice.
- ❌ "**roles/iam.roleViewer**": wrong role (see B).

📌 **When to use it:** Use it when a team needs to review role definitions.
🏢 **Office example:** Giving the team the badge rulebook instead of the floor plan.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud organizations add-iam-policy-binding 123456789 \
  --member=group:architects@shopnow.com --role=roles/browser
```
Architects see `Retail/shopnow-prod`, `Data/shopnow-data`, and so on, but opening a VM list gives "permission denied".

---

## 🧠 Key Takeaways / Memory Tips

- **See folders and projects only → roles/browser.**
- roles/viewer = also resources. iam.roleViewer = role definitions.
- **Groups, not individuals.**
  🧠 *"**Browse the tree → Browser.**"*
- Related: **Q080** (Viewer), **Q100** (group best practice).

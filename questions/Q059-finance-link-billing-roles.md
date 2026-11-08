# Q059: Only Finance Can Link Projects to Billing (Billing Account User + Project Billing Manager)

**Topic:** IAM + Billing (Billing Account User, Project Billing Manager, Project Creator, least privilege)

## ❓ Question
> You are the organization and billing administrator for your company. The engineering team has the Project Creator role on the organization. You do not want the engineering team to be able to link projects to the billing account. Only the finance team should be able to link a project to a billing account, but they should not be able to make any other changes to projects. What should you do?
>
> **A.** Assign the finance team only the Billing Account User role on the billing account.
>
> **B.** Assign the engineering team only the Billing Account User role on the billing account.
>
> **C.** Assign the finance team the Billing Account User role on the billing account and the Project Billing Manager role on the organization.
>
> **D.** Assign the engineering team the Billing Account User role on the billing account and the Project Billing Manager role on the organization.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are the organization and billing administrator. The engineering team can create projects (Project Creator role).
- **What you must achieve:** Only the finance team should be able to link projects to the billing account; engineers should not.
- **The limits:** Finance must not get any other permissions on projects.
- **What they're really asking:** Which roles do you give or take away?

| Question words | What they point to |
|---|---|
| "**do not want the engineering team to be able to link**" | Give engineering **no** billing roles → B and D are out |
| "**Only the finance team should be able to link a project to a billing account**" | Linking needs **two** permissions: one on the **billing account** side, one on the **project** side |
| "**should not be able to make any other changes to projects**" | On the project side use **Project Billing Manager** (billing link only), not Owner/Editor |

**Exam topic:** IAM + Billing.

---

## 📚 Key Terms Explained

### 1️⃣ Billing Account 
- **What it is:** The **payment record** (credit card or invoice) that Google charges for the projects linked to it.
- **Looks like:** `ShopNow Main Billing (0X1A2B-3C4D5E-6F7A8B)`
- **Not to be confused with:** a project. Projects hold resources, and the billing account pays for them.
- **Analogy:** 💳 The **company credit card**.
- **In the online store:** One billing account pays for `shopnow-prod`, `shopnow-dev`, etc.

### 2️⃣ Billing Account User 🔑
- **What it is:** An IAM role, granted **on the billing account**, that allows **attaching projects to that billing account**. It's the "card side" permission.
- **Looks like:** `roles/billing.user` on billing account `0X1A2B-...`
- **Not to be confused with:** Billing Account Administrator (manages the whole account, payments, users). Billing Account User can only **use** the account for linking.
- **Analogy:** 💳 Being **allowed to charge things to the company card**.
- **In the online store:** finance@shopnow.com may use the main billing account.

### 3️⃣ Project Billing Manager 🔑
- **What it is:** An IAM role, granted **on a project / folder / organization**, that allows **only** turning billing on/off or changing the billing account **for those projects**. Nothing else in the project. It's the "project side" permission.
- **Looks like:** `roles/billing.projectManager` on the organization
- **Not to be confused with:** Project Owner/Editor, which can change everything in the project.
- **Analogy:** 📋 Permission to **write the card number on a department's expense form**, but not touch anything else in that department.
- **In the online store:** Finance can link `shopnow-dev` to billing but can't create VMs or delete buckets.

### 4️⃣ Project Creator
- **What it is:** An IAM role that lets you **create new projects**.
- **Looks like:** `roles/resourcemanager.projectCreator` on the organization
- **Not to be confused with:** being able to pay for them. Creating a project ≠ linking it to billing.
- **Analogy:** 🏗️ Allowed to **open a new department**, but not to get it a company card.

### 🔗 How they fit together
```
Linking project → billing account needs BOTH sides:

 💳 Billing account side:  Billing Account User      (on the billing account)
 📁 Project side:          Project Billing Manager   (on the org = all projects)
                                    │
                       finance team has both ✅  → can link, nothing else
                       engineering has neither ✅ → can create projects, can't link
```

---

## 🌍 Real-World Scenario

Companies often let engineers spin up projects freely, but they don't want surprise costs. So the rule is: **projects start with no billing**, and only finance can attach them to the company billing account after checking the budget. Finance gets exactly the two roles needed for linking and nothing that lets them touch servers or data.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Assign the finance team only the Billing Account User role on the billing account.

**Wrong words:**
- ✔️ "Assign the finance team … the Billing Account User role on the billing account" is the right team and the right card-side role.
- ❌ "**only**": the card side alone isn't enough. Finance also needs a **project-side** permission (Project Billing Manager) to change billing on projects they don't own.

📌 **When to use it:** Use it when the person already owns the projects and only needs permission to use the billing account.
🏢 **Office example:** A department head who may use the company card for their own department.

### ❌ B
> **B.** Assign the engineering team only the Billing Account User role on the billing account.

**Wrong words:**
- ❌ "**Assign the engineering team**": the question says engineering must **not** link projects. Engineers own the projects they create, so with this role they **could** link them.

📌 **When to use it:** Use it when engineers are trusted to attach their own new projects to the company billing account.
🏢 **Office example:** Letting each department head charge their own new department to the company card.

### ✅ C (your answer)
> **C.** Assign the finance team the Billing Account User role on the billing account and the Project Billing Manager role on the organization.

**Why it's correct:**

- ✔️ "**Assign the finance team**" matches "**Only the finance team** should be able to link": Only finance gets the roles. Engineering gets nothing, so it **can't** link.
- ✔️ "**Billing Account User role on the billing account**" matches "link a project **to a billing account**": The card side: permission to attach projects to this billing account.
- ✔️ "**Project Billing Manager role on the organization**" matches "link **a project**" (any project in the org): The project side: permission to set billing on every project in the org.
- ✔️ Project Billing Manager (not Owner/Editor) matches "**should not be able to make any other changes to projects**": This role can only change the billing link. It can't touch VMs, buckets or settings.

📌 **When to use it:** Use it when one team should be the only one that connects projects to the company payment account and do nothing else.
🏢 **Office example:** Only the finance office may put the company card on a department's expense form, and they can't change anything else in that department.

### ❌ D
> **D.** Assign the engineering team the Billing Account User role on the billing account and the Project Billing Manager role on the organization.

**Wrong words:**
- ✔️ "Billing Account User role on the billing account and the Project Billing Manager role on the organization" is the right pair of roles.
- ❌ "**Assign the engineering team**": wrong team. This gives engineering **full** linking power, the exact opposite of what the question wants.

📌 **When to use it:** Use it when the engineering team is in charge of attaching projects to billing.
🏢 **Office example:** Giving the department heads the company card and the right to put it on any department's form.

---

## 🛒 E-Commerce Full-Stack Example

```bash
# Card side: finance may use the billing account
gcloud billing accounts add-iam-policy-binding 0X1A2B-3C4D5E-6F7A8B \
  --member=group:finance@shopnow.com --role=roles/billing.user

# Project side: finance may set billing on any project in the org, nothing else
gcloud organizations add-iam-policy-binding 123456789 \
  --member=group:finance@shopnow.com --role=roles/billing.projectManager
```

| Team | Create project? | Link to billing? | Change VMs/buckets? |
|---|---|---|---|
| engineering@shopnow.com | ✅ (Project Creator) | ❌ | ✅ in their projects |
| finance@shopnow.com | ❌ | ✅ | ❌ |

An engineer creates `shopnow-recs-dev`; it has no billing until finance approves and links it.

---

## 🧠 Key Takeaways / Memory Tips

- **Linking a project to billing needs two sides:** Billing Account User (**on the billing account**) + Project Billing Manager or Owner (**on the project**).
- **"Link billing but no other project changes" → Project Billing Manager**, never Owner/Editor.
  🧠 *"**Card side + project side = link.** Missing either = no link."*
- Read **which team** each option names; B and D have the right roles for the wrong team.
- Related: **Q007** (centralized billing account), **Q035** (Project Billing Manager to link a project).

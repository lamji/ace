# Q158: DevOps Needs Production Access That Won't Grow With New Google Features (Custom Role on the Production Project)

**Topic:** IAM (basic roles change over time, custom roles, scope)

## ❓ Question
> Your company uses a large number of Google Cloud services centralized in a single project. All teams have specific projects for testing and development. The DevOps team needs access to all of the production services in order to perform their job. You want to prevent Google Cloud product changes from broadening their permissions in the future. You want to follow Google-recommended practices. What should you do?
>
> **A.** Grant all members of the DevOps team the role of Project Editor on the organization level.
>
> **B.** Grant all members of the DevOps team the role of Project Editor on the production project.
>
> **C.** Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the production project.
>
> **D.** Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the organization level.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Production services live in one project; teams have separate test and dev projects. The DevOps team needs access to all production services.
- **What you must achieve:** Give DevOps the access they need in production.
- **The limits:** Their permissions must not grow on their own when Google adds new product features; follow recommended practice.
- **What they're really asking:** What kind of role keeps DevOps' permissions fixed even as Google Cloud changes?

**Clues in the question:**
- "**prevent Google Cloud product changes from broadening their permissions**": basic and predefined roles **gain new permissions** when Google updates them. A **custom role** only changes when **you** change it.
- "**production services**" in a **single project** → grant on the **production project**, not the org (least privilege).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Custom role 🔑 (review from Q102)
- **What it is:** A role with a **fixed list of permissions you choose**. Google doesn't add to it.
- **Looks like:** `gcloud iam roles create devopsProd --project=shop-prod --permissions=...`
- **Not to be confused with:** predefined or basic roles, which Google updates.
- **Analogy:** ✂️ A hand-made pass that lists exactly which rooms you can enter.
- **In the online store:** DevOps role in shopnow-prod.

### 2. Basic role (Editor)
- **What it is:** Very broad roles. They gain new permissions as Google launches new services.
- **Looks like:** `roles/editor`
- **Not to be confused with:** least privilege.
- **Analogy:** 🔑 A master key that opens every new room as it's built.
- **In the online store:** Avoid in production.

### 🔗 How they fit together
```
 custom role (fixed permissions) → granted on project shopnow-prod ✅
 Editor (grows with new features) ❌   org level (all projects) ❌
```

---

## 🌍 Real-World Scenario

A security team wants DevOps' production access to stay exactly as approved. They build a **custom role** with the needed permissions and grant it to the DevOps group **on the production project only**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant all members of the DevOps team the role of Project Editor on the organization level.

**Wrong words:**
- ❌ "**Project Editor**": a basic role that grows as Google adds features.
- ❌ "**organization level**": access to every project, not just production.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Master keys to every building.

### ❌ B
> **B.** Grant all members of the DevOps team the role of Project Editor on the production project.

**Wrong words:**
- ✔️ "on the production project" is the right scope.
- ❌ "**Project Editor**": broad, and grows with product changes.

📌 **When to use it:** Use basic roles only in small test projects.
🏢 **Office example:** A master key to the production building that opens new rooms automatically.

### ✅ C
> **C.** Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the production project.

**Why it's correct:**
- ✔️ "**Create a custom role that combines the required permissions**" matches "**prevent Google Cloud product changes from broadening their permissions**": only you can change it.
- ✔️ "**on the production project**" matches "**access to all of the production services**" (all in a single project), which is least privilege.

📌 **When to use it:** Use it when access must stay exactly as approved, in one place.
🏢 **Office example:** A hand-made pass listing exactly which rooms in the production building the team may enter.

### ❌ D
> **D.** Create a custom role that combines the required permissions. Grant the DevOps team the custom role on the organization level.

**Wrong words:**
- ✔️ "custom role" is right.
- ❌ "**organization level**": grants it on all projects, not only production.

📌 **When to use it:** Use org-level grants for org-wide jobs.
🏢 **Office example:** A fixed pass that works in every building, not just production.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud iam roles create devopsProd --project=shopnow-prod --permissions=compute.instances.get,compute.instances.start,container.deployments.update,...
gcloud projects add-iam-policy-binding shopnow-prod --member=group:devops@shopnow.com --role=projects/shopnow-prod/roles/devopsProd
```

---

## 🧠 Key Takeaways / Memory Tips

- **Permissions must not grow with Google changes → custom role.**
- Grant it where the need is (the project), not org-wide.
  🧠 *"**Fixed list, right place.**"*
- Related: **Q102**, **Q118** (custom roles).

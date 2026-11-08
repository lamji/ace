# Q273: Department-Specific Org Policies and Log Sinks That Project Owners Can't Remove (Folders per Department, Set Both on Folders)

**Topic:** Resource hierarchy (folders, aggregated sinks, org policies)

## ❓ Question
> You are a Google Cloud organization administrator. You need to configure organization policies and log sinks on Google Cloud projects that cannot be removed by project users to comply with your company's security policies. The security policies are different for each company department. Each company department has a user with the Project Owner role assigned to their projects. What should you do?
>
> **A.** Use a standard naming convention for projects that includes the department name. Configure organization policies on the organization and log sinks on the projects.
>
> **B.** Use a standard naming convention for projects that includes the department name. Configure both organization policies and log sinks on the projects.
>
> **C.** Organize projects under folders for each department. Configure both organization policies and log sinks on the folders.
>
> **D.** Organize projects under folders for each department. Configure organization policies on the organization and log sinks on the folders.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are the organization administrator. Each department has its own security policies, and each department has a Project Owner on its projects.
- **What you must achieve:** Apply organization policies and log sinks (log export rules) that project users cannot remove.
- **The limits:** Even Project Owners must not be able to remove them, and rules differ per department.
- **What they're really asking:** Where should you apply the policies and sinks so project owners can't remove them?

**Clues in the question:**
- "**cannot be removed by project users**" → set them **above** the project (folder), where Project Owners have no rights.
- "**different for each company department**" → **one folder per department**, policies and sinks on each folder.

**Exam topic:** Resource hierarchy.

---

## 📚 Key Terms Explained

### 1. Folder-level (aggregated) log sink 🔑
- **What it is:** A sink on a folder that collects logs from all projects inside (`--include-children`). Project owners can't delete it.
- **Looks like:** `gcloud logging sinks create fin-sink storage.googleapis.com/fin-logs --folder=FIN --include-children`
- **Not to be confused with:** project sink.
- **Analogy:** 📬 A chute from every office on the floor to the security room.
- **In the online store:** Finance audit logs.

### 2. Folder-level org policy
- **What it is:** Org policy set on a folder applies to all projects inside.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 📜 A floor-wide rule.
- **In the online store:** —

### 🔗 How they fit together
```
 Org
  ├─ Folder Finance [org policies + sink] ✅
  └─ Folder HR      [org policies + sink] ✅
       └─ projects (owners can't change folder settings)
```

---

## 🌍 Real-World Scenario

The org admin creates **Finance** and **HR** folders, sets each department's **org policies** and an **aggregated log sink** on its folder. Project Owners can't remove them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use a standard naming convention for projects that includes the department name. Configure organization policies on the organization and log sinks on the projects.

**Wrong words:**
- ❌ "**naming convention**": names don't apply policies.
- ❌ "**org policies on the organization**": same for everyone, not per department.
- ❌ "**log sinks on the projects**": Project Owners can delete them.

📌 **When to use it:** Use naming conventions for readability only.
🏢 **Office example:** Labeling offices but letting each manager remove the cameras.

### ❌ B
> **B.** Use a standard naming convention for projects that includes the department name. Configure both organization policies and log sinks on the projects.

**Wrong words:**
- ❌ "**on the projects**": Project Owners can change or remove both.

📌 **When to use it:** Use project-level settings for things owners may change.
🏢 **Office example:** Rules taped inside each office where the manager can peel them off.

### ✅ C
> **C.** Organize projects under folders for each department. Configure both organization policies and log sinks on the folders.

**Why it's correct:**
- ✔️ "**folders for each department**" matches "**security policies are different for each company department**".
- ✔️ "**organization policies and log sinks on the folders**" matches "**cannot be removed by project users**": project owners have no rights on the folder.

📌 **When to use it:** Use it when each department needs its own rules that department managers can't undo.
🏢 **Office example:** Posting each floor's rules and cameras at the floor level, where office managers can't reach.

### ❌ D
> **D.** Organize projects under folders for each department. Configure organization policies on the organization and log sinks on the folders.

**Wrong words:**
- ✔️ Sinks on folders are right.
- ❌ "**organization policies on the organization**": one set for all departments, not different per department.

📌 **When to use it:** Use org-level policies for company-wide rules.
🏢 **Office example:** One rule for every floor when each floor needs its own.

---

## 🛒 E-Commerce Full-Stack Example

Folders `Payments`, `Marketing`: payments folder gets `gcp.resourceLocations=in:eu-locations` + sink to `payments-audit` bucket.

---

## 🧠 Key Takeaways / Memory Tips

- **Unremovable, per-department policies/sinks → folders per department, set on the folders.**
  🧠 *"**Above the project, out of the owner's reach.**"*
- Related: **Q194**, **Q204**.

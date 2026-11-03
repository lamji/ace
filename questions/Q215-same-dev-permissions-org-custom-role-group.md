# Q215: Same Developer Permissions in Every Project, Limited to Compute, Functions and SQL (Group + Org-Level Custom Role)

**Topic:** IAM (organization-level custom roles, groups)

## ❓ Question
> Your company requires all developers to have the same permissions, regardless of the Google Cloud project they are working on. Your company's security policy also restricts developer permissions to Compute Engine, Cloud Functions, and Cloud SQL. You want to implement the security policy with minimal effort. What should you do?
>
> **A.** • Create a custom role with Compute Engine, Cloud Functions, and Cloud SQL permissions in one project within the Google Cloud organization. • Copy the role across all projects created within the organization with the gcloud iam roles copy command. • Assign the role to developers in those projects.
>
> **B.** • Add all developers to a Google group in Google Groups for Workspace. • Assign the predefined role of Compute Admin to the Google group at the Google Cloud organization level.
>
> **C.** • Add all developers to a Google group in Cloud Identity. • Assign predefined roles for Compute Engine, Cloud Functions, and Cloud SQL permissions to the Google group for each project in the Google Cloud organization.
>
> **D.** • Add all developers to a Google group in Cloud Identity. • Create a custom role with Compute Engine, Cloud Functions, and Cloud SQL permissions at the Google Cloud organization level. • Assign the custom role to the Google group.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Every developer, **every project**, the **same** permissions, only **Compute, Functions, SQL**, with **little effort**.

**Clues in the question:**
- "**same permissions, regardless of the … project**" → grant at the **organization level** (inherited everywhere).
- "**restricts … to Compute Engine, Cloud Functions, and Cloud SQL**" → one **custom role** combining exactly those.
- "**all developers**" + "**minimal effort**" → a **group**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Organization-level custom role 🔑
- **What it is:** A custom role defined at the org, usable on any project/folder in it.
- **Looks like:** `gcloud iam roles create devRole --organization=123 --permissions=compute.instances.*,cloudfunctions.functions.*,cloudsql.instances.*`
- **Not to be confused with:** project-level custom role.
- **Analogy:** 🔑 One company-wide key pattern.
- **In the online store:** ShopNow developer role.

### 🔗 How they fit together
```
 Org [group:devs → custom devRole] ✅
   └─ all folders/projects inherit
```

---

## 🌍 Real-World Scenario

Security wants developers limited to three services everywhere. The admin creates an **org-level custom role** and grants it once to the **developers group** at the org.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** • Create a custom role with Compute Engine, Cloud Functions, and Cloud SQL permissions in one project within the Google Cloud organization. • Copy the role across all projects created within the organization with the gcloud iam roles copy command. • Assign the role to developers in those projects.

**Wrong words:**
- ❌ "**in one project … Copy the role across all projects**": many copies to maintain and re-copy for new projects. Not minimal effort.
- ❌ "**Assign the role to developers**" individually.

📌 **When to use it:** Use project-level roles when only one project needs it.
🏢 **Office example:** Cutting a separate key for every branch office.

### ❌ B
> **B.** • Add all developers to a Google group in Google Groups for Workspace. • Assign the predefined role of Compute Admin to the Google group at the Google Cloud organization level.

**Wrong words:**
- ✔️ A group is right.
- ❌ "**Compute Admin**": only covers Compute Engine, not Cloud Functions or Cloud SQL.

📌 **When to use it:** Use Compute Admin for VM administrators.
🏢 **Office example:** A key for one room when three are needed.

### ❌ C
> **C.** • Add all developers to a Google group in Cloud Identity. • Assign predefined roles for Compute Engine, Cloud Functions, and Cloud SQL permissions to the Google group for each project in the Google Cloud organization.

**Wrong words:**
- ✔️ Group in Cloud Identity is right.
- ❌ "**for each project**": grants repeated per project, more effort and new projects are missed.
- ❌ Predefined roles usually include more than the policy allows.

📌 **When to use it:** Use per-project grants when access differs by project.
🏢 **Office example:** Handing out keys branch by branch.

### ✅ D
> **D.** • Add all developers to a Google group in Cloud Identity. • Create a custom role with Compute Engine, Cloud Functions, and Cloud SQL permissions at the Google Cloud organization level. • Assign the custom role to the Google group.

**Why it's correct:**
- ✔️ "**Add all developers to a Google group**" matches "**all developers**" + "**minimal effort**".
- ✔️ "**custom role with Compute Engine, Cloud Functions, and Cloud SQL permissions**" matches "**restricts developer permissions to Compute Engine, Cloud Functions, and Cloud SQL**".
- ✔️ "**at the Google Cloud organization level**" matches "**regardless of the Google Cloud project**".

📌 **When to use it:** Use it when a whole job type should have the same limited access everywhere in the company.
🏢 **Office example:** One company-wide badge type for all developers that opens the same three rooms in every office.

---

## 🛒 E-Commerce Full-Stack Example

Custom role `organizations/SHOPNOW/roles/shopDeveloper` → binding at org: `group:developers@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Same access everywhere → grant at the org. Exact service set → custom role. Many people → group.**
  🧠 *"**One role, one group, one grant at the top.**"*
- Related: **Q158**, **Q194**.

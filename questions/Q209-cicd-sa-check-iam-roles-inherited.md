# Q209: Check Whether the CI/CD Service Account Has the Right Roles (IAM Roles at the Project + Inherited)

**Topic:** IAM (inherited policies, troubleshooting)

## ❓ Question
> Your continuous integration and delivery (CI/CD) server can't execute Google Cloud actions in a specific project because of permission issues. You need to validate whether the used service account has the appropriate roles in the specific project. What should you do?
>
> **A.** Open the Google Cloud console, and check the Identity and Access Management (IAM) roles assigned to the service account at the project or inherited from the folder or organization levels.
>
> **B.** Open the Google Cloud console, and check the organization policies.
>
> **C.** Open the Google Cloud console, and run a query to determine which resources this service account can access.
>
> **D.** Open the Google Cloud console, and run a query of the audit logs to find permission denied errors for this service account.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Does the service account **have the right roles** in this project?

**Clues in the question:**
- "**validate whether the used service account has the appropriate roles in the specific project**" → look at its **IAM roles**, including those **inherited** from folder/org.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Inherited IAM roles 🔑
- **What it is:** Roles granted on a folder or org automatically apply to every project below it. The project's IAM page shows them.
- **Looks like:** IAM page → "Inherited" column
- **Not to be confused with:** organization policies.
- **Analogy:** 🏢 A badge from head office also opens doors in every branch.
- **In the online store:** deploy-sa granted at the Prod folder.

### 🔗 How they fit together
```
 Org ─ roles? ─► Folder ─ roles? ─► Project ─ roles? ⇒ effective roles of ci-sa ✅
```

---

## 🌍 Real-World Scenario

A build fails with PERMISSION_DENIED. The engineer opens **IAM** in the project, finds `ci-sa`, and checks its direct and **inherited** roles to see what's missing.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Open the Google Cloud console, and check the Identity and Access Management (IAM) roles assigned to the service account at the project or inherited from the folder or organization levels.

**Why it's correct:**
- ✔️ "**check the IAM roles assigned to the service account at the project**" matches "**has the appropriate roles in the specific project**".
- ✔️ "**or inherited from the folder or organization levels**": these count too, so you see the full picture.

📌 **When to use it:** Use it when you need to confirm what someone is actually allowed to do in one place.
🏢 **Office example:** Checking someone's badge permissions, including ones granted by head office.

### ❌ B
> **B.** Open the Google Cloud console, and check the organization policies.

**Wrong words:**
- ❌ "**organization policies**": they limit **what** can be done (e.g. locations), not which roles the SA has.

📌 **When to use it:** Use org policies for company-wide restrictions.
🏢 **Office example:** Reading the building rules instead of the badge list.

### ❌ C
> **C.** Open the Google Cloud console, and run a query to determine which resources this service account can access.

**Wrong words:**
- ❌ "**which resources this service account can access**": a broad inventory query; the question is about its **roles** in one project.

📌 **When to use it:** Use Policy Analyzer for broad access audits.
🏢 **Office example:** Listing every room someone could enter in every building.

### ❌ D
> **D.** Open the Google Cloud console, and run a query of the audit logs to find permission denied errors for this service account.

**Wrong words:**
- ❌ "**audit logs to find permission denied errors**": shows that it failed, not which roles it has.

📌 **When to use it:** Use it to find what failed and when.
🏢 **Office example:** Reading the alarm log instead of the badge list.

---

## 🛒 E-Commerce Full-Stack Example

IAM → `cloudbuild-deployer@shopnow-ci.iam.gserviceaccount.com` in `shopnow-prod`: has `run.developer` (inherited from Prod folder), missing `iam.serviceAccountUser` → add it.

---

## 🧠 Key Takeaways / Memory Tips

- **Does an account have the right roles? → check IAM (direct + inherited).**
  🧠 *"**Check the badge, including head office's.**"*
- Related: **Q148**, **Q161**.

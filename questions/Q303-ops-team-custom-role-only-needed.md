# Q303: Team Needs Specific Permissions Split Across Two Predefined Roles (Custom Role With Only the Required Permissions)

**Topic:** IAM (custom roles, least privilege)

## ❓ Question
> You are managing the security configuration of your company’s Google Cloud organization. The Operations team needs specific permissions on both a Google Kubernetes Engine (GKE) cluster and a Cloud SQL instance. Two predefined Identity and Access Management (IAM) roles exist that contain a subset of the permissions needed by the team. You need to configure the necessary IAM permissions for this team while following Google-recommended practices. What should you do?
>
> **A.** Create a custom IAM role that combines the permissions from the two relevant predefined roles.
>
> **B.** Grant the team the two predefined IAM roles.
>
> **C.** Create a custom IAM role that includes only the required permissions from the predefined roles.
>
> **D.** Grant the team the IAM roles of Kubernetes Engine Admin and Cloud SQL Admin.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The Operations team needs certain specific permissions on a GKE cluster and a Cloud SQL instance. Two existing predefined roles each contain part of what they need.
- **What you must achieve:** Give the team the permissions they need.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** How should you build or choose the role for the team?

**Clues in the question:**
- "**specific permissions**" + "**Google-recommended practices**" (least privilege) → a **custom role with only the required permissions**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Custom role 🔑
- **What it is:** A role you define by listing exact permissions.
- **Looks like:** `gcloud iam roles create opsRole --organization=123 --permissions=container.clusters.get,cloudsql.instances.restart`
- **Not to be confused with:** combining whole predefined roles.
- **Analogy:** 🔑 A key cut to open only the needed doors.
- **In the online store:** ShopNow ops role.

### 🔗 How they fit together
```
 role X ∩ needed + role Y ∩ needed → custom role (only needed) ✅
```

---

## 🌍 Real-World Scenario

Ops needs a handful of GKE and Cloud SQL permissions. The admin creates a **custom role** with just those.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a custom IAM role that combines the permissions from the two relevant predefined roles.

**Wrong words:**
- ❌ "**combines the permissions from the two relevant predefined roles**": includes extra permissions the team doesn't need.

📌 **When to use it:** Use a combined role only when all permissions are needed.
🏢 **Office example:** Merging two master keys.

### ❌ B
> **B.** Grant the team the two predefined IAM roles.

**Wrong words:**
- ❌ "**two predefined IAM roles**": grants more than required.

📌 **When to use it:** Use predefined roles when they fit closely.
🏢 **Office example:** Two broad keys.

### ✅ C
> **C.** Create a custom IAM role that includes only the required permissions from the predefined roles.

**Why it's correct:**
- ✔️ "**custom IAM role that includes only the required permissions**" matches "**specific permissions**" + least-privilege best practice.

📌 **When to use it:** Use it when no ready-made access level fits and you want to give exactly what's needed.
🏢 **Office example:** A key cut to open just the two needed doors.

### ❌ D
> **D.** Grant the team the IAM roles of Kubernetes Engine Admin and Cloud SQL Admin.

**Wrong words:**
- ❌ "**Kubernetes Engine Admin and Cloud SQL Admin**": full admin over both services.

📌 **When to use it:** Use admin roles for true administrators.
🏢 **Office example:** Handing over the master keys.

---

## 🛒 E-Commerce Full-Stack Example

`roles/shopnow.opsLimited` with 6 permissions, granted to `ops@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Predefined roles too broad → custom role with only required permissions.**
  🧠 *"**Only what's needed.**"*
- Related: **Q347**, **Q159**.

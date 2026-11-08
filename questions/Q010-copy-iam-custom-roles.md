# Q010: Copying IAM Custom Roles to Another Project

**Topic:** IAM (custom roles, `gcloud iam roles copy`, project vs organization scope)

## ❓ Question
> You have a development project with appropriate IAM roles defined. You are creating a production project and want to have the same IAM roles on the new project, using the fewest possible steps. What should you do?
>
> **A.** Use gcloud iam roles copy and specify the production project as the destination project.
>
> **B.** Use gcloud iam roles copy and specify your organization as the destination organization.
>
> **C.** In the Google Cloud Platform Console, use the 'create role from role' functionality.
>
> **D.** In the Google Cloud Platform Console, use the 'create role' functionality and select all applicable permissions.

*(The `λ€˜ λ€™` characters in the screenshot are broken quote marks, shown here as `'`.)*

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A development project already has IAM roles defined (IAM roles are named sets of permissions you give to people).
- **What you must achieve:** Have the same roles in a new production project.
- **The limits:** Use the fewest steps.
- **What they're really asking:** What is the quickest way to copy those roles from the dev project to the prod project?

| Keyword | What it hints at |
|---|---|
| "**IAM roles defined**" | **Custom roles** you made (predefined roles already exist in every project) |
| "**same IAM roles on the new project**" | The destination is the **production project**, not the whole organization |
| "**fewest possible steps**" | Use a **copy** command instead of rebuilding roles by hand |

**Exam topic:** IAM, specifically **custom roles and copying them between projects**.

---

## 📚 Key Terms Explained

### 1️⃣ IAM (Identity and Access Management)
- **What it is:** The Google Cloud system that decides **who** can do **what** on **which** resource.
- **Analogy:** 🪪 The office **access control system**: who gets which keycard, and which doors each card opens.
- **In the online store:** IAM decides that support staff can **view** orders but **not delete** them.

### 2️⃣ Permission
- **What it is:** One single allowed action, written like `service.resource.verb`, e.g., `cloudsql.instances.get` or `storage.objects.delete`.
- **Analogy:** 🔑 One **key for one door**.
- **In the online store:** `storage.objects.create` = allowed to upload a product image.

### 3️⃣ Role (Basic, Predefined, Custom)
- **What it is:** A **bundle of permissions** you give to people together. There are 3 kinds:
  | Type | Who makes it | Example | Notes |
  |---|---|---|---|
  | **Basic** | Google | Owner, Editor, Viewer | Very broad, so avoid in production |
  | **Predefined** | Google | `roles/cloudsql.client`, `roles/storage.objectViewer` | Already available in **every** project, so no copying needed |
  | **Custom** | **You** | `projects/shopnow-dev/roles/orderSupport` | Exactly the permissions you choose. **Lives in one project or organization**, so it must be copied to be used elsewhere |
- **Analogy:** 📄 A **job description**: a list of duties (permissions) for a position. Google's standard job descriptions = predefined. One your company writes itself = custom.
- **In the online store:** A custom role `orderSupport` = "can view orders and customer info, can issue refunds, can't delete anything."

### 4️⃣ Where Custom Roles Live (Project vs Organization)
- **Project-level custom role:** Only usable **inside that one project**.
- **Organization-level custom role:** Usable in **every project** in the organization.
- **Analogy:** 🏢 A job description kept in **one branch's** files vs one in the **company-wide HR handbook**.

### 5️⃣ IAM Policy / Role Binding
- **What it is:** The link that **gives a role to someone**: *member* (user, group, service account) + *role*. A role alone does nothing until it's **bound** to someone.
- **Analogy:** 📝 The HR record that says, "**Maria** has the **Support Agent** job description."
- ⚠️ **Note:** `gcloud iam roles copy` copies the **role definition** (the list of permissions), **not** who has it. You still grant it to people in prod separately.

### 6️⃣ Development vs Production Project
- **Dev:** Where you build and test. Mistakes are OK.
- **Prod:** The live system that real customers use. It must be safe and controlled.
- **Analogy:** 🧪 The **training room** vs the **real front desk**.

### 7️⃣ `gcloud iam roles copy`
- **What it is:** A command that **copies a custom role** from one project or organization to another.
- **Shape:** `gcloud iam roles copy --source=<role> --destination=<new role ID> --dest-project=<project>` (or `--dest-organization=<org>`)

### 🔗 How They Fit Together
```
📁 shopnow-dev (project)
   └── 📄 Custom role: orderSupport  [orders.view, refunds.create, customers.view]
            │
            │  gcloud iam roles copy ... --dest-project=shopnow-prod
            ▼
📁 shopnow-prod (project)
   └── 📄 Custom role: orderSupport  (same permissions) ✅
            │
            │  role binding (separate step)
            ▼
   👥 group: support@shopnow.com
```

---

## 🌍 Real-World Scenario

Teams usually build in a **dev** project first. Along the way they design **custom roles** that give each team exactly the right permissions, following **least privilege**. When it's time to launch **prod**, they need the **same roles** there.

Rebuilding each role by hand means clicking through dozens of permissions, and it's easy to miss one. **Copying** them with one command per role is faster and makes dev and prod match exactly.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use gcloud iam roles copy and specify the production project as the destination project.

**Why it's correct:**
- ✔️ `gcloud iam roles copy` copies a custom role's **exact permissions** in one command, so it's the fewest steps.
- ✔️ `--dest-project=<prod>` puts the role **exactly where it's needed**: the production project.
- ✔️ Dev and prod roles match exactly, with no clicking and no typos.

**📌 When to use it:** Use it when **you need the same custom role in another project**.
🏢 **Office example:** **Photocopying a job description** from the main branch for the new branch office, so both use exactly the same duties.

### ❌ B
> **B.** Use gcloud iam roles copy and specify your organization as the destination organization.

**Why it's wrong:**
- ❌ The question asks for the roles **on the new project**, not on the whole organization.
- ❌ An organization-level role is available to **every project** in the company. That's **broader than needed** and goes against least privilege.
- ❌ It may also require **organization-level** admin permissions, which you might not have.

**📌 When to use it:** Use it when **every project in the company** should be able to use the role.
🏢 **Office example:** Putting a job description in the **company-wide HR handbook** so every branch can use it.

### ❌ C
> **C.** In the Google Cloud Platform Console, use the 'create role from role' functionality.

**Why it's wrong:**
- ❌ It's a **manual, click-by-click** process for each role in the Console, so it takes more steps than one command.
- ❌ It's meant for making a **new, slightly different role** based on an existing one, not for copying roles to another project.

**📌 When to use it:** Use it when you want a **new role that's almost the same as an existing one**, with small changes.
🏢 **Office example:** Taking the "Senior Clerk" job description and **editing a few lines** to make a "Junior Clerk" one.

### ❌ D
> **D.** In the Google Cloud Platform Console, use the 'create role' functionality and select all applicable permissions.

**Why it's wrong:**
- ❌ You'd **rebuild every role from scratch**, choosing each permission one by one. That's the **most steps** of all.
- ❌ It's **error-prone**: easy to miss or add a permission, so prod may not match dev.

**📌 When to use it:** Use it when you need a **brand-new role** that isn't like anything you already have.
🏢 **Office example:** Writing a **new job description from scratch**, listing every duty one by one, for a position the company never had before.

---

## 🛒 E-Commerce Full-Stack Example

In `shopnow-dev`, the team created three custom roles while building the store:

| Custom role | Who uses it | Key permissions |
|---|---|---|
| `orderSupport` | Customer support team | View orders and customers, issue refunds |
| `catalogEditor` | Merchandising team | Upload/update product images in Cloud Storage |
| `checkoutDeployer` | CI/CD pipeline | Deploy new versions of the checkout service |

Now ShopNow is launching `shopnow-prod`.

**1. See the custom roles in dev:**
```bash
gcloud iam roles list --project=shopnow-dev
```

**2. Copy each one to prod (option A):**
```bash
gcloud iam roles copy \
  --source="projects/shopnow-dev/roles/orderSupport" \
  --destination=orderSupport \
  --dest-project=shopnow-prod

gcloud iam roles copy \
  --source="projects/shopnow-dev/roles/catalogEditor" \
  --destination=catalogEditor \
  --dest-project=shopnow-prod

gcloud iam roles copy \
  --source="projects/shopnow-dev/roles/checkoutDeployer" \
  --destination=checkoutDeployer \
  --dest-project=shopnow-prod
```

**3. Grant the roles to people in prod (a separate step, since copy doesn't move who has the role):**
```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member="group:support@shopnow.com" \
  --role="projects/shopnow-prod/roles/orderSupport"
```

**Result:** Support agents get **exactly the same** permissions in prod as in dev: they can issue a refund for order #1042, but they **can't** delete the orders database. ✅

**With the other options:**
- **B (organization):** `orderSupport` becomes available in **every** ShopNow project, including the finance and HR projects where it doesn't belong. ❌
- **C / D (Console clicking):** Someone clicks through 40+ permissions three times, misses `refunds.create`, and support can't issue refunds on launch day. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Same custom roles in another project, fewest steps" → `gcloud iam roles copy --dest-project=<project>`.**
- **Copy to the scope that's asked:** "new project" → `--dest-project`. "Whole organization" → `--dest-organization`.
- **Only CUSTOM roles need copying.** Basic and predefined roles exist everywhere already.
- **Copying a role ≠ granting it.** You still bind the role to users or groups in the new project.
- 🧠 *"Role = job description. Binding = giving the job to a person. Copy moves the description, not the people."*

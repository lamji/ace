# Q034: Checking Who Has Which Role in a Project (IAM Page vs Roles Page)

**Topic:** IAM (allow policy, principals/members, IAM page vs Roles page, `gcloud iam roles list`, `gcloud projects get-iam-policy`)

## ❓ Question
> You want to verify the IAM users and roles assigned within a GCP project named my-project. What should you do?
>
> **A.** Run gcloud iam roles list. Review the output section.
>
> **B.** Run gcloud iam service-accounts list. Review the output section.
>
> **C.** Navigate to the project and then to the IAM section in the GCP Console. Review the members and roles.
>
> **D.** Navigate to the project and then to the Roles section in the GCP Console. Review the roles and status.

**My answer:** D
**Correct answer:** C
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** There is a project named my-project.
- **What you must achieve:** Check which users have which IAM roles in it.
- **The limits:** None stated.
- **What they're really asking:** How do you see the users and roles assigned in that project?

| Keyword | What it hints at |
|---|---|
| "**users and roles assigned**" | You need the **pairs**: *person → role*. That's the project's **IAM policy** |
| "**within a GCP project**" | Look at **that project's** IAM page, not a global list of roles |
| "**verify**" | Just look and review, so a read-only view is fine |

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1️⃣ IAM Policy (allow policy) 🔑
- **What it is:** The **list of "who has which role"** attached to a project (or folder, bucket, etc.). Each entry is a **binding**: one role + the members who have it.
- **Looks like:**
  ```yaml
  bindings:
  - role: roles/owner
    members:
    - user:maria@shopnow.com
  - role: roles/storage.admin
    members:
    - group:storage-team@shopnow.com
  - role: roles/cloudsql.client
    members:
    - serviceAccount:checkout@my-project.iam.gserviceaccount.com
  ```
- **Not to be confused with:** a **list of roles**. A role list says what roles **exist**. The policy says **who has them**.
- **Analogy:** 📋 The **staff access sheet** at reception: "Maria = master key, Storage team = storage rooms, Checkout robot = database room".
- **In the online store:** Before an audit, you check the policy to make sure ex-employees are gone.

### 2️⃣ Member / Principal
- **What it is:** **Who** gets a role: a `user:`, `group:`, `serviceAccount:` or `domain:`. (Newer Console screens say **principal** instead of **member**.)
- **Looks like:** `user:ken@shopnow.com`, `group:ops-team@shopnow.com`
- **Not to be confused with:** a role. The member is the **person or machine**. The role is the **set of permissions**.
- **Analogy:** 👤 The **name** on the access sheet.

### 3️⃣ IAM page (IAM & Admin → IAM) ✅
- **What it is:** The Console page that **shows the project's IAM policy as a table**: each member and the roles they have. You can also add or remove access here.
- **Looks like:**
  | Principal | Role |
  |---|---|
  | maria@shopnow.com | Owner |
  | storage-team@shopnow.com | Storage Admin |
  | checkout@my-project.iam.gserviceaccount.com | Cloud SQL Client |
- **Not to be confused with:** the Roles page (next term).
- **Analogy:** 📋 Reading the **access sheet** at reception.

### 4️⃣ Roles page (IAM & Admin → Roles)
- **What it is:** A **catalog of roles** (predefined and custom) with their **permissions** and **status** (like *General Availability*, *Beta*, *Disabled*). It's where you **create and edit custom roles** (Q010).
- **Looks like:** `Storage Admin · roles/storage.admin · General Availability · 50 permissions`
- **Not to be confused with:** the IAM page. **It doesn't show who has each role.**
- **Analogy:** 📖 The **badge-type catalog**: it describes every badge type that exists, but not who carries one.

### 5️⃣ `gcloud iam roles list` and `gcloud iam service-accounts list`
- **What it is:**
  - `gcloud iam roles list` lists **role definitions** (the catalog, like the Roles page).
  - `gcloud iam service-accounts list` lists the project's **service accounts** (machine identities only), **not** their roles.
- **Not to be confused with:** `gcloud projects get-iam-policy my-project`, the **command-line** way to see who has which role.
- **Analogy:** 📖 Badge catalog / 🤖 list of robot staff. Neither tells you who holds which badge.

### 🔗 How They Fit Together
```
📖 Roles page / gcloud iam roles list           → WHAT roles exist (no names)
🤖 gcloud iam service-accounts list             → WHICH machine accounts exist (no roles)
📋 IAM page / gcloud projects get-iam-policy    → WHO has WHICH role ✅
     ├── user:maria@…            → Owner
     ├── group:storage-team@…    → Storage Admin
     └── serviceAccount:checkout@… → Cloud SQL Client
```

---

## 🌍 Real-World Scenario

Access reviews happen all the time: **security audits**, **an employee leaving**, **"why can Ken delete VMs?"**, or a **quarterly compliance check**. The first step is always the same: open the project's **IAM page** (or export the IAM policy) and read **who has what**. Then remove anything that shouldn't be there.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Run gcloud iam roles list. Review the output section.

**Why it's wrong:**
- ❌ It lists **role definitions** (names, titles, descriptions). It shows **no users** and nothing about who holds each role.
- 💡 The command that *does* answer the question is `gcloud projects get-iam-policy my-project`.

**📌 When to use it:** Use it when you want to look up which roles exist and what they're called.
🏢 **Office example:** Reading the catalog of badge types the building offers.

### ❌ B
> **B.** Run gcloud iam service-accounts list. Review the output section.

**Why it's wrong:**
- ❌ It shows only **service accounts** (machine identities). It doesn't show **human users** or **any roles**.

**📌 When to use it:** Use it when you want to see which machine accounts exist in a project.
🏢 **Office example:** Listing the badges issued to the office robots, without saying which doors they open.

### ✅ C
> **C.** Navigate to the project and then to the IAM section in the GCP Console. Review the members and roles.

**Why it's correct:**
- ✔️ The **IAM page** shows the project's IAM policy: **every member and the roles they have**, exactly "users and roles assigned".
- ✔️ It's **inside the project**, so you see `my-project`'s access specifically.
- ✔️ Simple and visual, and you can fix problems right there.

**📌 When to use it:** Use it when you need to see who has access to a project and what they're allowed to do.
🏢 **Office example:** Reading the access sheet at reception to see which employee holds which key.

### ❌ D (your answer)
> **D.** Navigate to the project and then to the Roles section in the GCP Console. Review the roles and status.

**Why it's wrong:**
- ❌ The **Roles** page is a **catalog** of roles and their permissions. "**Status**" means things like *General Availability* or *Disabled*, not "assigned to Maria".
- ❌ It **doesn't show users** at all.
- 💡 **Likely mix-up:** The question says "roles", and this page is literally called **Roles**. But the question asks for **users and roles together**, which is the **IAM** page.

**📌 When to use it:** Use the Roles page to read what a role allows, or to create and edit a custom role.
🏢 **Office example:** Reading the badge catalog to see what a "Manager badge" opens, or designing a new badge type.

---

## 🛒 E-Commerce Full-Stack Example

Ken from ShopNow's ops team just left the company. Security asks: **"Does Ken still have access to `shopnow-prod`, and who else has Owner?"**

**Console (option C):** IAM & Admin → **IAM** → filter "ken" → he still has **Compute Admin** → remove it.

**Same check from the CLI:**
```bash
gcloud projects get-iam-policy shopnow-prod \
  --flatten="bindings[].members" \
  --format="table(bindings.members, bindings.role)"
```
```
MEMBERS                                                 ROLE
user:maria@shopnow.com                                  roles/owner
user:ken@shopnow.com                                    roles/compute.admin      ← remove!
group:storage-team@shopnow.com                          roles/storage.admin
serviceAccount:checkout@shopnow-prod.iam.gserviceaccount.com  roles/cloudsql.client
```

| Where you looked | What you learn about Ken |
|---|---|
| **IAM page (C)** | "ken@shopnow.com → Compute Admin" ✅ |
| Roles page (D) | "Compute Admin: General Availability, 900+ permissions". Nothing about Ken ❌ |
| `gcloud iam roles list` (A) | A long list of role names ❌ |
| `gcloud iam service-accounts list` (B) | `checkout@…`. Ken isn't a service account ❌ |

---

## 🧠 Key Takeaways / Memory Tips

- **"Who has which role in a project" → IAM page** (or `gcloud projects get-iam-policy PROJECT`).
  🧠 *"**IAM page = WHO has WHAT. Roles page = WHAT each role can do.**"*
- `gcloud iam roles list` = catalog of roles. `gcloud iam service-accounts list` = machine accounts. Neither shows assignments.
- Roles page "**status**" = launch stage of the role (GA/Beta/Disabled), not who uses it.
- Related: **Q010** (custom roles live on the Roles page), **Q025** (granting roles to groups).

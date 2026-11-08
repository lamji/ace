# Q106: Minimum Role for the Person Who Creates and Manages Service Accounts (Service Account Admin)

**Topic:** IAM (service account roles: admin vs user, securityAdmin, roleAdmin)

## ❓ Question
> Your organization has a dedicated person who creates and manages all service accounts for Google Cloud projects. You need to assign this person the minimum role for projects. What should you do?
>
> **A.** Add the user to roles/iam.roleAdmin role.
>
> **B.** Add the user to roles/iam.securityAdmin role.
>
> **C.** Add the user to roles/iam.serviceAccountUser role.
>
> **D.** Add the user to roles/iam.serviceAccountAdmin role.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** One person creates and manages all service accounts in your projects.
- **What you must achieve:** Give that person the smallest role that lets them do this job.
- **The limits:** Minimum permissions.
- **What they're really asking:** Which role should they get?

**Clues in the question:**
- "**creates and manages all service accounts**" → **Service Account Admin**.
- "**minimum role**": not securityAdmin (much broader) and not roleAdmin (custom roles).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Service account (review from Q019)
- **What it is:** An **account for a program, not a person**. VMs and apps use it to call Google APIs.
- **Looks like:** `checkout-sa@shopnow-prod.iam.gserviceaccount.com`
- **Not to be confused with:** a user account.
- **Analogy:** 🤖 A **badge for the office robot**.
- **In the online store:** The checkout VM runs as checkout-sa.

### 2. roles/iam.serviceAccountAdmin 🔑
- **What it is:** Lets someone **create, update, disable and delete service accounts** and manage who can use them.
- **Looks like:** `gcloud iam service-accounts create checkout-sa`
- **Not to be confused with:** serviceAccountUser.
- **Analogy:** 🏭 The person who **makes and manages the robot badges**.
- **In the online store:** The platform admin creates all ShopNow service accounts.

### 3. roles/iam.serviceAccountUser
- **What it is:** Lets someone **run things as** an existing service account (for example, attach it to a VM). It can't create one.
- **Looks like:** `gcloud compute instances create web-1 --service-account=checkout-sa@...`
- **Not to be confused with:** serviceAccountAdmin.
- **Analogy:** 🤖 **Borrowing** a robot badge.
- **In the online store:** Developers attach checkout-sa to their VM.

### 4. roles/iam.securityAdmin / roleAdmin
- **What it is:** securityAdmin = manage **all IAM policies** (very broad). roleAdmin = create and edit **custom roles**.
- **Looks like:** `roles/iam.securityAdmin`
- **Not to be confused with:** a minimum role for service accounts.
- **Analogy:** 🔑 The head of security / the badge-type designer.
- **In the online store:** Not given to the service account admin.

### 🔗 How they fit together
```
 creates/manages service accounts → roles/iam.serviceAccountAdmin ✅ (minimum)
 uses an existing service account → roles/iam.serviceAccountUser
 manages all IAM policies         → roles/iam.securityAdmin (too broad)
 designs custom roles             → roles/iam.roleAdmin (different job)
```

---

## 🌍 Real-World Scenario

A platform engineer is the only person allowed to create service accounts for every app. The admin grants **Service Account Admin** on the projects. The engineer can create and manage service accounts, but can't change project IAM policies.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add the user to roles/iam.roleAdmin role.

**Wrong words:**
- ❌ "**roles/iam.roleAdmin**": it creates and edits custom roles. It doesn't create service accounts.

📌 **When to use it:** Use it for the person who designs custom roles.
🏢 **Office example:** Asking the badge-type designer to make the robot badges.

### ❌ B
> **B.** Add the user to roles/iam.securityAdmin role.

**Wrong words:**
- ❌ "**roles/iam.securityAdmin**": it can change IAM policies on everything. Far more than "minimum".

📌 **When to use it:** Use it for the security lead who manages all access.
🏢 **Office example:** Giving someone the master key just to make robot badges.

### ❌ C
> **C.** Add the user to roles/iam.serviceAccountUser role.

**Wrong words:**
- ❌ "**roles/iam.serviceAccountUser**": it can **use** an existing service account, but can't **create or manage** one.

📌 **When to use it:** Use it when someone must run a VM or app as an existing service account.
🏢 **Office example:** Letting someone borrow a robot badge, but not make new ones.

### ✅ D
> **D.** Add the user to roles/iam.serviceAccountAdmin role.

**Why it's correct:**
- ✔️ "**roles/iam.serviceAccountAdmin**" matches "**creates and manages all service accounts**": exactly the create/update/delete permissions for service accounts.
- ✔️ "**serviceAccountAdmin**" matches "**minimum role**": it doesn't grant broader IAM or custom-role powers.

📌 **When to use it:** Use it when one person's job is to make and manage the program accounts.
🏢 **Office example:** The person at the badge office who makes and manages the robot badges.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member=user:platform-admin@shopnow.com --role=roles/iam.serviceAccountAdmin
gcloud iam service-accounts create checkout-sa --project=shopnow-prod   # works ✅
gcloud projects add-iam-policy-binding shopnow-prod --member=... --role=roles/owner  # denied ✅
```

---

## 🧠 Key Takeaways / Memory Tips

- **Create/manage service accounts → serviceAccountAdmin. Use one → serviceAccountUser.**
- securityAdmin and roleAdmin are different, broader jobs.
  🧠 *"**Admin makes the robot badge, User borrows it.**"*
- Related: **Q070** (service account keys), **Q019** (service accounts on VMs), **Q100** (roleAdmin).

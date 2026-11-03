# Q083: Giving G Suite Users Access to a Project (Grant IAM Roles to Their Email)

**Topic:** IAM (Google Workspace / G Suite accounts, IAM members)

## ❓ Question
> Your organization uses G Suite for communication and collaboration. All users in your organization have a G Suite account. You want to grant some G Suite users access to your Cloud Platform project. What should you do?
>
> **A.** Enable Cloud Identity in the GCP Console for your domain.
>
> **B.** Grant them the required IAM roles using their G Suite email address.
>
> **C.** Create a CSV sheet with all users' email addresses. Use the gcloud command line tool to convert them into Google Cloud Platform accounts.
>
> **D.** In the G Suite console, add the users to a special group called cloud-console-users@yourdomain.com. Rely on the default behavior of the Cloud Platform to grant users access if they are members of this group.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Everyone already has a G Suite (now called **Google Workspace**) account. You want a few of them to use your Google Cloud project. What do you do?

**Clues in the question:**
- "**All users in your organization have a G Suite account**": they already have **Google accounts**, so nothing new needs to be created.
- "**grant some G Suite users access**": in Google Cloud, access = **IAM roles** given to an account's email.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1️⃣ G Suite / Google Workspace account
- **What it is:** A **company Google account** (email, Drive, Calendar) like `ana@shopnow.com`. It's a full Google identity, so it can sign in to Google Cloud too.
- **Looks like:** `ana@shopnow.com` (signs in to Gmail, Docs, and the Cloud console)
- **Not to be confused with:** a separate "Google Cloud account". There's no separate account to create.
- **Analogy:** 🪪 The **company ID card** everyone already has.
- **In the online store:** ShopNow developers use their `@shopnow.com` accounts.

### 2️⃣ IAM role binding 🔑
- **What it is:** A **rule that says "this email gets this role on this project"**. That's how anyone gets access in Google Cloud.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-prod --member=user:ana@shopnow.com --role=roles/viewer`
- **Not to be confused with:** creating an account. The account already exists; you're just giving it permission.
- **Analogy:** 🚪 Adding an employee's ID card to the **door access list** for one room.

### 3️⃣ Cloud Identity
- **What it is:** Google's **identity service for companies that don't have Google Workspace**. It creates Google accounts (without Gmail/Docs) for staff.
- **Not to be confused with:** a switch that grants project access. Workspace users already have identities.
- **Analogy:** 🪪 Issuing ID cards to people who **don't have one yet**.

### 🔗 How they fit together
```
 Google Workspace (shopnow.com)
   └── ana@shopnow.com  (already a Google identity)
           │
           ▼  IAM binding: user:ana@shopnow.com → roles/editor on shopnow-dev ✅
     Google Cloud project shopnow-dev
```

---

## 🌍 Real-World Scenario

A company already uses Gmail and Google Docs through Workspace. A few developers now need Google Cloud. The admin opens **IAM → Grant access**, types each developer's company email (or, better, a Google group), and picks the roles. The developers sign in to the Cloud console with the same account they use for email.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable Cloud Identity in the GCP Console for your domain.

**Wrong words:**
- ❌ "**Enable Cloud Identity**": Cloud Identity creates accounts for people who don't have Google accounts. Workspace users already have them, and enabling it grants **no** project access.

📌 **When to use it:** Use Cloud Identity when your staff don't have Google Workspace accounts and need Google identities.
🏢 **Office example:** Printing ID cards for new contractors who don't have one yet.

### ✅ B
> **B.** Grant them the required IAM roles using their G Suite email address.

**Why it's correct:**
- ✔️ "**using their G Suite email address**" matches "**All users in your organization have a G Suite account**": their existing accounts are already valid Google identities, so you use them directly.
- ✔️ "**Grant them the required IAM roles**" matches "**grant some G Suite users access to your Cloud Platform project**": IAM roles are how access is given, and only the chosen users get them.

📌 **When to use it:** Use it when people already have company accounts and just need permission for a project.
🏢 **Office example:** Adding a few employees' existing ID cards to the access list for the server room.

### ❌ C
> **C.** Create a CSV sheet with all users' email addresses. Use the gcloud command line tool to convert them into Google Cloud Platform accounts.

**Wrong words:**
- ❌ "**convert them into Google Cloud Platform accounts**": there's no such thing. A Workspace account **is** already a Google account, and gcloud has no "convert" command.
- ❌ "**all users' email addresses**": the question says only **some** users.

📌 **When to use it:** **Never use this.** Grant IAM roles to their existing emails (B).
🏢 **Office example:** Trying to swap everyone's ID card for a "server room card" that doesn't exist.

### ❌ D
> **D.** In the G Suite console, add the users to a special group called cloud-console-users@yourdomain.com. Rely on the default behavior of the Cloud Platform to grant users access if they are members of this group.

**Wrong words:**
- ✔️ Using a group is a good idea in general.
- ❌ "**a special group called cloud-console-users@yourdomain.com**" + "**Rely on the default behavior**": no such magic group exists. A group gets access only after **you grant it an IAM role**.

📌 **When to use it:** Use a group when many people need the same access, but you must still give the group an IAM role.
🏢 **Office example:** Putting names on a list called "server room people" and expecting the door to open without telling security.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow uses Google Workspace. Ana and Ben (developers) need access to `shopnow-dev`.

```bash
gcloud projects add-iam-policy-binding shopnow-dev --member=user:ana@shopnow.com --role=roles/editor
gcloud projects add-iam-policy-binding shopnow-dev --member=user:ben@shopnow.com --role=roles/editor
# Best practice: grant one group instead
gcloud projects add-iam-policy-binding shopnow-dev --member=group:devs@shopnow.com --role=roles/editor
```
Ana opens console.cloud.google.com, signs in with `ana@shopnow.com`, and sees `shopnow-dev`.

---

## 🧠 Key Takeaways / Memory Tips

- **Workspace/G Suite accounts are Google accounts.** Just grant IAM roles to their emails.
- **Cloud Identity** = accounts for people **without** Workspace.
- No group gets access "by default". Every group needs an IAM role.
  🧠 *"**Already have a Google email? Just add the role.**"*
- Related: **Q025** (groups for auditors), **Q080** (Viewer role).

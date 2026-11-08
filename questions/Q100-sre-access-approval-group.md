# Q100: Letting SREs Approve Google Support Access Requests (Group + Access Approval Approver)

**Topic:** IAM / security (Access Approval, groups, least privilege)

## ❓ Question
> Your organization has strict requirements to control access to Google Cloud projects. You need to enable your Site Reliability Engineers (SREs) to approve requests from the Google Cloud support team when an SRE opens a support case. You want to follow Google-recommended practices. What should you do?
>
> **A.** Add your SREs to roles/iam.roleAdmin role.
>
> **B.** Add your SREs to roles/accessapproval.approver role.
>
> **C.** Add your SREs to a group and then add this group to roles/iam.roleAdmin.role.
>
> **D.** Add your SREs to a group and then add this group to roles/accessapproval.approver role.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your organization strictly controls access to projects. When an SRE (site reliability engineer) opens a support case, Google support staff may ask for access.
- **What you must achieve:** Let SREs approve those access requests from Google support.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** Which feature and role let SREs approve Google support's access requests?

**Clues in the question:**
- "**approve requests from the Google Cloud support team**": that's **Access Approval** → role `roles/accessapproval.approver`.
- "**Google-recommended practices**": grant roles to a **group**, not to each person.
- "**strict requirements to control access**": least privilege, so not a role-management role like `iam.roleAdmin`.

**Exam topic:** IAM / security.

---

## 📚 Key Terms Explained

### 1️⃣ Access Approval 🔑
- **What it is:** A Google Cloud feature where **Google support staff must ask your permission** before accessing your content. Your approvers get a request and click **Approve** or **Dismiss**.
- **Looks like:** email: "Google Support requests access to project shopnow-prod for case #12345 — Approve / Dismiss"
- **Not to be confused with:** Access Transparency (which only **logs** what Google staff did, after the fact).
- **Analogy:** 🔐 An outside repair technician must get a manager's **signature** before entering the server room.

### 2️⃣ roles/accessapproval.approver
- **What it is:** The IAM role that lets someone **view and approve/dismiss** Access Approval requests.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-prod --member=group:sre@shopnow.com --role=roles/accessapproval.approver`

### 3️⃣ roles/iam.roleAdmin
- **What it is:** A role to **create and edit custom IAM roles**. It has nothing to do with approving support access, and it's powerful.
- **Not to be confused with:** an approver role.
- **Analogy:** 🔑 The person who **designs the badge types**, not the one who signs the repair visit.

### 4️⃣ Google group (best practice)
- **What it is:** A **named list of email addresses**. Grant the role once to the group; add or remove people from the list.
- **Looks like:** `sre@shopnow.com = [ana@shopnow.com, ben@shopnow.com, cara@shopnow.com]`
- **Not to be confused with:** a shared account. Each SRE signs in with their own account.

### 🔗 How they fit together
```
 Google Support → access request → Access Approval
                                       │
            group sre@shopnow.com ── roles/accessapproval.approver ✅ → Approve / Dismiss
```

---

## 🌍 Real-World Scenario

A bank opens a support case about a broken database. Google's engineer needs to look inside. Because the bank enabled **Access Approval**, the request goes to the `sre@` group. An on-call SRE reviews it and approves it for that case only.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add your SREs to roles/iam.roleAdmin role.

**Wrong words:**
- ❌ "**roles/iam.roleAdmin**": it manages custom roles. It **can't approve** support access, and it's far too powerful for "strict" access control.
- ❌ "**Add your SREs**" (individually): Google recommends granting roles to groups.

📌 **When to use it:** Use it for the security admin who creates and edits custom roles.
🏢 **Office example:** Letting SREs design new badge types, when they only needed to sign repair visits.

### ❌ B
> **B.** Add your SREs to roles/accessapproval.approver role.

**Wrong words:**
- ✔️ "roles/accessapproval.approver" is the right role.
- ❌ "**Add your SREs**" (each person directly): not Google's recommended practice. Use a group so you manage membership in one place.

📌 **When to use it:** Use it for a single person when there's no group, such as a small test project.
🏢 **Office example:** Writing each SRE's name on the door list one by one instead of using the team list.

### ❌ C
> **C.** Add your SREs to a group and then add this group to roles/iam.roleAdmin.role.

**Wrong words:**
- ✔️ "Add your SREs to a group" is the right practice.
- ❌ "**roles/iam.roleAdmin**": wrong role (see A).

📌 **When to use it:** Use it when a team of security admins must manage custom roles.
🏢 **Office example:** Giving the SRE team the badge-design job instead of the repair-sign-off job.

### ✅ D
> **D.** Add your SREs to a group and then add this group to roles/accessapproval.approver role.

**Why it's correct:**
- ✔️ "**roles/accessapproval.approver**" matches "**approve requests from the Google Cloud support team**": this role lets them approve or dismiss Google Support access requests.
- ✔️ "**Add your SREs to a group and then add this group**" matches "**follow Google-recommended practices**": roles go to groups, not individuals.
- ✔️ "**approver**" (only this one task) matches "**strict requirements to control access**": no extra powers.

📌 **When to use it:** Use it when a team must sign off on outside staff entering your systems.
🏢 **Office example:** Putting the on-call team on the list of people who can sign the repair technician's entry form.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow enables Access Approval on `shopnow-prod`.

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member=group:sre@shopnow.com --role=roles/accessapproval.approver
```
ShopNow opens a support case about Cloud SQL. Google's engineer requests access, and on-call SRE Ben gets the request and approves it for that case. When Ben leaves the company, he's removed from `sre@shopnow.com` and loses the approver role automatically.

---

## 🧠 Key Takeaways / Memory Tips

- **Approve Google Support access → Access Approval → `roles/accessapproval.approver`.**
- **Google best practice: grant roles to groups**, not individuals.
  🧠 *"**Support wants in? SRE group approves.**"*
- Related: **Q025** (groups for auditors), **Q099** (billing viewer), **Q080** (Viewer).

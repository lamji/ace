# G001: Employees Sign In With Their Existing Entra ID Accounts, No Account Sync (Workforce Identity Federation)

**Topic:** Identity (Workforce Identity Federation)
**Exam guide section:** 1.1 Setting up cloud projects and accounts: Configuring Workforce Identity Federation

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your company uses Microsoft Entra ID as its identity provider for all employees. The security team does not want employee accounts copied or synchronized into Cloud Identity. Members of the data team must sign in to the Google Cloud console and use BigQuery with their existing Entra ID credentials. You want to follow Google-recommended practices. What should you do?
>
> **A.** Configure Workforce Identity Federation with a workforce pool and an Entra ID provider, and grant the BigQuery roles to the data team's group by using its principalSet identifier.
>
> **B.** Use Google Cloud Directory Sync to copy the Entra ID users into Cloud Identity, and grant the BigQuery roles to the synced users.
>
> **C.** Configure Workload Identity Federation with a workload identity pool for Entra ID, and let employees impersonate a service account that has the BigQuery roles.
>
> **D.** Create a service account with the BigQuery roles, download a JSON key, and share the key with the data team through Secret Manager.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company keeps its employee logins in Microsoft Entra ID (Microsoft's company login system, formerly Azure AD). The security team does not want a second copy of those accounts inside Google.
- **What you must achieve:** Let the data team open the Google Cloud console and use BigQuery while signing in with the Microsoft login they already have.
- **The limits:** No copying or syncing accounts into Cloud Identity (Google's own user directory). It must follow Google's recommended way.
- **What they're really asking:** How do you let real people from an outside login system into Google Cloud without creating Google accounts for them?

**Clues in the question:**
- "**does not want employee accounts copied or synchronized**" rules out syncing tools like GCDS.
- "**employees … sign in to the Google Cloud console**" means these are **people** (a workforce), not apps. That points to **Workforce** Identity Federation.
- "**existing Entra ID credentials**" means the outside identity provider stays the place where people sign in.

**Exam topic:** Identity and access (exam guide section 1.1, plus IAM in section 4).

---

## 📚 Key Terms Explained

### 1. Identity provider (IdP)
- **What it is:** The system that holds a company's user accounts and checks passwords. Examples: Microsoft Entra ID, Okta, Google Cloud Identity.
- **Looks like:** `login.microsoftonline.com` asking for `ana@shopnow.com` and her password
- **Not to be confused with:** Google Cloud itself. Google Cloud can trust an outside IdP and does not need to store the password.
- **Analogy:** 🪪 The HR office that issues staff ID cards.
- **In the online store:** ShopNow staff already log in to email and HR tools with Entra ID.

### 2. Workforce Identity Federation 🔑
- **What it is:** A Google Cloud feature that lets **people** sign in to the console and gcloud with an **outside** IdP (Entra ID, Okta, any SAML or OIDC provider) without having Google accounts. You set it up once at the organization level as a **workforce pool** with a **provider**.
- **Looks like:** `gcloud iam workforce-pools create shopnow-staff --organization=123456 --location=global`
- **Not to be confused with:** **Workload** Identity Federation, which is for **apps and machines** (for example GitHub Actions or AWS workloads), not for people logging in.
- **Analogy:** 🏢 A partner building's guard accepts your company badge, so you never get a second badge.
- **In the online store:** Analysts sign in to BigQuery with their Entra ID login. Nobody creates a Google account for them.

### 3. principalSet identifier
- **What it is:** How you name a whole group from the outside IdP in an IAM policy, so you can grant roles to it.
- **Looks like:** `principalSet://iam.googleapis.com/locations/global/workforcePools/shopnow-staff/group/data-team`
- **Not to be confused with:** A Google Group email like `data-team@shopnow.com`. Federated groups are written as principalSet strings.
- **Analogy:** 📋 "Everyone whose company badge says *Data Team*."
- **In the online store:** `roles/bigquery.dataViewer` and `roles/bigquery.jobUser` are granted to the data-team principalSet.

### 4. Google Cloud Directory Sync (GCDS)
- **What it is:** A tool that **copies** users and groups from Active Directory or LDAP into Cloud Identity.
- **Looks like:** GCDS runs nightly and creates `ana@shopnow.com` in Cloud Identity
- **Not to be confused with:** Federation. GCDS duplicates accounts, and federation does not.
- **Analogy:** 📇 Photocopying the whole staff list into a second filing cabinet.
- **In the online store:** Not used here, because security refused account copies.

### 🔗 How they fit together
```
 Employee ──login──► Entra ID (IdP)
                        │ token (SAML/OIDC)
                        ▼
 Google Cloud ── workforce pool "shopnow-staff" ── provider "entra"
                        │
                IAM: principalSet …/group/data-team → BigQuery roles
```

---

## 🌍 Real-World Scenario

A retailer standardised on Microsoft Entra ID years ago. When the data team starts using BigQuery, security says: *"No second copy of our users anywhere."* The cloud engineer creates a **workforce pool** at the organization level, adds Entra ID as an OIDC provider, and grants BigQuery roles to the Entra ID group. Analysts open the console, get sent to the Microsoft login page, and land in BigQuery. When someone leaves the company, disabling them in Entra ID removes their Google Cloud access too.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Configure Workforce Identity Federation with a workforce pool and an Entra ID provider, and grant the BigQuery roles to the data team's group by using its principalSet identifier.

**Why it's correct:**
- ✔️ "**Workforce Identity Federation with a workforce pool and an Entra ID provider**" matches "**sign in … with their existing Entra ID credentials**": Google trusts Entra ID logins directly.
- ✔️ "**grant the BigQuery roles to the data team's group by using its principalSet identifier**" matches "**members of the data team**" and Google-recommended practice: grant to a group, not to individuals.
- ✔️ Nothing is copied into Cloud Identity, so it matches "**does not want employee accounts copied or synchronized**".

📌 **When to use it:** Use it when your staff already have company logins elsewhere and you want them to use those logins for Google Cloud.
🏢 **Office example:** A partner office accepts your own company badge at its front desk, so no second badge is printed.

### ❌ B
> **B.** Use Google Cloud Directory Sync to copy the Entra ID users into Cloud Identity, and grant the BigQuery roles to the synced users.

**Wrong words:**
- ❌ "**Use Google Cloud Directory Sync to copy the Entra ID users into Cloud Identity**": this copies the accounts, which the question explicitly forbids ("does not want employee accounts copied or synchronized").

📌 **When to use it:** Use it when the company is fine keeping a synced copy of its staff list in Google.
🏢 **Office example:** Photocopying the staff directory into a second cabinet each night.

### ❌ C
> **C.** Configure Workload Identity Federation with a workload identity pool for Entra ID, and let employees impersonate a service account that has the BigQuery roles.

**Wrong words:**
- ❌ "**Workload Identity Federation with a workload identity pool**": workload federation is for **apps and machines**, not for people signing in to the console.
- ❌ "**let employees impersonate a service account**": everyone would act as one shared robot account, and audit logs lose who did what.

📌 **When to use it:** Use it when a program running outside Google (for example in AWS or a CI pipeline) needs to call Google Cloud without a key file.
🏢 **Office example:** Giving the delivery robot its own access card, not the staff.

### ❌ D
> **D.** Create a service account with the BigQuery roles, download a JSON key, and share the key with the data team through Secret Manager.

**Wrong words:**
- ❌ "**download a JSON key, and share the key with the data team**": a shared, long-lived secret. Anyone with the file has access, and logs can't tell people apart. This is the opposite of recommended practice.

📌 **When to use it:** Never use this. Give each person their own login, through federation or through Cloud Identity accounts.
🏢 **Office example:** Never hand the whole team one copied master key to the records room.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** analysts use Entra ID:
- Workforce pool `shopnow-staff` → provider `entra-oidc`.
- IAM on project `shopnow-analytics`: `principalSet://…/group/data-team` gets `roles/bigquery.dataViewer` and `roles/bigquery.jobUser`.
- An analyst opens `console.cloud.google.com/?workforce_pool=…`, signs in with Microsoft, and queries the `orders` dataset.

---

## 🧠 Key Takeaways / Memory Tips

- **People + outside IdP + no account copy → Workforce Identity Federation.**
- **Apps or machines outside Google → Workload Identity Federation.** Remember *Work**force** = people, Work**load** = programs*.
  🧠 *"**Workforce = people, Workload = programs.**"*
- Related: **Q105**, **Q109**, **Q337** (GCDS and third-party IdP); **Q301**, **Q360** (Workload Identity).

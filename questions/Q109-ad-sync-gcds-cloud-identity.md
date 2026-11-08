# Q109: Active Directory as the Source of Truth for Google Accounts (Google Cloud Directory Sync)

**Topic:** Identity (GCDS, Cloud Identity, Active Directory)

## ❓ Question
> Your organization has user identities in Active Directory. Your organization wants to use Active Directory as their source of truth for identities. Your organization wants to have full control over the Google accounts used by employees for all Google services, including your Google Cloud Platform (GCP) organization. What should you do?
>
> **A.** Use Google Cloud Directory Sync (GCDS) to synchronize users into Cloud Identity.
>
> **B.** Use the cloud Identity APIs and write a script to synchronize users to Cloud Identity.
>
> **C.** Export users from Active Directory as a CSV and import them to Cloud Identity via the Admin Console.
>
> **D.** Ask each employee to create a Google account using self signup. Require that each employee use their company email address and password.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Employee identities live in Active Directory (Microsoft's company directory), which stays the source of truth.
- **What you must achieve:** Have full control over employees' Google accounts for all Google services, including Google Cloud.
- **The limits:** None stated.
- **What they're really asking:** How do you connect Active Directory to Google accounts?

**Clues in the question:**
- "**Active Directory as their source of truth**": users are created and removed in AD, and Google must follow automatically.
- "**full control over the Google accounts**": accounts must be **managed** in the company's Cloud Identity, not personal sign-ups.
- Google's ready-made tool for AD → Cloud Identity sync is **GCDS**.

**Exam topic:** Identity.

---

## 📚 Key Terms Explained

### 1. Active Directory (AD)
- **What it is:** Microsoft's **company directory**: the master list of employees, groups and passwords.
- **Looks like:** `CN=Ana Cruz,OU=Staff,DC=shopnow,DC=local`
- **Not to be confused with:** Google's directory.
- **Analogy:** 📇 HR's **official staff register**.
- **In the online store:** ShopNow's HR adds new hires in AD.

### 2. Google Cloud Directory Sync (GCDS) 🔑
- **What it is:** A **free Google tool** that regularly **copies users and groups from AD (or LDAP) into Cloud Identity / Workspace**. One-way: AD stays the master.
- **Looks like:** GCDS config: LDAP server `ad.shopnow.local`, sync every hour, create/suspend users and groups
- **Not to be confused with:** SSO (which handles passwords at login).
- **Analogy:** 📋 An assistant who copies the official staff register to the Google front desk every hour.
- **In the online store:** A new hire in AD gets a Google account within the hour.

### 3. Cloud Identity
- **What it is:** Google's **directory of managed company accounts** (without Gmail/Docs).
- **Looks like:** `ana@shopnow.com` managed by ShopNow's admin
- **Not to be confused with:** personal Gmail accounts.
- **Analogy:** 🪪 Company-issued ID cards.
- **In the online store:** All ShopNow staff accounts are managed here.

### 🔗 How they fit together
```
 Active Directory (source of truth)
     │  GCDS (scheduled one-way sync) ✅
     ▼
 Cloud Identity (shopnow.com) → Google Cloud org, Workspace, all Google services
```

---

## 🌍 Real-World Scenario

A company of 3,000 employees uses AD for everything. When it adopts Google Cloud, IT installs **GCDS**, which syncs users and groups every hour. When HR disables someone in AD, GCDS suspends their Google account too.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use Google Cloud Directory Sync (GCDS) to synchronize users into Cloud Identity.

**Why it's correct:**
- ✔️ "**Google Cloud Directory Sync (GCDS)**" matches "**Active Directory as their source of truth**": it copies AD to Google on a schedule, and AD stays the master.
- ✔️ "**synchronize users into Cloud Identity**" matches "**full control over the Google accounts … for all Google services**": the accounts are company-managed in Cloud Identity.

📌 **When to use it:** Use it when one official list must automatically drive accounts in another system.
🏢 **Office example:** An assistant who copies HR's official staff register to the Google front desk every hour.

### ❌ B
> **B.** Use the cloud Identity APIs and write a script to synchronize users to Cloud Identity.

**Wrong words:**
- ❌ "**write a script**": you'd build and maintain your own sync tool when Google already provides GCDS.

📌 **When to use it:** Use the APIs only for special cases GCDS can't handle.
🏢 **Office example:** Writing your own copy program instead of using the official assistant.

### ❌ C
> **C.** Export users from Active Directory as a CSV and import them to Cloud Identity via the Admin Console.

**Wrong words:**
- ❌ "**Export … as a CSV and import**": a one-time copy. New hires and leavers aren't synced afterwards, so AD isn't really the source of truth.

📌 **When to use it:** Use a CSV import for a one-time initial load.
🏢 **Office example:** Photocopying the staff list once and never updating it.

### ❌ D
> **D.** Ask each employee to create a Google account using self signup. Require that each employee use their company email address and password.

**Wrong words:**
- ❌ "**self signup**": employees create their own consumer accounts, so the company doesn't have full control.
- ❌ "**use their company email address and password**": reusing passwords is a security risk.

📌 **When to use it:** **Never use this.** Use GCDS (A).
🏢 **Office example:** Letting every employee print their own ID card.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow installs GCDS on a Windows server next to AD:
- Source: `ldap://ad.shopnow.local`, OU `Staff`
- Target: Cloud Identity `shopnow.com`
- Sync: every hour; create, update, suspend users; sync groups like `devs@`, `finance@`

New hire Cara is added to AD at 9:00 and can sign in to the Cloud console by 10:00.

---

## 🧠 Key Takeaways / Memory Tips

- **AD is the master list → GCDS sync into Cloud Identity.**
- Add **SAML SSO** (Q105) if users should also log in with AD passwords.
- CSV = one-time; self signup = no control.
  🧠 *"**AD is the boss, GCDS copies it to Google.**"*
- Related: **Q105** (SAML SSO), **Q083** (Workspace users).

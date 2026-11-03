# Q337: Provision Identities for Certain LDAP OUs, Auto-Updated on Changes (Google Cloud Directory Sync)

**Topic:** Identity (Cloud Identity, GCDS)

## ❓ Question
> Your company’s management has chosen Google Cloud as its strategic cloud provider. You need to provision Google Cloud identities for all employees in the IT and Data departments but not to other departments. This access should automatically update when employees change departments, join, or leave the company. All employees are managed centrally in an LDAP directory, with one organizational unit (OU) for each department. What should you do?
>
> **A.** Develop a containerized application that reads user information from the relevant OUs in the LDAP directory. Use the Directory API to create accounts in Cloud Identity for new users. Deploy the application as a scheduled Cloud Run job.
>
> **B.** Develop a containerized application that reads user information from the relevant OUs in the LDAP directory. Use the Admin SDK to synchronize user accounts in Identity Platform with the LDAP directory. Deploy the application as a scheduled Cloud Run job.
>
> **C.** Create a CSV file with the users from the relevant OUs. Upload the CSV file to Cloud Identity. Instruct your Human Resources department to repeat this process for any employee changes.
>
> **D.** Configure Google Cloud Directory Sync to synchronize the relevant OUs between the LDAP directory and Cloud Identity. Set up a scheduled task that triggers a provisioning run.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Create Google identities for **IT and Data OUs** from **LDAP**, auto-updated.

**Clues in the question:**
- "**LDAP directory**" + "**automatically update**" + only some OUs → **Google Cloud Directory Sync (GCDS)** with OU filters, scheduled.

**Exam topic:** Identity.

---

## 📚 Key Terms Explained

### 1. Google Cloud Directory Sync (GCDS) 🔑
- **What it is:** Free Google tool that syncs users/groups from LDAP/Active Directory to Cloud Identity / Workspace, one-way, with filters.
- **Looks like:** GCDS config: base DN `ou=IT,dc=corp` + `ou=Data,dc=corp`; scheduled hourly
- **Not to be confused with:** Identity Platform (customer app logins).
- **Analogy:** 📇 HR's list copied to the badge system every hour.
- **In the online store:** ShopNow employee accounts.

### 🔗 How they fit together
```
 LDAP (OU=IT, OU=Data) ─GCDS (scheduled)─► Cloud Identity ✅
```

---

## 🌍 Real-World Scenario

IT configures **GCDS** to sync the IT and Data OUs every hour; leavers are suspended automatically.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Develop a containerized application that reads user information from the relevant OUs in the LDAP directory. Use the Directory API to create accounts in Cloud Identity for new users. Deploy the application as a scheduled Cloud Run job.

**Wrong words:**
- ❌ "**Develop a containerized application**": custom code; only creates new users (no updates/removals).

📌 **When to use it:** **Avoid** — GCDS exists.
🏢 **Office example:** Writing your own HR sync program.

### ❌ B
> **B.** Develop a containerized application that reads user information from the relevant OUs in the LDAP directory. Use the Admin SDK to synchronize user accounts in Identity Platform with the LDAP directory. Deploy the application as a scheduled Cloud Run job.

**Wrong words:**
- ❌ "**Identity Platform**": for customer-facing app logins, not employee Google Cloud identities; plus custom code.

📌 **When to use it:** Use Identity Platform for your app's customers.
🏢 **Office example:** The shop's customer loyalty system for staff badges.

### ❌ C
> **C.** Create a CSV file with the users from the relevant OUs. Upload the CSV file to Cloud Identity. Instruct your Human Resources department to repeat this process for any employee changes.

**Wrong words:**
- ❌ "**CSV file … repeat this process**": manual.

📌 **When to use it:** Use CSV for one-time bulk uploads.
🏢 **Office example:** Retyping the staff list each month.

### ✅ D
> **D.** Configure Google Cloud Directory Sync to synchronize the relevant OUs between the LDAP directory and Cloud Identity. Set up a scheduled task that triggers a provisioning run.

**Why it's correct:**
- ✔️ "**Google Cloud Directory Sync … relevant OUs**" matches "**IT and Data departments but not to other departments**".
- ✔️ "**scheduled task that triggers a provisioning run**" matches "**automatically update when employees change departments, join, or leave**".

📌 **When to use it:** Use it when your staff list lives in your own directory and the cloud accounts should follow it automatically.
🏢 **Office example:** The badge system copies HR's list for two departments every hour.

---

## 🛒 E-Commerce Full-Stack Example

GCDS syncs `ou=Engineering` and `ou=Data` to `shopnow.com` Cloud Identity hourly.

---

## 🧠 Key Takeaways / Memory Tips

- **LDAP/AD → Cloud Identity automatically → GCDS.**
  🧠 *"**Directory → GCDS → Google.**"*
- Related: **Q187**.

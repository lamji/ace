# Q025: Giving External Auditors Access to BigQuery Audit Logs

**Topic:** IAM (Google groups vs individual users, predefined vs custom roles, `roles/logging.viewer`, `roles/bigquery.dataViewer`, audit logs)

## ❓ Question
> You need to configure IAM access audit logging in BigQuery for external auditors. You want to follow Google-recommended practices. What should you do?
>
> **A.** Add the auditors group to the 'logging.viewer' and 'bigQuery.dataViewer' predefined IAM roles.
>
> **B.** Add the auditors group to two new custom IAM roles.
>
> **C.** Add the auditor user accounts to the 'logging.viewer' and 'bigQuery.dataViewer' predefined IAM roles.
>
> **D.** Add the auditor user accounts to two new custom IAM roles.

*(The `λ€˜ λ€™` characters in the screenshot are broken quote marks, shown here as `'`.)*

**My answer:** C
**Correct answer:** A
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** External auditors need to review BigQuery IAM access audit logs (records of who accessed what and when).
- **What you must achieve:** Set up their access to those logs.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** What is the recommended way to give outside auditors access to these logs?

The question is really testing **two choices at once**:

| Choice | Option pair | Google's recommendation |
|---|---|---|
| **Who** gets the role? | **Group** (A, B) vs **individual users** (C, D) | ✅ **Group** |
| **Which** role? | **Predefined** (A, C) vs **custom** (B, D) | ✅ **Predefined**, when one fits |

**Group + predefined = A.**

| Keyword | What it hints at |
|---|---|
| "**external auditors**" | Several people, who change over time, so use a **group** |
| "**Google-recommended practices**" | **Groups over individual users. Predefined roles over custom roles** |
| "**audit logging**" + "**BigQuery**" | Read-only: **`logging.viewer`** (to read logs) + **`bigquery.dataViewer`** (to read data) |

**Exam topic:** IAM best practices.

---

## 📚 Key Terms Explained

### 1️⃣ IAM Role (review)
- **What it is:** A **bundle of permissions** that you grant to someone on a resource (project, dataset, etc.).
- **Analogy:** 🪪 A **badge type**. "Visitor badge" opens the lobby. "Auditor badge" opens the records room, read-only.
- **In the online store:** `roles/cloudsql.client` lets the checkout service connect to the orders database.

### 2️⃣ Predefined Role vs Custom Role (review from Q010)
| | **Predefined role** | **Custom role** |
|---|---|---|
| Made by | **Google** | **You** |
| Kept up to date | **Google adds new permissions automatically** | **You** must maintain it |
| When to use | **Default choice** whenever one fits | Only when **no predefined role** fits closely enough |
- **Analogy:** 👔 **Standard uniforms** from the supplier vs a **tailor-made** uniform you have to re-tailor every time things change.

### 3️⃣ Google Group vs Individual User Accounts
- **Google group, what it is:** A **named list of email addresses**. Each address is a person's **own** Google account. When you give a role **to the group**, **everyone on the list** gets it. Adding or removing a person = **edit the list**, not IAM.
- **Looks like:**
  ```
  external-auditors@shopnow.com  =  [ ana@auditfirm.com, ben@auditfirm.com, cara@auditfirm.com ]
  ```
- **Not to be confused with:** a **shared account**. The group has **no password** and **nobody logs in with it**. Ana signs in as `ana@auditfirm.com`, and the audit logs show **her** email.
- **Individual user accounts:** You grant the role **to each person separately**. Every new auditor = another IAM change, and every departure = remember to remove them everywhere.
- **Analogy:** 🗂️ The **"Audit Team" list at the front desk**. Each auditor uses their **own ID card**, and the guard checks if they're on the list. Granting access to individuals is like **writing each auditor's name on the door**, one by one.
- **In the online store:** Remove Ben from `external-auditors@shopnow.com` and his BigQuery access is gone. Ana and Cara aren't affected.

### 4️⃣ `roles/logging.viewer` (Logs Viewer)
- **What it is:** **Read-only access to logs** in Cloud Logging, including **Admin Activity audit logs**. *(Detail: reading **Data Access** audit logs, meaning who read which data, needs the stronger `roles/logging.privateLogViewer`. The exam answer uses `logging.viewer`.)*
- **Analogy:** 📓 Permission to **read the building's logbook**.

### 5️⃣ `roles/bigquery.dataViewer` (BigQuery Data Viewer)
- **What it is:** **Read-only access to BigQuery datasets and tables**, so auditors can view data and table details but **can't change or delete** anything.
- **Analogy:** 👀 Permission to **read the files in the records room**, but not write on them.

### 6️⃣ Audit Logs
- **What it is:** Google Cloud's automatic record of **"who did what, where, and when"**.
  - **Admin Activity** logs: config changes, always on.
  - **Data Access** logs: who read data. These are on by default for BigQuery.
- **Analogy:** 🎥 The building's **security camera and sign-in sheet**.

### 🔗 How They Fit Together
```
👥 Google group: external-auditors@shopnow.com
     ├── auditor1@auditfirm.com
     ├── auditor2@auditfirm.com
     └── auditor3@auditfirm.com
             │  (granted ONCE, to the group)
             ▼
🪪 Predefined roles on project shopnow-analytics
     ├── roles/logging.viewer        → read the audit logs 📓
     └── roles/bigquery.dataViewer   → read BigQuery data 👀 (no editing)

New auditor next year?  → add them to the GROUP.  IAM stays the same ✅
Audit finished?         → remove them from the GROUP. Access is gone everywhere ✅
```

---

## 🌍 Real-World Scenario

Every year an **external audit firm** checks that the company's data is handled correctly. The auditors need to **see who accessed what** (audit logs) and **look at the data**, but they must **never change anything**. The audit team **changes every year**.

If you grant roles **person by person**, you'll forget someone when they leave. That's a security risk, and ironically, it's exactly what the auditors look for. 😅 A **group** with **predefined read-only roles** is simple, safe and easy to check.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Add the auditors group to the 'logging.viewer' and 'bigQuery.dataViewer' predefined IAM roles.

**Why it's correct:**
- ✔️ **Group:** grant once. Adding or removing auditors = **change the group only**.
- ✔️ **Predefined roles:** Google maintains them, and they're **already read-only**.
- ✔️ **`logging.viewer`** = read the audit logs. **`bigquery.dataViewer`** = read the data. That's all auditors need (least privilege).

**📌 When to use it:** Use it when a team of people needs the same standard access, and the team members change over time.
🏢 **Office example:** Giving the "Audit Team" list a standard read-only badge for the records room. HR just updates the list each year.

### ❌ B
> **B.** Add the auditors group to two new custom IAM roles.

**Why it's wrong:**
- ✔️ Using a **group** is right.
- ❌ **Custom roles aren't needed.** Predefined roles that fit already exist. Custom roles are **extra work** and **you** have to keep them updated.

**📌 When to use it:** Use custom roles only when no standard role fits and you need an exact, unusual set of permissions.
🏢 **Office example:** Ordering a tailor-made uniform only when no standard uniform fits the job.

### ❌ C (your answer)
> **C.** Add the auditor user accounts to the 'logging.viewer' and 'bigQuery.dataViewer' predefined IAM roles.

**Why it's wrong:**
- ✔️ The **roles are right** (predefined, read-only). Half correct!
- ❌ **Individual user accounts** instead of a **group**. Every new auditor needs **new IAM changes**, and every departing auditor must be **removed by hand**. It's easy to forget, and harder to review.
- 💡 **Likely mix-up:** A and C look almost identical. The only difference is **"group"** vs **"user accounts"**, and Google always prefers **groups**.

**📌 When to use it:** Use individual accounts only for a one-off case, like a single person who needs temporary access.
🏢 **Office example:** Writing one visitor's name on the door for a single day's visit.

### ❌ D
> **D.** Add the auditor user accounts to two new custom IAM roles.

**Why it's wrong:**
- ❌ **Both choices are wrong**: individual users **and** unnecessary custom roles. This is the most work and the hardest to manage.

**📌 When to use it:** **Never use this** for a team. Use a group with predefined roles (A).
🏢 **Office example:** Tailor-making a uniform for each auditor and writing each name on the door. Lots of work for nothing.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow stores orders and customer analytics in BigQuery in the project **`shopnow-analytics`**. The yearly **PCI/finance audit** is coming.

**1. Create the group** (in Google Workspace / Cloud Identity admin, or Google Groups):
`external-auditors@shopnow.com` → add the 3 auditors from the audit firm.

**2. Grant the predefined roles to the group once:**
```bash
gcloud projects add-iam-policy-binding shopnow-analytics \
  --member="group:external-auditors@shopnow.com" \
  --role="roles/logging.viewer"

gcloud projects add-iam-policy-binding shopnow-analytics \
  --member="group:external-auditors@shopnow.com" \
  --role="roles/bigquery.dataViewer"
```

**3. What the auditors can do:**
- ✅ In **Logs Explorer**, see audit logs such as "who changed the `orders` table permissions on Oct 3".
- ✅ In **BigQuery**, view the `orders` and `payments` tables.
- ❌ They **can't** edit or delete tables, change IAM, or run up big costs by editing data.

**4. Next year:** One auditor is replaced. The admin **updates the group** and **doesn't touch IAM at all**. ✅

**🎬 With option C:** Three separate IAM entries for three people. Next year the old auditor is **still on the list** because nobody remembered to remove them, and the new auditors flag it as a finding. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Google's IAM best practices:**
  1. **Grant roles to groups, not individual users.**
  2. **Use predefined roles before custom roles.**
  3. **Least privilege**: give only what's needed (read-only for auditors).
- 🧠 *"**Group + Predefined = Google-approved.**"* If two options differ only by "group" vs "users", **pick group**.
- **Auditors → `logging.viewer` (read logs) + `bigquery.dataViewer` (read data).** Never editor or owner.
- Bonus: **Data Access** audit logs need `roles/logging.privateLogViewer`.
- Same idea as **Q001** (grant OS Login to **the team's Google group**).

---

## 🤔 Follow-up: "Do all auditors share one email and log in with it?"

**No.** A Google group is **not a shared account**. **Nobody logs in as the group.**

- Each auditor **keeps their own account** and **own password**: `ana@auditfirm.com`, `ben@auditfirm.com`, …
- The group email (`external-auditors@shopnow.com`) is just a **name for a list of members**. It has **no password** and **you can't sign in with it**.
- IAM gives the role **to the list**. When Ana signs in **as herself**, Google checks *"Is Ana on the list?"* → yes → she gets the access.
- The **audit logs show the real person** (`ana@auditfirm.com`), never the group, so you always know **who** did what.

```
❌ Shared account (bad)                 ✅ Google group (good)
auditors@shopnow.com + 1 password        external-auditors@shopnow.com = a LIST
 ├─ Ana logs in with it                   ├─ ana@auditfirm.com  (her own login)
 ├─ Ben logs in with it                   ├─ ben@auditfirm.com  (his own login)
 └─ Cara logs in with it                  └─ cara@auditfirm.com (her own login)
Logs: "auditors@ did it" 🤷 who?          Logs: "ben@auditfirm.com did it" ✅
Someone leaves → change the password,     Someone leaves → remove them from the list
  tell everyone else                        (no one else is affected)
```

**🏢 Office example:** A group is like the **"Audit Team" list at the front desk**. Each auditor still uses **their own ID card**. The guard checks *"Is this person on the list?"* and lets them in. A **shared account** would be like everyone **using one ID card**: the sign-in sheet just says "Audit Team card", and nobody knows who actually came in.

🧠 **Remember:** **Group = a list of people. Shared account = one login for many people.** Google recommends groups and says **never share accounts or keys** (same lesson as Q001, where one shared SSH key was wrong).

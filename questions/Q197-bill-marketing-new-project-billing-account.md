# Q197: Bill Marketing Only for Their New Initiative (New Project Linked to a Marketing Billing Account)

**Topic:** Billing (projects and billing accounts)

## ❓ Question
> Your organization has three existing Google Cloud projects. You need to bill the Marketing department for only their Google Cloud services for a new initiative within their group. What should you do?
>
> **A.** 1. Verify that you are assigned the Billing Administrator IAM role for your organization's Google Cloud Project for the Marketing department. 2. Link the new project to a Marketing Billing Account.
>
> **B.** 1. Verify that you are assigned the Billing Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Set the default key-value project labels to department:marketing for all services in this project.
>
> **C.** 1. Verify that you are assigned the Organization Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Link the new project to a Marketing Billing Account.
>
> **D.** 1. Verify that you are assigned the Organization Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Set the default key-value project labels to department:marketing for all services in this project.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between A and C. Most Voted is **C**: it is the only option that **creates** the new project and **links** it to Marketing's billing account. A links a "new project" that was never created. (Strictly, linking also needs Billing Account User on the Marketing billing account.)

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your organization has three Google Cloud projects.
- **What you must achieve:** Bill the Marketing department only for its new initiative.
- **The limits:** Only Marketing's services for that initiative.
- **What they're really asking:** How do you set up billing so Marketing pays only for its own work?

**Clues in the question:**
- "**bill the Marketing department for only their … services**" → a **new project** linked to a **Marketing billing account**.
- Labels only **tag** costs; Marketing would still be billed on the shared account.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Project ↔ billing account link 🔑
- **What it is:** Each project is paid by one billing account. A separate account means a separate invoice.
- **Looks like:** `gcloud billing projects link mkt-launch --billing-account=MKT-ACCT-ID`
- **Not to be confused with:** labels.
- **Analogy:** 💳 Using the marketing department's own card.
- **In the online store:** Marketing campaign project.

### 2. Organization Administrator
- **What it is:** Manages the org's IAM and structure, including creating projects.
- **Looks like:** `roles/resourcemanager.organizationAdmin`
- **Not to be confused with:** Billing Admin.
- **Analogy:** 🏢 The building manager.
- **In the online store:** —

### 🔗 How they fit together
```
 Org
  ├─ 3 existing projects → company billing account
  └─ NEW mkt-initiative → Marketing billing account ✅
```

---

## 🌍 Real-World Scenario

Marketing launches a campaign and must pay for it. The admin creates `mkt-campaign-2026` and links it to Marketing's billing account.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Verify that you are assigned the Billing Administrator IAM role for your organization's Google Cloud Project for the Marketing department. 2. Link the new project to a Marketing Billing Account.

**Wrong words:**
- ✔️ "Link the new project to a Marketing Billing Account" is the right idea.
- ❌ "**the new project**": this option never **creates** it.
- ❌ "**Billing Administrator … for your organization's Google Cloud Project**": billing roles are set on billing accounts or the org, not on a project.

📌 **When to use it:** Use it when the project already exists and only needs a new payer.
🏢 **Office example:** Switching a card on a subscription you haven't signed up for yet.

### ❌ B
> **B.** 1. Verify that you are assigned the Billing Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Set the default key-value project labels to department:marketing for all services in this project.

**Wrong words:**
- ❌ "**Set the default key-value project labels**": labels tag costs but don't change **who is billed**.

📌 **When to use it:** Use labels to break down costs in reports.
🏢 **Office example:** Putting a "Marketing" sticker on an invoice the company still pays.

### ✅ C
> **C.** 1. Verify that you are assigned the Organization Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Link the new project to a Marketing Billing Account.

**Why it's correct:**
- ✔️ "**Create a new Google Cloud Project for the Marketing department**" matches "**for a new initiative within their group**".
- ✔️ "**Link the new project to a Marketing Billing Account**" matches "**bill the Marketing department for only their Google Cloud services**".

📌 **When to use it:** Use it when one department must pay for its own new work separately.
🏢 **Office example:** Opening a new file for marketing's project and charging it to marketing's own card.

### ❌ D
> **D.** 1. Verify that you are assigned the Organization Administrator IAM role for your organization's Google Cloud account. 2. Create a new Google Cloud Project for the Marketing department. 3. Set the default key-value project labels to department:marketing for all services in this project.

**Wrong words:**
- ✔️ "Create a new Google Cloud Project" is right.
- ❌ "**labels**": doesn't bill Marketing separately.

📌 **When to use it:** Use labels for cost reporting inside one bill.
🏢 **Office example:** A sticker, not a separate invoice.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud projects create shopnow-mkt-blackfriday --folder=MARKETING` → `gcloud billing projects link shopnow-mkt-blackfriday --billing-account=MKT-ACCOUNT-ID`

---

## 🧠 Key Takeaways / Memory Tips

- **A department pays separately → its own project linked to its own billing account.** Labels only tag.
  🧠 *"**Separate payer = separate billing account link.**"*
- Related: **Q164**, **Q156**.

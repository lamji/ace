# Q066: One Invoice for Two Organizations by Tomorrow (Link Projects to One Billing Account)

**Topic:** Billing (billing account ↔ project link across organizations, single invoice, project migration vs linking, billing export)

## ❓ Question
> Your company has an existing GCP organization with hundreds of projects and a billing account. Your company recently acquired another company that also has hundreds of projects and its own billing account. You would like to consolidate all GCP costs of both GCP organizations onto a single invoice. You would like to consolidate all costs as of tomorrow. What should you do?
>
> **A.** Link the acquired company's projects to your company's billing account.
>
> **B.** Configure the acquired company's billing account and your company's billing account to export the billing data into the same BigQuery dataset.
>
> **C.** Migrate the acquired company's projects into your company's GCP organization. Link the migrated projects to your company's billing account.
>
> **D.** Create a new GCP organization and a new billing account. Migrate the acquired company's projects and your company's projects into the new GCP organization and link the projects to the new billing account.

**My answer:** D
**Correct answer:** A
**Result:** ❌ Incorrect

> Why D was tempting: it sounds like a clean, "fresh start" for the merged company. But it means **migrating hundreds of projects from both companies** plus building a new org, which can't be done "**as of tomorrow**", and it's far more work than needed. A **billing account can pay for projects in any organization**, so you only need to **re-link** the acquired projects.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company has an organization with hundreds of projects and one billing account. It bought another company that has its own organization, hundreds of projects and its own billing account.
- **What you must achieve:** Put all costs from both companies on a single invoice.
- **The limits:** It must start tomorrow.
- **What they're really asking:** What is the quickest way to combine both companies' costs onto one bill?

| Question words | What they point to |
|---|---|
| "**single invoice**" | One invoice = one **billing account**. All projects must be linked to the same billing account |
| "**as of tomorrow**" | Must be **fast**: no big migrations |
| "**both GCP organizations**" | The projects can **stay in their own org**. A billing account can pay for projects in **any** organization |
| "**consolidate all GCP costs**" | About **billing**, not about reorganizing projects (C, D) or reports (B) |

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1️⃣ Billing account (review from Q007, Q035)
- **What it is:** The **payment record** (credit card or invoice) that Google charges. **Each billing account gets its own invoice.**
- **Looks like:** `ShopNow Main Billing (0X1A2B-3C4D5E-6F7A8B)`
- **Not to be confused with:** an organization. The billing account **pays**; the organization **holds projects in a folder tree**. They're separate, and a billing account can pay for projects in **another** organization.
- **Analogy:** 💳 The **company credit card**. Any department, even one from the newly bought company, can be put on it.
- **In the online store:** ShopNow's card pays for `shopnow-prod`, `shopnow-dev`, and now the acquired company's projects too.

### 2️⃣ Linking a project to a billing account 🔑
- **What it is:** Choosing **which billing account pays** for a project. It takes effect **right away** and can be changed anytime (with the right roles, see Q059).
- **Looks like:** `gcloud billing projects link acme-prod --billing-account=0X1A2B-3C4D5E-6F7A8B`
- **Not to be confused with:** moving the project. The project **stays in its organization**; only the payer changes.
- **Analogy:** 📋 Changing the card number on a department's expense form. The department doesn't move offices.
- **In the online store:** `acme-prod` keeps running exactly as before, but ShopNow's card now pays.

### 3️⃣ GCP organization
- **What it is:** The **top folder** of a company's Google Cloud resources, tied to its domain (e.g., `shopnow.com`). It holds folders, projects and company-wide IAM policies.
- **Looks like:** `shopnow.com (org) → folders → projects`
- **Not to be confused with:** a billing account. Merging orgs is a **separate**, slow project.
- **Analogy:** 🏢 The **company's building and org chart**.

### 4️⃣ Project migration (between organizations)
- **What it is:** Moving a project from one organization to another. It needs special permissions on both sides, policy checks and planning, project by project.
- **Looks like:** `gcloud beta projects move acme-prod --organization=123456789`
- **Not to be confused with:** relinking billing. Migration changes **where the project lives**, not just who pays.
- **Analogy:** 🚚 **Physically moving departments** into your building: slow and lots of paperwork.

### 5️⃣ Billing export to BigQuery (review from Q017)
- **What it is:** Copying billing **details** into BigQuery so you can **analyze** costs with SQL.
- **Not to be confused with:** an invoice. Exporting both accounts into one dataset gives **one report**, but you'd still get **two invoices**.
- **Analogy:** 📊 Putting both companies' receipts into **one spreadsheet**. You still pay **two** credit card bills.

### 🔗 How they fit together
```
 Your org (shopnow.com)            Acquired org (acme.com)
   ├── shopnow-prod ─┐               ├── acme-prod ─┐
   └── shopnow-dev  ─┤               └── acme-dev  ─┤  A: just relink (minutes) ✅
                     ▼                               ▼
              💳 ShopNow billing account  ◄─────────┘
                     │
                     ▼
              🧾 ONE invoice
 (Projects stay in their own orgs. Only the payer changes.)
```

---

## 🌍 Real-World Scenario

After an acquisition, finance wants one cloud bill right away, while IT plans the longer job of merging organizations, IAM and policies over the next months. The quick win: link every acquired project to the parent company's billing account. It takes effect immediately, nothing moves, and nothing breaks. The org merge can happen later, at its own pace.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Link the acquired company's projects to your company's billing account.

**Why it's correct:**

- ✔️ "**Link … to your company's billing account**" matches "**single invoice**": One billing account = one invoice for every project linked to it.
- ✔️ "**the acquired company's projects**" matches "**both GCP organizations**": A billing account can pay for projects in **another** org. The projects don't have to move.
- ✔️ Just "**Link**" (no migration) matches "**as of tomorrow**": Relinking takes effect immediately; it can be scripted for hundreds of projects in an afternoon.

📌 **When to use it:** Use it when you want one bill for several groups' projects quickly, without moving anything.
🏢 **Office example:** After buying another company, putting their departments' expenses on your company card. Nobody moves desks.

### ❌ B
> **B.** Configure the acquired company's billing account and your company's billing account to export the billing data into the same BigQuery dataset.

**Wrong words:**
- ✔️ "export the billing data into the same BigQuery dataset" gives you **one combined report**.
- ❌ "**the acquired company's billing account and your company's billing account**": there are still **two billing accounts**, so there are still **two invoices**. The question wants a **single invoice**.

📌 **When to use it:** Use it when you want to analyze both accounts' costs together, while still paying them separately.
🏢 **Office example:** Putting both companies' receipts in one spreadsheet, while still paying two separate card bills.

### ❌ C
> **C.** Migrate the acquired company's projects into your company's GCP organization. Link the migrated projects to your company's billing account.

**Wrong words:**
- ✔️ "**Link the migrated projects to your company's billing account**" would give one invoice.
- ❌ "**Migrate the acquired company's projects into your company's GCP organization**": moving **hundreds** of projects between orgs takes planning, permissions and time. It can't be done "**as of tomorrow**", and it isn't needed for billing.

📌 **When to use it:** Use it later, as a separate project, when you want both companies under one org for shared policies and IAM.
🏢 **Office example:** Physically moving the acquired company's departments into your building. Good long-term, but not by tomorrow.

### ❌ D (your answer)
> **D.** Create a new GCP organization and a new billing account. Migrate the acquired company's projects and your company's projects into the new GCP organization and link the projects to the new billing account.

**Wrong words:**
- ❌ "**Create a new GCP organization and a new billing account**": unnecessary. Your company already has a working org and billing account.
- ❌ "**Migrate the acquired company's projects and your company's projects**": moving **hundreds of projects from both companies**, which is even more work than C. Impossible "**as of tomorrow**".

📌 **When to use it:** Almost never. Use it only when both companies are merging into a brand-new company with a new domain and want a full restart, planned over months.
🏢 **Office example:** Building a brand-new office and moving both companies into it, just to get one credit card bill.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow buys **Acme Shoes**, which has 300 projects in `acme.com` and its own billing account.

```bash
# List Acme's projects and relink each one to ShopNow's billing account
for p in $(gcloud projects list --filter="parent.id=ACME_ORG_ID" --format="value(projectId)"); do
  gcloud billing projects link "$p" --billing-account=0X1A2B-3C4D5E-6F7A8B
done
```

| | Before | After A (tomorrow) |
|---|---|---|
| Organizations | shopnow.com, acme.com | shopnow.com, acme.com (unchanged) |
| Billing accounts paying | 2 | **1** (ShopNow's) |
| Invoices | 2 | **1** ✅ |
| Acme apps | running | running, nothing moved |

*(The person running this needs Billing Account User on ShopNow's billing account and Project Billing Manager or Owner on Acme's projects. See Q059.)*

---

## 🧠 Key Takeaways / Memory Tips

- **One invoice = one billing account.** Link every project to it.
- **A billing account can pay for projects in any organization.** No need to move projects.
- **"Tomorrow" / "quickly" → relink billing, never migrate projects or create orgs.**
- **BigQuery billing export = one report, not one invoice.**
  🧠 *"**Change the card, not the building.**"*
- Related: **Q007** (centralized billing account), **Q017** (billing export to BigQuery), **Q035** (link a project), **Q059** (who can link).

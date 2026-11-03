# Q007: Centralizing Projects Under One Billing Account

**Topic:** Billing (Cloud Billing accounts, payment methods, linking projects, resource hierarchy)

## ❓ Question
> Several employees at your company have been creating projects with Cloud Platform and paying for it with their personal credit cards, which the company reimburses. The company wants to centralize all these projects under a single, new billing account. What should you do?
>
> **A.** Contact cloud-billing@google.com with your bank account details and request a corporate billing account for your company.
>
> **B.** Create a ticket with Google Support and wait for their call to share your credit card details over the phone.
>
> **C.** In the Google Platform Console, go to the Resource Manage and move all projects to the root Organizarion.
>
> **D.** In the Google Cloud Platform Console, create a new billing account and set up a payment method.

*(Typos like "Resource Manage" and "Organizarion" are from the original question.)*

**My answer:** D
**Correct answer:** D
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** Employees have been paying for their Google Cloud projects with **their own credit cards**, and the company pays them back later. That's messy. The company wants **one company billing account** that pays for **all** these projects. What's the first, correct step?

| Keyword | What it hints at |
|---|---|
| "**personal credit cards**" | Each project is linked to a different personal billing account |
| "**centralize**" | One place pays for everything |
| "**single, new billing account**" | You must **create** a billing account (then link the projects to it) |
| "**What should you do?**" | The standard, self-service way in the **Cloud Console** |

**Exam topic:** Billing, specifically **creating billing accounts and linking projects**.

---

## 📚 Key Terms Explained

### 1️⃣ Project
- **What it is:** The basic **container** in Google Cloud. Every VM, database, and bucket lives inside a project. Each project must be **linked to a billing account** to use paid services.
- **Analogy:** 📁 A **department folder** in an office. All the work for that department goes inside it.
- **In the online store:** `shopnow-api-test` is a project holding the test version of the Orders API.

### 2️⃣ Cloud Billing Account
- **What it is:** The account that **pays** for Google Cloud usage. It holds the **payment method** and receives the charges. **One billing account can pay for many projects.**
- **Analogy:** 💳 The **company credit account** at the office supply store. Every department buys supplies, and all the bills go to one company account.
- **In the online store:** `ShopNow Corporate Billing` pays for every ShopNow project.

### 3️⃣ Payment Method
- **What it is:** **How** the billing account pays: a company credit/debit card or bank account (self-serve), or monthly invoices (invoiced billing).
- **Analogy:** 🏦 Choosing whether the office pays the supplier by **company card** or by **monthly invoice**.

### 4️⃣ Self-serve vs Invoiced Billing Account
- **Self-serve (online):** You create it yourself in the Cloud Console and pay by card or bank account. Charges happen automatically.
- **Invoiced (offline):** For larger companies. You get a **monthly invoice** and pay by bank transfer or check. You need to be eligible and apply for it.
- **Analogy:** 🧾 Paying at the counter with a card (self-serve) vs a supplier sending the office a bill at the end of each month (invoiced).

### 5️⃣ Linking a Project to a Billing Account
- **What it is:** Telling Google Cloud **which billing account pays for a project**. You can **change** the link anytime, which is how you move projects from personal cards to the company account.
- To link, you need permission on **both sides**:
  - On the **billing account:** `Billing Account User` (or Billing Account Administrator)
  - On the **project:** `Project Billing Manager` (or Owner)
- **Analogy:** 📝 Filling out a form that says, "From now on, send this department's bills to the company account, not to Juan's personal card."

### 6️⃣ Organization and Resource Manager
- **Organization:** The **top level** of your company in Google Cloud (e.g., `shopnow.com`). Projects and folders sit under it.
- **Resource Manager:** The Console page where you **organize** projects into folders and the organization.
- ⚠️ **Important:** Where a project sits in the organization is **separate** from who **pays** for it. Moving a project under the organization does **not** change its billing account.
- **Analogy:** 🏢 The organization chart shows **which department a team belongs to**. Accounting decides **who pays the bills**. Moving a team on the org chart doesn't change the payment arrangement.

### 7️⃣ Google Support
- **What it is:** Google's help desk for technical and billing problems. You **don't** need it to create a billing account. Google will **never** ask you to share card details by phone or email.

### 🔗 How They Fit Together
```
🏢 Organization: shopnow.com            ← WHERE projects sit (org chart)
   ├── 📁 shopnow-frontend-dev ─┐
   ├── 📁 shopnow-api-test ─────┼──► 💳 Billing account: "ShopNow Corporate Billing"   ← WHO PAYS
   └── 📁 shopnow-analytics ────┘         └── 🏦 Payment method: company card / invoice

BEFORE:  each project ──► 💳 an employee's personal card 😩
AFTER:   all projects ──► 💳 one company billing account ✅
```

---

## 🌍 Real-World Scenario

This happens a lot in growing companies. Developers want to try Google Cloud, so they create projects and pay with their own cards. Then they file expense reports every month. Finance hates it: there are many small bills, no single view of costs, and a risk that a project **stops working** if an employee's card expires or they leave the company.

The fix is to **create one company billing account** in the Cloud Console, add a company payment method, and then **link every project** to it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Contact cloud-billing@google.com with your bank account details and request a corporate billing account for your company.

**Why it's wrong:**
- ❌ That's **not how billing accounts are created**. You create them yourself in the Cloud Console.
- ❌ **Never email bank account details.** Email isn't secure, and an address like this is a classic sign of a **phishing scam**.

**📌 When to use it:** **Never use this.** Don't email bank details to anyone. Create the billing account yourself in the Cloud Console (option D).
🏢 **Office example:** Like emailing the company's bank account numbers to a general address and hoping the right person reads it. Anyone could see them.

### ❌ B
> **B.** Create a ticket with Google Support and wait for their call to share your credit card details over the phone.

**Why it's wrong:**
- ❌ Google Support **doesn't create billing accounts** for you over the phone. You don't need a ticket at all.
- ❌ **Never give card details over the phone.** This is a common scam pattern, and Google never asks for it.
- ❌ It's slow too: you wait for a call when you could do it yourself in minutes.

**📌 When to use it:** **Never use this.** Don't share card details over the phone. Use option D instead. (Use support tickets only for real problems, like a charge you don't recognize.)
🏢 **Office example:** Like someone calling the office, saying they're from the bank, and asking for the company card number. Hang up.

### ❌ C
> **C.** In the Google Platform Console, go to the Resource Manage and move all projects to the root Organizarion.

**Why it's wrong:**
- ❌ Moving projects in **Resource Manager** only changes **where they sit** in the company structure. It does **not** change **who pays**.
- ❌ The projects would still be billed to the employees' personal cards.
- ❌ The question asks for a **new billing account**, and this option never creates one.
- ⚠️ **Trap option:** "centralize" sounds like "move everything under the organization," but organization and billing are **separate**.

**📌 When to use it:** Use it when you want the company to **own and organize** the projects (one set of rules and permissions), not to change who pays.
🏢 **Office example:** Moving every employee's folders into the company's main filing cabinet. It's neater and the company controls them, but it doesn't change who pays the bills.

### ✅ D
> **D.** In the Google Cloud Platform Console, create a new billing account and set up a payment method.

**Why it's correct:**
- ✔️ This is the **standard, self-service** way to create a billing account: **Console → Billing → Create account**, then add a company payment method.
- ✔️ After that, you **link each project** to the new billing account (Billing → Account management, or `gcloud billing projects link`).
- ✔️ The company now gets **one bill**, sees all costs in one place, and employees no longer use personal cards.

**📌 When to use it:** Use it when you want **one company account to pay for many projects**.
🏢 **Office example:** Opening one company credit account with the office supply store, so employees stop paying with personal cards and filing reimbursements.

---

## 🛒 E-Commerce Full-Stack Example

At **ShopNow**, three developers each made a project and paid with their own cards:

| Project | Who created it | Paid by (before) |
|---|---|---|
| `shopnow-frontend-dev` (Next.js storefront testing) | Ana | Ana's personal Visa 💳 |
| `shopnow-api-test` (Orders API testing) | Ben | Ben's personal Mastercard 💳 |
| `shopnow-analytics` (sales dashboards) | Carla | Carla's personal Visa 💳 |

😩 **Problems:** three separate bills, three expense reports each month. And when Ben's card expired, `shopnow-api-test` **stopped working** in the middle of testing a new checkout feature.

**✅ The fix (option D, then link the projects):**

**1. Create the billing account:** Cloud Console → **Billing** → **Create account** → name it `ShopNow Corporate Billing` → add the **company card** as the payment method.

**2. Find the new billing account ID:**
```bash
gcloud billing accounts list
# ACCOUNT_ID            NAME                       OPEN
# 01A2B3-C4D5E6-F7G8H9  ShopNow Corporate Billing  True
```

**3. Link every project to it:**
```bash
gcloud billing projects link shopnow-frontend-dev --billing-account=01A2B3-C4D5E6-F7G8H9
gcloud billing projects link shopnow-api-test     --billing-account=01A2B3-C4D5E6-F7G8H9
gcloud billing projects link shopnow-analytics    --billing-account=01A2B3-C4D5E6-F7G8H9
```

**4. (Good practice) Add a budget alert so costs don't surprise finance:**
```bash
gcloud billing budgets create \
  --billing-account=01A2B3-C4D5E6-F7G8H9 \
  --display-name="ShopNow monthly budget" \
  --budget-amount=500USD \
  --threshold-rule=percent=0.9
```

**After:**
```
📁 shopnow-frontend-dev ─┐
📁 shopnow-api-test ─────┼──► 💳 ShopNow Corporate Billing (company card) ✅
📁 shopnow-analytics ────┘
```
→ **One bill**, **one cost report**, no more reimbursements, and no project stops working because someone's card expired. 🎉

---

## 🧠 Key Takeaways / Memory Tips

- **"Centralize billing" / "new billing account" → create it in the Cloud Console (Billing) + add a payment method → link the projects.**
- **One billing account can pay for many projects.** Each project has exactly **one** billing account at a time.
- **Organization (where projects sit) ≠ Billing account (who pays).**
  🧠 *"The org chart is not the bank account."*
- **Linking needs permission on both sides:** `Billing Account User` on the billing account + `Project Billing Manager` (or Owner) on the project.
- 🚩 Any option that says **email or phone your bank/card details** is **always wrong**. It's a scam pattern.

# Q164: Charge Your Personal-Card Projects to the Company Invoice (Change the Projects' Billing Account)

**Topic:** Billing (linking projects to billing accounts)

## ❓ Question
> You have experimented with Google Cloud using your own credit card and expensed the costs to your company. Your company wants to streamline the billing process and charge the costs of your projects to their monthly invoice. What should you do?
>
> **A.** Grant the financial team the IAM role of "Billing Account User" on the billing account linked to your credit card.
>
> **B.** Set up BigQuery billing export and grant your financial department IAM access to query the data.
>
> **C.** Create a ticket with Google Billing Support to ask them to send the invoice to your company.
>
> **D.** Change the billing account of your projects to the billing account of your company.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your projects bill **your card**. The company wants them on **its invoice**.

**Clues in the question:**
- "**charge the costs of your projects to their monthly invoice**": link the **projects** to the **company's billing account** (Q066).

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Change a project's billing account 🔑 (review from Q066)
- **What it is:** A project is paid by **one** billing account at a time. You can **switch** it (you need Project Billing Manager / Billing Account User).
- **Looks like:** `gcloud billing projects link my-sandbox --billing-account=COMPANY-ACCOUNT-ID`
- **Not to be confused with:** moving the project to a new org.
- **Analogy:** 💳 Switching which **card** pays for a subscription.
- **In the online store:** Move sandbox projects to the company account.

### 2. Billing account
- **What it is:** Who pays: a card or an invoice.
- **Looks like:** `01AB23-CD45EF-678901`
- **Not to be confused with:** a project.
- **Analogy:** 💳 The payment method.
- **In the online store:** ShopNow's invoiced account.

### 🔗 How they fit together
```
 project sandbox ── was: my credit card account
                 └─ now: company invoiced account ✅ (monthly invoice)
```

---

## 🌍 Real-World Scenario

An engineer has been paying for test projects with a personal card. The admin switches those **projects' billing account** to the company's invoiced account. From now on the charges appear on the company's monthly invoice.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant the financial team the IAM role of "Billing Account User" on the billing account linked to your credit card.

**Wrong words:**
- ❌ "**Billing Account User … on the billing account linked to your credit card**": finance gets access, but **your card is still charged**.

📌 **When to use it:** Use Billing Account User to let people link projects to an account.
🏢 **Office example:** Giving finance a view of your card. You still pay.

### ❌ B
> **B.** Set up BigQuery billing export and grant your financial department IAM access to query the data.

**Wrong words:**
- ❌ "**BigQuery billing export**": it shows costs but doesn't change **who pays**.

📌 **When to use it:** Use it for cost analysis.
🏢 **Office example:** Sending finance your card statement every month.

### ❌ C
> **C.** Create a ticket with Google Billing Support to ask them to send the invoice to your company.

**Wrong words:**
- ❌ "**ticket with Google Billing Support**": you can switch billing accounts yourself; support doesn't move charges.

📌 **When to use it:** Contact support for real billing problems.
🏢 **Office example:** Asking the bank to send your card bill to your boss.

### ✅ D
> **D.** Change the billing account of your projects to the billing account of your company.

**Why it's correct:**
- ✔️ "**Change the billing account of your projects**" matches "**charge the costs of your projects**".
- ✔️ "**to the billing account of your company**" matches "**to their monthly invoice**": the company's account is invoiced.

📌 **When to use it:** Use it when the company, not you, should pay for your work.
🏢 **Office example:** Switching your subscription from your personal card to the company card.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud billing projects link ana-sandbox --billing-account=01AB23-CD45EF-678901` (ShopNow's invoiced account). Ana removes her credit card afterwards.

---

## 🧠 Key Takeaways / Memory Tips

- **Who pays = the billing account linked to the project.** Switch it to change the payer.
  🧠 *"**Change the card on the project.**"*
- Related: **Q066**, **Q059**, **Q099**.

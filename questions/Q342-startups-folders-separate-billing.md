# Q342: Central Management of Acquired Startups With Separate Invoices (One Org, a Folder per Startup, Separate Billing Accounts)

**Topic:** Resource hierarchy & Billing

## ❓ Question
> You work for a large company that recently acquired three smaller startups. All of the startups’ Google Cloud resources must be centrally managed under a single Google Cloud organization. However, each startup has its own budget and financial reporting structure. You need to ensure that each startup receives a separate monthly invoice for its Google Cloud consumption. What should you do?
>
> **A.** Create a Google Cloud organization with a folder for each startup. Share a single Cloud Billing account, and use the detailed billing export to allocate costs.
>
> **B.** Create a Google Cloud organization with a folder for each startup. Configure each startup to have its own Cloud Billing account.
>
> **C.** Create a Google Cloud organization for each startup. Configure each startup to have its own Cloud Billing account.
>
> **D.** Create a Google Cloud organization for each startup. Share a single Cloud Billing account, and use the detailed billing export to allocate costs.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **One organization**, but **separate invoices** per startup.

**Clues in the question:**
- "**single Google Cloud organization**" → one org, folder per startup.
- "**separate monthly invoice**" → a **Cloud Billing account per startup** (each billing account gets its own invoice).

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Cloud Billing account → invoice 🔑
- **What it is:** Each billing account is billed separately; projects link to one billing account.
- **Looks like:** Billing accounts: `startup-a-billing`, `startup-b-billing`, `startup-c-billing`
- **Not to be confused with:** folders (organize, don't bill).
- **Analogy:** 💳 Each subsidiary's own company card.
- **In the online store:** —

### 🔗 How they fit together
```
 Org
  ├ folder startup-a → billing A (own invoice) ✅
  ├ folder startup-b → billing B ✅
  └ folder startup-c → billing C ✅
```

---

## 🌍 Real-World Scenario

After acquisitions, each startup gets a **folder** and its **own billing account**, all under one org.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Google Cloud organization with a folder for each startup. Share a single Cloud Billing account, and use the detailed billing export to allocate costs.

**Wrong words:**
- ✔️ One org with folders is right.
- ❌ "**Share a single Cloud Billing account**": one invoice; cost allocation isn't a separate invoice.

📌 **When to use it:** Use a shared account + export when one invoice is fine.
🏢 **Office example:** One company card, splitting the statement later.

### ✅ B
> **B.** Create a Google Cloud organization with a folder for each startup. Configure each startup to have its own Cloud Billing account.

**Why it's correct:**
- ✔️ "**Google Cloud organization with a folder for each startup**" matches "**centrally managed under a single Google Cloud organization**".
- ✔️ "**its own Cloud Billing account**" matches "**separate monthly invoice**".

📌 **When to use it:** Use it when divisions are run by one company but each pays its own bill.
🏢 **Office example:** Subsidiaries in one company directory, each with its own company card.

### ❌ C
> **C.** Create a Google Cloud organization for each startup. Configure each startup to have its own Cloud Billing account.

**Wrong words:**
- ❌ "**organization for each startup**": not centrally managed.

📌 **When to use it:** Use separate orgs for truly independent companies.
🏢 **Office example:** Separate companies with no shared head office.

### ❌ D
> **D.** Create a Google Cloud organization for each startup. Share a single Cloud Billing account, and use the detailed billing export to allocate costs.

**Wrong words:**
- ❌ Separate orgs and ❌ shared billing.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Separate companies sharing one card.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow acquires `quickship`: folder `quickship/` + billing `quickship-billing`.

---

## 🧠 Key Takeaways / Memory Tips

- **Central management → one org + folders. Separate invoices → separate billing accounts.**
  🧠 *"**Folders organize; billing accounts invoice.**"*
- Related: **Q316**.

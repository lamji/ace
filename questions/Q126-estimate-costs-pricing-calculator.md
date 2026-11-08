# Q126: Estimating the Monthly Cost of a Multi-Product Solution (Pricing Pages + Pricing Calculator)

**Topic:** Billing (Google Cloud pricing calculator, cost estimation)

## ❓ Question
> You have designed a solution on Google Cloud that uses multiple Google Cloud products. Your company has asked you to estimate the costs of the solution. You need to provide estimates for the monthly total cost. What should you do?
>
> **A.** For each Google Cloud product in the solution, review the pricing details on the products pricing page. Use the pricing calculator to total the monthly costs for each Google Cloud product.
>
> **B.** For each Google Cloud product in the solution, review the pricing details on the products pricing page. Create a Google Sheet that summarizes the expected monthly costs for each product.
>
> **C.** Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Navigate to the Billing Report page in the Cloud Console. Multiply the 1 week cost to determine the monthly costs.
>
> **D.** Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Use Cloud Monitoring to determine the provisioned and used resource amounts. Multiply the 1 week cost to determine the monthly costs.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your design uses several Google Cloud products.
- **What you must achieve:** Estimate the total monthly cost.
- **The limits:** None stated.
- **What they're really asking:** Which tool do you use for the estimate?

**Clues in the question:**
- "**estimate**": no need to build and pay for it first.
- "**multiple Google Cloud products**" + "**monthly total cost**": the **pricing calculator** adds up many products into one monthly estimate.

**Exam topic:** Billing / planning.

---

## 📚 Key Terms Explained

### 1. Google Cloud pricing calculator 🔑
- **What it is:** A **free web tool** where you enter each product's usage (VMs, storage, egress…) and it shows the **estimated monthly cost** and total.
- **Looks like:** cloud.google.com/products/calculator → add Compute Engine, Cloud SQL, Cloud Storage → total $/month
- **Not to be confused with:** the Billing Reports page (actual costs).
- **Analogy:** 🧮 A **quote calculator** at the office supplier: add items, get the total.
- **In the online store:** Estimate for ShopNow's new region.

### 2. Pricing pages
- **What it is:** Each product's **official price list** with the pricing details and rules (tiers, free usage, discounts).
- **Looks like:** cloud.google.com/compute/all-pricing
- **Not to be confused with:** an estimate.
- **Analogy:** 📋 The supplier's price list.
- **In the online store:** Checking Cloud SQL's HA pricing.

### 3. Billing reports
- **What it is:** Charts of **actual spending** on resources that already exist.
- **Looks like:** Console → Billing → Reports
- **Not to be confused with:** an estimate before building.
- **Analogy:** 🧾 Last month's receipts.
- **In the online store:** Review October spend.

### 🔗 How they fit together
```
 design ─► pricing pages (understand prices) ─► pricing calculator (enter usage) ─► monthly total ✅
 (don't build it and wait a week to find out)
```

---

## 🌍 Real-World Scenario

An architect proposes GKE + Cloud SQL + Cloud Storage + a load balancer. Finance wants a monthly number before approving. The architect reads each **pricing page**, enters the expected usage in the **pricing calculator**, and shares the estimate link.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** For each Google Cloud product in the solution, review the pricing details on the products pricing page. Use the pricing calculator to total the monthly costs for each Google Cloud product.

**Why it's correct:**
- ✔️ "**review the pricing details on the products pricing page**" matches "**multiple Google Cloud products**": each product's pricing rules are understood.
- ✔️ "**Use the pricing calculator to total the monthly costs**" matches "**estimates for the monthly total cost**": the calculator gives a monthly total.

📌 **When to use it:** Use it when you need a price quote before buying anything.
🏢 **Office example:** Using the supplier's quote calculator to price a whole office setup before ordering.

### ❌ B
> **B.** For each Google Cloud product in the solution, review the pricing details on the products pricing page. Create a Google Sheet that summarizes the expected monthly costs for each product.

**Wrong words:**
- ✔️ "review the pricing details" is fine.
- ❌ "**Create a Google Sheet that summarizes**": building your own spreadsheet is slower and error-prone when the official calculator exists.

📌 **When to use it:** Use a spreadsheet to combine the calculator's estimate with non-cloud costs.
🏢 **Office example:** Adding up a quote by hand when the supplier's calculator does it for you.

### ❌ C
> **C.** Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Navigate to the Billing Report page in the Cloud Console. Multiply the 1 week cost to determine the monthly costs.

**Wrong words:**
- ❌ "**Provision the solution … Leave … for 1 week**": you pay for a week just to estimate. Test traffic isn't real traffic either.

📌 **When to use it:** Use billing reports to check actual spending after launch.
🏢 **Office example:** Renting the office for a week to find out what the rent is.

### ❌ D
> **D.** Provision the solution on Google Cloud. Leave the solution provisioned for 1 week. Use Cloud Monitoring to determine the provisioned and used resource amounts. Multiply the 1 week cost to determine the monthly costs.

**Wrong words:**
- ❌ "**Provision the solution … 1 week**": same problem as C.
- ❌ "**Cloud Monitoring to determine the provisioned and used resource amounts**": Monitoring shows usage, not prices.

📌 **When to use it:** Use Monitoring to check how much capacity you actually use.
🏢 **Office example:** Measuring how many desks get used to work out the rent.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's new EU storefront: 6× e2-standard-4 GKE nodes, Cloud SQL (HA, 4 vCPU), 2 TB Cloud Storage, 5 TB egress per month. Entered in the pricing calculator, which shows the cost per product and one **monthly total**. The estimate link is shared with finance.

---

## 🧠 Key Takeaways / Memory Tips

- **Estimate before building → pricing pages + pricing calculator.**
- Billing reports = actual costs after building.
  🧠 *"**Estimate? Calculator, not a test run.**"*
- Related: **Q077** (calculator for GKE), **Q088** (budgets).

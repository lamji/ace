# Q243: Estimate the Cost of VMs + Cloud SQL for a Three-Tier App (Pricing Calculator per Resource)

**Topic:** Billing (Pricing Calculator)

## ❓ Question
> Your company is running a three-tier web application on virtual machines that use a MySQL database. You need to create an estimated total cost of cloud infrastructure to run this application on Google Cloud instances and Cloud SQL. What should you do?
>
> **A.** Create a Google spreadsheet with multiple Google Cloud resource combinations. On a separate sheet, import the current Google Cloud prices and use these prices for the calculations within formulas.
>
> **B.** Use the Google Cloud Pricing Calculator and select the Cloud Operations template to define your web application with as much detail as possible.
>
> **C.** Implement a similar architecture on Google Cloud, and run a reasonable load test on a smaller scale. Check the billing information, and calculate the estimated costs based on the real load your system usually handles.
>
> **D.** Use the Google Cloud Pricing Calculator to determine the cost of every Google Cloud resource you expect to use. Use similar size instances for the web server, and use your current on-premises machines as a comparison for Cloud SQL.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Estimate cost **before** moving: VMs + Cloud SQL.

**Clues in the question:**
- "**estimated total cost**" → **Pricing Calculator**, adding **each resource** you'll use.
- Size them like your current machines.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Pricing Calculator 🔑
- **What it is:** Google's web tool to **estimate** monthly cost by adding products and settings.
- **Looks like:** cloud.google.com/products/calculator → Compute Engine + Cloud SQL
- **Not to be confused with:** billing reports (actual costs).
- **Analogy:** 🧮 A quote form.
- **In the online store:** Estimate ShopNow migration.

### 🔗 How they fit together
```
 Pricing Calculator: 3× web VM (like on-prem) + 2× app VM + Cloud SQL (like on-prem DB) → estimate ✅
```

---

## 🌍 Real-World Scenario

Before migrating, an architect adds each VM and the Cloud SQL instance to the **Pricing Calculator**, sized like the current servers, and gets a monthly estimate.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Google spreadsheet with multiple Google Cloud resource combinations. On a separate sheet, import the current Google Cloud prices and use these prices for the calculations within formulas.

**Wrong words:**
- ❌ "**Google spreadsheet … import the current Google Cloud prices**": manual, error-prone, reinvents the calculator.

📌 **When to use it:** Use a spreadsheet only for extra what-if notes.
🏢 **Office example:** Building your own price list instead of asking for a quote.

### ❌ B
> **B.** Use the Google Cloud Pricing Calculator and select the Cloud Operations template to define your web application with as much detail as possible.

**Wrong words:**
- ✔️ "Pricing Calculator" is right.
- ❌ "**Cloud Operations template**": that's for logging/monitoring costs, not your VMs and database.

📌 **When to use it:** Use it to estimate Cloud Logging/Monitoring costs.
🏢 **Office example:** Using the electricity quote form for furniture.

### ❌ C
> **C.** Implement a similar architecture on Google Cloud, and run a reasonable load test on a smaller scale. Check the billing information, and calculate the estimated costs based on the real load your system usually handles.

**Wrong words:**
- ❌ "**Implement a similar architecture … run a … load test**": costs real money and time just to estimate.

📌 **When to use it:** Use a pilot when you need real performance data.
🏢 **Office example:** Renting the office for a month to guess the rent.

### ✅ D
> **D.** Use the Google Cloud Pricing Calculator to determine the cost of every Google Cloud resource you expect to use. Use similar size instances for the web server, and use your current on-premises machines as a comparison for Cloud SQL.

**Why it's correct:**
- ✔️ "**Pricing Calculator to determine the cost of every Google Cloud resource**" matches "**estimated total cost**".
- ✔️ "**similar size instances … current on-premises machines as a comparison for Cloud SQL**" matches "**run this application on Google Cloud instances and Cloud SQL**".

📌 **When to use it:** Use it when you need a price estimate before buying anything.
🏢 **Office example:** Filling out a supplier's quote form with the same desks and cabinets you use today.

---

## 🛒 E-Commerce Full-Stack Example

Calculator: 3× e2-standard-2 (web), 2× e2-standard-4 (API), Cloud SQL MySQL db-custom-4-16384 HA, 500 GB SSD.

---

## 🧠 Key Takeaways / Memory Tips

- **Estimate before building → Pricing Calculator, one entry per resource.**
  🧠 *"**Quote first, build later.**"*
- Related: **Q229**, **Q201**.

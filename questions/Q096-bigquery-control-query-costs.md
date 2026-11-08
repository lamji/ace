# Q096: Controlling High BigQuery Query Costs (Custom Quotas + Flat-Rate Slots)

**Topic:** BigQuery cost control (custom query quotas, on-demand vs flat-rate / capacity pricing)

## ❓ Question
> Your company implemented BigQuery as an enterprise data warehouse. Users from multiple business units run queries on this data warehouse. However, you notice that query costs for BigQuery are very high, and you need to control costs. Which two methods should you use? (Choose two.)
>
> **A.** Split the users from business units to multiple projects.
>
> **B.** Apply a user- or project-level custom query quota for BigQuery data warehouse.
>
> **C.** Create separate copies of your BigQuery data warehouse for each business unit.
>
> **D.** Split your BigQuery data warehouse into multiple data warehouses for each business unit.
>
> **E.** Change your BigQuery query model from on-demand to flat rate. Apply the appropriate number of slots to each Project.

**My answer:** — (didn't know)
**Correct answer:** B, E
**Result:** ❓ Didn't know

> ℹ️ **Note:** "Flat rate" is now called **capacity pricing (BigQuery editions, slot reservations)**. The idea is the same: pay for a fixed amount of query power instead of per byte scanned.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Many business units query a BigQuery data warehouse, and query costs are very high.
- **What you must achieve:** Control the cost of queries.
- **The limits:** Choose two methods.
- **What they're really asking:** Which two ways reduce or cap BigQuery query spending?

**Clues in the question:**
- "**query costs … very high**": the cost is from **queries** (on-demand = pay per TB scanned), not storage.
- "**control costs**": either **cap** how much each user/project can scan (**custom quota**) or switch to a **fixed price** (**flat rate / slots**).
- Splitting or copying data doesn't reduce what queries scan, and copies add storage costs.

**Exam topic:** BigQuery / cost management.

---

## 📚 Key Terms Explained

### 1️⃣ On-demand pricing
- **What it is:** You pay **per TB of data each query scans**. A careless `SELECT *` on a huge table costs a lot.
- **Analogy:** 🚕 A **taxi meter**: the more you ride, the more you pay.

### 2️⃣ Custom query quota 🔑
- **What it is:** A **daily limit on how many bytes** queries may scan, set **per user** or **per project**. Once reached, more queries fail until the next day.
- **Looks like:** Console → IAM & Admin → Quotas → "BigQuery API: Query usage per day per user" = 1 TiB
- **Not to be confused with:** a billing budget (which only alerts).
- **Analogy:** 💳 A **daily spending limit** on each employee's company card.

### 3️⃣ Flat rate / slots (capacity pricing) 🔑
- **What it is:** You buy a fixed amount of **query capacity (slots)** for a fixed price, and assign it to projects. Queries no longer cost per byte.
- **Looks like:** a reservation of 500 slots → assigned to `finance-project` (200), `marketing-project` (300)
- **Not to be confused with:** on-demand. Costs become **predictable**.
- **Analogy:** 🚌 A **monthly bus pass**: ride as much as you want for one fixed price.

### 4️⃣ Copying / splitting the warehouse
- **What it is:** Making separate datasets or copies per team. Doesn't change how much queries scan; copies add storage costs and data gets out of sync.

### 🔗 How they fit together
```
 High query costs (on-demand, pay per TB)
   ├── B: custom quota → cap TB/day per user or project ✅
   └── E: flat rate     → fixed price, slots per project ✅
   (A, C, D: move or copy data → same scans, more cost/admin ❌)
```

---

## 🌍 Real-World Scenario

The finance team sees a $40,000 BigQuery bill, mostly from analysts running large ad-hoc queries. The engineer sets a **custom daily quota per user** so no one can scan more than 2 TiB a day, and moves heavy teams to **capacity pricing** with a fixed number of slots, making the monthly cost predictable.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Split the users from business units to multiple projects.

**Wrong words:**
- ❌ "**Split the users … to multiple projects**": moving users around doesn't limit how much they query. It only changes which project gets the bill.

📌 **When to use it:** Use separate projects when you want each team's costs **shown** separately on the bill.
🏢 **Office example:** Giving each department its own taxi account. They still ride as much as before.

### ✅ B
> **B.** Apply a user- or project-level custom query quota for BigQuery data warehouse.

**Why it's correct:**
- ✔️ "**custom query quota**" matches "**query costs for BigQuery are very high … control costs**": it caps how many bytes queries can scan per day, which caps the cost.
- ✔️ "**user- or project-level**" matches "**Users from multiple business units**": you can set limits per user or per business unit project.

📌 **When to use it:** Use it when you want to stop any one person or team from overspending each day.
🏢 **Office example:** A daily spending limit on each employee's company card.

### ❌ C
> **C.** Create separate copies of your BigQuery data warehouse for each business unit.

**Wrong words:**
- ❌ "**Create separate copies**": you pay storage for every copy, the copies get out of sync, and queries still scan the same amount.

📌 **When to use it:** **Never use this** to save money. Use B or E.
🏢 **Office example:** Photocopying the whole archive for every department. More paper, same reading.

### ❌ D
> **D.** Split your BigQuery data warehouse into multiple data warehouses for each business unit.

**Wrong words:**
- ❌ "**Split your BigQuery data warehouse into multiple data warehouses**": a big, messy redesign that doesn't limit query spending.

📌 **When to use it:** Use it when teams truly need separate data for security or legal reasons.
🏢 **Office example:** Splitting the central archive into many small archives. Everyone still reads as much.

### ✅ E
> **E.** Change your BigQuery query model from on-demand to flat rate. Apply the appropriate number of slots to each Project.

**Why it's correct:**
- ✔️ "**from on-demand to flat rate**" matches "**query costs … very high, and you need to control costs**": you pay a fixed price instead of per byte scanned.
- ✔️ "**Apply the appropriate number of slots to each Project**" matches "**multiple business units**": each unit's project gets its own share of capacity.

📌 **When to use it:** Use it when usage is heavy and steady, and you want a fixed, predictable bill.
🏢 **Office example:** Buying monthly bus passes for staff instead of paying for every taxi ride.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's analytics bill jumps after marketing runs `SELECT *` on the 20 TB `events` table every hour.
- **B:** Quota "Query usage per day per user" = 1 TiB for marketing analysts.
- **E:** Buy a 300-slot reservation and assign 100 slots to `shopnow-marketing`, 200 to `shopnow-finance`. Monthly cost is now fixed.

---

## 🧠 Key Takeaways / Memory Tips

- **Control BigQuery query costs → custom query quotas (cap) + flat rate / capacity slots (fixed price).**
- Copying or splitting data doesn't lower query costs.
  🧠 *"**Cap it (quota) or fix it (flat rate).**"*
- Related: **Q088** (budget alerts), **Q085** (external tables), **Q093** (Data Catalog).

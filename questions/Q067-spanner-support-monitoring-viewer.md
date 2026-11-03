# Q067: Support Team Can Monitor Spanner but Not Read Table Data (Monitoring Viewer)

**Topic:** IAM (roles/monitoring.viewer vs Spanner data roles vs stackdriver.accounts.viewer; groups; least privilege)

## ❓ Question
> You built an application on Google Cloud that uses Cloud Spanner. Your support team needs to monitor the environment but should not have access to table data. You need a streamlined solution to grant the correct permissions to your support team, and you want to follow Google-recommended practices. What should you do?
>
> **A.** Add the support team group to the roles/monitoring.viewer role
>
> **B.** Add the support team group to the roles/spanner.databaseUser role.
>
> **C.** Add the support team group to the roles/spanner.databaseReader role.
>
> **D.** Add the support team group to the roles/stackdriver.accounts.viewer role.

**My answer:** C
**Correct answer:** A
**Result:** ❌ Incorrect

> Why C was tempting: "Reader" sounds harmless, like "read-only access for watching". But **databaseReader reads the table data itself** (it can run SELECT queries), which is exactly what the question forbids. **Monitoring** means looking at **charts and metrics** (CPU, latency, storage), not the rows in the tables.

---

## 📖 What the Question Is Asking

**In plain words:** The support team must **watch how Spanner is doing** (is it busy? slow? full?), but must **never see the customer data** inside the tables. Which single role gives them exactly that?

**Clues in the question:**
- "**monitor the environment**": they need to see **metrics, charts and dashboards** in Cloud Monitoring.
- "**should not have access to table data**": no Spanner **data** roles (databaseReader, databaseUser).
- "**support team group**": grant the role to the **group**, not to each person (all options do this).
- "**streamlined**" + "**Google-recommended practices**": one **predefined** role with the **least privilege** that does the job.

**Exam topic:** IAM / Cloud Monitoring.

---

## 📚 Key Terms Explained

### 1️⃣ Monitoring (metrics) vs table data 🔑
- **What it is:** **Metrics** are numbers **about** the database: CPU use, number of requests, latency, storage used. **Table data** is the **content inside** the database: customer names, orders, card details.
- **Looks like:**
  - Metric: `spanner.googleapis.com/instance/cpu/utilization = 42%`
  - Table data: `SELECT name, email FROM customers` → `Ana, ana@mail.com`
- **Not to be confused with:** each other. You can watch every metric without ever seeing one row of data.
- **Analogy:** 🌡️ The **building's dashboard** (temperature, power use, elevator traffic) vs **the files inside the cabinets**.
- **In the online store:** Support sees "checkout DB CPU at 90%" but never sees a shopper's address.

### 2️⃣ roles/monitoring.viewer 🔑
- **What it is:** A predefined IAM role that gives **read-only access to Cloud Monitoring**: metrics, dashboards, charts, alerting policies, uptime checks. It does **not** give access to any service's data.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-prod --member=group:support@shopnow.com --role=roles/monitoring.viewer`
- **Not to be confused with:** monitoring.editor/admin (can change dashboards and alerts) or any Spanner role.
- **Analogy:** 📺 A pass to the **security room with the dashboard screens**, but no key to any filing cabinet.
- **In the online store:** Support watches the Spanner dashboard during Black Friday.

### 3️⃣ roles/spanner.databaseReader
- **What it is:** A Spanner role that can **read data**: run SELECT queries and read the schema.
- **Looks like:** `SELECT * FROM orders` ✅ works
- **Not to be confused with:** a monitoring role. "Reader" here means **reading the rows**.
- **Analogy:** 🗂️ A key that **opens the filing cabinet** to read files (but not change them).

### 4️⃣ roles/spanner.databaseUser (review from Q038)
- **What it is:** A Spanner role that can **read and write data** (SELECT, INSERT, UPDATE, DELETE) and update the schema.
- **Looks like:** `INSERT INTO orders ...` ✅ works
- **Not to be confused with:** databaseReader (read only). User can also **change** data.
- **Analogy:** 🗂️✏️ A key that opens the cabinet **and lets you edit the files**.

### 5️⃣ roles/stackdriver.accounts.viewer
- **What it is:** An old Stackdriver role that only lets you **see the account setup** (which projects are linked to the Stackdriver Workspace). It does **not** let you see metrics or dashboards.
- **Looks like:** viewing "Workspace shopnow-monitoring monitors projects: shopnow-prod, shopnow-dev"
- **Not to be confused with:** monitoring.viewer. Same old "Stackdriver" name, but this one shows **the setup**, not **the charts**.
- **Analogy:** 📋 Seeing the **list of which buildings the security company watches**, but not the cameras.

### 6️⃣ Google group (review from Q025)
- **What it is:** A named **list of email addresses**. Giving a role to the group gives it to everyone on the list.
- **Looks like:** `support@shopnow.com = [li@shopnow.com, sam@shopnow.com, kai@shopnow.com]`
- **Not to be confused with:** a shared login. Each person signs in with their own account.
- **Analogy:** 📇 The "Support Team" list at the front desk.

### 🔗 How they fit together
```
 support@shopnow.com (group)
        │
        ├── roles/monitoring.viewer       → 📺 Spanner CPU, latency, storage charts ✅
        │                                    🚫 no table rows
        ├── roles/spanner.databaseReader  → 🗂️ SELECT * FROM customers ❌ (sees data)
        ├── roles/spanner.databaseUser    → 🗂️✏️ read AND write data ❌❌
        └── roles/stackdriver.accounts.viewer → 📋 workspace setup only, no charts ❌
```

---

## 🌍 Real-World Scenario

Support and on-call teams need to answer "is the database healthy?" at 3 AM: CPU spikes, slow queries, storage filling up. But privacy rules (and laws like GDPR or PCI) say they must not see customer data. The standard fix: put them in a **group** and give that group **Monitoring Viewer**. They see every chart and alert, and the Spanner tables stay closed to them.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Add the support team group to the roles/monitoring.viewer role

**Why it's correct:**
- ✔️ "**roles/monitoring.viewer**" matches "**monitor the environment**": it shows all Cloud Monitoring metrics and dashboards, including Spanner's CPU, latency and storage.
- ✔️ "**roles/monitoring.viewer**" matches "**should not have access to table data**": it has no Spanner data permissions at all, so no rows can be read.
- ✔️ "**Add the support team group**" matches "**streamlined**": one grant to one group covers the whole team, and new members just join the group.
- ✔️ A single **predefined, read-only** role matches "**Google-recommended practices**": least privilege, nothing custom to maintain.

📌 **When to use it:** Use it when a team needs to watch how systems are doing but must not see or change any data.
🏢 **Office example:** Giving the night guard a pass to the room with the dashboard screens, but no key to any filing cabinet.

### ❌ B
> **B.** Add the support team group to the roles/spanner.databaseUser role.

**Wrong words:**
- ✔️ "Add the support team group" is the right way to grant access.
- ❌ "**roles/spanner.databaseUser**": this can **read AND write** table data. It breaks "should not have access to table data" even more than C, and it doesn't give monitoring dashboards.

📌 **When to use it:** Use it for the application's service account or developers who must read and change data in the database.
🏢 **Office example:** The records clerk who has the key to the cabinet and can edit the files.

### ❌ C (your answer)
> **C.** Add the support team group to the roles/spanner.databaseReader role.

**Wrong words:**
- ✔️ "Add the support team group" is the right way to grant access.
- ❌ "**roles/spanner.databaseReader**": "Reader" means it **reads the table data** (runs SELECT queries). That's exactly what "**should not have access to table data**" forbids. It's also not a monitoring role, so it doesn't give access to the Cloud Monitoring dashboards.

📌 **When to use it:** Use it for analysts or reporting tools that must read the data but never change it.
🏢 **Office example:** An auditor who may open the cabinet and read the files, but not write in them.

### ❌ D
> **D.** Add the support team group to the roles/stackdriver.accounts.viewer role.

**Wrong words:**
- ✔️ "Add the support team group" is the right way to grant access.
- ❌ "**roles/stackdriver.accounts.viewer**": it only shows **which projects are linked** to the Stackdriver Workspace, not the metrics or dashboards. The support team still couldn't monitor anything.

📌 **When to use it:** Use it when someone only needs to see how the monitoring workspace is set up, not the charts.
🏢 **Office example:** Seeing the list of which buildings the security company watches, without seeing any camera.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow stores orders and customers in Spanner. The support team (`support@shopnow.com`) does on-call.

```bash
gcloud projects add-iam-policy-binding shopnow-prod \
  --member=group:support@shopnow.com --role=roles/monitoring.viewer
```

What support can do now:
- ✅ Open the Spanner dashboard: CPU 85%, p99 latency 40 ms, storage 2.1 TB.
- ✅ See which alerts fired overnight.
- 🚫 `gcloud spanner databases execute-sql orders-db --sql="SELECT * FROM customers"` → **permission denied**.

When Kai joins support, the admin adds Kai to `support@shopnow.com`. No IAM change needed.

---

## 🧠 Key Takeaways / Memory Tips

- **"Monitor" but "no access to data" → roles/monitoring.viewer.**
- **Spanner databaseReader = reads rows. databaseUser = reads and writes rows.** Neither is for monitoring.
- **stackdriver.accounts.viewer = sees the workspace setup, not the charts.**
- Always grant roles to a **group**, not to individual people.
  🧠 *"**Watch the dashboard, don't open the cabinet.**"*
- Related: **Q025** (auditors group + predefined roles), **Q032** (monitoring many projects), **Q038** (Spanner databaseUser).

# Q090: Archiving Old Object Versions Read Monthly (Lifecycle Rule → Nearline)

**Topic:** Cloud Storage (object versioning, lifecycle rules, Nearline vs Coldline)

## ❓ Question
> You want to configure a solution for archiving data in a Cloud Storage bucket. The solution must be cost-effective. Data with multiple versions should be archived after 30 days. Previous versions are accessed once a month for reporting. This archive data is also occasionally updated at month-end. What should you do?
>
> **A.** Add a bucket lifecycle rule that archives data with newer versions after 30 days to Coldline Storage.
>
> **B.** Add a bucket lifecycle rule that archives data with newer versions after 30 days to Nearline Storage.
>
> **C.** Add a bucket lifecycle rule that archives data from regional storage after 30 days to Coldline Storage.
>
> **D.** Add a bucket lifecycle rule that archives data from regional storage after 30 days to Nearline Storage.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Data in a bucket has several versions (versioning keeps older copies of each file).
- **What you must achieve:** Archive older versions after 30 days.
- **The limits:** Keep it cost-effective; older versions are read once a month for reports and sometimes updated at month-end.
- **What they're really asking:** Which storage class and lifecycle rule fit this access pattern?

**Clues in the question:**
- "**Data with multiple versions**": the rule should target **older versions** (objects that have **newer versions**), not "everything in regional storage".
- "**accessed once a month**": once a month = **Nearline** (built for about monthly access, 30-day minimum).
- "**occasionally updated at month-end**": Coldline has a **90-day minimum** and higher read costs, so monthly use makes it more expensive.
- "**cost-effective**": the cheapest class **for this access pattern**, which is Nearline.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1️⃣ Object versioning
- **What it is:** A **bucket setting that keeps old copies** of a file when it's overwritten or deleted. The newest copy is **live**; older copies are **noncurrent** ("data with newer versions").
- **Looks like:** `report.csv#1700000001` (old), `report.csv#1700000099` (live)
- **Not to be confused with:** backups to another bucket.
- **Analogy:** 📑 Keeping **every earlier draft** of a document in the folder.

### 2️⃣ Lifecycle rule 🔑
- **What it is:** A **bucket rule that automatically changes the storage class of objects, or deletes them**, when conditions are met (age, is it noncurrent, etc.).
- **Looks like:**
  ```json
  {"rule": [{"action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
             "condition": {"age": 30, "isLive": false}}]}
  ```
- **Not to be confused with:** a manual move. It runs by itself.
- **Analogy:** 🗄️ An office policy: "**drafts older than 30 days go to the monthly-records cabinet**."

### 3️⃣ Nearline vs Coldline (review from Q006)
- **Nearline:** for data opened **about once a month**. Minimum storage **30 days**. Cheap storage, small read fee.
- **Coldline:** for data opened **about once a quarter**. Minimum storage **90 days**. Cheaper storage, but higher read fees.
- **Not to be confused with:** each other. Monthly → Nearline. Quarterly → Coldline.
- **Analogy:** 📁 Nearline = the **month-end accounting cabinet**. 🧊 Coldline = the **storage room opened for audits**.

### 4️⃣ Regional storage
- **What it is:** The bucket's **location type** (one region). It's not a version state, so a rule "from regional storage" would move **all** objects, including live ones.

### 🔗 How they fit together
```
 bucket (versioning ON)
   report.csv  live      → stays Standard
   report.csv  older ver → after 30 days → lifecycle → NEARLINE ✅ (read monthly)
                                                      COLDLINE ❌ (monthly reads cost more)
```

---

## 🌍 Real-World Scenario

A finance team overwrites its reports every day, with versioning on. Old versions pile up and cost money in Standard storage. They're opened once a month for reporting. The engineer adds a lifecycle rule: **noncurrent versions older than 30 days → Nearline**. Costs drop, and monthly reads stay cheap.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add a bucket lifecycle rule that archives data with newer versions after 30 days to Coldline Storage.

**Wrong words:**
- ✔️ "archives data with newer versions after 30 days" is the right target.
- ❌ "**to Coldline Storage**": Coldline is for about once-a-**quarter** access. Reading and updating monthly means higher access fees and early-deletion charges (90-day minimum). Not cost-effective here.

📌 **When to use it:** Use Coldline when old versions are opened only a few times a year.
🏢 **Office example:** Old records in the storage room, opened only when auditors come.

### ✅ B
> **B.** Add a bucket lifecycle rule that archives data with newer versions after 30 days to Nearline Storage.

**Why it's correct:**
- ✔️ "**archives data with newer versions**" matches "**Data with multiple versions should be archived**": the rule only moves older versions, not the live files.
- ✔️ "**after 30 days**" matches "**archived after 30 days**": the exact timing.
- ✔️ "**to Nearline Storage**" matches "**accessed once a month**" + "**updated at month-end**": Nearline is built for monthly access, with a 30-day minimum.
- ✔️ "**Nearline**" matches "**cost-effective**": cheaper storage than Standard, with low fees for monthly reads.

📌 **When to use it:** Use it when old copies are opened about once a month.
🏢 **Office example:** Last month's drafts go to the accounting cabinet that's opened at every month-end close.

### ❌ C
> **C.** Add a bucket lifecycle rule that archives data from regional storage after 30 days to Coldline Storage.

**Wrong words:**
- ❌ "**from regional storage**": this targets **all** objects, including the live versions, not just the older versions.
- ❌ "**to Coldline Storage**": wrong class for monthly access (see A).

📌 **When to use it:** Use it when **all** files older than 30 days are rarely opened, a few times a year.
🏢 **Office example:** Moving every file, even today's working copies, to the storage room after a month.

### ❌ D
> **D.** Add a bucket lifecycle rule that archives data from regional storage after 30 days to Nearline Storage.

**Wrong words:**
- ✔️ "to Nearline Storage" is the right class.
- ❌ "**from regional storage**": it moves **all** objects older than 30 days, not just the older versions the question talks about.

📌 **When to use it:** Use it when every file older than 30 days is opened about once a month, with or without versions.
🏢 **Office example:** Moving all files, not just old drafts, to the month-end cabinet.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `shopnow-reports` bucket has versioning on. The sales report `daily-sales.csv` is overwritten every night, and finance reads old versions at month-end.

```bash
cat > lifecycle.json <<'EOF'
{"rule": [{"action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
           "condition": {"daysSinceNoncurrentTime": 30, "isLive": false}}]}
EOF
gsutil lifecycle set lifecycle.json gs://shopnow-reports
```
The live `daily-sales.csv` stays in Standard. Versions older than 30 days move to Nearline, and month-end reads cost a little each time.

---

## 🧠 Key Takeaways / Memory Tips

- **Once a month → Nearline** (30-day min). **Once a quarter → Coldline** (90-day min). **Once a year → Archive.**
- "**Data with newer versions**" = noncurrent versions. A rule "from regional storage" hits **all** objects.
- Cheapest storage isn't cheapest overall if you read it often.
  🧠 *"**Monthly? Nearline. Versions? Target the noncurrent ones.**"*
- Related: **Q006** (storage classes), **Q061** (Coldline for audit logs).

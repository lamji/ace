# Q027: Checking Who Viewed Files and Changed Labels (Data Access Logs in Cloud Logging)

**Topic:** Cloud Logging / Audit logs (Data Access vs Admin Activity logs, Console Activity page, Logs Explorer filters, Cloud Trace)

## ❓ Question
> You have sensitive data stored in three Cloud Storage buckets and have enabled data access logging. You want to verify activities for a particular user for these buckets, using the fewest possible steps. You need to verify the addition of metadata labels and which files have been viewed from those buckets. What should you do?
>
> **A.** Using the GCP Console, filter the Activity log to view the information.
>
> **B.** Using the GCP Console, filter the Stackdriver log to view the information.
>
> **C.** View the bucket in the Storage section of the GCP Console.
>
> **D.** Create a trace in Stackdriver to view the information.

**My answer:** A
**Correct answer:** B
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** You turned on **data access logging** for 3 sensitive buckets. Now you want to see what **one specific person** did: **which files they opened** and **which metadata labels they added**. Where do you look, with the fewest steps?

| Keyword | What it hints at |
|---|---|
| "**have enabled data access logging**" | The records you need are **Data Access audit logs**, which live in **Cloud Logging** (formerly Stackdriver Logging) |
| "**which files have been viewed**" | Reading data = a **Data Access** log entry. Only Cloud Logging shows these |
| "**a particular user**" + "**three buckets**" | You need to **filter** by user email and by bucket, which Logs Explorer does in one query |
| "**fewest possible steps**" | One filtered query in Logs Explorer, not opening each bucket or building something new |

**Exam topic:** Cloud Logging / Cloud Audit Logs.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Audit Logs: Admin Activity vs Data Access 🔑
- **What it is:** Google Cloud's automatic records of **"who did what, where, and when"**. There are two main kinds:
  | | **Admin Activity logs** | **Data Access logs** |
  |---|---|---|
  | Records | **Changes to settings/config** (create a bucket, change IAM, change bucket settings) | **Reading data** (view/download a file) and **writing data** (upload a file, change an object's metadata) |
  | On by default? | ✅ Always on | ❌ Mostly **off**; you turn them on (this question says it's on) |
  | Where to see them | Cloud Logging (and the Console's Activity page) | **Only in Cloud Logging** |
- **Looks like (one Data Access entry):**
  ```
  principalEmail: ana@shopnow.com
  methodName:     storage.objects.get
  resourceName:   projects/_/buckets/shopnow-invoices/objects/2026/inv-1043.pdf
  timestamp:      2026-10-22T09:14:03Z
  ```
- **Not to be confused with:** your app's own logs (like "order 1043 created"). Audit logs are written **by Google** about **API calls**.
- **Analogy:** 🎥 Admin Activity = the **renovation logbook** (who moved walls, changed locks). Data Access = the **records-room sign-out sheet** (who opened which file).
- **In the online store:** Data Access logs show which employee opened which customer invoice PDF.

### 2️⃣ Cloud Logging / Logs Explorer (formerly "Stackdriver Logging")
- **What it is:** Google Cloud's service that **stores and searches all logs**, including **audit logs**. **Logs Explorer** is its search page in the Console, where you **filter** by user, resource, method and time.
- **Looks like (a filter):**
  ```
  protoPayload.authenticationInfo.principalEmail="ana@shopnow.com"
  resource.type="gcs_bucket"
  resource.labels.bucket_name=("shopnow-invoices" OR "shopnow-payroll" OR "shopnow-contracts")
  ```
- **Not to be confused with:** the Console's **Activity** page. "Stackdriver" is just the **old brand name** for Google's monitoring and logging tools (now Cloud Logging, Cloud Monitoring, Cloud Trace).
- **Analogy:** 🔎 The **security office's searchable archive** of every camera recording and sign-in sheet.
- **In the online store:** The security team searches "everything Ana did in the invoice bucket last week".

### 3️⃣ The Console "Activity" page (Activity log / Activity stream)
- **What it is:** A **simple summary page** on the project dashboard showing recent **Admin Activity** events (who created or changed resources). It has only **basic filters**.
- **Looks like:** "Ben created bucket shopnow-invoices · 2 hours ago"
- **Not to be confused with:** Cloud Logging. The Activity page **doesn't show Data Access logs**, so **"who viewed which file" never appears there**.
- **Analogy:** 📰 The **building's notice board** listing recent renovations. It never lists who read which file.

### 4️⃣ Metadata Labels
- **What it is:** **Key-value tags** attached to an object or bucket to describe it.
- **Looks like:** `confidential=true`, `team=finance`
- **Not to be confused with:** the file's **content**. Labels describe the file. They aren't inside it.
- **Analogy:** 🏷️ **Sticky labels** on a folder: "CONFIDENTIAL · Finance".
- **In the online store:** Ana tags invoice PDFs with `confidential=true`.

### 5️⃣ Cloud Trace (formerly "Stackdriver Trace")
- **What it is:** A tool that measures **how long each step of a request takes** inside your app (speed/latency), to find slow parts.
- **Looks like:** `GET /checkout 820 ms → payment-api 600 ms → db query 150 ms`
- **Not to be confused with:** logs. Trace shows **speed**, not **who did what**.
- **Analogy:** ⏱️ A **stopwatch** on each step of the mail delivery route.
- **In the online store:** Finds out why checkout is slow.

### 🔗 How They Fit Together
```
👩 Ana opens inv-1043.pdf and adds the label confidential=true
           │
           ▼
📜 Cloud Audit Logs (written automatically by Google)
   ├── Admin Activity (config changes)  ──► shown in Logs Explorer ✅ and Console Activity page
   └── Data Access (read/write data)    ──► shown ONLY in Logs Explorer ✅
                                            (needs to be enabled; it is here)
           │
           ▼
🔎 Logs Explorer: filter by user = ana@… AND the 3 buckets → one list with everything ✅

❌ Activity page → no Data Access logs → can't see "viewed files"
❌ Storage page  → shows files and labels now, not who did what
❌ Cloud Trace   → measures speed, not user actions
```

---

## 🌍 Real-World Scenario

Security gets an alert: *"An employee may have looked at payroll files they shouldn't have."* Compliance needs **proof**: exactly **which files** that person opened and **what they changed**, across all the sensitive buckets. A security or cloud engineer opens **Logs Explorer**, filters by the **employee's email** and the **sensitive buckets**, and exports the result for the investigation.

This only works because **Data Access logging was enabled in advance**. It isn't on by default for most services.

---

## 🔍 Option-by-Option Breakdown

### ❌ A (your answer)
> **A.** Using the GCP Console, filter the Activity log to view the information.

**Why it's wrong:**
- ❌ The Console **Activity** page shows **Admin Activity** events only. It **doesn't show Data Access logs**, so **"which files have been viewed" won't be there**.
- ❌ Its filters are basic. It's a summary page, not a search tool.
- 💡 **Likely mix-up:** "Activity log" *sounds* like "a log of all activity". In Google Cloud it means **admin/config activity** only.

**📌 When to use it:** Use it for a quick look at recent changes to the project, like who created or deleted something.
🏢 **Office example:** Checking the building notice board to see which offices were renovated this week.

### ✅ B
> **B.** Using the GCP Console, filter the Stackdriver log to view the information.

**Why it's correct:**
- ✔️ "Stackdriver log" = **Cloud Logging (Logs Explorer)**, where **both Admin Activity and Data Access** audit logs live.
- ✔️ **One filter** (user email + the 3 buckets) shows **file views** (`storage.objects.get`) and **label changes** together.
- ✔️ Fewest steps: one page, one query.

**📌 When to use it:** Use it when you need to find out exactly who did what, when, across many places.
🏢 **Office example:** The security office searching all sign-out sheets for one employee's name to see every file they took out.

### ❌ C
> **C.** View the bucket in the Storage section of the GCP Console.

**Why it's wrong:**
- ❌ The Storage page shows **what's in the bucket right now** (files, labels, settings). It **doesn't show who viewed or changed** anything.
- ❌ You'd also have to open **3 buckets** one by one.

**📌 When to use it:** Use it when you want to see or manage the files and settings in a bucket today.
🏢 **Office example:** Walking into the records room to see which folders are on the shelf. That doesn't tell you who read them.

### ❌ D
> **D.** Create a trace in Stackdriver to view the information.

**Why it's wrong:**
- ❌ **Cloud Trace** measures **how fast requests are**. It doesn't record **who opened which file**.
- ❌ "Create" something new = extra steps.

**📌 When to use it:** Use Trace when your app is slow and you need to find which step takes the most time.
🏢 **Office example:** Timing each step of the mail delivery route to find where letters get delayed.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow keeps sensitive files in 3 buckets: `shopnow-invoices`, `shopnow-payroll`, `shopnow-contracts`. **Data Access logs for Cloud Storage** were turned on earlier (IAM & Admin → **Audit Logs** → Cloud Storage → ✅ Data Read, ✅ Data Write).

HR reports: *"Ana from support may have opened payroll files."*

**In the Console → Logging → Logs Explorer, one query:**
```
protoPayload.authenticationInfo.principalEmail="ana@shopnow.com"
resource.type="gcs_bucket"
resource.labels.bucket_name=("shopnow-invoices" OR "shopnow-payroll" OR "shopnow-contracts")
```
**Results:**
| Time | Method | Object | Meaning |
|---|---|---|---|
| 09:14 | `storage.objects.get` | `shopnow-payroll/2026-09/salaries.xlsx` | 👀 Ana **viewed** the payroll file |
| 09:16 | `storage.objects.update` | `shopnow-invoices/inv-1043.pdf` | 🏷️ Ana **added a metadata label** |

Same search with the CLI:
```bash
gcloud logging read \
  'protoPayload.authenticationInfo.principalEmail="ana@shopnow.com" AND resource.type="gcs_bucket"' \
  --freshness=7d --format="table(timestamp, protoPayload.methodName, protoPayload.resourceName)"
```

**🎬 With option A:** The Activity page shows "Ben created bucket shopnow-payroll" but **nothing about Ana viewing salaries.xlsx**. The investigation stalls. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Who viewed / read which data" → Data Access audit logs → Cloud Logging (Logs Explorer).**
- **Activity page = Admin Activity only.** It never shows who read data.
  🧠 *"**Activity** = who **changed** things. **Logging** = **everything**, including who **read** things."*
- **"Stackdriver" on old exam questions = today's Cloud Logging / Monitoring / Trace.**
  - Stackdriver **log** → Cloud Logging (who did what) ✅
  - Stackdriver **trace** → Cloud Trace (how fast) ❌ for audits
- **Data Access logs are mostly off by default.** Turn them on **before** you need them.
- Related: **Q025** (auditors get `logging.viewer` to read these logs; Data Access logs need `logging.privateLogViewer`).

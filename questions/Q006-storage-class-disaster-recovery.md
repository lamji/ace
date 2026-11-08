# Q006: Cloud Storage Class for Disaster Recovery Backups

**Topic:** Cloud Storage (storage classes: Standard / Nearline / Coldline / Archive, location types)

## ❓ Question
> Your company uses Cloud Storage to store application backup files for disaster recovery purposes. You want to follow Google's recommended practices. Which storage option should you use?
>
> **A.** Multi-Regional Storage
>
> **B.** Regional Storage
>
> **C.** Nearline Storage
>
> **D.** Coldline Storage

**My answer:** D
**Correct answer:** D
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company keeps backup copies of application files in Cloud Storage (Google's file storage), only so it can restore them if a disaster happens.
- **What you must achieve:** Choose the storage class (price tier) for these backup files.
- **The limits:** Follow Google's recommended practice for disaster-recovery backups.
- **What they're really asking:** Which Cloud Storage class does Google recommend for backup files kept for disaster recovery?

| Keyword | What it hints at |
|---|---|
| "**backup files**" | Data written often, but **rarely read** |
| "**disaster recovery**" | Only accessed in emergencies (maybe once a quarter or less) |
| "**Google's recommended practices**" | Google's docs name **Coldline** for backup / disaster recovery (Archive too, but it isn't an option here) |
| "**storage option**" | Choose a **storage class** |

**Exam topic:** Cloud Storage, specifically **choosing a storage class by access frequency**.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Storage
- **What it is:** Google's **object storage** service for storing **files** of any size (images, videos, backups, logs). It's not a database and not a disk attached to a VM.
- **Analogy:** 🗄️ A **giant online warehouse** where you store boxes (files) and get each one back by its label.
- **In the online store:** Product images, invoice PDFs, and database backups.

### 2️⃣ Bucket and Object
- **Bucket:** A **container** for files, with a globally unique name (e.g., `gs://shopnow-dr-backups`). You choose its **location** and **default storage class**.
- **Object:** A single **file** inside a bucket (e.g., `orders-2026-10-17.sql.gz`).
- **Analogy:** 📦 Bucket = a **storage room**. Objects = the **boxes** inside.
- **In the online store:** `gs://shopnow-product-images` (bucket) holds `red-shoes.jpg` (object).

### 3️⃣ Backup and Disaster Recovery (DR)
- **Backup:** A **copy** of your data kept somewhere safe.
- **Disaster recovery:** The plan for **restoring your system** after something terrible happens (data deleted, database corrupted, ransomware, region outage).
- **Analogy:** 🧯 A **fire extinguisher**. You hope you never use it, but it must be there and work when needed.
- **In the online store:** Nightly copies of the orders database, kept in case the live database is destroyed.

### 4️⃣ Storage Classes (the key concept)
Every object has a **storage class**. Rule of thumb: **the less often you read data, the cheaper it is to store, but the more it costs to read**.

| Class | Access pattern | Min. storage duration | Storage cost | Retrieval cost | Typical use |
|---|---|---|---|---|---|
| **Standard** | Frequently ("hot") | None | 💰💰💰💰 Highest | Free | Website images, active app data |
| **Nearline** | ≤ **once a month** | 30 days | 💰💰💰 | Low fee | Monthly reports, recent backups you might check |
| **Coldline** | ≤ **once a quarter** (90 days) | 90 days | 💰💰 | Higher fee | **Backups, disaster recovery** ✅ |
| **Archive** | < **once a year** | 365 days | 💰 Lowest | Highest fee | Legal/compliance archives, long-term DR |

*Approx. US region storage prices: Standard ~$0.020, Nearline ~$0.010, Coldline ~$0.004, Archive ~$0.0012 per GB per month. Prices change; check the pricing page.*

- **Minimum storage duration:** If you delete an object early, you're still charged for the minimum (e.g., delete a Coldline file after 10 days → charged for 90).
- **Retrieval fee:** A charge per GB when you **read** data from Nearline, Coldline, or Archive.
- ⚡ **GCP fact:** All classes return data in **milliseconds**. "Cold" means cheaper storage and pricier reads, **not** slower access (unlike AWS Glacier, where you wait hours).
- **Analogy:** 🏠 Standard = **your bedroom closet** (grab anytime, expensive space). Nearline = **the garage**. Coldline = **a storage unit across town** (cheap rent, small fee each visit). Archive = **a vault in the countryside**.

### 5️⃣ Location Types (Region / Dual-region / Multi-region)
- **What it is:** **Where** your bucket's data physically lives. This is a **separate choice** from the storage class:
  - **Region:** One location (e.g., `asia-southeast1`, Singapore).
  - **Dual-region:** Two specific regions.
  - **Multi-region:** A large area with several regions (e.g., `asia`, `us`, `eu`).
- **Analogy:** 📍 Location = **which city** your storage unit is in. Storage class = **what kind of unit** (closet, garage, cold storage).
- **In the online store:** DR backups can be **Coldline + multi-region `asia`**, so they're cheap **and** survive a single-region outage.

### 6️⃣ Legacy "Multi-Regional" and "Regional" Storage Classes
- **What it is:** Older Cloud Storage **storage classes**. Today Google has replaced them: they're now simply **Standard** storage in a **multi-region** or **region** location. That's why old exam questions list them next to Nearline and Coldline.
- Both are designed for **frequently accessed (hot)** data, which is the opposite of backups.

### 7️⃣ Object Lifecycle Management
- **What it is:** Rules that **automatically change an object's storage class or delete it** based on age or other conditions.
- **Analogy:** 🧹 An **automatic cleaner** that moves old boxes to the cheaper vault and throws out very old ones.
- **In the online store:** "Move backups older than 365 days to Archive, delete after 7 years."

### 🔗 How They Fit Together
```
🗄️ Cloud Storage
└── 📦 Bucket: gs://shopnow-dr-backups
      ├── 📍 Location:  asia (multi-region)  ← WHERE data lives
      ├── 🧊 Default storage class: COLDLINE  ← HOW OFTEN you read it (≤ 1×/quarter)
      ├── 🧹 Lifecycle: age > 365 days → ARCHIVE; age > 2555 days → DELETE
      └── 📄 Objects:
            orders-2026-10-15.sql.gz
            orders-2026-10-16.sql.gz
            orders-2026-10-17.sql.gz
```

---

## 🌍 Real-World Scenario

Every company needs backups. They're created **every day** but **read almost never**, only during a disaster or a yearly DR drill. Storing terabytes of backups in **Standard** class means paying premium "hot storage" prices for data nobody touches. Choosing **Coldline** cuts storage cost by roughly **80%** compared with Standard. You pay a retrieval fee only on the rare day you actually restore.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Multi-Regional Storage

**Why it's wrong:**
- ❌ Multi-Regional (now **Standard** in a multi-region) is designed for **frequently accessed** data served worldwide, like website content and streaming video.
- ❌ It's the **most expensive** option for data you almost never read.
- ⚠️ **Trap option:** "multi-regional" *sounds* good for disaster recovery (data in multiple places). But the question asks which **storage option** Google recommends for backups, and that's about **access frequency**. (In practice you can combine Coldline **with** a multi-region location.)

**📌 When to use it:** Use it when **many people in many countries open the file all the time**.
🏢 **Office example:** The company handbook on the intranet that employees in every country open every day.

### ❌ B
> **B.** Regional Storage

**Why it's wrong:**
- ❌ Regional (now **Standard** in a region) is for **frequently accessed** data used by compute in the same region (e.g., data processed by VMs or analytics jobs).
- ❌ You pay hot-storage prices for cold data, so it isn't cost-effective for backups.

**📌 When to use it:** Use it when **people in one office open the file all the time**.
🏢 **Office example:** The daily schedule that staff in the Manila office check all day long.

### ❌ C
> **C.** Nearline Storage

**Why it's wrong:**
- ✔️ Closer: it's designed for infrequent access, so it's cheaper than Standard.
- ❌ But Nearline is designed for data read about **once a month**. Disaster recovery backups are read **much less often** than that.
- ❌ Coldline is **cheaper to store** for this pattern, and Google specifically lists **backup / disaster recovery** as a Coldline use case.

**📌 When to use it:** Use it when **you open the file about once a month**.
🏢 **Office example:** The accounting files opened once a month for month-end closing.

### ✅ D
> **D.** Coldline Storage

**Why it's correct:**
- ✔️ Designed for data accessed **at most once a quarter**, which fits disaster recovery backups.
- ✔️ **Very low storage cost**, with retrieval fees paid only when you actually restore.
- ✔️ Data is still available **in milliseconds** when disaster strikes, with no waiting.
- ✔️ Google's documentation names **backup and disaster recovery** as a Coldline use case.

**📌 When to use it:** Use it when **the file is stored but almost never opened**, only for an audit or an emergency.
🏢 **Office example:** Old records in the storage room, opened only when auditors come.

---

## 🛒 E-Commerce Full-Stack Example

```
🗄️ Cloud SQL: shopnow-db (orders, customers)
        │  nightly export at 2:00 AM
        ▼
📦 gs://shopnow-dr-backups   (Coldline, multi-region: asia)
        │  read only if disaster strikes (or quarterly DR drill)
        ▼
⏪ Restore into a new Cloud SQL instance
```

ShopNow uses **different storage classes for different data**:

| Data | Bucket | Class | Why |
|---|---|---|---|
| 🖼️ Product images shown on the storefront | `shopnow-product-images` | **Standard** | Read thousands of times per minute |
| 📊 Monthly sales report CSVs | `shopnow-reports` | **Nearline** | Finance opens them about once a month |
| 💾 Nightly database backups for DR | `shopnow-dr-backups` | **Coldline** ✅ | Only read in an emergency or quarterly drill |
| 📜 7-year tax/invoice records | `shopnow-tax-archive` | **Archive** | Almost never read; kept for legal reasons |

**1. Create the DR backup bucket:**
```bash
gcloud storage buckets create gs://shopnow-dr-backups \
  --location=asia \
  --default-storage-class=COLDLINE
```

**2. Export the orders database to it every night (e.g., with Cloud Scheduler):**
```bash
gcloud sql export sql shopnow-db \
  gs://shopnow-dr-backups/orders-2026-10-17.sql.gz \
  --database=shop
```

**3. Add a lifecycle rule to move very old backups to Archive, then delete them:**
```json
{
  "rule": [
    { "action": { "type": "SetStorageClass", "storageClass": "ARCHIVE" },
      "condition": { "age": 365 } },
    { "action": { "type": "Delete" },
      "condition": { "age": 2555 } }
  ]
}
```
```bash
gcloud storage buckets update gs://shopnow-dr-backups --lifecycle-file=lifecycle.json
```

**💰 Why it matters:** ShopNow keeps about **5 TB** of backups. In Standard, that's roughly **5× the monthly storage bill** of Coldline, for files nobody opens. On the one day the database gets corrupted, the restore starts **immediately** (millisecond access), and paying a one-time retrieval fee is a small price.

---

## 🧠 Key Takeaways / Memory Tips

- **Backup / disaster recovery → Coldline** (Archive if accessed less than once a year and it's offered).
- **Remember the classes by access frequency:**
  🧠 *"Standard = **daily**, Nearline = **monthly** (30), Coldline = **quarterly** (90), Archive = **yearly** (365)." Think of the 4 seasons: **cold** comes once a **quarter**.*
  Minimum durations: **0 / 30 / 90 / 365 days**.
- **The colder the class, the cheaper to store and the pricier to read**, but always millisecond access.
- **"Multi-Regional" and "Regional" are legacy classes** for **hot** data (now Standard + location). Location (*where*) and class (*how often*) are **separate choices**.
- 🚩 Don't fall for "multi-regional = safer = DR." The question is about **access frequency and cost**.

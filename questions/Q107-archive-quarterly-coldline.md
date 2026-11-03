# Q107: Archive Data Read Once a Quarter (Coldline Storage)

**Topic:** Cloud Storage (storage classes: Nearline, Coldline, location types)

## ❓ Question
> You are building an archival solution for your data warehouse and have selected Cloud Storage to archive your data. Your users need to be able to access this archived data once a quarter for some regulatory requirements. You want to select a cost-efficient option. Which storage option should you use?
>
> **A.** Cold Storage
>
> **B.** Nearline Storage
>
> **C.** Regional Storage
>
> **D.** Multi-Regional Storage

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Archived data, read **once every 3 months**. Which storage class is cheapest?

**Clues in the question:**
- "**once a quarter**" → **Coldline** (built for about quarterly access, 90-day minimum). "Cold Storage" in option A means Coldline.
- "**cost-efficient**": cheaper than Nearline (monthly) for data read only quarterly.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Coldline 🔑
- **What it is:** A storage class for data read **about once a quarter**. Very cheap to store, a small fee to read, **90-day minimum**.
- **Looks like:** `gsutil mb -c coldline -l us-central1 gs://shopnow-warehouse-archive`
- **Not to be confused with:** Nearline (monthly) or Archive (yearly).
- **Analogy:** 🧊 The **storage room** opened for quarterly audits.
- **In the online store:** Old warehouse exports for quarterly compliance checks.

### 2. Nearline
- **What it is:** For data read **about once a month**, 30-day minimum.
- **Looks like:** `-c nearline`
- **Not to be confused with:** Coldline.
- **Analogy:** 📁 The month-end cabinet.
- **In the online store:** Monthly sales reports.

### 3. Regional / Multi-regional
- **What it is:** **Location types** (where data lives), not access-frequency classes. Older names for Standard storage in one region or many.
- **Looks like:** `-l us-central1` / `-l US`
- **Not to be confused with:** storage classes for archives.
- **Analogy:** 🏢 Which building the files are in, not how often you open them.
- **In the online store:** Live product images use Standard.

### 🔗 How they fit together
```
 read every month   → Nearline (30 days min)
 read every quarter → Coldline (90 days min) ✅
 read once a year   → Archive  (365 days min)
```

---

## 🌍 Real-World Scenario

A bank must pull archived warehouse snapshots every quarter for regulators. The engineer stores them in **Coldline**: storage is cheap, and four reads a year cost little.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Cold Storage

**Why it's correct:**
- ✔️ "**Cold Storage**" (Coldline) matches "**access this archived data once a quarter**": Coldline is designed for about quarterly access.
- ✔️ "**Cold**" matches "**cost-efficient**" + "**archival solution**": cheaper storage than Nearline or Standard.

📌 **When to use it:** Use it when files are opened about every three months.
🏢 **Office example:** Records kept in the storage room and opened for each quarterly audit.

### ❌ B
> **B.** Nearline Storage

**Wrong words:**
- ❌ "**Nearline Storage**": built for monthly access. Storing data you read only quarterly costs more than in Coldline.

📌 **When to use it:** Use it when files are opened about once a month.
🏢 **Office example:** The month-end accounting cabinet.

### ❌ C
> **C.** Regional Storage

**Wrong words:**
- ❌ "**Regional Storage**": a location (Standard storage in one region), priced for frequent access. Not an archive class.

📌 **When to use it:** Use it for active data used often in one region.
🏢 **Office example:** Keeping archive boxes on your desk.

### ❌ D
> **D.** Multi-Regional Storage

**Wrong words:**
- ❌ "**Multi-Regional Storage**": Standard storage across many regions. The most expensive option, for hot data.

📌 **When to use it:** Use it for files used often by people all over the world.
🏢 **Office example:** Copying the archive to every office's front desk.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's data warehouse exports go to `gs://shopnow-dw-archive` (Coldline). Each quarter, the compliance team reads the last quarter's export for the auditor, and pays only a small retrieval fee.

---

## 🧠 Key Takeaways / Memory Tips

- **Monthly → Nearline, quarterly → Coldline, yearly → Archive.**
- Regional and multi-regional are **locations**, not archive classes.
  🧠 *"**Quarterly? Coldline.**"*
- Related: **Q090** (Nearline for versions), **Q092** (regional + Coldline), **Q006** (storage classes).

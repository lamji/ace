# G043: Unpredictable Access Patterns: Let Cloud Storage Move Objects Between Classes Automatically (Autoclass)

**Topic:** Cloud Storage (Autoclass)
**Exam guide section:** 3.2 Managing storage: Estimating costs of data storage resources; 2.2 Cloud Storage options

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your bucket holds millions of user-uploaded files. Some are accessed often, some rarely, and the access pattern for each file is unpredictable. You want to minimize storage cost automatically without writing lifecycle rules and without paying retrieval fees when cold files are suddenly accessed. What should you do?
>
> **A.** Set the bucket's default storage class to Archive.
>
> **B.** Create lifecycle rules that move objects to Coldline after 30 days.
>
> **C.** Enable Autoclass on the bucket.
>
> **D.** Move all files to a Filestore instance.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A bucket (a Cloud Storage folder) holds millions of files uploaded by users. You can't predict which files will be opened often and which almost never.
- **What you must achieve:** Keep storage costs as low as possible automatically.
- **The limits:** No hand-written lifecycle rules (age-based move rules), and no retrieval fees (charges for reading from cold storage classes) when an old file is suddenly opened.
- **What they're really asking:** Which Cloud Storage feature moves each file to the right storage class based on how it's actually used?

**Clues in the question:**
- "**access pattern … unpredictable**" + "**automatically without writing lifecycle rules**": **Autoclass**.
- "**without paying retrieval fees**": Autoclass buckets don't charge retrieval or early-deletion fees, and it moves accessed objects back to Standard.

**Exam topic:** Storage cost management (exam guide sections 2.2 and 3.2).

---

## 📚 Key Terms Explained

### 1. Storage classes
- **What it is:** Standard (hot), Nearline (about monthly), Coldline (about quarterly), Archive (about yearly). Colder classes have cheaper storage but retrieval fees and minimum storage durations.
- **Looks like:** Standard $$ storage / no retrieval fee vs Archive ¢ storage / retrieval fee
- **Not to be confused with:** Locations (region, multi-region).
- **Analogy:** 🗄️ Desk drawer → back office → basement → off-site warehouse.
- **In the online store:** User avatars vs old order exports.

### 2. Autoclass 🔑
- **What it is:** A bucket setting that automatically moves each object to colder classes when it isn't accessed, and back to Standard when it is, with no retrieval or early-deletion fees.
- **Looks like:** `gcloud storage buckets update gs://shop-uploads --enable-autoclass`
- **Not to be confused with:** Lifecycle rules, which follow fixed age or condition rules you write.
- **Analogy:** 🤖 A filing assistant who moves each folder based on how often it's actually pulled.
- **In the online store:** User review photos bucket.

### 🔗 How they fit together
```
 object accessed? ─yes─► Standard
                  └no (30d)─► Nearline ─► Coldline ─► Archive  (auto, no retrieval fees) ✅
```

---

## 🌍 Real-World Scenario

A marketplace stores 50 million review photos. Most are never viewed again, but some go viral years later. **Autoclass** quietly moves cold photos to cheaper classes and brings viral ones back to Standard. Storage cost drops 40% with no rules to tune.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Set the bucket's default storage class to Archive.

**Wrong words:**
- ❌ "**Archive**": cheapest storage, but frequently accessed files get retrieval fees and slower economics, which breaks "**without paying retrieval fees**".

📌 **When to use it:** Use Archive for data you almost never read, like 7-year records.
🏢 **Office example:** Sending everything to the off-site warehouse, including files used daily.

### ❌ B
> **B.** Create lifecycle rules that move objects to Coldline after 30 days.

**Wrong words:**
- ❌ "**lifecycle rules**": the question says without writing them, and Coldline charges retrieval fees when files are read.

📌 **When to use it:** Use lifecycle rules when access drops predictably with age.
🏢 **Office example:** A fixed rule: "after 30 days, everything goes to the basement".

### ✅ C
> **C.** Enable Autoclass on the bucket.

**Why it's correct:**
- ✔️ "**Autoclass**" matches "**access pattern … unpredictable**" and "**automatically without writing lifecycle rules**".
- ✔️ Autoclass has no retrieval fees and moves accessed objects back to Standard, matching "**without paying retrieval fees when cold files are suddenly accessed**".

📌 **When to use it:** Use it when you can't predict which files will be used and want costs handled for you.
🏢 **Office example:** An assistant who moves each folder to the right room depending on how often it's really used.

### ❌ D
> **D.** Move all files to a Filestore instance.

**Wrong words:**
- ❌ "**Filestore**": a file server that costs more per GB, with no automatic tiering for millions of objects.

📌 **When to use it:** Use Filestore when apps need a shared NFS folder.
🏢 **Office example:** Moving the archive into expensive office space.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `gs://shop-review-photos`: Autoclass enabled. Product images stay Standard behind CDN. Tax archives use Archive with lifecycle rules.

---

## 🧠 Key Takeaways / Memory Tips

- **Unpredictable access + automatic cost savings + no retrieval fees → Autoclass.** Predictable aging → lifecycle rules.
  🧠 *"**Autoclass = auto filing assistant.**"*
- Related: **Q018**, **Q090**, **Q248**, **Q367**.

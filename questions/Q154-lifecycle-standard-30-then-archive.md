# Q154: Hot for 30 Days, Then Rarely Read, Kept 3 Years (Standard → Archive)

**Topic:** Cloud Storage (lifecycle rules, Standard, Nearline, Coldline, Archive)

## ❓ Question
> You have been asked to set up Object Lifecycle Management for objects stored in storage buckets. The objects are written once and accessed frequently for 30 days. After 30 days, the objects are not read again unless there is a special need. The objects should be kept for three years, and you need to minimize cost. What should you do?
>
> **A.** Set up a policy that uses Nearline storage for 30 days and then moves to Archive storage for three years.
>
> **B.** Set up a policy that uses Standard storage for 30 days and then moves to Archive storage for three years.
>
> **C.** Set up a policy that uses Nearline storage for 30 days, then moves the Coldline for one year, and then moves to Archive storage for two years.
>
> **D.** Set up a policy that uses Standard storage for 30 days, then moves to Coldline for one year, and then moves to Archive storage for two years.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Files in a bucket are written once and read often for 30 days. After that they are almost never read, but must be kept for three years.
- **What you must achieve:** Set up Object Lifecycle Management (automatic rules that change or delete files based on age).
- **The limits:** Keep costs as low as possible.
- **What they're really asking:** Which age-based rules should move and then delete these files?

**Clues in the question:**
- "**accessed frequently for 30 days**" → **Standard** (no read fees).
- "**not read again unless there is a special need**" + "**three years**" + "**minimize cost**" → **Archive** right away (cheapest storage, 365-day minimum).

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Archive storage 🔑
- **What it is:** The **cheapest** class, for data read **less than once a year**. Minimum storage 365 days, highest read fee.
- **Looks like:** `SetStorageClass ARCHIVE` after age 30
- **Not to be confused with:** Coldline (quarterly).
- **Analogy:** 🏚️ The **off-site warehouse**.
- **In the online store:** Old invoices kept for tax law.

### 2. Standard storage
- **What it is:** For **frequently accessed** data. No minimum duration and no read fee.
- **Looks like:** default class
- **Not to be confused with:** Nearline.
- **Analogy:** 🗂️ Files on your desk.
- **In the online store:** This month's uploads.

### 🔗 How they fit together
```
 day 0–30: Standard (read often, no read fees) ✅
 day 30 → 3 yrs: Archive (cheapest, rarely read) ✅
```

---

## 🌍 Real-World Scenario

A company's scanned contracts are reviewed heavily in the first month, then kept for legal reasons. A lifecycle rule moves them from **Standard** to **Archive** after 30 days.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Set up a policy that uses Nearline storage for 30 days and then moves to Archive storage for three years.

**Wrong words:**
- ❌ "**Nearline storage for 30 days**": Nearline charges for every read. Data "accessed frequently" costs more there than in Standard.
- ✔️ "Archive storage for three years" is right.

📌 **When to use it:** Use Nearline for data read about once a month.
🏢 **Office example:** Paying a fee every time you open a file you use daily.

### ✅ B
> **B.** Set up a policy that uses Standard storage for 30 days and then moves to Archive storage for three years.

**Why it's correct:**
- ✔️ "**Standard storage for 30 days**" matches "**accessed frequently for 30 days**": no read fees.
- ✔️ "**moves to Archive storage for three years**" matches "**not read again unless there is a special need**" + "**minimize cost**": the cheapest storage.

📌 **When to use it:** Use it when files are busy at first and then just need to be kept for years.
🏢 **Office example:** Papers stay on your desk for a month, then go straight to the off-site warehouse.

### ❌ C
> **C.** Set up a policy that uses Nearline storage for 30 days, then moves the Coldline for one year, and then moves to Archive storage for two years.

**Wrong words:**
- ❌ "**Nearline … 30 days**": read fees on hot data.
- ❌ "**Coldline for one year**": more expensive than Archive for data that's not read.

📌 **When to use it:** Use Coldline for data read about quarterly.
🏢 **Office example:** An extra stop in the storage room you don't need.

### ❌ D
> **D.** Set up a policy that uses Standard storage for 30 days, then moves to Coldline for one year, and then moves to Archive storage for two years.

**Wrong words:**
- ✔️ "Standard for 30 days" is right.
- ❌ "**moves to Coldline for one year**": Coldline costs more per GB than Archive, and the data isn't read.

📌 **When to use it:** Use it when data is still read quarterly during year one.
🏢 **Office example:** Paying for a closer storage room when nobody goes there.

---

## 🛒 E-Commerce Full-Stack Example

```json
{"rule":[{"action":{"type":"SetStorageClass","storageClass":"ARCHIVE"},"condition":{"age":30}},
         {"action":{"type":"Delete"},"condition":{"age":1095}}]}
```
ShopNow's order invoices: busy for the first month, then archived and deleted after 3 years.

---

## 🧠 Key Takeaways / Memory Tips

- **Hot → Standard. Never read → Archive straight away.**
- Nearline/Coldline only if there are monthly or quarterly reads.
  🧠 *"**Busy month on the desk, then straight to the warehouse.**"*
- Related: **Q090**, **Q092**, **Q107** (classes).

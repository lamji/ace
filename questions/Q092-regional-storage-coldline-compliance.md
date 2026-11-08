# Q092: One-Location Compliance, Archived After 30 Days, Read Yearly (Regional + Coldline)

**Topic:** Cloud Storage (location types, storage classes, lifecycle rules)

## ❓ Question
> You want to select and configure a solution for storing and archiving data on Google Cloud Platform. You need to support compliance objectives for data from one geographic location. This data is archived after 30 days and needs to be accessed annually. What should you do?
>
> **A.** Select Multi-Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Coldline Storage.
>
> **B.** Select Multi-Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Nearline Storage.
>
> **C.** Select Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Nearline Storage.
>
> **D.** Select Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Coldline Storage.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** Today, the **Archive** class (365-day minimum) is the best fit for "once a year". It isn't an option here, so **Coldline** is the cheapest choice offered.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Data from one geographic location must be stored and archived to meet compliance rules.
- **What you must achieve:** Store and archive the data.
- **The limits:** It is archived after 30 days and read about once a year.
- **What they're really asking:** Which storage class and location setup fit?

**Clues in the question:**
- "**compliance objectives for data from one geographic location**": keep it in **one region** → **Regional** storage. Multi-regional spreads data across a large area.
- "**accessed annually**": very rare access → the coldest class offered → **Coldline**.
- "**archived after 30 days**": a **lifecycle rule** with age 30.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1️⃣ Location type: Regional vs Multi-regional 🔑
- **What it is:** Where the bucket's data is physically stored. **Regional** = one region (e.g., `europe-west3`, Frankfurt). **Multi-regional** = copies across a large area (e.g., `EU`, `US`).
- **Looks like:** `gsutil mb -l europe-west3 gs://shopnow-tax-records`
- **Not to be confused with:** storage class (how often you read it).
- **Analogy:** 🏢 Keeping files in **one city's office** (regional) vs in **offices across the country** (multi-regional).
- **In the online store:** German tax records must stay in Germany.

### 2️⃣ Storage classes (review from Q006, Q090)
- **Nearline:** about **once a month**, 30-day minimum.
- **Coldline:** about **once a quarter or less**, 90-day minimum, cheaper storage, higher read fee.
- **Archive:** about **once a year**, 365-day minimum, cheapest storage.
- **Analogy:** 📁 Nearline = month-end cabinet. 🧊 Coldline = storage room for audits.

### 3️⃣ Lifecycle rule (review from Q090)
- **What it is:** A bucket rule that changes the class of objects automatically after a condition, such as age.
- **Looks like:** `{"action": {"type": "SetStorageClass", "storageClass": "COLDLINE"}, "condition": {"age": 30}}`

### 🔗 How they fit together
```
 "one geographic location" → Regional bucket (europe-west3) ✅
 "accessed annually"       → Coldline after 30 days ✅ (Archive would be even better, not offered)
```

---

## 🌍 Real-World Scenario

A company must keep customer records inside one country by law. Records are needed only for the yearly audit. The engineer creates a **regional** bucket in that country's region and adds a lifecycle rule that moves files to **Coldline** after 30 days.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Select Multi-Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Coldline Storage.

**Wrong words:**
- ❌ "**Select Multi-Regional Storage**": copies data across a large area, which breaks "**one geographic location**".
- ✔️ "archives data after 30 days to Coldline Storage" is right.

📌 **When to use it:** Use multi-regional when files must survive a whole region going down and there's no location rule.
🏢 **Office example:** Keeping copies of records in offices across the country, when the law says one city only.

### ❌ B
> **B.** Select Multi-Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Nearline Storage.

**Wrong words:**
- ❌ "**Select Multi-Regional Storage**": breaks the one-location rule (see A).
- ❌ "**to Nearline Storage**": Nearline is for monthly reads. For yearly reads, it costs more than Coldline.

📌 **When to use it:** Use it for files read about monthly, with copies across a wide area.
🏢 **Office example:** Month-end files copied to offices nationwide.

### ❌ C
> **C.** Select Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Nearline Storage.

**Wrong words:**
- ✔️ "Select Regional Storage" is right.
- ❌ "**to Nearline Storage**": built for **monthly** access. Data read once a year is cheaper in Coldline.

📌 **When to use it:** Use it when files must stay in one region and are read about once a month.
🏢 **Office example:** The local month-end accounting cabinet.

### ✅ D
> **D.** Select Regional Storage. Add a bucket lifecycle rule that archives data after 30 days to Coldline Storage.

**Why it's correct:**
- ✔️ "**Select Regional Storage**" matches "**compliance objectives for data from one geographic location**": the data stays in one region.
- ✔️ "**archives data after 30 days**" matches "**archived after 30 days**": the exact timing.
- ✔️ "**to Coldline Storage**" matches "**accessed annually**": the coldest, cheapest class offered for very rare reads.

📌 **When to use it:** Use it when files must stay in one place and are opened only about once a year.
🏢 **Office example:** Old records kept in the local storage room, opened only for the yearly audit.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's German invoices must stay in Germany and are pulled once a year for the tax audit.

```bash
gsutil mb -l europe-west3 gs://shopnow-de-invoices
cat > lc.json <<'EOF'
{"rule": [{"action": {"type": "SetStorageClass", "storageClass": "COLDLINE"}, "condition": {"age": 30}}]}
EOF
gsutil lifecycle set lc.json gs://shopnow-de-invoices
```

---

## 🧠 Key Takeaways / Memory Tips

- **"One geographic location" → Regional.** Multi-regional spreads data out.
- **Monthly → Nearline, quarterly/yearly (from these options) → Coldline.** Archive is best for yearly when offered.
  🧠 *"**One place → Regional. Once a year → as cold as possible.**"*
- Related: **Q090** (versions → Nearline), **Q006** (storage classes), **Q061** (Coldline for audit logs).

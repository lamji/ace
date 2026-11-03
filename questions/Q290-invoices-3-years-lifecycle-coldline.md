# Q290: Invoices Kept 3 Years, Frequent Use for 6 Months, Then Audit Only (Cloud Storage Lifecycle → Coldline After 6 Months)

**Topic:** Cloud Storage (storage classes, lifecycle)

## ❓ Question
> Your company would like to store invoices and other financial documents in Google Cloud. You need to identify a Google-managed solution to store this information for your company. You must ensure that the documents are kept for a duration of three years. Your company's analysts need frequent access to invoices from the past six months. After six months, invoices should be archived for audit purposes only. You want to minimize costs and follow Google-recommended practices. What should you do?
>
> **A.** Use Cloud Storage with Object Lifecycle Management to change the object storage class to Coldline after six months.
>
> **B.** Use Cloud Storage with Object Lifecycle Management to change the object storage class to Standard after six months.
>
> **C.** Store your documents on Filestore, and move the documents to Cloud Storage with object storage class set to Coldline after six months.
>
> **D.** Store your documents on Filestore, and move the documents to Cloud Storage with object storage class set to Standard after six months.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Frequent for **6 months**, then **audit only** until **3 years**. Cheapest managed option.

**Clues in the question:**
- "**Google-managed**" + documents → **Cloud Storage**.
- "**archived for audit purposes only**" after six months → cheaper class (**Coldline** is the only cheaper option offered).
- Moving automatically → **Object Lifecycle Management**.

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Coldline 🔑 (review)
- **What it is:** Low-cost class for data accessed about once a quarter or less; 90-day minimum.
- **Looks like:** `SetStorageClass COLDLINE` at `age: 180`
- **Not to be confused with:** Standard.
- **Analogy:** 🗄️ A back-room cabinet.
- **In the online store:** Old invoices.

### 2. Filestore
- **What it is:** Managed NFS file shares for VMs/GKE. More expensive than Cloud Storage for documents.
- **Looks like:** —
- **Not to be confused with:** Cloud Storage.
- **Analogy:** 🗂️ A shared network drive.
- **In the online store:** —

### 🔗 How they fit together
```
 Standard (0–6 months, frequent) ─ lifecycle age>180 ─► Coldline (audit only) ✅ ... delete at 3 years
```

---

## 🌍 Real-World Scenario

Finance stores invoices in **Cloud Storage Standard**; a **lifecycle rule** moves them to **Coldline** at 6 months and deletes them after 3 years.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use Cloud Storage with Object Lifecycle Management to change the object storage class to Coldline after six months.

**Why it's correct:**
- ✔️ "**Cloud Storage with Object Lifecycle Management**" matches "**Google-managed solution**" + "**minimize costs**".
- ✔️ "**change the object storage class to Coldline after six months**" matches "**After six months, invoices should be archived for audit purposes only**".

📌 **When to use it:** Use it when files are busy for a few months, then rarely touched but must be kept.
🏢 **Office example:** Moving last half-year's invoices from the front desk to the back-room cabinet automatically.

### ❌ B
> **B.** Use Cloud Storage with Object Lifecycle Management to change the object storage class to Standard after six months.

**Wrong words:**
- ❌ "**to Standard after six months**": they already start in Standard; no savings.

📌 **When to use it:** Use Standard for frequently used files.
🏢 **Office example:** Moving papers from the desk to... the desk.

### ❌ C
> **C.** Store your documents on Filestore, and move the documents to Cloud Storage with object storage class set to Coldline after six months.

**Wrong words:**
- ❌ "**Store your documents on Filestore**": a pricey file share; moving files means extra work.

📌 **When to use it:** Use Filestore for shared file systems for apps.
🏢 **Office example:** Keeping invoices on an expensive network drive first.

### ❌ D
> **D.** Store your documents on Filestore, and move the documents to Cloud Storage with object storage class set to Standard after six months.

**Wrong words:**
- ❌ "**Filestore**" and ❌ "**Standard after six months**": costly on both ends.

📌 **When to use it:** **Never use this** for this need.
🏢 **Office example:** Expensive drive, then the expensive cabinet.

---

## 🛒 E-Commerce Full-Stack Example

Bucket `shopnow-invoices` (Standard): lifecycle `age 180 → COLDLINE`, `age 1095 → Delete`.

---

## 🧠 Key Takeaways / Memory Tips

- **Busy then rarely used documents → Cloud Storage + lifecycle to a colder class.**
  🧠 *"**Hot for six months, Coldline after.**"*
- Related: **Q154**, **Q248**, **Q250**.

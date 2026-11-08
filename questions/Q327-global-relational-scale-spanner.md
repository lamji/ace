# Q327: Relational DB That Scales Globally With Minimal Admin (Spanner)

**Topic:** Databases (Spanner)

## ❓ Question
> Your company wants to migrate your data from an on-premises relational database to Google Cloud. Your current database can no longer scale with respect to the growth of your users, and you expect the number of users to rapidly grow. You need to choose a relational database that allows you to globally scale while minimizing your management and administration efforts. You also want to follow Google-recommended practices. What should you do?
>
> **A.** Use Cloud SQL.
>
> **B.** Use Spanner.
>
> **C.** Use Firestore.
>
> **D.** Use BigQuery.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your on-premises relational database can no longer keep up as users grow fast.
- **What you must achieve:** Move to a relational database that can scale globally.
- **The limits:** Minimal management work and recommended practice.
- **What they're really asking:** Which relational database scales worldwide with little management?

**Clues in the question:**
- "**relational**" + "**globally scale**" → **Spanner**.

**Exam topic:** Databases.

---

## 📚 Key Terms Explained

### 1. Spanner 🔑 (review from Q308)
- **What it is:** Global relational DB with automatic sharding.
- **Looks like:** —
- **Not to be confused with:** Cloud SQL.
- **Analogy:** 🏦 Synced global ledger.
- **In the online store:** —

### 🔗 How they fit together
```
 relational + global scale → Spanner ✅
```

---

## 🌍 Real-World Scenario

A fast-growing app moves to **Spanner** for global relational scale.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Cloud SQL.

**Wrong words:**
- ❌ "**Cloud SQL**": regional, vertical scaling limits.

📌 **When to use it:** Use Cloud SQL for regional apps.
🏢 **Office example:** One branch ledger.

### ✅ B
> **B.** Use Spanner.

**Why it's correct:**
- ✔️ "**Spanner**" matches "**relational database that allows you to globally scale**" + "**minimizing your management**".

📌 **When to use it:** Use it when a growing app needs one relational database that works worldwide.
🏢 **Office example:** One ledger kept in sync across every branch office.

### ❌ C
> **C.** Use Firestore.

**Wrong words:**
- ❌ "**Firestore**": NoSQL document DB.

📌 **When to use it:** Use Firestore for app documents.
🏢 **Office example:** Index cards.

### ❌ D
> **D.** Use BigQuery.

**Wrong words:**
- ❌ "**BigQuery**": analytics warehouse.

📌 **When to use it:** Use BigQuery for analytics.
🏢 **Office example:** The reports library.

---

## 🛒 E-Commerce Full-Stack Example

Global loyalty points on Spanner.

---

## 🧠 Key Takeaways / Memory Tips

- **Relational + global → Spanner.**
  🧠 *"**Global SQL = Spanner.**"*
- Related: **Q308**.

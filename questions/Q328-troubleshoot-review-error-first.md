# Q328: One User Can't Access Cloud SQL, Another Can — First Step (Review the Error Message)

**Topic:** Troubleshooting (IAM, Cloud SQL)

## ❓ Question
> You are the Google Cloud systems administrator for your organization. User A reports that they received an error when attempting to access the Cloud SQL database in their Google Cloud project, while User B can access the database. You need to troubleshoot the issue for User A, while following Google-recommended practices. What should you do first?
>
> **A.** Confirm that network firewall rules are not blocking traffic for User A.
>
> **B.** Verify that User A has the Identity and Access Management (IAM) Project Owner role assigned.
>
> **C.** Review recent configuration changes that may have caused unintended modifications to permissions.
>
> **D.** Review the error message that User A received.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** User A gets an error, User B doesn't. **What first?**

**Clues in the question:**
- "**What should you do first**" → start with the **error message**; it tells you if it's permissions, network, or something else.

**Exam topic:** Troubleshooting.

---

## 📚 Key Terms Explained

### 1. Troubleshooting order 🔑
- **What it is:** Read the error first, then check the likely cause (IAM, network, config).
- **Looks like:** `ERROR: (gcloud.sql.connect) PERMISSION_DENIED: cloudsql.instances.connect`
- **Not to be confused with:** guessing.
- **Analogy:** 🩺 Doctor asks about symptoms before testing.
- **In the online store:** —

### 🔗 How they fit together
```
 error message → points to IAM / network / config ✅
```

---

## 🌍 Real-World Scenario

Before touching anything, the admin reads User A's **error**: `PERMISSION_DENIED` → missing `roles/cloudsql.client`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Confirm that network firewall rules are not blocking traffic for User A.

**Wrong words:**
- ❌ Checking **firewall rules** first: a guess; error may be IAM.

📌 **When to use it:** Use it when the error shows a timeout or connection refused.
🏢 **Office example:** Checking the doors before asking what went wrong.

### ❌ B
> **B.** Verify that User A has the Identity and Access Management (IAM) Project Owner role assigned.

**Wrong words:**
- ❌ "**Project Owner role**": far too broad; never the fix.

📌 **When to use it:** **Never use this** to fix access.
🏢 **Office example:** Giving the master key to fix a badge problem.

### ❌ C
> **C.** Review recent configuration changes that may have caused unintended modifications to permissions.

**Wrong words:**
- ❌ Reviewing **recent changes** first: useful later, but the error is the quickest clue.

📌 **When to use it:** Use it after the error points to a permissions change.
🏢 **Office example:** Reading the change log before asking the symptom.

### ✅ D
> **D.** Review the error message that User A received.

**Why it's correct:**
- ✔️ "**Review the error message**" matches "**What should you do first**" + "**troubleshoot the issue for User A**".

📌 **When to use it:** Use it as the first step whenever something fails for one person.
🏢 **Office example:** Asking the staff member exactly what the screen said before calling IT.

---

## 🛒 E-Commerce Full-Stack Example

Ana's error says `cloudsql.instances.connect` denied → grant `roles/cloudsql.client`.

---

## 🧠 Key Takeaways / Memory Tips

- **Troubleshooting first step → read the error message.**
  🧠 *"**Read before you fix.**"*
- Related: —

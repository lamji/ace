# Q186: New Cloud Identity Users Already Have Google Accounts (Invite Them to Transfer Their Account)

**Topic:** Cloud Identity (conflicting / unmanaged accounts)

## ❓ Question
> You need to add a group of new users to Cloud Identity. Some of the users already have existing Google accounts. You want to follow one of Google's recommended practices and avoid conflicting accounts. What should you do?
>
> **A.** Invite the user to transfer their existing account.
>
> **B.** Invite the user to use an email alias to resolve the conflict.
>
> **C.** Tell the user that they must delete their existing account.
>
> **D.** Tell the user to remove all personal email from the existing account.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You need to add new users to Cloud Identity. Some already have personal Google accounts using their work email.
- **What you must achieve:** Add them without creating clashing duplicate accounts.
- **The limits:** Follow a Google-recommended practice.
- **What they're really asking:** How do you handle users who already have a Google account with that email?

**Clues in the question:**
- "**avoid conflicting accounts**" + "**Google's recommended practices**" → **invite them to transfer** the unmanaged account into your Cloud Identity.

**Exam topic:** Cloud Identity.

---

## 📚 Key Terms Explained

### 1. Unmanaged (conflicting) account 🔑
- **What it is:** A Google account someone created with a **company email** before the company used Cloud Identity. The company doesn't control it.
- **Looks like:** ana@shopnow.com created on her own in 2021
- **Not to be confused with:** a personal gmail.
- **Analogy:** 🔑 An employee who copied an office key before the locks were managed.
- **In the online store:** Old dev accounts.

### 2. Account transfer
- **What it is:** An admin **invites** the user. When they accept, the account becomes **managed** and their data is kept.
- **Looks like:** Admin console → Users → Transfer tool for unmanaged users
- **Not to be confused with:** deletion.
- **Analogy:** 📝 Bringing the copied key into the official key register.
- **In the online store:** —

### 🔗 How they fit together
```
 ana@shopnow.com (unmanaged) ── invite to transfer ── accepts ──► managed by Cloud Identity ✅
```

---

## 🌍 Real-World Scenario

When ShopNow set up Cloud Identity, some developers already had Google accounts on their work email. The admin used the **transfer tool** to invite them, and they accepted.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Invite the user to transfer their existing account.

**Why it's correct:**
- ✔️ "**Invite the user to transfer their existing account**" matches "**avoid conflicting accounts**" + "**Google's recommended practices**".

📌 **When to use it:** Use it when someone already has an account under the company name that the company should now manage.
🏢 **Office example:** Asking the employee to register their old key with the office key system.

### ❌ B
> **B.** Invite the user to use an email alias to resolve the conflict.

**Wrong words:**
- ❌ "**email alias**": doesn't fix the conflict. The unmanaged account still exists.

📌 **When to use it:** Use aliases to give a user extra addresses.
🏢 **Office example:** Giving someone a nickname instead of fixing their duplicate key.

### ❌ C
> **C.** Tell the user that they must delete their existing account.

**Wrong words:**
- ❌ "**must delete their existing account**": they'd lose data. Not the recommended practice.

📌 **When to use it:** **Never** force this. Offer the transfer first.
🏢 **Office example:** Making someone shred their files instead of bringing them in.

### ❌ D
> **D.** Tell the user to remove all personal email from the existing account.

**Wrong words:**
- ❌ "**remove all personal email**": irrelevant to the account conflict.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Asking someone to empty their pockets to fix a key problem.

---

## 🛒 E-Commerce Full-Stack Example

Admin console → **Transfer tool for unmanaged users** → invite `ben@shopnow.com` → he accepts → his account joins ShopNow's Cloud Identity.

---

## 🧠 Key Takeaways / Memory Tips

- **Existing Google account on a work email → invite to transfer** (recommended).
  🧠 *"**Don't delete, transfer.**"*
- Related: **Q110**, **Q114**.

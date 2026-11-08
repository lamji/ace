# G044: Keep Weekly Firestore Backups for 8 Weeks and Restore to a New Database (Firestore Backup Schedule)

**Topic:** Firestore (backup and restore)
**Exam guide section:** 3.2 Managing storage and data solutions: Backing up and restoring database instances (Firestore)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your application stores shopping carts and user profiles in a Firestore database. Compliance requires a backup every week that is kept for 8 weeks, and the ability to restore a backup into a new database for investigation. You want a managed solution. What should you do?
>
> **A.** Write a script that reads every document and saves it to a JSON file on a VM each week.
>
> **B.** Enable point-in-time recovery only, and rely on it for 8 weeks of history.
>
> **C.** Create a Firestore backup schedule with weekly recurrence and 8-week retention, and restore backups to a new database when needed.
>
> **D.** Create a Persistent Disk snapshot of the Firestore database.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app keeps shopping carts and user profiles in Firestore (Google's managed document database).
- **What you must achieve:** Take a backup every week, keep each one for 8 weeks, and be able to load a backup into a new database to investigate.
- **The limits:** Use a managed (Google-run) solution, not scripts.
- **What they're really asking:** Which Firestore feature makes scheduled backups with a retention period?

**Clues in the question:**
- "**backup every week … kept for 8 weeks**": a Firestore **backup schedule** (weekly, retention 8w).
- "**restore … into a new database**": Firestore restores create a new database.
- Point-in-time recovery only covers up to 7 days.

**Exam topic:** Database backup and restore (exam guide section 3.2).

---

## 📚 Key Terms Explained

### 1. Firestore backup schedule 🔑
- **What it is:** A managed schedule (daily or weekly) that takes backups of a Firestore database and keeps each for a chosen retention (up to 14 weeks). You restore a backup into a **new** database.
- **Looks like:** `gcloud firestore backups schedules create --database='(default)' --recurrence=weekly --day-of-week=SUN --retention=8w` → `gcloud firestore databases restore --source-backup=… --destination-database=investigate-1`
- **Not to be confused with:** Point-in-time recovery (PITR), which gives a short window of per-minute versions (up to 7 days).
- **Analogy:** 📅 A weekly photocopy of the records, each kept for two months.
- **In the online store:** Weekly backups of carts and profiles.

### 2. Point-in-time recovery (PITR)
- **What it is:** Keeps versions of data so you can read or recover data as of any minute in the last 7 days.
- **Looks like:** `gcloud firestore databases update --enable-pitr`
- **Not to be confused with:** Long-term backups.
- **Analogy:** ⏪ A 7-day rewind button.
- **In the online store:** Undoing a bad import from yesterday.

### 🔗 How they fit together
```
 Firestore (default) ─weekly (Sun)─► backup (kept 8w) ─restore─► new DB investigate-1 ✅
 PITR: only last 7 days
```

---

## 🌍 Real-World Scenario

After a bug corrupted some profiles, auditors wanted to see the data as it was three weeks earlier. With a weekly **backup schedule** kept 8 weeks, the team restores that week's backup into `investigate-1` and compares, without touching production.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Write a script that reads every document and saves it to a JSON file on a VM each week.

**Wrong words:**
- ❌ "**script … JSON file on a VM**": custom, slow at scale, not consistent, and not managed.

📌 **When to use it:** Avoid it for backups. Use the built-in schedules.
🏢 **Office example:** Copying every record by hand each week.

### ❌ B
> **B.** Enable point-in-time recovery only, and rely on it for 8 weeks of history.

**Wrong words:**
- ✔️ PITR is useful for recent mistakes.
- ❌ "**rely on it for 8 weeks of history**": PITR covers at most 7 days.

📌 **When to use it:** Use PITR to undo a mistake from the last few days.
🏢 **Office example:** A rewind button that only goes back a week.

### ✅ C
> **C.** Create a Firestore backup schedule with weekly recurrence and 8-week retention, and restore backups to a new database when needed.

**Why it's correct:**
- ✔️ "**backup schedule with weekly recurrence and 8-week retention**" matches "**backup every week that is kept for 8 weeks**".
- ✔️ "**restore backups to a new database**" matches "**restore a backup into a new database for investigation**".
- ✔️ It's built into Firestore, matching "**managed solution**".

📌 **When to use it:** Use it when the rules say keep regular copies of the database for a set time.
🏢 **Office example:** A weekly photocopy of all records, each copy kept for two months.

### ❌ D
> **D.** Create a Persistent Disk snapshot of the Firestore database.

**Wrong words:**
- ❌ "**Persistent Disk snapshot of the Firestore database**": Firestore is serverless, so there's no disk you can snapshot.

📌 **When to use it:** Use disk snapshots for VM disks.
🏢 **Office example:** Photographing a filing cabinet that isn't yours.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** Firestore `(default)`: PITR on (7 days) + weekly backup schedule on Sunday, retention 8w. Investigations restore into a separate database.

---

## 🧠 Key Takeaways / Memory Tips

- **Firestore: last 7 days → PITR. Regular backups kept for weeks → backup schedule (daily/weekly, retention). Restore → new database.**
  🧠 *"**PITR = rewind a week; schedule = weekly photocopies.**"*
- Related: **Q003**, **G045**.

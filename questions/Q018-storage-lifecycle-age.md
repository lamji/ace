# Q018: Lifecycle Policy to Move Objects to Coldline, Then Delete Them

**Topic:** Cloud Storage (Object Lifecycle Management, Age condition, SetStorageClass / Delete actions, gsutil rewrite)

## ❓ Question
> You need to set up a policy so that videos stored in a specific Cloud Storage Regional bucket are moved to Coldline after 90 days, and then deleted after one year from their creation. How should you set up the policy?
>
> **A.** Use Cloud Storage Object Lifecycle Management using Age conditions with SetStorageClass and Delete actions. Set the SetStorageClass action to 90 days and the Delete action to 275 days (365 – 90)
>
> **B.** Use Cloud Storage Object Lifecycle Management using Age conditions with SetStorageClass and Delete actions. Set the SetStorageClass action to 90 days and the Delete action to 365 days.
>
> **C.** Use gsutil rewrite and set the Delete action to 275 days (365-90).
>
> **D.** Use gsutil rewrite and set the Delete action to 365 days.

*(The `"€λ` characters in option A are a broken dash, shown here as `–`.)*

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Videos are stored in a regional Cloud Storage bucket (a bucket is a named container for files).
- **What you must achieve:** After 90 days, move each video to Coldline (a cheaper class for rarely opened files); one year after it was created, delete it.
- **The limits:** It should happen automatically.
- **What they're really asking:** How do you set up rules that first move and then delete the videos on schedule?

| Keyword | What it hints at |
|---|---|
| "**set up a policy**" | An **automatic rule**, so **Object Lifecycle Management** |
| "**moved to Coldline after 90 days**" | **SetStorageClass** action with **Age = 90** |
| "**deleted after one year from their creation**" | **Delete** action with **Age = 365** |
| "**from their creation**" | 🔑 **Age always counts from the object's creation date**, so there's no subtracting |

**Exam topic:** Cloud Storage, specifically **Object Lifecycle Management**.

🔑 **The key trick:** The **Age** condition counts days **since the object was created**. Moving it to Coldline **does not reset the clock**. So "delete after one year" is **Age 365**, not 275.

---

## 📚 Key Terms Explained

### 1️⃣ Cloud Storage Bucket and Object (review from Q006)
- **Bucket:** A container for files. **Regional** means its data lives in **one region**.
- **Object:** One file in the bucket (here, a **video**).
- **Analogy:** 📦 Bucket = a **storage room**. Objects = the **boxes** in it.

### 2️⃣ Storage Class: Standard → Coldline (review from Q006)
- **Standard:** For files used **often**. Higher storage price.
- **Coldline:** For files used **about once a quarter or less**. Much cheaper to store, with a **90-day minimum storage duration**.
- **Analogy:** 🏠 Moving boxes from the **office shelf** to the **cheap storage unit across town**.

### 3️⃣ Object Lifecycle Management
- **What it is:** **Automatic rules** on a bucket that **change an object's storage class** or **delete it** when conditions are met. You set it **once**, and Google applies it to **every object, every day**, including new uploads.
- Each rule = **an action** + **a condition**.
- **Analogy:** 🧹 The company's **records retention policy**, enforced automatically by the records team, with nobody doing it by hand.

### 4️⃣ Actions: SetStorageClass and Delete
- **SetStorageClass:** Changes the object's class (e.g., Standard → Coldline).
- **Delete:** Removes the object.
- **Analogy:** 📦 "**Move** the box to the basement" vs "**Shred** the box."

### 5️⃣ Age Condition 🔑
- **What it is:** The number of **days since the object was CREATED** (uploaded). It's **not** "days since the last action" or "days since it moved to Coldline."
- Changing storage class with a lifecycle rule **doesn't change the creation date**, so the clock keeps counting from **day 0**.
- **Analogy:** 🎂 Like a person's **age**: it counts from their **birthday**, not from the day they moved house.
- **In the online store:** A video uploaded on Jan 1 is "Age 90" on about Apr 1 and "Age 365" on about Jan 1 of the next year, wherever it's stored.

### 6️⃣ gsutil and `gsutil rewrite`
- **gsutil:** The **older** command-line tool for Cloud Storage. Google now recommends **`gcloud storage`** instead.
- **`gsutil rewrite`:** **Rewrites existing objects right now**, e.g., to change their storage class (`-s coldline`) or encryption key. It's a **one-time manual action**. It **doesn't create rules**, and it has **no "Delete action" or schedule**.
- **Analogy:** 📦 **Repacking every box by hand today**. It doesn't set any rule for the future.

### 🔗 How They Fit Together
```
📦 Bucket: gs://shopnow-warehouse-videos  (Regional, asia-southeast1)
   └── 🧹 Lifecycle policy (runs automatically, every day)
         ├── Rule 1: IF Age ≥ 90  AND class = STANDARD → SetStorageClass COLDLINE
         └── Rule 2: IF Age ≥ 365                      → Delete

🎥 One video's life (Age = days since CREATED, never reset):
   Day 0 ──────────── Day 90 ──────────────────────────── Day 365
   uploaded            ➜ moved to Coldline                 ➜ 🗑️ deleted
   (Standard)          (still Age 90, clock keeps going)    (Age 365 = 1 year from creation ✅)

   ❌ Option A: Delete at Age 275 → deleted on day 275, ~3 months TOO EARLY
```

---

## 🌍 Real-World Scenario

Companies store **lots of video**: security cameras, recorded meetings, training clips. New videos get watched; old ones almost never do. And company or legal policy often says, *"Keep recordings for exactly 1 year, then delete them."*

Doing this by hand is impossible at scale. **Lifecycle rules** handle it automatically: **cheaper storage after 90 days**, **deletion at 1 year**, for every video, forever.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Cloud Storage Object Lifecycle Management using Age conditions with SetStorageClass and Delete actions. Set the SetStorageClass action to 90 days and the Delete action to 275 days (365 – 90)

**Why it's wrong:**
- ✔️ The right **tool** (Lifecycle Management) and the right **actions**.
- ❌ The **math is wrong**. **Age counts from creation**, not from when the video moved to Coldline. Age 275 deletes videos on **day 275**, about **3 months too early**.
- ⚠️ **Trap option:** it assumes the clock **restarts** after the move to Coldline. It doesn't.

**📌 When to use it:** Use a 275-day delete **only if you really want files gone 275 days after they were created**. Here it deletes them too early.
🏢 **Office example:** **Shredding files after 9 months** when the rule says keep them for 1 year. The clock starts on the day the file was **created**, not the day it moved to the storage room.

### ✅ B
> **B.** Use Cloud Storage Object Lifecycle Management using Age conditions with SetStorageClass and Delete actions. Set the SetStorageClass action to 90 days and the Delete action to 365 days.

**Why it's correct:**
- ✔️ **Lifecycle Management** is the built-in way to **automatically** change class and delete objects.
- ✔️ **SetStorageClass at Age 90** moves videos to Coldline **90 days after creation**.
- ✔️ **Delete at Age 365** deletes them **1 year after creation**, exactly as asked, because Age always counts from creation.
- ✔️ **Bonus:** each video stays in Coldline from day 90 to day 365 = **275 days**, well over Coldline's **90-day minimum**, so there's **no early-deletion charge**.

**📌 When to use it:** Use it when files should **automatically move to cheaper storage** and **later be deleted**, on a schedule.
🏢 **Office example:** A **records retention policy**: after 3 months, papers move to the **basement storage room**, and **1 year after they were made**, they're **shredded**. The records team does it automatically.

### ❌ C
> **C.** Use gsutil rewrite and set the Delete action to 275 days (365-90).

**Why it's wrong:**
- ❌ **`gsutil rewrite` doesn't create policies.** It rewrites existing objects **once, right now**. It has **no "Delete action"** and **no schedule**.
- ❌ New videos uploaded tomorrow wouldn't be covered.
- ❌ It also uses the **wrong number** (275, same mistake as A).

**📌 When to use it:** Use `gsutil rewrite` when you want to **change existing files once, right now** (for example, their storage class or encryption key). It's not for automatic rules.
🏢 **Office example:** **Re-labeling every box in the storage room by hand, one time**. It doesn't set any rule for the future.

### ❌ D
> **D.** Use gsutil rewrite and set the Delete action to 365 days.

**Why it's wrong:**
- ✔️ The **number** (365) is right.
- ❌ But the **tool** is wrong. `gsutil rewrite` has **no Delete action** and **can't schedule** anything. Only **Lifecycle Management** creates automatic rules.

**📌 When to use it:** Same as C: use `gsutil rewrite` only for a **one-time change to existing files**. For automatic delete rules, use **Lifecycle Management** (option B).
🏢 **Office example:** **Repacking every box into new boxes by hand today**. It doesn't set any rule for shredding them later.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **warehouse security cameras** upload videos to `gs://shopnow-warehouse-videos` (a **Regional** bucket in `asia-southeast1`).
- First **90 days**: often watched (checking missing packages, damaged items) → **Standard**
- After 90 days: rarely watched → **Coldline** (cheaper)
- After **1 year from recording**: company privacy policy says **delete** → **Delete**

**`lifecycle.json` (option B):**
```json
{
  "rule": [
    {
      "action": { "type": "SetStorageClass", "storageClass": "COLDLINE" },
      "condition": { "age": 90, "matchesStorageClass": ["STANDARD"] }
    },
    {
      "action": { "type": "Delete" },
      "condition": { "age": 365 }
    }
  ]
}
```
```bash
gcloud storage buckets update gs://shopnow-warehouse-videos --lifecycle-file=lifecycle.json
```

**🎬 Timeline for a video recorded on 2026-01-01:**
| Date | Age | What happens |
|---|---|---|
| 2026-01-01 | 0 | Uploaded (Standard). Staff review it after a "missing package" complaint |
| 2026-04-01 | 90 | ➜ **Moved to Coldline** automatically 💰 |
| 2027-01-01 | 365 | ➜ **Deleted** automatically 🗑️ (exactly 1 year after recording ✅) |

**With the other options:**
- **A (275):** The video is deleted on **2026-10-03**. In November, a customer disputes a June delivery, and the footage is **already gone**. ❌
- **C / D (`gsutil rewrite`):** Someone runs a one-time command (e.g., `gsutil rewrite -s coldline gs://shopnow-warehouse-videos/**`). It moves today's videos, but sets **no deletion rule**, and **new videos aren't covered**. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Automatically change class / delete objects after X days" → Object Lifecycle Management.**
- **🔑 Age = days since CREATION.** It's **never reset** by a class change. **Don't subtract!**
  🧠 *"Age counts from the **birthday**, not from the **move**."*
- **"1 year from creation" → Delete at Age 365.** "90 days" → SetStorageClass at Age 90.
- **`gsutil rewrite` = one-time change to existing objects** (class or encryption). It's **not a policy** and has **no Delete action**.
- **gsutil is legacy.** Google now recommends **`gcloud storage`**.
- Remember the minimum storage durations (from Q006): **Nearline 30, Coldline 90, Archive 365 days**. Plan rules so objects stay at least that long.

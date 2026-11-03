# Q184: Mission-Critical Analytics Files Used Continually, Minimal Cost, Users in Boston (Regional Standard)

**Topic:** Cloud Storage (location types and storage classes)

## ❓ Question
> You need to configure optimal data storage for files stored in Cloud Storage for minimal cost. The files are used in a mission-critical analytics pipeline that is used continually. The users are in Boston, MA (United States). What should you do?
>
> **A.** Configure regional storage for the region closest to the users. Configure a Nearline storage class.
>
> **B.** Configure regional storage for the region closest to the users. Configure a Standard storage class.
>
> **C.** Configure dual-regional storage for the dual region closest to the users. Configure a Nearline storage class.
>
> **D.** Configure dual-regional storage for the dual region closest to the users. Configure a Standard storage class.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated.** Many voters pick **D** because "mission-critical" suggests surviving a region outage (dual-region). **B** wins on "**minimal cost**": regional is cheaper and still highly available across zones. If your site's Most Voted is D, tell me and I'll update this file.

---

## 📖 What the Question Is Asking

**In plain words:** Files used **all the time**, at **lowest cost**, users in **one city**.

**Clues in the question:**
- "**used continually**" → **Standard** (Nearline charges per read and suits monthly access).
- "**minimal cost**" + users in one place → **regional**, the region nearest Boston (e.g. `us-east4`).

**Exam topic:** Cloud Storage.

---

## 📚 Key Terms Explained

### 1. Regional vs dual-region 🔑
- **What it is:** **Regional**: data in one region (copies across zones). **Dual-region**: copies in two regions, which survives a region outage but costs more.
- **Looks like:** `gsutil mb -l us-east4 gs://…` vs `-l nam4`
- **Not to be confused with:** multi-region.
- **Analogy:** 🏢 One building with several vaults vs two buildings in different cities.
- **In the online store:** Analytics bucket.

### 2. Standard vs Nearline (review)
- **What it is:** Standard = frequent access, no read fee. Nearline = about monthly, cheaper storage but per-GB read fee and 30-day minimum.
- **Looks like:** `-c standard`
- **Not to be confused with:** —
- **Analogy:** 🗄️ Desk drawer vs monthly cabinet.
- **In the online store:** —

### 🔗 How they fit together
```
 used continually → Standard
 minimal cost + one city → regional (us-east4) ✅
```

---

## 🌍 Real-World Scenario

A Boston analytics team reads pipeline files constantly. A **Standard** bucket in `us-east4` gives fast, cheap access with no retrieval fees.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure regional storage for the region closest to the users. Configure a Nearline storage class.

**Wrong words:**
- ✔️ "regional … closest to the users" is fine.
- ❌ "**Nearline**": continual reads would rack up retrieval fees.

📌 **When to use it:** Use Nearline for files opened about once a month.
🏢 **Office example:** A monthly cabinet for papers you use every hour.

### ✅ B
> **B.** Configure regional storage for the region closest to the users. Configure a Standard storage class.

**Why it's correct:**
- ✔️ "**regional storage for the region closest to the users**" matches "**minimal cost**" + "**users are in Boston**".
- ✔️ "**Standard storage class**" matches "**used continually**": no read fees, made for frequent access.

📌 **When to use it:** Use it when files are used all day by people in one area and you want to keep costs low.
🏢 **Office example:** Keeping today's working files in the desk drawers of your own office building.

### ❌ C
> **C.** Configure dual-regional storage for the dual region closest to the users. Configure a Nearline storage class.

**Wrong words:**
- ❌ "**dual-regional**": costs more.
- ❌ "**Nearline**": wrong for constant reads.

📌 **When to use it:** Use dual-region Nearline for monthly-accessed data needing two-region safety.
🏢 **Office example:** A monthly cabinet copied in two cities.

### ❌ D
> **D.** Configure dual-regional storage for the dual region closest to the users. Configure a Standard storage class.

**Wrong words:**
- ✔️ "Standard" is right.
- ❌ "**dual-regional**": higher cost than regional, against "**minimal cost**" (but see the note: some people pick this for "mission-critical").

📌 **When to use it:** Use it when files must survive the loss of a whole region.
🏢 **Office example:** Keeping copies of daily files in two office buildings in different cities.

---

## 🛒 E-Commerce Full-Stack Example

`gsutil mb -c standard -l us-east4 gs://shopnow-analytics-pipeline`

---

## 🧠 Key Takeaways / Memory Tips

- **Frequent access → Standard. Minimal cost + one area → regional.** Dual-region only when you must survive a region outage and can pay more.
  🧠 *"**Hot and local: Standard, regional.**"*
- Related: **Q154**, **Q103**.

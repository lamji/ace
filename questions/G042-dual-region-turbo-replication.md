# G042: Bucket Data Must Be Copied to a Second Region Within 15 Minutes (Dual-Region Bucket + Turbo Replication)

**Topic:** Cloud Storage (dual-region, turbo replication)
**Exam guide section:** 2.2 Planning storage and data solutions: Maintaining multi-region redundancy across data solutions

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your company stores order receipts in Cloud Storage. A disaster recovery requirement states that every newly written object must be copied to a second region within 15 minutes, and both regions must be in the United States. What should you do?
>
> **A.** Create a multi-region US bucket with default replication.
>
> **B.** Create a regional bucket in us-central1 and enable Object Versioning.
>
> **C.** Create a regional bucket and run a gcloud storage rsync script to another bucket once a day.
>
> **D.** Create a dual-region bucket in two US regions and enable turbo replication.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Order receipts are saved as files (objects) in Cloud Storage.
- **What you must achieve:** Make sure every new file is also copied to a second region (a different geographic area) within 15 minutes.
- **The limits:** Both regions must be in the United States.
- **What they're really asking:** Which bucket setup guarantees a copy in a second region within 15 minutes?

**Clues in the question:**
- "**second region**" + "**United States**": a **dual-region** bucket with two chosen US regions.
- "**within 15 minutes**": **turbo replication** has a 15-minute RPO (recovery point objective) for newly written objects. Default replication can take up to 12 hours for 100% of objects.

**Exam topic:** Storage redundancy (exam guide section 2.2).

---

## 📚 Key Terms Explained

### 1. Dual-region bucket
- **What it is:** A Cloud Storage bucket whose data is stored in two specific regions that you choose.
- **Looks like:** `gcloud storage buckets create gs://shop-receipts --location=US --placement=us-central1,us-east1 --rpo=ASYNC_TURBO`
- **Not to be confused with:** A multi-region bucket (a large area like `US`, where Google picks the places).
- **Analogy:** 🏙️ Keeping records in two named city offices.
- **In the online store:** Receipts in us-central1 + us-east1.

### 2. Turbo replication 🔑
- **What it is:** A premium option for dual-region buckets: 100% of newly written objects are replicated to both regions within **15 minutes** (the RPO target).
- **Looks like:** `--rpo=ASYNC_TURBO`
- **Not to be confused with:** Default replication (most objects within an hour, all within 12 hours).
- **Analogy:** 🚚 Express courier between the two offices.
- **In the online store:** Meets the receipts DR rule.

### 🔗 How they fit together
```
 write receipt ─► dual-region bucket (us-central1 + us-east1)
                   └─ turbo replication: copy in other region ≤ 15 min ✅
```

---

## 🌍 Real-World Scenario

Regulators require that receipts survive a regional outage with at most 15 minutes of loss. The engineer creates a **dual-region** bucket with **turbo replication** across two US regions. No scripts are needed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a multi-region US bucket with default replication.

**Wrong words:**
- ✔️ It is redundant across US locations.
- ❌ "**default replication**": no 15-minute guarantee (up to 12 hours), and turbo replication applies to dual-region buckets.

📌 **When to use it:** Use multi-region for highly available content served across a large area.
🏢 **Office example:** Storing records "somewhere in the country" with a slow courier.

### ❌ B
> **B.** Create a regional bucket in us-central1 and enable Object Versioning.

**Wrong words:**
- ❌ "**regional bucket**": one region only.
- ❌ "**Object Versioning**": keeps old versions, not copies in another region.

📌 **When to use it:** Use versioning to recover overwritten or deleted files.
🏢 **Office example:** Keeping old drafts in the same cabinet.

### ❌ C
> **C.** Create a regional bucket and run a gcloud storage rsync script to another bucket once a day.

**Wrong words:**
- ❌ "**once a day**": up to 24 hours of loss, which breaks "**within 15 minutes**". It's also a custom script to maintain.

📌 **When to use it:** Use scheduled syncs for non-critical copies.
🏢 **Office example:** A daily courier when you need express.

### ✅ D
> **D.** Create a dual-region bucket in two US regions and enable turbo replication.

**Why it's correct:**
- ✔️ "**dual-region bucket in two US regions**" matches "**second region**" and "**both regions must be in the United States**".
- ✔️ "**enable turbo replication**" matches "**within 15 minutes**".

📌 **When to use it:** Use it when files must be copied to a second chosen region very quickly for disaster recovery.
🏢 **Office example:** Sending every new record by express courier to a second named office.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `gs://shop-receipts`: dual-region `us-central1` + `us-east1`, `--rpo=ASYNC_TURBO`. Product images stay in a multi-region bucket behind Cloud CDN.

---

## 🧠 Key Takeaways / Memory Tips

- **Two chosen regions + copy within 15 minutes → dual-region bucket + turbo replication.**
  🧠 *"**Turbo = 15-minute copy.**"*
- Related: **Q092**, **Q184**, **G041**.

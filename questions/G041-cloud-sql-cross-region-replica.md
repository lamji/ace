# G041: Cloud SQL Must Recover in Another Region if the Primary Region Fails (Cross-Region Read Replica, Promote on Failure)

**Topic:** Cloud SQL (cross-region DR)
**Exam guide section:** 2.2 Planning storage and data solutions: Maintaining multi-region redundancy across data solutions

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your Cloud SQL for MySQL instance in us-east1 is configured for high availability within the region. The business now requires that the database can be recovered in another region within minutes if the entire us-east1 region becomes unavailable, with minimal data loss. What should you do?
>
> **A.** Take a daily export of the database to a Cloud Storage bucket in us-east1.
>
> **B.** Create a cross-region read replica in another region, such as us-west1, and promote it if us-east1 fails.
>
> **C.** Add a second zone to the existing high-availability configuration.
>
> **D.** Increase the instance's machine type and storage.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your MySQL database on Cloud SQL (Google's managed database) runs in us-east1, with a standby in another zone of the same region.
- **What you must achieve:** If the whole us-east1 region goes down, be able to run the database in another region within minutes and lose very little data.
- **The limits:** Recovery must take minutes, not hours, with minimal data loss.
- **What they're really asking:** How do you keep a near-live copy of a Cloud SQL database in another region?

**Clues in the question:**
- "**HA within the region**" covers zones, not regions.
- "**another region within minutes … minimal data loss**": a **cross-region read replica** (continuously replicated) that you **promote**.

**Exam topic:** Data redundancy (exam guide section 2.2).

---

## 📚 Key Terms Explained

### 1. Cloud SQL high availability (HA)
- **What it is:** A primary plus a standby in **another zone of the same region**, with automatic failover.
- **Looks like:** Primary `us-east1-b`, standby `us-east1-c`
- **Not to be confused with:** Cross-region DR.
- **Analogy:** 🏢 A backup office on another floor of the same building.
- **In the online store:** ShopNow orders DB today.

### 2. Cross-region read replica 🔑
- **What it is:** A read-only copy of a Cloud SQL instance in another region, kept up to date by asynchronous replication. You can **promote** it to a standalone primary during a regional disaster. (Enterprise Plus also offers managed DR replica switchover.)
- **Looks like:** `gcloud sql instances create orders-replica-west --master-instance-name=orders-db --region=us-west1` → disaster: `gcloud sql instances promote-replica orders-replica-west`
- **Not to be confused with:** A backup or export file, which takes longer to restore and loses more data.
- **Analogy:** 🏙️ A live copy of the records in another city's office.
- **In the online store:** Orders DB copy in us-west1.

### 🔗 How they fit together
```
 us-east1: orders-db (HA primary+standby) ──async replication──► us-west1: orders-replica-west
 Region down → promote replica → apps point to us-west1 ✅
```

---

## 🌍 Real-World Scenario

After a cloud region outage elsewhere made the news, a store's board asks for regional DR. A **cross-region replica** in us-west1 keeps a near-live copy, and a tested runbook promotes it and switches the app's connection in under 15 minutes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Take a daily export of the database to a Cloud Storage bucket in us-east1.

**Wrong words:**
- ❌ "**daily export … in us-east1**": up to a day of data loss, slow restore, and the backup sits in the same failed region.

📌 **When to use it:** Use exports for long-term archives or moving data.
🏢 **Office example:** Photocopying records daily but keeping the copies in the same building.

### ✅ B
> **B.** Create a cross-region read replica in another region, such as us-west1, and promote it if us-east1 fails.

**Why it's correct:**
- ✔️ "**cross-region read replica in another region**" matches "**recovered in another region**" and "**minimal data loss**": it's continuously replicated.
- ✔️ "**promote it if us-east1 fails**" matches "**within minutes**".

📌 **When to use it:** Use it when the database must survive a whole region going down.
🏢 **Office example:** Keeping a live copy of the records in another city's office, ready to take over.

### ❌ C
> **C.** Add a second zone to the existing high-availability configuration.

**Wrong words:**
- ❌ "**second zone**": HA already uses zones in one region. A full region outage takes them all.

📌 **When to use it:** Use HA for zone failures.
🏢 **Office example:** Another floor of the same building.

### ❌ D
> **D.** Increase the instance's machine type and storage.

**Wrong words:**
- ❌ "**machine type and storage**": more capacity, still one region.

📌 **When to use it:** Use it when the database is too slow or full.
🏢 **Office example:** A bigger office in the same building.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: `orders-db` (us-east1, HA) → replica `orders-replica-west` (us-west1). Runbook: promote → update the Secret Manager `DB_HOST` → redeploy Cloud Run in us-west1.

---

## 🧠 Key Takeaways / Memory Tips

- **Zone failure → Cloud SQL HA. Region failure → cross-region read replica + promote.**
  🧠 *"**HA = floors; replica = cities.**"*
- Related: **Q003**, **Q188**, **Q217**.

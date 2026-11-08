# G032: Real-Time Notification When Any Firewall Rule Changes Anywhere in the Organization (Cloud Asset Inventory Feed)

**Topic:** Security (Cloud Asset Inventory feeds)
**Exam guide section:** 1.1 Setting up projects: Configuring Cloud Asset Inventory

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your security team wants to be notified in near real time whenever a firewall rule is created, modified, or deleted in any project in your organization, so that an automated function can review the change. What should you do?
>
> **A.** Create an uptime check for each VPC network.
>
> **B.** Export Cloud Asset Inventory to BigQuery once a month and compare snapshots.
>
> **C.** Ask each project owner to email the security team when they change firewall rules.
>
> **D.** Create a Cloud Asset Inventory feed at the organization level for the compute.googleapis.com/Firewall asset type that publishes changes to a Pub/Sub topic, and trigger a function from that topic.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company has many projects, each with its own firewall rules.
- **What you must achieve:** Find out within moments whenever any firewall rule is created, changed or deleted, anywhere in the organization, and let an automatic function check it.
- **The limits:** It must cover every project and be near real time.
- **What they're really asking:** Which Google Cloud feature streams resource changes across the organization?

**Clues in the question:**
- "**notified in near real time**" + "**any project in your organization**": a Cloud Asset Inventory **feed** at the org level.
- "**automated function can review**": the feed publishes to **Pub/Sub**, which can trigger a function.

**Exam topic:** Resource management and security (exam guide sections 1.1 and 4).

---

## 📚 Key Terms Explained

### 1. Cloud Asset Inventory 🔑
- **What it is:** A service that keeps an inventory and history of your Google Cloud resources and IAM policies. You can search it, export it (to Cloud Storage or BigQuery), or create **feeds** that stream changes to Pub/Sub.
- **Looks like:** `gcloud asset feeds create fw-changes --organization=123456 --asset-types=compute.googleapis.com/Firewall --content-type=resource --pubsub-topic=projects/sec/topics/fw-changes`
- **Not to be confused with:** Cloud Logging audit logs. Those are related, but feeds give structured resource states across the org.
- **Analogy:** 📒 The building's master inventory with a bell that rings whenever anything changes.
- **In the online store:** Alerts on any firewall change in the ShopNow org.

### 2. Pub/Sub topic
- **What it is:** A message channel. Publishers send messages and subscribers (like a function) receive them.
- **Looks like:** `projects/sec/topics/fw-changes`
- **Not to be confused with:** A database.
- **Analogy:** 📮 A mailbox that triggers a helper when a letter arrives.
- **In the online store:** Triggers the `review-fw-change` function.

### 🔗 How they fit together
```
 Any project firewall change ─► Asset Inventory feed (org, Firewall type) ─► Pub/Sub fw-changes
                                                                              └─► Cloud Run function: review ✅
```

---

## 🌍 Real-World Scenario

A developer once opened SSH to the whole internet by mistake. Now an org-level **Asset Inventory feed** streams every firewall change to Pub/Sub, and a function flags any rule with `0.0.0.0/0` within a minute.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an uptime check for each VPC network.

**Wrong words:**
- ❌ "**uptime check for each VPC network**": uptime checks test whether an endpoint responds. They don't track configuration changes.

📌 **When to use it:** Use uptime checks for website availability.
🏢 **Office example:** Testing that the doors open, not who changed the locks.

### ❌ B
> **B.** Export Cloud Asset Inventory to BigQuery once a month and compare snapshots.

**Wrong words:**
- ❌ "**once a month**": not near real time. A bad rule could stay open for weeks.

📌 **When to use it:** Use BigQuery exports for periodic analysis and reports.
🏢 **Office example:** Checking the lock inventory once a month.

### ❌ C
> **C.** Ask each project owner to email the security team when they change firewall rules.

**Wrong words:**
- ❌ "**Ask each project owner to email**": manual, unreliable and unenforced.

📌 **When to use it:** Never rely on email for security change tracking.
🏢 **Office example:** Hoping every office remembers to report lock changes.

### ✅ D
> **D.** Create a Cloud Asset Inventory feed at the organization level for the compute.googleapis.com/Firewall asset type that publishes changes to a Pub/Sub topic, and trigger a function from that topic.

**Why it's correct:**
- ✔️ "**Cloud Asset Inventory feed at the organization level**" matches "**any project in your organization**".
- ✔️ "**publishes changes to a Pub/Sub topic**" matches "**near real time**".
- ✔️ "**trigger a function from that topic**" matches "**automated function can review the change**".

📌 **When to use it:** Use it when you want to be told right away whenever a certain kind of setting changes anywhere in the company.
🏢 **Office example:** A bell that rings at the security desk whenever any office changes its door lock.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** org: feed `fw-changes` → topic `fw-changes` → Cloud Run function `review-fw` posts to #security if a rule allows `0.0.0.0/0` on 22 or 3389.

---

## 🧠 Key Takeaways / Memory Tips

- **Near-real-time resource changes across the org → Cloud Asset Inventory feed → Pub/Sub.**
  🧠 *"**Asset feed = change doorbell.**"*
- Related: **Q340**, **Q348**, **G033**.

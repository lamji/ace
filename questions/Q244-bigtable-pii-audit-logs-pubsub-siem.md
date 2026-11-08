# Q244: Log All Reads, Writes and Metadata Reads on Bigtable to a SIEM (Data Read/Write + Admin Read Logs, Sink to Pub/Sub)

**Topic:** Logging (audit log types, sinks to Pub/Sub)

## ❓ Question
> You have a Bigtable instance that consists of three nodes that store personally identifiable information (PII) data. You need to log all read or write operations, including any metadata or configuration reads of this database table, in your company's Security Information and Event Management (SIEM) system. What should you do?
>
> **A.** • Navigate to Cloud Monitoring in the Google Cloud console, and create a custom monitoring job for the Bigtable instance to track all changes. • Create an alert by using webhook endpoints, with the SIEM endpoint as a receiver.
>
> **B.** • Navigate to the Audit Logs page in the Google Cloud console, and enable Admin Write logs for the Bigtable instance. • Create a Cloud Functions instance to export logs from Cloud Logging to your SIEM.
>
> **C.** • Navigate to the Audit Logs page in the Google Cloud console, and enable Data Read, Data Write and Admin Read logs for the Bigtable instance. • Create a Pub/Sub topic as a Cloud Logging sink destination, and add your SIEM as a subscriber to the topic.
>
> **D.** • Install the Ops Agent on the Bigtable instance during configuration. • Create a service account with read permissions for the Bigtable instance. • Create a custom Dataflow job with this service account to export logs to the company's SIEM system.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A three-node Bigtable instance stores personal data (PII). Your company's SIEM (a security tool that collects logs) must receive the logs.
- **What you must achieve:** Log every read and write, including metadata and configuration reads, and send them to the SIEM.
- **The limits:** Nothing may be missed.
- **What they're really asking:** Which logs must be turned on, and how do they reach the SIEM?

**Clues in the question:**
- "**read or write operations**" → **Data Read** + **Data Write** logs.
- "**metadata or configuration reads**" → **Admin Read** logs (all three are Data Access logs, off by default).
- "**in your company's SIEM**" → a **log sink to Pub/Sub**, SIEM subscribes.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Data Access log types 🔑
- **What it is:** **Admin Read** (reads of config/metadata), **Data Read**, **Data Write**. All off by default. (Admin **Write** = Admin Activity, always on.)
- **Looks like:** IAM & Admin → Audit Logs → Cloud Bigtable → ☑ Admin Read ☑ Data Read ☑ Data Write
- **Not to be confused with:** Admin Activity.
- **Analogy:** 📄 Logbooks for who looked at settings, read files, or changed files.
- **In the online store:** PII table access.

### 2. Log sink → Pub/Sub
- **What it is:** Routes matching logs to a Pub/Sub topic in near real time for outside tools.
- **Looks like:** `gcloud logging sinks create siem pubsub.googleapis.com/projects/p/topics/siem --log-filter='resource.type="bigtable_instance"'`
- **Not to be confused with:** —
- **Analogy:** 📬 A mail chute to the security office.
- **In the online store:** —

### 🔗 How they fit together
```
 Bigtable audit logs (Admin Read, Data Read, Data Write) → sink → Pub/Sub → SIEM ✅
```

---

## 🌍 Real-World Scenario

A company stores PII in Bigtable. Security enables **Admin Read, Data Read, Data Write** logs and routes them through a **sink to Pub/Sub**, which their SIEM subscribes to.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** • Navigate to Cloud Monitoring in the Google Cloud console, and create a custom monitoring job for the Bigtable instance to track all changes. • Create an alert by using webhook endpoints, with the SIEM endpoint as a receiver.

**Wrong words:**
- ❌ "**Cloud Monitoring … custom monitoring job**": Monitoring tracks metrics, not who read which data.

📌 **When to use it:** Use Monitoring for performance and alerts on numbers.
🏢 **Office example:** Watching the electricity meter to see who opened files.

### ❌ B
> **B.** • Navigate to the Audit Logs page in the Google Cloud console, and enable Admin Write logs for the Bigtable instance. • Create a Cloud Functions instance to export logs from Cloud Logging to your SIEM.

**Wrong words:**
- ❌ "**enable Admin Write logs**": those are already on and only cover config **changes**, not reads/writes of data.
- ❌ "**Cloud Functions … to export logs**": custom code instead of a sink.

📌 **When to use it:** Use Admin Activity logs for "who changed settings".
🏢 **Office example:** Logging only lock changes, not who opened the files.

### ✅ C
> **C.** • Navigate to the Audit Logs page in the Google Cloud console, and enable Data Read, Data Write and Admin Read logs for the Bigtable instance. • Create a Pub/Sub topic as a Cloud Logging sink destination, and add your SIEM as a subscriber to the topic.

**Why it's correct:**
- ✔️ "**enable Data Read, Data Write**" matches "**log all read or write operations**".
- ✔️ "**and Admin Read logs**" matches "**including any metadata or configuration reads**".
- ✔️ "**Pub/Sub topic as a Cloud Logging sink destination, and add your SIEM as a subscriber**" matches "**in your company's SIEM system**".

📌 **When to use it:** Use it when every look and change at sensitive records must reach the security team's system.
🏢 **Office example:** Turning on all three logbooks and sending each new entry down a chute to the security office.

### ❌ D
> **D.** • Install the Ops Agent on the Bigtable instance during configuration. • Create a service account with read permissions for the Bigtable instance. • Create a custom Dataflow job with this service account to export logs to the company's SIEM system.

**Wrong words:**
- ❌ "**Install the Ops Agent on the Bigtable instance**": Bigtable is managed; you can't install agents on it.
- ❌ "**custom Dataflow job**": unnecessary.

📌 **When to use it:** Use the Ops Agent on your own VMs.
🏢 **Office example:** Installing a camera inside a bank's vault you don't own.

---

## 🛒 E-Commerce Full-Stack Example

Enable Bigtable audit logs (Admin Read, Data Read, Data Write) → sink `bt-pii-siem` → Pub/Sub `siem-feed` → SIEM subscription.

---

## 🧠 Key Takeaways / Memory Tips

- **Reads/writes → Data Read/Write. Metadata reads → Admin Read. To a SIEM → sink to Pub/Sub.**
  🧠 *"**Three logbooks, one chute.**"*
- Related: **Q155**, **Q169**, **Q287**.

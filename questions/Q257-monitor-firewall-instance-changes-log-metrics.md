# Q257: Simply Monitor Unexpected Firewall Changes and Instance Creation (Log-Based Metrics + Alerts)

**Topic:** Monitoring (log-based metrics on audit logs)

## ❓ Question
> After a recent security incident, your startup company wants better insight into what is happening in the Google Cloud environment. You need to monitor unexpected firewall changes and instance creation. Your company prefers simple solutions. What should you do?
>
> **A.** Create a log sink to forward Cloud Audit Logs filtered for firewalls and compute instances to Cloud Storage. Use BigQuery to periodically analyze log events in the storage bucket.
>
> **B.** Use Cloud Logging filters to create log-based metrics for firewall and instance actions. Monitor the changes and set up reasonable alerts.
>
> **C.** Install Kibana on a compute instance. Create a log sink to forward Cloud Audit Logs filtered for firewalls and compute instances to Pub/Sub. Target the Pub/Sub topic to push messages to the Kibana instance. Analyze the logs on Kibana in real time.
>
> **D.** Turn on Google Cloud firewall rules logging, and set up alerts for any insert, update, or delete events.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** After a security incident, your startup wants better visibility of what happens in Google Cloud.
- **What you must achieve:** Monitor unexpected firewall changes and VM creation.
- **The limits:** Keep it simple.
- **What they're really asking:** How do you get alerts for firewall changes and new VMs?

**Clues in the question:**
- Firewall changes and VM creation are in **Admin Activity audit logs** (always on).
- "**simple**" → **log-based metrics + alerts**, all built in.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Log-based metric on audit logs 🔑 (review from Q172)
- **What it is:** Counts matching audit log entries, e.g. `methodName:"compute.firewalls.insert"`.
- **Looks like:** filter `protoPayload.methodName=~"compute.firewalls.(insert|patch|delete)"`
- **Not to be confused with:** firewall rules logging.
- **Analogy:** 🧮 A tally of lock changes.
- **In the online store:** Alert on firewall edits.

### 2. Firewall rules logging
- **What it is:** Logs **connections** allowed/denied by a rule, not changes to the rule.
- **Looks like:** `--enable-logging`
- **Not to be confused with:** audit logs.
- **Analogy:** 🚪 Door-swipe log vs lock-change log.
- **In the online store:** —

### 🔗 How they fit together
```
 Admin Activity logs → log-based metrics (firewall changes, instance inserts) → alerts ✅
```

---

## 🌍 Real-World Scenario

After an incident, a startup creates **log-based metrics** for `compute.firewalls.*` and `compute.instances.insert` and alerts the team on any change.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a log sink to forward Cloud Audit Logs filtered for firewalls and compute instances to Cloud Storage. Use BigQuery to periodically analyze log events in the storage bucket.

**Wrong words:**
- ❌ "**sink … to Cloud Storage … periodically analyze**": not real-time and not simple.

📌 **When to use it:** Use it for long-term log archives.
🏢 **Office example:** Reading old logbooks once a week.

### ✅ B
> **B.** Use Cloud Logging filters to create log-based metrics for firewall and instance actions. Monitor the changes and set up reasonable alerts.

**Why it's correct:**
- ✔️ "**log-based metrics for firewall and instance actions**" matches "**monitor unexpected firewall changes and instance creation**".
- ✔️ "**set up reasonable alerts**" + built-in tools match "**prefers simple solutions**".

📌 **When to use it:** Use it when you want to be told whenever certain important changes happen.
🏢 **Office example:** A tally clicker for lock changes and new desks, wired to the manager's phone.

### ❌ C
> **C.** Install Kibana on a compute instance. Create a log sink to forward Cloud Audit Logs filtered for firewalls and compute instances to Pub/Sub. Target the Pub/Sub topic to push messages to the Kibana instance. Analyze the logs on Kibana in real time.

**Wrong words:**
- ❌ "**Install Kibana … Pub/Sub … push**": extra software and VMs to run; not simple.

📌 **When to use it:** Use it if you already standardize on Elastic tools.
🏢 **Office example:** Building your own security office.

### ❌ D
> **D.** Turn on Google Cloud firewall rules logging, and set up alerts for any insert, update, or delete events.

**Wrong words:**
- ❌ "**firewall rules logging**": logs traffic hitting rules, not **changes** to rules, and doesn't cover instance creation.

📌 **When to use it:** Use it to see which connections a rule allowed or blocked.
🏢 **Office example:** Reading the door-swipe log to find who changed the lock.

---

## 🛒 E-Commerce Full-Stack Example

Metric `fw_changes` (methodName =~ compute.firewalls.(insert|patch|delete)) and `vm_creates` (compute.instances.insert) → alert to #security.

---

## 🧠 Key Takeaways / Memory Tips

- **Watch config changes simply → log-based metrics on audit logs + alerts.**
  🧠 *"**Changes are in audit logs; count and alert.**"*
- Related: **Q172**, **Q244**.

# Q231: Diagnosing an App That Writes Logs to Disk (Install the Ops Agent, View in Cloud Logging)

**Topic:** Logging (Ops Agent)

## ❓ Question
> You have deployed an application on a single Compute Engine instance. The application writes logs to disk. Users start reporting errors with the application. You want to diagnose the problem. What should you do?
>
> **A.** Navigate to Cloud Logging and view the application logs.
>
> **B.** Configure a health check on the instance and set a "consecutive successes" Healthy threshold value of 1.
>
> **C.** Connect to the instance's serial console and read the application logs.
>
> **D.** Install and configure the Ops agent and view the logs from Cloud Logging.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Same as Q132, with the newer **Ops Agent**.

**Clues in the question:**
- "**writes logs to disk**" → those files aren't in Cloud Logging until an **agent** ships them → **Ops Agent**.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Ops Agent 🔑
- **What it is:** Google's current agent that sends a VM's **log files and metrics** to Cloud Logging and Monitoring (replaces the old Logging/Monitoring agents).
- **Looks like:** `sudo bash add-google-cloud-ops-agent-repo.sh --also-install`
- **Not to be confused with:** Cloud Logging itself.
- **Analogy:** 📬 A courier carrying the desk notebook to the records office.
- **In the online store:** Checkout VM logs.

### 🔗 How they fit together
```
 /var/log/app.log ─ Ops Agent ─► Cloud Logging ✅ (search, filter)
```

---

## 🌍 Real-World Scenario

Users report errors. The engineer installs the **Ops Agent**, configures it to read `/var/log/myapp/*.log`, and searches the errors in Cloud Logging.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Navigate to Cloud Logging and view the application logs.

**Wrong words:**
- ❌ "**Navigate to Cloud Logging and view the application logs**": the app logs aren't there yet without an agent.

📌 **When to use it:** Use it once logs are being sent (e.g. Cloud Run, GKE, or a VM with the agent).
🏢 **Office example:** Looking in the records office for a notebook still on someone's desk.

### ❌ B
> **B.** Configure a health check on the instance and set a "consecutive successes" Healthy threshold value of 1.

**Wrong words:**
- ❌ "**health check … Healthy threshold value of 1**": checks if the VM responds; doesn't show why the app errors.

📌 **When to use it:** Use health checks for load balancing and autohealing.
🏢 **Office example:** Checking the employee is at their desk instead of reading their notes.

### ❌ C
> **C.** Connect to the instance's serial console and read the application logs.

**Wrong words:**
- ❌ "**serial console**": shows boot/system output, an emergency tool, not app log files.

📌 **When to use it:** Use it when a VM won't boot or SSH fails.
🏢 **Office example:** Using the emergency intercom to read someone's notebook.

### ✅ D
> **D.** Install and configure the Ops agent and view the logs from Cloud Logging.

**Why it's correct:**
- ✔️ "**Install and configure the Ops agent**" matches "**The application writes logs to disk**": the agent ships those files.
- ✔️ "**view the logs from Cloud Logging**" matches "**diagnose the problem**".

📌 **When to use it:** Use it when a program keeps its notes on its own machine and you want to search them centrally.
🏢 **Office example:** A courier who brings each desk's notebook to the central records office.

---

## 🛒 E-Commerce Full-Stack Example

Ops Agent config `/etc/google-cloud-ops-agent/config.yaml` receiver `files` include `/var/log/shopnow/*.log`.

---

## 🧠 Key Takeaways / Memory Tips

- **Logs on a VM's disk → install the Ops Agent → Cloud Logging.**
  🧠 *"**Disk logs need a courier.**"*
- Related: **Q132**, **Q172**.

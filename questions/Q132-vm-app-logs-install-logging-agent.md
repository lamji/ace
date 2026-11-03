# Q132: Diagnosing an App That Writes Logs to Disk (Install the Logging Agent, View in Cloud Logging)

**Topic:** Logging (Ops Agent / Logging agent, serial console, health checks)

## ❓ Question
> You have deployed an application on a single Compute Engine instance. The application writes logs to disk. Users start reporting errors with the application. You want to diagnose the problem. What should you do?
>
> **A.** Navigate to Cloud Logging and view the application logs.
>
> **B.** Connect to the instance's serial console and read the application logs.
>
> **C.** Configure a Health Check on the instance and set a Low Healthy Threshold value.
>
> **D.** Install and configure the Cloud Logging Agent and view the logs from Cloud Logging.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The app writes logs to **files on the VM's disk**. Users see errors. How do you look at those logs the Google way?

**Clues in the question:**
- "**writes logs to disk**": Cloud Logging **doesn't** see files on a VM's disk by itself. You need the **agent** (today: Ops Agent) to send them.
- "**diagnose the problem**": then you can search the logs in Cloud Logging.

**Exam topic:** Logging.

---

## 📚 Key Terms Explained

### 1. Logging agent / Ops Agent 🔑
- **What it is:** A **program installed on the VM** that reads log files (like `/var/log/myapp.log`) and sends them to Cloud Logging.
- **Looks like:** `curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh && sudo bash add-google-cloud-ops-agent-repo.sh --also-install`
- **Not to be confused with:** Cloud Logging itself.
- **Analogy:** 📬 A **courier** who carries the desk's notebook to the central records office.
- **In the online store:** Ships the checkout VM's app logs.

### 2. Serial console
- **What it is:** A text console for **boot and system messages**, used when the VM won't boot or SSH fails.
- **Looks like:** `gcloud compute connect-to-serial-port vm-1`
- **Not to be confused with:** a log viewer for app files.
- **Analogy:** 🛠️ The building's emergency intercom.
- **In the online store:** Debugging a VM that won't boot.

### 🔗 How they fit together
```
 app → /var/log/app.log (disk) ──Ops/Logging agent──► Cloud Logging ✅ search & filter
 (without the agent, Cloud Logging never sees the file)
```

---

## 🌍 Real-World Scenario

An app on one VM writes to `/var/log/app/error.log`. The team installs the **Ops Agent**, configures it to collect that file, and searches Cloud Logging for the error. They also keep the logs for later.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Navigate to Cloud Logging and view the application logs.

**Wrong words:**
- ❌ "**Navigate to Cloud Logging and view the application logs**": the app logs are only on the disk. Without an agent, they aren't in Cloud Logging.

📌 **When to use it:** Use it when the logs are already sent to Cloud Logging (for example, Cloud Run or GKE).
🏢 **Office example:** Looking in the central records office for a notebook that's still on someone's desk.

### ❌ B
> **B.** Connect to the instance's serial console and read the application logs.

**Wrong words:**
- ❌ "**serial console and read the application logs**": the serial console shows boot and system output, not your app's log files. It's for emergencies.

📌 **When to use it:** Use it when a VM won't boot or you can't SSH in.
🏢 **Office example:** Using the emergency intercom to read someone's notebook.

### ❌ C
> **C.** Configure a Health Check on the instance and set a Low Healthy Threshold value.

**Wrong words:**
- ❌ "**Configure a Health Check**": it tells you whether the app is up, not **why** errors happen.

📌 **When to use it:** Use health checks so load balancers and MIGs can detect broken VMs.
🏢 **Office example:** Checking whether a worker is at their desk, not what went wrong.

### ✅ D
> **D.** Install and configure the Cloud Logging Agent and view the logs from Cloud Logging.

**Why it's correct:**
- ✔️ "**Install and configure the Cloud Logging Agent**" matches "**The application writes logs to disk**": the agent sends those files to Cloud Logging.
- ✔️ "**view the logs from Cloud Logging**" matches "**diagnose the problem**": you search and filter the errors there.

📌 **When to use it:** Use it when a machine keeps its records locally and you want them in one searchable place.
🏢 **Office example:** Sending a courier to bring each desk's notebook to the central records office.

---

## 🛒 E-Commerce Full-Stack Example

```yaml
# /etc/google-cloud-ops-agent/config.yaml on checkout-1
logging:
  receivers:
    checkout_app: {type: files, include_paths: [/var/log/checkout/*.log]}
  service:
    pipelines:
      checkout: {receivers: [checkout_app]}
```
In Logs Explorer: `log_name:"checkout_app" "PaymentError"`, which shows 312 errors since 14:02.

---

## 🧠 Key Takeaways / Memory Tips

- **App logs on a VM's disk → install the Ops/Logging agent**, then use Cloud Logging.
- Serial console = boot problems.
  🧠 *"**Logs on disk? Send the agent.**"*
- Related: **Q123** (Monitoring alerts), **Q068** (log sinks).

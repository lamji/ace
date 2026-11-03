# Q055: Stopping Expensive Logs From One Dev GKE Container (Logs Ingestion / Exclusion)

**Topic:** Cloud Logging (log ingestion costs, excluding a log source, GKE container vs cluster operations logs, legacy Stackdriver options)

## ❓ Question
> Your projects incurred more costs than you expected last month. Your research reveals that a development GKE container emitted a huge number of logs, which resulted in higher costs. You want to disable the logs quickly using the minimum number of steps. What should you do?
>
> **A.** 1. Go to the Logs ingestion window in Stackdriver Logging, and disable the log source for the GKE container resource.
>
> **B.** 1. Go to the Logs ingestion window in Stackdriver Logging, and disable the log source for the GKE Cluster Operations resource.
>
> **C.** 1. Go to the GKE console, and delete existing clusters. 2. Recreate a new cluster. 3. Clear the option to enable legacy Stackdriver Logging.
>
> **D.** 1. Go to the GKE console, and delete existing clusters. 2. Recreate a new cluster. 3. Clear the option to enable legacy Stackdriver Monitoring.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** One **development container** in GKE wrote **tons of logs**, and you're paying for storing them. Stop those logs **quickly**, in the **fewest steps**.

| Keyword | What it hints at |
|---|---|
| "**GKE container emitted**" | The noisy source is the **container** logs (your app's output), not the cluster's own operations |
| "**higher costs**" | Cloud Logging charges for logs **ingested** (stored). Stop them **before** they're stored |
| "**quickly**" + "**minimum number of steps**" | One setting in Logging, **not** deleting and rebuilding clusters |

**Exam topic:** Cloud Logging / cost control.

> ⚠️ **Name update:** "Logs ingestion window in Stackdriver Logging" is the **old** screen. Today you do the same thing in **Cloud Logging → Log Router**, by adding an **exclusion filter** (for example `resource.type="k8s_container"`) to the `_Default` sink. Same idea: stop the noisy source from being stored.

---

## 📚 Key Terms Explained

### 1️⃣ Log Ingestion (and why it costs money) 🔑
- **What it is:** **Ingestion** = Cloud Logging **receiving and storing** a log entry. You pay per GB ingested (beyond the free amount). **Excluded** logs aren't stored, so they **cost nothing** to store.
- **Looks like:** "Logs ingested this month: 4.2 TiB" on the Logging usage page
- **Not to be confused with:** the app **writing** logs. The container can keep printing, but Logging simply **drops** the excluded ones.
- **Analogy:** 🗄️ The **records room charges per box** you file. An exclusion = telling the clerk "**don't file anything from the test lab**".
- **In the online store:** A debug line printed on every product view filled up the bill.

### 2️⃣ GKE Container logs (`k8s_container`)
- **What it is:** The **output of your apps** running in the pods (`stdout`/`stderr`): "user added to cart", stack traces, debug lines.
- **Looks like:** `resource.type="k8s_container" resource.labels.container_name="recommender-dev"`
- **Not to be confused with:** cluster operations logs (next term).
- **Analogy:** 📢 What **each employee says out loud** at their desk.

### 3️⃣ GKE Cluster Operations logs (`gke_cluster`)
- **What it is:** Logs about the **cluster itself**: creating node pools, upgrades, resizing. Usually **small**.
- **Looks like:** `resource.type="gke_cluster" … "Upgrading node pool default-pool"`
- **Not to be confused with:** the container's app logs. Disabling these **wouldn't stop** the noisy container.
- **Analogy:** 🏗️ The **building manager's logbook** (renovations, elevator repairs), not the employees' chatter.

### 4️⃣ Legacy Stackdriver Logging / Monitoring (cluster options)
- **What it is:** Old **checkboxes on a GKE cluster** that turn the whole cluster's logging or monitoring integration on or off.
- **Not to be confused with:** a quick fix. Changing them as described here means **deleting and recreating clusters**, which is slow and risky.
- **Analogy:** 🏢 **Demolishing the building** to stop one noisy employee.

### 🔗 How They Fit Together
```
🐳 dev container "recommender-dev"  ──prints 10,000 lines/sec──►  📜 Cloud Logging
                                                                   │
                                      Log Router / Logs ingestion  │  exclusion:
                                      resource.type="k8s_container"│  container=recommender-dev
                                                                   ▼
                                                          🗑️ dropped (not stored, not billed) ✅
🏗️ gke_cluster operations logs (small) ───────────────────────────► stored as usual
```

---

## 🌍 Real-World Scenario

A developer leaves **debug logging** turned on in a dev service, and it logs every request in detail. At the end of the month, finance asks why the Logging bill tripled. The quick fix is to **exclude that source** in Cloud Logging so new entries aren't stored. Later, the developer **lowers the log level** in the code, and the team sets a **budget alert** so it's caught sooner next time.

---

## 🔍 Option-by-Option Breakdown

### ✅ A (your answer)
> **A.** 1. Go to the Logs ingestion window in Stackdriver Logging, and disable the log source for the GKE container resource.

**Why it's correct:**
- ✔️ "**Logs ingestion window**": the place that controls **what gets stored** (and billed).
- ✔️ "**GKE container resource**": exactly the noisy source.
- ✔️ **One step**, instant, nothing deleted.

**📌 When to use it:** Use it when one source is writing far too many logs and you want to stop paying for them right away.
🏢 **Office example:** Telling the records clerk "stop filing the test lab's printouts" instead of renovating the office.

### ❌ B
> **B.** 1. Go to the Logs ingestion window in Stackdriver Logging, and disable the log source for the GKE Cluster Operations resource.

**Wrong words:**
- ✔️ "Go to the Logs ingestion window in Stackdriver Logging" is the right place.
- ❌ "**GKE Cluster Operations resource**": that's the cluster's **own small logbook** (upgrades, resizes), not the noisy **container**. The container keeps filling the bill.

**📌 When to use it:** Use it only if the cluster's own operation messages are what you want to stop storing (rare).
🏢 **Office example:** Telling the clerk to stop filing the building manager's repair notes, while the noisy employee's printouts keep piling up.

### ❌ C
> **C.** 1. Go to the GKE console, and delete existing clusters. 2. Recreate a new cluster. 3. Clear the option to enable legacy Stackdriver Logging.

**Wrong words:**
- ❌ "**delete existing clusters**" + "**Recreate a new cluster**": slow, risky, and many steps. It breaks "quickly" and "minimum number of steps".
- ❌ "**Clear the option to enable legacy Stackdriver Logging**": turns off logging for the **whole** cluster, not just the noisy container.

**📌 When to use it:** **Never use this** to stop one noisy source. Exclude that source in Logging (A).
🏢 **Office example:** Demolishing and rebuilding the office to stop one employee from printing too much.

### ❌ D
> **D.** 1. Go to the GKE console, and delete existing clusters. 2. Recreate a new cluster. 3. Clear the option to enable legacy Stackdriver Monitoring.

**Wrong words:**
- ❌ "**delete existing clusters**" + "**Recreate a new cluster**": same slow, risky rebuild as C.
- ❌ "**Stackdriver Monitoring**": monitoring is **metrics** (CPU, memory charts), not **logs**. Logs would still flow.

**📌 When to use it:** **Never use this** for a log-cost problem. It doesn't even touch logs. Use A.
🏢 **Office example:** Rebuilding the office and switching off the temperature sensors, while the noisy printouts keep coming.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's dev cluster runs `recommender-dev`, which logs every product it scores, about **3 TB last month**.

**Today's way (Log Router exclusion):**
```bash
gcloud logging sinks update _Default \
  --add-exclusion=name=drop-recommender-dev,filter='resource.type="k8s_container" AND resource.labels.container_name="recommender-dev"'
```

| Logs | Before | After |
|---|---|---|
| `recommender-dev` container | 3 TB/month stored 💸 | **0**, dropped at ingestion ✅ |
| Checkout and API containers | stored | still stored ✅ |
| Cluster operations (`gke_cluster`) | stored | still stored ✅ |

**Follow-up:** the developer changes `LOG_LEVEL=debug` → `LOG_LEVEL=warning`, and a **budget alert** is added.

---

## 🧠 Key Takeaways / Memory Tips

- **Too many logs from one source → exclude that source at ingestion** (old: Logs ingestion window; today: **Log Router exclusion filter**).
  🧠 *"**Stop the noisy source, don't demolish the building.**"*
- **Container logs** = your app's output (big). **Cluster operations** = the cluster's own events (small).
- **Monitoring = metrics, Logging = logs.** Don't mix them up.
- Deleting and recreating clusters is never "quick" or "minimum steps".
- Related: **Q027** (Cloud Logging = old "Stackdriver log"), **Q017** (billing export / cost tracking).

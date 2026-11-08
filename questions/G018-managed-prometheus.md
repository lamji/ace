# G018: Stop Running Your Own Prometheus Server but Keep PromQL and Grafana (Managed Service for Prometheus)

**Topic:** Monitoring (Managed Service for Prometheus)
**Exam guide section:** 3.4 Monitoring and logging: Deploying Google Cloud Managed Service for Prometheus

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your team runs a self-managed Prometheus server on a GKE cluster to collect application metrics. The server often runs out of storage and requires constant maintenance. The team wants to keep using PromQL queries and existing Grafana dashboards, but have Google manage metric storage and scaling. What should you do?
>
> **A.** Use Google Cloud Managed Service for Prometheus with managed collection, define PodMonitoring resources for the applications, and point Grafana at the Prometheus-compatible query endpoint.
>
> **B.** Export the metrics to a Cloud Storage bucket every hour, and query them with BigQuery.
>
> **C.** Increase the size of the Prometheus server's Persistent Disk.
>
> **D.** Install the Ops Agent on every GKE node, and rebuild the dashboards without PromQL.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team runs its own Prometheus (a popular open-source metrics collector) inside Kubernetes. It keeps filling its disk and needs constant care.
- **What you must achieve:** Hand metric storage and scaling to Google.
- **The limits:** Keep the same PromQL queries (Prometheus's query language) and the same Grafana dashboards (a chart tool).
- **What they're really asking:** Which Google service is a managed Prometheus that still speaks PromQL?

**Clues in the question:**
- "**self-managed Prometheus … constant maintenance**" + "**Google manage metric storage and scaling**": **Managed Service for Prometheus** (data stored in Cloud Monitoring).
- "**keep using PromQL … Grafana**": it supports PromQL and Grafana through a Prometheus-compatible API.

**Exam topic:** Monitoring (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Prometheus / PromQL
- **What it is:** Prometheus collects ("scrapes") metrics from apps. PromQL is its query language.
- **Looks like:** `rate(http_requests_total{job="checkout"}[5m])`
- **Not to be confused with:** Cloud Logging (logs, not metrics).
- **Analogy:** 🌡️ Thermometers in every room, plus the language for asking about them.
- **In the online store:** Checkout request rate.

### 2. Managed Service for Prometheus 🔑
- **What it is:** Google Cloud's fully managed Prometheus. **Managed collection** runs collectors in GKE (on by default in newer clusters), you choose what to scrape with **PodMonitoring** resources, data lives in Cloud Monitoring's global store, and you query with PromQL in Cloud Monitoring or Grafana.
- **Looks like:** `apiVersion: monitoring.googleapis.com/v1\nkind: PodMonitoring\nspec: {selector: {matchLabels: {app: checkout}}, endpoints: [{port: metrics}]}`
- **Not to be confused with:** The Ops Agent, which collects system metrics and logs from VMs.
- **Analogy:** 🏢 Handing the thermometer records to a professional records office that never runs out of shelves.
- **In the online store:** Checkout and cart metrics in managed storage.

### 🔗 How they fit together
```
 Pods (/metrics) ◄─scrape─ managed collectors (GKE) ─► Cloud Monitoring (Monarch store)
 Grafana / Cloud Monitoring ─PromQL─► query ✅
```

---

## 🌍 Real-World Scenario

An online store's self-run Prometheus crashed during Black Friday when its disk filled up. Moving to **Managed Service for Prometheus** keeps every PromQL dashboard, removes the server to babysit, and keeps metrics for 24 months.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use Google Cloud Managed Service for Prometheus with managed collection, define PodMonitoring resources for the applications, and point Grafana at the Prometheus-compatible query endpoint.

**Why it's correct:**
- ✔️ "**Managed Service for Prometheus with managed collection**" matches "**Google manage metric storage and scaling**".
- ✔️ "**PodMonitoring resources for the applications**" replaces the self-managed scrape config.
- ✔️ "**point Grafana at the Prometheus-compatible query endpoint**" matches "**keep using PromQL queries and existing Grafana dashboards**".

📌 **When to use it:** Use it when you like your current metric tool and charts but want someone else to store and scale the data.
🏢 **Office example:** Keeping your forms but handing the archive to a professional records office.

### ❌ B
> **B.** Export the metrics to a Cloud Storage bucket every hour, and query them with BigQuery.

**Wrong words:**
- ❌ "**every hour**" and "**query them with BigQuery**": not real-time monitoring, and it breaks PromQL and Grafana.

📌 **When to use it:** Use exports to BigQuery for long-term analysis, not live dashboards.
🏢 **Office example:** Mailing yesterday's readings to accounting.

### ❌ C
> **C.** Increase the size of the Prometheus server's Persistent Disk.

**Wrong words:**
- ❌ "**Increase the size of the … Persistent Disk**": a short-term patch. You still run and maintain the server.

📌 **When to use it:** Use it as a quick stopgap while planning the move.
🏢 **Office example:** Buying a bigger filing cabinet when you need a records office.

### ❌ D
> **D.** Install the Ops Agent on every GKE node, and rebuild the dashboards without PromQL.

**Wrong words:**
- ❌ "**Ops Agent on every GKE node**": the Ops Agent is for Compute Engine VMs, not GKE app metrics.
- ❌ "**rebuild the dashboards without PromQL**": breaks "**keep using PromQL queries and existing Grafana dashboards**".

📌 **When to use it:** Use the Ops Agent on regular VMs to send their system metrics and logs.
🏢 **Office example:** Throwing away the team's reports and starting new forms.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** GKE:
- PodMonitoring `checkout-metrics` (port `metrics`, every 30s).
- Grafana data source → Cloud Monitoring Prometheus API.
- Alert on `rate(checkout_errors_total[5m]) > 1` in Cloud Monitoring.

---

## 🧠 Key Takeaways / Memory Tips

- **Prometheus without running it, keep PromQL/Grafana → Managed Service for Prometheus (PodMonitoring).**
  🧠 *"**Keep PromQL, drop the server.**"*
- Related: **Q300**, **Q231** (Ops Agent).

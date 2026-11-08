# G022: One Console Place for Your Apps' Deployments, Health, Incidents, Maintenance and Optimizations (Cloud Hub)

**Topic:** Monitoring (Cloud Hub)
**Exam guide section:** 3.4 Monitoring and logging: Using Cloud Hub to monitor active events and application health data

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your operations lead wants a single place in the Google Cloud console that shows, for the applications your team runs, their deployments, application health, active Google Cloud incidents that affect them, upcoming maintenance, and optimization suggestions. What should you use?
>
> **A.** Logs Explorer, searching each project's logs one at a time
>
> **B.** The Cloud Billing reports page
>
> **C.** Cloud Hub
>
> **D.** A Cloud Asset Inventory export to BigQuery

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team runs several applications on Google Cloud, and the operations lead wants one overview screen.
- **What you must achieve:** See each app's deployments, health, any Google Cloud incidents (outages) affecting them, planned maintenance, and suggestions to save money or improve them, all in one place.
- **The limits:** It must be one place in the console, not many separate tools.
- **What they're really asking:** Which console experience brings application health, incidents and recommendations together?

**Clues in the question:**
- "**single place in the Google Cloud console**" + "**applications … deployments, application health, active … incidents, upcoming maintenance, optimization suggestions**": **Cloud Hub**.

**Exam topic:** Monitoring (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Cloud Hub 🔑
- **What it is:** A central console view, organized around your applications (as defined in App Hub), that brings together deployments, health and troubleshooting, Google Cloud incidents, maintenance events, quotas and optimization recommendations.
- **Looks like:** Console → Cloud Hub → app `storefront`: 2 alerts, 1 Google incident in us-east1, upcoming GKE maintenance
- **Not to be confused with:** Logs Explorer (one tool, raw logs) or Billing reports (cost only).
- **Analogy:** 🛫 An airport control tower: one screen for every flight's status.
- **In the online store:** The ShopNow ops lead's morning check.

### 2. App Hub application
- **What it is:** A logical grouping of the services and workloads that make up one app.
- **Looks like:** App `storefront` = Cloud Run `web` + `orders-api` + Cloud SQL `orders-db`
- **Not to be confused with:** A project. One app can span projects.
- **Analogy:** 📁 A folder grouping one team's paperwork.
- **In the online store:** `storefront`, `checkout`, `catalog`.

### 🔗 How they fit together
```
 App Hub apps ─► Cloud Hub ─► deployments | health | incidents | maintenance | optimizations ✅
```

---

## 🌍 Real-World Scenario

Every morning the ops lead used to open five tools. **Cloud Hub** now shows per application whether anything is unhealthy, whether a Google incident affects it, and what maintenance is coming, on one page.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Logs Explorer, searching each project's logs one at a time

**Wrong words:**
- ❌ "**searching each project's logs one at a time**": raw logs only, scattered, and no app-level health, incidents or maintenance.

📌 **When to use it:** Use Logs Explorer to dig into specific log messages.
🏢 **Office example:** Reading every department's diary to get a status update.

### ❌ B
> **B.** The Cloud Billing reports page

**Wrong words:**
- ❌ "**Cloud Billing reports**": cost only, with no health, incidents or deployments.

📌 **When to use it:** Use it to see where money goes.
🏢 **Office example:** The accounting summary, not the control tower.

### ✅ C
> **C.** Cloud Hub

**Why it's correct:**
- ✔️ "**Cloud Hub**" matches "**single place in the Google Cloud console**".
- ✔️ It is organized by application and shows deployments, health, incidents, maintenance and optimizations, matching every item the lead listed.

📌 **When to use it:** Use it when you want one screen that tells you how each of your apps is doing.
🏢 **Office example:** The control tower screen showing every flight's status at once.

### ❌ D
> **D.** A Cloud Asset Inventory export to BigQuery

**Wrong words:**
- ❌ "**Asset Inventory export to BigQuery**": a list of resources for analysis. It doesn't show health or incidents.

📌 **When to use it:** Use it to analyze what resources exist across the org.
🏢 **Office example:** The furniture inventory, not the operations board.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** ops: Cloud Hub → `checkout` app: Cloud Run error rate alert, Google incident "Cloud SQL us-east1 degraded", GKE maintenance window Saturday, 2 rightsizing recommendations.

---

## 🧠 Key Takeaways / Memory Tips

- **One app-centric console view of health, incidents, maintenance, optimizations → Cloud Hub.**
  🧠 *"**Hub = everything in the middle.**"*
- Related: **G020**, **G025** (Personalized Service Health).

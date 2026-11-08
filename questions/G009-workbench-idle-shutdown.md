# G009: Managed Jupyter Notebook With a GPU That Stops Wasting Money Overnight (Workbench Instance + Idle Shutdown)

**Topic:** AI/ML notebooks (Workbench)
**Exam guide section:** 3.1 Managing compute: Managing notebooks in Gemini Enterprise Agent Platform Workbench (formerly Vertex AI Workbench) and BigQuery

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> A data scientist needs a JupyterLab environment with a GPU to explore data stored in BigQuery. The notebook is used only a few hours each day, and the finance team has complained about notebook VMs left running overnight. You want a managed notebook environment that controls this cost with minimal effort. What should you do?
>
> **A.** Create a Workbench instance with a GPU in Gemini Enterprise Agent Platform Workbench, and enable idle shutdown.
>
> **B.** Create a Compute Engine VM, install JupyterLab manually, and ask the data scientist to stop the VM every evening.
>
> **C.** Have the data scientist run Jupyter on a laptop and download the BigQuery tables as CSV files.
>
> **D.** Create a GKE Autopilot cluster and deploy JupyterHub on it.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A data scientist explores data with Jupyter notebooks (web pages where you write and run code step by step) and needs a GPU (an AI/graphics chip). The data is in BigQuery (Google's data warehouse).
- **What you must achieve:** Give them a ready-made notebook environment that doesn't keep charging money when nobody is using it.
- **The limits:** The notebook is used only a few hours a day, and you want the least setup and upkeep.
- **What they're really asking:** Which managed notebook option can switch itself off when it's idle?

**Clues in the question:**
- "**managed notebook environment**": Workbench instances are Google-managed JupyterLab.
- "**left running overnight**" + "**controls this cost with minimal effort**": Workbench **idle shutdown** stops the instance automatically after a set idle time.

**Exam topic:** Managing compute: notebooks (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. JupyterLab / notebook
- **What it is:** A browser-based workspace where you write code in cells, run them, and see results and charts inline.
- **Looks like:** Cell: `%%bigquery\nSELECT category, SUM(total) FROM orders GROUP BY 1`
- **Not to be confused with:** A full code editor (IDE) for building apps.
- **Analogy:** 📓 A lab notebook where each step's result is written right below it.
- **In the online store:** Analysts explore sales by category.

### 2. Workbench instance 🔑
- **What it is:** A Google-managed JupyterLab VM in Gemini Enterprise Agent Platform (formerly Vertex AI Workbench), with BigQuery integration, optional GPUs, and an **idle shutdown** setting.
- **Looks like:** Workbench instance `ds-ana`, `n1-standard-8` + 1× T4 GPU, idle shutdown after 180 min
- **Not to be confused with:** A raw Compute Engine VM where you install and maintain everything yourself.
- **Analogy:** 🧪 A lab bench that's set up for you and switches its lights off when you leave.
- **In the online store:** `ds-ana` explores the `orders` dataset.

### 3. Idle shutdown
- **What it is:** A Workbench setting that stops the instance after it has been idle for a chosen number of minutes. You pay for compute only while it's running.
- **Looks like:** `Idle shutdown: on, 60 minutes`
- **Not to be confused with:** Deleting the instance. Files on its disk stay.
- **Analogy:** 💡 Motion-sensor lights in the office.
- **In the online store:** Ana's GPU notebook stops at night automatically.

### 🔗 How they fit together
```
 Data scientist ──► Workbench instance (JupyterLab + GPU) ──► BigQuery
                       └─ idle 60 min → auto stop 💰 ✅
```

---

## 🌍 Real-World Scenario

Finance spotted thousands of dollars in GPU notebook VMs running every weekend. The cloud engineer moves the team to **Workbench instances** with **idle shutdown**, so notebooks stop by themselves when nobody is using them.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a Workbench instance with a GPU in Gemini Enterprise Agent Platform Workbench, and enable idle shutdown.

**Why it's correct:**
- ✔️ "**Workbench instance**" matches "**managed notebook environment**".
- ✔️ "**with a GPU**" matches "**JupyterLab environment with a GPU**".
- ✔️ "**enable idle shutdown**" matches "**left running overnight**" and "**controls this cost with minimal effort**".

📌 **When to use it:** Use it when someone needs a ready-made notebook workspace that turns itself off when they walk away.
🏢 **Office example:** A meeting room whose lights and heating switch off automatically when it's empty.

### ❌ B
> **B.** Create a Compute Engine VM, install JupyterLab manually, and ask the data scientist to stop the VM every evening.

**Wrong words:**
- ❌ "**install JupyterLab manually**": not managed, so more effort.
- ❌ "**ask the data scientist to stop the VM every evening**": relies on people remembering, which is exactly what failed before.

📌 **When to use it:** Use it when you need a fully custom machine and accept looking after it yourself.
🏢 **Office example:** Asking staff to remember to turn the lights off.

### ❌ C
> **C.** Have the data scientist run Jupyter on a laptop and download the BigQuery tables as CSV files.

**Wrong words:**
- ❌ "**download the BigQuery tables as CSV files**": copies data onto a laptop, which is slow and a security risk, and a laptop has no cloud GPU.

📌 **When to use it:** Use local notebooks for small personal experiments with tiny public datasets.
🏢 **Office example:** Photocopying the whole archive to take home.

### ❌ D
> **D.** Create a GKE Autopilot cluster and deploy JupyterHub on it.

**Wrong words:**
- ❌ "**GKE Autopilot cluster and deploy JupyterHub**": a whole platform to build and run for one user. Not minimal effort.

📌 **When to use it:** Use it when a large group needs a shared, customised notebook platform you're ready to run.
🏢 **Office example:** Building a library to lend out one notebook.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** analytics:
- Workbench instance `ds-ana` with a T4 GPU and idle shutdown after 60 minutes.
- Ana queries `shopnow_dw.orders` with the `%%bigquery` magic.
- Simpler SQL-only notebooks can run in BigQuery Studio (Colab Enterprise notebooks).

---

## 🧠 Key Takeaways / Memory Tips

- **Managed Jupyter (+GPU) → Workbench instance. Stop paying when unused → idle shutdown.**
  🧠 *"**Workbench naps when idle.**"*
- Related: **Q101**, **G010**.

# Q140: One Monitoring View for Projects A, B and C (Workspace / Metrics Scope With All Three)

**Topic:** Cloud Monitoring (workspace / metrics scope, multiple projects)

## ❓ Question
> You are asked to set up application performance monitoring on Google Cloud projects A, B, and C as a single pane of glass. You want to monitor CPU, memory, and disk. What should you do?
>
> **A.** Enable API and then share charts from project A, B, and C.
>
> **B.** Enable API and then give the metrics.reader role to projects A, B, and C.
>
> **C.** Enable API and then use default dashboards to view all projects in sequence.
>
> **D.** Enable API, create a workspace under project A, and then add projects B and C.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You have projects A, B and C.
- **What you must achieve:** Monitor CPU, memory and disk for all of them in one view.
- **The limits:** A single pane of glass (one screen).
- **What they're really asking:** How do you monitor all three projects together?

**Clues in the question:**
- "**single pane of glass**": one Monitoring view for all three → a **workspace** (now called a **metrics scope**) in project A that **includes** B and C.

**Exam topic:** Monitoring.

---

## 📚 Key Terms Explained

### 1. Workspace / metrics scope 🔑
- **What it is:** The setting that decides **which projects' metrics** a Cloud Monitoring view can see. One **scoping project** can add other projects.
- **Looks like:** Monitoring → Settings → Metrics scope → Add projects B, C
- **Not to be confused with:** a dashboard.
- **Analogy:** 🖥️ One control room with screens for every building.
- **In the online store:** `shopnow-ops` watches dev, staging and prod.

### 2. Memory and disk metrics
- **What it is:** CPU is built in. Memory and disk usage inside the VM need the **Ops Agent**.
- **Looks like:** `agent.googleapis.com/memory/percent_used`
- **Not to be confused with:** CPU utilization.
- **Analogy:** 🌡️ Extra sensors inside the room.
- **In the online store:** Disk-full alerts on the DB VM.

### 🔗 How they fit together
```
 project A (scoping project) ── metrics scope ── project B, project C ✅
   one dashboard: CPU / memory / disk for A + B + C
```

---

## 🌍 Real-World Scenario

An SRE team supports three projects. They pick project A as the **scoping project** and add B and C to its metrics scope. One dashboard and one set of alerts covers all VMs.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable API and then share charts from project A, B, and C.

**Wrong words:**
- ❌ "**share charts from project A, B, and C**": still three separate places, not one view.

📌 **When to use it:** Use chart sharing to show one chart to someone.
🏢 **Office example:** Passing around screenshots from three control rooms.

### ❌ B
> **B.** Enable API and then give the metrics.reader role to projects A, B, and C.

**Wrong words:**
- ❌ "**give the metrics.reader role to projects**": roles are given to people or service accounts, not projects, and a role alone doesn't create a combined view.

📌 **When to use it:** Use metric reader roles for tools that read metrics.
🏢 **Office example:** Giving buildings a key instead of building one control room.

### ❌ C
> **C.** Enable API and then use default dashboards to view all projects in sequence.

**Wrong words:**
- ❌ "**view all projects in sequence**": you switch between projects one by one, which isn't a single pane.

📌 **When to use it:** Use default dashboards for a quick look at one project.
🏢 **Office example:** Walking from control room to control room.

### ✅ D
> **D.** Enable API, create a workspace under project A, and then add projects B and C.

**Why it's correct:**
- ✔️ "**create a workspace under project A**" matches "**single pane of glass**": one Monitoring home.
- ✔️ "**add projects B and C**" matches "**projects A, B, and C**": all three are visible together.
- ✔️ That view shows the VMs' metrics, matching "**CPU, memory, and disk**".

📌 **When to use it:** Use it when one team watches several areas from one screen.
🏢 **Office example:** One control room with live screens for all three buildings.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow sets `shopnow-ops` as the scoping project and adds `shopnow-dev`, `shopnow-staging` and `shopnow-prod`. One dashboard shows CPU, memory and disk for every VM, using the Ops Agent for memory and disk.

---

## 🧠 Key Takeaways / Memory Tips

- **Many projects, one monitoring view → workspace / metrics scope with all projects added.**
  🧠 *"**One room, many screens.**"*
- Related: **Q123** (alerting), **Q067** (monitoring.viewer).

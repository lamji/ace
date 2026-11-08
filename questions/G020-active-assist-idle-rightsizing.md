# G020: Let Google Find Idle and Oversized VMs Across Projects (Active Assist Recommendations)

**Topic:** Cost optimization (Active Assist)
**Exam guide section:** 3.4 Monitoring and logging: Using Active Assist to optimize resource utilization

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your finance team asks you to reduce Compute Engine costs across many projects. You suspect that some VMs are idle and others are much larger than needed. You want Google Cloud to identify these VMs based on their actual usage, with the least effort. What should you do?
>
> **A.** Write a script that connects to each VM over SSH every hour and records CPU usage.
>
> **B.** Delete every VM whose CPU utilization is below 50% right now.
>
> **C.** Convert every VM to a Spot VM.
>
> **D.** Review Active Assist recommendations, such as idle VM and machine type rightsizing recommendations, in the Recommendation Hub.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Finance wants lower costs for VMs (rented computers) across many projects.
- **What you must achieve:** Find VMs that sit idle and VMs that are much bigger than they need to be.
- **The limits:** Base it on real usage, and with the least effort, letting Google Cloud do the finding.
- **What they're really asking:** Which built-in Google Cloud feature recommends idle and oversized VMs to fix?

**Clues in the question:**
- "**Google Cloud to identify these VMs based on their actual usage**": **Active Assist recommenders** (idle VM, machine type).
- "**across many projects**" + "**least effort**": the **Recommendation Hub** gathers recommendations across projects.

**Exam topic:** Cost optimization (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Active Assist 🔑
- **What it is:** Google Cloud's set of **recommenders** that analyze your usage and suggest improvements: idle VMs, idle disks and IPs, rightsizing machine types, IAM permissions to remove, and more. Shown in the Recommendation Hub and on resource pages.
- **Looks like:** "VM `old-batch-2` has been idle for 14 days: stop or delete, saves $83/month"
- **Not to be confused with:** Billing reports, which show spending but don't analyze usage.
- **Analogy:** 🧾 An efficiency consultant who walks the office and lists empty desks and oversized rooms.
- **In the online store:** Flags `test-api-old` as idle.

### 2. Rightsizing (machine type recommendation)
- **What it is:** A suggestion to change a VM to a smaller (or bigger) machine type based on its real CPU and memory use.
- **Looks like:** `e2-standard-16` → `e2-standard-4` (saves 74%)
- **Not to be confused with:** Autoscaling, which changes the number of VMs, not their size.
- **Analogy:** 📏 Moving a two-person team out of a 20-seat room.
- **In the online store:** The `reporting` VM is downsized.

### 🔗 How they fit together
```
 Usage data ─► Active Assist recommenders ─► Recommendation Hub
   idle VM: stop/delete 💰   rightsizing: smaller type 💰 ✅
```

---

## 🌍 Real-World Scenario

At quarter end, finance wants 20% savings. In the **Recommendation Hub**, the engineer sees 37 idle VMs and 52 oversized VMs, with estimated savings. Applying the safe ones meets the target in an afternoon.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Write a script that connects to each VM over SSH every hour and records CPU usage.

**Wrong words:**
- ❌ "**script … SSH every hour**": custom work, intrusive, and Google already measures this for you.

📌 **When to use it:** Avoid it. Use built-in monitoring and recommendations.
🏢 **Office example:** Asking a clerk to check every desk every hour.

### ❌ B
> **B.** Delete every VM whose CPU utilization is below 50% right now.

**Wrong words:**
- ❌ "**Delete every VM … below 50% right now**": one moment's CPU doesn't prove a VM is idle. You could delete important servers.

📌 **When to use it:** Never delete based on one snapshot of usage. Review recommendations first.
🏢 **Office example:** Throwing out every desk that's empty at lunchtime.

### ❌ C
> **C.** Convert every VM to a Spot VM.

**Wrong words:**
- ❌ "**Convert every VM to a Spot VM**": Spot VMs can be stopped at any time. That's wrong for many workloads, and it doesn't find idle or oversized VMs.

📌 **When to use it:** Use Spot for fault-tolerant batch work.
🏢 **Office example:** Making every employee a temp who can be sent home any minute.

### ✅ D
> **D.** Review Active Assist recommendations, such as idle VM and machine type rightsizing recommendations, in the Recommendation Hub.

**Why it's correct:**
- ✔️ "**Active Assist recommendations**" matches "**Google Cloud to identify these VMs based on their actual usage**".
- ✔️ "**idle VM and machine type rightsizing**" matches "**some VMs are idle and others are much larger than needed**".
- ✔️ "**Recommendation Hub**" matches "**across many projects**" and "**least effort**".

📌 **When to use it:** Use it when you want Google to point out wasted or oversized resources for you.
🏢 **Office example:** An efficiency consultant's list of empty and oversized offices with the savings for each.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: the Recommendation Hub shows idle `promo-2025-vm` (stop it) and oversized `catalog-sync` (`n2-standard-16` → `n2-standard-4`). Total savings: $1,240/month.

---

## 🧠 Key Takeaways / Memory Tips

- **Find idle or oversized resources automatically → Active Assist (Recommender / Recommendation Hub).**
  🧠 *"**Active Assist actively points at waste.**"*
- Related: **G021** (IAM recommender), **Q077**.

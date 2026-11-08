# G011: Patch Hundreds of Linux and Windows VMs Monthly and Report Results (VM Manager Patch Deployment)

**Topic:** Compute Engine (VM Manager)
**Exam guide section:** 2.1 Planning compute resources: Configuring VM Manager

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You manage several hundred Linux and Windows VMs in a project. You must apply operating system security patches automatically every month during a maintenance window and see which VMs were patched successfully. You want to use a Google-managed approach. What should you do?
>
> **A.** SSH into each VM every month and run the operating system update commands manually.
>
> **B.** Recreate every VM each month from the latest public image without preserving data.
>
> **C.** Enable VM Manager, make sure the OS Config agent is running on the VMs, create a patch deployment with a monthly schedule, and review the patch job results.
>
> **D.** Create a Cloud Monitoring uptime check for each VM.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You look after several hundred VMs (rented computers), some running Linux and some Windows.
- **What you must achieve:** Install the operating system's security updates (patches) automatically once a month at a set time, and see a report of which VMs updated successfully.
- **The limits:** It must be automatic and use a Google-managed tool, not something you build.
- **What they're really asking:** Which Google Cloud tool schedules and reports OS patching across many VMs?

**Clues in the question:**
- "**apply operating system security patches automatically every month**": a **patch deployment** (a scheduled patch job).
- "**see which VMs were patched successfully**": patch job results in VM Manager.
- "**Google-managed approach**": **VM Manager** (OS Config API + agent).

**Exam topic:** Compute Engine management (exam guide section 2.1).

---

## 📚 Key Terms Explained

### 1. VM Manager 🔑
- **What it is:** A set of Compute Engine tools for managing the operating systems of large VM fleets: **patch management**, **OS inventory**, vulnerability reports and **OS policies**. It needs the OS Config API enabled and the OS Config agent running (it's preinstalled on most Google images).
- **Looks like:** `gcloud services enable osconfig.googleapis.com`
- **Not to be confused with:** Cloud Monitoring, which watches health but doesn't install updates.
- **Analogy:** 🧑‍🔧 The building's maintenance department that services every office on a schedule.
- **In the online store:** Patches all ShopNow API VMs each month.

### 2. Patch deployment
- **What it is:** A schedule (one-time or recurring) that runs patch jobs on chosen VMs, picked by labels, zones or name prefixes.
- **Looks like:** `gcloud compute os-config patch-deployments create monthly --file=monthly.yaml` (monthly, 2nd Sunday 02:00, label env=prod)
- **Not to be confused with:** A single manual patch job run once.
- **Analogy:** 📅 "Service every air conditioner on the 2nd Sunday."
- **In the online store:** `monthly-prod` patches VMs labeled `env=prod`.

### 3. Patch job
- **What it is:** One run of patching. It shows per-VM status: succeeded, failed or skipped.
- **Looks like:** Patch job `monthly-2026-11`: 812 succeeded, 3 failed
- **Not to be confused with:** The schedule itself.
- **Analogy:** ✅ The checklist from one maintenance visit.
- **In the online store:** Failed VMs are investigated the next morning.

### 🔗 How they fit together
```
 Patch deployment (monthly, 2nd Sun 02:00, label env=prod)
      └─► patch job ─► OS Config agent on each VM ─► apt/yum/Windows Update
                └─► results per VM (succeeded / failed) ✅
```

---

## 🌍 Real-World Scenario

After an audit flags unpatched servers, a retailer sets a **VM Manager patch deployment** for all production VMs: every second Sunday at 2 a.m., with a report ready on Monday morning. No one SSHes into anything.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** SSH into each VM every month and run the operating system update commands manually.

**Wrong words:**
- ❌ "**SSH into each VM every month … manually**": not automatic, error-prone, and gives no central report for hundreds of VMs.

📌 **When to use it:** Use it for one urgent fix on a single machine.
🏢 **Office example:** Walking to every office to fix each heater by hand.

### ❌ B
> **B.** Recreate every VM each month from the latest public image without preserving data.

**Wrong words:**
- ❌ "**Recreate every VM … without preserving data**": destroys data and is disruptive. Patching is the safer, simpler way.

📌 **When to use it:** Use rebuilding from fresh images only for stateless VMs in a managed instance group.
🏢 **Office example:** Rebuilding the office every month to fix the light bulbs.

### ✅ C
> **C.** Enable VM Manager, make sure the OS Config agent is running on the VMs, create a patch deployment with a monthly schedule, and review the patch job results.

**Why it's correct:**
- ✔️ "**Enable VM Manager … OS Config agent**" matches "**Google-managed approach**".
- ✔️ "**patch deployment with a monthly schedule**" matches "**automatically every month during a maintenance window**".
- ✔️ "**review the patch job results**" matches "**see which VMs were patched successfully**".

📌 **When to use it:** Use it when many machines need regular updates on a schedule with a report afterwards.
🏢 **Office example:** A maintenance company that services every office monthly and leaves a checklist.

### ❌ D
> **D.** Create a Cloud Monitoring uptime check for each VM.

**Wrong words:**
- ❌ "**uptime check**": tells you if a VM answers. It doesn't install patches.

📌 **When to use it:** Use uptime checks to be alerted when a website stops responding.
🏢 **Office example:** A guard checking that doors open, not a repair crew.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** fleet:
- VM Manager patch deployment `prod-monthly` (label `env=prod`, 2nd Sunday 02:00 UTC, reboot if required).
- Vulnerability reports (Q254) show which CVEs remain.
- Managed instance groups are rolled to new images instead.

---

## 🧠 Key Takeaways / Memory Tips

- **OS patching / inventory / OS policies for many VMs → VM Manager (OS Config). Scheduled patching → patch deployment.**
  🧠 *"**VM Manager = the fleet's maintenance crew.**"*
- Related: **Q254** (vulnerability reports).

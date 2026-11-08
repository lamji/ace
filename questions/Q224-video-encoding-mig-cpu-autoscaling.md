# Q224: Highly Available Video Encoding With Automated Scaling (Instance Group + CPU Autoscaling)

**Topic:** Compute Engine (managed instance groups, autoscaling)

## ❓ Question
> You want to host your video encoding software on Compute Engine. Your user base is growing rapidly, and users need to be able to encode their videos at any time without interruption or CPU limitations. You must ensure that your encoding solution is highly available, and you want to follow Google-recommended practices to automate operations. What should you do?
>
> **A.** Deploy your solution on multiple standalone Compute Engine instances, and increase the number of existing instances when CPU utilization on Cloud Monitoring reaches a certain threshold.
>
> **B.** Deploy your solution on multiple standalone Compute Engine instances, and replace existing instances with high-CPU instances when CPU utilization on Cloud Monitoring reaches a certain threshold.
>
> **C.** Deploy your solution to an instance group, and increase the number of available instances whenever you see high CPU utilization in Cloud Monitoring.
>
> **D.** Deploy your solution to an instance group, and set the autoscaling based on CPU utilization.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will host video-encoding software (software that converts videos) on Compute Engine. Users are growing fast and must be able to encode at any time.
- **What you must achieve:** Run the encoding service so it is always available.
- **The limits:** No interruptions or CPU limits, high availability, and automated operations following Google's recommendations.
- **What they're really asking:** How do you set up VMs that stay available and grow with demand automatically?

**Clues in the question:**
- "**highly available**" → **instance group** (autohealing, multi-zone).
- "**automate operations**" + "**without … CPU limitations**" → **autoscaling on CPU**.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. MIG autoscaling 🔑
- **What it is:** The group adds/removes VMs automatically to hit a target (e.g. 60% CPU).
- **Looks like:** `gcloud compute instance-groups managed set-autoscaling enc-mig --max-num-replicas=50 --target-cpu-utilization=0.6`
- **Not to be confused with:** manual scaling.
- **Analogy:** 👥 A shift manager who calls in staff automatically when it's busy.
- **In the online store:** Image processing workers.

### 🔗 How they fit together
```
 CPU > 60% → MIG adds VMs ✅   CPU low → removes VMs
```

---

## 🌍 Real-World Scenario

A video platform runs encoders in a **MIG with CPU autoscaling**. When uploads spike, VMs are added automatically; at night the group shrinks.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy your solution on multiple standalone Compute Engine instances, and increase the number of existing instances when CPU utilization on Cloud Monitoring reaches a certain threshold.

**Wrong words:**
- ❌ "**standalone Compute Engine instances**": no autohealing or automatic scaling.
- ❌ "**increase the number … when CPU … reaches a threshold**": manual.

📌 **When to use it:** Use standalone VMs for one-off servers.
🏢 **Office example:** Calling in staff by hand whenever someone notices a queue.

### ❌ B
> **B.** Deploy your solution on multiple standalone Compute Engine instances, and replace existing instances with high-CPU instances when CPU utilization on Cloud Monitoring reaches a certain threshold.

**Wrong words:**
- ❌ "**standalone**" and ❌ "**replace existing instances with high-CPU instances**": manual, disruptive.

📌 **When to use it:** Use bigger machines when one job needs more power.
🏢 **Office example:** Swapping every worker's desk mid-shift.

### ❌ C
> **C.** Deploy your solution to an instance group, and increase the number of available instances whenever you see high CPU utilization in Cloud Monitoring.

**Wrong words:**
- ✔️ "instance group" is right.
- ❌ "**increase the number … whenever you see high CPU**": a person must watch and act. Not automated.

📌 **When to use it:** Use manual resizing for planned one-off changes.
🏢 **Office example:** A manager who must notice the queue first.

### ✅ D
> **D.** Deploy your solution to an instance group, and set the autoscaling based on CPU utilization.

**Why it's correct:**
- ✔️ "**Deploy your solution to an instance group**" matches "**highly available**".
- ✔️ "**set the autoscaling based on CPU utilization**" matches "**automate operations**" + "**without … CPU limitations**".

📌 **When to use it:** Use it when demand grows and shrinks and you want capacity to follow by itself.
🏢 **Office example:** A team that automatically calls in more staff when everyone gets too busy.

---

## 🛒 E-Commerce Full-Stack Example

MIG `image-resizer` (regional, autohealing) with autoscaling target CPU 0.6, max 40.

---

## 🧠 Key Takeaways / Memory Tips

- **HA + automated scaling on Compute Engine → MIG + autoscaling.**
  🧠 *"**Group for HA, autoscaler for growth.**"*
- Related: **Q182**, **Q221**.

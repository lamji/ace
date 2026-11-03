# Q319: Warm Instances for a New Cloud Run Revision Before Shifting Traffic (Revision Min Instances = 2)

**Topic:** Cloud Run (revisions, min instances)

## ❓ Question
> You ate managing an application deployed on Cloud Run. The development team has released a new version of the application. You want to deploy and redirect traffic to this new version of the application. To ensure traffic to the new version of the application is served with no startup time, you want to ensure that there are two idle instances available for incoming traffic before adjusting the traffic flow. You also want to minimize administrative overhead. What should you do?
>
> **A.** Ensure the checkbox “Serve this revision immediately” is unchecked when deploying the new revision. Before changing the traffic rules, use a traffic simulation tool to send load to the new revision.
>
> **B.** Configure service autoscaling and set the minimum number of instances to 2.
>
> **C.** Configure revision autoscaling for the new revision and set the minimum number of instances to 2.
>
> **D.** Configure revision autoscaling for the existing revision and set the minimum number of instances to 2.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** New version must have **2 warm instances** before traffic moves.

**Clues in the question:**
- "**two idle instances**" for the **new** version → **revision min instances = 2** on the **new revision**.

**Exam topic:** Cloud Run.

---

## 📚 Key Terms Explained

### 1. Revision min instances 🔑
- **What it is:** Keeps N instances warm for a specific revision so no cold start.
- **Looks like:** `gcloud run deploy web --image=...:v2 --min-instances=2 --no-traffic`
- **Not to be confused with:** service-level min instances (applies across revisions).
- **Analogy:** 🧑‍💼 Two staff at their desks before the doors open.
- **In the online store:** —

### 🔗 How they fit together
```
 deploy v2 (--no-traffic, min=2) → 2 warm → shift traffic ✅
```

---

## 🌍 Real-World Scenario

A team deploys v2 with **min instances 2** and no traffic, then shifts traffic once instances are warm.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Ensure the checkbox “Serve this revision immediately” is unchecked when deploying the new revision. Before changing the traffic rules, use a traffic simulation tool to send load to the new revision.

**Wrong words:**
- ❌ "**traffic simulation tool**": extra work and doesn't guarantee idle instances.

📌 **When to use it:** Use load tests for performance testing.
🏢 **Office example:** Sending fake customers to wake staff.

### ❌ B
> **B.** Configure service autoscaling and set the minimum number of instances to 2.

**Wrong words:**
- ❌ "**service autoscaling**": applies to the service overall, not specifically warming the new revision before the switch.

📌 **When to use it:** Use service min instances to keep the whole service warm.
🏢 **Office example:** Two staff somewhere in the building.

### ✅ C
> **C.** Configure revision autoscaling for the new revision and set the minimum number of instances to 2.

**Why it's correct:**
- ✔️ "**revision autoscaling for the new revision**" matches "**traffic to the new version … no startup time**".
- ✔️ "**minimum number of instances to 2**" matches "**two idle instances available … before adjusting the traffic flow**".

📌 **When to use it:** Use it when the new version should be ready and waiting before customers are sent to it.
🏢 **Office example:** Two staff at the new counter before the line is redirected.

### ❌ D
> **D.** Configure revision autoscaling for the existing revision and set the minimum number of instances to 2.

**Wrong words:**
- ❌ "**existing revision**": warms the old version, not the new one.

📌 **When to use it:** Use it to keep the current version warm.
🏢 **Office example:** Staffing the old counter.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud run deploy storefront --image=...:v42 --min-instances=2 --no-traffic` → `gcloud run services update-traffic storefront --to-latest`.

---

## 🧠 Key Takeaways / Memory Tips

- **Warm the new version → min instances on the new revision.**
  🧠 *"**Warm the new before you move.**"*
- Related: **Q229**.

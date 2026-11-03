# Q033: Exactly One VM, Always Running (MIG Autoscaling Min 1 / Max 1)

**Topic:** Compute Engine managed instance groups (autoscaler min/max, target size, autohealing)

## ❓ Question
> You are deploying an application to a Compute Engine VM in a managed instance group. The application must be running at all times, but only a single instance of the VM should run per GCP project. How should you configure the instance group?
>
> **A.** Set autoscaling to On, set the minimum number of instances to 1, and then set the maximum number of instances to 1.
>
> **B.** Set autoscaling to Off, set the minimum number of instances to 1, and then set the maximum number of instances to 1.
>
> **C.** Set autoscaling to On, set the minimum number of instances to 1, and then set the maximum number of instances to 2.
>
> **D.** Set autoscaling to Off, set the minimum number of instances to 1, and then set the maximum number of instances to 2.

**My answer:** B
**Correct answer:** A
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** You run an app on a VM inside a **managed instance group (MIG)**. Two rules:
1. **Always running**: if the VM dies, a new one must replace it.
2. **Never more than one** VM at the same time.

Which MIG setting guarantees "**exactly one, always**"?

| Keyword | What it hints at |
|---|---|
| "**running at all times**" | At least **1** → **minimum = 1** |
| "**only a single instance**" | Never 2 → **maximum = 1** |
| "**minimum / maximum number of instances**" | These two settings **only exist when autoscaling is On**. That's why A wins over B |

**Exam topic:** Compute Engine / managed instance groups.

> ⚠️ **Honest note:** This is one of the most debated questions (132 comments). Many people pick **B** because "why autoscale if it never changes?" The accepted answer is **A**, because in a real MIG **"min" and "max" are autoscaler settings**. With autoscaling **Off**, those fields don't exist. You set a fixed **target size** instead. So option B describes a setup you can't actually configure.

---

## 📚 Key Terms Explained

### 1️⃣ Managed Instance Group (MIG) (review from Q004, Q016)
- **What it is:** A **group of identical VMs** made from one **instance template**. Google **creates, replaces and counts** them for you.
- **Looks like:** `mig-license-server` (template `license-tmpl-v3`, zone `us-central1-a`, size 1)
- **Not to be confused with:** a single VM you made by hand. A plain VM that dies **stays dead**. A MIG **recreates** it.
- **Analogy:** 🏢 A **staffing agency contract**: "Keep N receptionists at this desk." If one leaves, the agency sends a replacement.
- **In the online store:** The storefront web servers run in a MIG.

### 2️⃣ Autoscaling, Minimum and Maximum 🔑
- **What it is:** The **autoscaler** changes the number of VMs based on load (CPU, requests, schedule), but always **stays between a minimum and a maximum** that you set.
- **Looks like:**
  ```bash
  gcloud compute instance-groups managed set-autoscaling mig-license-server \
    --zone=us-central1-a --min-num-replicas=1 --max-num-replicas=1
  ```
- **Not to be confused with:** "autoscaling = always grows". With **min 1 / max 1**, it can **never** go above or below 1. You're using the autoscaler as a **fence**, not to grow.
- **Analogy:** 🌡️ A thermostat locked between **21° and 21°**. It's "on", but the temperature never changes.

### 3️⃣ Autoscaling Off → Target Size
- **What it is:** With autoscaling **Off**, a MIG keeps a **fixed number** of VMs, called the **target size** (`--size=1`). There's **no min or max field**.
- **Looks like:** `gcloud compute instance-groups managed create mig-license-server --size=1 --template=license-tmpl-v3`
- **Not to be confused with:** option B's wording. "Autoscaling Off **with min and max**" mixes settings from two different modes.
- **Analogy:** 📋 A fixed staff roster: "1 receptionist", no range.

### 4️⃣ Autohealing / Recreating Instances (review from Q004)
- **What it is:** The MIG **recreates a VM** if it stops, is deleted, or (with a **health check**) stops answering. This is what keeps it "**running at all times**".
- **Looks like:** `--health-check=license-hc --initial-delay=120`
- **Not to be confused with:** autoscaling. **Autohealing replaces broken VMs**, while **autoscaling changes how many** VMs there are.
- **Analogy:** 🩺 The agency **replaces a sick receptionist** the same morning.

### 🔗 How They Fit Together
```
           MIG: mig-license-server  (template license-tmpl-v3)
                         │
      ┌──────────────────┼───────────────────┐
      ▼                  ▼                   ▼
 Autoscaler ON       Autohealing         Result
 min=1, max=1        (health check)
 never 0, never 2    replaces a dead VM  → exactly 1 VM, always ✅

 A: ON  1/1 → exactly 1 ✅
 B: OFF + min/max → not a real setting (Off uses a fixed size)
 C: ON  1/2 → can grow to 2 ❌
 D: OFF + 1/2 → not a real setting, and 2 breaks the rule ❌
```

---

## 🌍 Real-World Scenario

Some software **must never run twice**: a **license server** that allows one copy, a **scheduler / cron job runner** that would send every email twice if duplicated, or a **leader process** that writes to a shared file. But it also **must not stay down**. A MIG with **min 1 / max 1** gives you "**self-healing singleton**": Google keeps one copy alive and never starts a second.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set autoscaling to On, set the minimum number of instances to 1, and then set the maximum number of instances to 1.

**Why it's correct:**
- ✔️ **Min 1** → never zero, so the app is always there.
- ✔️ **Max 1** → the autoscaler can **never** add a second VM, even under heavy load.
- ✔️ Min and max are **real autoscaler settings**, so this can actually be configured as written.
- ✔️ The MIG still **recreates** the VM if it dies (add a health check for full autohealing).

**📌 When to use it:** Use it when exactly one copy must always be running, never zero and never two.
🏢 **Office example:** A contract with the agency: "Always exactly one night guard at the front door. Replace them if they're sick, but never send two."

### ❌ B (your answer)
> **B.** Set autoscaling to Off, set the minimum number of instances to 1, and then set the maximum number of instances to 1.

**Why it's wrong:**
- ❌ **Min and max only exist when autoscaling is On.** With autoscaling Off you set a fixed **size**, so this combination can't be configured.
- 💡 **Likely mix-up:** Your thinking was sensible: "the number never changes, so why turn autoscaling on?" In practice, a MIG with autoscaling Off and **size 1** would also keep one VM running. But the exam's wording ties **min/max** to **autoscaling On**, so A is the accepted answer.

**📌 When to use it:** Turn autoscaling off when you want a fixed number of VMs, set as a size rather than a min/max.
🏢 **Office example:** A fixed roster that says "2 receptionists", with no range and no adjustments.

### ❌ C
> **C.** Set autoscaling to On, set the minimum number of instances to 1, and then set the maximum number of instances to 2.

**Why it's wrong:**
- ✔️ Always at least 1…
- ❌ …but under load the autoscaler can start a **second** VM, which breaks "only a single instance".

**📌 When to use it:** Use it when one copy is normal but a second can help on busy days.
🏢 **Office example:** One cashier usually, with a second called in when the queue gets long.

### ❌ D
> **D.** Set autoscaling to Off, set the minimum number of instances to 1, and then set the maximum number of instances to 2.

**Why it's wrong:**
- ❌ Same problem as B: min/max aren't settings when autoscaling is Off.
- ❌ And **max 2** breaks the "single instance" rule anyway.

**📌 When to use it:** **Never use this.** It mixes settings that don't go together, and allows 2. Use A.
🏢 **Office example:** A roster that says "fixed staff" and "1 to 2 people" at the same time. It contradicts itself.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow has an **order-export job** that sends each day's orders to the accounting system. If **two** copies ran, accounting would get **every order twice**. If **zero** ran, the books would be empty.

```bash
# MIG from the template
gcloud compute instance-groups managed create mig-order-exporter \
  --zone=us-central1-a --template=order-exporter-tmpl --size=1

# Fence it to exactly one (option A)
gcloud compute instance-groups managed set-autoscaling mig-order-exporter \
  --zone=us-central1-a --min-num-replicas=1 --max-num-replicas=1

# Recreate it if it stops responding (autohealing, Q004)
gcloud compute instance-groups managed update mig-order-exporter \
  --zone=us-central1-a --health-check=exporter-hc --initial-delay=120
```

| Event | Result |
|---|---|
| The VM crashes at 2 AM | The MIG recreates it → still 1 ✅ |
| CPU hits 100% during the Black Friday export | The autoscaler wants more, but **max = 1** → still 1 ✅ (no duplicate orders) |
| With C (max 2) | A second exporter starts → accounting gets duplicate orders ❌ |

---

## 🧠 Key Takeaways / Memory Tips

- **"Always running" + "only one" → MIG with autoscaling On, min = 1, max = 1.**
  🧠 *"**1 and 1 = exactly one, forever.**"*
- **Min/max = autoscaler settings.** Autoscaling Off = a fixed **size**, with no min/max. Options that mix "Off" with min/max are traps.
- **Autohealing (replace broken VMs) ≠ autoscaling (change the count).** Here you want both: the MIG heals, and the autoscaler fences the count.
- Related: **Q004** (MIG autohealing), **Q016** (MIG CPU autoscaling).

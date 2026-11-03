# Q057: Updating a Live MIG Without Losing Capacity (maxSurge 1, maxUnavailable 0)

**Topic:** Compute Engine MIG (rolling update, maxSurge, maxUnavailable, instance template)

## ❓ Question
> You have a web application deployed as a managed instance group. You have a new version of the application to gradually deploy. Your web application is currently receiving live web traffic. You want to ensure that the available capacity does not decrease during the deployment. What should you do?
>
> **A.** Perform a rolling-action start-update with maxSurge set to 0 and maxUnavailable set to 1.
>
> **B.** Perform a rolling-action start-update with maxSurge set to 1 and maxUnavailable set to 0.
>
> **C.** Create a new managed instance group with an updated instance template. Add the group to the backend service for the load balancer. When all instances in the new managed instance group are healthy, delete the old managed instance group.
>
> **D.** Create a new instance template with the new application version. Update the existing managed instance group with the new instance template. Delete the instances in the managed instance group to allow the managed instance group to recreate the instance using the new instance template.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❌ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your website runs on a group of identical VMs (a MIG) and real customers are using it. You want to swap in the new version **a few VMs at a time**, and the number of working VMs must **never go down** while you do it.

| Keyword | What it hints at |
|---|---|
| "**managed instance group**" | MIGs have a built-in **rolling update** command |
| "**gradually deploy**" | Replace VMs a few at a time → **rolling update** |
| "**live web traffic**" | You can't take the site down |
| "**capacity does not decrease**" | **maxUnavailable = 0** (never remove a VM before its replacement is ready) |

**Exam topic:** Compute Engine / managed instance groups.

---

## 📚 Key Terms Explained

### 1️⃣ Managed Instance Group (MIG) (review from Q004, Q016)
- **What it is:** A **group of identical VMs** made from one **instance template**. Google keeps the count right, heals broken VMs and can update them all.
- **Looks like:** `web-mig` → `web-a1b2`, `web-c3d4`, `web-e5f6` (3 VMs)
- **Analogy:** 🏢 A team of **identical help-desk staff** hired from the same job description.

### 2️⃣ Instance Template
- **What it is:** A **saved recipe** for a VM: machine type, disk image, startup script. New version of the app = **new template**.
- **Looks like:** `web-template-v1` (image `web-v1`), `web-template-v2` (image `web-v2`)
- **Not to be confused with:** a running VM. A template is only the recipe.
- **Analogy:** 📄 The **job description** you hire from.

### 3️⃣ Rolling Update (`rolling-action start-update`) 🔑
- **What it is:** A built-in MIG command that **replaces VMs a few at a time** with ones made from the new template, while the rest keep serving.
- **Looks like:**
  ```bash
  gcloud compute instance-groups managed rolling-action start-update web-mig \
    --version=template=web-template-v2 --max-surge=1 --max-unavailable=0 --zone=us-central1-a
  ```
- **Analogy:** 🔄 Replacing staff **one at a time** instead of firing the whole team on Monday.

### 4️⃣ maxSurge 🔑
- **What it is:** How many **EXTRA VMs** the MIG may create **above** the normal size during the update.
- **Looks like:** size 3, `maxSurge=1` → up to **4** VMs for a moment
- **Analogy:** ➕ Bringing in **the new hire before** the old one leaves.

### 5️⃣ maxUnavailable 🔑
- **What it is:** How many VMs may be **out of service** at once during the update.
- **Looks like:** `maxUnavailable=0` → **never** fewer than 3 working VMs
- **Not to be confused with:** maxSurge. Surge = **extra** VMs added. Unavailable = VMs **missing**.
- **Analogy:** ➖ How many desks may sit **empty** during the swap.

### 🔗 How They Fit Together (size 3)
```
✅ B: maxSurge=1, maxUnavailable=0   → "add first, then remove"
   [v1][v1][v1]       3 working
   [v1][v1][v1][v2]   4 working  ← new one added first
   [v1][v1][v2]       3 working  ← then an old one removed
   ... never below 3 ✅

❌ A: maxSurge=0, maxUnavailable=1   → "remove first, then add"
   [v1][v1][v1]       3 working
   [v1][v1][ ✖ ]      2 working  ← capacity drops ❌
   [v1][v1][v2]       3 working
```

---

## 🌍 Real-World Scenario

You release new website code during business hours. You use a rolling update so customers never see downtime. Because traffic is already high, you also can't afford to run on fewer servers even briefly, so you set **maxUnavailable=0** and let the MIG **add one extra VM first (maxSurge=1)**. You pay for one extra VM for a few minutes, and capacity stays full the whole time.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Perform a rolling-action start-update with maxSurge set to 0 and maxUnavailable set to 1.

**Wrong words:**
- ✔️ "Perform a rolling-action start-update" is the right tool.
- ❌ "**maxSurge set to 0**": no extra VM may be added, so the MIG must remove an old VM **before** adding a new one.
- ❌ "**maxUnavailable set to 1**": allows one VM to be down, so capacity **drops**, which the question forbids.

**📌 When to use it:** Use it when you can't pay for even one extra VM and a short dip in capacity is OK.
🏢 **Office example:** Letting one employee leave before their replacement starts, so the desk is empty for a day.

### ✅ B
> **B.** Perform a rolling-action start-update with maxSurge set to 1 and maxUnavailable set to 0.

**Why it's correct:**

- ✔️ "**Perform a rolling-action start-update**" matches "managed instance group", "**gradually deploy**", "live web traffic": A rolling update is the MIG's built-in way to replace VMs **a few at a time** while the others keep serving users.
- ✔️ "**maxUnavailable set to 0**" matches "available capacity **does not decrease**": 0 = **zero** VMs may be out of service at any moment, so the count of working VMs never goes below normal.
- ✔️ "**maxSurge set to 1**" matches "gradually deploy" (the update must still be able to move): With 0 allowed missing, the MIG needs room to **add one extra new VM first**. Surge 1 gives that room. If surge were 0 too, the update could never start.

**Put together:** add 1 new VM → it becomes healthy → remove 1 old VM → repeat. Capacity is always 3 or 4, never 2.

**📌 When to use it:** Use it when you must update servers gradually and never run with fewer than normal.
🏢 **Office example:** The new hire starts and is trained before the old employee leaves, so every desk stays filled.

### ❌ C
> **C.** Create a new managed instance group with an updated instance template. Add the group to the backend service for the load balancer. When all instances in the new managed instance group are healthy, delete the old managed instance group.

**Wrong words:**
- ❌ "**Create a new managed instance group**": builds a **whole second fleet** by hand. It keeps capacity, but it's extra manual work when the MIG can roll itself.
- ❌ "**When all instances … are healthy, delete the old managed instance group**": this is an all-at-once switch, not a **gradual** deployment.

**📌 When to use it:** Use it when you want a full second copy ready before switching everyone over at once.
🏢 **Office example:** Setting up a whole new office floor with new staff, then moving everyone over and closing the old floor.

### ❌ D
> **D.** Create a new instance template with the new application version. Update the existing managed instance group with the new instance template. Delete the instances in the managed instance group to allow the managed instance group to recreate the instance using the new instance template.

**Wrong words:**
- ✔️ "Create a new instance template … Update the existing managed instance group" is fine.
- ❌ "**Delete the instances in the managed instance group**": the VMs go away **before** new ones exist, so capacity drops (maybe to zero) and live users get errors.

**📌 When to use it:** Use it on a test group nobody is using, where downtime doesn't matter.
🏢 **Office example:** Sending the whole team home and waiting for new hires, fine only when the office is closed.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's storefront runs on `web-mig` (3 VMs) behind the load balancer. A new checkout version ships at noon on a sale day.

```bash
# New recipe with the new code
gcloud compute instance-templates create web-template-v2 --image=shopnow-web-v2 ...

# Roll it out: add 1 new VM first, never drop below 3
gcloud compute instance-groups managed rolling-action start-update web-mig \
  --version=template=web-template-v2 --max-surge=1 --max-unavailable=0 --zone=us-central1-a
```

| Setting | Working VMs during update | Sale-day shoppers |
|---|---|---|
| **B** (surge 1, unavailable 0) | 3 → 4 → 3 → 4 → 3 | ✅ no slowdown |
| A (surge 0, unavailable 1) | 3 → 2 → 3 → 2 → 3 | ❌ slow pages at dips |
| D (delete instances) | 3 → 0 → 3 | ❌ site down |

---

## 🧠 Key Takeaways / Memory Tips

- **"Capacity must not decrease" → maxUnavailable = 0, maxSurge ≥ 1.**
  🧠 *"**Surge = add extra. Unavailable = allowed missing.** Keep capacity → add first, remove nothing."*
- "**Gradually deploy**" a MIG → `rolling-action start-update`.
- Deleting instances by hand = downtime.
- Related: **Q004** (MIG autohealing), **Q016** (MIG autoscaling), **Q043** (MIG health checks).

# Q147: Survive a Zone Failure With No Downtime at Low Cost (VMs in Two Zones Behind a Load Balancer)

**Topic:** High availability (multi-zone, load balancing, MIGs)

## ❓ Question
> You are hosting an application from Compute Engine virtual machines (VMs) in us-central1-a. You want to adjust your design to support the failure of a single Compute Engine zone, eliminate downtime, and minimize cost. What should you do?
>
> **A.** - Create Compute Engine resources in us-central1-b. - Balance the load across both us-central1-a and us-central1-b.
>
> **B.** - Create a Managed Instance Group and specify us-central1-a as the zone. - Configure the Health Check with a short Health Interval.
>
> **C.** - Create an HTTP(S) Load Balancer. - Create one or more global forwarding rules to direct traffic to your VMs.
>
> **D.** - Perform regular backups of your application. - Create a Cloud Monitoring Alert and be notified if your application becomes unavailable. - Restore from backups when notified.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs on VMs in one zone, us-central1-a.
- **What you must achieve:** Keep running if that one zone fails.
- **The limits:** No downtime and lowest cost.
- **What they're really asking:** How do you change the design to survive a zone outage?

**Clues in the question:**
- "**support the failure of a single … zone**": run VMs in a **second zone**.
- "**eliminate downtime**": a **load balancer** sends traffic to whichever zone is healthy.
- "**minimize cost**": a second zone in the **same region** (cheap, simple), not a new region.

**Exam topic:** High availability.

---

## 📚 Key Terms Explained

### 1. Zone vs region
- **What it is:** A **zone** is one data center area (us-central1-a). A **region** has several zones. Zones fail independently.
- **Looks like:** us-central1-a, us-central1-b
- **Not to be confused with:** a region.
- **Analogy:** 🏢 Two buildings on the same campus.
- **In the online store:** Storefront VMs in -a and -b.

### 2. Load balancing across zones 🔑
- **What it is:** A load balancer spreads traffic over backends in several zones and **stops sending traffic to an unhealthy zone**.
- **Looks like:** backend service with instance groups in -a and -b (or one regional MIG)
- **Not to be confused with:** DNS round-robin.
- **Analogy:** 🛎️ Reception sends visitors to whichever building is open.
- **In the online store:** Checkout survives a zone outage.

### 🔗 How they fit together
```
 Load balancer ──► VMs us-central1-a
              └──► VMs us-central1-b   (a fails → all traffic to b, no downtime) ✅
```

---

## 🌍 Real-World Scenario

A retailer's app runs in one zone. After a zone outage costs them a day of sales, they add VMs in **us-central1-b** (ideally a regional MIG) and put a **load balancer** in front. During the next zone incident, traffic moves to zone b automatically.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** - Create Compute Engine resources in us-central1-b. - Balance the load across both us-central1-a and us-central1-b.

**Why it's correct:**
- ✔️ "**Create Compute Engine resources in us-central1-b**" matches "**support the failure of a single … zone**": a second zone takes over if one fails.
- ✔️ "**Balance the load across both**" matches "**eliminate downtime**": traffic keeps flowing to the healthy zone.
- ✔️ Same region, which matches "**minimize cost**": no cross-region extras.

📌 **When to use it:** Use it when one building going dark must not stop the business.
🏢 **Office example:** Opening a second office on the same campus with a shared reception that sends visitors to whichever office is open.

### ❌ B
> **B.** - Create a Managed Instance Group and specify us-central1-a as the zone. - Configure the Health Check with a short Health Interval.

**Wrong words:**
- ✔️ A MIG with health checks replaces broken VMs.
- ❌ "**specify us-central1-a as the zone**": still only one zone. If the zone fails, everything fails.

📌 **When to use it:** Use a zonal MIG for self-healing within one zone.
🏢 **Office example:** A great staffing agency, but every worker is in the same building that just lost power.

### ❌ C
> **C.** - Create an HTTP(S) Load Balancer. - Create one or more global forwarding rules to direct traffic to your VMs.

**Wrong words:**
- ❌ "**Create an HTTP(S) Load Balancer … forwarding rules to your VMs**": a load balancer alone doesn't help if all VMs are in the failed zone.

📌 **When to use it:** Use it once you have backends in several zones.
🏢 **Office example:** A reception desk sending visitors to the only building, which is closed.

### ❌ D
> **D.** - Perform regular backups of your application. - Create a Cloud Monitoring Alert and be notified if your application becomes unavailable. - Restore from backups when notified.

**Wrong words:**
- ❌ "**Restore from backups when notified**": there's downtime while you restore, so it doesn't eliminate downtime.

📌 **When to use it:** Use backups plus alerts for disaster recovery when some downtime is OK.
🏢 **Office example:** Waiting for the building to burn, then rebuilding from photocopies.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute instance-groups managed create storefront-mig --region=us-central1 \
  --zones=us-central1-a,us-central1-b --template=storefront-v3 --size=4
```
Behind the HTTPS load balancer, if `us-central1-a` goes down, `us-central1-b` serves all shoppers.

---

## 🧠 Key Takeaways / Memory Tips

- **Survive a zone failure → VMs in 2+ zones + a load balancer** (e.g., a regional MIG).
- Same region keeps it cheap.
  🧠 *"**Two zones, one load balancer.**"*
- Related: **Q057** (MIG), **Q078** (LB), **Q054** (regions/zones).

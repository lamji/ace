# Q004: Autohealing with a Managed Instance Group

**Topic:** Compute Engine (Managed Instance Groups, health checks, autohealing vs autoscaling, load balancing)

## ❓ Question
> You want to configure autohealing for network load balancing for a group of Compute Engine instances that run in multiple zones, using the fewest possible steps. You need to configure re-creation of VMs if they are unresponsive after 3 attempts of 10 seconds each. What should you do?
>
> **A.** Create an HTTP load balancer with a backend configuration that references an existing instance group. Set the health check to healthy (HTTP)
>
> **B.** Create an HTTP load balancer with a backend configuration that references an existing instance group. Define a balancing mode and set the maximum RPS to 10.
>
> **C.** Create a managed instance group. Set the Autohealing health check to healthy (HTTP)
>
> **D.** Create a managed instance group. Verify that the autoscaling setting is on.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A group of VMs running in several zones (separate data-center buildings inside one region) sits behind a network load balancer (a traffic distributor).
- **What you must achieve:** Turn on autohealing: when a VM stops answering, it is automatically deleted and created again.
- **The limits:** A VM counts as broken after 3 failed checks, 10 seconds apart, and you want the fewest setup steps.
- **What they're really asking:** What do you set up so broken VMs are replaced automatically after 3 failed 10-second checks?

| Keyword | What it hints at |
|---|---|
| "**autohealing**" | A feature that exists only in **managed instance groups (MIGs)** |
| "**re-creation of VMs**" | Only a MIG can recreate VMs (it has a template to rebuild from) |
| "**multiple zones**" | A **regional** MIG spreads VMs across zones |
| "**3 attempts of 10 seconds each**" | Health check settings: **check interval = 10s**, **unhealthy threshold = 3** |
| "**fewest possible steps**" | Don't add extra things like a new load balancer |

**Exam topic:** Compute Engine, specifically **Managed Instance Groups + health checks + autohealing**.

---

## 📚 Key Terms Explained

### 1️⃣ Compute Engine Instance (VM)
- **What it is:** A virtual machine, meaning a computer you rent in Google's data center.
- **Analogy:** 🧑‍🍳 One **cook** in a restaurant kitchen.
- **In the online store:** One VM running the ShopNow Orders API.

### 2️⃣ Zone / Multiple Zones
- **What it is:** A zone is one isolated data center area inside a region (e.g., `asia-southeast1-a`, `-b`, `-c`). Spreading VMs across zones means one zone failing doesn't take down your app.
- **Analogy:** 🏢 Having **branches in 3 buildings** of the same city. If one building loses power, the other two keep serving.
- **In the online store:** ShopNow's API VMs run in zones `a`, `b`, and `c`.

### 3️⃣ Instance Group: Unmanaged vs Managed
- **Unmanaged instance group:** Just a **list** of VMs you created yourself, possibly all different. Google **cannot recreate** them because it doesn't know how they were built. No autohealing and no autoscaling.
- **Managed instance group (MIG):** A group of **identical VMs** created from an **instance template**. Because Google has the "recipe," it can **create, delete, and recreate** VMs automatically. It supports **autohealing**, **autoscaling**, and rolling updates.
- **Analogy:** 👥 Unmanaged = a **group chat** of random friends. Managed = a **franchise** with a recipe book: if one cook quits, HQ hires and trains an identical one.
- **In the online store:** `shopnow-api-mig`, a MIG of identical Orders API VMs.
- 🌍 **Zonal MIG** = all VMs in one zone. **Regional MIG** = VMs spread across **multiple zones** (this question's case).

### 4️⃣ Instance Template
- **What it is:** The **blueprint** for a VM: machine type, disk image, startup script, network, and so on. A MIG uses it to build every VM.
- **Analogy:** 📄 A **recipe card**. Every cook follows it, so every dish (VM) comes out the same.
- **In the online store:** `shopnow-api-template` says: e2-medium, Ubuntu, install Node.js, start the Orders API on port 8080.

### 5️⃣ Health Check
- **What it is:** Google Cloud regularly sends a small request (e.g., HTTP `GET /healthz`) to each VM to ask, *"Are you OK?"* Key settings:
  - **Check interval:** how often to check (here, **10 seconds**)
  - **Timeout:** how long to wait for an answer
  - **Unhealthy threshold:** how many failures in a row before the VM is marked unhealthy (here, **3**)
  - **Healthy threshold:** how many successes in a row before it's healthy again
- **Analogy:** 🩺 A **nurse checking a patient's pulse every 10 seconds**. Three missed pulses in a row → call the doctor.
- **In the online store:** Every 10 seconds GCP calls `http://<vm-ip>:8080/healthz`. The API replies `200 OK` if it can reach the database.

### 6️⃣ Autohealing
- **What it is:** A **MIG feature**. When the **autohealing health check** marks a VM unhealthy, the MIG **deletes and recreates** that VM from the template.
- **Analogy:** 🔧 A **self-repairing machine**. A broken part is automatically swapped for a new one.
- **In the online store:** An API VM freezes because of a memory leak, fails 3 checks (~30 seconds), and the MIG replaces it with a fresh VM. No engineer is woken up at 3 AM.

### 7️⃣ Autoscaling
- **What it is:** A **MIG feature** that **adds or removes VMs based on load** (CPU, requests per second, etc.). It's about **how many** VMs you have, not whether each one is **healthy**.
- **Analogy:** 👨‍🍳 Hiring **extra cooks during the lunch rush** and sending them home when it's quiet. It doesn't fix a cook who passed out.
- **In the online store:** On Black Friday the MIG grows from 3 VMs to 30, then shrinks back afterward.

### 8️⃣ Load Balancer (Network vs HTTP)
- **What it is:** A single front door that **spreads incoming traffic** across many VMs.
  - **Network load balancer:** works at Layer 4 (TCP/UDP), passing raw connections.
  - **HTTP(S) load balancer:** works at Layer 7 (HTTP), so it understands URLs, cookies, etc.
- Load balancers also use health checks, but only to **stop sending traffic** to an unhealthy VM. **They never recreate VMs.**
- **Analogy:** 🚦 A **host at a restaurant entrance** who seats guests at open tables. If a table is broken, the host stops seating people there but doesn't fix the table.
- **In the online store:** The load balancer receives shoppers' requests and sends each one to a healthy API VM.

### 9️⃣ Backend, Balancing Mode, and RPS
- **Backend:** The group of VMs a load balancer sends traffic to.
- **Balancing mode:** The rule for deciding when a backend is "full" (by CPU utilization or by **RPS**).
- **RPS (requests per second):** Maximum requests each VM should receive per second.
- **Analogy:** 🍽️ "Each table seats at most 10 guests." It's about **capacity**, not health.

### 🔗 How They Fit Together
```
👥 Shoppers
    │
    ▼
🚦 Load Balancer ── LB health check → "don't send traffic to sick VMs"
    │
    ▼
🏭 Regional Managed Instance Group: shopnow-api-mig
    │   📄 Instance template: shopnow-api-template (the recipe)
    │   🩺 Autohealing health check: every 10s, 3 fails → unhealthy → 🔧 RECREATE VM
    │   📈 Autoscaling (optional): more load → more VMs
    │
    ├── zone a: 🖥️ api-vm-1   ✅
    ├── zone b: 🖥️ api-vm-2   ❌ (froze) → deleted → 🖥️ api-vm-2 (new) ✅
    └── zone c: 🖥️ api-vm-3   ✅
```

---

## 🌍 Real-World Scenario

Your app runs on a group of VMs. Sometimes a VM **freezes** (memory leak, crashed process, stuck disk). It's still "running" as far as Google is concerned, but your app isn't responding. Without autohealing, an engineer has to notice, log in, and fix or replace it by hand, maybe at 3 AM.

With a **MIG + autohealing health check**, Google detects the frozen VM in about 30 seconds (3 × 10s) and **replaces it automatically**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an HTTP load balancer with a backend configuration that references an existing instance group. Set the health check to healthy (HTTP)

**Why it's wrong:**
- ❌ A **load balancer's** health check only **stops sending traffic** to unhealthy VMs. It **does not recreate** them.
- ❌ An "existing instance group" might be **unmanaged**, which can't recreate VMs at all.
- ❌ The question says **network** load balancing, but this creates an **HTTP** load balancer, which is a different type. It also adds an extra step, so it isn't the fewest steps.

**📌 When to use it:** Use it when you just want to **stop sending visitors to a broken server**, without replacing it.
🏢 **Office example:** A receptionist who stops sending visitors to a staff member who's out sick, but doesn't hire a replacement.

### ❌ B
> **B.** Create an HTTP load balancer with a backend configuration that references an existing instance group. Define a balancing mode and set the maximum RPS to 10.

**Why it's wrong:**
- ❌ **Balancing mode and max RPS** control **how much traffic** each VM gets (capacity). They have **nothing to do with health** or recreating VMs.
- ⚠️ **Trap option:** the "10" looks like the "10 seconds" in the question, but **10 RPS** means 10 requests per second, which is a completely different thing.
- ❌ It has the same problems as A: wrong load balancer type and no recreation.

**📌 When to use it:** Use it when you want to **limit how much work each server gets**.
🏢 **Office example:** A rule that each cashier serves at most 10 customers a minute. Extra customers go to the next cashier.

### ✅ C
> **C.** Create a managed instance group. Set the Autohealing health check to healthy (HTTP)

**Why it's correct:**
- ✔️ **Autohealing is a MIG feature.** Only a MIG can **recreate** VMs, because it has an instance template.
- ✔️ The **autohealing health check** is where you set **check interval = 10s** and **unhealthy threshold = 3**, which matches "3 attempts of 10 seconds each."
- ✔️ A **regional** MIG covers **multiple zones**.
- ✔️ **Fewest steps:** create the MIG and attach the health check. Done.

**📌 When to use it:** Use it when **broken servers must be replaced automatically**.
🏢 **Office example:** A staffing agency contract. If a worker gets sick, the agency sends an identical trained replacement right away.

### ❌ D
> **D.** Create a managed instance group. Verify that the autoscaling setting is on.

**Why it's wrong:**
- ✔️ A MIG is the right resource.
- ❌ **Autoscaling ≠ autohealing.** Autoscaling changes the **number** of VMs based on **load**. It does **not** replace a frozen VM.
- ⚠️ **Trap option:** "auto-scaling" and "auto-healing" sound similar, but they do completely different jobs.

**📌 When to use it:** Use it when the **amount of work goes up and down** and you want more servers only when it's busy.
🏢 **Office example:** Hiring temporary staff during tax season, then letting them go when it's quiet.

---

## 🛒 E-Commerce Full-Stack Example

```
🛍️ Shoppers ──► 🚦 Load Balancer ──► 🏭 Regional MIG: shopnow-api-mig (asia-southeast1)
                                        ├─ zone a: Orders API VM
                                        ├─ zone b: Orders API VM
                                        └─ zone c: Orders API VM
                                              │
                                              ▼
                                        🗄️ Cloud SQL (orders)
```

**1. The Orders API exposes a health endpoint (Node.js/Express):**
```javascript
app.get('/healthz', async (req, res) => {
  try {
    await db.query('SELECT 1');      // can we reach the database?
    res.status(200).send('OK');      // ✅ healthy
  } catch (e) {
    res.status(500).send('DB down'); // ❌ unhealthy
  }
});
```

**2. Create the autohealing health check (10s interval, 3 failures):**
```bash
gcloud compute health-checks create http shopnow-api-hc \
  --port=8080 \
  --request-path=/healthz \
  --check-interval=10s \
  --timeout=5s \
  --unhealthy-threshold=3 \
  --healthy-threshold=2
```

**3. Create the regional MIG with autohealing attached:**
```bash
gcloud compute instance-groups managed create shopnow-api-mig \
  --template=shopnow-api-template \
  --size=3 \
  --region=asia-southeast1 \
  --health-check=shopnow-api-hc \
  --initial-delay=300        # give new VMs 5 min to boot before checking
```

💡 **Tip:** Also add a firewall rule that allows Google's health-check probes (`35.191.0.0/16` and `130.211.0.0/22`) to reach port 8080. Otherwise every VM looks unhealthy and gets recreated over and over.

**🎬 What happens on Black Friday:**
- **8:00 PM:** A memory leak freezes the API VM in zone b.
- **8:00:10, 8:00:20, 8:00:30:** 3 health checks fail.
- **8:00:30:** The MIG marks it unhealthy, **deletes it, and creates a new VM** from `shopnow-api-template`. 🔧
- Meanwhile, the load balancer stops sending shoppers to the sick VM, so customers barely notice. ✅

**With the other options:**
- **A / B (only a load balancer):** Traffic avoids the frozen VM, but it **stays frozen forever**. You now have 2 VMs doing the work of 3 until someone fixes it by hand. ❌
- **D (only autoscaling):** If load rises, the MIG might add VMs, but the **frozen VM is never replaced**. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Recreate unhealthy VMs" / "autohealing" → Managed Instance Group + autohealing health check.**
- **"3 attempts of 10 seconds" → health check: `check-interval=10s`, `unhealthy-threshold=3`.**
- **Load balancer health check = stop sending traffic. MIG autohealing health check = recreate the VM.**
  🧠 *"The load balancer **avoids** sick VMs. The MIG **heals** them."*
- **Autoscaling = how MANY VMs. Autohealing = are they HEALTHY.**
  🧠 *"Scaling = size. Healing = health."*
- **Multiple zones → regional MIG.**

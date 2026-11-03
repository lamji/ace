# Q016: Autoscaling a VM-Based Application on CPU Usage

**Topic:** Compute Engine (instance templates, Managed Instance Groups, CPU-based autoscaling vs schedule-based, GKE HPA)

## ❓ Question
> You have a single binary application that you want to run on Google Cloud Platform. You decided to automatically scale the application based on underlying infrastructure CPU usage. Your organizational policies require you to use virtual machines directly. You need to ensure that the application scaling is operationally efficient and completed as quickly as possible. What should you do?
>
> **A.** Create a Google Kubernetes Engine cluster, and use horizontal pod autoscaling to scale the application.
>
> **B.** Create an instance template, and use the template in a managed instance group with autoscaling configured.
>
> **C.** Create an instance template, and use the template in a managed instance group that scales up and down based on the time of day.
>
> **D.** Use a set of third-party tools to build automation around scaling the application up and down, based on Stackdriver CPU usage monitoring.

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You have **one program** that you want to run on **VMs** (company rule). When the VMs' **CPU gets busy**, more VMs should be added **automatically**, and when it's quiet, they should be removed. You want this to be **easy to manage** and **fast**. What do you use?

| Keyword | What it hints at |
|---|---|
| "**single binary application**" | One program, easy to put on identical VMs |
| "**scale based on ... CPU usage**" | **Autoscaling on CPU utilization** |
| "**use virtual machines directly**" | **Compute Engine VMs**, not GKE/containers |
| "**operationally efficient**" | Use a **built-in, managed** feature, not homemade tools |
| "**as quickly as possible**" | Google's autoscaler reacts automatically within minutes |

**Exam topic:** Compute Engine, specifically **Managed Instance Groups + autoscaling**.

*(Review: in **Q004**, autoscaling was the **wrong** answer because the question asked about **replacing broken VMs** (autohealing). Here the question is about **adding VMs when CPU is busy**, so autoscaling is **right**.)*

---

## 📚 Key Terms Explained

### 1️⃣ Single Binary Application
- **What it is:** An app built as **one executable file** (e.g., a compiled Go or C++ program). You copy it to a server and run it.
- **Analogy:** 🧰 A **single all-in-one tool**. Hand it to any worker and they can use it immediately.
- **In the online store:** `shopnow-search`, a compiled program that powers product search.

### 2️⃣ Autoscaling and CPU Usage
- **CPU usage (utilization):** How busy a VM's processor is (0–100%).
- **Autoscaling:** Automatically **adding VMs** when they're busy and **removing VMs** when they're quiet.
- **Analogy:** 👷 Bringing in **more workers** when everyone is overloaded, and sending some home when it's slow.

### 3️⃣ Organizational Policy ("use VMs directly")
- **What it is:** A **company rule** that limits which technologies teams can use. Here: run apps on **Compute Engine VMs**, not on containers/Kubernetes or serverless.
- **Analogy:** 📜 A **company policy** like "all staff must work from the main office."

### 4️⃣ Instance Template (review from Q004)
- **What it is:** The **blueprint** for a VM: machine type, disk image, startup script (e.g., "download and start `shopnow-search`").
- **Analogy:** 📄 A **recipe card**. Every new VM is built exactly the same.

### 5️⃣ Managed Instance Group (MIG) (review from Q004)
- **What it is:** A group of **identical VMs** made from an instance template, with **autoscaling**, **autohealing**, and rolling updates built in.
- **Analogy:** 🏭 A **staffing agency** with a recipe book. It can add, remove, or replace identical workers anytime.

### 6️⃣ MIG Autoscaling Policies
| Policy | Scales on | Example |
|---|---|---|
| **CPU utilization** ✅ (this question) | Average CPU across VMs | "Keep CPU around 60%" |
| **Load balancer serving capacity** | Requests per second per VM | "Max 100 RPS per VM" |
| **Cloud Monitoring metrics** | Any custom metric | "Queue length > 1,000" |
| **Schedules** | Time of day / day of week | "10 VMs every Friday at noon" |
- You can **combine** them. The autoscaler uses whichever asks for the **most** VMs.

### 7️⃣ GKE + Horizontal Pod Autoscaler (HPA)
- **GKE:** Google's managed **Kubernetes** (review from Q012). Apps run in **containers** (Pods), not directly on VMs.
- **HPA:** Adds or removes **Pods** (not VMs) based on CPU or other metrics.
- **Analogy:** 🏢 A **shared coworking floor**. The building manager adds **desks** for your team, but you don't control the **rooms** (VMs) directly.

### 8️⃣ Stackdriver → Cloud Monitoring
- **What it is:** **Stackdriver** is the **old name** for Google's monitoring and logging tools, now called **Cloud Monitoring** and **Cloud Logging**. It collects metrics like CPU usage.
- **Analogy:** 📊 The office's **dashboard of meters**: electricity, temperature, how busy each desk is.

### 9️⃣ Third-Party Tools / Custom Automation
- **What it is:** Building your **own** scaling system with outside tools and scripts: read CPU from monitoring, then create or delete VMs yourself.
- **Analogy:** 🛠️ Building a **homemade timekeeping system** when the company already pays for HR software that does it.

### 🔗 How They Fit Together
```
📄 Instance template: shopnow-search-template
   (e2-medium, Debian, startup script: download + run ./shopnow-search)
        │
        ▼
🏭 Managed Instance Group: shopnow-search-mig
        │
        ├── 📈 Autoscaler policy: target CPU 60%, min 2, max 20
        │       CPU 85% → add VMs ➕      CPU 25% → remove VMs ➖
        │
        ├── 🖥️ VM  🖥️ VM  (quiet: 2 VMs)
        └── 🖥️ VM ×12      (sale: 12 VMs)

📊 Cloud Monitoring (formerly Stackdriver) supplies the CPU numbers, built in, no extra tools
```

---

## 🌍 Real-World Scenario

Many companies have older or compiled apps that **must run on VMs** (security rules, licensing, or simply company policy). Traffic goes up and down during the day. Running **too few** VMs makes the app slow, and running **too many** wastes money.

Google's built-in answer is to build **one instance template**, put it in a **MIG**, and turn on **CPU-based autoscaling**. Google watches CPU and adds or removes VMs **automatically**, with no scripts to maintain.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Google Kubernetes Engine cluster, and use horizontal pod autoscaling to scale the application.

**Why it's wrong:**
- ❌ The company policy says **use VMs directly**. GKE runs apps in **containers (Pods)** managed by Kubernetes, not directly on VMs.
- ❌ HPA scales **Pods**, not VMs. (Adding VMs to the cluster is a separate feature, the cluster autoscaler.)
- ❌ You'd also need to **containerize** the binary and run a cluster, which is more work.

**📌 When to use it:** Use it when your app is **packaged as containers** and **many apps share one Kubernetes setup**.
🏢 **Office example:** A **shared coworking floor** where the building manager **adds more desks** for your team when you're busy.

### ✅ B
> **B.** Create an instance template, and use the template in a managed instance group with autoscaling configured.

**Why it's correct:**
- ✔️ Uses **VMs directly** (Compute Engine), so it **follows the company policy**.
- ✔️ The **instance template** makes every new VM identical and ready to run the binary.
- ✔️ **MIG autoscaling** on **CPU utilization** is **built in and fully managed**, so it's **operationally efficient**.
- ✔️ The autoscaler reacts **automatically** when CPU rises, so it's **fast**.

**📌 When to use it:** Use it when your program runs on **your own servers**, and you want **more servers added automatically when they get busy**.
🏢 **Office example:** A **staffing agency** that sends **more identical workers** when everyone is overloaded, and sends them home when it's quiet.

### ❌ C
> **C.** Create an instance template, and use the template in a managed instance group that scales up and down based on the time of day.

**Why it's wrong:**
- ✔️ A MIG with an instance template is the right setup.
- ❌ But **time-of-day (schedule) scaling** follows the **clock**, not **CPU usage**. The question says scale based on **CPU**.
- ❌ If traffic spikes at an unexpected time (like a viral post at 3 AM), a schedule won't react.

**📌 When to use it:** Use it when you **know in advance when it gets busy**, like the same hours every day.
🏢 **Office example:** **Scheduling extra cashiers every lunch hour** (11 AM to 2 PM), because you know it's always busy then.

### ❌ D
> **D.** Use a set of third-party tools to build automation around scaling the application up and down, based on Stackdriver CPU usage monitoring.

**Why it's wrong:**
- ❌ You'd **build and maintain your own** scaling system (scripts, tools, error handling), which is **not operationally efficient**.
- ❌ It's **slower** to build and more likely to break than Google's **built-in** MIG autoscaler, which already does exactly this.
- (Stackdriver is now called **Cloud Monitoring**.)

**📌 When to use it:** Use it **only when the built-in tools can't do what you need**. For CPU-based VM scaling, use B instead.
🏢 **Office example:** Building a **homemade timekeeping system** when the company already pays for HR software that does it.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **product search** is a compiled Go program, `shopnow-search` (a single binary). Company policy says it must run on **Compute Engine VMs**. During flash sales, thousands of shoppers search at once, and CPU spikes.

```
🛍️ Shoppers ──"red shoes size 9"──► 🚦 Load Balancer
                                        │
                                        ▼
                       🏭 MIG: shopnow-search-mig (asia-southeast1)
                          📈 Autoscaler: target CPU 60%, min 2, max 20
                          ├─ quiet:      🖥️🖥️                (2 VMs)
                          └─ flash sale: 🖥️🖥️🖥️🖥️🖥️🖥️🖥️🖥️ (8+ VMs)
```

**1. Instance template (the recipe):**
```bash
gcloud compute instance-templates create shopnow-search-template \
  --machine-type=e2-medium \
  --image-family=debian-12 --image-project=debian-cloud \
  --metadata-from-file=startup-script=start-search.sh   # downloads & runs ./shopnow-search
```

**2. Managed instance group from the template:**
```bash
gcloud compute instance-groups managed create shopnow-search-mig \
  --template=shopnow-search-template \
  --size=2 \
  --region=asia-southeast1
```

**3. Turn on CPU-based autoscaling (option B):**
```bash
gcloud compute instance-groups managed set-autoscaling shopnow-search-mig \
  --region=asia-southeast1 \
  --min-num-replicas=2 \
  --max-num-replicas=20 \
  --target-cpu-utilization=0.60 \
  --cool-down-period=90        # give new VMs 90s to start before judging their CPU
```

**🎬 Flash sale at 12:00:** CPU jumps to 85% → the autoscaler adds VMs → CPU settles back near 60%. At 2 PM, traffic drops → VMs are removed → ShopNow stops paying for idle servers. ✅

**💡 Bonus: combine B with a schedule (C) when you know a sale is coming:**
```bash
gcloud compute instance-groups managed update-autoscaling shopnow-search-mig \
  --region=asia-southeast1 \
  --set-schedule=friday-flash-sale \
  --schedule-cron="0 11 * * 5" \
  --schedule-duration-sec=10800 \
  --schedule-min-required-replicas=8 \
  --schedule-time-zone="Asia/Manila"
```
→ 8 VMs are ready **before** the Friday sale starts, and CPU autoscaling still handles any surprise spikes.

---

## 🧠 Key Takeaways / Memory Tips

- **"VMs + autoscale on CPU" → Instance template + Managed Instance Group + autoscaling (CPU utilization).**
- **"Use VMs directly" → not GKE, not App Engine, not Cloud Run.**
- **Schedule-based scaling = by the clock. CPU-based = by actual load.** Match what the question asks.
- **Built-in > homemade.** "Operationally efficient" means use Google's managed feature, not third-party scripts.
- **Stackdriver = old name for Cloud Monitoring / Cloud Logging.**
- **HPA scales Pods (containers), MIG autoscaler scales VMs.**
- 🧠 *"**Template → Group → Autoscale.** Recipe card → staffing agency → hire more when busy."*

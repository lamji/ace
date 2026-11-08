# Q011: Provisioning VMs from a Configuration File (Infrastructure as Code)

**Topic:** Infrastructure as Code (Deployment Manager / Infrastructure Manager / Terraform) vs Cloud Composer vs instance groups

## ❓ Question
> You need a dynamic way of provisioning VMs on Compute Engine. The exact specifications will be in a dedicated configuration file. You want to follow Google's recommended practices. Which method should you use?
>
> **A.** Deployment Manager
>
> **B.** Cloud Composer
>
> **C.** Managed Instance Group
>
> **D.** Unmanaged Instance Group

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You need to create VMs on Compute Engine automatically. All their details (size, disk, operating system image) are written in a separate configuration file.
- **What you must achieve:** A repeatable way to create VMs from that file.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** Which tool or method creates VMs from a configuration file the recommended way?

| Keyword | What it hints at |
|---|---|
| "**provisioning VMs**" | **Creating** infrastructure |
| "**dedicated configuration file**" | **Infrastructure as Code (IaC)**: describe infrastructure in a file |
| "**dynamic way**" | Run the file again anytime to create, update, or recreate |
| "**Google's recommended practices**" | Google's own IaC tool: **Deployment Manager** (in this older question) |

**Exam topic:** Resource deployment, specifically **Infrastructure as Code**.

⚠️ **Update:** This question is older. Google has **deprecated Deployment Manager** (end of support announced for **March 31, 2026**) and now recommends **Infrastructure Manager**, which runs **Terraform**. The idea is the same: infrastructure described in a config file. If a newer exam version offers **Terraform / Infrastructure Manager**, choose that. If it offers only these four options, choose **Deployment Manager**.

---

## 📚 Key Terms Explained

### 1️⃣ Provisioning
- **What it is:** **Creating and setting up** infrastructure (VMs, networks, disks, databases) so it's ready to use.
- **Analogy:** 🏢 Setting up a **new office**: desks, computers, phones, and internet, all ready before staff arrive.
- **In the online store:** Creating the VMs, network, and firewall rules that the ShopNow API runs on.

### 2️⃣ Configuration File
- **What it is:** A text file (usually **YAML**, or **HCL** for Terraform) that **describes exactly what to build**: "one VM, type e2-medium, in asia-southeast1-a, with a Debian disk."
- **Analogy:** 📐 An **architect's blueprint**. The builders follow it exactly, and you can build the same building again from it.
- **In the online store:** `shopnow-infra.yaml` lists every ShopNow VM and network.

### 3️⃣ Infrastructure as Code (IaC)
- **What it is:** Managing infrastructure by **writing config files** instead of clicking. The files can be stored in **Git**, reviewed, reused, and run again.
- **Why it's good:**
  - ✔️ **Repeatable:** build identical dev, staging, and prod environments
  - ✔️ **Version history:** see who changed what, and roll back
  - ✔️ **No manual mistakes:** no forgotten checkbox in the Console
- **Analogy:** 📋 A **written setup checklist** for opening a new branch. Every branch is set up the same, instead of depending on someone's memory.

### 4️⃣ Deployment Manager
- **What it is:** Google Cloud's **original IaC service**. You write a **YAML config** (optionally with Jinja/Python **templates**), and it creates the resources as one **deployment**. Change the file, run an update, and it changes the resources to match.
- **Analogy:** 🏗️ A **construction company** that builds exactly what's on the blueprint, and remodels when you hand in a new blueprint.
- **In the online store:** `gcloud deployment-manager deployments create shopnow-infra --config=shopnow-infra.yaml`
- ⚠️ **Deprecated**, replaced by **Infrastructure Manager (Terraform)**.

### 5️⃣ Terraform / Infrastructure Manager
- **Terraform:** The most popular IaC tool, used for Google Cloud, AWS, Azure, and others. Config files are written in **HCL** (`.tf` files).
- **Infrastructure Manager:** Google's **managed service that runs Terraform** for you. It's the current recommendation.
- **Analogy:** 🏗️ A newer construction company that can build in **any city** (any cloud), not just one.

### 6️⃣ Cloud Composer
- **What it is:** Google's managed **Apache Airflow**, a tool that **schedules and runs workflows**: a series of tasks in order (a **DAG**), e.g., "every night at 2 AM: export data → clean it → load it into BigQuery → email a report."
- It's for **data pipelines and task scheduling**, **not** for describing infrastructure in a config file.
- **Analogy:** 📅 An **office manager with a checklist** who makes sure each task happens in the right order, at the right time.

### 7️⃣ Managed vs Unmanaged Instance Group (review from Q004)
- **Managed Instance Group (MIG):** Many **identical VMs** built from an **instance template**, with **autoscaling** and **autohealing**.
- **Unmanaged Instance Group:** A **list of existing, possibly different VMs**, grouped mainly so a load balancer can send traffic to them. No autoscaling or autohealing.
- Neither one is a way to **define your infrastructure in a config file**.

### 🔗 How They Fit Together
```
📐 Config file (shopnow-infra.yaml  or  main.tf)   ← Infrastructure as Code, stored in Git
        │
        │  Deployment Manager (old)  /  Infrastructure Manager + Terraform (current)
        ▼
🏗️ Google Cloud builds exactly what the file says:
        ├── 🏘️ VPC + subnet
        ├── 🔥 Firewall rules
        ├── 🖥️ VM: shopnow-api-vm
        └── 🏭 (can even create a MIG with an instance template)

📅 Cloud Composer  → runs WORKFLOWS (tasks in order on a schedule), not infrastructure
👥 Instance groups → GROUP VMs (MIG = identical + auto; unmanaged = just a list)
```

---

## 🌍 Real-World Scenario

A company needs the **same setup** in dev, staging, and prod. If engineers click through the Console each time, the environments slowly **drift apart** ("it works in staging but not in prod!"), and nobody remembers exactly how prod was built.

With **Infrastructure as Code**, the whole setup lives in a **config file in Git**. Need a new environment? Run the file. Need to change the machine type? Edit one line, get it reviewed, and apply it. Every change is recorded.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deployment Manager

**Why it's correct:**
- ✔️ It's Google's IaC tool: it **reads a configuration file** and **provisions** the resources described in it.
- ✔️ It's **dynamic**: edit the file and run an update, and the VMs change to match. Templates let you reuse configs with different values.
- ✔️ For this question's time period, it's **Google's recommended practice** for config-file provisioning.
- ⚠️ Today Google recommends **Infrastructure Manager (Terraform)** instead, but it's the same idea.

**📌 When to use it:** Use it when you want to **build things automatically from a written plan**, the same way every time.
🏢 **Office example:** Giving the facilities team a **written setup plan** ("5 desks, 2 printers, 1 meeting room"), so every new branch office is set up exactly the same.

### ❌ B
> **B.** Cloud Composer

**Why it's wrong:**
- ❌ Cloud Composer **schedules and runs workflows** (data pipelines, tasks in order). It's **not** a tool for defining VMs in a config file.
- ❌ You *could* make a workflow that calls other tools to create VMs, but that's a complicated workaround, not the recommended practice.

**📌 When to use it:** Use it when you have **many tasks that must run in a certain order, on a schedule**.
🏢 **Office example:** The **month-end checklist**: first collect receipts, then balance the books, then send the report to the boss, in that order, every month.

### ❌ C
> **C.** Managed Instance Group

**Why it's wrong:**
- ❌ A MIG **runs many identical copies** of one VM (from an instance template) and handles autoscaling and autohealing. It's **not** a way to describe your infrastructure in a dedicated config file.
- ❌ You still have to create the MIG and its template somehow, ideally **with** an IaC tool like Deployment Manager.

**📌 When to use it:** Use it when you need **many identical servers** that **grow, shrink, and replace themselves** automatically.
🏢 **Office example:** A **staffing agency** that sends identical trained workers, adds more when it's busy, and replaces anyone who gets sick.

### ❌ D
> **D.** Unmanaged Instance Group

**Why it's wrong:**
- ❌ An unmanaged group is just a **list of VMs you already created by hand**. It doesn't create VMs at all, and it has no config file, autoscaling, or autohealing.
- ❌ It's the **least** "dynamic" option.

**📌 When to use it:** Use it when you have **a few different servers that already exist** and just want to **group them together**.
🏢 **Office example:** Putting existing staff with different jobs (one accountant, one designer) on **one team list**, so the receptionist knows where to send visitors.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow wants **identical staging and production** environments for its Orders API, defined in a file stored in Git.

```
📁 Git repo: shopnow-infra/
   ├── shopnow-infra.yaml   (Deployment Manager)   or   main.tf  (Terraform)
   └── reviewed in a pull request before every change
          │
          ▼
🏗️ Deployment Manager / Infrastructure Manager
          │
          ├──► 🧪 staging: shopnow-api-vm (e2-small)
          └──► 🚀 prod:    shopnow-api-vm (e2-standard-4)
```

**Option A: Deployment Manager config (`shopnow-infra.yaml`):**
```yaml
resources:
- name: shopnow-api-vm
  type: compute.v1.instance
  properties:
    zone: asia-southeast1-a
    machineType: zones/asia-southeast1-a/machineTypes/e2-medium
    disks:
    - deviceName: boot
      type: PERSISTENT
      boot: true
      autoDelete: true
      initializeParams:
        sourceImage: projects/debian-cloud/global/images/family/debian-12
    networkInterfaces:
    - network: global/networks/default
```
```bash
# Create everything in the file
gcloud deployment-manager deployments create shopnow-infra --config=shopnow-infra.yaml

# Later: edit the file (e.g., change machine type), then apply the change
gcloud deployment-manager deployments update shopnow-infra --config=shopnow-infra.yaml
```

**The modern way (Terraform, run by Infrastructure Manager), same idea:**
```hcl
resource "google_compute_instance" "api" {
  name         = "shopnow-api-vm"
  machine_type = "e2-medium"
  zone         = "asia-southeast1-a"

  boot_disk {
    initialize_params { image = "debian-cloud/debian-12" }
  }
  network_interface { network = "default" }
}
```

**🎬 Why it matters for ShopNow:**
- Before Black Friday, the team changes `e2-medium` → `e2-standard-4` in **one line**, a teammate reviews it, and they apply it. ✅
- A bug appears only in prod? They compare the staging and prod config files and spot the difference in minutes. ✅
- **Without IaC:** someone clicked "create VM" months ago, nobody remembers the settings, and staging doesn't match prod. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Configuration file" + "provisioning" → Infrastructure as Code → Deployment Manager** (older exams) / **Terraform + Infrastructure Manager** (current).
- **Cloud Composer = workflow scheduler (Apache Airflow)**, not infrastructure.
- **MIG = many identical VMs that scale and heal. Unmanaged group = a list of existing VMs.** Neither defines infrastructure in a file.
- 🧠 *"**Blueprint → builder.** Config file = blueprint, Deployment Manager / Terraform = builder."*
- 🧠 *"**Composer** = **composes** tasks into a workflow, like a conductor leading an orchestra."*

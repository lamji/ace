# Q084: Daily List of VMs in Two Projects (gcloud Configurations + Script)

**Topic:** gcloud CLI (configurations, gcloud compute instances list, gcloud vs gsutil)

## ❓ Question
> You have a Google Cloud Platform account with access to both production and development projects. You need to create an automated process to list all compute instances in development and production projects on a daily basis. What should you do?
>
> **A.** Create two configurations using gcloud config. Write a script that sets configurations as active, individually. For each configuration, use gcloud compute instances list to get a list of compute resources.
>
> **B.** Create two configurations using gsutil config. Write a script that sets configurations as active, individually. For each configuration, use gsutil compute instances list to get a list of compute resources.
>
> **C.** Go to Cloud Shell and export this information to Cloud Storage on a daily basis.
>
> **D.** Go to GCP Console and export this information to Cloud SQL on a daily basis.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Every day, a script must list all VMs in **two projects** (dev and prod). How do you set that up?

**Clues in the question:**
- "**automated process**": a **script** that runs by itself, not someone clicking in the console every day.
- "**development and production projects**": two projects, so the script must **switch between them**. gcloud **configurations** save one setup per project.
- "**list all compute instances**": the command is `gcloud compute instances list`. **gsutil** is only for Cloud Storage.

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1️⃣ gcloud configuration 🔑
- **What it is:** A **saved set of gcloud settings** (account, project, default region/zone) with a name. You can keep several and switch with one command.
- **Looks like:**
  ```bash
  gcloud config configurations create dev
  gcloud config set project shopnow-dev
  gcloud config configurations create prod
  gcloud config set project shopnow-prod
  gcloud config configurations activate dev
  ```
- **Not to be confused with:** a project. A configuration just **points gcloud at** a project.
- **Analogy:** 🗂️ **Saved profiles** on the office printer: "Accounting floor" and "HR floor". Pick one and it knows where to send things.
- **In the online store:** `dev` → `shopnow-dev`, `prod` → `shopnow-prod`.

### 2️⃣ gcloud compute instances list
- **What it is:** A command that **prints every VM in the active project**: name, zone, status, IPs.
- **Looks like:** `NAME  ZONE  MACHINE_TYPE  STATUS` / `web-1  us-central1-a  e2-medium  RUNNING`

### 3️⃣ gsutil
- **What it is:** The older command-line tool **for Cloud Storage only** (buckets and files). It has **no** `compute` commands.
- **Looks like:** `gsutil ls gs://shopnow-images`
- **Not to be confused with:** gcloud, which handles almost every Google Cloud service.

### 🔗 How they fit together
```
 script (runs daily via cron / Cloud Scheduler)
   ├── gcloud config configurations activate dev  → gcloud compute instances list
   └── gcloud config configurations activate prod → gcloud compute instances list ✅
```

---

## 🌍 Real-World Scenario

An ops team must report every morning which VMs exist in dev and prod, to catch forgotten (and costly) machines. The engineer creates a gcloud configuration per project and writes a small script that switches configurations and lists the VMs. A scheduler runs it daily.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create two configurations using gcloud config. Write a script that sets configurations as active, individually. For each configuration, use gcloud compute instances list to get a list of compute resources.

**Why it's correct:**
- ✔️ "**Create two configurations using gcloud config**" matches "**development and production projects**": one saved configuration per project.
- ✔️ "**Write a script that sets configurations as active, individually**" matches "**automated process … on a daily basis**": a script can run every day by itself and switch projects.
- ✔️ "**gcloud compute instances list**" matches "**list all compute instances**": this is the exact command that lists VMs.

📌 **When to use it:** Use it when the same job must be repeated automatically for several places.
🏢 **Office example:** A printer with saved profiles for two floors, and a scheduled job that prints the asset list for each floor every morning.

### ❌ B
> **B.** Create two configurations using gsutil config. Write a script that sets configurations as active, individually. For each configuration, use gsutil compute instances list to get a list of compute resources.

**Wrong words:**
- ❌ "**gsutil config**": gsutil can't create named configurations like this.
- ❌ "**gsutil compute instances list**": this command doesn't exist. gsutil is for Cloud Storage only.

📌 **When to use it:** Use gsutil when you're copying or listing files in Cloud Storage buckets.
🏢 **Office example:** Asking the file clerk for a list of company cars. Wrong person.

### ❌ C
> **C.** Go to Cloud Shell and export this information to Cloud Storage on a daily basis.

**Wrong words:**
- ❌ "**Go to Cloud Shell … on a daily basis**": someone has to open Cloud Shell by hand every day. That's not automated.
- ❌ It also doesn't say **how** to get the list from both projects.

📌 **When to use it:** Use Cloud Shell for quick one-time commands in the browser.
🏢 **Office example:** Walking around the building every morning to count the computers yourself.

### ❌ D
> **D.** Go to GCP Console and export this information to Cloud SQL on a daily basis.

**Wrong words:**
- ❌ "**Go to GCP Console … on a daily basis**": manual clicking every day, not automated.
- ❌ "**export this information to Cloud SQL**": the console has no "export VM list to Cloud SQL" button, and a database isn't needed for a simple list.

📌 **When to use it:** **Never use this.** Script it with gcloud configurations (A).
🏢 **Office example:** Typing the computer count into the accounting system by hand every morning.

---

## 🛒 E-Commerce Full-Stack Example

```bash
#!/bin/bash
# daily-vm-report.sh (cron: 0 7 * * *)
for cfg in dev prod; do
  gcloud config configurations activate "$cfg"
  echo "== $cfg =="
  gcloud compute instances list --format="table(name,zone,status)"
done > /reports/vms-$(date +%F).txt
```
Every morning ShopNow's ops team sees, for example, that `test-big-vm` has been running in dev for 9 days, and shuts it down.

*(Tip: `gcloud compute instances list --project=shopnow-prod` also works without switching configurations.)*

---

## 🧠 Key Takeaways / Memory Tips

- **Several projects/accounts in gcloud → configurations** (`gcloud config configurations create/activate`).
- **gsutil = Cloud Storage only.** There's no "gsutil compute".
- "Automated / daily" → a **script**, never "go to the console every day".
  🧠 *"**Many projects? Many configurations.**"*
- Related: **Q075** (`gcloud services list --project`).

# Q181: New Project Made With gcloud: Prerequisite Before Creating a VM (Enable compute.googleapis.com)

**Topic:** APIs (enabling Compute Engine API)

## ❓ Question
> You have created a new project in Google Cloud through the gcloud command line interface (CLI) and linked a billing account. You need to create a new Compute Engine instance using the CLI. You need to perform the prerequisite steps. What should you do?
>
> **A.** Create a Cloud Monitoring Workspace.
>
> **B.** Create a VPC network in the project.
>
> **C.** Enable the compute googleapis.com API.
>
> **D.** Grant yourself the IAM role of Computer Admin.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You created a new project with the gcloud CLI and linked a billing account.
- **What you must achieve:** Create a Compute Engine VM from the command line.
- **The limits:** Do the required setup steps first.
- **What they're really asking:** What must you set up before you can create the VM?

**Clues in the question:**
- "**new project … through the gcloud CLI**": APIs are **not** enabled automatically → **enable `compute.googleapis.com`**.
- Enabling the Compute API also creates the **default VPC**, so you don't need to make one.

**Exam topic:** APIs.

---

## 📚 Key Terms Explained

### 1. compute.googleapis.com 🔑
- **What it is:** The **Compute Engine API**. It must be enabled before any VM can be created in the project.
- **Looks like:** `gcloud services enable compute.googleapis.com`
- **Not to be confused with:** IAM roles.
- **Analogy:** 💡 The main power switch for the VM room.
- **In the online store:** Before the first ShopNow VM.

### 2. Default VPC
- **What it is:** A network created automatically when the Compute API is enabled.
- **Looks like:** `default` with a subnet per region
- **Not to be confused with:** a custom VPC.
- **Analogy:** 🛣️ Streets that come with the neighborhood.
- **In the online store:** Quick test VMs.

### 🔗 How they fit together
```
 create project → link billing → enable compute API ✅ (default VPC appears) → create VM
```

---

## 🌍 Real-World Scenario

An engineer scripts project setup with gcloud. The first `instances create` fails with "API not enabled" until they run `gcloud services enable compute.googleapis.com`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Monitoring Workspace.

**Wrong words:**
- ❌ "**Cloud Monitoring Workspace**": optional, not needed to create a VM.

📌 **When to use it:** Use it to watch several projects' metrics in one place.
🏢 **Office example:** Installing security cameras before the office has power.

### ❌ B
> **B.** Create a VPC network in the project.

**Wrong words:**
- ❌ "**Create a VPC network**": enabling the Compute API creates the default VPC, and you can't create a VPC before the API is on anyway.

📌 **When to use it:** Use a custom VPC when you need your own IP plan.
🏢 **Office example:** Building roads before the town is founded.

### ✅ C
> **C.** Enable the compute googleapis.com API.

**Why it's correct:**
- ✔️ "**Enable the compute googleapis.com API**" matches "**perform the prerequisite steps**" for "**create a new Compute Engine instance**" in a "**new project**".

📌 **When to use it:** Use it whenever a new project will run its first virtual machine.
🏢 **Office example:** Flipping the main power switch before setting up computers in a new office.

### ❌ D
> **D.** Grant yourself the IAM role of Computer Admin.

**Wrong words:**
- ❌ "**Grant yourself … Computer Admin**": the project creator is already Owner. (And the role is Compute Admin.)

📌 **When to use it:** Use Compute Admin to give others VM rights.
🏢 **Office example:** Issuing yourself a key to a building you own.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects create shopnow-staging && gcloud billing projects link shopnow-staging --billing-account=01AB23-…
gcloud services enable compute.googleapis.com --project=shopnow-staging
gcloud compute instances create web-1 --zone=us-central1-a --project=shopnow-staging
```

---

## 🧠 Key Takeaways / Memory Tips

- **New project → enable the service's API first** (compute.googleapis.com for VMs).
  🧠 *"**Power on, then build.**"*
- Related: **Q136**, **Q180**.

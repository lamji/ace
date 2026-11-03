# Q232: New Project: Create VMs, Firewalls and Store Data (Enable compute and storage APIs With gcloud services enable)

**Topic:** APIs (enabling only needed services)

## ❓ Question
> You recently received a new Google Cloud project with an attached billing account where you will work. You need to create instances, set firewalls, and store data in Cloud Storage. You want to follow Google-recommended practices. What should you do?
>
> **A.** Use the gcloud CLI services enable cloudresourcemanager.googleapis.com command to enable all resources.
>
> **B.** Use the gcloud services enable compute.googleapis.com command to enable Compute Engine and the gcloud services enable storage-api.googleapis.com command to enable the Cloud Storage APIs.
>
> **C.** Open the Google Cloud console and enable all Google Cloud APIs from the API dashboard.
>
> **D.** Open the Google Cloud console and run gcloud init --project in a Cloud Shell.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Turn on **only** the APIs you need: Compute (VMs + firewalls) and Cloud Storage.

**Clues in the question:**
- "**create instances, set firewalls**" → **compute.googleapis.com** (firewalls are part of Compute).
- "**store data in Cloud Storage**" → **storage-api.googleapis.com**.
- "**Google-recommended practices**" → enable only what you need.

**Exam topic:** APIs.

---

## 📚 Key Terms Explained

### 1. gcloud services enable 🔑 (review from Q181)
- **What it is:** Turns on a Google API in the project.
- **Looks like:** `gcloud services enable compute.googleapis.com storage-api.googleapis.com`
- **Not to be confused with:** IAM.
- **Analogy:** 💡 Switching on only the rooms you'll use.
- **In the online store:** —

### 2. cloudresourcemanager.googleapis.com
- **What it is:** The API for managing projects/folders/IAM policies. It doesn't turn on other services.
- **Looks like:** —
- **Not to be confused with:** "enable all".
- **Analogy:** 🏢 The building management office.
- **In the online store:** —

### 🔗 How they fit together
```
 enable compute.googleapis.com (VMs + firewalls) ✅
 enable storage-api.googleapis.com (Cloud Storage) ✅
```

---

## 🌍 Real-World Scenario

An engineer gets a new project and enables just **Compute Engine** and **Cloud Storage** APIs before creating VMs, firewall rules and a bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the gcloud CLI services enable cloudresourcemanager.googleapis.com command to enable all resources.

**Wrong words:**
- ❌ "**cloudresourcemanager.googleapis.com … to enable all resources**": that API manages projects; it doesn't enable everything.

📌 **When to use it:** Use it when tools need to read or change project/IAM settings.
🏢 **Office example:** Opening the building office and expecting every room to unlock.

### ✅ B
> **B.** Use the gcloud services enable compute.googleapis.com command to enable Compute Engine and the gcloud services enable storage-api.googleapis.com command to enable the Cloud Storage APIs.

**Why it's correct:**
- ✔️ "**enable compute.googleapis.com**" matches "**create instances, set firewalls**".
- ✔️ "**enable storage-api.googleapis.com**" matches "**store data in Cloud Storage**".
- ✔️ Only what's needed matches "**Google-recommended practices**".

📌 **When to use it:** Use it when starting work in a new project: switch on only the services you'll actually use.
🏢 **Office example:** Switching on the lights in just the rooms you'll work in.

### ❌ C
> **C.** Open the Google Cloud console and enable all Google Cloud APIs from the API dashboard.

**Wrong words:**
- ❌ "**enable all Google Cloud APIs**": against least privilege; more surface and possible surprise costs.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Turning on every light and machine in the building.

### ❌ D
> **D.** Open the Google Cloud console and run gcloud init --project in a Cloud Shell.

**Wrong words:**
- ❌ "**gcloud init --project**": sets up your CLI; doesn't enable APIs.

📌 **When to use it:** Use gcloud init to configure your CLI.
🏢 **Office example:** Setting up your phone; it doesn't unlock any rooms.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud services enable compute.googleapis.com storage-api.googleapis.com --project=shopnow-sandbox`

---

## 🧠 Key Takeaways / Memory Tips

- **Enable only the APIs you need** (Compute covers VMs and firewalls).
  🧠 *"**Switch on only your rooms.**"*
- Related: **Q181**, **Q180**, **Q135**.

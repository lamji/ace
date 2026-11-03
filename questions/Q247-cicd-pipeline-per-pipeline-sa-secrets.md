# Q247: CI/CD on VMs Managing All Infrastructure With Least Privilege (One SA per Pipeline, Keys in Secret Manager)

**Topic:** IAM (service accounts for CI/CD)

## ❓ Question
> Your company is moving its continuous integration and delivery (CI/CD) pipeline to Compute Engine instances. The pipeline will manage the entire cloud infrastructure through code. How can you ensure that the pipeline has appropriate permissions while your system is following security best practices?
>
> **A.** • Attach a single service account to the compute instances. • Add minimal rights to the service account. • Allow the service account to impersonate a Cloud Identity user with elevated permissions to create, update, or delete resources.
>
> **B.** • Add a step for human approval to the CI/CD pipeline before the execution of the infrastructure provisioning. • Use the human approvals IAM account for the provisioning.
>
> **C.** • Attach a single service account to the compute instances. • Add all required Identity and Access Management (IAM) permissions to this service account to create, update, or delete resources.
>
> **D.** • Create multiple service accounts, one for each pipeline with the appropriate minimal Identity and Access Management (IAM) permissions. • Use a secret manager service to store the key files of the service accounts. • Allow the CI/CD pipeline to request the appropriate secrets during the execution of the pipeline.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between C and D. Most Voted is **D** (least privilege per pipeline). Today Google would prefer **impersonating** each pipeline's service account instead of storing key files, but among these options D best follows least privilege. If your site differs, tell me.

---

## 📖 What the Question Is Asking

**In plain words:** A pipeline that manages **all** infrastructure needs permissions, but **securely**.

**Clues in the question:**
- "**appropriate permissions**" + "**security best practices**" → **least privilege**: separate service accounts per pipeline, each with only what it needs.
- Secrets (keys) stored in **Secret Manager**, not on disk.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Secret Manager 🔑
- **What it is:** A managed store for passwords, API keys and key files, with IAM access and versions.
- **Looks like:** `gcloud secrets versions access latest --secret=network-pipeline-sa-key`
- **Not to be confused with:** files on disk.
- **Analogy:** 🔐 A locked key cabinet.
- **In the online store:** Deploy keys.

### 2. Least privilege per pipeline
- **What it is:** Each pipeline (network, DB, apps) gets its own service account with just its permissions.
- **Looks like:** `net-pipeline-sa` = Compute Network Admin only
- **Not to be confused with:** one all-powerful account.
- **Analogy:** 🔑 Separate keys per job.
- **In the online store:** —

### 🔗 How they fit together
```
 pipeline net → net-sa (network roles)
 pipeline db  → db-sa  (cloudsql roles)    keys in Secret Manager ✅
```

---

## 🌍 Real-World Scenario

A platform team splits CI/CD into network, database and app pipelines, each with its own **least-privilege** service account; credentials are fetched from **Secret Manager** at run time.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** • Attach a single service account to the compute instances. • Add minimal rights to the service account. • Allow the service account to impersonate a Cloud Identity user with elevated permissions to create, update, or delete resources.

**Wrong words:**
- ❌ "**impersonate a Cloud Identity user with elevated permissions**": service accounts impersonate service accounts, not human users; elevated human access is bad practice.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A robot borrowing the manager's personal badge.

### ❌ B
> **B.** • Add a step for human approval to the CI/CD pipeline before the execution of the infrastructure provisioning. • Use the human approvals IAM account for the provisioning.

**Wrong words:**
- ❌ "**Use the human approvals IAM account for the provisioning**": a person's account running automation is insecure and untraceable.

📌 **When to use it:** Use human approval as a gate, but provision with a service account.
🏢 **Office example:** Using the manager's login for the robot's work.

### ❌ C
> **C.** • Attach a single service account to the compute instances. • Add all required Identity and Access Management (IAM) permissions to this service account to create, update, or delete resources.

**Wrong words:**
- ❌ "**single service account … all required … permissions**": one account with power over everything; if leaked, everything is exposed.

📌 **When to use it:** Use one SA only for very small, single-purpose pipelines.
🏢 **Office example:** One master key for every room, carried by every robot.

### ✅ D
> **D.** • Create multiple service accounts, one for each pipeline with the appropriate minimal Identity and Access Management (IAM) permissions. • Use a secret manager service to store the key files of the service accounts. • Allow the CI/CD pipeline to request the appropriate secrets during the execution of the pipeline.

**Why it's correct:**
- ✔️ "**multiple service accounts, one for each pipeline with the appropriate minimal … permissions**" matches "**appropriate permissions**" + "**security best practices**" (least privilege).
- ✔️ "**secret manager service to store the key files**": credentials aren't left on VMs.

📌 **When to use it:** Use it when several automated jobs each need different, limited access.
🏢 **Office example:** Each robot gets its own key for only its rooms, kept in a locked key cabinet until needed.

---

## 🛒 E-Commerce Full-Stack Example

`ci-network-sa` (compute.networkAdmin), `ci-db-sa` (cloudsql.admin), `ci-apps-sa` (run.admin); credentials in Secret Manager (better: impersonation).

---

## 🧠 Key Takeaways / Memory Tips

- **CI/CD permissions → least privilege per pipeline.** Store secrets in Secret Manager (prefer impersonation over keys).
  🧠 *"**One pipeline, one badge, only its rooms.**"*
- Related: **Q284**, **Q242**.

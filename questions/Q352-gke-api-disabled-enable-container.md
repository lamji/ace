# Q352: Cluster Creation Fails: Kubernetes Engine API Disabled (gcloud services enable container.googleapis.com)

**Topic:** GKE (APIs)

## ❓ Question
> You are using the gcloud container clusters create app-cluster command to deploy a Google Kubernetes Engine (GKE) cluster in a new Google Cloud project. The command fails with the following error: ERROR: (gcloud.container.clusters.create) ResponseError: code=403, message=Kubernetes Engine API has not been used in the project before or it is disabled. You need to resolve the issue. What should you do?
>
> **A.** Rerun the command with the --enable-autoprovisioning flag.
>
> **B.** Disable the “Require enabling Workload Identity Federation for GKE” organization policy, and then run the cluster creation command again.
>
> **C.** Add the Kubernetes Engine Admin IAM role to your user account, and then run the cluster creation command again.
>
> **D.** Run the gcloud services enable container.googleapis.com command, and then run the cluster creation command again.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You ran gcloud container clusters create app-cluster in a new project, and it failed with: Kubernetes Engine API has not been used in the project before or it is disabled.
- **What you must achieve:** Fix the problem.
- **The limits:** None stated.
- **What they're really asking:** What do you do before running the create command again?

**Clues in the question:**
- The error names the cause: the API isn't enabled → **enable `container.googleapis.com`**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Enabling APIs 🔑 (review from Q181)
- **What it is:** Each Google Cloud service's API must be enabled per project before use.
- **Looks like:** `gcloud services enable container.googleapis.com`
- **Not to be confused with:** IAM roles.
- **Analogy:** 🔌 Switching on the service at the office's power board.
- **In the online store:** —

### 🔗 How they fit together
```
 403 API disabled → services enable container.googleapis.com → create ✅
```

---

## 🌍 Real-World Scenario

In a new project, cluster creation fails until the engineer **enables the Kubernetes Engine API**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Rerun the command with the --enable-autoprovisioning flag.

**Wrong words:**
- ❌ "**--enable-autoprovisioning**": node auto-provisioning; unrelated.

📌 **When to use it:** Use NAP for automatic node pools.
🏢 **Office example:** Adding rooms when the power is off.

### ❌ B
> **B.** Disable the “Require enabling Workload Identity Federation for GKE” organization policy, and then run the cluster creation command again.

**Wrong words:**
- ❌ "**Disable the … Workload Identity … organization policy**": unrelated to the error.

📌 **When to use it:** **Avoid** weakening security policies.
🏢 **Office example:** Removing a security rule to fix a power problem.

### ❌ C
> **C.** Add the Kubernetes Engine Admin IAM role to your user account, and then run the cluster creation command again.

**Wrong words:**
- ❌ "**Kubernetes Engine Admin IAM role**": the error is API disabled, not permission denied.

📌 **When to use it:** Use it when the error says permission denied.
🏢 **Office example:** Getting a new key when the lights are off.

### ✅ D
> **D.** Run the gcloud services enable container.googleapis.com command, and then run the cluster creation command again.

**Why it's correct:**
- ✔️ "**gcloud services enable container.googleapis.com**" matches "**Kubernetes Engine API has not been used in the project before or it is disabled**".

📌 **When to use it:** Use it when a new project says a service is turned off.
🏢 **Office example:** Flipping on the power switch for that office service.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud services enable container.googleapis.com artifactregistry.googleapis.com --project=shopnow-new`

---

## 🧠 Key Takeaways / Memory Tips

- **"API … disabled" error → gcloud services enable.**
  🧠 *"**Read the error; enable the API.**"*
- Related: **Q181**.

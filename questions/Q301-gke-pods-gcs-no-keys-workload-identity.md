# Q301: GKE Pods Reach a Private Bucket When SA Keys Are Banned (Workload Identity Federation for GKE)

**Topic:** GKE security (Workload Identity Federation for GKE)

## ❓ Question
> You are deploying an application to Google Kubernetes Engine (GKE). The application needs to make API calls to a private Cloud Storage bucket. You need to configure your application Pods to authenticate to the Cloud Storage API, but your organization policy prevents the usage of service account keys. You want to follow Google-recommended practices. What should you do?
>
> **A.** Create the GKE cluster with Workload Identity Federation. Configure the default node service account to access the bucket. Deploy the application into the cluster so the application can use the node service account permissions. Use Identity and Access Management (IAM) to grant the service account access to the bucket.
>
> **B.** Create the GKE cluster with Workload Identity Federation. Create a Google service account and a Kubernetes ServiceAccount, and configure both service accounts to use Workload Identity Federation. Attach the Kubernetes ServiceAccount to the application Pods and configure the Google service account to access the bucket with Identity and Access Management (IAM).
>
> **C.** Create the GKE cluster and deploy the application. Request a security exception to create a Google service account key. Set the constraints/iam.serviceAccountKeyExpiryHours organization policy to 24 hours.
>
> **D.** Create the GKE cluster and deploy the application. Request a security exception to create a Google service account key. Set the constraints/iam.serviceAccountKeyExpiryHours organization policy to 8 hours.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are deploying an app to GKE whose Pods (running containers) must call a private Cloud Storage bucket.
- **What you must achieve:** Let the Pods sign in to the Cloud Storage API.
- **The limits:** An organization policy forbids service account keys (downloadable secret files); follow recommended practice.
- **What they're really asking:** How do the Pods get access to the bucket without any key file?

**Clues in the question:**
- "**prevents the usage of service account keys**" + Pods → **Workload Identity Federation for GKE**.
- Recommended setup: a **dedicated** Kubernetes ServiceAccount (KSA) linked to a **dedicated** Google service account (GSA), not the node SA.

**Exam topic:** GKE / IAM.

---

## 📚 Key Terms Explained

### 1. Workload Identity Federation for GKE 🔑
- **What it is:** Lets a Kubernetes ServiceAccount act as an IAM identity, so Pods get short-lived Google tokens without keys.
- **Looks like:** `kubectl annotate sa app-ksa iam.gke.io/gcp-service-account=app-gsa@proj.iam.gserviceaccount.com`
- **Not to be confused with:** node service account (shared by every Pod on the node).
- **Analogy:** 🪪 Each department's badge is linked to one company badge.
- **In the online store:** ShopNow image service Pods.

### 2. Kubernetes ServiceAccount (KSA)
- **What it is:** An identity object inside Kubernetes that Pods run as.
- **Looks like:** `kubectl create serviceaccount app-ksa`
- **Not to be confused with:** a Google service account (IAM).
- **Analogy:** 🎫 Building badge vs company badge.
- **In the online store:** —

### 🔗 How they fit together
```
 Pod → KSA app-ksa ──linked──► GSA app-gsa ──IAM──► bucket ✅ (no keys)
```

---

## 🌍 Real-World Scenario

A team deploys an app that reads a private bucket. Keys are banned, so they link `app-ksa` to `app-gsa` with **Workload Identity Federation** and grant the GSA access to the bucket.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create the GKE cluster with Workload Identity Federation. Configure the default node service account to access the bucket. Deploy the application into the cluster so the application can use the node service account permissions. Use Identity and Access Management (IAM) to grant the service account access to the bucket.

**Wrong words:**
- ✔️ Workload Identity Federation is right.
- ❌ "**default node service account … use the node service account permissions**": every Pod on the node shares it; not least privilege.

📌 **When to use it:** Use the node SA only for node tasks (logging, pulling images).
🏢 **Office example:** Everyone on the floor using the floor manager's badge.

### ✅ B
> **B.** Create the GKE cluster with Workload Identity Federation. Create a Google service account and a Kubernetes ServiceAccount, and configure both service accounts to use Workload Identity Federation. Attach the Kubernetes ServiceAccount to the application Pods and configure the Google service account to access the bucket with Identity and Access Management (IAM).

**Why it's correct:**
- ✔️ "**Workload Identity Federation**" matches "**organization policy prevents the usage of service account keys**": no keys needed.
- ✔️ "**Kubernetes ServiceAccount … Attach … to the application Pods**" matches "**configure your application Pods to authenticate**".
- ✔️ "**Google service account to access the bucket with … IAM**" matches "**API calls to a private Cloud Storage bucket**".

📌 **When to use it:** Use it when programs in a container cluster need to reach other services without any saved passwords.
🏢 **Office example:** Each team's building badge is linked to its own company badge that opens only the right room.

### ❌ C
> **C.** Create the GKE cluster and deploy the application. Request a security exception to create a Google service account key. Set the constraints/iam.serviceAccountKeyExpiryHours organization policy to 24 hours.

**Wrong words:**
- ❌ "**Request a security exception to create a … key**": goes against the policy and best practice.

📌 **When to use it:** **Never use this** when keyless options exist.
🏢 **Office example:** Asking for a master key exception instead of using badges.

### ❌ D
> **D.** Create the GKE cluster and deploy the application. Request a security exception to create a Google service account key. Set the constraints/iam.serviceAccountKeyExpiryHours organization policy to 8 hours.

**Wrong words:**
- ❌ Same key exception, just shorter expiry.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A master key that expires faster is still a master key.

---

## 🛒 E-Commerce Full-Stack Example

`image-svc-ksa` ↔ `image-svc@shopnow-prod` with `roles/storage.objectViewer` on `gs://shopnow-images`.

---

## 🧠 Key Takeaways / Memory Tips

- **Pods + no keys → Workload Identity Federation: one KSA ↔ one GSA.**
  🧠 *"**Pods borrow a Google badge, no keys.**"*
- Related: **Q360**, **Q228**.

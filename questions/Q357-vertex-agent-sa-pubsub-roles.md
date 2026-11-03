# Q357: App Deployed to Vertex AI Needs Pub/Sub Access via Its New Service Account (Grant Roles to the Agent's Service Account)

**Topic:** IAM (service accounts)

## ❓ Question
> You have an application that reads data from a Pub/Sub topic. During local development, you authenticated using your personal credentials to test the application. You now want to deploy the application to Vertex AI and have created a new service account to be used as the application's identity. You need to ensure that the deployed application can still access the Pub/Sub topic. What should you do?
>
> **A.** Grant the relevant IAM roles to the service account used as your agent identity.
>
> **B.** Generate a JSON private key for the service account, and upload the key as Vertex AI metadata.
>
> **C.** Extract your access token by using the gcloud auth print-access-token command, and store it with the application.
>
> **D.** Create a secret in Secret Manager to store your personal credentials, and configure the application’s authentication code to use this secret.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** App now runs as a **new service account** on Vertex AI; it must still read Pub/Sub.

**Clues in the question:**
- New identity → grant **it** the needed roles (e.g., `roles/pubsub.subscriber`). No keys, no personal credentials.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Agent identity / service account 🔑
- **What it is:** The service account the deployed app runs as; its IAM roles decide what it can access.
- **Looks like:** `gcloud pubsub subscriptions add-iam-policy-binding events-sub --member=serviceAccount:agent@proj.iam.gserviceaccount.com --role=roles/pubsub.subscriber`
- **Not to be confused with:** your personal account.
- **Analogy:** 🪪 The new hire's own badge.
- **In the online store:** —

### 🔗 How they fit together
```
 Vertex AI app (agent SA) → roles/pubsub.subscriber ✅
```

---

## 🌍 Real-World Scenario

After deploying, the team grants the agent's SA **Pub/Sub Subscriber**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Grant the relevant IAM roles to the service account used as your agent identity.

**Why it's correct:**
- ✔️ "**Grant the relevant IAM roles to the service account used as your agent identity**" matches "**created a new service account to be used as the application's identity**" + "**can still access the Pub/Sub topic**".

📌 **When to use it:** Use it whenever a program gets its own account: give that account just the access it needs.
🏢 **Office example:** Giving the new hire's own badge access to the mail room.

### ❌ B
> **B.** Generate a JSON private key for the service account, and upload the key as Vertex AI metadata.

**Wrong words:**
- ❌ "**Generate a JSON private key**": unnecessary secret; Vertex AI uses the attached SA.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Printing a master key for a badge holder.

### ❌ C
> **C.** Extract your access token by using the gcloud auth print-access-token command, and store it with the application.

**Wrong words:**
- ❌ "**print-access-token … store it**": your personal token, expires in an hour.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Leaving your own badge with the robot.

### ❌ D
> **D.** Create a secret in Secret Manager to store your personal credentials, and configure the application’s authentication code to use this secret.

**Wrong words:**
- ❌ "**store your personal credentials**": the app acts as you; insecure.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Lending your ID card to software.

---

## 🛒 E-Commerce Full-Stack Example

`reco-agent@shopnow-ml` → `roles/pubsub.subscriber` on `click-events-sub`.

---

## 🧠 Key Takeaways / Memory Tips

- **New app identity → grant roles to that service account.**
  🧠 *"**New badge, new permissions.**"*
- Related: **Q369**, **Q297**.

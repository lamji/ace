# Q070: On-Premises App Calling Google APIs (Service Account Key File)

**Topic:** IAM (service accounts, service account key files, authenticating from outside Google Cloud, GOOGLE_APPLICATION_CREDENTIALS; Workload Identity Federation today)

## ❓ Question
> You are building an application that will run in your data center. The application will use Google Cloud Platform (GCP) services like AutoML. You created a service account that has appropriate access to AutoML. You need to enable authentication to the APIs from your on-premises environment. What should you do?
>
> **A.** Use service account credentials in your on-premises application.
>
> **B.** Use gcloud to create a key file for the service account that has appropriate permissions.
>
> **C.** Set up direct interconnect between your data center and Google Cloud Platform to enable authentication for your on-premises applications.
>
> **D.** Go to the IAM & admin console, grant a user account permissions similar to the service account permissions, and use this user account for authentication from your data center.

**My answer:** A
**Correct answer:** B
**Result:** ❌ Incorrect

> Why A was tempting: A **is what happens in the end**: the app uses the service account's credentials. But A is **vague**: it doesn't say **how you get** those credentials. A VM inside Google Cloud gets them automatically, but a server in **your data center** has nothing until you **create a key file** (B). B is the concrete step that makes authentication possible.

> ℹ️ **Real-life note:** Today Google recommends **Workload Identity Federation** (no key files) for on-premises apps when possible, because key files can leak. On this older exam question, B (key file) is the expected answer.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An app runs in your own data center and calls Google services such as AutoML. You created a service account with the right access.
- **What you must achieve:** Let the on-premises app sign in to Google's APIs.
- **The limits:** None stated.
- **What they're really asking:** How does the app in your data center prove it is that service account?

**Clues in the question:**
- "**run in your data center**" / "**on-premises environment**": outside Google Cloud, the app does **not** get credentials automatically (unlike a VM with an attached service account, Q019).
- "**You created a service account that has appropriate access**": permissions are already done. You only need a way for the app to **sign in as** that service account.
- "**enable authentication to the APIs**": you need an actual credential the app can load: a **key file**.
- "**What should you do?**": the answer must be a concrete **action** (B: create the key file), not a general idea (A).

**Exam topic:** IAM / service accounts.

---

## 📚 Key Terms Explained

### 1️⃣ Service account (review from Q019, Q036)
- **What it is:** A **non-human Google account** for apps. You give it IAM roles, and the app acts as it.
- **Looks like:** `automl-app@shopnow.iam.gserviceaccount.com` with role `roles/automl.predictor`
- **Not to be confused with:** a user account (a person who logs in with a password and 2FA).
- **Analogy:** 🤖 A **company robot's employee record**: it has a job title (roles), but it needs an **ID card** to get through the door.
- **In the online store:** The recommendation app's identity for calling AutoML.

### 2️⃣ Service account key file 🔑
- **What it is:** A **JSON file containing a private key** for the service account. Whoever has this file can **sign in as** the service account. You create it with gcloud or the console.
- **Looks like:**
  ```bash
  gcloud iam service-accounts keys create automl-key.json \
    --iam-account=automl-app@shopnow.iam.gserviceaccount.com
  ```
  ```json
  { "type": "service_account", "client_email": "automl-app@shopnow.iam...", "private_key": "-----BEGIN PRIVATE KEY-----..." }
  ```
- **Not to be confused with:** the service account itself. The account is the **record**; the key file is the **ID card** that proves you're it.
- **Analogy:** 🪪 **Printing an ID card** for the robot so it can badge in from a different building.
- **In the online store:** The on-premises recommendation server loads `automl-key.json` to call AutoML.

### 3️⃣ Credentials (inside vs outside Google Cloud)
- **What it is:** Proof of identity that a Google API accepts.
  - **Inside Google Cloud** (VM, Cloud Run): Google **automatically** gives the app short-lived credentials for the attached service account. No file needed.
  - **Outside Google Cloud** (your data center): nothing is automatic. You must give the app a **key file** (or set up Workload Identity Federation).
- **Looks like:** `export GOOGLE_APPLICATION_CREDENTIALS=/etc/app/automl-key.json`
- **Not to be confused with:** permissions (IAM roles). Credentials prove **who** you are; roles say **what** you may do.
- **Analogy:** 🏢 Inside head office, the robot is recognized at the door. At a branch office, it must **show its ID card**.

### 4️⃣ Dedicated Interconnect
- **What it is:** A **physical private network line** between your data center and Google.
- **Not to be confused with:** authentication. It's a **network cable**, not an identity. API calls still need credentials.
- **Analogy:** 🛣️ A **private road** to Google's building. You still need an ID card at the door.

### 5️⃣ Workload Identity Federation (modern best practice)
- **What it is:** Lets an outside app use its **own identity** (from AWS, Azure, or your company's identity system) to get **short-lived** Google credentials. **No key file** to leak.
- **Not to be confused with:** a key file. Federation **avoids** long-lived keys.
- **Analogy:** 🤝 Google accepts your **company's own badge** and hands out a day pass, so no permanent card is ever printed.

### 🔗 How they fit together
```
 🏢 Your data center                         ☁️ Google Cloud
   App ── loads automl-key.json ──────────► AutoML API
          (key for automl-app@...)           checks: valid key? ✅
                                             roles of automl-app? ✅ automl.predictor
 No key file = no way to prove who you are ❌
```

---

## 🌍 Real-World Scenario

A company keeps its main app on-premises but wants to use Google's ML APIs. The security team creates a dedicated service account with only the AutoML role. The engineer then **creates a key file** for it, stores the file securely on the server (secret manager, restricted permissions), and points the app at it with `GOOGLE_APPLICATION_CREDENTIALS`. Keys are rotated regularly, or the team moves to Workload Identity Federation to avoid keys entirely.

---

## 🔍 Option-by-Option Breakdown

### ❌ A (your answer)
> **A.** Use service account credentials in your on-premises application.

**Wrong words:**
- ✔️ "**in your on-premises application**" and "**service account**" point in the right direction.
- ❌ "**Use service account credentials**": it doesn't say **how to get** them. On-premises, there are **no** credentials until you create a key file. This describes the end result, not the step you must take, so it doesn't answer "What should you do?".

📌 **When to use it:** It's the step **after** B: once the key file exists, the app uses it.
🏢 **Office example:** Telling the robot "just show your ID card" before anyone has printed it one.

### ✅ B (correct answer)
> **B.** Use gcloud to create a key file for the service account that has appropriate permissions.

**Why it's correct:**
- ✔️ "**create a key file for the service account**" matches "**enable authentication to the APIs from your on-premises environment**": outside Google Cloud, a key file is how the app proves it's the service account.
- ✔️ "**Use gcloud to create**" matches "**What should you do?**": it's a concrete action you can take right now (`gcloud iam service-accounts keys create`).
- ✔️ "**the service account that has appropriate permissions**" matches "**You created a service account that has appropriate access to AutoML**": it reuses the account that already has the right roles. No new permissions needed.

📌 **When to use it:** Use it when an app outside Google Cloud must act as a service account and no keyless option is available.
🏢 **Office example:** Printing an ID card for the robot so it can badge in at head office from the branch office.

### ❌ C
> **C.** Set up direct interconnect between your data center and Google Cloud Platform to enable authentication for your on-premises applications.

**Wrong words:**
- ❌ "**Set up direct interconnect**": a physical network line is expensive and takes weeks to install, and it's not needed to call Google APIs.
- ❌ "**to enable authentication**": Interconnect is a **network connection**, not an identity. API calls over it still need credentials.

📌 **When to use it:** Use Interconnect when you need a fast, private, high-bandwidth link between your data center and Google Cloud.
🏢 **Office example:** Building a private road to head office. You still need an ID card at the door.

### ❌ D
> **D.** Go to the IAM & admin console, grant a user account permissions similar to the service account permissions, and use this user account for authentication from your data center.

**Wrong words:**
- ❌ "**grant a user account permissions similar to the service account permissions**": duplicates permissions on a **person's** account, which is harder to manage and audit.
- ❌ "**use this user account for authentication from your data center**": apps should **never** run as a person. If that person leaves or changes their password, the app breaks, and logs show a human doing the app's work.

📌 **When to use it:** **Never use this** for apps. Use a service account (B).
🏢 **Office example:** Letting the robot use the manager's personal ID card. When the manager quits, the robot is locked out.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **recommendation server** runs in its own data center and calls AutoML for "you may also like" predictions.

```bash
# 1. Service account already exists with roles/automl.predictor
# 2. Create the key file (B)
gcloud iam service-accounts keys create /secure/automl-key.json \
  --iam-account=automl-app@shopnow.iam.gserviceaccount.com

# 3. On the on-prem server, point the app at it
export GOOGLE_APPLICATION_CREDENTIALS=/secure/automl-key.json
python recommend.py   # Google client libraries pick up the key automatically
```

Good habits:
- 🔒 Store the key file with restricted access (only the app's user can read it).
- 🔁 Rotate the key regularly, and delete old keys.
- 🚀 Long-term: switch to Workload Identity Federation so there's no key file at all.

---

## 🧠 Key Takeaways / Memory Tips

- **Inside Google Cloud → attach the service account (no key).** **Outside Google Cloud → key file** (or Workload Identity Federation today).
- **Interconnect/VPN = network, not identity.** They never "enable authentication".
- **Apps never use a person's account.**
- On the exam, pick the **concrete action** (create the key) over a vague result ("use credentials").
  🧠 *"**Outside Google, the robot needs a printed ID card: create the key file.**"*
- Related: **Q019** (attach SA to VM, avoid keys inside GCP), **Q036** (keys are wrong when the VM is in GCP), **Q064** (service account for Pub/Sub push).

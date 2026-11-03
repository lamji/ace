# Q134: App Using Application Default Credentials Moves to a VM (Give the VM's Service Account Access)

**Topic:** IAM / authentication (Application Default Credentials, attached service accounts, keys)

## ❓ Question
> You built an application on your development laptop that uses Google Cloud services. Your application uses Application Default Credentials for authentication and works fine on your development laptop. You want to migrate this application to a Compute Engine virtual machine (VM) and set up authentication using Google-recommended practices and minimal changes. What should you do?
>
> **A.** Assign appropriate access for Google services to the service account used by the Compute Engine VM.
>
> **B.** Create a service account with appropriate access for Google services, and configure the application to use this account.
>
> **C.** Store credentials for service accounts with appropriate access for Google services in a config file, and deploy this config file with your application.
>
> **D.** Store credentials for your user account with appropriate access for Google services in a config file, and deploy this config file with your application.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The app uses **ADC**, which on your laptop uses your own login. On a VM, ADC automatically uses the **VM's service account**. What do you change?

**Clues in the question:**
- "**Application Default Credentials**": ADC looks for credentials automatically. On a VM, it finds the **attached service account** through the metadata server.
- "**minimal changes**": no code changes, just give that service account the right roles.
- "**Google-recommended practices**": no key files.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Application Default Credentials (ADC) 🔑
- **What it is:** A **search order the Google client libraries follow to find credentials**: env var `GOOGLE_APPLICATION_CREDENTIALS` → your gcloud user login (laptop) → the **attached service account** (on Google Cloud).
- **Looks like:** `storage.Client()`  # no key in code
- **Not to be confused with:** a specific key file.
- **Analogy:** 🔑 A worker who uses **whatever badge they're wearing** at that location.
- **In the online store:** The same code runs on the laptop and on the VM.

### 2. Attached service account
- **What it is:** The service account a VM runs as. Its tokens come from the metadata server, so no key files are needed.
- **Looks like:** `gcloud compute instances create app-1 --service-account=app-sa@…`
- **Not to be confused with:** a downloaded key.
- **Analogy:** 🤖 The badge clipped to the robot.
- **In the online store:** checkout-sa on checkout VMs.

### 🔗 How they fit together
```
 laptop: ADC → your user login (gcloud auth application-default login)
 VM:     ADC → VM's attached service account ✅ (give it the right roles, no code change)
```

---

## 🌍 Real-World Scenario

A developer's script reads from Cloud Storage using the client library and ADC. It's moved to a VM. The admin grants the **VM's service account** `roles/storage.objectViewer`, and the script works unchanged.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Assign appropriate access for Google services to the service account used by the Compute Engine VM.

**Why it's correct:**
- ✔️ "**the service account used by the Compute Engine VM**" matches "**Application Default Credentials**": on a VM, ADC automatically uses that account.
- ✔️ "**Assign appropriate access**" matches "**minimal changes**": no code or config changes, just roles.
- ✔️ No key files, which matches "**Google-recommended practices**".

📌 **When to use it:** Use it when your program already picks up whatever identity it's running as.
🏢 **Office example:** A worker moves to a new office and just wears that office's badge, which you give the right access.

### ❌ B
> **B.** Create a service account with appropriate access for Google services, and configure the application to use this account.

**Wrong words:**
- ✔️ A service account with the right access is fine.
- ❌ "**configure the application to use this account**": it means changing the app (and usually a key file). That's not "minimal changes".

📌 **When to use it:** Use it when the app must use a specific different account (better: attach that account to the VM).
🏢 **Office example:** Rewriting the worker's instructions to use another badge.

### ❌ C
> **C.** Store credentials for service accounts with appropriate access for Google services in a config file, and deploy this config file with your application.

**Wrong words:**
- ❌ "**Store credentials for service accounts … in a config file, and deploy**": shipping key files is risky and isn't Google's recommendation when the VM can use its attached account.

📌 **When to use it:** Use keys only when running outside Google Cloud with no federation option.
🏢 **Office example:** Taping a copy of the key inside every toolbox.

### ❌ D
> **D.** Store credentials for your user account with appropriate access for Google services in a config file, and deploy this config file with your application.

**Wrong words:**
- ❌ "**credentials for your user account**": an app running with your personal credentials is a security risk, and access breaks when you leave.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Leaving your own ID card in the machine so it can work.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's image-resizer reads `gs://shopnow-uploads` with `storage.Client()`.
```bash
gcloud compute instances create resizer-1 --service-account=resizer-sa@shopnow-prod.iam.gserviceaccount.com --scopes=cloud-platform
gcloud storage buckets add-iam-policy-binding gs://shopnow-uploads --member=serviceAccount:resizer-sa@shopnow-prod.iam.gserviceaccount.com --role=roles/storage.objectViewer
```
The code is the same as on the laptop.

---

## 🧠 Key Takeaways / Memory Tips

- **ADC on a VM = the attached service account.** Grant it roles; no code changes.
- Avoid key files and personal credentials.
  🧠 *"**ADC wears the VM's badge.**"*
- Related: **Q070** (key file for on-prem), **Q019** (service accounts on VMs).

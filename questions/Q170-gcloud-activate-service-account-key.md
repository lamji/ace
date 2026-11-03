# Q170: Use a Service Account Key File With gcloud (gcloud auth activate-service-account)

**Topic:** gcloud CLI (authentication with service account keys)

## ❓ Question
> You received a JSON file that contained a private key of a Service Account in order to get access to several resources in a Google Cloud project. You downloaded and installed the Cloud SDK and want to use this private key for authentication and authorization when performing gcloud commands. What should you do?
>
> **A.** Use the command gcloud auth login and point it to the private key.
>
> **B.** Use the command gcloud auth activate-service-account and point it to the private key.
>
> **C.** Place the private key file in the installation directory of the Cloud SDK and rename it to "credentials.json".
>
> **D.** Place the private key file in your home directory and rename it to "GOOGLE_APPLICATION_CREDENTIALS".

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You have a **service account key file** and want **gcloud** to use it.

**Clues in the question:**
- "**use this private key for … gcloud commands**" → `gcloud auth activate-service-account --key-file=key.json`.
- `gcloud auth login` is for **user accounts** in a browser.

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. gcloud auth activate-service-account 🔑
- **What it is:** Makes gcloud act **as a service account**, using its key file.
- **Looks like:** `gcloud auth activate-service-account --key-file=sa-key.json`
- **Not to be confused with:** gcloud auth login (users).
- **Analogy:** 🪪 Clipping on the robot's badge.
- **In the online store:** CI server runs gcloud as deploy-sa.

### 2. GOOGLE_APPLICATION_CREDENTIALS
- **What it is:** An **environment variable** that holds the **path** to a key file, used by client libraries (ADC). It's not a file name.
- **Looks like:** `export GOOGLE_APPLICATION_CREDENTIALS=/keys/sa.json`
- **Not to be confused with:** a gcloud login.
- **Analogy:** 🧭 A signpost pointing to where the badge is kept.
- **In the online store:** Apps using client libraries.

### 🔗 How they fit together
```
 gcloud auth activate-service-account --key-file=key.json ✅
 gcloud config list → account = sa-name@project.iam.gserviceaccount.com
```

---

## 🌍 Real-World Scenario

A build server receives a service account key. The engineer runs `gcloud auth activate-service-account --key-file=deploy-sa.json`, and the gcloud commands now run as that service account.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the command gcloud auth login and point it to the private key.

**Wrong words:**
- ❌ "**gcloud auth login**": it signs in a **user** through a browser. It doesn't take a service account key.

📌 **When to use it:** Use it to log in with your own Google account.
🏢 **Office example:** Showing your personal ID when you meant to use the robot's badge.

### ✅ B
> **B.** Use the command gcloud auth activate-service-account and point it to the private key.

**Why it's correct:**
- ✔️ "**gcloud auth activate-service-account**" matches "**use this private key for authentication**".
- ✔️ "**point it to the private key**" (`--key-file`) matches "**JSON file that contained a private key of a Service Account**".

📌 **When to use it:** Use it when a machine or script must run gcloud as a program account.
🏢 **Office example:** Clipping the robot's badge on before working.

### ❌ C
> **C.** Place the private key file in the installation directory of the Cloud SDK and rename it to "credentials.json".

**Wrong words:**
- ❌ "**rename it to credentials.json**" in the SDK folder: gcloud doesn't automatically load such a file.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Leaving the badge in a drawer and hoping the door notices.

### ❌ D
> **D.** Place the private key file in your home directory and rename it to "GOOGLE_APPLICATION_CREDENTIALS".

**Wrong words:**
- ❌ "**rename it to GOOGLE_APPLICATION_CREDENTIALS**": that's an **environment variable name**, not a file name, and gcloud commands don't use it this way.

📌 **When to use it:** Set the env var (to the file path) for client libraries.
🏢 **Office example:** Naming the badge "badge location".

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud auth activate-service-account deploy-sa@shopnow-prod.iam.gserviceaccount.com --key-file=/secrets/deploy-sa.json
gcloud run deploy storefront --image=… --project=shopnow-prod
```

---

## 🧠 Key Takeaways / Memory Tips

- **gcloud + service account key → `gcloud auth activate-service-account --key-file`.**
- `auth login` = users. `GOOGLE_APPLICATION_CREDENTIALS` = env var for libraries.
  🧠 *"**Robot key? activate-service-account.**"*
- Related: **Q070** (key files), **Q134** (ADC).

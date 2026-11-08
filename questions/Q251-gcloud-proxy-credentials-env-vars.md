# Q251: Keep Proxy Credentials Out of gcloud Logs (Set CLOUDSDK_PROXY_USERNAME/PASSWORD as Environment Variables)

**Topic:** gcloud CLI (proxy configuration)

## ❓ Question
> You installed the Google Cloud CLI on your workstation and set the proxy configuration. However, you are worried that your proxy credentials will be recorded in the gcloud CLI logs. You want to prevent your proxy credential from being logged. What should you do?
>
> **A.** Configure username and password by using gcloud config set proxy/username and gcloud config set proxy/password commands.
>
> **B.** Encode username and password in sha256 encoding, and save in to a text file. Use filename as a value in the gcloud config set core/custom_ca_certs_file command.
>
> **C.** Provide values for CLOUDSDK_PROXY_USERNAME and CLOUDSDK_PROXY_PASSWORD in the gcloud CLI tool configuration file.
>
> **D.** Set the CLOUDSDK_PROXY_USERNAME and CLOUDSDK_PROXY_PASSWORD properties by using environment variables in your command line tool.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You installed the Google Cloud CLI and set up a proxy (a middle server your traffic goes through) with credentials.
- **What you must achieve:** Keep the proxy credentials out of gcloud's logs.
- **The limits:** None stated.
- **What they're really asking:** How do you stop your proxy credentials from being written to the logs?

**Clues in the question:**
- Google's docs: to avoid logging proxy credentials, set them as **environment variables** `CLOUDSDK_PROXY_USERNAME` / `CLOUDSDK_PROXY_PASSWORD` instead of `gcloud config set`.

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. CLOUDSDK_* environment variables 🔑
- **What it is:** Any gcloud property can be set as an environment variable `CLOUDSDK_SECTION_PROPERTY`. Env vars aren't written to gcloud's config or logs.
- **Looks like:** `export CLOUDSDK_PROXY_USERNAME=ana` / `export CLOUDSDK_PROXY_PASSWORD=…`
- **Not to be confused with:** gcloud config set.
- **Analogy:** 🗣️ Telling the clerk the PIN aloud instead of writing it in the logbook.
- **In the online store:** Corporate proxy on dev laptops.

### 🔗 How they fit together
```
 gcloud config set proxy/password → saved in config, may be logged ✗
 export CLOUDSDK_PROXY_PASSWORD   → only in the shell session ✅
```

---

## 🌍 Real-World Scenario

A developer behind a corporate proxy sets `CLOUDSDK_PROXY_USERNAME` and `CLOUDSDK_PROXY_PASSWORD` in their shell, so gcloud uses them without storing them.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure username and password by using gcloud config set proxy/username and gcloud config set proxy/password commands.

**Wrong words:**
- ❌ "**gcloud config set proxy/username and … proxy/password**": saves them in gcloud's properties, which can show up in logs.

📌 **When to use it:** Use config set for non-secret proxy settings like address and port.
🏢 **Office example:** Writing your PIN in the shared logbook.

### ❌ B
> **B.** Encode username and password in sha256 encoding, and save in to a text file. Use filename as a value in the gcloud config set core/custom_ca_certs_file command.

**Wrong words:**
- ❌ "**sha256 encoding … core/custom_ca_certs_file**": that setting is for CA certificates, not credentials; hashing breaks the password.

📌 **When to use it:** Use custom_ca_certs_file for corporate TLS certificates.
🏢 **Office example:** Putting a scrambled PIN in the certificate drawer.

### ❌ C
> **C.** Provide values for CLOUDSDK_PROXY_USERNAME and CLOUDSDK_PROXY_PASSWORD in the gcloud CLI tool configuration file.

**Wrong words:**
- ❌ "**in the gcloud CLI tool configuration file**": still stored in a file gcloud reads and may log.

📌 **When to use it:** **Avoid** storing secrets in config files.
🏢 **Office example:** Writing the PIN on a note in your desk drawer.

### ✅ D
> **D.** Set the CLOUDSDK_PROXY_USERNAME and CLOUDSDK_PROXY_PASSWORD properties by using environment variables in your command line tool.

**Why it's correct:**
- ✔️ "**Set the CLOUDSDK_PROXY_USERNAME and CLOUDSDK_PROXY_PASSWORD properties by using environment variables**" matches "**prevent your proxy credential from being logged**": env vars aren't saved or logged by gcloud.

📌 **When to use it:** Use it when a tool needs a secret but you don't want it written down anywhere.
🏢 **Office example:** Telling the clerk the code aloud each time instead of writing it in the logbook.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud config set proxy/type http; gcloud config set proxy/address proxy.shopnow.local; gcloud config set proxy/port 3128
export CLOUDSDK_PROXY_USERNAME=dev1; export CLOUDSDK_PROXY_PASSWORD='********'
```

---

## 🧠 Key Takeaways / Memory Tips

- **Proxy secrets for gcloud → CLOUDSDK_PROXY_USERNAME/PASSWORD environment variables.**
  🧠 *"**Secrets in env, not in config.**"*
- Related: **Q170**, **Q189**.

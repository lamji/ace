# Q269: Encrypted, Authenticated, IAM-Integrated DB Connection With Little Management (Cloud SQL IAM Auth + Cloud SQL Auth Proxy)

**Topic:** Cloud SQL (Auth Proxy, IAM database authentication)

## ❓ Question
> You are deploying an application on Google Cloud that requires a relational database for storage. To satisfy your company's security policies, your application must connect to your database through an encrypted and authenticated connection that requires minimal management and integrates with Identity and Access Management (IAM). What should you do?
>
> **A.** Deploy a Cloud SQL database with the SSL mode set to encrypted only, configure SSL/TLS client certificates, and configure a database user and password.
>
> **B.** Deploy a Cloud SQL database with the SSL mode set to encrypted only, configure SSL/TLS client certificates, and configure IAM database authentication.
>
> **C.** Deploy a Cloud SQL database and configure IAM database authentication. Access the database through the Cloud SQL Auth Proxy.
>
> **D.** Deploy a Cloud SQL database and configure a database user and password. Access the database through the Cloud SQL Auth Proxy.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Encrypted + authenticated + **IAM** + **minimal management**.

**Clues in the question:**
- "**encrypted and authenticated connection**" + "**minimal management**" → **Cloud SQL Auth Proxy** (TLS automatically, no certs to manage).
- "**integrates with IAM**" → **IAM database authentication** (no DB passwords).

**Exam topic:** Cloud SQL.

---

## 📚 Key Terms Explained

### 1. Cloud SQL Auth Proxy 🔑
- **What it is:** A small program/sidecar that opens an **encrypted, IAM-authorized** tunnel to Cloud SQL; no client certificates to manage.
- **Looks like:** `cloud-sql-proxy --auto-iam-authn shopnow:us-central1:orders`
- **Not to be confused with:** SSL certs by hand.
- **Analogy:** 🚇 A secure private tunnel with ID check.
- **In the online store:** Checkout → orders DB.

### 2. IAM database authentication
- **What it is:** Log in to the database with an IAM user/service account instead of a DB password.
- **Looks like:** DB user `checkout-sa@shopnow.iam`
- **Not to be confused with:** password.
- **Analogy:** 🪪 Badge instead of a PIN.
- **In the online store:** —

### 🔗 How they fit together
```
 app ─► Cloud SQL Auth Proxy (TLS + IAM) ─► Cloud SQL (IAM DB auth) ✅
```

---

## 🌍 Real-World Scenario

A checkout service connects through the **Cloud SQL Auth Proxy** using its service account with **IAM database authentication** — encrypted, no passwords, no certificates to rotate.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy a Cloud SQL database with the SSL mode set to encrypted only, configure SSL/TLS client certificates, and configure a database user and password.

**Wrong words:**
- ❌ "**configure SSL/TLS client certificates**": certificates to manage and rotate.
- ❌ "**database user and password**": not IAM-integrated.

📌 **When to use it:** Use client certs when you can't use the proxy or connectors.
🏢 **Office example:** Managing your own keys and PINs for every door.

### ❌ B
> **B.** Deploy a Cloud SQL database with the SSL mode set to encrypted only, configure SSL/TLS client certificates, and configure IAM database authentication.

**Wrong words:**
- ✔️ IAM DB auth is right.
- ❌ "**configure SSL/TLS client certificates**": extra management.

📌 **When to use it:** Use manual SSL when tools can't use the proxy.
🏢 **Office example:** A badge plus hand-cut keys to maintain.

### ✅ C
> **C.** Deploy a Cloud SQL database and configure IAM database authentication. Access the database through the Cloud SQL Auth Proxy.

**Why it's correct:**
- ✔️ "**configure IAM database authentication**" matches "**integrates with Identity and Access Management (IAM)**".
- ✔️ "**Access the database through the Cloud SQL Auth Proxy**" matches "**encrypted and authenticated connection that requires minimal management**".

📌 **When to use it:** Use it when an app must connect to its database securely without anyone managing passwords or certificates.
🏢 **Office example:** A private tunnel to the records room that only opens for the right staff badge.

### ❌ D
> **D.** Deploy a Cloud SQL database and configure a database user and password. Access the database through the Cloud SQL Auth Proxy.

**Wrong words:**
- ✔️ Auth Proxy is right.
- ❌ "**database user and password**": not IAM-integrated; passwords to manage.

📌 **When to use it:** Use DB passwords only when IAM auth isn't supported.
🏢 **Office example:** A secure tunnel, but still a shared PIN at the end.

---

## 🛒 E-Commerce Full-Stack Example

Cloud Run `checkout` with Cloud SQL connector (built-in Auth Proxy) + IAM DB user `checkout-sa@shopnow-prod.iam`.

---

## 🧠 Key Takeaways / Memory Tips

- **Encrypted + IAM + low management → Cloud SQL Auth Proxy + IAM database authentication.**
  🧠 *"**Proxy encrypts, IAM authenticates.**"*
- Related: **Q188**, **Q217**.

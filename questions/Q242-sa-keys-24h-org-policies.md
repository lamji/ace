# Q242: Short-Lived Service Account Keys Only in pj-sa (Org Policies: Key Expiry 24h + Deny Key Creation Except pj-sa)

**Topic:** Organization Policy (service account key constraints)

## ❓ Question
> You recently discovered that your developers are using many service account keys during their development process. While you work on a long term improvement, you need to quickly implement a process to enforce short-lived service account credentials in your company. You have the following requirements: • All service accounts that require a key should be created in a centralized project called pj-sa. • Service account keys should only be valid for one day. You need a Google-recommended solution that minimizes cost. What should you do?
>
> **A.** Implement a Cloud Run job to rotate all service account keys periodically in pj-sa. Enforce an org policy to deny service account key creation with an exception to pj-sa.
>
> **B.** Implement a Kubernetes CronJob to rotate all service account keys periodically. Disable attachment of service accounts to resources in all projects with an exception to pj-sa.
>
> **C.** Enforce an org policy constraint allowing the lifetime of service account keys to be 24 hours. Enforce an org policy constraint denying service account key creation with an exception on pj-sa.
>
> **D.** Enforce a DENY org policy constraint over the lifetime of service account keys for 24 hours. Disable attachment of service accounts to resources in all projects with an exception to pj-sa.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Keys must **expire after 1 day**, and only **pj-sa** may create keys. Quick and cheap.

**Clues in the question:**
- "**valid for one day**" → org policy **`iam.serviceAccountKeyExpiryHours`** = 24h.
- "**should be created in … pj-sa**" → **`iam.disableServiceAccountKeyCreation`** enforced everywhere **except pj-sa**.
- "**minimizes cost**" → built-in policies, no code to run.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. iam.serviceAccountKeyExpiryHours 🔑
- **What it is:** Org policy that sets how long new service account keys stay valid (e.g. 24h).
- **Looks like:** allowed value `24h`
- **Not to be confused with:** manual rotation.
- **Analogy:** ⏳ Day passes that stop working at midnight.
- **In the online store:** Dev keys expire daily.

### 2. iam.disableServiceAccountKeyCreation
- **What it is:** Org policy that blocks creating SA keys; can be turned off for chosen projects.
- **Looks like:** enforced at org, not enforced on pj-sa
- **Not to be confused with:** —
- **Analogy:** 🚫 "No key cutting" rule except at the key office.
- **In the online store:** —

### 🔗 How they fit together
```
 Org: disableServiceAccountKeyCreation = ON   (pj-sa: OFF) ✅
 Org: serviceAccountKeyExpiryHours = 24h ✅
```

---

## 🌍 Real-World Scenario

Security sees too many long-lived keys. The admin sets **key expiry to 24h** and **blocks key creation everywhere except pj-sa**. No code to maintain.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Implement a Cloud Run job to rotate all service account keys periodically in pj-sa. Enforce an org policy to deny service account key creation with an exception to pj-sa.

**Wrong words:**
- ✔️ "deny service account key creation with an exception to pj-sa" is right.
- ❌ "**Cloud Run job to rotate all service account keys**": custom code and running cost, and rotation isn't expiry.

📌 **When to use it:** Use rotation jobs only if no built-in expiry exists.
🏢 **Office example:** Hiring someone to swap everyone's keys daily.

### ❌ B
> **B.** Implement a Kubernetes CronJob to rotate all service account keys periodically. Disable attachment of service accounts to resources in all projects with an exception to pj-sa.

**Wrong words:**
- ❌ "**Kubernetes CronJob to rotate**": code + cluster cost.
- ❌ "**Disable attachment of service accounts to resources**": breaks normal workloads and doesn't limit keys.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Banning staff badges to stop key copying.

### ✅ C
> **C.** Enforce an org policy constraint allowing the lifetime of service account keys to be 24 hours. Enforce an org policy constraint denying service account key creation with an exception on pj-sa.

**Why it's correct:**
- ✔️ "**org policy constraint allowing the lifetime of service account keys to be 24 hours**" matches "**Service account keys should only be valid for one day**".
- ✔️ "**denying service account key creation with an exception on pj-sa**" matches "**All service accounts that require a key should be created in … pj-sa**".
- ✔️ Built-in policies, no code, which matches "**minimizes cost**".

📌 **When to use it:** Use it when you want company rules enforced automatically without anyone writing programs.
🏢 **Office example:** A company rule: keys can only be cut at the central key office, and every key stops working after one day.

### ❌ D
> **D.** Enforce a DENY org policy constraint over the lifetime of service account keys for 24 hours. Disable attachment of service accounts to resources in all projects with an exception to pj-sa.

**Wrong words:**
- ❌ "**DENY org policy constraint over the lifetime**": the expiry constraint is an allow-list of durations, not a deny.
- ❌ "**Disable attachment of service accounts**": wrong control.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A rule worded backwards and banning badges.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud resource-manager org-policies enable-enforce iam.disableServiceAccountKeyCreation --organization=SHOPNOW_ORG
gcloud resource-manager org-policies disable-enforce iam.disableServiceAccountKeyCreation --project=pj-sa
# set iam.serviceAccountKeyExpiryHours allowedValues: ["24h"] at the org
```

---

## 🧠 Key Takeaways / Memory Tips

- **Limit SA keys → org policies: key expiry hours + disable key creation (with exceptions).**
  🧠 *"**Expire in a day, create in one place.**"*
- Related: **Q204**, **Q220**, **Q170**.

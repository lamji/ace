# Q323: Company-Wide SSH Standard With Audit Compliance and Few Manual Steps (Enforce OS Login via Organization Policy)

**Topic:** Compute Engine (OS Login, org policy)

## ❓ Question
> You are implementing a company-wide standard to control SSH access for your Google Cloud projects. You want to simplify SSH access management to your Compute Engine instances while maintaining audit compliance and eliminating as many manual steps as possible. What should you do?
>
> **A.** Configure a service account to add SSH keys for all VMs.
>
> **B.** Configure metadata SSH keys to manage sudo access to instances.
>
> **C.** Enable OS Login by using an organization policy for each Google Cloud project.
>
> **D.** Enable OS Login with two-factor authentication for the domain.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **C**. In practice, the org policy `constraints/compute.requireOsLogin` is set once at the organization (it applies to all projects). D (2-step verification) adds security but isn't the step that standardizes SSH management.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are creating a company-wide standard for SSH access to Compute Engine VMs.
- **What you must achieve:** Make SSH access simple to manage.
- **The limits:** Keep audit compliance (records of who logged in) and remove as many manual steps as possible.
- **What they're really asking:** How do you enforce one SSH standard across all projects?

**Clues in the question:**
- "**company-wide standard**" + "**eliminating as many manual steps**" → enforce **OS Login** with the **org policy** `compute.requireOsLogin`.
- "**audit compliance**" → OS Login logs each user's identity.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. constraints/compute.requireOsLogin 🔑
- **What it is:** Org policy that turns OS Login on for all VMs under the org/folder/project.
- **Looks like:** `gcloud resource-manager org-policies enable-enforce compute.requireOsLogin --organization=123`
- **Not to be confused with:** OS Login 2FA (extra login step).
- **Analogy:** 🏢 HQ rule: every door uses badges.
- **In the online store:** ShopNow org.

### 🔗 How they fit together
```
 org policy requireOsLogin → all projects' VMs use OS Login ✅
```

---

## 🌍 Real-World Scenario

Security enforces **OS Login** across the org with an **org policy**, so SSH is tied to IAM and audited.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure a service account to add SSH keys for all VMs.

**Wrong words:**
- ❌ "**service account to add SSH keys**": still key management; no individual audit trail.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** A robot copying keys to every door.

### ❌ B
> **B.** Configure metadata SSH keys to manage sudo access to instances.

**Wrong words:**
- ❌ "**metadata SSH keys**": manual key management, weak audit.

📌 **When to use it:** Use metadata keys for edge cases without Google accounts.
🏢 **Office example:** Hand-cut keys.

### ✅ C
> **C.** Enable OS Login by using an organization policy for each Google Cloud project.

**Why it's correct:**
- ✔️ "**Enable OS Login by using an organization policy**" matches "**company-wide standard to control SSH access**" + "**eliminating as many manual steps**".
- ✔️ OS Login ties logins to identities, matching "**maintaining audit compliance**".

📌 **When to use it:** Use it when every office in the company should use the same badge system without setting each door by hand.
🏢 **Office example:** HQ rules that every door in every branch uses staff badges.

### ❌ D
> **D.** Enable OS Login with two-factor authentication for the domain.

**Wrong words:**
- ✔️ OS Login is good; 2FA adds security.
- ❌ "**two-factor authentication for the domain**": extra login step; doesn't by itself standardize enabling OS Login across projects.

📌 **When to use it:** Use OS Login 2FA when you need stronger login checks.
🏢 **Office example:** Adding a PIN to the badge, but not every door uses badges yet.

---

## 🛒 E-Commerce Full-Stack Example

Org policy `compute.requireOsLogin` enforced at `organizations/shopnow`.

---

## 🧠 Key Takeaways / Memory Tips

- **Company-wide SSH standard → enforce OS Login with an org policy.**
  🧠 *"**One policy, every door.**"*
- Related: **Q294**, **Q302**.

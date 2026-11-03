# Q318: Let Teams Deploy Independently While Following Company Practices (Compliant Terraform Modules)

**Topic:** Infrastructure as Code (Terraform modules)

## ❓ Question
> You assist different engineering teams in deploying their infrastructure on Google Cloud. Your company has defined certain practices required for all workloads. You need to provide the engineering teams with a solution that enables teams to deploy their infrastructure independently without having to know all implementation details of the company’s required practices. What should you do?
>
> **A.** Configure organization policies to enforce your company's required practices. Ask the teams to provision their infrastructure by using the Google Cloud console.
>
> **B.** Create a service account per team, and grant the service account the Project Editor role. Ask the teams to provision their infrastructure through the Google Cloud CLI (gcloud CL), while impersonating their dedicated service account.
>
> **C.** Write Terraform modules for each component that are compliant with the company's required practices, and ask teams to implement their infrastructure through these modules.
>
> **D.** Provide training for all engineering teams you work with to understand the company’s required practices. Allow the engineering teams to provision the infrastructure to best meet their needs.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Teams deploy on their own **without knowing every detail** of company practices.

**Clues in the question:**
- "**without having to know all implementation details**" → reusable **Terraform modules** that build in the practices.

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Terraform module 🔑
- **What it is:** A reusable package of Terraform code with inputs; callers fill in a few values.
- **Looks like:** `module "bucket" { source = "git::.../secure-bucket" name = "team-a-data" }`
- **Not to be confused with:** copy-pasted code.
- **Analogy:** 📋 A pre-approved form template.
- **In the online store:** ShopNow secure bucket module.

### 🔗 How they fit together
```
 platform team → compliant modules → teams call modules ✅
```

---

## 🌍 Real-World Scenario

A platform team publishes **compliant modules** (bucket, VPC, GKE); teams just fill in names and sizes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure organization policies to enforce your company's required practices. Ask the teams to provision their infrastructure by using the Google Cloud console.

**Wrong words:**
- ✔️ Org policies help.
- ❌ "**provision … by using the Google Cloud console**": teams must still know the practices; manual.

📌 **When to use it:** Use org policies as guardrails.
🏢 **Office example:** Rules on the wall but everyone fills forms from scratch.

### ❌ B
> **B.** Create a service account per team, and grant the service account the Project Editor role. Ask the teams to provision their infrastructure through the Google Cloud CLI (gcloud CL), while impersonating their dedicated service account.

**Wrong words:**
- ❌ "**Project Editor role**": broad access, no built-in practices.

📌 **When to use it:** **Avoid** — Editor is too broad.
🏢 **Office example:** Master keys for each team.

### ✅ C
> **C.** Write Terraform modules for each component that are compliant with the company's required practices, and ask teams to implement their infrastructure through these modules.

**Why it's correct:**
- ✔️ "**Terraform modules … compliant with the company's required practices**" matches "**without having to know all implementation details**".
- ✔️ "**ask teams to implement their infrastructure through these modules**" matches "**deploy their infrastructure independently**".

📌 **When to use it:** Use it when many teams should build things their own way but always follow company rules.
🏢 **Office example:** Pre-approved form templates: teams fill blanks, the rules are already built in.

### ❌ D
> **D.** Provide training for all engineering teams you work with to understand the company’s required practices. Allow the engineering teams to provision the infrastructure to best meet their needs.

**Wrong words:**
- ❌ "**Provide training … best meet their needs**": relies on everyone remembering; inconsistent.

📌 **When to use it:** Use training alongside tooling.
🏢 **Office example:** A class instead of a template.

---

## 🛒 E-Commerce Full-Stack Example

`modules/secure-bucket` enforces UBLA, CMEK, labels; teams call it.

---

## 🧠 Key Takeaways / Memory Tips

- **Self-service + built-in standards → reusable Terraform modules.**
  🧠 *"**Modules carry the rules.**"*
- Related: **Q304**.

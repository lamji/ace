# G014: Build an Enterprise Google Cloud Foundation With Terraform From Google's Reference Design (Fabric FAST)

**Topic:** Infrastructure as Code (Fabric FAST)
**Exam guide section:** 2.4 Planning and implementing resources using tooling: Infrastructure as Code tooling (Fabric FAST)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your company is adopting Google Cloud and must build an enterprise foundation that includes the organization setup, folders, billing, centralized logging, Shared VPC networking, and security baselines. The platform team wants to use Terraform and start from an opinionated reference design published by Google instead of writing everything from scratch. What should you use?
>
> **A.** Fabric FAST from the Cloud Foundation Fabric repository.
>
> **B.** A Helm chart installed on a GKE cluster.
>
> **C.** Cloud Deployment Manager templates written by your team.
>
> **D.** Manual configuration in the Google Cloud console.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A company is starting on Google Cloud and needs the base setup every large company needs (a landing zone): the organization, folders, billing, central logs, shared networking, and security rules.
- **What you must achieve:** Build that base with Terraform (a tool that creates cloud resources from code files).
- **The limits:** Don't start from a blank page. Start from a ready-made, opinionated design published by Google.
- **What they're really asking:** Which Google-published Terraform toolkit sets up a full enterprise foundation?

**Clues in the question:**
- "**enterprise foundation … organization setup, folders, billing, centralized logging, Shared VPC**": a **landing zone**.
- "**Terraform**" + "**opinionated reference design published by Google**": **Fabric FAST** (part of Cloud Foundation Fabric on GitHub).

**Exam topic:** Tooling and IaC (exam guide section 2.4).

---

## 📚 Key Terms Explained

### 1. Landing zone
- **What it is:** The foundation of a cloud setup: org structure, identity, billing, networking, logging and security guardrails, all in place before apps arrive.
- **Looks like:** Org → folders `prod`, `dev`, `shared` → Shared VPC host project, log sink project
- **Not to be confused with:** A single app project.
- **Analogy:** 🏗️ The building's foundation, plumbing and wiring before tenants move in.
- **In the online store:** ShopNow's org, folders and shared network.

### 2. Fabric FAST 🔑
- **What it is:** A Terraform-based set of **stages** (bootstrap, resource management, security, networking, project factory) from Google's open-source Cloud Foundation Fabric repository. It builds an enterprise landing zone following Google's recommendations.
- **Looks like:** `git clone github.com/GoogleCloudPlatform/cloud-foundation-fabric` → `fast/stages/0-bootstrap` → `terraform apply`
- **Not to be confused with:** Helm (Kubernetes app packages) or Config Connector (Kubernetes-style resources).
- **Analogy:** 📐 An architect's tested blueprint for an office tower.
- **In the online store:** Stage `2-networking` creates the Shared VPC.

### 🔗 How they fit together
```
 Fabric FAST stages (Terraform):
 0-bootstrap → 1-resman (folders) → 2-security / 2-networking (Shared VPC) → 3-project factory ✅
```

---

## 🌍 Real-World Scenario

A retailer moving from on-prem needs a secure foundation in weeks, not months. The platform team forks **Fabric FAST**, fills in its organization ID, billing account and IP ranges, and applies the stages in order. They get folders, a log sink, a Shared VPC and org policies that follow Google's recommendations.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Fabric FAST from the Cloud Foundation Fabric repository.

**Why it's correct:**
- ✔️ "**Fabric FAST**" matches "**opinionated reference design published by Google**".
- ✔️ It is Terraform, which matches "**use Terraform**".
- ✔️ Its stages cover "**organization setup, folders, billing, centralized logging, Shared VPC networking, and security baselines**".

📌 **When to use it:** Use it when you must set up a company-wide cloud foundation with code and want a proven blueprint to start from.
🏢 **Office example:** Using a tested architect's blueprint for a new office building instead of sketching one yourself.

### ❌ B
> **B.** A Helm chart installed on a GKE cluster.

**Wrong words:**
- ❌ "**Helm chart**": installs apps inside Kubernetes, not organizations, folders or billing.

📌 **When to use it:** Use Helm to install packaged apps on Kubernetes clusters.
🏢 **Office example:** An appliance installer, not a building blueprint.

### ❌ C
> **C.** Cloud Deployment Manager templates written by your team.

**Wrong words:**
- ❌ "**Deployment Manager**": Google's older tool, now deprecated, and not Terraform.
- ❌ "**written by your team**": the opposite of starting from Google's reference design.

📌 **When to use it:** Avoid it for new work. Use Terraform-based tooling.
🏢 **Office example:** An old drafting kit that's being retired.

### ❌ D
> **D.** Manual configuration in the Google Cloud console.

**Wrong words:**
- ❌ "**Manual configuration in the Google Cloud console**": not code, hard to repeat or review, and not Terraform.

📌 **When to use it:** Use the console to explore or for one-off small changes.
🏢 **Office example:** Building the office by hand with no blueprint.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** foundation (Fabric FAST):
- Folders `storefront`, `data`, `shared`; Shared VPC host `shopnow-net-prod`.
- Org log sink → `shopnow-audit-logs`; org policies such as `iam.disableServiceAccountKeyCreation`.

---

## 🧠 Key Takeaways / Memory Tips

- **Enterprise landing zone + Terraform + Google's opinionated reference → Fabric FAST.**
  🧠 *"**FAST foundation.**"*
- Related: **Q272**, **Q318**, **Q341** (Terraform).

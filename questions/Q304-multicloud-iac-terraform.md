# Q304: Infrastructure as Code Across Google Cloud and Two Other Clouds (Terraform)

**Topic:** Infrastructure as Code (Terraform)

## ❓ Question
> Your organization has decided to deploy all its compute workloads to Kubernetes on Google Cloud and two other cloud providers. You want to build an Infrastructure-as-code solution to automate the provisioning process for all cloud resources. What should you do?
>
> **A.** Build the solution by using Config Connector, and provision the resources.
>
> **B.** Build the solution by using Terraform, and provision the resources.
>
> **C.** Build solution by using Python and the cloud SDKs from all providers to provision the resources.
>
> **D.** Build the solution by using YAML manifests, and provision the resources.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company will run all its workloads on Kubernetes in Google Cloud and two other cloud providers.
- **What you must achieve:** Build an Infrastructure as Code solution (resources described in code) that creates resources in all three clouds.
- **The limits:** It must work across all three providers.
- **What they're really asking:** Which tool can provision resources in all three clouds?

**Clues in the question:**
- "**two other cloud providers**" + "**Infrastructure-as-code**" → **Terraform** (multi-cloud providers).

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Terraform 🔑
- **What it is:** Open-source IaC tool; describe resources in HCL; providers for Google Cloud, AWS, Azure, and more.
- **Looks like:** `resource "google_container_cluster" "main" { ... }` + `resource "aws_eks_cluster" ...`
- **Not to be confused with:** Config Connector (Google Cloud only).
- **Analogy:** 📐 One blueprint language every builder reads.
- **In the online store:** ShopNow infra repo.

### 🔗 How they fit together
```
 Terraform → Google Cloud + AWS + Azure ✅
```

---

## 🌍 Real-World Scenario

A company running Kubernetes on three clouds uses **Terraform** to provision all of them from one repo.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Build the solution by using Config Connector, and provision the resources.

**Wrong words:**
- ❌ "**Config Connector**": manages Google Cloud resources only.

📌 **When to use it:** Use Config Connector for Google Cloud resources managed from Kubernetes.
🏢 **Office example:** A blueprint only one builder can read.

### ✅ B
> **B.** Build the solution by using Terraform, and provision the resources.

**Why it's correct:**
- ✔️ "**Terraform**" matches "**Kubernetes on Google Cloud and two other cloud providers**" + "**Infrastructure-as-code**".

📌 **When to use it:** Use it when you build the same kind of setup in several different clouds and want one way to describe it.
🏢 **Office example:** One blueprint language that builders in every city understand.

### ❌ C
> **C.** Build solution by using Python and the cloud SDKs from all providers to provision the resources.

**Wrong words:**
- ❌ "**Python and the cloud SDKs**": custom code, not declarative IaC; heavy to maintain.

📌 **When to use it:** Use SDK scripts for small automations.
🏢 **Office example:** Writing your own construction manual.

### ❌ D
> **D.** Build the solution by using YAML manifests, and provision the resources.

**Wrong words:**
- ❌ "**YAML manifests**": Kubernetes objects, not cloud resources like networks and clusters.

📌 **When to use it:** Use manifests for apps inside a cluster.
🏢 **Office example:** Furniture layout plans, not building plans.

---

## 🛒 E-Commerce Full-Stack Example

`terraform/` with `google`, `aws`, `azurerm` providers.

---

## 🧠 Key Takeaways / Memory Tips

- **Multi-cloud IaC → Terraform.**
  🧠 *"**Many clouds, one Terraform.**"*
- Related: **Q318**, **Q372**.

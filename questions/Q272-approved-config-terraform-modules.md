# Q272: Engineers Deploy Google Cloud Products Only in an Approved Configuration (Terraform Modules in a Repository)

**Topic:** Infrastructure as Code (Terraform modules)

## ❓ Question
> Your company requires that Google Cloud products are created with a specific configuration to comply with your company's security policies. You need to implement a mechanism that will allow software engineers at your company to deploy and update Google Cloud products in a preconfigured and approved manner. What should you do?
>
> **A.** Create Java packages that utilize the Google Cloud Client Libraries for Java to configure Google Cloud products. Store and share the packages in a source code repository.
>
> **B.** Create bash scripts that utilize the Google Cloud CLI to configure Google Cloud products. Store and share the bash scripts in a source code repository.
>
> **C.** Use the Google Cloud APIs by using curl to configure Google Cloud products. Store and share the curl commands in a source code repository.
>
> **D.** Create Terraform modules that utilize the Google Cloud Terraform Provider to configure Google Cloud products. Store and share the modules in a source code repository.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Company security policy requires Google Cloud products to be created with a specific configuration.
- **What you must achieve:** Let engineers deploy and update products only in a pre-approved setup.
- **The limits:** It must be preconfigured and approved.
- **What they're really asking:** How can engineers deploy products that already follow company settings?

**Clues in the question:**
- "**deploy and update … in a preconfigured and approved manner**" → reusable **Terraform modules** (declarative, handle updates, reviewable).

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Terraform module 🔑
- **What it is:** A reusable, parameterized block of Terraform code (e.g. "secure bucket") that others call with a few inputs.
- **Looks like:** `module "bucket" { source = "git::…//secure-bucket" name = "x" }`
- **Not to be confused with:** scripts.
- **Analogy:** 📄 An approved template form.
- **In the online store:** ShopNow secure-bucket module.

### 🔗 How they fit together
```
 approved module (secure defaults) ─► engineers: terraform apply ✅ (create + update)
```

---

## 🌍 Real-World Scenario

A platform team publishes **Terraform modules** (secure bucket, private GKE) in a repo. Engineers reuse them; every resource follows policy.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create Java packages that utilize the Google Cloud Client Libraries for Java to configure Google Cloud products. Store and share the packages in a source code repository.

**Wrong words:**
- ❌ "**Java packages … Client Libraries**": imperative code; hard to manage updates and drift.

📌 **When to use it:** Use client libraries inside applications.
🏢 **Office example:** Writing a custom program to fill in a form.

### ❌ B
> **B.** Create bash scripts that utilize the Google Cloud CLI to configure Google Cloud products. Store and share the bash scripts in a source code repository.

**Wrong words:**
- ❌ "**bash scripts … Google Cloud CLI**": imperative; updates and state are hard.

📌 **When to use it:** Use scripts for small one-off tasks.
🏢 **Office example:** A checklist people may follow differently.

### ❌ C
> **C.** Use the Google Cloud APIs by using curl to configure Google Cloud products. Store and share the curl commands in a source code repository.

**Wrong words:**
- ❌ "**curl commands**": raw API calls; error-prone and no state.

📌 **When to use it:** Use curl for quick API tests.
🏢 **Office example:** Phoning in each setting by hand.

### ✅ D
> **D.** Create Terraform modules that utilize the Google Cloud Terraform Provider to configure Google Cloud products. Store and share the modules in a source code repository.

**Why it's correct:**
- ✔️ "**Terraform modules**" matches "**preconfigured and approved manner**": the module holds the approved settings.
- ✔️ Terraform tracks state, which matches "**deploy and update Google Cloud products**".
- ✔️ "**Store and share the modules in a source code repository**": reviewed, versioned, reusable.

📌 **When to use it:** Use it when everyone should build things from the same approved templates.
🏢 **Office example:** An approved template form that staff fill in, so every request follows company rules.

---

## 🛒 E-Commerce Full-Stack Example

Repo `shopnow-tf-modules`: `secure-bucket`, `private-gke`, `cloudsql-ha`. Teams: `module "img" { source = "git::…//secure-bucket" }`.

---

## 🧠 Key Takeaways / Memory Tips

- **Approved, repeatable deployments → Terraform modules in a shared repo.**
  🧠 *"**Approved template = module.**"*
- Related: **Q143**, **Q160**, **Q222**.

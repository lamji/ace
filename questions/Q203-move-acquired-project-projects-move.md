# Q203: Move an Acquired Startup's Project Into Your Organization and Billing (projects.move + Change Billing Account)

**Topic:** Resource hierarchy (migrating projects between organizations)

## ❓ Question
> Your company completed the acquisition of a startup and is now merging the IT systems of both companies. The startup had a production Google Cloud project in their organization. You need to move this project into your organization and ensure that the project is billed to your organization. You want to accomplish this task with minimal effort. What should you do?
>
> **A.** Use the projects.move method to move the project to your organization. Update the billing account of the project to that of your organization.
>
> **B.** Ensure that you have an Organization Administrator Identity and Access Management (IAM) role assigned to you in both organizations. Navigate to the Resource Manager in the startup's Google Cloud organization, and drag the project to your company's organization.
>
> **C.** Create a Private Catalog for the Google Cloud Marketplace, and upload the resources of the startup's production project to the Catalog. Share the Catalog with your organization, and deploy the resources in your company's project.
>
> **D.** Create an infrastructure-as-code template for all resources in the project by using Terraform, and deploy that template to a new project in your organization. Delete the project from the startup's Google Cloud organization.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company bought a startup that has a production project in its own organization.
- **What you must achieve:** Move that project into your organization and bill it to your company.
- **The limits:** Minimal effort.
- **What they're really asking:** How do you move the project and its billing?

**Clues in the question:**
- "**move this project into your organization**" → **projects.move** (`gcloud beta projects move`).
- "**billed to your organization**" → **change its billing account**.
- "**minimal effort**" → don't rebuild.

**Exam topic:** Resource hierarchy.

---

## 📚 Key Terms Explained

### 1. projects.move 🔑
- **What it is:** The Resource Manager API call (or `gcloud beta projects move`) that moves a project to a **new parent** (folder or org). Resources stay as they are.
- **Looks like:** `gcloud beta projects move startup-prod --organization=123456789`
- **Not to be confused with:** rebuilding.
- **Analogy:** 🚚 Moving a whole office with furniture in place.
- **In the online store:** Merge acquired shop.

### 2. Change billing account (review from Q164)
- **What it is:** Link the project to a different billing account.
- **Looks like:** `gcloud billing projects link startup-prod --billing-account=…`
- **Not to be confused with:** —
- **Analogy:** 💳 Switching the card.
- **In the online store:** —

### 🔗 How they fit together
```
 startup org: startup-prod ── projects.move ──► your org ✅ → link to your billing account ✅
```

---

## 🌍 Real-World Scenario

After an acquisition, the admin uses **projects.move** to bring the startup's project under the parent org (with the needed permissions in both orgs), then links it to the parent company's billing account.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use the projects.move method to move the project to your organization. Update the billing account of the project to that of your organization.

**Why it's correct:**
- ✔️ "**Use the projects.move method to move the project to your organization**" matches "**move this project into your organization**" + "**minimal effort**".
- ✔️ "**Update the billing account of the project**" matches "**ensure that the project is billed to your organization**".

📌 **When to use it:** Use it when a whole team's workspace changes owner and should keep running as is.
🏢 **Office example:** Moving an office to the new head company with all furniture in place, then switching the rent to the new company's account.

### ❌ B
> **B.** Ensure that you have an Organization Administrator Identity and Access Management (IAM) role assigned to you in both organizations. Navigate to the Resource Manager in the startup's Google Cloud organization, and drag the project to your company's organization.

**Wrong words:**
- ✔️ Admin rights in both orgs are useful.
- ❌ "**drag the project to your company's organization**": there's no drag-and-drop between orgs.
- ❌ It also doesn't change the **billing**.

📌 **When to use it:** **Never** rely on this — it isn't a real feature.
🏢 **Office example:** Trying to drag a building across town on a map.

### ❌ C
> **C.** Create a Private Catalog for the Google Cloud Marketplace, and upload the resources of the startup's production project to the Catalog. Share the Catalog with your organization, and deploy the resources in your company's project.

**Wrong words:**
- ❌ "**Private Catalog … upload the resources**": Private Catalog shares deployable solutions, not existing production resources. Lots of effort.

📌 **When to use it:** Use Private Catalog to share approved templates internally.
🏢 **Office example:** Writing a brochure about the office instead of moving it.

### ❌ D
> **D.** Create an infrastructure-as-code template for all resources in the project by using Terraform, and deploy that template to a new project in your organization. Delete the project from the startup's Google Cloud organization.

**Wrong words:**
- ❌ "**Terraform … new project … Delete the project**": rebuilding is a lot of work and risks losing data.

📌 **When to use it:** Use IaC for new, repeatable environments.
🏢 **Office example:** Rebuilding the office from blueprints and demolishing the old one.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud beta projects move acquired-shop-prod --organization=SHOPNOW_ORG_ID
gcloud billing projects link acquired-shop-prod --billing-account=01AB23-CD45EF-678901
```

---

## 🧠 Key Takeaways / Memory Tips

- **Move a project between orgs → projects.move + relink billing.**
  🧠 *"**Move it, then pay for it.**"*
- Related: **Q164**, **Q190**.

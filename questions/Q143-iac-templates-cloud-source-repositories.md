# Q143: Sharing Proposed Infrastructure Changes With the Team (Deployment Manager Templates in Cloud Source Repositories)

**Topic:** Infrastructure as Code (Deployment Manager, source control, Cloud Source Repositories)

## ❓ Question
> Your team maintains the infrastructure for your organization. The current infrastructure requires changes. You need to share your proposed changes with the rest of the team. You want to follow Google's recommended best practices. What should you do?
>
> **A.** Use Deployment Manager templates to describe the proposed changes and store them in a Cloud Storage bucket.
>
> **B.** Use Deployment Manager templates to describe the proposed changes and store them in Cloud Source Repositories.
>
> **C.** Apply the changes in a development environment, run gcloud compute instances list, and then save the output in a shared Storage bucket.
>
> **D.** Apply the changes in a development environment, run gcloud compute instances list, and then save the output in Cloud Source Repositories.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team maintains the company's infrastructure, and you have proposed changes.
- **What you must achieve:** Share those changes with the rest of the team.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** How should infrastructure changes be shared?

**Clues in the question:**
- "**describe the proposed changes**": write infrastructure as **code** (templates).
- "**share … with the rest of the team**": put code in **version control** (a Git repo), so people can review, comment and see the history.

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Deployment Manager templates 🔑
- **What it is:** Files (YAML/Jinja/Python) that **describe Google Cloud resources as code**. Deploying the file creates or updates them.
- **Looks like:** `resources: - name: web-1, type: compute.v1.instance, properties: {machineType: …}`
- **Not to be confused with:** clicking in the console.
- **Analogy:** 📐 **Blueprints** for the building.
- **In the online store:** ShopNow's network and VMs as YAML.

### 2. Cloud Source Repositories
- **What it is:** Google's private **Git repository** service, with branches, history and reviews.
- **Looks like:** `git push google main`
- **Not to be confused with:** a Cloud Storage bucket (no history or review).
- **Analogy:** 📚 A **shared binder with change tracking**.
- **In the online store:** The `infra` repo with all templates.

### 🔗 How they fit together
```
 edit template (code) → git commit → Cloud Source Repositories ✅ → team reviews diff → deploy
```

---

## 🌍 Real-World Scenario

A platform engineer proposes adding a new subnet and firewall rule. They change the **Deployment Manager template**, commit it to a branch in **Cloud Source Repositories**, and ask the team to review the diff before deploying.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Deployment Manager templates to describe the proposed changes and store them in a Cloud Storage bucket.

**Wrong words:**
- ✔️ "Deployment Manager templates" is right.
- ❌ "**store them in a Cloud Storage bucket**": no version history, diffs or review workflow.

📌 **When to use it:** Use a bucket to store build artifacts or backups.
🏢 **Office example:** Putting blueprints in a box instead of a tracked binder.

### ✅ B
> **B.** Use Deployment Manager templates to describe the proposed changes and store them in Cloud Source Repositories.

**Why it's correct:**
- ✔️ "**Deployment Manager templates to describe the proposed changes**" matches "**infrastructure requires changes**": changes as reviewable code.
- ✔️ "**store them in Cloud Source Repositories**" matches "**share your proposed changes with the rest of the team**" + "**best practices**": Git gives history, diffs and reviews.

📌 **When to use it:** Use it when team members should review and track changes before they're made.
🏢 **Office example:** Putting the new blueprints in the shared binder with change tracking for everyone to review.

### ❌ C
> **C.** Apply the changes in a development environment, run gcloud compute instances list, and then save the output in a shared Storage bucket.

**Wrong words:**
- ❌ "**Apply the changes**": you're making changes before sharing the proposal.
- ❌ "**gcloud compute instances list**": a list of VMs doesn't describe the changes.

📌 **When to use it:** Use instance lists to check what's running.
🏢 **Office example:** Building the extension first, then sharing a list of rooms.

### ❌ D
> **D.** Apply the changes in a development environment, run gcloud compute instances list, and then save the output in Cloud Source Repositories.

**Wrong words:**
- ❌ "**Apply the changes … instances list**": same problem as C, even though it's stored in a repo.

📌 **When to use it:** **Never use this** for proposals.
🏢 **Office example:** Filing a room list in the binder after building the extension.

---

## 🛒 E-Commerce Full-Stack Example

```bash
git checkout -b add-eu-subnet
vim network.yaml        # Deployment Manager template: new subnet + firewall
git commit -am "Add eu-west1 subnet for storefront" && git push google add-eu-subnet
```
Teammates review the diff, then run `gcloud deployment-manager deployments update shop-net --config network.yaml`.

---

## 🧠 Key Takeaways / Memory Tips

- **Infrastructure changes → IaC templates in a Git repo** (Cloud Source Repositories).
- Buckets don't track changes.
  🧠 *"**Blueprints belong in Git.**"*
- Related: **Q069** (Deployment Manager), **Q160** (templates reduce repetition).

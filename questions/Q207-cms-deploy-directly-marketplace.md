# Q207: Quick and Easy CMS Install (Deploy Directly From Cloud Marketplace)

**Topic:** Marketplace

## ❓ Question
> Your team wants to deploy a specific content management system (CMS) solution to Google Cloud. You need a quick and easy way to deploy and install the solution. What should you do?
>
> **A.** Search for the CMS solution in Google Cloud Marketplace. Use gcloud CLI to deploy the solution.
>
> **B.** Search for the CMS solution in Google Cloud Marketplace. Deploy the solution directly from Cloud Marketplace.
>
> **C.** Search for the CMS solution in Google Cloud Marketplace. Use Terraform and the Cloud Marketplace ID to deploy the solution with the appropriate parameters.
>
> **D.** Use the installation guide of the CMS provider. Perform the installation through your configuration management system.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team wants to use a specific content management system (CMS, software for running websites).
- **What you must achieve:** Deploy and install it.
- **The limits:** Quick and easy.
- **What they're really asking:** What is the fastest way to deploy a ready-made CMS?

**Clues in the question:**
- "**quick and easy**" → **Marketplace**, and click **Deploy right there** (no extra tools).

**Exam topic:** Marketplace.

---

## 📚 Key Terms Explained

### 1. Cloud Marketplace deploy 🔑 (review from Q137)
- **What it is:** Ready-made solutions you deploy in a few clicks from the console; it creates the VMs, disks and firewall rules.
- **Looks like:** Marketplace → WordPress → Launch
- **Not to be confused with:** manual installation.
- **Analogy:** 🛒 Buying a pre-assembled desk instead of a kit.
- **In the online store:** ShopNow blog CMS.

### 🔗 How they fit together
```
 Marketplace → WordPress → [Launch] → running VM ✅
```

---

## 🌍 Real-World Scenario

Marketing wants a WordPress blog today. The engineer finds it in **Marketplace** and clicks **Launch**; it's live in minutes.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Search for the CMS solution in Google Cloud Marketplace. Use gcloud CLI to deploy the solution.

**Wrong words:**
- ✔️ "Search … in Google Cloud Marketplace" is right.
- ❌ "**Use gcloud CLI to deploy**": extra steps; the console deploy is quicker and easier.

📌 **When to use it:** Use the CLI when scripting many deployments.
🏢 **Office example:** Ordering the pre-assembled desk, then rebuilding it yourself.

### ✅ B
> **B.** Search for the CMS solution in Google Cloud Marketplace. Deploy the solution directly from Cloud Marketplace.

**Why it's correct:**
- ✔️ "**Search for the CMS solution in Google Cloud Marketplace**" matches "**deploy a specific content management system**".
- ✔️ "**Deploy the solution directly from Cloud Marketplace**" matches "**quick and easy way to deploy and install**".

📌 **When to use it:** Use it when you want common software running fast with the least setup.
🏢 **Office example:** Ordering a pre-assembled desk that's delivered and placed for you.

### ❌ C
> **C.** Search for the CMS solution in Google Cloud Marketplace. Use Terraform and the Cloud Marketplace ID to deploy the solution with the appropriate parameters.

**Wrong words:**
- ❌ "**Use Terraform and the Cloud Marketplace ID**": more setup than needed.

📌 **When to use it:** Use Terraform when the deployment must be repeatable code.
🏢 **Office example:** Writing a full work order for a simple desk delivery.

### ❌ D
> **D.** Use the installation guide of the CMS provider. Perform the installation through your configuration management system.

**Wrong words:**
- ❌ "**installation guide … configuration management system**": manual and slow.

📌 **When to use it:** Use it when no Marketplace option exists.
🏢 **Office example:** Building the desk from a kit.

---

## 🛒 E-Commerce Full-Stack Example

Marketplace → **WordPress (Google Click to Deploy)** → `blog.shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Quick and easy third-party install → deploy directly from Marketplace.**
  🧠 *"**Quick install? Marketplace, click Deploy.**"*
- Related: **Q137**, **Q177**.

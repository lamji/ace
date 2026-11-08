# G015: Developers Design and Deploy Apps From Approved Templates on a Visual Canvas (Application Design Center)

**Topic:** AI-assisted tooling (Application Design Center)
**Exam guide section:** 2.4 Planning and implementing resources using tooling: AI-assisted planning and implementation (Application Design Center)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your platform team wants application developers to design and deploy new applications by selecting approved, reusable architecture templates, such as Cloud Run with Cloud SQL behind a load balancer, on a visual canvas in the Google Cloud console. The designs should deploy as infrastructure as code. What should you use?
>
> **A.** Application Design Center
>
> **B.** Cloud Asset Inventory
>
> **C.** Cloud Shell Editor
>
> **D.** Cloud Billing reports

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A platform team (the people who set up shared cloud tools) wants app developers to build new apps on their own, but only from approved building blocks.
- **What you must achieve:** Let developers pick ready-made architecture templates (for example "web app + database + load balancer") on a drag-and-drop canvas in the console and deploy them.
- **The limits:** The templates must be approved and reusable, and the result must deploy as infrastructure as code (resources defined in code files).
- **What they're really asking:** Which Google Cloud console tool lets you design apps visually from templates and deploy them as code?

**Clues in the question:**
- "**visual canvas**" + "**approved, reusable architecture templates**": **Application Design Center**.
- "**deploy as infrastructure as code**": its designs are backed by Terraform.

**Exam topic:** Tooling (exam guide section 2.4).

---

## 📚 Key Terms Explained

### 1. Application Design Center 🔑
- **What it is:** A Google Cloud console tool for designing application architectures on a canvas from components and shared **templates** that platform teams publish, then deploying them as Terraform-backed infrastructure. Gemini Cloud Assist can help draft designs.
- **Looks like:** Canvas: [Load balancer] → [Cloud Run] → [Cloud SQL] → Deploy
- **Not to be confused with:** Cloud Asset Inventory, which lists what already exists. It doesn't design anything.
- **Analogy:** 🏠 A home builder's catalog of approved floor plans you customise and order.
- **In the online store:** Developers create the `gift-cards` app from the "web + SQL" template.

### 2. Architecture template
- **What it is:** A pre-approved pattern of connected resources with sensible defaults.
- **Looks like:** "Serverless web app": HTTPS LB + Cloud Run + Cloud SQL + Secret Manager
- **Not to be confused with:** A single VM image.
- **Analogy:** 📐 A standard office layout plan.
- **In the online store:** The platform team publishes `shopnow-web-template`.

### 🔗 How they fit together
```
 Platform team publishes templates ─► Application Design Center canvas
 Developer drags template, edits ─► deploy (Terraform under the hood) ✅
```

---

## 🌍 Real-World Scenario

Developers kept asking the platform team for the same "Cloud Run + database" setup. The team publishes that pattern as a template in **Application Design Center**, and developers now create and deploy new services themselves, within approved guardrails.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Application Design Center

**Why it's correct:**
- ✔️ "**Application Design Center**" matches "**visual canvas in the Google Cloud console**".
- ✔️ It uses templates from the platform team, matching "**approved, reusable architecture templates**".
- ✔️ It deploys Terraform-based infrastructure, matching "**deploy as infrastructure as code**".

📌 **When to use it:** Use it when teams should build new systems by picking from approved designs on a drawing board.
🏢 **Office example:** Choosing from the builder's approved floor plans instead of designing a house from nothing.

### ❌ B
> **B.** Cloud Asset Inventory

**Wrong words:**
- ❌ "**Cloud Asset Inventory**": an inventory and search of existing resources. It doesn't design or deploy apps.

📌 **When to use it:** Use it to find and list everything that already exists.
🏢 **Office example:** The office's furniture inventory list.

### ❌ C
> **C.** Cloud Shell Editor

**Wrong words:**
- ❌ "**Cloud Shell Editor**": a code editor in the browser, with no visual architecture canvas or template catalog.

📌 **When to use it:** Use it to edit files and run commands quickly in the browser.
🏢 **Office example:** A notepad, not a design studio.

### ❌ D
> **D.** Cloud Billing reports

**Wrong words:**
- ❌ "**Cloud Billing reports**": shows spending. It doesn't design or deploy anything.

📌 **When to use it:** Use it to see what you're spending and where.
🏢 **Office example:** The accounts department's monthly statement.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: template `serverless-web` (LB + Cloud Run + Cloud SQL). The loyalty team designs `loyalty-api` from it and deploys it to the dev folder.

---

## 🧠 Key Takeaways / Memory Tips

- **Visual app design from approved templates, deployed as code → Application Design Center.**
  🧠 *"**Design Center = drawing board for cloud apps.**"*
- Related: **G014**, **G016**.

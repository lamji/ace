# G034: Project Hits the GPU Quota in a Region: Check Usage and Request an Increase (Cloud Quotas)

**Topic:** Quotas (assess and request increases)
**Exam guide section:** 1.1 Setting up cloud projects: Assessing quotas and requesting increases

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your team cannot create more VMs with NVIDIA L4 GPUs in us-central1 because a quota error says the regional GPU limit has been reached. You need more GPUs for a planned training run next week. What should you do?
>
> **A.** Create a new billing account, because quotas are reset for each billing account.
>
> **B.** Delete and recreate the project to reset its quotas.
>
> **C.** On the Quotas & System Limits page in the Google Cloud console, find the L4 GPU quota for us-central1, review current usage, and submit a quota increase request.
>
> **D.** Add the Owner role to your account so that quota limits no longer apply.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team can't create more VMs with L4 GPUs (graphics chips for AI) in the us-central1 region. The error says a quota (a limit on how much of a resource a project may use) has been reached.
- **What you must achieve:** Get permission to use more GPUs in time for next week.
- **The limits:** Fix it properly, without hacks that break the project.
- **What they're really asking:** Where do you check a quota and ask Google to raise it?

**Clues in the question:**
- "**quota error**" + "**need more**": review usage and **request a quota increase**.
- Quotas are per project, per region (for regional resources). They're managed on the **Quotas & System Limits** page (Cloud Quotas).

**Exam topic:** Project setup (exam guide section 1.1).

---

## 📚 Key Terms Explained

### 1. Quota 🔑
- **What it is:** A limit on how much of a resource a project can use, for example GPUs per region or API requests per minute. Many can be increased on request. They protect you and Google from runaway usage.
- **Looks like:** `NVIDIA_L4_GPUS` in us-central1: 8 of 8 used
- **Not to be confused with:** A budget, which is about money, not resource counts.
- **Analogy:** 🎫 The number of parking spaces your office is allowed in the garage.
- **In the online store:** GPU quota for ShopNow's training project.

### 2. Quota increase request
- **What it is:** A request (console or Cloud Quotas API) to raise a quota value. Google reviews it, and some are approved automatically.
- **Looks like:** Console → IAM & Admin → Quotas & System Limits → filter "L4" → Edit → new value 32 → justification
- **Not to be confused with:** A billing change.
- **Analogy:** 📝 Asking building management for more parking spaces.
- **In the online store:** Requested 32 L4 GPUs for next week.

### 🔗 How they fit together
```
 Quota error ─► Quotas & System Limits ─► L4 GPUs us-central1 (8/8) ─► request 32 ✅ (plan ahead)
```

---

## 🌍 Real-World Scenario

A data team plans a big model-training run. They hit the GPU quota during tests, file a **quota increase request** with a short business justification a week ahead, and it's approved before the run.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a new billing account, because quotas are reset for each billing account.

**Wrong words:**
- ❌ "**quotas are reset for each billing account**": quotas belong to projects (and regions), not billing accounts.

📌 **When to use it:** Use new billing accounts for separate payment or invoicing.
🏢 **Office example:** Opening a new bank account to get more parking spaces.

### ❌ B
> **B.** Delete and recreate the project to reset its quotas.

**Wrong words:**
- ❌ "**Delete and recreate the project**": destroys everything, and new projects get default (often lower) quotas.

📌 **When to use it:** Never do this to get around a quota.
🏢 **Office example:** Demolishing the office to get more parking.

### ✅ C
> **C.** On the Quotas & System Limits page in the Google Cloud console, find the L4 GPU quota for us-central1, review current usage, and submit a quota increase request.

**Why it's correct:**
- ✔️ "**Quotas & System Limits page … find the L4 GPU quota for us-central1**" matches "**regional GPU limit has been reached**".
- ✔️ "**review current usage, and submit a quota increase request**" matches "**need more GPUs for a planned training run next week**".

📌 **When to use it:** Use it when your project runs into a resource limit and you need it raised ahead of time.
🏢 **Office example:** Asking building management for more parking spaces before the big event.

### ❌ D
> **D.** Add the Owner role to your account so that quota limits no longer apply.

**Wrong words:**
- ❌ "**Owner role … quota limits no longer apply**": false. Quotas apply no matter what role you have.

📌 **When to use it:** Never grant Owner for this.
🏢 **Office example:** A master key doesn't create more parking spaces.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** project `shop-ml`: request `NVIDIA_L4_GPUS` us-central1 from 8 to 32, a week before the holiday-recommendation training run.

---

## 🧠 Key Takeaways / Memory Tips

- **Quota error → check Quotas & System Limits → request an increase (per project / per region). Plan ahead.**
  🧠 *"**Quota = parking spaces; ask management for more.**"*
- Related: **G035**, **G036**.

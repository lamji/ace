# Q115: Turn Off Everything in a Project in the Fewest Steps (Project Owner + Shut Down)

**Topic:** Resource Manager (shutting down projects, Project Owner)

## ❓ Question
> You need to reduce GCP service costs for a division of your company using the fewest possible steps. You need to turn off all configured services in an existing GCP project. What should you do?
>
> **A.** 1. Verify that you are assigned the Project Owners IAM role for this project. 2. Locate the project in the GCP console, click Shut down and then enter the project ID.
>
> **B.** 1. Verify that you are assigned the Project Owners IAM role for this project. 2. Switch to the project in the GCP console, locate the resources and delete them.
>
> **C.** 1. Verify that you are assigned the Organizational Administrator IAM role for this project. 2. Locate the project in the GCP console, enter the project ID and then click Shut down.
>
> **D.** 1. Verify that you are assigned the Organizational Administrators IAM role for this project. 2. Switch to the project in the GCP console, locate the resources and delete them.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Stop **everything** in one project, in as **few steps** as possible.

**Clues in the question:**
- "**turn off all configured services**" + "**fewest possible steps**": **shut down the project**. One action stops all of it.
- Shutting down a project needs the **Project Owner** role (`resourcemanager.projects.delete`).
- In the console you click **Shut down**, then type the project ID to confirm.

**Exam topic:** Resource management / Billing.

---

## 📚 Key Terms Explained

### 1. Shut down (delete) a project 🔑
- **What it is:** Marks the project for deletion. **All billing and traffic stop right away**, resources are turned off, and after **30 days** it's permanently deleted. You can restore it within those 30 days.
- **Looks like:** `gcloud projects delete old-division-proj` · Console → IAM & Admin → Settings → **Shut down** → type the project ID
- **Not to be confused with:** deleting resources one by one.
- **Analogy:** 🏢 **Closing an entire branch office** in one decision, with a 30-day grace period.
- **In the online store:** Closing the old `shopnow-legacy` project.

### 2. Project Owner
- **What it is:** The basic role with full control of a project, including **shutting it down**.
- **Looks like:** `roles/owner`
- **Not to be confused with:** Organization Administrator, which manages org-level IAM.
- **Analogy:** 🔑 The branch manager.
- **In the online store:** Only owners can close a project.

### 3. Organization Administrator
- **What it is:** A role to manage **IAM for the whole organization**. It doesn't by itself include deleting projects.
- **Looks like:** `roles/resourcemanager.organizationAdmin`
- **Not to be confused with:** Project Owner.
- **Analogy:** 🏢 HQ's access manager.
- **In the online store:** Sets org-wide policies.

### 🔗 How they fit together
```
 Project Owner → Console → Shut down → type project ID ✅
   → billing stops now, everything off, deleted after 30 days (restorable before)
 vs. delete every VM, bucket, DB, LB… one by one ❌ (many steps)
```

---

## 🌍 Real-World Scenario

A division ends a pilot and wants zero cloud costs. The project owner opens **IAM & Admin → Settings → Shut down**, types the project ID, and every resource stops billing right away.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** 1. Verify that you are assigned the Project Owners IAM role for this project. 2. Locate the project in the GCP console, click Shut down and then enter the project ID.

**Why it's correct:**
- ✔️ "**Verify that you are assigned the Project Owners IAM role**" matches "**an existing GCP project**": owners can shut a project down.
- ✔️ "**click Shut down and then enter the project ID**" matches "**turn off all configured services**": everything in the project stops at once.
- ✔️ "**Shut down**" matches "**fewest possible steps**": one action instead of deleting each resource.

📌 **When to use it:** Use it when you want to close down an entire area and stop all its costs at once.
🏢 **Office example:** The branch manager closes the whole branch office in one decision.

### ❌ B
> **B.** 1. Verify that you are assigned the Project Owners IAM role for this project. 2. Switch to the project in the GCP console, locate the resources and delete them.

**Wrong words:**
- ✔️ "Project Owners IAM role" is right.
- ❌ "**locate the resources and delete them**": many steps, and it's easy to miss something that keeps costing money.

📌 **When to use it:** Use it when you want to keep the project but remove certain resources.
🏢 **Office example:** Clearing each desk one by one instead of closing the branch.

### ❌ C
> **C.** 1. Verify that you are assigned the Organizational Administrator IAM role for this project. 2. Locate the project in the GCP console, enter the project ID and then click Shut down.

**Wrong words:**
- ❌ "**Organizational Administrator IAM role**": it manages org IAM, and doesn't by itself let you shut down projects.
- ✔️ "Shut down" is the right action.

📌 **When to use it:** Use Organization Administrator for managing who has access across the whole organization.
🏢 **Office example:** HQ's access manager trying to close a branch, which is the branch manager's call.

### ❌ D
> **D.** 1. Verify that you are assigned the Organizational Administrators IAM role for this project. 2. Switch to the project in the GCP console, locate the resources and delete them.

**Wrong words:**
- ❌ "**Organizational Administrators IAM role**": wrong role (see C).
- ❌ "**locate the resources and delete them**": too many steps (see B).

📌 **When to use it:** **Never use this.** Use A.
🏢 **Office example:** The wrong person clearing desks one by one.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's old marketing pilot lives in `shopnow-promo-2025`.
```bash
gcloud projects delete shopnow-promo-2025   # same as console "Shut down"
```
All VMs, buckets and load balancers stop billing right away. If someone needs a file back, `gcloud projects undelete shopnow-promo-2025` works within 30 days.

---

## 🧠 Key Takeaways / Memory Tips

- **Turn off everything in a project → shut it down (Project Owner).** 30 days to restore.
- Deleting resources one by one = many steps.
  🧠 *"**Close the whole branch: Owner clicks Shut down.**"*
- Related: **Q088** (budget alerts), **Q066** (billing accounts).

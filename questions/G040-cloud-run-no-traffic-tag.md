# G040: Deploy a New Cloud Run Revision for Testing With Zero User Traffic and Its Own URL (--no-traffic --tag)

**Topic:** Cloud Run (revisions and tags)
**Exam guide section:** 3.1 Deploying new versions of a Cloud Run application; Adjusting application traffic splitting parameters

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You want to deploy a new revision of your Cloud Run service so that QA can test it at a dedicated URL, while 100% of users continue to be served by the current revision. What should you do?
>
> **A.** Deploy the new revision normally, and immediately roll back if QA finds problems.
>
> **B.** Deploy the new revision with gcloud run deploy using the --no-traffic and --tag=qa flags, and give QA the tagged revision URL.
>
> **C.** Create a new Cloud Run service with a different name for every test.
>
> **D.** Split traffic 50/50 between the current and new revisions.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You have a live Cloud Run service (Google's serverless container service). Each deploy creates a new revision (a saved version).
- **What you must achieve:** Let QA testers try the new version at its own web address.
- **The limits:** Real users must keep getting 100% of their traffic from the current version.
- **What they're really asking:** How do you deploy a version that gets no user traffic but still has its own test URL?

**Clues in the question:**
- "**100% of users continue to be served by the current revision**": deploy with **`--no-traffic`**.
- "**dedicated URL**": a revision **tag** creates a URL like `https://qa---service-xyz.run.app`.

**Exam topic:** Cloud Run operations (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. Revision
- **What it is:** An immutable snapshot of a Cloud Run service's code and settings, created on each deploy.
- **Looks like:** `orders-api-00042-abc`
- **Not to be confused with:** A separate service.
- **Analogy:** 📄 A numbered version of a document.
- **In the online store:** Each orders-api release.

### 2. Revision tag 🔑
- **What it is:** A name attached to a revision that gives it its own URL, even when it gets 0% of normal traffic.
- **Looks like:** `gcloud run deploy orders-api --image=…:v43 --no-traffic --tag=qa` → `https://qa---orders-api-xyz-uc.a.run.app`
- **Not to be confused with:** Traffic splitting, which sends a share of real users.
- **Analogy:** 🔖 A sticky tab on a draft so reviewers can find it.
- **In the online store:** QA tests v43 before any customer sees it.

### 🔗 How they fit together
```
 users ─100%─► revision 42 (current)
 QA ─► https://qa---orders-api… ─► revision 43 (0% traffic, tag qa) ✅
```

---

## 🌍 Real-World Scenario

A store's QA team needs to test checkout changes against production settings. The engineer deploys with `--no-traffic --tag=qa`. QA tests at the tagged URL, and once approved, traffic is shifted gradually.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Deploy the new revision normally, and immediately roll back if QA finds problems.

**Wrong words:**
- ❌ "**Deploy … normally**": the new revision gets 100% of users immediately, which breaks "**100% of users continue to be served by the current revision**".

📌 **When to use it:** Use a normal deploy for low-risk changes when you trust your tests.
🏢 **Office example:** Publishing the draft and pulling it back if someone complains.

### ✅ B
> **B.** Deploy the new revision with gcloud run deploy using the --no-traffic and --tag=qa flags, and give QA the tagged revision URL.

**Why it's correct:**
- ✔️ "**--no-traffic**" matches "**100% of users continue to be served by the current revision**".
- ✔️ "**--tag=qa**" plus "**tagged revision URL**" matches "**test it at a dedicated URL**".

📌 **When to use it:** Use it when testers need to try a new version before any customer sees it.
🏢 **Office example:** Putting a draft in the review tray with a tab, while the official version stays on the noticeboard.

### ❌ C
> **C.** Create a new Cloud Run service with a different name for every test.

**Wrong words:**
- ❌ "**new Cloud Run service … for every test**": different settings and URL, more clutter, and it doesn't test the real service's revisions.

📌 **When to use it:** Use separate services for truly separate apps.
🏢 **Office example:** Opening a new branch office to test a form.

### ❌ D
> **D.** Split traffic 50/50 between the current and new revisions.

**Wrong words:**
- ❌ "**50/50**": half of real users get the untested version.

📌 **When to use it:** Use small percentage splits for gradual rollouts after testing.
🏢 **Office example:** Giving half the customers the draft.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: `gcloud run deploy orders-api --image=…:v43 --no-traffic --tag=qa` → QA tests → `gcloud run services update-traffic orders-api --to-tags=qa=10` → then 100%.

---

## 🧠 Key Takeaways / Memory Tips

- **Test a new Cloud Run revision with 0 user traffic and its own URL → `--no-traffic --tag=NAME`.**
  🧠 *"**No traffic, but a tag to find it.**"*
- Related: **Q166**, **Q253**, **Q255**.

# Q333: Ensure All Resources Use EEA Locations (Resource Locations Constraint at Org Level With Allowed Locations)

**Topic:** Organization Policy (resource locations)

## ❓ Question
> Your company is active in the European Economic Area (EEA), and will adopt Google Cloud for its workloads. Projects are currently structured within different folders. You need to ensure any resources that will be deployed are using Google Cloud locations within the EEA by using the Organization Policy Service resource locations constraint. What should you do?
>
> **A.** Configure the policy at the folder level, and add all allowed locations to the policy.
>
> **B.** Configure the policy at the organization level, and add all allowed locations to the policy.
>
> **C.** Configure the policy at the folder level, and add all disallowed locations to the policy.
>
> **D.** Configure the policy at the organization level, and add all disallowed locations to the policy.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** All resources in the **EEA**; projects are in many folders.

**Clues in the question:**
- "**any resources**" across folders → set at the **organization** level (inherits everywhere).
- Use an **allowed** list (allowlist) of EEA locations; a deny list could miss new regions.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. gcp.resourceLocations 🔑
- **What it is:** Org policy constraint listing where resources may be created.
- **Looks like:** `allowedValues: [in:eu-locations]`
- **Not to be confused with:** folder-level only.
- **Analogy:** 🗺️ HQ rule: offices only in these countries.
- **In the online store:** ShopNow EU org.

### 🔗 How they fit together
```
 Org (allowed: in:eu-locations) → all folders → all projects ✅
```

---

## 🌍 Real-World Scenario

A company in the EEA sets `gcp.resourceLocations` at the **org** with **allowed** EU locations.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure the policy at the folder level, and add all allowed locations to the policy.

**Wrong words:**
- ❌ "**folder level**": must repeat per folder; new folders could be missed.

📌 **When to use it:** Use folder level when only some folders need it.
🏢 **Office example:** Posting the rule in some departments only.

### ✅ B
> **B.** Configure the policy at the organization level, and add all allowed locations to the policy.

**Why it's correct:**
- ✔️ "**organization level**" matches "**any resources that will be deployed**" across "**different folders**".
- ✔️ "**add all allowed locations**" matches "**using Google Cloud locations within the EEA**".

📌 **When to use it:** Use it when the whole company must keep everything inside certain countries.
🏢 **Office example:** An HQ rule: every branch may only rent space in these countries.

### ❌ C
> **C.** Configure the policy at the folder level, and add all disallowed locations to the policy.

**Wrong words:**
- ❌ "**folder level**" and ❌ "**disallowed locations**": misses folders and new regions.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** A list of banned countries in some departments.

### ❌ D
> **D.** Configure the policy at the organization level, and add all disallowed locations to the policy.

**Wrong words:**
- ✔️ Org level is right.
- ❌ "**disallowed locations**": any new non-EEA region would be allowed by default.

📌 **When to use it:** Use deny lists to block a few specific places.
🏢 **Office example:** A banned list that needs updating every time a new country opens.

---

## 🛒 E-Commerce Full-Stack Example

Org policy `gcp.resourceLocations` allowed `in:eu-locations` on `organizations/shopnow-eu`.

---

## 🧠 Key Takeaways / Memory Tips

- **Company-wide location rule → org level + allowed list.**
  🧠 *"**Top level, allow list.**"*
- Related: **Q364**, **Q350**.

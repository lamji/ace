# Q204: Dev Teams May Only Create Resources in the US (Folder + Organization Policy on Locations)

**Topic:** Organization Policy (resource locations constraint)

## ❓ Question
> All development (dev) teams in your organization are located in the United States. Each dev team has its own Google Cloud project. You want to restrict access so that each dev team can only create cloud resources in the United States (US). What should you do?
>
> **A.** Create a folder to contain all the dev projects. Create an organization policy to limit resources in US locations.
>
> **B.** Create an organization to contain all the dev projects. Create an Identity and Access Management (IAM) policy to limit the resources in US regions.
>
> **C.** Create an Identity and Access Management (IAM) policy to restrict the resources locations in the US. Apply the policy to all dev projects.
>
> **D.** Create an Identity and Access Management (IAM) policy to restrict the resources locations in all dev projects. Apply the policy to all dev roles.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** All dev teams are in the United States, and each has its own project.
- **What you must achieve:** Each team may create resources only in the US.
- **The limits:** None stated.
- **What they're really asking:** How do you limit where resources can be created?

**Clues in the question:**
- "**only create cloud resources in the United States**" → limit **where** resources go → **Organization Policy** `gcp.resourceLocations`.
- IAM controls **who** can do things, not **where**.
- A **folder** groups the dev projects so the policy applies once.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. Organization Policy 🔑
- **What it is:** Rules on **what** can be done with resources (allowed locations, no external IPs…). Set on org, folder or project and inherited.
- **Looks like:** constraint `gcp.resourceLocations` = `in:us-locations`
- **Not to be confused with:** IAM (who).
- **Analogy:** 📜 Company rule: "all offices must be in the US."
- **In the online store:** Keep data in the US.

### 2. IAM policy
- **What it is:** Who has which role on a resource.
- **Looks like:** `group:dev@ → roles/editor`
- **Not to be confused with:** org policy.
- **Analogy:** 🔑 Who holds which keys.
- **In the online store:** —

### 🔗 How they fit together
```
 Org
  └─ Folder Dev [org policy: resourceLocations = in:us-locations] ✅
       ├─ dev-team-a
       └─ dev-team-b
```

---

## 🌍 Real-World Scenario

Compliance requires dev resources to stay in the US. The admin puts all dev projects in a **Dev folder** and sets the **resource locations** org policy on it.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a folder to contain all the dev projects. Create an organization policy to limit resources in US locations.

**Why it's correct:**
- ✔️ "**Create a folder to contain all the dev projects**" matches "**Each dev team has its own Google Cloud project**": one place to apply the rule.
- ✔️ "**organization policy to limit resources in US locations**" matches "**only create cloud resources in the United States**".

📌 **When to use it:** Use it when a whole group of teams must follow the same company rule.
🏢 **Office example:** Putting all dev offices in one division and posting the rule "US offices only" for that division.

### ❌ B
> **B.** Create an organization to contain all the dev projects. Create an Identity and Access Management (IAM) policy to limit the resources in US regions.

**Wrong words:**
- ❌ "**Create an organization**": you already have one, and orgs come from your domain.
- ❌ "**IAM policy to limit the resources in US regions**": IAM can't restrict locations.

📌 **When to use it:** Use IAM to grant roles.
🏢 **Office example:** Handing out keys to enforce where offices are built.

### ❌ C
> **C.** Create an Identity and Access Management (IAM) policy to restrict the resources locations in the US. Apply the policy to all dev projects.

**Wrong words:**
- ❌ "**IAM policy to restrict the resources locations**": IAM doesn't do locations.

📌 **When to use it:** Use IAM for who-can-do-what.
🏢 **Office example:** Using the key list as a building code.

### ❌ D
> **D.** Create an Identity and Access Management (IAM) policy to restrict the resources locations in all dev projects. Apply the policy to all dev roles.

**Wrong words:**
- ❌ "**IAM policy … Apply the policy to all dev roles**": wrong tool, and policies aren't applied to roles.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Attaching rules to job titles instead of locations.

---

## 🛒 E-Commerce Full-Stack Example

Folder `ShopNow-Dev` → `gcloud resource-manager org-policies allow gcp.resourceLocations in:us-locations --folder=DEV_FOLDER_ID`

---

## 🧠 Key Takeaways / Memory Tips

- **Where resources may live → Organization Policy (resourceLocations).** IAM = who.
  🧠 *"**IAM = who. Org policy = what/where.**"*
- Related: **Q194**, **Q220**.

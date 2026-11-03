# Q350: Isolated Data Science Area: us-east1 Only, Only BigQuery and Cloud Storage, Full Admin (Folder + Org Policy Locations & Services + Owner)

**Topic:** Organization Policy / IAM

## ❓ Question
> You are creating an isolated Google Cloud environment for a new data science team. The team needs to experiment with machine learning models in short-lived projects and requires full administrative access. All team members belong to the same group. Your solution must restrict resource creation to the us-east1 region and only allow the use of BigQuery and Cloud Storage. What should you do?
>
> **A.** Create a new folder. Create an organization policy with constraints to restrict resource locations and allowed services, and apply it to the folder. Grant the Owner IAM role to the group at the folder level.
>
> **B.** Create a new folder. Create an organization policy with constraints to restrict resource locations and allowed services, and apply it to the folder. Grant the BigQuery Admin and Storage Admin IAM roles to the group at the folder level.
>
> **C.** Create a new folder. Create an organization policy with constraints to restrict resource locations, and apply it to the folder. Grant the Owner IAM role to the group at the folder level.
>
> **D.** Create a new folder. Create an organization policy with constraints to restrict resource locations, and apply it to the folder. Grant the BigQuery Admin and Storage Admin IAM roles to the group at the folder level.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Team needs **full admin**, but only in **us-east1** and only **BigQuery + Cloud Storage**.

**Clues in the question:**
- "**restrict … us-east1**" → resource locations constraint.
- "**only allow … BigQuery and Cloud Storage**" → restrict allowed services (`gcp.restrictServiceUsage`).
- "**full administrative access**" → **Owner** on the folder; guardrails limit what Owner can do.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. gcp.restrictServiceUsage 🔑
- **What it is:** Org policy constraint listing which Google Cloud services may be used.
- **Looks like:** `allowedValues: [bigquery.googleapis.com, storage.googleapis.com]`
- **Not to be confused with:** IAM roles (who), not which services exist.
- **Analogy:** 🚧 Building rules on which rooms exist.
- **In the online store:** —

### 🔗 How they fit together
```
 folder ds/ ── org policy: locations=us-east1, services=BQ+GCS
           └─ group ds@ → Owner ✅
```

---

## 🌍 Real-World Scenario

A data science folder has org policies for **us-east1** and **BigQuery + Cloud Storage only**; the team is **Owner** inside it.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a new folder. Create an organization policy with constraints to restrict resource locations and allowed services, and apply it to the folder. Grant the Owner IAM role to the group at the folder level.

**Why it's correct:**
- ✔️ "**restrict resource locations and allowed services … apply it to the folder**" matches "**restrict resource creation to the us-east1 region and only allow the use of BigQuery and Cloud Storage**".
- ✔️ "**Owner IAM role to the group at the folder level**" matches "**requires full administrative access**" + "**All team members belong to the same group**".

📌 **When to use it:** Use it when a team can do anything they want, but only inside clear company limits.
🏢 **Office example:** A team gets full keys to their floor, but building rules say which rooms and which city.

### ❌ B
> **B.** Create a new folder. Create an organization policy with constraints to restrict resource locations and allowed services, and apply it to the folder. Grant the BigQuery Admin and Storage Admin IAM roles to the group at the folder level.

**Wrong words:**
- ✔️ Org policy is right.
- ❌ "**BigQuery Admin and Storage Admin**": not full admin (can't create projects or manage IAM).

📌 **When to use it:** Use service admin roles when full admin isn't needed.
🏢 **Office example:** Keys to two rooms, not the floor.

### ❌ C
> **C.** Create a new folder. Create an organization policy with constraints to restrict resource locations, and apply it to the folder. Grant the Owner IAM role to the group at the folder level.

**Wrong words:**
- ✔️ Owner is right.
- ❌ Only locations restricted; other services are still allowed.

📌 **When to use it:** Use it when any service is fine in one region.
🏢 **Office example:** Full keys and a city rule, but any room.

### ❌ D
> **D.** Create a new folder. Create an organization policy with constraints to restrict resource locations, and apply it to the folder. Grant the BigQuery Admin and Storage Admin IAM roles to the group at the folder level.

**Wrong words:**
- ❌ No services restriction and ❌ not full admin.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Missing both rules.

---

## 🛒 E-Commerce Full-Stack Example

Folder `ds-sandbox` with locations `in:us-east1-locations`, services BQ + GCS; `group:ds@shopnow.com` → Owner.

---

## 🧠 Key Takeaways / Memory Tips

- **Guardrails by org policy (where, which services); power by IAM (Owner).**
  🧠 *"**Policies fence, roles empower.**"*
- Related: **Q333**, **Q364**.

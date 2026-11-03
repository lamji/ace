# Q261: Give SREs the Same Permissions in an Acquired Startup's Organization (gcloud iam roles copy to the Startup's Org ID)

**Topic:** IAM (copying custom roles)

## ❓ Question
> You are in charge of provisioning access for all Google Cloud users in your organization. Your company recently acquired a startup company that has their own Google Cloud organization. You need to ensure that your Site Reliability Engineers (SREs) have the same project permissions in the startup company's organization as in your own organization. What should you do?
>
> **A.** In the Google Cloud console for your organization, select Create role from selection, and choose destination as the startup company's organization.
>
> **B.** In the Google Cloud console for the startup company, select Create role from selection and choose source as the startup company's Google Cloud organization.
>
> **C.** Use the gcloud iam roles copy command, and provide the Organization ID of the startup company's Google Cloud Organization as the destination.
>
> **D.** Use the gcloud iam roles copy command, and provide the project IDs of all projects in the startup company's organization as the destination.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Copy your SRE custom role into **another organization**.

**Clues in the question:**
- "**same project permissions in the startup company's organization**" → `gcloud iam roles copy` with **`--dest-organization`** = the startup's org ID; then it's usable on all their projects.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. gcloud iam roles copy 🔑
- **What it is:** Copies a custom (or predefined) role to another project or organization.
- **Looks like:** `gcloud iam roles copy --source=organizations/111/roles/sre --destination=sre --dest-organization=222`
- **Not to be confused with:** granting a role.
- **Analogy:** 📄 Photocopying a job description to the new branch.
- **In the online store:** SRE role in acquired org.

### 🔗 How they fit together
```
 org 111: custom role sre ── roles copy ──► org 222 (startup): role sre ✅ → grant to SREs
```

---

## 🌍 Real-World Scenario

After an acquisition, the admin copies the **SRE custom role** into the startup's organization with `gcloud iam roles copy --dest-organization`, then grants it to the SRE group there.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In the Google Cloud console for your organization, select Create role from selection, and choose destination as the startup company's organization.

**Wrong words:**
- ❌ "**Create role from selection, and choose destination as the startup company's organization**": the console's Create-from-selection makes a role in the current org/project; it can't target another org.

📌 **When to use it:** Use Create role from selection to start a role from existing ones in the same place.
🏢 **Office example:** Copying a form into your own drawer, not the other branch's.

### ❌ B
> **B.** In the Google Cloud console for the startup company, select Create role from selection and choose source as the startup company's Google Cloud organization.

**Wrong words:**
- ❌ "**choose source as the startup company's … organization**": wrong direction; your SRE role lives in your org.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Copying the new branch's form back into itself.

### ✅ C
> **C.** Use the gcloud iam roles copy command, and provide the Organization ID of the startup company's Google Cloud Organization as the destination.

**Why it's correct:**
- ✔️ "**gcloud iam roles copy**" matches "**the same project permissions**": the role definition is copied exactly.
- ✔️ "**Organization ID of the startup company's … Organization as the destination**": one copy usable on every project in that org.

📌 **When to use it:** Use it when a job role defined in one company area must exist in another.
🏢 **Office example:** Photocopying the official job description to the new branch's HR office so it applies to all their departments.

### ❌ D
> **D.** Use the gcloud iam roles copy command, and provide the project IDs of all projects in the startup company's organization as the destination.

**Wrong words:**
- ❌ "**project IDs of all projects … as the destination**": a copy per project — more work and new projects are missed.

📌 **When to use it:** Use project-level copies when only one project needs it.
🏢 **Office example:** Photocopying the form for every single desk.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud iam roles copy --source=organizations/SHOPNOW_ORG/roles/shopSRE --destination=shopSRE --dest-organization=STARTUP_ORG`

---

## 🧠 Key Takeaways / Memory Tips

- **Same custom role in another org → `gcloud iam roles copy --dest-organization`.**
  🧠 *"**Copy the role to the org, not to each project.**"*
- Related: **Q215**, **Q203**.

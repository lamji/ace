# Q190: Marketing Needs Similar Resources Organized Separately From Sales (New Project acme-marketing-data-digest)

**Topic:** Resource hierarchy (projects, project IDs)

## ❓ Question
> The sales team has a project named Sales Data Digest that has the ID acme-data-digest. You need to set up similar Google Cloud resources for the marketing team but their resources must be organized independently of the sales team. What should you do?
>
> **A.** Grant the Project Editor role to the Marketing team for acme-data-digest.
>
> **B.** Create a Project Lien on acme-data-digest and then grant the Project Editor role to the Marketing team.
>
> **C.** Create another project with the ID acme-marketing-data-digest for the Marketing team and deploy the resources there.
>
> **D.** Create a new project named Marketing Data Digest and use the ID acme-data-digest. Grant the Project Editor role to the Marketing team.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The sales team has a project named Sales Data Digest (ID acme-data-digest).
- **What you must achieve:** Set up similar resources for the marketing team.
- **The limits:** Marketing's resources must be organized separately from sales.
- **What they're really asking:** How do you create marketing's environment?

**Clues in the question:**
- "**organized independently of the sales team**" → a **new project**.
- Project IDs are **globally unique**, so you can't reuse `acme-data-digest`.

**Exam topic:** Resource hierarchy.

---

## 📚 Key Terms Explained

### 1. Project ID 🔑
- **What it is:** A **globally unique**, permanent ID for a project. The name can repeat; the ID can't.
- **Looks like:** name "Marketing Data Digest", ID `acme-marketing-data-digest`
- **Not to be confused with:** project name.
- **Analogy:** 🔢 A unique account number vs a display name.
- **In the online store:** shopnow-prod, shopnow-dev.

### 2. Project lien
- **What it is:** A lock that stops a project from being **deleted**.
- **Looks like:** `gcloud alpha resource-manager liens create --restrictions=resourcemanager.projects.delete`
- **Not to be confused with:** access control.
- **Analogy:** 🔒 A "do not demolish" sign.
- **In the online store:** Protect prod project.

### 🔗 How they fit together
```
 acme-data-digest (Sales)    acme-marketing-data-digest (Marketing) ✅ separate
```

---

## 🌍 Real-World Scenario

Marketing wants the same reporting setup as Sales. The admin creates **acme-marketing-data-digest** and deploys a copy of the resources there, with separate IAM and billing reports.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant the Project Editor role to the Marketing team for acme-data-digest.

**Wrong words:**
- ❌ "**Project Editor … for acme-data-digest**": marketing would work inside Sales' project, not separately.

📌 **When to use it:** Use it when someone should help on that same project.
🏢 **Office example:** Moving marketing into the sales office.

### ❌ B
> **B.** Create a Project Lien on acme-data-digest and then grant the Project Editor role to the Marketing team.

**Wrong words:**
- ❌ "**Project Lien**": only prevents deletion. Marketing still shares Sales' project.

📌 **When to use it:** Use a lien to protect an important project from deletion.
🏢 **Office example:** A "do not demolish" sign on a shared office.

### ✅ C
> **C.** Create another project with the ID acme-marketing-data-digest for the Marketing team and deploy the resources there.

**Why it's correct:**
- ✔️ "**Create another project**" matches "**organized independently of the sales team**".
- ✔️ "**ID acme-marketing-data-digest**" is a new, unique ID.
- ✔️ "**deploy the resources there**" matches "**set up similar Google Cloud resources**".

📌 **When to use it:** Use it when a team needs its own separate space with its own setup.
🏢 **Office example:** Giving marketing its own office with its own filing cabinets, set up like the sales office.

### ❌ D
> **D.** Create a new project named Marketing Data Digest and use the ID acme-data-digest. Grant the Project Editor role to the Marketing team.

**Wrong words:**
- ✔️ "new project named Marketing Data Digest" is fine.
- ❌ "**use the ID acme-data-digest**": that ID is taken. Project IDs are globally unique.

📌 **When to use it:** **Never use this.** Pick a new unique ID.
🏢 **Office example:** Giving the new office the same account number as sales.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud projects create shopnow-marketing-analytics --name="Marketing Analytics" --folder=MARKETING_FOLDER_ID`

---

## 🧠 Key Takeaways / Memory Tips

- **Independent resources → separate project.** Project IDs are globally unique.
  🧠 *"**New team, new project, new ID.**"*
- Related: **Q140**, **Q156**.

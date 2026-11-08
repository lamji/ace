# Q362: Team-Based Access to Hundreds of Resources, Easy Join/Leave (Google Groups With Security Label)

**Topic:** IAM (Google Groups, security groups)

## ❓ Question
> You are defining a standard procedure for managing team access to hundreds of Google Cloud resources. Your organization uses Cloud Identity as its primary identity provider, and you want to base access on team membership. You need a solution that simplifies the process of granting and revoking access as individuals join and leave teams. Your solution must minimize administrative effort and follow Google-recommended security practices. What should you do?
>
> **A.** For each team, create a Google Group in Cloud Identity with the cloudidentity.googleapis.com/groups.discussion_forum group property label. Add team members to the group, and use the group in IAM policies.
>
> **B.** For each team, create a service account. Grant each team member the IAM permission to impersonate that service account.
>
> **C.** For each team, create a service account. Grant each team member the IAM permission to generate and download keys for that service account.
>
> **D.** For each team, create a Google Group in Cloud Identity with the cloudidentity.googleapis.com/groups.discussion_forum and cloudidentity.googleapis.com/groups.security group property labels. Add team members to the group, and use the group in IAM policies.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are defining how teams get access to hundreds of resources. Your identity provider is Cloud Identity, and access should follow team membership.
- **What you must achieve:** Make granting and removing access easy as people join and leave teams.
- **The limits:** Minimal admin effort and recommended security practice.
- **What they're really asking:** How should you represent teams and grant them access?

**Clues in the question:**
- Use **Google Groups** in IAM.
- "**Google-recommended security practices**" → label the group as a **security group** (`groups.security`).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Security group label 🔑
- **What it is:** A Cloud Identity group label marking the group as used for access control; enables stricter rules (e.g., limits on nesting outside groups) and auditability.
- **Looks like:** labels: `cloudidentity.googleapis.com/groups.discussion_forum` + `cloudidentity.googleapis.com/groups.security`
- **Not to be confused with:** discussion-only group.
- **Analogy:** 🏷️ A 'security list' tag on the team list.
- **In the online store:** —

### 🔗 How they fit together
```
 team group (discussion_forum + security) → IAM policies ✅
```

---

## 🌍 Real-World Scenario

Each team gets a **security-labeled Google Group**, used in IAM across hundreds of resources.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** For each team, create a Google Group in Cloud Identity with the cloudidentity.googleapis.com/groups.discussion_forum group property label. Add team members to the group, and use the group in IAM policies.

**Wrong words:**
- ✔️ Groups in IAM are right.
- ❌ Missing the "**security**" label: Google recommends security groups for access control.

📌 **When to use it:** Use plain discussion groups for mailing lists.
🏢 **Office example:** A team list without the security stamp.

### ❌ B
> **B.** For each team, create a service account. Grant each team member the IAM permission to impersonate that service account.

**Wrong words:**
- ❌ "**create a service account … impersonate**": shared identity; logs show the SA, not the person.

📌 **When to use it:** Use SAs for workloads, not teams.
🏢 **Office example:** Everyone wearing one shared badge.

### ❌ C
> **C.** For each team, create a service account. Grant each team member the IAM permission to generate and download keys for that service account.

**Wrong words:**
- ❌ "**generate and download keys**": insecure secrets.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Copying master keys for everyone.

### ✅ D
> **D.** For each team, create a Google Group in Cloud Identity with the cloudidentity.googleapis.com/groups.discussion_forum and cloudidentity.googleapis.com/groups.security group property labels. Add team members to the group, and use the group in IAM policies.

**Why it's correct:**
- ✔️ "**Google Group … Add team members … use the group in IAM policies**" matches "**base access on team membership**" + "**simplifies … as individuals join and leave**".
- ✔️ "**groups.security group property label**" matches "**follow Google-recommended security practices**".

📌 **When to use it:** Use it when access should follow which team a person is on, managed in one list.
🏢 **Office example:** A team list stamped 'security' that controls which rooms open.

---

## 🛒 E-Commerce Full-Stack Example

`sre@shopnow.com` with security label → roles across projects.

---

## 🧠 Key Takeaways / Memory Tips

- **Team access → Google Groups with the security label in IAM.**
  🧠 *"**Groups for people, security label for access.**"*
- Related: **Q294**, **Q361**.

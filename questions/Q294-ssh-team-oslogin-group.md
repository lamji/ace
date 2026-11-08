# Q294: SSH for an Engineering Team With Little Overhead When People Join or Leave (OS Login + Google Group)

**Topic:** Compute Engine (OS Login)

## ❓ Question
> You are managing a fleet of Compute Engine Linux instances in a Google Cloud project. Your company's engineering team requires SSH access to all instances to perform routine maintenance tasks. You need to manage the SSH access for the engineering team, and you want to minimize operational overhead when engineers join or leave the team. What should you do?
>
> **A.** Create a single SSH key pair to be shared by all engineering team members. Add the public SSH key to project metadata.
>
> **B.** Create an SSH key pair for each engineer on the team, and add the public SSH key to the metadata of the relevant instances.
>
> **C.** Create a Google Group for all engineering team members, and grant them the Compute Viewer IAM role. Manage group membership when engineers join or leave the team.
>
> **D.** Create a Google Group for all engineering team members, and set up OS Login for this group on the project. Manage group membership when engineers join or leave the team.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You manage many Linux VMs, and the engineering team needs SSH (command-line login) access to all of them for maintenance.
- **What you must achieve:** Give the engineering team SSH access.
- **The limits:** Adding and removing engineers when they join or leave must take very little work.
- **What they're really asking:** How do you manage SSH access for the team so joining and leaving is easy?

**Clues in the question:**
- "**minimize operational overhead when engineers join or leave**" → **OS Login** (SSH tied to IAM) + a **group** (add/remove members).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. OS Login 🔑
- **What it is:** Ties Linux SSH access to Google identities and IAM roles (`roles/compute.osLogin`/`osAdminLogin`). No keys in metadata to manage.
- **Looks like:** metadata `enable-oslogin=TRUE` + `group:eng@ → roles/compute.osAdminLogin`
- **Not to be confused with:** metadata SSH keys.
- **Analogy:** 🪪 Door opens with your staff badge; HR removes you from the list.
- **In the online store:** Ops team SSH.

### 🔗 How they fit together
```
 group eng@ → roles/compute.osAdminLogin; OS Login ON → join/leave = group membership ✅
```

---

## 🌍 Real-World Scenario

An ops team's SSH access is managed with **OS Login** and the `eng@` group. New hires join the group; leavers are removed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a single SSH key pair to be shared by all engineering team members. Add the public SSH key to project metadata.

**Wrong words:**
- ❌ "**single SSH key pair to be shared**": no individual accountability; when someone leaves you must rotate for everyone.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** One shared key for the whole team.

### ❌ B
> **B.** Create an SSH key pair for each engineer on the team, and add the public SSH key to the metadata of the relevant instances.

**Wrong words:**
- ❌ "**SSH key pair for each engineer … metadata of the relevant instances**": manual key work every time someone joins or leaves.

📌 **When to use it:** Use metadata keys for people without Google accounts.
🏢 **Office example:** Cutting and removing individual keys by hand.

### ❌ C
> **C.** Create a Google Group for all engineering team members, and grant them the Compute Viewer IAM role. Manage group membership when engineers join or leave the team.

**Wrong words:**
- ✔️ Group is right.
- ❌ "**Compute Viewer**": can view VMs, not SSH into them.

📌 **When to use it:** Use Compute Viewer for read-only visibility.
🏢 **Office example:** A visitor list that doesn't open doors.

### ✅ D
> **D.** Create a Google Group for all engineering team members, and set up OS Login for this group on the project. Manage group membership when engineers join or leave the team.

**Why it's correct:**
- ✔️ "**set up OS Login for this group**" matches "**manage the SSH access for the engineering team**".
- ✔️ "**Manage group membership when engineers join or leave**" matches "**minimize operational overhead when engineers join or leave**".

📌 **When to use it:** Use it when a team needs to log in to many machines and staff change often.
🏢 **Office example:** Doors that open with the staff badge; HR just updates the team list.

---

## 🛒 E-Commerce Full-Stack Example

Project metadata `enable-oslogin=TRUE`; `group:sre@shopnow.com` → `roles/compute.osAdminLogin`.

---

## 🧠 Key Takeaways / Memory Tips

- **Team SSH with easy join/leave → OS Login + Google Group.**
  🧠 *"**Badge, not keys.**"*
- Related: **Q302**, **Q323**, **Q191**.

# Q361: New Developer Deploys Apps to GKE, Least Privilege (Add to Group With container.developer)

**Topic:** IAM (GKE roles, groups)

## ❓ Question
> You manage Identity and Access Management (IAM) for your Google Cloud project. A new developer joined the cloud-developer team, and they need to be able to deploy containerized applications to an existing Google Kubernetes Engine (GKE) cluster. They do not need to manage other cloud resources or the GKE cluster itself. You need to grant access following the principle of least privilege. What should you do?
>
> **A.** Add the developer to the cloud-developer group that already has the container.developer IAM role.
>
> **B.** Grant the developer the container.admin IAM role for the project.
>
> **C.** Grant the developer the container.serviceAgent IAM role for the project.
>
> **D.** Grant the developer the editor IAM role for the project.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new developer joined the cloud-developer team and must deploy containerized apps to an existing GKE cluster.
- **What you must achieve:** Give them deploy access.
- **The limits:** They must not manage other resources or the cluster itself; least privilege.
- **What they're really asking:** How do you give the new developer the right access?

**Clues in the question:**
- Deploy workloads only → **`roles/container.developer`**.
- Team already has a group with it → just **add the developer to the group**.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/container.developer 🔑
- **What it is:** Full access to Kubernetes API objects (Deployments, Services) in clusters, but can't create/delete/modify clusters.
- **Looks like:** `group:cloud-developer@ → roles/container.developer`
- **Not to be confused with:** container.admin (manages clusters too).
- **Analogy:** 🧑‍🍳 Can cook in the kitchen, can't remodel it.
- **In the online store:** ShopNow devs.

### 🔗 How they fit together
```
 new dev → cloud-developer@ (container.developer) ✅
```

---

## 🌍 Real-World Scenario

A new hire is added to `cloud-developer@`, which already has **Kubernetes Engine Developer**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Add the developer to the cloud-developer group that already has the container.developer IAM role.

**Why it's correct:**
- ✔️ "**Add the developer to the cloud-developer group**" matches "**A new developer joined the cloud-developer team**".
- ✔️ "**container.developer IAM role**" matches "**deploy containerized applications to an existing … cluster**" + "**do not need to manage … the GKE cluster itself**".

📌 **When to use it:** Use it when a new person joins a team that already has the right access set up.
🏢 **Office example:** Adding the new cook to the kitchen staff list, which already opens the kitchen.

### ❌ B
> **B.** Grant the developer the container.admin IAM role for the project.

**Wrong words:**
- ❌ "**container.admin**": can manage clusters; too much.

📌 **When to use it:** Use it for cluster administrators.
🏢 **Office example:** Keys to remodel the kitchen.

### ❌ C
> **C.** Grant the developer the container.serviceAgent IAM role for the project.

**Wrong words:**
- ❌ "**container.serviceAgent**": meant for Google's GKE service agent, not people.

📌 **When to use it:** **Never grant this** to users.
🏢 **Office example:** A badge meant for the building's robots.

### ❌ D
> **D.** Grant the developer the editor IAM role for the project.

**Wrong words:**
- ❌ "**editor**": broad access to almost all resources.

📌 **When to use it:** **Avoid** basic roles.
🏢 **Office example:** A key to nearly every room.

---

## 🛒 E-Commerce Full-Stack Example

Add `newdev@shopnow.com` to `cloud-developer@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Deploy to GKE only → container.developer, via a group.**
  🧠 *"**Developers deploy; admins manage clusters.**"*
- Related: **Q294**.

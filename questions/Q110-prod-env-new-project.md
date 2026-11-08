# Q110: New Production Environment With No Network Routes to Development (Separate Project)

**Topic:** Resource hierarchy / networking (project per environment, VPC isolation, Shared VPC)

## ❓ Question
> You have successfully created a development environment in a project for an application. This application uses Compute Engine and Cloud SQL. Now you need to create a production environment for this application. The security team has forbidden the existence of network routes between these 2 environments and has asked you to follow Google-recommended practices. What should you do?
>
> **A.** Create a new project, enable the Compute Engine and Cloud SQL APIs in that project, and replicate the setup you have created in the development environment.
>
> **B.** Create a new production subnet in the existing VPC and a new production Cloud SQL instance in your existing project, and deploy your application using those resources.
>
> **C.** Create a new project, modify your existing VPC to be a Shared VPC, share that VPC with your new project, and replicate the setup you have in the development environment in that new project in the Shared VPC.
>
> **D.** Ask the security team to grant you the Project Editor role in an existing production project used by another division of your company. Once they grant you that role, replicate the setup you have in the development environment in that project.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A development environment (Compute Engine plus Cloud SQL) exists in a project.
- **What you must achieve:** Create the production environment.
- **The limits:** Security forbids any network route between the two environments; follow recommended practice.
- **What they're really asking:** How do you set up production so it is completely separate?

**Clues in the question:**
- "**forbidden the existence of network routes between these 2 environments**": prod needs its **own separate network**. A new project has its own VPC.
- "**Google-recommended practices**": **one project per environment** (dev, prod).

**Exam topic:** Resource management / networking.

---

## 📚 Key Terms Explained

### 1. Project per environment 🔑
- **What it is:** Keeping dev, test and prod in **separate projects**, each with its own IAM, billing view, quotas and networks.
- **Looks like:** `shopnow-dev`, `shopnow-prod`
- **Not to be confused with:** one project with several subnets.
- **Analogy:** 🏢 Separate **office buildings** for the training center and the real bank branch.
- **In the online store:** ShopNow's prod is fully separate from dev.

### 2. VPC routes (review from Q079, Q082)
- **What it is:** Subnets in the same VPC are connected by **automatic routes**. Separate VPCs in separate projects have **no routes** between them unless you add peering or VPN.
- **Looks like:** `default-route-...` / subnet routes
- **Not to be confused with:** firewall rules.
- **Analogy:** 🛣️ Hallways between rooms in the same building.
- **In the online store:** Dev subnets can't reach prod subnets.

### 3. Shared VPC
- **What it is:** One host project's network used by other projects. Everything in it is **one network with routes** between subnets.
- **Looks like:** `gcloud compute shared-vpc enable shopnow-dev`
- **Not to be confused with:** isolation.
- **Analogy:** 📞 One phone system for many offices.
- **In the online store:** Not used to separate dev from prod.

### 🔗 How they fit together
```
 shopnow-dev  (VPC dev-net)  ── no routes ──  shopnow-prod (VPC prod-net) ✅
   VMs + Cloud SQL                                VMs + Cloud SQL (replicated setup)
```

---

## 🌍 Real-World Scenario

A team finishes building an app in a dev project. For launch, they create `app-prod`, enable the Compute Engine and Cloud SQL APIs, and rebuild the same setup there, ideally with Terraform. The two projects have separate VPCs, so there are no routes between them.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a new project, enable the Compute Engine and Cloud SQL APIs in that project, and replicate the setup you have created in the development environment.

**Why it's correct:**
- ✔️ "**Create a new project**" matches "**follow Google-recommended practices**": one project per environment.
- ✔️ "**new project**" (own VPC) matches "**forbidden the existence of network routes between these 2 environments**": separate networks have no routes between them.
- ✔️ "**enable the Compute Engine and Cloud SQL APIs … and replicate the setup**" matches "**uses Compute Engine and Cloud SQL**": prod gets the same pieces.

📌 **When to use it:** Use it when the real thing must be completely separate from the practice version.
🏢 **Office example:** Opening the real branch in its own building, separate from the training center.

### ❌ B
> **B.** Create a new production subnet in the existing VPC and a new production Cloud SQL instance in your existing project, and deploy your application using those resources.

**Wrong words:**
- ❌ "**new production subnet in the existing VPC**": subnets in one VPC have automatic routes between them, which security forbids.
- ❌ "**in your existing project**": mixes dev and prod, against best practice.

📌 **When to use it:** Use extra subnets when the parts are allowed to talk to each other.
🏢 **Office example:** Putting the real branch in a room next to the training center, with an open hallway.

### ❌ C
> **C.** Create a new project, modify your existing VPC to be a Shared VPC, share that VPC with your new project, and replicate the setup you have in the development environment in that new project in the Shared VPC.

**Wrong words:**
- ✔️ "Create a new project" is a good start.
- ❌ "**modify your existing VPC to be a Shared VPC, share that VPC with your new project**": prod would use the **same network** as dev, with routes between them.

📌 **When to use it:** Use Shared VPC when many projects should share one network.
🏢 **Office example:** Building a new branch but plugging it into the training center's phone system.

### ❌ D
> **D.** Ask the security team to grant you the Project Editor role in an existing production project used by another division of your company. Once they grant you that role, replicate the setup you have in the development environment in that project.

**Wrong words:**
- ❌ "**existing production project used by another division**": mixes your app into another team's project.
- ❌ "**Project Editor role**": a broad basic role, not least privilege.

📌 **When to use it:** **Never use this.** Create your own prod project (A).
🏢 **Office example:** Moving into another department's office without asking.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects create shopnow-prod --folder=RETAIL_FOLDER_ID
gcloud services enable compute.googleapis.com sqladmin.googleapis.com --project=shopnow-prod
terraform apply -var project=shopnow-prod   # same setup as dev
```
`shopnow-dev` (10.10.0.0/16) and `shopnow-prod` (10.20.0.0/16) are in different VPCs with no peering, so there are no routes between them.

---

## 🧠 Key Takeaways / Memory Tips

- **Separate environments → separate projects** (each with its own VPC).
- Same VPC or Shared VPC = routes between subnets.
  🧠 *"**New environment, new project.**"*
- Related: **Q079** (Shared VPC), **Q060** (peering), **Q082** (subnets).

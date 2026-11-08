# Q079: Letting VMs in Two Projects Talk (Shared VPC)

**Topic:** VPC networking (Shared VPC, host and service projects, organization requirement, VPCs belong to one project)

## ❓ Question
> You need to enable traffic between multiple groups of Compute Engine instances that are currently running two different GCP projects. Each group of Compute Engine instances is running in its own VPC. What should you do?
>
> **A.** Verify that both projects are in a GCP Organization. Create a new VPC and add all instances.
>
> **B.** Verify that both projects are in a GCP Organization. Share the VPC from one project and request that the Compute Engine instances in the other project use this shared VPC.
>
> **C.** Verify that you are the Project Administrator of both projects. Create two new VPCs and add all instances.
>
> **D.** Verify that you are the Project Administrator of both projects. Create a new VPC and add all instances.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

> ℹ️ **Note:** In real life, **VPC Network Peering** (Q060) is another common way to connect two VPCs in different projects. It isn't offered here, so **Shared VPC** is the answer.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Groups of VMs run in two different projects, each group in its own VPC network.
- **What you must achieve:** Let the groups talk to each other.
- **The limits:** None stated.
- **What they're really asking:** How do you connect the two networks?

**Clues in the question:**
- "**two different GCP projects**": a normal VPC belongs to **one project**, so a VM in another project can't simply "join" it.
- "**enable traffic between**": the VMs need a shared private network.
- **Shared VPC** lets one project (the **host**) share its VPC with other projects (**service projects**), and it **requires an Organization**. That's why B starts with "verify … in a GCP Organization".

**Exam topic:** VPC networking.

---

## 📚 Key Terms Explained

### 1️⃣ VPC belongs to one project (review from Q050, Q054)
- **What it is:** A **VPC** (private network) is created **inside one project**. Normally only that project's VMs can use it.
- **Looks like:** `projects/shopnow-net/global/networks/shared-vpc`
- **Not to be confused with:** something any project can use. That needs Shared VPC or peering.
- **Analogy:** 🏢 A **phone system owned by one company**.
- **In the online store:** `shopnow-net` owns the main network.

### 2️⃣ Shared VPC 🔑
- **What it is:** A setup where a **host project** shares its VPC (and subnets) with **service projects**. VMs in the service projects are created **in the host's network**, so they all talk by private IP. Requires an **Organization**.
- **Looks like:**
  ```bash
  gcloud compute shared-vpc enable shopnow-net                     # host project
  gcloud compute shared-vpc associated-projects add shopnow-app \
    --host-project=shopnow-net                                     # service project
  ```
- **Not to be confused with:** VPC peering (two separate VPCs linked). Shared VPC = **one** network used by many projects.
- **Analogy:** 📞 **Head office's phone system** that the branch offices plug into, so everyone dials internal extensions.
- **In the online store:** The network team owns `shopnow-net`; the app team's VMs in `shopnow-app` use its subnets.

### 3️⃣ GCP Organization
- **What it is:** The **top-level container** for a company's projects, tied to its domain. Shared VPC only works between projects in the **same organization**.
- **Looks like:** `shopnow.com (org) → shopnow-net, shopnow-app`
- **Analogy:** 🏢 The **parent company** that owns all branch offices.

### 4️⃣ Project Administrator / Owner
- **What it is:** Someone with full control of one project.
- **Not to be confused with:** a cross-project network feature. Being admin of both projects doesn't let a VPC span them.
- **Analogy:** 🔑 Having the **keys to two buildings** doesn't connect their phone systems.

### 🔗 How they fit together
```
 🏢 Organization shopnow.com
   ├── host project shopnow-net
   │     └── 🌐 shared-vpc (subnet 10.0.1.0/24) ◄─── VMs of host project
   └── service project shopnow-app ───────────────► VMs created IN shared-vpc
         (now all VMs talk by private IP) ✅
```

---

## 🌍 Real-World Scenario

Big companies split work into many projects (one per team or app) but want **one network** managed centrally by the network/security team. They set up **Shared VPC**: the network team owns the host project with the VPC, subnets and firewall rules; app teams create their VMs in it from their own projects. Traffic flows privately, and network control stays in one place.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Verify that both projects are in a GCP Organization. Create a new VPC and add all instances.

**Wrong words:**
- ✔️ "Verify that both projects are in a GCP Organization" is a good first step.
- ❌ "**Create a new VPC and add all instances**": a new VPC belongs to **one project**, so the other project's VMs **can't join** it. Without sharing, nothing changes.

📌 **When to use it:** Use a new VPC when you're starting a fresh network for VMs **in one project**.
🏢 **Office example:** Installing a new phone system in one building and expecting the other building's phones to just work.

### ✅ B
> **B.** Verify that both projects are in a GCP Organization. Share the VPC from one project and request that the Compute Engine instances in the other project use this shared VPC.

**Why it's correct:**
- ✔️ "**Verify that both projects are in a GCP Organization**" matches "**two different GCP projects**": Shared VPC only works for projects in the same organization, so this is the required check.
- ✔️ "**Share the VPC from one project**" matches "**enable traffic between multiple groups of Compute Engine instances**": the host project's network becomes available to the other project.
- ✔️ "**request that the Compute Engine instances in the other project use this shared VPC**" matches "**each group … running in its own VPC**": the other project's VMs move onto the shared network, so all VMs talk by private IP.

📌 **When to use it:** Use it when several departments should all use one central network run by one team.
🏢 **Office example:** Branch offices plugging into head office's phone system so everyone can dial internal extensions.

### ❌ C
> **C.** Verify that you are the Project Administrator of both projects. Create two new VPCs and add all instances.

**Wrong words:**
- ❌ "**Verify that you are the Project Administrator of both projects**": being admin doesn't create a cross-project network.
- ❌ "**Create two new VPCs**": two separate VPCs are **isolated** from each other, the same problem you started with.

📌 **When to use it:** Use separate VPCs when you **want** two groups kept apart.
🏢 **Office example:** Buying two new phone systems for two buildings. They still can't call each other.

### ❌ D
> **D.** Verify that you are the Project Administrator of both projects. Create a new VPC and add all instances.

**Wrong words:**
- ❌ "**Verify that you are the Project Administrator of both projects**": admin rights don't connect networks.
- ❌ "**Create a new VPC and add all instances**": the VPC lives in **one** project; VMs from the other project can't be added to it without Shared VPC.

📌 **When to use it:** Use it only when all the VMs are in the **same** project.
🏢 **Office example:** Having keys to both buildings but installing a phone system in only one of them.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's network team owns `shopnow-net`. The payments team works in `shopnow-payments`. Payments VMs must call the inventory VMs privately.

```bash
# Host project shares its VPC
gcloud compute shared-vpc enable shopnow-net
gcloud compute shared-vpc associated-projects add shopnow-payments --host-project=shopnow-net

# Payments team creates its VM IN the shared subnet
gcloud compute instances create pay-1 --project=shopnow-payments --zone=us-central1-a \
  --subnet=projects/shopnow-net/regions/us-central1/subnetworks/app-subnet

# pay-1 (10.0.1.20) → inventory-1 (10.0.1.5) ✅ private traffic
```

---

## 🧠 Key Takeaways / Memory Tips

- **A VPC belongs to one project.** To use it from another project → **Shared VPC** (same organization) or **VPC peering**.
- **Shared VPC needs an Organization.** "Verify both projects are in an Organization" is the giveaway.
- Being Project Admin of both projects doesn't connect networks.
  🧠 *"**Many projects, one network → Shared VPC.**"*
- Related: **Q060** (VPC peering), **Q054** (global VPC, regional subnets), **Q050** (VPC basics).

# Q022: Checking a Changed Deployment Manager Template with --preview

**Topic:** Deployment Manager (`--preview`, dependencies between resources, fast feedback before committing)

## ❓ Question
> You significantly changed a complex Deployment Manager template and want to confirm that the dependencies of all defined resources are properly met before committing it to the project. You want the most rapid feedback on your changes. What should you do?
>
> **A.** Use granular logging statements within a Deployment Manager template authored in Python.
>
> **B.** Monitor activity of the Deployment Manager execution on the Stackdriver Logging page of the GCP Console.
>
> **C.** Execute the Deployment Manager template against a separate project with the same configuration, and monitor for failures.
>
> **D.** Execute the Deployment Manager template using the --preview option in the same project, and observe the state of interdependent resources.

*(The `λ€"` characters in option D are a broken dash, shown here as `--`.)*

**My answer:** D
**Correct answer:** D
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You made big changes to a complex Deployment Manager template (a file describing the resources to create and how they depend on each other).
- **What you must achieve:** Check that every resource and its dependencies (what needs what first) are correct before committing the change.
- **The limits:** You want the fastest feedback.
- **What they're really asking:** How do you check the template quickly without actually building everything?

| Keyword | What it hints at |
|---|---|
| "**before committing it to the project**" | Don't create real resources yet, so **preview first** |
| "**dependencies of all defined resources are properly met**" | Deployment Manager has to read the whole template and work out **what depends on what** |
| "**most rapid feedback**" | No new project, no waiting for real resources to build, no digging through logs |
| "**Deployment Manager**" | The answer is a Deployment Manager feature: **`--preview`** |

**Exam topic:** Deployment Manager (infrastructure as code), specifically **previewing changes**. Related to Q011 and Q014.

---

## 📚 Key Terms Explained

### 1️⃣ Deployment Manager and Templates (review from Q011 and Q014)
- **What it is:** Google's older **infrastructure-as-code** tool. You describe resources (VMs, networks, firewall rules, buckets) in a **config file (YAML)** plus **templates (Jinja or Python)**, and Deployment Manager builds them for you. *Note: it's now deprecated in favor of Infrastructure Manager (Terraform), but it's still on the exam.*
- **Analogy:** 📐 An **office floor plan** that the builders follow to set up a new branch.
- **In the online store:** `shopnow-infra.yaml` describes ShopNow's VPC, subnet, firewall rules and the checkout VMs.

### 2️⃣ Deployment
- **What it is:** The **set of real resources** that Deployment Manager created from your config (for example, the deployment named `shop-infra`).
- **Analogy:** 🏢 The **actual branch office** that was built from the floor plan.

### 3️⃣ Dependencies (interdependent resources)
- **What it is:** When one resource **needs another one to exist first**. A **VM** needs its **subnet**, and a subnet needs its **VPC**. In Deployment Manager this comes from **references** (`$(ref.shop-vpc.selfLink)`) or `dependsOn`, and it decides the **order** things are built in.
- **Analogy:** 🧱 You can't put **desks** in a room that hasn't been **built**, and you can't build the room before the **floor** exists.
- **In the online store:** `checkout-vm` → needs `shop-subnet` → needs `shop-vpc`. If the template references a subnet name that doesn't exist, the dependency is **not met**.

### 4️⃣ `--preview` 🔑
- **What it is:** A flag for `gcloud deployment-manager deployments create` or `update`. Deployment Manager **reads and expands the whole template**, checks the resources and their references, and shows you **what it would create, change or delete**, **without actually building anything**. Then you either:
  - **commit:** `gcloud deployment-manager deployments update NAME` (with no config), or
  - **throw it away:** `gcloud deployment-manager deployments cancel-preview NAME`.
- **Analogy:** 🔍 The builders **walk through the floor plan with you** and say, *"Here's what we'll build, in this order."* No one picks up a hammer until you say "Go."

### 5️⃣ Stackdriver Logging (now Cloud Logging)
- **What it is:** Google Cloud's service for **collecting and searching logs**. "Stackdriver" is the **old name**.
- **Analogy:** 📓 The building's **logbook**, where you read what happened **after** it happened.

### 6️⃣ Logging statements in a Python template
- **What it is:** Extra lines in your **Python template code** that print messages while it runs, for debugging the code itself.
- **Analogy:** 📝 Sticky notes on the floor plan saying *"I got to page 3."* They help you follow the drawing, but they don't check whether the building works.

### 🔗 How They Fit Together
```
📄 Config (YAML) + 📐 Templates (Jinja/Python)
        │
        │  gcloud deployment-manager deployments update shop-infra --config shop-infra.yaml --preview
        ▼
🔍 PREVIEW: Deployment Manager expands the templates, works out dependencies, shows the plan
        │   shop-vpc ──► shop-subnet ──► checkout-vm   (nothing is built yet)
        │
        ├── Looks right?  → deployments update shop-infra            ✅ commit (now it builds)
        └── Problem?      → deployments cancel-preview shop-infra    ❌ fix the template, try again
```

---

## 🌍 Real-World Scenario

An engineer rewrites a big infrastructure template: new subnet names, a new firewall rule, VMs moved into the new subnet. If one **reference is wrong** (for example, a VM points to a subnet that was renamed), the deployment might **fail halfway**, or **change or delete live production resources** by mistake.

Teams always want a **dry run before the real thing**. In Deployment Manager, that dry run is **`--preview`**. (In Terraform the same idea is `terraform plan`.)

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use granular logging statements within a Deployment Manager template authored in Python.

**Why it's wrong:**
- ❌ Logging statements help you **debug the template code**, but they **don't check dependencies** between resources.
- ❌ It **only works for Python** templates, not Jinja or YAML.
- ❌ It's **slow**: you have to add the log lines, run it, then read the output.

**📌 When to use it:** Use it when your own template code does something strange and you want to follow it step by step.
🏢 **Office example:** Writing notes in the margin of a long form so you can see where you made a mistake.

### ❌ B
> **B.** Monitor activity of the Deployment Manager execution on the Stackdriver Logging page of the GCP Console.

**Why it's wrong:**
- ❌ Logs show what happened **after it ran**. By then the change is **already committed** to the project, which is too late.
- ❌ Reading through logs is **not the fastest** feedback.

**📌 When to use it:** Use it when something already ran and you want to find out what happened.
🏢 **Office example:** Reading the building's visitor logbook the next morning to see who came in.

### ❌ C
> **C.** Execute the Deployment Manager template against a separate project with the same configuration, and monitor for failures.

**Why it's wrong:**
- ❌ **Slow:** you have to set up a whole second project and **actually build every resource**.
- ❌ It **costs money**, because real VMs and networks run there.
- ✔️ It *would* find problems, but it's **not the most rapid**.

**📌 When to use it:** Use it when you want a full rehearsal in a safe test copy before a big launch.
🏢 **Office example:** Setting up a complete practice branch office to test a new layout before changing the real one.

### ✅ D (your answer)
> **D.** Execute the Deployment Manager template using the --preview option in the same project, and observe the state of interdependent resources.

**Why it's correct:**
- ✔️ **`--preview`** makes Deployment Manager **expand the whole template** and lay out **all resources and their dependencies**, **without building or changing anything**.
- ✔️ It's the **fastest** feedback: there's no second project and no waiting for real VMs.
- ✔️ It runs **in the same project**, so it checks your changes **against what really exists there**.
- ✔️ Then you **commit** (`deployments update NAME`) or **cancel** (`deployments cancel-preview NAME`).

**📌 When to use it:** Use it when you want to see exactly what a change will do before it really happens.
🏢 **Office example:** The builders walk through the new floor plan with you and say what they'll build, before anyone picks up a hammer.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's infrastructure lives in the deployment **`shop-infra`**. Maria makes a big change to the template: she **renames the subnet** to `shop-subnet-v2` and **adds 2 checkout VMs** that use it.

```yaml
# shop-infra.yaml (simplified)
resources:
- name: shop-vpc
  type: compute.v1.network
  properties: { autoCreateSubnetworks: false }

- name: shop-subnet-v2
  type: compute.v1.subnetwork
  properties:
    network: $(ref.shop-vpc.selfLink)          # depends on shop-vpc
    ipCidrRange: 10.10.0.0/20
    region: us-central1

- name: checkout-vm-3
  type: compute.v1.instance
  properties:
    zone: us-central1-a
    networkInterfaces:
    - subnetwork: $(ref.shop-subnet-v2.selfLink)   # depends on shop-subnet-v2
```

**1. Preview (nothing is built yet):**
```bash
gcloud deployment-manager deployments update shop-infra \
  --config shop-infra.yaml --preview
```
Deployment Manager lists every resource and what will happen to each one (create / update / delete). If a reference is wrong, for example `$(ref.shop-subnet.selfLink)` pointing to the **old** name, the preview **fails right away** and tells her which reference is broken.

**2a. Looks good → commit:**
```bash
gcloud deployment-manager deployments update shop-infra
```
**2b. Something's wrong → cancel, fix, preview again:**
```bash
gcloud deployment-manager deployments cancel-preview shop-infra
```

**🎬 With the other options:**
- **B (logs):** Maria runs it for real, the update **fails halfway**, and checkout is down while she reads the logs. ❌
- **C (second project):** She spends an hour creating `shopnow-test`, waits for the VMs to build, and pays for them. It works, but it's **slow**. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Check a Deployment Manager change before committing" + "fastest" → `--preview`.**
- **Preview = see the plan, build nothing.** Then **`update`** (commit) or **`cancel-preview`** (throw it away).
- **Logs = after the fact.** **A separate project = slow and costs money.** **Python logging = debugs code, not dependencies.**
- 🧠 *"**Preview** before you **build**: look at the plan before anyone picks up a hammer."*
- Same idea in other tools: **`terraform plan`**, and the BigQuery **dry run** from Q015.
- Deployment Manager family so far: **Q011** (what it is), **Q014** (`deployments update`), **Q022** (`--preview`).

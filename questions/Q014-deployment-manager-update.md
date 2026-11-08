# Q014: Updating a Deployment Manager Deployment Without Downtime

**Topic:** Infrastructure as Code (Deployment Manager commands: `deployments create` vs `deployments update` vs `resources`)

## ❓ Question
> You need to update a deployment in Deployment Manager without any resource downtime in the deployment. Which command should you use?
>
> **A.** gcloud deployment-manager deployments create --config <deployment-config-path>
>
> **B.** gcloud deployment-manager deployments update --config <deployment-config-path>
>
> **C.** gcloud deployment-manager resources create --config <deployment-config-path>
>
> **D.** gcloud deployment-manager resources update --config <deployment-config-path>

**My answer:** B
**Correct answer:** B
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You manage infrastructure with Deployment Manager (an older Google tool that creates cloud resources from template files).
- **What you must achieve:** Apply changes to an existing deployment.
- **The limits:** The resources must not go down while the update happens.
- **What they're really asking:** Which command updates the deployment without causing downtime?

| Keyword | What it hints at |
|---|---|
| "**update a deployment**" | The deployment **already exists**, so use `deployments update`, not `create` |
| "**without any resource downtime**" | Change only what's different and leave everything else running |
| "**Which command**" | Know which `gcloud deployment-manager` commands **actually exist** |

**Exam topic:** Infrastructure as Code, specifically **Deployment Manager commands**.

⚠️ **Reminder from Q011:** Deployment Manager is **deprecated**, and Google now recommends **Infrastructure Manager (Terraform)**. The idea is the same in Terraform: `terraform plan` (preview) → `terraform apply` (update only what changed).

*(Note: the real commands also need the **deployment name**, e.g., `deployments update shopnow-infra --config=...`. The question leaves it out.)*

---

## 📚 Key Terms Explained

### 1️⃣ Deployment Manager (review from Q011)
- **What it is:** Google's (older) **Infrastructure as Code** tool. You describe resources in a **YAML config file**, and it builds them.
- **Analogy:** 🏗️ A **construction company** that builds exactly what's on your blueprint.

### 2️⃣ Deployment
- **What it is:** **One named group of resources** that Deployment Manager created from a config file (e.g., `shopnow-infra` = a VPC + firewall + 2 VMs). You manage the whole group together.
- **Analogy:** 🏢 **One branch office** built from one setup plan, with all its desks, printers, and rooms.
- **In the online store:** The `shopnow-infra` deployment contains the API VM, the worker VM, and the firewall rules.

### 3️⃣ Resource
- **What it is:** **One single item** inside a deployment: one VM, one firewall rule, one disk.
- **Analogy:** 🪑 **One desk** or **one printer** in the branch office.
- In Deployment Manager, the `resources` commands can only **list** and **describe** (look at) resources. You **can't** create or update single resources with them. You change resources by **updating the deployment**.

### 4️⃣ Configuration File (review from Q011)
- **What it is:** The YAML **blueprint** that lists every resource and its settings.
- **Analogy:** 📐 The **office floor plan**.

### 5️⃣ Create vs Update
- **`deployments create`:** Builds a **brand-new** deployment. It **fails** if a deployment with that name already exists.
- **`deployments update`:** **Compares** the new config with what's running, then **only adds, changes, or removes what's different**. Unchanged resources **keep running untouched**, so there's no downtime for them.
- **Analogy:** 🏢 **Create** = opening a **new branch** from scratch. **Update** = giving the existing branch a **new floor plan**, where only the desks that changed get moved and everyone else keeps working.

### 6️⃣ Downtime
- **What it is:** Time when your app or server is **not available** to users.
- **Analogy:** 🚪 A **"Closed for renovation"** sign on the office door.
- **In the online store:** Shoppers can't check out. 😱

### 7️⃣ Preview (bonus, good to know)
- **What it is:** `deployments update ... --preview` shows **what would change** without changing anything yet. Then you apply it (run `update` again without `--config`) or cancel it (`cancel-preview`).
- **Analogy:** 📋 Showing the boss the **new floor plan for approval** before anyone moves a desk.

### 🔗 How They Fit Together
```
📐 shopnow-infra.yaml (edited: added a worker VM + HTTPS firewall rule)
        │
        │  gcloud deployment-manager deployments update shopnow-infra --config=shopnow-infra.yaml
        ▼
🏢 Deployment: shopnow-infra
   ├── 🖥️ api-vm          → unchanged → keeps running ✅ (no downtime)
   ├── 🔥 allow-http      → unchanged → untouched ✅
   ├── 🔥 allow-https     → NEW       → created ➕
   └── 🖥️ worker-vm       → NEW       → created ➕

🔍 gcloud deployment-manager resources list / describe  → only LOOK at resources (no create/update)
```

---

## 🌍 Real-World Scenario

Infrastructure changes all the time: add a server, open a port, increase a disk size. With Infrastructure as Code, you **edit the config file** and **apply** it. The key skill is applying changes **safely**: only touch what changed, so the live app keeps serving users.

In Deployment Manager, that's `deployments update` (ideally with `--preview` first to double-check).

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** gcloud deployment-manager deployments create --config <deployment-config-path>

**Why it's wrong:**
- ❌ `create` makes a **brand-new** deployment. The question asks to **update an existing** one.
- ❌ If you reuse the same name, it **fails** ("already exists"). If you use a new name, you get a **second copy** of everything (double cost, and the old one isn't updated).

**📌 When to use it:** Use it when you're **building something brand new** for the first time.
🏢 **Office example:** **Opening a brand-new branch office** from the setup plan.

### ✅ B
> **B.** gcloud deployment-manager deployments update --config <deployment-config-path>

**Why it's correct:**
- ✔️ `update` applies your edited config to the **existing** deployment.
- ✔️ It **compares** the new config with what's running and **only changes what's different**. Unchanged resources **keep running**, so there's **no downtime** for them.
- ✔️ You can add `--preview` to check the changes first, which is a safe habit for production.

**📌 When to use it:** Use it when you want to **change something that already exists**, while everything else **keeps running**.
🏢 **Office example:** Giving the branch a **new floor plan**: only the desks that changed get moved, and **everyone else keeps working**.

### ❌ C
> **C.** gcloud deployment-manager resources create --config <deployment-config-path>

**Why it's wrong:**
- ❌ **This command doesn't exist.** `gcloud deployment-manager resources` only has **`list`** and **`describe`** (read-only).
- ❌ You don't create single resources directly. You add them to the config and run `deployments update`.
- ⚠️ **Trap option:** it *sounds* real.

**📌 When to use it:** **Never use this.** The command doesn't exist. Use `deployments create` for new deployments, or `deployments update` to add resources.
🏢 **Office example:** Like asking the **records clerk** to build a new office. The clerk can only **show you the list** of what already exists.

### ❌ D
> **D.** gcloud deployment-manager resources update --config <deployment-config-path>

**Why it's wrong:**
- ❌ **This command doesn't exist either.** `resources` is read-only (`list`, `describe`).
- ❌ To change a resource, edit the config and run **`deployments update`** (option B).

**📌 When to use it:** **Never use this.** The command doesn't exist. Use option B instead.
🏢 **Office example:** Like asking the **records clerk** to remodel a room. They can only **tell you what's in it**.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's infrastructure lives in the `shopnow-infra` deployment. The API VM is **serving live shoppers**. The team needs to:
1. Add a **worker VM** that sends order confirmation emails
2. Open **port 443 (HTTPS)**

**The edited config (`shopnow-infra.yaml`), new parts marked:**
```yaml
resources:
- name: api-vm                      # existing, unchanged
  type: compute.v1.instance
  properties:
    zone: asia-southeast1-a
    machineType: zones/asia-southeast1-a/machineTypes/e2-medium
    disks:
    - deviceName: boot
      boot: true
      autoDelete: true
      initializeParams:
        sourceImage: projects/debian-cloud/global/images/family/debian-12
    networkInterfaces:
    - network: global/networks/default

- name: worker-vm                   # ➕ NEW
  type: compute.v1.instance
  properties:
    zone: asia-southeast1-a
    machineType: zones/asia-southeast1-a/machineTypes/e2-small
    disks:
    - deviceName: boot
      boot: true
      autoDelete: true
      initializeParams:
        sourceImage: projects/debian-cloud/global/images/family/debian-12
    networkInterfaces:
    - network: global/networks/default

- name: allow-https                 # ➕ NEW
  type: compute.v1.firewall
  properties:
    network: global/networks/default
    sourceRanges: ["0.0.0.0/0"]
    allowed:
    - IPProtocol: TCP
      ports: ["443"]
```

**Safe update with preview (option B):**
```bash
# 1. Preview: see what WOULD change (nothing is changed yet)
gcloud deployment-manager deployments update shopnow-infra \
  --config=shopnow-infra.yaml --preview

# 2. Check: api-vm = no change, worker-vm + allow-https = to be created
gcloud deployment-manager deployments describe shopnow-infra

# 3. Apply the previewed changes
gcloud deployment-manager deployments update shopnow-infra

# 4. Look at the resources (read-only, this is what "resources" commands are for)
gcloud deployment-manager resources list --deployment=shopnow-infra
```

**🎬 Result:** `worker-vm` and `allow-https` are created. `api-vm` is **never touched**, so shoppers keep checking out the whole time. ✅

**With the other options:**
- **A (`create`):** `ERROR: ... 'shopnow-infra' already exists`. Or, with a new name, you get a **second** API VM and double the cost. ❌
- **C / D (`resources create/update`):** `ERROR: Invalid choice`. The commands don't exist. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Existing deployment + change config → `gcloud deployment-manager deployments update NAME --config=FILE`.**
- **`update` only changes what's different**, so unchanged resources keep running (no downtime).
- **`deployments create` = brand new only.** It fails if the name already exists.
- **`resources` commands are read-only: only `list` and `describe`.** There's no `resources create` or `resources update`.
- **Safe habit:** `update --preview` first, then apply.
- 🧠 *"**Deployments** = do things (create, update, delete). **Resources** = just look (list, describe)."*
- Modern equivalent: **Terraform** → `terraform plan` (preview) → `terraform apply` (update).

# Q005: Reviewing an Inactive gcloud Configuration

**Topic:** Cloud SDK / gcloud CLI (named configurations, properties) + kubectl contexts

## ❓ Question
> You are using multiple configurations for gcloud. You want to review the configured Kubernetes Engine cluster of an inactive configuration using the fewest possible steps. What should you do?
>
> **A.** Use gcloud config configurations describe to review the output.
>
> **B.** Use gcloud config configurations activate and gcloud config list to review the output.
>
> **C.** Use kubectl config get-contexts to review the output.
>
> **D.** Use kubectl config use-context and kubectl config view to review the output.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You have several saved **gcloud profiles** (configurations), for example one for dev and one for prod. You're currently using one of them. You want to **peek at the settings of a different one** (the inactive one), specifically which GKE cluster it points to, **without switching to it** and with **as few commands as possible**.

| Keyword | What it hints at |
|---|---|
| "**multiple configurations for gcloud**" | The answer is a **gcloud config configurations** command, not kubectl |
| "**inactive configuration**" | Not the one you're currently using |
| "**review**" | Just look, don't change anything |
| "**fewest possible steps**" | **One** command beats two |

**Exam topic:** Cloud SDK / gcloud CLI, specifically **named configurations**.

---

## 📚 Key Terms Explained

### 1️⃣ gcloud CLI (Cloud SDK)
- **What it is:** Google Cloud's **command-line tool**. You type commands in a terminal to create VMs, clusters, databases, and so on, instead of clicking in the web console.
- **Analogy:** 🎮 A **remote control** for Google Cloud.
- **In the online store:** `gcloud compute instances list` shows all of ShopNow's VMs.

### 2️⃣ gcloud Configuration (Named Configuration)
- **What it is:** A **saved profile** of gcloud settings (called **properties**), like which **account**, **project**, **region/zone**, and **GKE cluster** to use by default. You can have many configurations and switch between them.
- **Analogy:** 👤 **User profiles on Netflix**. Each profile remembers its own settings. Switching profiles changes everything at once.
- **In the online store:** `shopnow-dev` points to the dev project and cluster. `shopnow-prod` points to the production project and cluster.

### 3️⃣ Active vs Inactive Configuration
- **Active:** The configuration gcloud is **using right now**. Every command uses its settings. Only **one** can be active at a time.
- **Inactive:** Any other saved configuration. It exists, but it isn't being used.
- **Analogy:** 🔑 You have keys to your **home** and your **office**, but you can only be standing in one place. The other key is "inactive" in your pocket.
- **In the online store:** You're working in `shopnow-dev` (active), and you want to check what `shopnow-prod` (inactive) is set to.

### 4️⃣ Properties (including `container/cluster`)
- **What it is:** The individual settings stored inside a configuration, grouped into sections:
  - `core/account`: which Google account
  - `core/project`: which GCP project
  - `compute/region`, `compute/zone`: default location
  - `container/cluster`: **default GKE cluster** ← what this question asks about
- **Analogy:** 📝 The **fields on a profile card**: name, address, favorite store.
- **In the online store:** `shopnow-prod` has `container/cluster = shopnow-prod-gke`.

### 5️⃣ Kubernetes Engine (GKE) Cluster
- **What it is:** Google's **managed Kubernetes** service. A cluster is a group of machines (nodes) that run your apps as **containers**.
- **Analogy:** 🚢 A **cargo ship** (cluster) carrying many **shipping containers** (your apps). Kubernetes is the captain deciding where each container goes.
- **In the online store:** `shopnow-prod-gke` runs the storefront, Orders API, and Payments API as containers.

### 6️⃣ kubectl
- **What it is:** The **command-line tool for Kubernetes**. It talks directly to a cluster (deploy apps, view Pods, check logs). It's **separate** from gcloud.
- **Analogy:** 🎮 gcloud is the remote for **all of Google Cloud**. kubectl is the remote for **just the Kubernetes ship**.
- **In the online store:** `kubectl get pods` lists the running storefront and API containers.

### 7️⃣ kubeconfig and Contexts
- **kubeconfig:** kubectl's own settings file (`~/.kube/config`). It lists clusters, users, and **contexts**.
- **Context:** A saved combination of **cluster + user + namespace** that kubectl uses. You switch with `kubectl config use-context`.
- ⚠️ **Important:** kubectl contexts are **not** gcloud configurations. They're two different tools with two separate settings files.
- **Analogy:** 📒 gcloud keeps its own address book, and kubectl keeps a separate one. Changing one doesn't change the other.

### 🔗 How They Fit Together
```
💻 Your laptop
│
├── 🎮 gcloud  (settings in ~/.config/gcloud/configurations/)
│     ├── ✅ shopnow-dev   (ACTIVE)
│     │      core/project      = shopnow-dev
│     │      container/cluster = shopnow-dev-gke
│     └── 💤 shopnow-prod  (INACTIVE)  ← question: "which cluster does this point to?"
│            core/project      = shopnow-prod
│            container/cluster = shopnow-prod-gke
│
└── 🎮 kubectl (settings in ~/.kube/config)  ← separate file, separate tool
      ├── context: gke_shopnow-dev_asia-southeast1_shopnow-dev-gke   (current)
      └── context: gke_shopnow-prod_asia-southeast1_shopnow-prod-gke
```

---

## 🌍 Real-World Scenario

A cloud engineer manages several environments (dev, staging, prod), often in different projects or even for different clients. They keep one gcloud configuration per environment.

While working in dev, they want to double-check which cluster the **prod** configuration is set to, maybe before running a deployment script. **Switching** to prod just to look is risky: if they forget to switch back, their next command might hit production. 😱 They want to **look without switching**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use gcloud config configurations describe to review the output.

**Why it's correct:**
- ✔️ `gcloud config configurations describe <NAME>` shows **all properties of any configuration**, active **or inactive**, including `container/cluster`.
- ✔️ **One command**, so it's the fewest steps.
- ✔️ It **doesn't switch** your active configuration, so it's safe.

**📌 When to use it:** Use it when you just want to **look at a saved profile's settings without switching** to it.
🏢 **Office example:** Reading another department's information sheet in the company directory, without moving to their desk.

### ❌ B
> **B.** Use gcloud config configurations activate and gcloud config list to review the output.

**Why it's wrong:**
- ✔️ It would **work**: activate the inactive configuration, then list its properties.
- ❌ It takes **two commands** (plus a third to switch back), so it isn't the fewest steps.
- ❌ It **changes your active configuration**, which is a side effect you didn't want. A risky habit with prod.

**📌 When to use it:** Use it when you actually want to **switch to that profile and start working** in it.
🏢 **Office example:** Moving to the other department's desk to work there today.

### ❌ C
> **C.** Use kubectl config get-contexts to review the output.

**Why it's wrong:**
- ❌ This lists **kubectl contexts** from `~/.kube/config`, not **gcloud configurations**.
- ❌ It doesn't tell you which cluster a specific **gcloud** configuration is set to. Those are separate settings.
- ⚠️ **Trap option:** it mentions clusters, but it's the **wrong tool**.

**📌 When to use it:** Use it when you want to see **which Kubernetes clusters kubectl can connect to**.
🏢 **Office example:** Checking the list of buildings your keycard can open.

### ❌ D
> **D.** Use kubectl config use-context and kubectl config view to review the output.

**Why it's wrong:**
- ❌ **Wrong tool** (kubectl, not gcloud), same as C.
- ❌ **Two commands**, and `use-context` **switches** your current kubectl context, which is another unwanted side effect.

**📌 When to use it:** Use it when you want to **switch kubectl to a different cluster** and check its settings.
🏢 **Office example:** Switching your keycard to another building, then reading that building's rules.

---

## 🛒 E-Commerce Full-Stack Example

You're Maria, a DevOps engineer at **ShopNow**. You have two environments:

| Configuration | Project | GKE cluster | Used for |
|---|---|---|---|
| `shopnow-dev` | shopnow-dev | shopnow-dev-gke | testing new checkout features |
| `shopnow-prod` | shopnow-prod | shopnow-prod-gke | real shoppers 💰 |

**One-time setup:**
```bash
gcloud config configurations create shopnow-prod
gcloud config set project shopnow-prod
gcloud config set compute/region asia-southeast1
gcloud config set container/cluster shopnow-prod-gke

gcloud config configurations create shopnow-dev     # creating also activates it
gcloud config set project shopnow-dev
gcloud config set container/cluster shopnow-dev-gke
```

**See all configurations:**
```bash
$ gcloud config configurations list
NAME          IS_ACTIVE  ACCOUNT            PROJECT
shopnow-dev   True       maria@shopnow.com  shopnow-dev
shopnow-prod  False      maria@shopnow.com  shopnow-prod
```

**✅ Option A: check prod's cluster without leaving dev (1 command):**
```bash
$ gcloud config configurations describe shopnow-prod
is_active: false
name: shopnow-prod
properties:
  compute:
    region: asia-southeast1
  container:
    cluster: shopnow-prod-gke      # ← the answer
  core:
    account: maria@shopnow.com
    project: shopnow-prod
```
You're **still safely in dev**. ✅

**❌ Option B: the risky way:**
```bash
gcloud config configurations activate shopnow-prod   # now in PROD!
gcloud config list
# ...forget to switch back...
gcloud container clusters delete shopnow-dev-gke     # intended for dev 😱
#   → runs against the PROD project instead
```

---

## 🧠 Key Takeaways / Memory Tips

- **"Review an inactive gcloud configuration" → `gcloud config configurations describe <NAME>`.**
- **gcloud configurations ≠ kubectl contexts.** Separate tools, separate files.
  🧠 *"Question says **gcloud** → answer uses **gcloud**."*
- **"Fewest steps" + "review" → pick the single read-only command.** Avoid options that **activate** or **use** (switch) something.
- Useful gcloud config commands:
  | Command | What it does |
  |---|---|
  | `gcloud config configurations list` | List all configurations, showing which is active |
  | `gcloud config configurations describe NAME` | Show one configuration's properties (no switching) |
  | `gcloud config configurations activate NAME` | Switch to a configuration |
  | `gcloud config configurations create NAME` | Create a new configuration (and activate it) |
  | `gcloud config list` | Show properties of the **active** configuration only |
  | `gcloud config set container/cluster NAME` | Set the default GKE cluster |

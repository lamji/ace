# Q032: One Monitoring Dashboard for Many Projects (Stackdriver Account → Metrics Scope)

**Topic:** Cloud Monitoring (formerly Stackdriver): Workspace / metrics scope, monitored projects, Monitoring groups, Shared VPC

## ❓ Question
> You need to monitor resources that are distributed over different projects in Google Cloud Platform. You want to consolidate reporting under the same Stackdriver Monitoring dashboard. What should you do?
>
> **A.** Use Shared VPC to connect all projects, and link Stackdriver to one of the projects.
>
> **B.** For each project, create a Stackdriver account. In each project, create a service account for that project and grant it the role of Stackdriver Account Editor in all other projects.
>
> **C.** Configure a single Stackdriver account, and link all projects to the same account.
>
> **D.** Configure a single Stackdriver account for one of the projects. In Stackdriver, create a Group and add the other project names as criteria for that Group.

**My answer:** D
**Correct answer:** C
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** Your VMs, databases and apps live in **several different projects**. You want to see **all of them on one monitoring dashboard**. How do you set that up?

| Keyword | What it hints at |
|---|---|
| "**distributed over different projects**" | Monitoring normally sees **one project**. You must **connect** the others |
| "**consolidate**" / "**same dashboard**" | **One** monitoring home, with every project **linked** into it |
| "**Stackdriver account**" | Old name for a **Monitoring Workspace**, called a **metrics scope** today |

**Exam topic:** Cloud Monitoring (multi-project monitoring).

---

## 📚 Key Terms Explained

### 1️⃣ Stackdriver Account → Workspace → Metrics Scope 🔑
- **What it is:** The **"home" of Cloud Monitoring** that decides **which projects' metrics you can see**. It lives in one project (the **scoping project**), and you **add other projects** to it as **monitored projects**. The name changed over the years: **Stackdriver account → Workspace → metrics scope**. Same idea.
- **Looks like:**
  ```
  Metrics scope of project: shopnow-monitoring   (scoping project)
    ├── shopnow-monitoring (itself)
    ├── shopnow-web        (monitored project)
    ├── shopnow-orders     (monitored project)
    └── shopnow-data       (monitored project)
  ```
- **Not to be confused with:** a billing account or a user account. Nobody logs in to it. It's a **list of projects** whose metrics are pulled together.
- **Analogy:** 🖥️ The **head office security room**. You **wire the cameras** from each branch into it, then watch every branch on one wall of screens.
- **In the online store:** One dashboard shows the web VMs, the orders database and the data pipeline, even though they're in 3 projects.

### 2️⃣ "Link a project" (add a monitored project)
- **What it is:** **Adding a project to the metrics scope** so its metrics show up in that Monitoring home.
- **Looks like:** Console: **Monitoring → Settings → Metrics scope → Add projects → shopnow-orders**
  CLI: `gcloud beta monitoring metrics-scopes create projects/shopnow-orders --project=shopnow-monitoring`
- **Not to be confused with:** connecting networks. Linking is about **metrics visibility**, not network traffic.
- **Analogy:** 🔌 **Plugging a branch's camera cable** into the head office.

### 3️⃣ Monitoring Group (Stackdriver Group)
- **What it is:** A **saved filter** inside Monitoring that bundles **resources you can already see** by rules like name, label or region, so you can chart or alert on them together.
- **Looks like:** Group `checkout-servers` = "VM name contains `checkout`" or "label `tier=web`"
- **Not to be confused with:** linking projects. A Group can only filter what's **already in the metrics scope**. It **can't pull in** resources from projects that aren't linked.
- **Analogy:** 🏷️ **Labelling screens** in the security room ("all checkout cameras"). That doesn't connect any new cameras.

### 4️⃣ Shared VPC (VPC basics in Q002)
- **What it is:** One project's **network** shared with other projects so their VMs use the same private network.
- **Looks like:** host project `shopnow-net` shares subnet `10.10.0.0/20` with `shopnow-web` and `shopnow-orders`.
- **Not to be confused with:** monitoring. It shares **network roads**, not **metrics**.
- **Analogy:** 🛣️ **One private road** between branch offices. It doesn't put their cameras on your screens.

### 5️⃣ Dashboard
- **What it is:** A page of **charts** in Cloud Monitoring (CPU, requests, errors…).
- **Analogy:** 📺 The **wall of screens** in the security room.

### 🔗 How They Fit Together
```
            🖥️ Metrics scope (old: "Stackdriver account")  in  shopnow-monitoring
                       │  linked (monitored) projects
     ┌─────────────────┼──────────────────┐
     ▼                 ▼                  ▼
 shopnow-web      shopnow-orders      shopnow-data
 (web VMs)        (Cloud SQL, API)    (Dataflow, BigQuery)
                       │
                       ▼
     📺 ONE dashboard with charts from all 3 ✅
     🏷️ Groups = filters INSIDE this view (optional extra)

❌ Shared VPC → shares the network, not metrics
❌ One account per project → many separate dashboards
❌ A Group alone → can't see unlinked projects
```

---

## 🌍 Real-World Scenario

Companies split work into **many projects**: one per team, per app, or per environment. The ops/on-call team doesn't want to switch between 10 dashboards during an outage. The standard setup is a **dedicated monitoring project** whose metrics scope **includes all the other projects**, so one dashboard and one set of alerts covers everything.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use Shared VPC to connect all projects, and link Stackdriver to one of the projects.

**Why it's wrong:**
- ❌ **Shared VPC shares a network**, not monitoring data. Monitoring would still see only the one project it's linked to.

**📌 When to use it:** Use Shared VPC when several projects' servers must talk to each other on one private network.
🏢 **Office example:** Building one private road between all branch offices so staff can drive between them.

### ❌ B
> **B.** For each project, create a Stackdriver account. In each project, create a service account for that project and grant it the role of Stackdriver Account Editor in all other projects.

**Why it's wrong:**
- ❌ **One account per project = many separate dashboards**, the opposite of "consolidate".
- ❌ A web of service accounts and cross-project roles: lots of work, and it doesn't create one shared view.

**📌 When to use it:** **Never use this.** It's a lot of work and still leaves you with separate views. Link all projects to one account (C).
🏢 **Office example:** Every branch builds its own security room and gives every other branch a key, but nobody gets one wall showing everything.

### ✅ C
> **C.** Configure a single Stackdriver account, and link all projects to the same account.

**Why it's correct:**
- ✔️ **One Monitoring home** (today: a metrics scope in one project) **with every project linked** = all metrics in one place.
- ✔️ Dashboards and alerts built there can show **resources from all linked projects**.
- ✔️ This is exactly how Google designed multi-project monitoring.

**📌 When to use it:** Use it when you want to watch things that live in many projects from one screen.
🏢 **Office example:** Wiring every branch's security cameras into the head office's one control room.

### ❌ D (your answer)
> **D.** Configure a single Stackdriver account for one of the projects. In Stackdriver, create a Group and add the other project names as criteria for that Group.

**Why it's wrong:**
- ✔️ "A single Stackdriver account" is a good start…
- ❌ …but **Groups only filter resources that are already visible**. The other projects were **never linked**, so their resources **aren't in the account**, and the Group finds nothing.
- 💡 **Likely mix-up:** "Group" sounds like "bring things together". In Monitoring it's just a **filter**. It can't connect new projects. (It's also different from a **Google group** of people in Q001/Q025.)

**📌 When to use it:** Use Monitoring Groups to bundle servers you can already see, like "all checkout servers", so you can chart or alert on them together.
🏢 **Office example:** Labelling screens in the control room "Checkout cameras". That only works for cameras already wired in.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow splits its system into 3 projects: **`shopnow-web`** (Next.js VMs), **`shopnow-orders`** (checkout API + Cloud SQL), **`shopnow-data`** (Pub/Sub, Dataflow, BigQuery). On Black Friday, on-call needs **one** screen.

```bash
# Use shopnow-monitoring as the scoping project and link the others
gcloud beta monitoring metrics-scopes create projects/shopnow-web    --project=shopnow-monitoring
gcloud beta monitoring metrics-scopes create projects/shopnow-orders --project=shopnow-monitoring
gcloud beta monitoring metrics-scopes create projects/shopnow-data   --project=shopnow-monitoring
```

**The "Black Friday" dashboard in `shopnow-monitoring` now shows:**
| Chart | Comes from |
|---|---|
| Storefront VM CPU | `shopnow-web` |
| Checkout API errors + Cloud SQL connections | `shopnow-orders` |
| Pub/Sub backlog of `order-placed` | `shopnow-data` |

**Optional extra:** a Monitoring **Group** `checkout-tier` (name contains `checkout`) for one alert on all checkout servers. This works **because** the projects are already linked.

**🎬 With option D:** The Group "project = shopnow-orders" shows **0 resources**, because that project was never linked. On-call misses the database overload. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"Many projects → one monitoring dashboard" → one Monitoring home (metrics scope) with all projects linked.**
  🧠 *"**Link the projects first, then build the dashboard.** Groups only filter what's already linked."*
- **Name history:** Stackdriver account → Workspace → **metrics scope** (same concept).
- **Shared VPC = network**, not monitoring. **Monitoring Group = filter**, not a connector.
- Related: **Q027** (Stackdriver = old name for Cloud Logging/Monitoring), **Q002** (VPC basics).

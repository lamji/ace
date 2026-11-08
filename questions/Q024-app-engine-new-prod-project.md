# Q024: Creating a Production Project for an App Engine App

**Topic:** App Engine + Resource Manager (`gcloud projects create`, `gcloud app create`, `gcloud app deploy --project`; dev and prod as separate projects)

## ❓ Question
> You have a project for your App Engine application that serves a development environment. The required testing has succeeded and you want to create a new project to serve as your production environment. What should you do?
>
> **A.** Use gcloud to create the new project, and then deploy your application to the new project.
>
> **B.** Use gcloud to create the new project and to copy the deployed application to the new project.
>
> **C.** Create a Deployment Manager configuration file that copies the current App Engine deployment into a new project.
>
> **D.** Deploy your application again using gcloud and specify the project parameter with the new project name to create the new project.

**My answer:** C
**Correct answer:** A
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An App Engine app runs in a development project, and testing passed.
- **What you must achieve:** Create a new project to serve as production.
- **The limits:** None stated.
- **What they're really asking:** What is the correct way to set up the production App Engine app?

The two steps are **(1) create the project** and **(2) deploy your source code to it**. Nothing in Google Cloud **copies** a running App Engine app from one project to another, and deploying doesn't **create** a project.

| Keyword | What it hints at |
|---|---|
| "**create a new project**" | Step 1: `gcloud projects create` |
| "**serve as your production environment**" | Step 2: deploy the **same code** there with `gcloud app deploy --project=…` |
| "**testing has succeeded**" | The code is ready. You deploy the code you already tested, rather than copying the dev deployment |

**Exam topic:** App Engine deployment and project setup (Resource Manager).

---

## 📚 Key Terms Explained

### 1️⃣ Project (review)
- **What it is:** The **container** for everything in Google Cloud: resources, billing, permissions. Companies usually keep **dev, test and prod in separate projects** so a mistake in dev can't break prod.
- **Analogy:** 🏢 **Separate office buildings**: the training center (dev) and the real branch serving customers (prod).
- **In the online store:** `shopnow-dev` and `shopnow-prod`.

### 2️⃣ Development vs Production Environment
- **Development (dev):** Where the team **builds and tests**. Mistakes are fine.
- **Production (prod):** What **real customers** use. Must be stable.
- **Analogy:** 🎭 **Rehearsal** vs **opening night**.

### 3️⃣ App Engine Application
- **What it is:** A fully managed platform. You upload your **code** and Google runs it. Each project has **one App Engine app**, set up once with `gcloud app create` and a **region you can't change later**.
- **Analogy:** 🏬 A **serviced office**: you bring your team and files (your code), and the building handles power, cleaning and security (servers).
- **In the online store:** ShopNow's storefront API runs on App Engine.

### 4️⃣ `gcloud projects create`
- **What it is:** Creates a **new, empty project**. Then you **link billing** (Q007) so it can run paid services.
- **Analogy:** 🏗️ **Opening a new, empty branch office**.

### 5️⃣ `gcloud app deploy` and `--project`
- **What it is:** **Uploads your source code** (with `app.yaml`) to App Engine and starts a new version. `--project=NAME` says **which existing project** to deploy into. It **doesn't create** projects.
- **Analogy:** 🚚 **Moving your team and files into a branch office.** The building must already exist.

### 6️⃣ Deployment Manager (review from Q011, Q014, Q022)
- **What it is:** Builds infrastructure from config files. It **creates resources**, but it **can't copy an existing App Engine deployment** (your code and versions) from another project.
- **Analogy:** 📐 A **floor plan** for building new rooms. It can't **pick up** a working office and move it.

### 🔗 How They Fit Together
```
💻 Your source code (tested in dev, stored in Git)
        │
        ├── gcloud app deploy --project=shopnow-dev    → 🧪 shopnow-dev  (App Engine, testing done ✅)
        │
        │   ① gcloud projects create shopnow-prod      → 🏢 empty project
        │   ①b link billing + gcloud app create --region=us-central --project=shopnow-prod
        └── ② gcloud app deploy --project=shopnow-prod → 🛒 shopnow-prod (live for customers)

  ❌ There is no "copy app from dev to prod" command.
  ❌ "app deploy --project=new-name" does NOT create the project.
```

---

## 🌍 Real-World Scenario

Teams **build in dev, test, then release to prod**. Prod lives in its **own project** so that:
- developers can't accidentally break the live site,
- prod gets its **own permissions** (fewer people) and its **own billing** view,
- the same **tested code** goes out in a **repeatable** way.

The normal flow: **create the prod project once**, then **deploy the same code** to it, usually from a CI/CD pipeline (for example Cloud Build).

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use gcloud to create the new project, and then deploy your application to the new project.

**Why it's correct:**
- ✔️ **Step 1:** `gcloud projects create` makes the production project. (Then link billing and run `gcloud app create` to pick its region.)
- ✔️ **Step 2:** `gcloud app deploy --project=<prod>` uploads the **same tested code** to the new project.
- ✔️ Both steps use **real commands** and the normal Google Cloud way of working.

**📌 When to use it:** Use it when you want a brand-new, separate place for the live version of your app.
🏢 **Office example:** Open the new branch office first, then move the trained team and their files in.

### ❌ B
> **B.** Use gcloud to create the new project and to copy the deployed application to the new project.

**Why it's wrong:**
- ✔️ Creating the project with gcloud is right.
- ❌ **There's no gcloud command to copy a deployed App Engine app** to another project. You **deploy the code** again instead.

**📌 When to use it:** **Never use this.** The copy command doesn't exist. Create the project and deploy the code (A).
🏢 **Office example:** You can't photocopy a working office. You open the new branch and move the team in.

### ❌ C (your answer)
> **C.** Create a Deployment Manager configuration file that copies the current App Engine deployment into a new project.

**Why it's wrong:**
- ❌ **Deployment Manager creates resources from a config file. It can't "copy" a running App Engine deployment** (your code and versions) from one project to another.
- ❌ It adds a lot of extra work compared with two simple gcloud commands.
- 💡 **Likely mix-up:** After Q011, Q014 and Q022, "Deployment Manager" feels like the answer for anything about environments. But Deployment Manager **builds infrastructure**. It doesn't **move deployed app code**.

**📌 When to use it:** Use Deployment Manager when you want to build the same networks, VMs and other resources again and again from a written plan.
🏢 **Office example:** Using a floor plan to build identical rooms in a new branch. The plan doesn't move the people in.

### ❌ D
> **D.** Deploy your application again using gcloud and specify the project parameter with the new project name to create the new project.

**Why it's wrong:**
- ✔️ Deploying again with `--project` is half right. That's **step 2**.
- ❌ But **`gcloud app deploy` never creates a project.** If the project doesn't exist, the deploy **fails**.

**📌 When to use it:** Use `gcloud app deploy --project=NAME` when the target project already exists and you want to put your app there.
🏢 **Office example:** Sending the moving truck to a branch address. It only works if the building is already there.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's storefront API runs on App Engine in **`shopnow-dev`**. QA signs off, and it's time for **`shopnow-prod`**.

```bash
# ① Create the production project
gcloud projects create shopnow-prod --name="ShopNow Production" --organization=123456789012

# ①b Link billing (Q007) and set up App Engine (region is permanent!)
gcloud billing projects link shopnow-prod --billing-account=01A2B3-C4D5E6-F7G8H9
gcloud app create --project=shopnow-prod --region=us-central

# ② Deploy the same tested code (same app.yaml)
gcloud app deploy app.yaml --project=shopnow-prod
```

**Better long term:** a **Cloud Build** pipeline deploys the same commit to `shopnow-dev` first, then to `shopnow-prod` after approval. The team never deploys by hand.

**Keep prod separate:**
| | `shopnow-dev` | `shopnow-prod` |
|---|---|---|
| Who can deploy | All developers | Only the release pipeline / leads |
| Database | Test Cloud SQL with fake orders | Real Cloud SQL with customer orders |
| Billing | Small budget alert | Production budget + alerts |

**🎬 With the other options:**
- **B / C:** Maria searches for a "copy app" feature that doesn't exist and loses an afternoon. ❌
- **D:** `gcloud app deploy --project=shopnow-prod` fails because the project doesn't exist yet. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **New environment for App Engine = ① create the project → ② deploy the code to it.**
  🧠 *"**Build the house, then move in.**" Deploying never builds the house.*
- **App Engine apps are never "copied" between projects.** You **redeploy the source code**.
- **`gcloud app deploy --project=X`** only works if **project X already exists** (with App Engine set up via `gcloud app create`).
- **Deployment Manager builds infrastructure from a plan.** It doesn't **move** a running app.
- Keep **dev and prod in separate projects** for safety, permissions and billing.

# Q075: Listing the Enabled APIs of a Project (gcloud services list --project)

**Topic:** gcloud CLI (project name vs project ID, gcloud services list, --available, gcloud init/info/describe)

## ❓ Question
> You need to produce a list of the enabled Google Cloud Platform APIs for a GCP project using the gcloud command line in the Cloud Shell. The project name is my-project. What should you do?
>
> **A.** Run gcloud projects list to get the project ID, and then run gcloud services list --project <project ID>.
>
> **B.** Run gcloud init to set the current project to my-project, and then run gcloud services list --available.
>
> **C.** Run gcloud info to view the account value, and then run gcloud services list --account <Account>.
>
> **D.** Run gcloud projects describe <project ID> to verify the project value, and then run gcloud services list --available.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You work in Cloud Shell with a project named my-project.
- **What you must achieve:** Get a list of the APIs (Google services) that are enabled in that project.
- **The limits:** Use the gcloud command line.
- **What they're really asking:** Which gcloud command lists the enabled APIs for my-project?

**Clues in the question:**
- "**The project name is my-project**": gcloud commands need the **project ID**, which can differ from the name. So first look up the ID.
- "**list of the enabled … APIs**": `gcloud services list` shows **enabled** services by default.
- Watch out for `--available`: that lists **all APIs you could enable**, not the enabled ones.

**Exam topic:** gcloud / project setup.

---

## 📚 Key Terms Explained

### 1️⃣ Project name vs project ID 🔑
- **What it is:** The **name** is a friendly label you can change and that doesn't have to be unique. The **project ID** is the **unique, permanent identifier** gcloud uses.
- **Looks like:**
  ```
  PROJECT_ID          NAME         PROJECT_NUMBER
  my-project-381204   my-project   559012345678
  ```
- **Not to be confused with:** each other. `my-project` (name) may have ID `my-project-381204`.
- **Analogy:** 🏷️ A person's **nickname** vs their **employee number**.
- **In the online store:** Name "ShopNow Prod", ID `shopnow-prod-4821`.

### 2️⃣ `gcloud projects list`
- **What it is:** Shows every project you can see, with its **ID, name and number**.
- **Looks like:** `gcloud projects list --filter="name:my-project"`
- **Analogy:** 📇 The **staff directory**: look up a nickname to find the employee number.

### 3️⃣ `gcloud services list` 🔑
- **What it is:** Lists the APIs (services) **enabled** in a project. Add `--available` to list **all** APIs that **could** be enabled.
- **Looks like:**
  ```bash
  gcloud services list --project=my-project-381204
  # NAME                          TITLE
  # compute.googleapis.com        Compute Engine API
  # storage.googleapis.com        Cloud Storage API
  ```
- **Not to be confused with:** `--available` (a catalog of hundreds of APIs, mostly not enabled).
- **Analogy:** 💡 Enabled = the **light switches that are ON**. `--available` = **every switch in the building**.

### 4️⃣ `gcloud init`, `gcloud info`, `gcloud projects describe`
- **What it is:** `init` = interactive setup (account, default project). `info` = shows your gcloud setup (account, config paths). `projects describe` = shows one project's details.
- **Not to be confused with:** listing APIs. None of them lists enabled APIs.

### 🔗 How they fit together
```
 name "my-project" ──gcloud projects list──► ID my-project-381204
                                              │
                    gcloud services list --project my-project-381204
                                              ▼
                                   ✅ ENABLED APIs only
 (--available → every API you COULD enable ❌)
```

---

## 🌍 Real-World Scenario

During an audit or before a migration, an engineer is asked "which APIs are turned on in project X?". They look up the project ID from the name, then run `gcloud services list --project <ID>`, and paste the output into the report.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run gcloud projects list to get the project ID, and then run gcloud services list --project <project ID>.

**Why it's correct:**
- ✔️ "**Run gcloud projects list to get the project ID**" matches "**The project name is my-project**": gcloud needs the ID, and this finds it from the name.
- ✔️ "**gcloud services list --project <project ID>**" matches "**list of the enabled … APIs**": without `--available`, it lists only the **enabled** APIs of that project.

📌 **When to use it:** Use it when you know a project's friendly name and need the list of features turned on in it.
🏢 **Office example:** Looking up a colleague's employee number in the directory, then asking IT which systems are switched on for them.

### ❌ B
> **B.** Run gcloud init to set the current project to my-project, and then run gcloud services list --available.

**Wrong words:**
- ❌ "**gcloud init to set the current project to my-project**": init is a full interactive setup, and `my-project` is the **name**, while it needs the **ID**.
- ❌ "**--available**": lists **every API you could enable**, not the enabled ones.

📌 **When to use it:** Use `gcloud services list --available` when you want to browse which APIs exist before enabling one.
🏢 **Office example:** Reading the catalog of every service IT offers, when you wanted the ones you already use.

### ❌ C
> **C.** Run gcloud info to view the account value, and then run gcloud services list --account <Account>.

**Wrong words:**
- ❌ "**gcloud info to view the account value**": the **account** is **who you are**, not which project to look at.
- ❌ "**gcloud services list --account <Account>**": `--account` only chooses which login to run the command as. It doesn't pick the project.

📌 **When to use it:** Use `gcloud info` to check which account and settings your gcloud is using.
🏢 **Office example:** Checking whose badge you're wearing, when the question was which room's lights are on.

### ❌ D
> **D.** Run gcloud projects describe <project ID> to verify the project value, and then run gcloud services list --available.

**Wrong words:**
- ✔️ "gcloud projects describe <project ID>" is a valid command to check a project.
- ❌ "**gcloud services list --available**": again, the **catalog** of all APIs, not the **enabled** ones.

📌 **When to use it:** Use `gcloud projects describe` when you need details (number, parent, state) of one project.
🏢 **Office example:** Reading an employee's HR file, then reading the whole IT catalog instead of their active systems.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects list --filter="name:ShopNow Prod"
# PROJECT_ID          NAME          PROJECT_NUMBER
# shopnow-prod-4821   ShopNow Prod  559012345678

gcloud services list --project=shopnow-prod-4821
# compute.googleapis.com       Compute Engine API
# sqladmin.googleapis.com      Cloud SQL Admin API
# pubsub.googleapis.com        Cloud Pub/Sub API
# run.googleapis.com           Cloud Run Admin API
```

Security review sees exactly which APIs ShopNow production uses.

---

## 🧠 Key Takeaways / Memory Tips

- **Enabled APIs → `gcloud services list --project <ID>`.** `--available` = every API you **could** enable.
- **Name ≠ ID.** gcloud uses the **project ID**; find it with `gcloud projects list`.
- `--account` picks **who** runs the command, not **which project**.
  🧠 *"**`services list` = switches ON. `--available` = every switch.**"*
- Related: **Q031** (enable an API), **Q034** (gcloud projects get-iam-policy).

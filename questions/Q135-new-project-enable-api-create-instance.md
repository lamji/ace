# Q135: Create a VM in a Project That Doesn't Exist Yet (Create Project → Enable API → Create Instance)

**Topic:** Resource Manager / Compute Engine (project creation, enabling APIs, gcloud --project)

## ❓ Question
> You need to create a Compute Engine instance in a new project that doesn't exist yet. What should you do?
>
> **A.** Using the Cloud SDK, create a new project, enable the Compute Engine API in that project, and then create the instance specifying your new project.
>
> **B.** Enable the Compute Engine API in the Cloud Console, use the Cloud SDK to create the instance, and then use the --project flag to specify a new project.
>
> **C.** Using the Cloud SDK, create the new instance, and use the --project flag to specify the new project. Answer yes when prompted by Cloud SDK to enable the Compute Engine API.
>
> **D.** Enable the Compute Engine API in the Cloud Console. Go to the Compute Engine section of the Console to create a new instance, and look for the Create In A New Project option in the creation form.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** The project you need does not exist yet.
- **What you must achieve:** Create a Compute Engine VM in a new project.
- **The limits:** None stated.
- **What they're really asking:** What steps are needed, and in what order?

**Clues in the question:**
- "**new project that doesn't exist yet**": step 1 must be **create the project**.
- APIs are enabled **per project**, so enable Compute Engine **in that project**, then create the VM there.

**Exam topic:** Resource management.

---

## 📚 Key Terms Explained

### 1. Enabling an API 🔑
- **What it is:** Each project must **turn on** a service's API before using it. It's per project.
- **Looks like:** `gcloud services enable compute.googleapis.com --project=shop-new`
- **Not to be confused with:** IAM permission.
- **Analogy:** 🔌 Plugging in a machine in **that** office before using it.
- **In the online store:** Compute Engine enabled in each new ShopNow project.

### 2. --project flag
- **What it is:** Tells gcloud which **existing** project to use for this command.
- **Looks like:** `gcloud compute instances create web-1 --project=shop-new`
- **Not to be confused with:** creating a project.
- **Analogy:** 🏷️ The address label on a package, which must point to a real office.
- **In the online store:** Run commands against prod without switching config.

### 🔗 How they fit together
```
 1. gcloud projects create shop-new
 2. (link billing) + gcloud services enable compute.googleapis.com --project=shop-new
 3. gcloud compute instances create web-1 --project=shop-new ✅
```

---

## 🌍 Real-World Scenario

A team lead needs a VM for a new initiative. They run `gcloud projects create`, link billing, enable the Compute Engine API in the new project, then create the VM with `--project`.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Using the Cloud SDK, create a new project, enable the Compute Engine API in that project, and then create the instance specifying your new project.

**Why it's correct:**
- ✔️ "**create a new project**" matches "**a new project that doesn't exist yet**": it must exist first.
- ✔️ "**enable the Compute Engine API in that project**": APIs are enabled per project.
- ✔️ "**create the instance specifying your new project**" matches "**create a Compute Engine instance in a new project**".

📌 **When to use it:** Use it whenever you start work in a brand-new place: create it, turn on what you need, then use it.
🏢 **Office example:** Opening the new office, plugging in the equipment, then setting up the desk.

### ❌ B
> **B.** Enable the Compute Engine API in the Cloud Console, use the Cloud SDK to create the instance, and then use the --project flag to specify a new project.

**Wrong words:**
- ❌ "**Enable the Compute Engine API in the Cloud Console**" (before the project exists): it gets enabled in some other project.
- ❌ "**--project flag to specify a new project**": the flag can't create a project.

📌 **When to use it:** Use `--project` for projects that already exist.
🏢 **Office example:** Addressing a package to an office that hasn't been built.

### ❌ C
> **C.** Using the Cloud SDK, create the new instance, and use the --project flag to specify the new project. Answer yes when prompted by Cloud SDK to enable the Compute Engine API.

**Wrong words:**
- ❌ "**create the new instance, and use the --project flag to specify the new project**": the project doesn't exist, so the command fails. gcloud won't create the project for you.

📌 **When to use it:** Use the yes-prompt to enable an API in an existing project.
🏢 **Office example:** Asking the courier to build the office when the package arrives.

### ❌ D
> **D.** Enable the Compute Engine API in the Cloud Console. Go to the Compute Engine section of the Console to create a new instance, and look for the Create In A New Project option in the creation form.

**Wrong words:**
- ❌ "**Create In A New Project option**": no such option exists in the VM creation form.

📌 **When to use it:** **Never use this.** Use A.
🏢 **Office example:** Looking for a "build new office" checkbox on a desk order form.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud projects create shopnow-promo-2027 --folder=RETAIL
gcloud billing projects link shopnow-promo-2027 --billing-account=01AB23-CD45EF-678901
gcloud services enable compute.googleapis.com --project=shopnow-promo-2027
gcloud compute instances create promo-web-1 --zone=us-central1-a --project=shopnow-promo-2027
```

---

## 🧠 Key Takeaways / Memory Tips

- **Order: create project → (billing) → enable API in it → create resources.**
- `--project` only points to existing projects.
  🧠 *"**Build the office, plug it in, then set up the desk.**"*
- Related: **Q110** (new prod project), **Q180**, **Q181** (enable API first).

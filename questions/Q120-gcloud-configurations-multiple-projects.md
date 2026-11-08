# Q120: Managing Multiple Projects in the CLI With the Fewest Steps (One Configuration per Project + Activate)

**Topic:** gcloud CLI (configurations, gcloud config configurations activate, gcloud init)

## ❓ Question
> You need to manage multiple Google Cloud projects in the fewest steps possible. You want to configure the Google Cloud SDK command line interface (CLI) so that you can easily manage multiple projects. What should you do?
>
> **A.** 1. Create a configuration for each project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.
>
> **B.** 1. Create a configuration for each project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project
>
> **C.** 1. Use the default configuration for one project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.
>
> **D.** 1. Use the default configuration for one project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You manage several projects with the gcloud CLI.
- **What you must achieve:** Switch between projects easily.
- **The limits:** Fewest steps.
- **What they're really asking:** How do you set up gcloud for quick switching?

**Clues in the question:**
- "**multiple Google Cloud projects**": make **one configuration per project**.
- "**fewest steps**" + "**easily manage**": switching = **one command**: `gcloud config configurations activate <name>`. Running `gcloud init` again each time is more steps.

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. gcloud configuration 🔑 (review from Q084)
- **What it is:** A **named, saved set of settings** (account, project, region/zone). Switch between them with one command.
- **Looks like:** `gcloud config configurations create prod` → `gcloud config set project shopnow-prod` → `gcloud config configurations activate prod`
- **Not to be confused with:** a project.
- **Analogy:** 🗂️ **Saved printer profiles** for each floor.
- **In the online store:** `dev`, `staging`, `prod` configurations.

### 2. gcloud init
- **What it is:** An **interactive wizard** that logs you in and asks which project, region and zone to use. Re-running it means answering the questions again.
- **Looks like:** `gcloud init` → "Pick configuration… Pick project…"
- **Not to be confused with:** a quick switch.
- **Analogy:** 📝 Filling in the **whole setup form** again.
- **In the online store:** Used once on a new laptop.

### 3. default configuration
- **What it is:** The configuration gcloud creates first, named `default`.
- **Looks like:** `gcloud config configurations list` → `default  True`
- **Not to be confused with:** a setup for many projects.
- **Analogy:** 🗂️ The one printer profile that came out of the box.
- **In the online store:** Fine for a single project.

### 🔗 How they fit together
```
 gcloud config configurations create dev   (project shopnow-dev)
 gcloud config configurations create prod  (project shopnow-prod)
 switch: gcloud config configurations activate prod ✅ (1 command)
```

---

## 🌍 Real-World Scenario

A consultant manages five client projects. They create a gcloud **configuration** for each (with the right account, project and region) and switch with `gcloud config configurations activate client-b`. Commands go to the right project.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** 1. Create a configuration for each project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.

**Why it's correct:**
- ✔️ "**Create a configuration for each project**" matches "**manage multiple Google Cloud projects**": each project's settings are saved once.
- ✔️ "**Activate the appropriate configuration**" matches "**fewest steps possible**" + "**easily manage**": switching is one command.

📌 **When to use it:** Use it when you regularly switch between several places and want each one's settings saved.
🏢 **Office example:** Saved printer profiles for each floor: pick one and print.

### ❌ B
> **B.** 1. Create a configuration for each project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project

**Wrong words:**
- ✔️ "Create a configuration for each project" is right.
- ❌ "**Use gcloud init to update the configuration values**": re-runs the setup wizard every time, which is more steps than activating.

📌 **When to use it:** Use gcloud init when you first set up gcloud or create a new configuration interactively.
🏢 **Office example:** Having saved profiles, but filling in the setup form again anyway.

### ❌ C
> **C.** 1. Use the default configuration for one project you need to manage. 2. Activate the appropriate configuration when you work with each of your assigned Google Cloud projects.

**Wrong words:**
- ❌ "**Use the default configuration for one project**": you'd only have one configuration, so "activate the appropriate configuration" doesn't work for the others.

📌 **When to use it:** Use the default configuration when you only manage one project.
🏢 **Office example:** Keeping one printer profile and expecting to pick others that don't exist.

### ❌ D
> **D.** 1. Use the default configuration for one project you need to manage. 2. Use gcloud init to update the configuration values when you need to work with a non-default project.

**Wrong words:**
- ❌ "**default configuration**" + "**gcloud init**": you'd re-enter settings every time you switch. The most steps.

📌 **When to use it:** Use it only for a single project that rarely changes.
🏢 **Office example:** Re-filling the whole printer setup form every time you change floors.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud config configurations create shop-dev  && gcloud config set project shopnow-dev
gcloud config configurations create shop-prod && gcloud config set project shopnow-prod
gcloud config configurations activate shop-prod
gcloud compute instances list   # lists prod VMs
```

---

## 🧠 Key Takeaways / Memory Tips

- **Many projects → one configuration each, switch with `activate`.**
- `gcloud init` = setup wizard, not a quick switch.
  🧠 *"**Create once, activate to switch.**"*
- Related: **Q084** (configurations in a daily script), **Q075** (project ID vs name).

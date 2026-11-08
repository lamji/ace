# Q138: Stop Typing the Zone on Every gcloud Command (gcloud config set compute/zone)

**Topic:** gcloud CLI (default properties, compute/zone)

## ❓ Question
> You have downloaded and installed the gcloud command line interface (CLI) and have authenticated with your Google Account. Most of your Compute Engine instances in your project run in the europe-west1-d zone. You want to avoid having to specify this zone with each CLI command when managing these instances. What should you do?
>
> **A.** Set the europe-west1-d zone as the default zone using the gcloud config subcommand.
>
> **B.** In the Settings page for Compute Engine under Default location, set the zone to europe-west1-d.
>
> **C.** In the CLI installation directory, create a file called default.conf containing zone=europe-west1-d.
>
> **D.** Create a Metadata entry on the Compute Engine page with key compute/zone and value europe-west1-d.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Most of your VMs are in the europe-west1-d zone.
- **What you must achieve:** Stop having to type the zone in every gcloud command.
- **The limits:** None stated.
- **What they're really asking:** How do you set a default zone?

**Clues in the question:**
- "**avoid having to specify this zone with each CLI command**": a **gcloud property**, set with `gcloud config set compute/zone europe-west1-d`.

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. gcloud config properties 🔑
- **What it is:** Saved defaults in your active gcloud **configuration** (project, account, region, zone).
- **Looks like:** `gcloud config set compute/zone europe-west1-d`
- **Not to be confused with:** console settings.
- **Analogy:** 🗂️ A saved preference in your printer profile.
- **In the online store:** ShopNow devs default to their main zone.

### 2. Project metadata compute/zone
- **What it is:** A project-level default that the console and some tools read. The **CLI uses its own config first**, and creating metadata isn't the documented way to set the CLI default.
- **Looks like:** `gcloud compute project-info add-metadata --metadata google-compute-default-zone=europe-west1-d`
- **Not to be confused with:** the CLI's config.
- **Analogy:** 🏢 An office-wide notice board.
- **In the online store:** Default for new console users.

### 🔗 How they fit together
```
 gcloud config set compute/zone europe-west1-d ✅
 gcloud compute instances stop web-1   ← no --zone needed
```

---

## 🌍 Real-World Scenario

An engineer working mostly in Belgium runs `gcloud config set compute/zone europe-west1-d` once. From then on, `gcloud compute instances list/stop/ssh` works without `--zone`.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Set the europe-west1-d zone as the default zone using the gcloud config subcommand.

**Why it's correct:**
- ✔️ "**default zone using the gcloud config subcommand**" matches "**avoid having to specify this zone with each CLI command**": `gcloud config set compute/zone` saves it for the CLI.

📌 **When to use it:** Use it when you almost always work in the same place.
🏢 **Office example:** Saving your floor as the default in your printer profile.

### ❌ B
> **B.** In the Settings page for Compute Engine under Default location, set the zone to europe-west1-d.

**Wrong words:**
- ❌ "**Settings page for Compute Engine … Default location**": this sets a project default for the console, and doesn't directly set your CLI configuration.

📌 **When to use it:** Use it to set defaults for console users in the project.
🏢 **Office example:** Changing the office notice board instead of your own printer profile.

### ❌ C
> **C.** In the CLI installation directory, create a file called default.conf containing zone=europe-west1-d.

**Wrong words:**
- ❌ "**create a file called default.conf**": gcloud doesn't read such a file. Its settings live in `~/.config/gcloud/configurations/`, managed with `gcloud config`.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Writing your preference on a sticky note the printer never reads.

### ❌ D
> **D.** Create a Metadata entry on the Compute Engine page with key compute/zone and value europe-west1-d.

**Wrong words:**
- ❌ "**Metadata entry on the Compute Engine page with key compute/zone**": that isn't the CLI setting (the project metadata key is `google-compute-default-zone`).

📌 **When to use it:** Use project metadata for project-wide defaults.
🏢 **Office example:** Posting your preference on the building notice board.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud config set compute/zone europe-west1-d
gcloud config set compute/region europe-west1
gcloud compute ssh shop-eu-web-1   # no --zone needed
```

---

## 🧠 Key Takeaways / Memory Tips

- **CLI defaults → `gcloud config set compute/zone|region|project`.**
  🧠 *"**Tired of --zone? gcloud config set it.**"*
- Related: **Q120**, **Q084** (configurations), **Q189** (container/cluster default).

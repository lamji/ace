# Q265: New Laptop: Before gcloud compute instances list (gcloud auth login + gcloud config set project)

**Topic:** gcloud CLI (initial setup)

## ❓ Question
> You just installed the Google Cloud CLI on your new corporate laptop. You need to list the existing instances of your company on Google Cloud. What must you do before you run the gcloud compute instances list command? (Choose two.)
>
> **A.** Run gcloud auth login, enter your login credentials in the dialog window, and paste the received login token to gcloud CLI.
>
> **B.** Create a Google Cloud service account, and download the service account key. Place the key file in a folder on your machine where gcloud CLI can find it.
>
> **C.** Download your Cloud Identity user account key. Place the key file in a folder on your machine where gcloud CLI can find it.
>
> **D.** Run gcloud config set compute/zone $my_zone to set the default zone for gcloud CLI.
>
> **E.** Run gcloud config set project $my_project to set the default project for gcloud CLI.

**My answer:** — (didn't know)
**Correct answer:** A, E
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Fresh gcloud install. What two things are **required** before listing VMs?

**Clues in the question:**
- You must be **signed in** → `gcloud auth login`.
- gcloud must know **which project** → `gcloud config set project`.
- Zone is optional for `list` (it lists all zones).

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. gcloud auth login 🔑
- **What it is:** Signs gcloud in with **your user account** through a browser.
- **Looks like:** `gcloud auth login`
- **Not to be confused with:** service account keys.
- **Analogy:** 🪪 Showing your badge at the door.
- **In the online store:** Dev laptop setup.

### 2. gcloud config set project
- **What it is:** Sets the default project for commands.
- **Looks like:** `gcloud config set project shopnow-prod`
- **Not to be confused with:** zone.
- **Analogy:** 🏢 Choosing which building.
- **In the online store:** —

### 🔗 How they fit together
```
 gcloud auth login ✅ → gcloud config set project ✅ → gcloud compute instances list
```

---

## 🌍 Real-World Scenario

A new engineer installs gcloud, runs **`gcloud auth login`**, then **`gcloud config set project shopnow-prod`**, and lists VMs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run gcloud auth login, enter your login credentials in the dialog window, and paste the received login token to gcloud CLI.

**Why it's correct:**
- ✔️ "**Run gcloud auth login, enter your login credentials**" matches "**before you run the gcloud compute instances list command**": gcloud needs your identity.

📌 **When to use it:** Use it the first time you use gcloud on a new computer.
🏢 **Office example:** Signing in at reception with your own badge.

### ❌ B
> **B.** Create a Google Cloud service account, and download the service account key. Place the key file in a folder on your machine where gcloud CLI can find it.

**Wrong words:**
- ❌ "**Create a Google Cloud service account, and download the service account key**": unnecessary and less secure for a person.

📌 **When to use it:** Use service account keys only for machines that can't use other methods.
🏢 **Office example:** Making a robot badge for yourself.

### ❌ C
> **C.** Download your Cloud Identity user account key. Place the key file in a folder on your machine where gcloud CLI can find it.

**Wrong words:**
- ❌ "**Download your Cloud Identity user account key**": user accounts don't have downloadable keys.

📌 **When to use it:** **Not a real thing.**
🏢 **Office example:** Asking for a copy of your fingerprint file.

### ❌ D
> **D.** Run gcloud config set compute/zone $my_zone to set the default zone for gcloud CLI.

**Wrong words:**
- ❌ "**set the default zone**": optional; `instances list` shows all zones.

📌 **When to use it:** Use it to avoid typing --zone on zone-specific commands.
🏢 **Office example:** Picking a favorite floor before you've entered the building.

### ✅ E
> **E.** Run gcloud config set project $my_project to set the default project for gcloud CLI.

**Why it's correct:**
- ✔️ "**Run gcloud config set project**" matches "**list the existing instances of your company**": gcloud must know which project to look in.

📌 **When to use it:** Use it to tell your tools which company area you're working in.
🏢 **Office example:** Choosing which office building you want to look around in.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud auth login
gcloud config set project shopnow-prod
gcloud compute instances list
```

---

## 🧠 Key Takeaways / Memory Tips

- **New gcloud install → `gcloud auth login` + `gcloud config set project`.** (Or `gcloud init`, which does both.)
  🧠 *"**Who are you? Which project?**"*
- Related: **Q170**, **Q189**, **Q138**.

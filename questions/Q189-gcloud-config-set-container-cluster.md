# Q189: Make Future CLI Commands Target the 'dev' Cluster by Default (gcloud config set container/cluster dev)

**Topic:** gcloud CLI (configuration defaults)

## ❓ Question
> You are assigned to maintain a Google Kubernetes Engine (GKE) cluster named 'dev' that was deployed on Google Cloud. You want to manage the GKE configuration using the command line interface (CLI). You have just downloaded and installed the Cloud SDK. You want to ensure that future CLI commands by default address this specific cluster What should you do?
>
> **A.** Use the command gcloud config set container/cluster dev.
>
> **B.** Use the command gcloud container clusters update dev.
>
> **C.** Create a file called gke.default in the ~/.gcloud folder that contains the cluster name.
>
> **D.** Create a file called defaults.json in the ~/.gcloud folder that contains the cluster name.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You maintain a GKE cluster named dev and just installed the Cloud SDK.
- **What you must achieve:** Future command-line commands should target this cluster by default.
- **The limits:** None stated.
- **What they're really asking:** What do you set so gcloud and kubectl use the dev cluster by default?

**Clues in the question:**
- "**future CLI commands by default address this specific cluster**" → `gcloud config set container/cluster dev` (like `compute/zone` in Q138).

**Exam topic:** gcloud CLI.

---

## 📚 Key Terms Explained

### 1. gcloud config set 🔑 (review from Q138)
- **What it is:** Saves a **default value** in your active gcloud configuration.
- **Looks like:** `gcloud config set container/cluster dev`
- **Not to be confused with:** changing the cluster.
- **Analogy:** 📌 Pinning your usual room number.
- **In the online store:** Default ShopNow cluster.

### 🔗 How they fit together
```
 gcloud config set container/cluster dev ✅
 gcloud container clusters describe → uses dev automatically
```

---

## 🌍 Real-World Scenario

An engineer who manages the `dev` cluster sets it as the default so they don't type `--cluster=dev` every time.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Use the command gcloud config set container/cluster dev.

**Why it's correct:**
- ✔️ "**gcloud config set container/cluster dev**" matches "**future CLI commands by default address this specific cluster**".

📌 **When to use it:** Use it when you work with the same thing every day and don't want to name it each time.
🏢 **Office example:** Setting your phone's speed-dial to your usual department.

### ❌ B
> **B.** Use the command gcloud container clusters update dev.

**Wrong words:**
- ❌ "**gcloud container clusters update dev**": changes the cluster's settings. It doesn't set a CLI default.

📌 **When to use it:** Use it to change cluster settings.
🏢 **Office example:** Remodeling the room instead of saving its number.

### ❌ C
> **C.** Create a file called gke.default in the ~/.gcloud folder that contains the cluster name.

**Wrong words:**
- ❌ "**gke.default in the ~/.gcloud folder**": gcloud doesn't read such a file.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A sticky note gcloud never reads.

### ❌ D
> **D.** Create a file called defaults.json in the ~/.gcloud folder that contains the cluster name.

**Wrong words:**
- ❌ "**defaults.json in the ~/.gcloud folder**": not a real gcloud mechanism.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Another note nobody reads.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud config set project shopnow-dev
gcloud config set compute/zone us-central1-a
gcloud config set container/cluster dev
```

---

## 🧠 Key Takeaways / Memory Tips

- **CLI default → `gcloud config set <section/property> <value>`.**
  🧠 *"**Default? config set.**"*
- Related: **Q138**, **Q170**.

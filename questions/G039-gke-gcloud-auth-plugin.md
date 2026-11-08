# G039: kubectl Fails With "gke-gcloud-auth-plugin not found" (Install the Plugin, Then Get Credentials)

**Topic:** GKE (kubectl install and authentication)
**Exam guide section:** 2.1 Installing and configuring the command-line interface (CLI) for Kubernetes (kubectl)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You installed kubectl on a new workstation and ran gcloud container clusters get-credentials for your GKE cluster. When you run kubectl get pods, you receive an error saying that gke-gcloud-auth-plugin was not found. What should you do?
>
> **A.** Install gke-gcloud-auth-plugin (for example, with gcloud components install gke-gcloud-auth-plugin), then run gcloud container clusters get-credentials again.
>
> **B.** Create a service account key and paste it into the kubeconfig file.
>
> **C.** Disable authentication on the GKE cluster's control plane.
>
> **D.** Reinstall the Google Cloud CLI without kubectl.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** On a new computer you installed kubectl (the Kubernetes command-line tool) and pointed it at your GKE cluster with `get-credentials`.
- **What you must achieve:** Make `kubectl get pods` work.
- **The limits:** The error says a piece called `gke-gcloud-auth-plugin` is missing.
- **What they're really asking:** What does kubectl need to sign in to GKE, and how do you install it?

**Clues in the question:**
- "**gke-gcloud-auth-plugin was not found**": kubectl uses this plugin to get Google credentials for GKE (required for recent versions).
- Install the plugin, then refresh the kubeconfig with `get-credentials`.

**Exam topic:** GKE tooling (exam guide section 2.1).

---

## 📚 Key Terms Explained

### 1. kubectl
- **What it is:** The command-line tool for Kubernetes clusters.
- **Looks like:** `kubectl get pods -n shop`
- **Not to be confused with:** gcloud, which manages Google Cloud resources, including creating clusters.
- **Analogy:** 🎮 The remote control for your cluster.
- **In the online store:** Developers check ShopNow Pods.

### 2. gke-gcloud-auth-plugin 🔑
- **What it is:** A small helper that kubectl calls to fetch a short-lived Google access token for GKE. It's required since Kubernetes 1.26.
- **Looks like:** `gcloud components install gke-gcloud-auth-plugin` (or `sudo apt-get install google-cloud-cli-gke-gcloud-auth-plugin`)
- **Not to be confused with:** A service account key.
- **Analogy:** 🪪 The badge reader that lets your remote control talk to the building.
- **In the online store:** Lets ShopNow devs use kubectl with their Google login.

### 🔗 How they fit together
```
 kubectl ─needs─► gke-gcloud-auth-plugin ─► gcloud login token ─► GKE API ✅
```

---

## 🌍 Real-World Scenario

A new developer gets the plugin error on day one. They install the plugin, rerun `get-credentials`, and `kubectl get pods` works using their own Google identity. No keys are involved.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Install gke-gcloud-auth-plugin (for example, with gcloud components install gke-gcloud-auth-plugin), then run gcloud container clusters get-credentials again.

**Why it's correct:**
- ✔️ "**Install gke-gcloud-auth-plugin**" matches "**gke-gcloud-auth-plugin was not found**".
- ✔️ "**run … get-credentials again**" refreshes the kubeconfig to use the plugin.

📌 **When to use it:** Use it when the command tool says a sign-in helper is missing.
🏢 **Office example:** Installing the missing badge reader so your remote control can open the door.

### ❌ B
> **B.** Create a service account key and paste it into the kubeconfig file.

**Wrong words:**
- ❌ "**service account key … kubeconfig**": creates a long-lived secret and swaps your identity for a robot's. Bad practice.

📌 **When to use it:** Avoid it. Use the auth plugin with your own identity.
🏢 **Office example:** Taping a master key to the remote control.

### ❌ C
> **C.** Disable authentication on the GKE cluster's control plane.

**Wrong words:**
- ❌ "**Disable authentication**": you can't, and it would be extremely unsafe.

📌 **When to use it:** Never use this.
🏢 **Office example:** Removing the lock from the front door.

### ❌ D
> **D.** Reinstall the Google Cloud CLI without kubectl.

**Wrong words:**
- ❌ "**Reinstall … without kubectl**": you need kubectl and the plugin. This removes the tool.

📌 **When to use it:** Not expected to help.
🏢 **Office example:** Throwing away the remote control.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** onboarding: `gcloud components install kubectl gke-gcloud-auth-plugin` → `gcloud container clusters get-credentials shop-prod --region=us-central1` → `kubectl get pods -n shop`.

---

## 🧠 Key Takeaways / Memory Tips

- **"gke-gcloud-auth-plugin not found" → install the plugin, rerun get-credentials.**
  🧠 *"**kubectl needs its badge reader.**"*
- Related: **Q241**, **Q189**.

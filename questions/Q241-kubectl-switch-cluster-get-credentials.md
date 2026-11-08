# Q241: kubectl Only Shows prod-cluster Nodes; Check dev-cluster (gcloud container clusters get-credentials dev-cluster)

**Topic:** GKE (kubectl contexts, get-credentials)

## ❓ Question
> You used the gcloud container clusters command to create two Google Cloud Kubernetes (GKE) clusters: prod-cluster and dev-cluster. • prod-cluster is a standard cluster. • dev-cluster is an auto-pilot cluster. When you run the kubectl get nodes command, you only see the nodes from prod-cluster. Which commands should you run to check the node status for dev-cluster?
>
> **A.** gcloud container clusters get-credentials dev-cluster kubectl get nodes
>
> **B.** gcloud container clusters update -generate-password dev-cluster kubectl get nodes
>
> **C.** kubectl config set-context dev-cluster kubectl cluster-info
>
> **D.** kubectl config set-credentials dev-cluster kubectl cluster-info

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You created two GKE clusters with gcloud: prod-cluster (Standard) and dev-cluster (Autopilot). kubectl get nodes only shows prod-cluster's nodes.
- **What you must achieve:** See the node status for dev-cluster.
- **The limits:** None stated.
- **What they're really asking:** Which commands point kubectl at dev-cluster and list its nodes?

**Clues in the question:**
- kubectl talks to whichever cluster is in its current **context**. `gcloud container clusters get-credentials dev-cluster` adds dev-cluster's entry to kubeconfig and **switches** to it.
- Then `kubectl get nodes` shows **node status**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. get-credentials 🔑
- **What it is:** Writes a cluster's address and login details into `~/.kube/config` and makes it the current context.
- **Looks like:** `gcloud container clusters get-credentials dev-cluster --region=us-central1`
- **Not to be confused with:** creating a cluster.
- **Analogy:** 📇 Adding a building to your keyring and picking its key.
- **In the online store:** Switch from prod to dev.

### 2. kubeconfig context
- **What it is:** An entry in kubeconfig naming a cluster + user. kubectl uses the **current** one.
- **Looks like:** `kubectl config get-contexts`
- **Not to be confused with:** —
- **Analogy:** 🔑 The key currently in your hand.
- **In the online store:** —

### 🔗 How they fit together
```
 kubectl → context: prod-cluster
 get-credentials dev-cluster → context: dev-cluster ✅ → kubectl get nodes
```

---

## 🌍 Real-World Scenario

An engineer sees only prod nodes. They run `get-credentials dev-cluster`, then `kubectl get nodes` lists the Autopilot nodes.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** gcloud container clusters get-credentials dev-cluster kubectl get nodes

**Why it's correct:**
- ✔️ "**gcloud container clusters get-credentials dev-cluster**" matches "**you only see the nodes from prod-cluster**": it switches kubectl to dev-cluster.
- ✔️ "**kubectl get nodes**" matches "**check the node status for dev-cluster**".

📌 **When to use it:** Use it whenever you need to start working with a different Kubernetes cluster.
🏢 **Office example:** Taking the right building's key off the hook before going in.

### ❌ B
> **B.** gcloud container clusters update -generate-password dev-cluster kubectl get nodes

**Wrong words:**
- ❌ "**update -generate-password**": not a real way to switch clusters (legacy basic auth, and the flag is wrong).

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Asking for a new password to a building you just need the key for.

### ❌ C
> **C.** kubectl config set-context dev-cluster kubectl cluster-info

**Wrong words:**
- ❌ "**kubectl config set-context dev-cluster**": creates/edits a context entry but has no credentials for dev-cluster, and doesn't switch to it (`use-context` does).
- ❌ "**kubectl cluster-info**": doesn't show node status.

📌 **When to use it:** Use set-context to edit an existing context's settings.
🏢 **Office example:** Writing a new label on an empty key hook.

### ❌ D
> **D.** kubectl config set-credentials dev-cluster kubectl cluster-info

**Wrong words:**
- ❌ "**kubectl config set-credentials**": sets a user entry manually; doesn't fetch GKE credentials.
- ❌ "**cluster-info**": not node status.

📌 **When to use it:** Use it for custom kubeconfig users.
🏢 **Office example:** Making a badge by hand without the building's approval.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud container clusters get-credentials shopnow-dev --region=us-central1
kubectl get nodes
kubectl config use-context gke_shopnow_us-central1_shopnow-prod   # back to prod
```

---

## 🧠 Key Takeaways / Memory Tips

- **Point kubectl at another GKE cluster → `gcloud container clusters get-credentials NAME`.**
  🧠 *"**Get credentials, get nodes.**"*
- Related: **Q189**, **Q123**.

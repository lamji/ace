# Q071: GKE Pulling Images From Container Registry in Another Project (Storage Object Viewer)

**Topic:** IAM + GKE (Container Registry storage bucket, node service account, Storage Object Viewer, access scopes)

## ❓ Question
> You are using Container Registry to centrally store your company's container images in a separate project. In another project, you want to create a Google Kubernetes Engine (GKE) cluster. You want to ensure that Kubernetes can download images from Container Registry. What should you do?
>
> **A.** In the project where the images are stored, grant the Storage Object Viewer IAM role to the service account used by the Kubernetes nodes.
>
> **B.** When you create the GKE cluster, choose the Allow full access to all Cloud APIs option under 'Access scopes'.
>
> **C.** Create a service account, and give it access to Cloud Storage. Create a P12 key for this service account and use it as an imagePullSecrets in Kubernetes.
>
> **D.** Configure the ACLs on each image in Cloud Storage to give read-only access to the default Compute Engine service account.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Real-life note:** Container Registry has been replaced by **Artifact Registry**. The same idea applies there: grant the node service account **Artifact Registry Reader** on the repository's project.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Container images are stored in Container Registry in a separate project. A GKE cluster is in another project.
- **What you must achieve:** Let Kubernetes download images from that registry.
- **The limits:** None stated.
- **What they're really asking:** Which permission do you give, and to which identity?

**Clues in the question:**
- "**Container Registry … in a separate project**": Container Registry stores images as files in a **Cloud Storage bucket** in that project. Reading them = reading Cloud Storage objects.
- "**In another project … GKE cluster**": the nodes run as a **service account from project B**, which has no access to project A by default.
- "**download images**": read-only access is enough → **Storage Object Viewer**.

**Exam topic:** IAM / GKE.

---

## 📚 Key Terms Explained

### 1️⃣ Container Registry
- **What it is:** Google's older service for storing container images. Behind the scenes, each image is a set of **files in a Cloud Storage bucket** named like `artifacts.PROJECT.appspot.com`.
- **Looks like:** `gcr.io/shopnow-images/web:1.4`
- **Not to be confused with:** Artifact Registry, the newer replacement with its own roles.
- **Analogy:** 📦 The company's **central parts warehouse**.
- **In the online store:** All ShopNow images (web, checkout, worker) live in `shopnow-images`.

### 2️⃣ Node service account 🔑
- **What it is:** The **service account the GKE nodes (VMs) run as**. When a node pulls an image, it uses this identity. By default it's the project's Compute Engine default service account.
- **Looks like:** `123456789-compute@developer.gserviceaccount.com`
- **Not to be confused with:** a person's account, or a Kubernetes service account inside the cluster.
- **Analogy:** 🪪 The **delivery truck's company badge** that the warehouse checks at the gate.
- **In the online store:** The `shop-cluster` nodes' badge.

### 3️⃣ Storage Object Viewer (`roles/storage.objectViewer`)
- **What it is:** A role that can **read (download) and list** objects in Cloud Storage, but not change or delete them.
- **Looks like:** `gcloud projects add-iam-policy-binding shopnow-images --member=serviceAccount:123456789-compute@developer.gserviceaccount.com --role=roles/storage.objectViewer`
- **Not to be confused with:** Storage Object Admin (can also change and delete).
- **Analogy:** 📖 A **read-only pass** to the warehouse: pick up parts, but not move or throw them out.
- **In the online store:** The cluster can pull images, but can't push or delete them.

### 4️⃣ Access scopes (review from Q036)
- **What it is:** An old, extra **limit** on what APIs a VM's service account can call. Scopes can only **narrow** permissions; they never **grant** IAM access.
- **Looks like:** "Allow full access to all Cloud APIs" checkbox when creating a VM or cluster
- **Not to be confused with:** IAM roles. Even with full scopes, the service account still needs a role in project A.
- **Analogy:** 🚦 A **speed limit sign**. It can slow you down, but it can't give you a driver's license.

### 5️⃣ imagePullSecrets / P12 key
- **What it is:** A Kubernetes secret holding credentials to pull images from a private registry. A **P12 key** is an **old key file format** for service accounts (JSON replaced it).
- **Not to be confused with:** the recommended way on GKE, which is to use the node service account's IAM role, with no key files.
- **Analogy:** 🔑 Making a **copy of a key** and taping it inside the truck.

### 6️⃣ ACLs (Access Control Lists) on objects
- **What it is:** Old-style permissions set **on each individual file** in Cloud Storage.
- **Not to be confused with:** IAM roles, which apply to a whole bucket or project at once.
- **Analogy:** 🏷️ Putting a **permission tag on every single box** instead of giving one pass to the warehouse.

### 🔗 How they fit together
```
 Project shopnow-images                      Project shopnow-prod
   📦 Container Registry                        ☸️ GKE cluster
      = bucket artifacts.shopnow-images…        nodes run as 🪪 123-compute@…
        │                                              │
        └── IAM: storage.objectViewer for 123-compute@ ◄┘  ✅ nodes can pull
```

---

## 🌍 Real-World Scenario

Companies often keep **one central project for images**, so every team pulls from the same trusted place. Each cluster in each project must be allowed to read from it. The platform team grants each cluster's **node service account** a read-only role in the image project. Nothing to rotate, no keys to leak.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** In the project where the images are stored, grant the Storage Object Viewer IAM role to the service account used by the Kubernetes nodes.

**Why it's correct:**
- ✔️ "**In the project where the images are stored**" matches "**in a separate project**": permissions must be given where the images (the bucket) actually live.
- ✔️ "**Storage Object Viewer IAM role**" matches "**download images from Container Registry**": Container Registry images are Cloud Storage files, and this role reads them, nothing more.
- ✔️ "**the service account used by the Kubernetes nodes**" matches "**Kubernetes can download images**": the nodes pull images using this identity.

📌 **When to use it:** Use it when machines in one department must pick up items from another department's storage, read-only.
🏢 **Office example:** Giving the branch office's delivery driver a read-only pass to the central warehouse.

### ❌ B
> **B.** When you create the GKE cluster, choose the Allow full access to all Cloud APIs option under 'Access scopes'.

**Wrong words:**
- ❌ "**Allow full access to all Cloud APIs option under 'Access scopes'**": scopes only **limit**; they never **grant** IAM permissions. The node service account still has **no role in the image project**, so pulls still fail.

📌 **When to use it:** Use full scopes when you want IAM roles alone to decide what a VM can do (Google's current advice), not as a way to grant access.
🏢 **Office example:** Removing the speed limit on the truck. It still can't enter a warehouse it has no pass for.

### ❌ C
> **C.** Create a service account, and give it access to Cloud Storage. Create a P12 key for this service account and use it as an imagePullSecrets in Kubernetes.

**Wrong words:**
- ❌ "**Create a P12 key**": an old key format, and any key file is a secret that can leak and must be rotated.
- ❌ "**use it as an imagePullSecrets**": extra setup in every namespace, when GKE nodes can pull with their own service account and an IAM role.

📌 **When to use it:** Use imagePullSecrets when pulling from a **non-Google** private registry (like Docker Hub private repos).
🏢 **Office example:** Copying a warehouse key and taping it inside every truck, instead of giving the drivers a pass.

### ❌ D
> **D.** Configure the ACLs on each image in Cloud Storage to give read-only access to the default Compute Engine service account.

**Wrong words:**
- ❌ "**Configure the ACLs on each image**": every image is many files (layers). Setting permissions file by file is a lot of work and breaks every time a new image is pushed.
- ❌ "**the default Compute Engine service account**": which project's default account? The nodes may use a different, custom service account.

📌 **When to use it:** Almost never. Use it only for a few individual files that need special access.
🏢 **Office example:** Putting a permission tag on every single box in the warehouse instead of giving one pass.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow keeps all images in `shopnow-images`. The production cluster is in `shopnow-prod`.

```bash
# Find the node service account of shop-cluster (here: the default compute SA)
NODE_SA=123456789-compute@developer.gserviceaccount.com

# Grant read-only access in the IMAGE project
gcloud projects add-iam-policy-binding shopnow-images \
  --member=serviceAccount:$NODE_SA --role=roles/storage.objectViewer

# Now this works in shopnow-prod
kubectl create deployment web --image=gcr.io/shopnow-images/web:1.4
```

---

## 🧠 Key Takeaways / Memory Tips

- **Container Registry = Cloud Storage files → nodes need Storage Object Viewer in the image project.**
- **Scopes never grant access; IAM roles do.**
- On GKE, prefer the **node service account + IAM role** over key files and imagePullSecrets.
  🧠 *"**Give the truck a pass to the warehouse.**"*
- Related: **Q036** (cross-project role for a service account, scopes are wrong), **Q012** (deploy images to GKE).

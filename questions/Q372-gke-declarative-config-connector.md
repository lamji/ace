# Q372: Manage Other Google Cloud Resources With the Same Declarative Kubernetes Tooling (Config Connector)

**Topic:** Infrastructure as Code (Config Connector)

## ❓ Question
> Your company uses Google Kubernetes Engine (GKE) for all application deployments. Your team needs to provision and manage other Google Cloud resources using the same declarative approach and tooling as your application deployments. What should you do?
>
> **A.** Use the Google Cloud console to provision and manage Google Cloud resources.
>
> **B.** Write shell scripts using gcloud commands to provision and manage Google Cloud resources.
>
> **C.** Create Terraform configurations for your Google Cloud resources, and store the state file in a Cloud Storage bucket.
>
> **D.** Install Config Connector in a GKE cluster, and define your Google Cloud resources as custom resources in Kubernetes manifests.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company deploys all apps on GKE.
- **What you must achieve:** Create and manage other Google Cloud resources the same way.
- **The limits:** Use the same declarative approach and tools as your app deployments.
- **What they're really asking:** Which tool lets you manage cloud resources with Kubernetes-style files?

**Clues in the question:**
- "**same declarative approach and tooling as your application deployments**" on GKE → **Config Connector** (Google Cloud resources as Kubernetes custom resources).

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Config Connector 🔑
- **What it is:** A Kubernetes add-on that lets you define Google Cloud resources (buckets, Cloud SQL, Pub/Sub) as Kubernetes YAML; it creates and reconciles them.
- **Looks like:** `apiVersion: storage.cnrm.cloud.google.com/v1beta1\nkind: StorageBucket\nmetadata: {name: shopnow-assets}`
- **Not to be confused with:** Terraform (different tool).
- **Analogy:** 📝 Ordering office supplies on the same form you use for staff requests.
- **In the online store:** ShopNow buckets/topics via kubectl.

### 🔗 How they fit together
```
 kubectl apply (Deployment + StorageBucket + PubSubTopic) → Config Connector → Google Cloud ✅
```

---

## 🌍 Real-World Scenario

A GKE-centric team defines buckets and topics as **Config Connector** manifests alongside their Deployments.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the Google Cloud console to provision and manage Google Cloud resources.

**Wrong words:**
- ❌ "**Google Cloud console**": manual, not declarative.

📌 **When to use it:** Use the console for exploration.
🏢 **Office example:** Filling paper forms by hand.

### ❌ B
> **B.** Write shell scripts using gcloud commands to provision and manage Google Cloud resources.

**Wrong words:**
- ❌ "**shell scripts using gcloud**": imperative, not the same tooling.

📌 **When to use it:** Use scripts for one-off automation.
🏢 **Office example:** A to-do list instead of a blueprint.

### ❌ C
> **C.** Create Terraform configurations for your Google Cloud resources, and store the state file in a Cloud Storage bucket.

**Wrong words:**
- ✔️ Declarative IaC.
- ❌ "**Terraform**": a different tool from their Kubernetes tooling.

📌 **When to use it:** Use Terraform for multi-cloud or non-Kubernetes teams.
🏢 **Office example:** A different form system.

### ✅ D
> **D.** Install Config Connector in a GKE cluster, and define your Google Cloud resources as custom resources in Kubernetes manifests.

**Why it's correct:**
- ✔️ "**Config Connector … Kubernetes manifests**" matches "**same declarative approach and tooling as your application deployments**".

📌 **When to use it:** Use it when your team already describes everything with one kind of form and wants to order cloud resources the same way.
🏢 **Office example:** Requesting new supplies on the same form you already use for everything else.

---

## 🛒 E-Commerce Full-Stack Example

`k8s/infra/bucket.yaml` (StorageBucket) applied with the app manifests via Config Sync.

---

## 🧠 Key Takeaways / Memory Tips

- **GKE team, manage Google Cloud resources via Kubernetes YAML → Config Connector.**
  🧠 *"**Kubernetes YAML for cloud stuff: Config Connector.**"*
- Related: **Q304**.

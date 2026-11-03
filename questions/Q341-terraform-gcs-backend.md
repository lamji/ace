# Q341: Team Terraform Without State Conflicts or Secrets on Laptops (Cloud Storage Backend)

**Topic:** Infrastructure as Code (Terraform remote state)

## ❓ Question
> You are managing Google Cloud infrastructure with Terraform. The Terraform configuration files are stored in a Git repository. You need to implement a solution that enables multiple team members to work on the Terraform configurations concurrently without conflicts and ensures that sensitive values are not persisted to local machines. What should you do?
>
> **A.** Configure a local backend in Terraform, and deploy all changes by using a shared account on a bastion server.
>
> **B.** Configure a Cloud Storage backend in Terraform.
>
> **C.** Configure a local backend in Terraform, and store the state file in a Git repository.
>
> **D.** Configure a local backend in Terraform, and manually share the Terraform state file with team members after every change.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Many people edit Terraform **concurrently**; **no sensitive values on local machines**.

**Clues in the question:**
- Shared state + locking + nothing stored locally → **remote backend in Cloud Storage** (`gcs` backend locks state).

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Terraform state / gcs backend 🔑
- **What it is:** State = Terraform's record of what it built (can contain secrets). The `gcs` backend stores it in a bucket with locking.
- **Looks like:** `terraform { backend "gcs" { bucket = "shopnow-tfstate" prefix = "prod" } }`
- **Not to be confused with:** local backend (file on your laptop).
- **Analogy:** 📒 One shared master logbook in a locked office.
- **In the online store:** ShopNow infra.

### 🔗 How they fit together
```
 dev A ─┐
 dev B ─┼─► gs://tfstate (locked, versioned) ✅
 CI ────┘
```

---

## 🌍 Real-World Scenario

A team moves state to a **Cloud Storage backend**; locking prevents two applies at once and laptops hold no state.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Configure a local backend in Terraform, and deploy all changes by using a shared account on a bastion server.

**Wrong words:**
- ❌ "**local backend … shared account on a bastion server**": shared login, no individual audit; bottleneck.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Everyone using one shared login at one desk.

### ✅ B
> **B.** Configure a Cloud Storage backend in Terraform.

**Why it's correct:**
- ✔️ "**Cloud Storage backend**" matches "**work … concurrently without conflicts**" (state locking) + "**sensitive values are not persisted to local machines**".

📌 **When to use it:** Use it when several people change the same setup and the shared record must stay safe in one place.
🏢 **Office example:** One master logbook in a locked office that only one person can write in at a time.

### ❌ C
> **C.** Configure a local backend in Terraform, and store the state file in a Git repository.

**Wrong words:**
- ❌ "**store the state file in a Git repository**": secrets end up in Git and on every clone; no locking.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Photocopying the logbook with passwords for everyone.

### ❌ D
> **D.** Configure a local backend in Terraform, and manually share the Terraform state file with team members after every change.

**Wrong words:**
- ❌ "**manually share the Terraform state file**": conflicts and secrets on laptops.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Emailing the logbook back and forth.

---

## 🛒 E-Commerce Full-Stack Example

`gs://shopnow-tfstate` (versioning on, UBLA, restricted IAM).

---

## 🧠 Key Takeaways / Memory Tips

- **Team Terraform → remote state in Cloud Storage (locking, no local state).**
  🧠 *"**State lives in a bucket.**"*
- Related: **Q318**, **Q304**.

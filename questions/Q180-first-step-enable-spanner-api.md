# Q180: First Step Before Creating a Spanner Instance (Enable the Cloud Spanner API)

**Topic:** APIs (enabling services in a new project)

## ❓ Question
> You have just created a new project which will be used to deploy a globally distributed application. You will use Cloud Spanner for data storage. You want to create a Cloud Spanner instance. You want to perform the first step in preparation of creating the instance. What should you do?
>
> **A.** Enable the Cloud Spanner API.
>
> **B.** Configure your Cloud Spanner instance to be multi-regional.
>
> **C.** Create a new VPC network with subnetworks in all desired regions.
>
> **D.** Grant yourself the IAM role of Cloud Spanner Admin.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** New project. What's the **first step** before making a Spanner instance?

**Clues in the question:**
- "**just created a new project**" + "**first step**" → **enable the API** (Q136 pattern).
- As project creator you're already Owner, so you don't need to grant yourself a role.

**Exam topic:** APIs.

---

## 📚 Key Terms Explained

### 1. Enabling an API 🔑 (review from Q136)
- **What it is:** Turns on a Google service in a project. Nothing works until it's enabled.
- **Looks like:** `gcloud services enable spanner.googleapis.com`
- **Not to be confused with:** IAM roles.
- **Analogy:** 💡 Flipping on the power for a room.
- **In the online store:** Enable sqladmin, run, spanner.

### 🔗 How they fit together
```
 new project → enable spanner API ✅ → create instance (choose multi-region config)
```

---

## 🌍 Real-World Scenario

A developer creates a project for a global app. Before anything else they run `gcloud services enable spanner.googleapis.com`.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Enable the Cloud Spanner API.

**Why it's correct:**
- ✔️ "**Enable the Cloud Spanner API**" matches "**first step in preparation of creating the instance**" in a "**new project**".

📌 **When to use it:** Use it whenever you start using a new kind of service in a project.
🏢 **Office example:** Turning on the power to a new room before moving in furniture.

### ❌ B
> **B.** Configure your Cloud Spanner instance to be multi-regional.

**Wrong words:**
- ❌ "**Configure your Cloud Spanner instance to be multi-regional**": that's part of **creating** the instance, which comes after enabling the API.

📌 **When to use it:** Use multi-region configs for global apps, at creation.
🏢 **Office example:** Arranging furniture before the power's on.

### ❌ C
> **C.** Create a new VPC network with subnetworks in all desired regions.

**Wrong words:**
- ❌ "**new VPC network**": Spanner doesn't need your VPC subnets.

📌 **When to use it:** Use custom VPCs for your VMs.
🏢 **Office example:** Building corridors for a room that doesn't need them.

### ❌ D
> **D.** Grant yourself the IAM role of Cloud Spanner Admin.

**Wrong words:**
- ❌ "**Grant yourself … Cloud Spanner Admin**": as project creator you're already Owner.

📌 **When to use it:** Use it to give others Spanner admin rights.
🏢 **Office example:** Giving yourself a key to a building you own.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud services enable spanner.googleapis.com --project=shopnow-global` → then `gcloud spanner instances create inventory --config=nam6 --nodes=1`.

---

## 🧠 Key Takeaways / Memory Tips

- **New project → first enable the API.**
  🧠 *"**Power on before furniture.**"*
- Related: **Q136**, **Q181**, **Q173**.

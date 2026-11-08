# Q176: Choose a Different Service Account per VM (Specify It When Creating the Instance)

**Topic:** Compute Engine (service accounts on VMs)

## ❓ Question
> You will have several applications running on different Compute Engine instances in the same project. You want to specify at a more granular level the service account each instance uses when calling Google Cloud APIs. What should you do?
>
> **A.** When creating the instances, specify a Service Account for each instance.
>
> **B.** When creating the instances, assign the name of each Service Account as instance metadata.
>
> **C.** After starting the instances, use gcloud compute instances update to specify a Service Account for each instance.
>
> **D.** After starting the instances, use gcloud compute instances update to assign the name of the relevant Service Account as instance metadata.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Several apps run on different VMs in the same project.
- **What you must achieve:** Choose exactly which service account (the identity it uses for Google APIs) each VM uses.
- **The limits:** Control it VM by VM.
- **What they're really asking:** How do you give each VM its own service account?

**Clues in the question:**
- "**specify … the service account each instance uses**" → set it **at creation** with `--service-account`.
- Changing it later requires **stopping** the VM, and `instances update` doesn't do it.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Service account on a VM 🔑
- **What it is:** The identity the VM uses to call Google APIs. Set at creation (or `set-service-account` while stopped).
- **Looks like:** `gcloud compute instances create app1 --service-account=app1-sa@proj.iam.gserviceaccount.com --scopes=cloud-platform`
- **Not to be confused with:** metadata.
- **Analogy:** 🪪 The badge you give a robot on day one.
- **In the online store:** Each ShopNow VM its own SA.

### 2. Instance metadata
- **What it is:** Key/value settings for the VM. **Not** how the identity is chosen.
- **Looks like:** `startup-script=…`
- **Not to be confused with:** service account.
- **Analogy:** 📝 A sticky note on the desk.
- **In the online store:** Startup scripts.

### 🔗 How they fit together
```
 create app1 --service-account=app1-sa ✅
 create app2 --service-account=app2-sa ✅
```

---

## 🌍 Real-World Scenario

Two apps run on separate VMs. Each VM is **created with its own service account**, so the orders app can't touch the reports bucket.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** When creating the instances, specify a Service Account for each instance.

**Why it's correct:**
- ✔️ "**When creating the instances, specify a Service Account for each instance**" matches "**specify at a more granular level the service account each instance uses**".

📌 **When to use it:** Use it when each machine should have its own identity from the start.
🏢 **Office example:** Giving each new robot its own badge on its first day.

### ❌ B
> **B.** When creating the instances, assign the name of each Service Account as instance metadata.

**Wrong words:**
- ❌ "**assign the name of each Service Account as instance metadata**": metadata doesn't change the VM's identity.

📌 **When to use it:** Use metadata for settings like startup scripts.
🏢 **Office example:** Writing a badge number on a sticky note instead of issuing a badge.

### ❌ C
> **C.** After starting the instances, use gcloud compute instances update to specify a Service Account for each instance.

**Wrong words:**
- ❌ "**After starting the instances, use gcloud compute instances update**": you can't change the SA on a running VM this way (the VM must be stopped and you use `set-service-account`).

📌 **When to use it:** Use `set-service-account` on a stopped VM to change it later.
🏢 **Office example:** Swapping a badge while the robot is on shift.

### ❌ D
> **D.** After starting the instances, use gcloud compute instances update to assign the name of the relevant Service Account as instance metadata.

**Wrong words:**
- ❌ "**instance metadata**" after starting: wrong mechanism on two counts.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A sticky note on a running robot.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instances create orders-vm --service-account=orders-sa@shopnow-prod.iam.gserviceaccount.com --scopes=cloud-platform`

---

## 🧠 Key Takeaways / Memory Tips

- **Per-VM identity → `--service-account` at creation.**
  🧠 *"**Badge on day one.**"*
- Related: **Q134**, **Q183**.

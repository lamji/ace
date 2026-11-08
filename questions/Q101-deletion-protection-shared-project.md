# Q101: Stopping Other Teams From Accidentally Taking Down Your VM (Deletion Protection)

**Topic:** Compute Engine (deletion protection, Shielded VM, preemptible VM, sole-tenant nodes)

## ❓ Question
> You need to host an application on a Compute Engine instance in a project shared with other teams. You want to prevent the other teams from accidentally causing downtime on that application. Which feature should you use?
>
> **A.** Use a Shielded VM.
>
> **B.** Use a Preemptible VM.
>
> **C.** Use a sole-tenant node.
>
> **D.** Enable deletion protection on the instance.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You host an app on a VM in a project that other teams also use.
- **What you must achieve:** Stop other teams from accidentally causing downtime for your app.
- **The limits:** None stated.
- **What they're really asking:** Which feature protects the VM from being taken down by mistake?

**Clues in the question:**
- "**project shared with other teams**": other people have permissions in this project.
- "**accidentally causing downtime**": the risk is a **mistake**, like someone deleting the wrong VM → **deletion protection** blocks deletes.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Deletion protection 🔑
- **What it is:** A **checkbox (a true/false setting) on a VM**. While it's on, any attempt to delete the VM fails until someone turns it off first.
- **Looks like:** `gcloud compute instances update shop-api --deletion-protection`
- **Not to be confused with:** a permission. People with delete rights still can't delete it until they untick the box.
- **Analogy:** 🔒 A **"Do not remove" lock** on an important filing cabinet.
- **In the online store:** The checkout VM can't be deleted by a teammate cleaning up test VMs.

### 2. Shielded VM
- **What it is:** A VM with **secure boot and integrity checks** that protect against boot-level malware.
- **Looks like:** `--shielded-secure-boot`
- **Not to be confused with:** protection from people deleting it.
- **Analogy:** 🛡️ A tamper-proof seal on a computer.
- **In the online store:** Protects the payment VM from rootkits.

### 3. Preemptible VM
- **What it is:** A **cheap VM Google can stop at any time**.
- **Looks like:** `--preemptible`
- **Not to be confused with:** a safer VM. It makes downtime **more** likely.
- **Analogy:** 🪑 A borrowed desk the owner can take back.
- **In the online store:** Nightly image resizing jobs.

### 4. Sole-tenant node
- **What it is:** A **physical server only your VMs run on**, for licensing or compliance.
- **Looks like:** `gcloud compute sole-tenancy node-groups create ...`
- **Not to be confused with:** protection from your own coworkers.
- **Analogy:** 🏠 Renting a whole house instead of an apartment.
- **In the online store:** Rarely needed for a shop.

### 🔗 How they fit together
```
 shared project: team A, team B, you
   shop-api VM (deletion protection = ON)
     teammate runs: gcloud compute instances delete shop-api
     → ERROR: resource is protected ✅
```

---

## 🌍 Real-World Scenario

Several teams share a dev/ops project. During a cleanup, someone runs a delete command on a list of VMs and your app's VM is on it. With **deletion protection** on, the delete fails and your app keeps running.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use a Shielded VM.

**Wrong words:**
- ❌ "**Use a Shielded VM**": it protects against boot malware, not against a coworker deleting the VM.

📌 **When to use it:** Use it when you want protection against hidden malware at startup.
🏢 **Office example:** A tamper-proof seal on a computer: it doesn't stop a coworker from throwing it out.

### ❌ B
> **B.** Use a Preemptible VM.

**Wrong words:**
- ❌ "**Use a Preemptible VM**": Google can stop it at any time, which **adds** downtime.

📌 **When to use it:** Use it for cheap jobs that can be interrupted.
🏢 **Office example:** Working at a borrowed desk that can be taken back anytime.

### ❌ C
> **C.** Use a sole-tenant node.

**Wrong words:**
- ❌ "**Use a sole-tenant node**": it isolates the hardware from other customers, but your coworkers in the same project can still delete the VM.

📌 **When to use it:** Use it when licenses or rules require your own physical server.
🏢 **Office example:** Renting a whole building: your coworkers can still throw out your files.

### ✅ D
> **D.** Enable deletion protection on the instance.

**Why it's correct:**
- ✔️ "**Enable deletion protection**" matches "**prevent the other teams from accidentally causing downtime**": a delete attempt fails, so a mistake can't remove the VM.
- ✔️ "**on the instance**" matches "**host an application on a Compute Engine instance**": the protection is on exactly that VM.

📌 **When to use it:** Use it when an important item could be removed by mistake by people who share the space.
🏢 **Office example:** A "Do not remove" lock on the important filing cabinet in a shared office.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's `checkout-api` VM lives in `shopnow-shared` with other teams' test VMs.

```bash
gcloud compute instances update checkout-api --zone=us-central1-a --deletion-protection
```
A teammate runs `gcloud compute instances delete $(gcloud compute instances list --format='value(name)')`. Every test VM is deleted, but `checkout-api` returns an error and stays up.

---

## 🧠 Key Takeaways / Memory Tips

- **Prevent accidental deletion → deletion protection.**
- Shielded VM = boot security. Preemptible = can be stopped. Sole-tenant = own hardware.
  🧠 *"**Afraid of an accidental delete? Turn on deletion protection.**"*
- Related: **Q089** (machine types), **Q094** (preemptible nodes).

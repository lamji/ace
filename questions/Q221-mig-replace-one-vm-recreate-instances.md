# Q221: Quickly Replace One Unresponsive VM in a MIG (gcloud compute instance-groups managed recreate-instances)

**Topic:** Compute Engine (managed instance groups)

## ❓ Question
> Your application is running on Google Cloud in a managed instance group (MIG). You see errors in Cloud Logging for one VM that one of the processes is not responsive. You want to replace this VM in the MIG quickly. What should you do?
>
> **A.** Use the gcloud compute instances update command with a REFRESH action for the VM.
>
> **B.** Use the gcloud compute instance-groups managed recreate-instances command to recreate the VM.
>
> **C.** Select the MIG from the Compute Engine console and, in the menu, select Replace VMs.
>
> **D.** Update and apply the instance template of the MIG.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

> ℹ️ **Note:** **Debated** between B and C. B targets exactly the one broken VM. The console's **Replace VMs** starts a rolling replace of the group's VMs, which is slower and touches healthy VMs too. If your site's Most Voted differs, tell me.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your app runs in a managed instance group (a group of identical VMs kept running from a template). Cloud Logging shows that a process on one VM is not responding.
- **What you must achieve:** Replace that one VM in the group.
- **The limits:** Do it quickly.
- **What they're really asking:** What is the quickest way to swap out that single broken VM?

**Clues in the question:**
- "**replace this VM**" (one VM) + "**quickly**" → `recreate-instances --instances=VM` deletes it and creates a fresh one from the template.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. recreate-instances 🔑
- **What it is:** A MIG command that **deletes and recreates** specific VMs from the current template, keeping their names.
- **Looks like:** `gcloud compute instance-groups managed recreate-instances web-mig --instances=web-x7k2 --zone=us-central1-a`
- **Not to be confused with:** update (template change).
- **Analogy:** 🔁 Swapping one faulty printer for a fresh one of the same model.
- **In the online store:** Fix a stuck checkout VM.

### 2. Replace VMs (rolling replace)
- **What it is:** Replaces VMs across the group in waves (used after template changes).
- **Looks like:** console → Restart/Replace VMs
- **Not to be confused with:** recreate one VM.
- **Analogy:** 🔁 Swapping every printer on the floor.
- **In the online store:** —

### 🔗 How they fit together
```
 MIG: vm1 ✅ vm2 ❌ vm3 ✅ → recreate-instances --instances=vm2 → vm2 (fresh) ✅
```

---

## 🌍 Real-World Scenario

One checkout VM's process hangs. The on-call engineer runs **`recreate-instances`** for just that VM; it comes back fresh in a minute.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use the gcloud compute instances update command with a REFRESH action for the VM.

**Wrong words:**
- ❌ "**gcloud compute instances update … REFRESH**": not how you replace a MIG VM, and a refresh doesn't recreate it.

📌 **When to use it:** Use MIG commands, not single-instance updates, for MIG VMs.
🏢 **Office example:** Polishing a broken printer instead of swapping it.

### ✅ B
> **B.** Use the gcloud compute instance-groups managed recreate-instances command to recreate the VM.

**Why it's correct:**
- ✔️ "**recreate-instances command to recreate the VM**" matches "**replace this VM in the MIG**": it targets the one VM.
- ✔️ One command, done in a minute, which matches "**quickly**".

📌 **When to use it:** Use it when one machine in an identical group goes bad and you just want a fresh copy.
🏢 **Office example:** Swapping out the one jammed printer for a new one of the same model.

### ❌ C
> **C.** Select the MIG from the Compute Engine console and, in the menu, select Replace VMs.

**Wrong words:**
- ❌ "**Replace VMs**" from the MIG menu: a rolling replace that works through the group, slower and touching healthy VMs.

📌 **When to use it:** Use rolling replace after changing the template.
🏢 **Office example:** Replacing every printer on the floor because one jammed.

### ❌ D
> **D.** Update and apply the instance template of the MIG.

**Wrong words:**
- ❌ "**Update and apply the instance template**": nothing is wrong with the template; it's a slow, group-wide change.

📌 **When to use it:** Use it to roll out a new configuration.
🏢 **Office example:** Changing the printer model company-wide for one jam.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instance-groups managed recreate-instances checkout-mig --instances=checkout-mig-x7k2 --zone=us-central1-a`

---

## 🧠 Key Takeaways / Memory Tips

- **Replace one MIG VM quickly → `recreate-instances`.** (Autohealing can do it automatically.)
  🧠 *"**One bad apple? Recreate that one.**"*
- Related: **Q224**, **Q225**.

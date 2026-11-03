# Q157: Prevent Anyone Destroying the Production VM by Mistake (Delete Protection)

**Topic:** Compute Engine (deletion protection)

## ❓ Question
> You are deploying a production application on Compute Engine. You want to prevent anyone from accidentally destroying the instance by clicking the wrong button. What should you do?
>
> **A.** Disable the flag "Delete boot disk when instance is deleted."
>
> **B.** Enable delete protection on the instance.
>
> **C.** Disable Automatic restart on the instance.
>
> **D.** Enable Preemptibility on the instance.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Stop people from **accidentally deleting** the production VM.

**Clues in the question:**
- "**prevent anyone from accidentally destroying the instance**" → **deletion protection** (same idea as Q101).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Deletion protection 🔑 (review from Q101)
- **What it is:** A VM setting. While it's on, **delete requests fail**.
- **Looks like:** `gcloud compute instances update prod-1 --deletion-protection`
- **Not to be confused with:** disk auto-delete.
- **Analogy:** 🔒 A "Do not remove" lock.
- **In the online store:** Checkout VM can't be deleted by a misclick.

### 2. Delete boot disk when instance is deleted
- **What it is:** A **disk** setting (auto-delete). Turning it off keeps the disk **after** the VM is gone, but doesn't prevent the deletion.
- **Looks like:** `--keep-disks=boot`
- **Not to be confused with:** deletion protection.
- **Analogy:** 🗄️ Keeping the cabinet after the desk is thrown out.
- **In the online store:** Keep data disks.

### 🔗 How they fit together
```
 deletion protection ON → "Delete" button → ERROR ✅ instance survives
```

---

## 🌍 Real-World Scenario

A junior admin cleaning up test VMs clicks Delete on the production server by mistake. **Deletion protection** blocks it.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Disable the flag "Delete boot disk when instance is deleted."

**Wrong words:**
- ❌ "**Disable … Delete boot disk when instance is deleted**": the VM is still destroyed. Only the disk is kept.

📌 **When to use it:** Use it when you want to keep a disk after deleting a VM.
🏢 **Office example:** Keeping the cabinet but still throwing out the desk.

### ✅ B
> **B.** Enable delete protection on the instance.

**Why it's correct:**
- ✔️ "**Enable delete protection on the instance**" matches "**prevent anyone from accidentally destroying the instance**": delete attempts fail until someone turns it off.

📌 **When to use it:** Use it for any important machine that must not be removed by mistake.
🏢 **Office example:** A "Do not remove" lock on the key cabinet.

### ❌ C
> **C.** Disable Automatic restart on the instance.

**Wrong words:**
- ❌ "**Disable Automatic restart**": it controls restarting after a crash. It doesn't protect against deletion, and it makes things worse.

📌 **When to use it:** Disable automatic restart only for special cases.
🏢 **Office example:** Telling the guard not to reopen the office after a power cut.

### ❌ D
> **D.** Enable Preemptibility on the instance.

**Wrong words:**
- ❌ "**Enable Preemptibility**": Google may stop the VM at any time. That's the opposite of protection.

📌 **When to use it:** Use it for cheap interruptible jobs.
🏢 **Office example:** Using a desk that can be taken away anytime.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instances update checkout-prod-1 --zone=us-central1-a --deletion-protection`. A wrong click on Delete gives an error, and checkout stays online.

---

## 🧠 Key Takeaways / Memory Tips

- **Accidental deletion → deletion protection.** (Same as Q101.)
  🧠 *"**Misclick-proof: deletion protection.**"*
- Related: **Q101**.

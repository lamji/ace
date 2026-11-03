# Q347: Ops Team Can Only Start, Stop and Reset VMs (Custom Role With Exactly Those Permissions)

**Topic:** IAM (custom roles)

## ❓ Question
> You manage IAM policies for your organization’s Google Cloud project. A new operations team needs the capability to start, stop, and reset existing Compute Engine VM instances within this project for basic troubleshooting. Due to strict security requirements, the operations team must be prevented from deleting any instances or modifying any networking or configuration settings. You need to grant the minimum necessary permissions to the team members. What should you do?
>
> **A.** Grant the operations team the roles/writer IAM role, and add the resource.type =='compute.googleapis.com/Instance' condition to the role.
>
> **B.** Grant the operations team the predefined roles/compute.instanceAdmin.v1 IAM role on the project. Apply an IAM condition to exclude the compute.instances.delete permission.
>
> **C.** Create a custom IAM role that includes only the compute.instances.start, compute.instances.stop, and compute.instances.reset permissions. Assign this role to the operations team on the project.
>
> **D.** Grant the operations team the predefined roles/compute.viewer IAM role to allow them to view the instances. Instruct them to use the Google Cloud Console’s basic actions such as starting, stopping, and resetting.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Start/stop/reset VMs only. **No delete, no config changes.**

**Clues in the question:**
- "**minimum necessary permissions**" + no predefined role fits exactly → **custom role** with `start`, `stop`, `reset`.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Custom role 🔑 (review from Q303)
- **What it is:** Exact list of permissions.
- **Looks like:** `--permissions=compute.instances.start,compute.instances.stop,compute.instances.reset`
- **Not to be confused with:** IAM conditions (can't remove permissions).
- **Analogy:** 🔑 A key cut for three doors.
- **In the online store:** —

### 🔗 How they fit together
```
 custom role {start, stop, reset} → ops team ✅
```

---

## 🌍 Real-World Scenario

Ops gets a **custom role** with just start/stop/reset on the project.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Grant the operations team the roles/writer IAM role, and add the resource.type =='compute.googleapis.com/Instance' condition to the role.

**Wrong words:**
- ❌ "**roles/writer**": not a valid Google Cloud IAM role; basic Editor would be far too broad anyway.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** A made-up master key.

### ❌ B
> **B.** Grant the operations team the predefined roles/compute.instanceAdmin.v1 IAM role on the project. Apply an IAM condition to exclude the compute.instances.delete permission.

**Wrong words:**
- ❌ "**IAM condition to exclude the compute.instances.delete permission**": conditions limit *where/when* a role applies, not which permissions it has; instanceAdmin still allows config changes.

📌 **When to use it:** Use instanceAdmin for VM administrators.
🏢 **Office example:** A master key with a sticky note saying 'don't'.

### ✅ C
> **C.** Create a custom IAM role that includes only the compute.instances.start, compute.instances.stop, and compute.instances.reset permissions. Assign this role to the operations team on the project.

**Why it's correct:**
- ✔️ "**custom IAM role … only the compute.instances.start, compute.instances.stop, and compute.instances.reset**" matches "**start, stop, and reset**" + "**prevented from deleting … or modifying**" + "**minimum necessary permissions**".

📌 **When to use it:** Use it when a team should press only a few specific buttons and nothing else.
🏢 **Office example:** A key that only opens the power switch room.

### ❌ D
> **D.** Grant the operations team the predefined roles/compute.viewer IAM role to allow them to view the instances. Instruct them to use the Google Cloud Console’s basic actions such as starting, stopping, and resetting.

**Wrong words:**
- ❌ "**compute.viewer**": can't start/stop/reset.

📌 **When to use it:** Use viewer for read-only monitoring.
🏢 **Office example:** A window, no switch.

---

## 🛒 E-Commerce Full-Stack Example

`roles/shopnow.vmOperator` → `group:ops@shopnow.com`.

---

## 🧠 Key Takeaways / Memory Tips

- **Exact few actions → custom role. IAM conditions can't remove permissions.**
  🧠 *"**Three buttons, custom key.**"*
- Related: **Q303**.

# Q121: Managed Instance Group Can't Create New Instances (Valid Template, Leftover Disks, autoDelete)

**Topic:** Compute Engine (managed instance groups, instance templates, persistent disk names, autoDelete)

## ❓ Question
> Your managed instance group raised an alert stating that new instance creation has failed to create new instances. You need to maintain the number of running instances specified by the template to be able to process expected application traffic. What should you do?
>
> **A.** Create an instance template that contains valid syntax which will be used by the instance group. Delete any persistent disks with the same name as instance names.
>
> **B.** Create an instance template that contains valid syntax that will be used by the instance group. Verify that the instance name and persistent disk name values are not the same in the template.
>
> **C.** Verify that the instance template being used by the instance group contains valid syntax. Delete any persistent disks with the same name as instance names. Set the disks.autoDelete property to true in the instance template.
>
> **D.** Delete the current instance template and replace it with a new instance template. Verify that the instance name and persistent disk name values are not the same in the template. Set the disks.autoDelete property to true in the instance template.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

> ℹ️ **Note:** This is the site's accepted (most voted) answer, but it's debated. Instance templates can't be edited after creation, so "set autoDelete in the template" really means using a template that has it. Some people pick A for that reason. The ideas to remember are: **check the template, delete leftover disks with the instance's name, and make disks auto-delete**.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A managed instance group alerted that it failed to create new instances.
- **What you must achieve:** Keep the number of running VMs that the template asks for.
- **The limits:** None stated.
- **What they're really asking:** What should you check or fix so new instances can be created?

**Clues in the question:**
- "**new instance creation has failed**": Google's troubleshooting lists two common causes: **invalid template syntax**, or a **leftover persistent disk with the same name** as the new instance.
- "**maintain the number of running instances**": fix the causes now, and stop them coming back with **disks.autoDelete=true** (disks are deleted with their VM, so names don't clash next time).

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Managed instance group (MIG) (review from Q057)
- **What it is:** A group of identical VMs created from **one instance template**. It recreates VMs automatically to keep the target size.
- **Looks like:** `gcloud compute instance-groups managed create web-mig --template=web-v3 --size=4`
- **Not to be confused with:** an unmanaged group.
- **Analogy:** 🏭 A **staffing agency** that always keeps 4 workers on shift.
- **In the online store:** The web tier MIG.

### 2. Leftover persistent disk name clash 🔑
- **What it is:** When a MIG recreates `web-mig-abcd`, it creates a boot disk named `web-mig-abcd`. If an **old disk with that name still exists** (autoDelete was off), creation **fails**.
- **Looks like:** `ERROR: The resource 'projects/shop/zones/us-central1-a/disks/web-mig-abcd' already exists`
- **Not to be confused with:** a quota error.
- **Analogy:** 🪪 Trying to print a new badge for "Desk 12", but an old "Desk 12" badge is still registered.
- **In the online store:** Old disks from replaced web VMs block new ones.

### 3. disks.autoDelete
- **What it is:** A disk setting: **true** = delete the disk when its VM is deleted.
- **Looks like:** `--create-disk=auto-delete=yes` / `"autoDelete": true` in the template
- **Not to be confused with:** snapshots.
- **Analogy:** 🗑️ Clearing out the desk when the worker leaves.
- **In the online store:** Web VM boot disks are disposable.

### 🔗 How they fit together
```
 MIG wants web-mig-abcd → create disk web-mig-abcd → ❌ "already exists" (old disk, autoDelete=false)
 Fix: valid template ✔ + delete leftover disks ✔ + autoDelete=true ✔ → creation works ✅
```

---

## 🌍 Real-World Scenario

After a template change, a MIG stops scaling up and shows "resource already exists" errors. The engineer checks the template, deletes the leftover boot disks named like the instances, and makes sure the template sets **autoDelete=true**. The group grows back to its target size.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create an instance template that contains valid syntax which will be used by the instance group. Delete any persistent disks with the same name as instance names.

**Wrong words:**
- ✔️ "valid syntax" and "Delete any persistent disks with the same name" fix today's failure.
- ❌ It doesn't set **autoDelete**, so leftover disks can block creation again next time.

📌 **When to use it:** Use it when a template has an error and leftover disks exist, as a one-time fix.
🏢 **Office example:** Removing the old badges today without changing the rule that leaves them behind.

### ❌ B
> **B.** Create an instance template that contains valid syntax that will be used by the instance group. Verify that the instance name and persistent disk name values are not the same in the template.

**Wrong words:**
- ❌ "**Verify that the instance name and persistent disk name values are not the same in the template**": a MIG names the boot disk after the instance by default. The clash comes from **leftover disks**, which this option never deletes.

📌 **When to use it:** Use custom disk names only in special templates.
🏢 **Office example:** Checking the badge form when the real problem is old badges still on file.

### ✅ C
> **C.** Verify that the instance template being used by the instance group contains valid syntax. Delete any persistent disks with the same name as instance names. Set the disks.autoDelete property to true in the instance template.

**Why it's correct:**
- ✔️ "**Verify that the instance template … contains valid syntax**" matches "**failed to create new instances**": a broken template is one cause.
- ✔️ "**Delete any persistent disks with the same name as instance names**" matches "**failed to create**": it removes the name clash that blocks new VMs.
- ✔️ "**Set the disks.autoDelete property to true**" matches "**maintain the number of running instances**": future disks are deleted with their VMs, so the clash doesn't come back.

📌 **When to use it:** Use it when replacement workers can't start because the old workers' stuff is still in the way.
🏢 **Office example:** Clearing out old badges and setting a rule that a worker's desk is cleared when they leave.

### ❌ D
> **D.** Delete the current instance template and replace it with a new instance template. Verify that the instance name and persistent disk name values are not the same in the template. Set the disks.autoDelete property to true in the instance template.

**Wrong words:**
- ❌ "**Delete the current instance template**": you can't delete a template that a MIG is still using, and replacing it doesn't remove the leftover disks.
- ❌ "**instance name and persistent disk name values are not the same**": not the real cause.

📌 **When to use it:** Use a new template when you deliberately change the VM setup (then roll it out).
🏢 **Office example:** Rewriting the whole staffing contract while old badges still block new hires.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute instance-groups managed list-errors web-mig --region=us-central1
# ... disks/web-mig-7k2p already exists
gcloud compute disks delete web-mig-7k2p --zone=us-central1-b
gcloud compute instance-templates create web-v4 --machine-type=e2-medium \
  --create-disk=boot=yes,image-family=debian-12,image-project=debian-cloud,auto-delete=yes
gcloud compute instance-groups managed set-instance-template web-mig --template=web-v4 --region=us-central1
```

---

## 🧠 Key Takeaways / Memory Tips

- **MIG can't create VMs → check the template, delete leftover same-name disks, set autoDelete=true.**
- Templates can't be edited; create a new one and point the MIG at it.
  🧠 *"**Old disk blocks new VM: delete it and auto-delete next time.**"*
- Related: **Q057** (MIG rolling update), **Q112** (snapshots).

# Q225: MIG Fails to Create New Instances (New Valid Template + Delete Disks With Conflicting Names)

**Topic:** Compute Engine (MIG troubleshooting)

## ❓ Question
> Your managed instance group raised an alert stating that new instance creation has failed to create new instances. You need to solve the instance creation problem. What should you do?
>
> **A.** Create an instance template that contains valid syntax which will be used by the instance group. Delete any persistent disks with the same name as instance names.
>
> **B.** Create an instance template that contains valid syntax that will be used by the instance group. Verify that the instance name and persistent disk name values are not the same in the template.
>
> **C.** Verify that the instance template being used by the instance group contains valid syntax. Delete any persistent disks with the same name as instance names. Set the disks.autoDelete property to true in the instance template.
>
> **D.** Delete the current instance template and replace it with a new instance template. Verify that the instance name and persistent disk name values are not the same in the template. Set the disks.autoDelete property to true in the instance template.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

> ℹ️ **Note:** Most Voted is **A**. Instance templates **can't be edited**, so you create a new valid one (C and D change an existing template). A common cause of failure is a leftover **disk with the same name** as the VM the MIG wants to create; deleting it fixes that.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A managed instance group alerted that it failed to create new instances.
- **What you must achieve:** Fix the problem so new instances can be created.
- **The limits:** None stated.
- **What they're really asking:** What should you check or change to fix instance creation?

**Clues in the question:**
- Templates are **immutable** → **create a new** template with valid syntax.
- A leftover **persistent disk** named like the new VM blocks creation → **delete it**.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Instance template (immutable) 🔑
- **What it is:** A saved VM recipe for a MIG. You can't edit it; you create a new one and point the MIG at it.
- **Looks like:** `gcloud compute instance-templates create web-v2 …` + `set-instance-template`
- **Not to be confused with:** an instance.
- **Analogy:** 📄 A printed recipe card.
- **In the online store:** web-v2 template.

### 2. Disk name conflict
- **What it is:** The MIG names a new VM's boot disk after the VM. If an old disk has that name, creation fails.
- **Looks like:** old disk `web-mig-abcd` left behind
- **Not to be confused with:** —
- **Analogy:** 🏷️ A name tag already taken.
- **In the online store:** —

### 🔗 How they fit together
```
 new valid template → MIG ✅
 delete leftover disk named web-mig-abcd → creation succeeds ✅
```

---

## 🌍 Real-World Scenario

A MIG keeps failing to create VMs. The engineer finds the template has a typo and an old disk named like the next VM. They create a **new template** and **delete the leftover disk**.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create an instance template that contains valid syntax which will be used by the instance group. Delete any persistent disks with the same name as instance names.

**Why it's correct:**
- ✔️ "**Create an instance template that contains valid syntax**" matches "**solve the instance creation problem**": templates can't be edited, so you create a new one.
- ✔️ "**Delete any persistent disks with the same name as instance names**": removes the name clash that blocks new VMs.

📌 **When to use it:** Use it when the automatic hiring of new machines keeps failing and you need a clean recipe and no name clashes.
🏢 **Office example:** Printing a corrected recipe card and removing an old name tag that's blocking a new employee's desk.

### ❌ B
> **B.** Create an instance template that contains valid syntax that will be used by the instance group. Verify that the instance name and persistent disk name values are not the same in the template.

**Wrong words:**
- ✔️ "Create an instance template … valid syntax" is right.
- ❌ "**Verify that the instance name and persistent disk name values are not the same in the template**": the template doesn't hold fixed instance/disk names; the clash is with existing disks.

📌 **When to use it:** **Not a real fix.**
🏢 **Office example:** Checking the recipe for a name that isn't on it.

### ❌ C
> **C.** Verify that the instance template being used by the instance group contains valid syntax. Delete any persistent disks with the same name as instance names. Set the disks.autoDelete property to true in the instance template.

**Wrong words:**
- ❌ "**Verify that the instance template being used … contains valid syntax**": if it's invalid you can't fix it in place.
- ❌ "**Set the disks.autoDelete property … in the instance template**": you can't edit an existing template.

📌 **When to use it:** Use autoDelete in **new** templates to avoid leftover disks.
🏢 **Office example:** Correcting a laminated recipe card with a pen.

### ❌ D
> **D.** Delete the current instance template and replace it with a new instance template. Verify that the instance name and persistent disk name values are not the same in the template. Set the disks.autoDelete property to true in the instance template.

**Wrong words:**
- ❌ "**Delete the current instance template**": can't delete a template that a MIG is using.
- ❌ "**instance name and persistent disk name values … in the template**": not how templates work.

📌 **When to use it:** **Never use this** order of steps.
🏢 **Office example:** Throwing away the recipe while the kitchen is using it.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud compute instance-templates create checkout-v3 …` → `gcloud compute instance-groups managed set-instance-template checkout-mig --template=checkout-v3` → `gcloud compute disks delete checkout-mig-x7k2`

---

## 🧠 Key Takeaways / Memory Tips

- **MIG creation fails → new valid template (templates are immutable) + delete disks with conflicting names.**
  🧠 *"**New recipe, clear the name tags.**"*
- Related: **Q221**, **Q224**.

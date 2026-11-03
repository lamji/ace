# Q133: VM in One Project Writes Reports to a Bucket in Another (Storage Object Creator for the VM's Service Account)

**Topic:** IAM / Cloud Storage (cross-project service account access)

## ❓ Question
> An application generates daily reports in a Compute Engine virtual machine (VM). The VM is in the project corp-iot-insights. Your team operates only in the project corp-aggregate-reports and needs a copy of the daily exports in the bucket corp-aggregate-reports-storage. You want to configure access so that the daily reports from the VM are available in the bucket corp-aggregate-reports-storage and use as few steps as possible while following Google-recommended practices. What should you do?
>
> **A.** Move both projects under the same folder.
>
> **B.** Grant the VM Service Account the role Storage Object Creator on corp-aggregate-reports-storage.
>
> **C.** Create a Shared VPC network between both projects. Grant the VM Service Account the role Storage Object Creator on corp-iot-insights.
>
> **D.** Make corp-aggregate-reports-storage public and create a folder with a pseudo-randomized suffix name. Share the folder with the IoT team.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** A VM in **project A** must write report files into a bucket in **project B**. Fewest steps, best practice.

**Clues in the question:**
- "**available in the bucket corp-aggregate-reports-storage**": grant permission **on that bucket**.
- "**from the VM**": the member is the **VM's service account**.
- Writing new files = **Storage Object Creator** (least privilege).

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. roles/storage.objectCreator 🔑
- **What it is:** A role that can **create (upload) objects** in a bucket, but not read, overwrite or delete them.
- **Looks like:** `gcloud storage buckets add-iam-policy-binding gs://corp-aggregate-reports-storage --member=serviceAccount:vm-sa@corp-iot-insights.iam.gserviceaccount.com --role=roles/storage.objectCreator`
- **Not to be confused with:** objectAdmin (full control).
- **Analogy:** 📮 A **drop-box slot**: you can put letters in, not take them out.
- **In the online store:** Order exports land in the finance bucket.

### 2. Cross-project grant (review from Q116)
- **What it is:** Grant the role on the resource (here the bucket) to a service account from another project.
- **Looks like:** member = other project's SA
- **Not to be confused with:** moving projects.
- **Analogy:** 🪪 HQ adds a branch robot to its drop-box list.
- **In the online store:** IoT VM writes to reports bucket.

### 🔗 How they fit together
```
 corp-iot-insights: VM (runs as vm-sa) ──writes──► gs://corp-aggregate-reports-storage (corp-aggregate-reports)
                                                    IAM on bucket: vm-sa → Storage Object Creator ✅
```

---

## 🌍 Real-World Scenario

An IoT project produces daily reports that the analytics team needs in their own bucket. The bucket owner grants the IoT VM's **service account** the **Storage Object Creator** role on the bucket. The VM's script runs `gsutil cp report.csv gs://…` every night.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Move both projects under the same folder.

**Wrong words:**
- ❌ "**Move both projects under the same folder**": folders organize projects. They don't give a VM permission to write to a bucket.

📌 **When to use it:** Use folders to group projects and apply shared policies.
🏢 **Office example:** Moving two departments to the same floor doesn't give one a key to the other's mailbox.

### ✅ B
> **B.** Grant the VM Service Account the role Storage Object Creator on corp-aggregate-reports-storage.

**Why it's correct:**
- ✔️ "**Grant the VM Service Account**" matches "**daily reports from the VM**": the VM writes as its service account.
- ✔️ "**Storage Object Creator**" matches "**available in the bucket**" + "**Google-recommended practices**": just enough to upload files.
- ✔️ "**on corp-aggregate-reports-storage**" matches "**as few steps as possible**": one grant on the target bucket.

📌 **When to use it:** Use it when a program elsewhere needs to drop files into your storage.
🏢 **Office example:** Adding the branch's delivery robot to HQ's drop-box list.

### ❌ C
> **C.** Create a Shared VPC network between both projects. Grant the VM Service Account the role Storage Object Creator on corp-iot-insights.

**Wrong words:**
- ❌ "**Create a Shared VPC network**": networking isn't needed to reach Cloud Storage.
- ❌ "**Storage Object Creator on corp-iot-insights**": the role is on the wrong project, not the target bucket.

📌 **When to use it:** Use Shared VPC when projects should share one network.
🏢 **Office example:** Building a shared hallway and giving a key to your own mailbox.

### ❌ D
> **D.** Make corp-aggregate-reports-storage public and create a folder with a pseudo-randomized suffix name. Share the folder with the IoT team.

**Wrong words:**
- ❌ "**Make corp-aggregate-reports-storage public**": anyone on the internet could access it. A random folder name isn't security.

📌 **When to use it:** **Never use this.** Grant a role to the service account (B).
🏢 **Office example:** Leaving the mailbox open on the street and hiding it behind a weird name.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud storage buckets add-iam-policy-binding gs://shopnow-finance-reports \
  --member=serviceAccount:orders-vm@shopnow-orders.iam.gserviceaccount.com \
  --role=roles/storage.objectCreator
```
Nightly on the orders VM: `gsutil cp /exports/orders-$(date +%F).csv gs://shopnow-finance-reports/`

---

## 🧠 Key Takeaways / Memory Tips

- **Program in project A writes to a bucket in project B → grant its service account a role on that bucket.**
- Upload only → Storage Object Creator.
  🧠 *"**Grant the robot a slot on the target bucket.**"*
- Related: **Q116**, **Q130** (cross-project service accounts), **Q071**.

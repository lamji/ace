# G037: Run a Cloud Run Service Whenever Someone Creates a VM, Using Audit Log Events (Eventarc Trigger)

**Topic:** Serverless (Eventarc audit log triggers)
**Exam guide section:** 2.1 Deploying an application to serverless compute platforms, including for the processing of Google Cloud events (Eventarc)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your security team wants a Cloud Run service to run automatically every time a Compute Engine VM is created in a project, so that it can check the VM's configuration. You want a managed, event-driven solution with minimal code for routing events. What should you do?
>
> **A.** Create a Cloud Scheduler job that calls the Cloud Run service every hour to list all VMs.
>
> **B.** Ask developers to call the Cloud Run service manually after creating a VM.
>
> **C.** Create an Eventarc trigger for Cloud Audit Logs events with serviceName compute.googleapis.com and the VM insert methodName, with the Cloud Run service as the destination.
>
> **D.** Create a log-based metric for VM creation and an alert that emails the security team.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Security has a small program on Cloud Run (Google's serverless container service) that checks how a VM (virtual machine) is configured.
- **What you must achieve:** Make that program run automatically every time someone creates a VM in the project.
- **The limits:** It should be managed and event-driven (reacting to events as they happen), with little routing code to write.
- **What they're really asking:** Which Google Cloud service turns "a VM was created" into a call to Cloud Run?

**Clues in the question:**
- "**every time a Compute Engine VM is created**": VM creation is recorded in **Admin Activity audit logs**.
- "**managed, event-driven**" + "**Cloud Run**": **Eventarc** routes Cloud Audit Logs events to Cloud Run.

**Exam topic:** Serverless and events (exam guide section 2.1).

---

## 📚 Key Terms Explained

### 1. Eventarc 🔑
- **What it is:** A managed event-routing service. It delivers events from Google Cloud sources (Cloud Audit Logs, Cloud Storage, Pub/Sub and more) to destinations like Cloud Run, using **triggers** with filters.
- **Looks like:** `gcloud eventarc triggers create vm-created --location=us-central1 --destination-run-service=vm-checker --event-filters=type=google.cloud.audit.log.v1.written --event-filters=serviceName=compute.googleapis.com --event-filters=methodName=v1.compute.instances.insert --service-account=eventarc-sa@p.iam.gserviceaccount.com`
- **Not to be confused with:** Cloud Scheduler, which runs things on a clock, not when events happen.
- **Analogy:** 🔔 A doorbell wired to ring the security desk whenever a new office is opened.
- **In the online store:** Triggers `vm-checker` on new VMs.

### 2. Admin Activity audit log
- **What it is:** An always-on log of configuration changes (create, delete, set IAM) made through Google Cloud APIs.
- **Looks like:** `methodName: v1.compute.instances.insert`, `principalEmail: dev@shopnow.com`
- **Not to be confused with:** Data Access logs (data reads and writes, often off by default).
- **Analogy:** 📒 The building's change register.
- **In the online store:** Records every VM creation.

### 🔗 How they fit together
```
 dev creates VM ─► Admin Activity audit log ─► Eventarc trigger (filters) ─► Cloud Run vm-checker ✅
```

---

## 🌍 Real-World Scenario

A company requires every VM to have no public IP and to carry an owner label. An **Eventarc** trigger on `compute.instances.insert` audit events calls `vm-checker`, which posts a warning to Slack within a minute of a bad VM being created.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a Cloud Scheduler job that calls the Cloud Run service every hour to list all VMs.

**Wrong words:**
- ❌ "**every hour**": a VM could sit misconfigured for an hour. Polling isn't event-driven.

📌 **When to use it:** Use Cloud Scheduler for timed jobs like nightly reports.
🏢 **Office example:** Walking the building every hour looking for new offices.

### ❌ B
> **B.** Ask developers to call the Cloud Run service manually after creating a VM.

**Wrong words:**
- ❌ "**manually**": people forget, so it isn't automatic or enforced.

📌 **When to use it:** Never rely on manual steps for security checks.
🏢 **Office example:** Asking people to report themselves.

### ✅ C
> **C.** Create an Eventarc trigger for Cloud Audit Logs events with serviceName compute.googleapis.com and the VM insert methodName, with the Cloud Run service as the destination.

**Why it's correct:**
- ✔️ "**Eventarc trigger for Cloud Audit Logs events**" matches "**managed, event-driven solution with minimal code for routing events**".
- ✔️ "**serviceName compute.googleapis.com and the VM insert methodName**" matches "**every time a Compute Engine VM is created**".
- ✔️ "**Cloud Run service as the destination**" matches "**a Cloud Run service to run**".

📌 **When to use it:** Use it when a program should start automatically the moment a certain thing happens in your cloud.
🏢 **Office example:** A doorbell that rings the inspection team every time a new office opens.

### ❌ D
> **D.** Create a log-based metric for VM creation and an alert that emails the security team.

**Wrong words:**
- ✔️ It detects VM creation.
- ❌ "**alert that emails the security team**": it notifies people but doesn't run the Cloud Run service.

📌 **When to use it:** Use log-based alerts when a person just needs to know.
🏢 **Office example:** A bell rings, but nobody runs the inspection.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: Eventarc trigger `vm-created` → Cloud Run `vm-checker` checks for an external IP and the `owner` label, then posts to #security.

---

## 🧠 Key Takeaways / Memory Tips

- **React to Google Cloud events (audit logs, Storage, Pub/Sub) with Cloud Run → Eventarc trigger.**
  🧠 *"**Event happens → Eventarc routes it.**"*
- Related: **Q305**, **Q262**, **G032**.

# Q047: Compute Engine restart and host maintenance settings

**Topic:** Compute Engine instance templates, restart behavior, and host maintenance

## ❓ Question
> You want to configure 10 Compute Engine instances for availability when maintenance occurs. Your requirements state that these instances should attempt to automatically restart if they crash. Also, the instances should be highly available including during system maintenance. What should you do?
>
> **A.** Create an instance template for the instances. Set the “Automatic Restart” to on. Set the “On-host maintenance” to Migrate VM instance. Add the instance template to an instance group.
>
> **B.** Create an instance template for the instances. Set the “Automatic Restart” to off. Set the “On-host maintenance” to Terminate VM instances. Add the instance template to an instance group.
>
> **C.** Create an instance group for the instances. Set the “Autohealing” health check to healthy (HTTP).
>
> **D.** Create an instance group for the instance. Verify that the “Advanced creation options” setting for “do not retry machine creation” is set to off.

**My answer:** C  
**Correct answer:** A — Create an instance template for the instances. Set the “Automatic Restart” to on. Set the “On-host maintenance” to Migrate VM instance. Add the instance template to an instance group.  
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **C** is a reasonable thought because autohealing is related to keeping applications available. The question, however, specifically asks for two VM behaviors: restart after a crash and remain available during host maintenance. C's HTTP health check detects an unhealthy application and can cause a managed instance group (MIG) to replace a VM; it does not set either of those two host scheduling behaviors.

**Correct answer: A — Create an instance template for the instances. Set the “Automatic Restart” to on. Set the “On-host maintenance” to Migrate VM instance. Add the instance template to an instance group.** Automatic restart asks Compute Engine to restart the VM after eligible crashes or host events. “Migrate VM instance” lets Compute Engine move a supported VM to another host during planned maintenance, helping it continue running. An instance template lets a group create the 10 instances with the same settings.

## 2. 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You need 10 Compute Engine VMs.
- **What you must achieve:** They must restart by themselves if they crash, and keep running while Google does maintenance on the physical servers underneath.
- **The limits:** They must be highly available.
- **What they're really asking:** How do you create and configure the VMs to meet both needs?

Clues:
- **“10 Compute Engine instances”**: use a repeatable template and an instance group to manage multiple VMs.
- **“automatically restart if they crash”**: turn **Automatic Restart** on.
- **“highly available including during system maintenance”**: choose **Migrate VM instance** for host maintenance, where the VM type supports live migration.

**Exam domain:** Compute Engine, instance groups, VM restart scheduling, and host maintenance. “High availability” here means reducing interruption; it does not promise zero interruption for every kind of failure.

## 2.5 📚 Key Terms Explained

### Compute Engine instance / VM
- **What it is:** A virtual machine (VM) is a software-based computer running in Google Cloud. An instance is one running VM.
- **Analogy:** One employee's assigned computer in an office.
- **In the online store:** A VM can run the store's API or background order processor.

### Instance template
- **What it is:** A reusable specification for creating VMs with consistent settings, such as machine type, image, disks, and scheduling behavior.
- **Analogy:** A standard equipment order form used to set up each new workstation.
- **In the online store:** The operations team defines one template for the store's API servers, then creates matching instances from it.

### Instance group
- **What it is:** A collection of VM instances managed together. A managed instance group can create and maintain instances based on a template.
- **Analogy:** A team of identical workstations managed from one inventory list.
- **In the online store:** A managed group runs multiple copies of the store API so requests can be handled by more than one VM.

### Automatic Restart
- **What it is:** A VM scheduling setting that lets Compute Engine restart an instance after certain crashes, host errors, or programmed stops. It does not restart a VM after every manual stop or every possible outage.
- **Analogy:** A computer configured to turn itself back on after an unexpected shutdown.
- **In the online store:** It helps bring a store API VM back after an eligible underlying failure.

### Host / system maintenance
- **What it is:** Google sometimes maintains the physical server that runs a VM. The VM's host maintenance policy controls what happens to it during that work.
- **Analogy:** Building maintenance that requires moving a worker's desk and computer temporarily.
- **In the online store:** Maintenance on a physical host should cause the store API VM to move where supported, rather than simply remain stopped.

### Live migration (“Migrate VM instance”)
- **What it is:** For supported VM configurations, Compute Engine moves the running VM to another host during maintenance, aiming to keep it running with little disruption.
- **Analogy:** Moving a worker's desk to another room while keeping their work session going.
- **In the online store:** The API VM can be moved during scheduled host work so the store can continue serving shoppers.

### Autohealing and HTTP health check
- **What it is:** A managed instance group's autohealing policy checks whether an application responds as healthy. If it fails the configured checks, the group can recreate that VM. An HTTP check tests an application endpoint over web traffic.
- **Analogy:** A supervisor checks whether a workstation's service is responding; if it is broken, the workstation is replaced.
- **In the online store:** An HTTP check can test the API's `/health` endpoint and prompt replacement if the app is stuck.

### High availability
- **What it is:** Designing a service to remain usable despite some failures or maintenance. Multiple instances and recovery policies reduce the chance that one VM interruption takes down the service.
- **Analogy:** Having several staff members able to answer the same office phone line.
- **In the online store:** Multiple API VMs behind a load balancer can keep checkout available if one VM needs repair.

### How the pieces fit

```text
Instance template (shared VM settings)
                 ↓
Managed instance group (creates/manages 10 VMs)
                 ↓
Automatic restart + host maintenance migration
                 ↓
VMs recover from eligible crashes and move during supported maintenance
```

An autohealing HTTP check is an additional application recovery mechanism; it is not a substitute for the restart and maintenance policies.

## 3. 🌍 Real-World Scenario

A company runs ten web-service VMs. A physical host needs scheduled maintenance, and another VM might crash unexpectedly. The engineer wants Google Cloud to move supported VMs during planned host maintenance and restart them after eligible crashes. A shared instance template ensures every VM has those same scheduling settings. Autohealing can separately be configured if the application itself becomes unhealthy.

## 4. 🔍 Option-by-Option Breakdown

### ✅ A — Correct

> **A.** Create an instance template for the instances. Set the “Automatic Restart” to on. Set the “On-host maintenance” to Migrate VM instance. Add the instance template to an instance group.

**Why it is correct:** This matches both explicit requirements. **Automatic Restart on** tells Compute Engine to try restarting the VM after eligible crashes or host errors. **Migrate VM instance** tells Compute Engine to live-migrate supported VMs during host maintenance, which is the recommended availability-oriented behavior for most supported VM types. The instance template packages the settings so the instance group can create consistent instances. For ten VMs, a managed instance group can manage the fleet from that template.

Live migration has limits: some VM types or attached hardware do not support it and must terminate during maintenance. The question gives no such exception, so the standard exam choice is migration.

📌 When to use it: Use it when computers should restart after crashes and move during planned building work.  
🏢 Office example: Set up ten staff computers with automatic recovery and move them during scheduled electrical maintenance.

### ❌ B

> **B.** Create an instance template for the instances. Set the “Automatic Restart” to off. Set the “On-host maintenance” to Terminate VM instances. Add the instance template to an instance group.

**Why it is wrong:** It reverses both requested settings. **Automatic Restart off** means Compute Engine will not automatically restart the VM after eligible failures. **Terminate VM instances** stops the VM for host maintenance instead of moving it to another host. The group and template provide repeatable management, but they cannot make these contradictory settings meet the availability requirements. This would make interruptions more likely and may leave recovery to other mechanisms or a person.

📌 When to use it: Use it when a computer must stop and must stay off until a person decides what to do.  
🏢 Office example: Shut down a test workstation during repairs so an employee can inspect it before restarting.

### ❌ C — Your answer

> **C.** Create an instance group for the instances. Set the “Autohealing” health check to healthy (HTTP).

**Why it is wrong:** Autohealing checks application health, not the VM's **Automatic Restart** or **On-host maintenance** settings. If an HTTP endpoint fails long enough to be considered unhealthy, a managed instance group can recreate the VM. But this option does not explicitly configure automatic restart after a crash, nor does it choose live migration during system maintenance. It also gives no HTTP endpoint or probe policy to tune; simply choosing HTTP is not a universal guarantee that an app is healthy. C describes a useful additional safety net for application failures, but it misses the two settings named by the question.

📌 When to use it: Use it when a service should be replaced if it stops answering the office's check call.  
🏢 Office example: Have a supervisor replace a broken reception phone when a scheduled test call gets no answer.

### ❌ D

> **D.** Create an instance group for the instance. Verify that the “Advanced creation options” setting for “do not retry machine creation” is set to off.

**Why it is wrong:** This is about retrying a failed **creation attempt**, not how an already running VM recovers from a crash or behaves during host maintenance. Allowing a creation attempt to retry can help if provisioning a VM fails temporarily, but it does not enable automatic restart or live migration. It also speaks of an instance group for “the instance,” rather than establishing the specific restart and maintenance policies for all ten instances.

📌 When to use it: Use it when a computer setup attempt may need another try after a temporary setup problem.  
🏢 Office example: Ask IT to retry setting up a new workstation if the first installation fails.

## 5. 🛒 E-Commerce Full-Stack Example

An online store runs its checkout API on ten Compute Engine VMs in a managed instance group. The instance template gives each VM the same image and settings, including Automatic Restart on and host maintenance migration. If a supported VM's host needs planned maintenance, Google Cloud moves it to another host; if a VM crashes for an eligible reason, Compute Engine attempts to restart it. The other API VMs can continue serving traffic during the interruption. An HTTP autohealing check on `/health` can be added separately to detect an application that is running but no longer responding correctly.

## 6. 🧠 Key Takeaway / Memory Tip

For **VM crash recovery**, think **Automatic Restart on**. For **planned host maintenance**, think **Migrate VM instance** when supported; an HTTP autohealing check repairs an unhealthy application but does not replace those scheduling settings.

**Current Google Cloud documentation:** [Set the host maintenance policy for a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options), [About repairing VMs in a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair), and [Set up an application-based health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

# G010: Contractors Get Identical Dev Environments Inside Your VPC, No Code on Laptops (Cloud Workstations)

**Topic:** Developer environments (Cloud Workstations)
**Exam guide section:** 3.1 Managing compute: Managing developer environments (e.g., Cloud Workstations)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your company is onboarding 40 contractors to work on the payment service. Security requires that source code is never stored on contractors' laptops, every developer uses the same preconfigured tools and IDE, and development environments run inside your VPC. You want a managed solution. What should you do?
>
> **A.** Give each contractor a Compute Engine VM with an external IP address, and share one SSH key with all of them.
>
> **B.** Use Cloud Workstations with a workstation configuration that defines the container image, machine type, and VPC, and grant contractors access to their workstations.
>
> **C.** Send the contractors a setup script, and require them to install the tools on laptops with full-disk encryption.
>
> **D.** Have all contractors use Cloud Shell for development.

**My answer:** — (not tried yet)
**Correct answer:** B
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** 40 outside contractors are joining to write code for the payment system.
- **What you must achieve:** Give each one a coding setup that's identical for everyone, with the same tools and the same code editor (IDE).
- **The limits:** Code must never land on their laptops, the setups must run inside your company's private cloud network (VPC), and it should be a managed service.
- **What they're really asking:** Which Google Cloud service gives developers ready-made, secure coding machines in the cloud?

**Clues in the question:**
- "**source code is never stored on contractors' laptops**": developers must work on remote machines, through the browser or a remote IDE.
- "**same preconfigured tools and IDE**": a **workstation configuration** (one template for everyone).
- "**inside your VPC**" + "**managed**": Cloud Workstations runs in your VPC and Google manages it.

**Exam topic:** Developer environments (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. Cloud Workstations 🔑
- **What it is:** A managed service that gives each developer a cloud machine for coding, opened in the browser or from a local IDE. Admins define a **workstation configuration** (container image with tools, machine type, disk, network). It runs in your VPC.
- **Looks like:** Config `payments-dev`: image `us-docker.pkg.dev/.../code-oss:latest`, `e2-standard-8`, network `corp-vpc`
- **Not to be confused with:** Cloud Shell, which is a free, small, temporary personal terminal, not a managed team environment in your VPC.
- **Analogy:** 💻 Company-owned desks in a secure office that look the same for every temp worker.
- **In the online store:** Payment-service contractors code in the browser.

### 2. Workstation configuration
- **What it is:** The template for workstations: image, machine size, idle timeout, network, and who can use them.
- **Looks like:** `gcloud workstations configs create payments-dev --cluster=dev-cluster --region=us-central1 --machine-type=e2-standard-8`
- **Not to be confused with:** An individual workstation. One config can create many workstations.
- **Analogy:** 📋 The standard desk setup sheet.
- **In the online store:** One config for all 40 contractors.

### 3. Cloud Shell
- **What it is:** A free browser terminal with a small, temporary VM and 5 GB of home storage, tied to your own account.
- **Looks like:** `ana@cloudshell:~$`
- **Not to be confused with:** A secure team dev environment in your VPC.
- **Analogy:** 🖊️ A shared pen at the counter.
- **In the online store:** Quick `gcloud` commands by admins.

### 🔗 How they fit together
```
 Contractor browser ──► Cloud Workstations (config payments-dev, in corp-vpc) ──► Git repo
                         code stays in the cloud ✅  laptop holds nothing
```

---

## 🌍 Real-World Scenario

A fintech company brings in an outside agency. Instead of shipping laptops with code, the platform team creates a **Cloud Workstations** configuration with the company's IDE image in the corporate VPC. Contractors start coding on day one in the browser, and access ends the moment their IAM access is removed.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Give each contractor a Compute Engine VM with an external IP address, and share one SSH key with all of them.

**Wrong words:**
- ❌ "**external IP address**": exposes dev machines to the internet.
- ❌ "**share one SSH key with all of them**": no individual accountability, and it can't be revoked per person.
- ❌ No standard tools or IDE are defined.

📌 **When to use it:** Never share one SSH key. Use per-user access, such as Cloud Workstations or OS Login.
🏢 **Office example:** Handing all temps one copied master key.

### ✅ B
> **B.** Use Cloud Workstations with a workstation configuration that defines the container image, machine type, and VPC, and grant contractors access to their workstations.

**Why it's correct:**
- ✔️ "**Cloud Workstations**" matches "**managed solution**" and "**never stored on contractors' laptops**": the code lives on cloud workstations.
- ✔️ "**workstation configuration that defines the container image, machine type**" matches "**same preconfigured tools and IDE**".
- ✔️ "**and VPC**" matches "**run inside your VPC**".

📌 **When to use it:** Use it when many developers need identical, secure coding setups that you control centrally.
🏢 **Office example:** Giving every temp an identical company desk in the secure office instead of letting them work from home.

### ❌ C
> **C.** Send the contractors a setup script, and require them to install the tools on laptops with full-disk encryption.

**Wrong words:**
- ❌ "**install the tools on laptops**": the code ends up on laptops, which breaks "**never stored on contractors' laptops**".
- ❌ "**setup script**": environments drift apart and aren't managed.

📌 **When to use it:** Use it when your own employees work on company-managed laptops and storing code locally is allowed.
🏢 **Office example:** Sending files home with temps and hoping they lock them up.

### ❌ D
> **D.** Have all contractors use Cloud Shell for development.

**Wrong words:**
- ✔️ Code doesn't stay on the laptop.
- ❌ "**Cloud Shell**": a small temporary personal VM, not in your VPC and not centrally configured with your tools.

📌 **When to use it:** Use it for quick command-line tasks in the console.
🏢 **Office example:** Borrowing the reception desk computer for a minute.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** payments team:
- Workstation cluster `dev-cluster` in `corp-vpc`; config `payments-dev` uses a Code OSS image with Node, Python and the payments SDK.
- Contractors get the `roles/workstations.user` role.
- The repo is reachable only from inside the VPC.

---

## 🧠 Key Takeaways / Memory Tips

- **Standard, secure, managed developer environments, no code on laptops → Cloud Workstations.**
  🧠 *"**Code in the cloud desk, not on the laptop.**"*
- Related: **G009**, **Q191**.

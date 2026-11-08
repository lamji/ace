# Q073: Logging Into a Windows VM With RDP (gcloud compute reset-windows-password)

**Topic:** Compute Engine (Windows VMs, RDP, Windows passwords, metadata, service account keys)

## ❓ Question
> You are setting up a Windows VM on Compute Engine and want to make sure you can log in to the VM via RDP. What should you do?
>
> **A.** After the VM has been created, use your Google Account credentials to log in into the VM.
>
> **B.** After the VM has been created, use gcloud compute reset-windows-password to retrieve the login credentials for the VM.
>
> **C.** When creating the VM, add metadata to the instance using 'windows-password' as the key and a password as the value.
>
> **D.** After the VM has been created, download the JSON private key for the default Compute Engine service account. Use the credentials in the JSON file to log in to the VM.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are setting up a Windows VM on Compute Engine.
- **What you must achieve:** Log in to it with RDP (Remote Desktop).
- **The limits:** None stated.
- **What they're really asking:** What do you need to set up to log in with RDP?

**Clues in the question:**
- "**Windows VM**": Windows uses a **username + password**, not SSH keys like Linux.
- "**log in to the VM via RDP**": you need Windows login credentials for that VM.
- Google provides a built-in way: **`gcloud compute reset-windows-password`** (or the "Set Windows password" button in the console), which creates a user and gives you its password.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1️⃣ RDP (Remote Desktop Protocol)
- **What it is:** The standard way to **see and control a Windows computer's desktop** over the network. You open the Remote Desktop app, enter the VM's IP, a username and a password.
- **Looks like:** Remote Desktop Connection → `34.123.45.67` → user `ana` → password `••••••`
- **Not to be confused with:** SSH, which is a text terminal used mostly for Linux.
- **Analogy:** 🖥️ **Sitting at the office computer from home**, seeing its screen.
- **In the online store:** Logging into the Windows reporting server to check a report job.

### 2️⃣ `gcloud compute reset-windows-password` 🔑
- **What it is:** A command that **creates a Windows user (or resets its password) on the VM** and **shows you the new password**. Google sends it securely to the VM's guest agent; it's never stored in plain text.
- **Looks like:**
  ```bash
  gcloud compute reset-windows-password win-reports --zone=us-central1-a --user=ana
  # ip_address: 34.123.45.67
  # password:   x7#Kq9!mPz2L
  # username:   ana
  ```
- **Not to be confused with:** your Google Account password. This is a **Windows** password for **that VM only**.
- **Analogy:** 🔐 **IT creating a new login** for you on a company PC and handing you the password in a sealed envelope.
- **In the online store:** The ops engineer gets a login for the Windows reporting server.

### 3️⃣ Google Account credentials
- **What it is:** Your Google email + password, used to sign in to the **Google Cloud console**.
- **Not to be confused with:** a Windows login. Windows on the VM doesn't know your Google password.
- **Analogy:** 🪪 Your **building ID card**. It opens the front door, not the PC's login screen.

### 4️⃣ Instance metadata
- **What it is:** Key-value settings attached to a VM (startup scripts, SSH keys for Linux, etc.).
- **Looks like:** `startup-script = ...`, `enable-oslogin = TRUE`
- **Not to be confused with:** a place for passwords. There's **no** `windows-password` key, and passwords in metadata would be readable by anyone with view access.
- **Analogy:** 🏷️ A **label on the PC**. You wouldn't write the password on it.

### 5️⃣ Service account JSON key (review from Q070)
- **What it is:** A file that lets an **app** call Google **APIs** as a service account.
- **Not to be confused with:** a Windows login. It doesn't log anyone into a VM's desktop.
- **Analogy:** 🤖 The **robot's API badge**. It doesn't unlock a human's desktop.

### 🔗 How they fit together
```
 You ──gcloud compute reset-windows-password──► 🖥️ Windows VM (creates user "ana", new password)
     ◄──────────── username + password ────────
 You ──RDP (IP, ana, password)──► Windows desktop ✅
```

---

## 🌍 Real-World Scenario

A team runs a Windows-only tool (an old reporting app, a .NET service) on Compute Engine. After creating the VM, the admin clicks **"Set Windows password"** in the console (or runs the gcloud command), copies the generated password into a password manager, and connects with Remote Desktop.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** After the VM has been created, use your Google Account credentials to log in into the VM.

**Wrong words:**
- ❌ "**use your Google Account credentials to log in into the VM**": Windows on the VM doesn't know your Google account. Your Google login is for the **Cloud console**, not the VM's Windows desktop.

📌 **When to use it:** Use your Google Account to sign in to the Google Cloud console.
🏢 **Office example:** Using your building ID card to log in to a PC. It opens the front door, not the computer.

### ✅ B
> **B.** After the VM has been created, use gcloud compute reset-windows-password to retrieve the login credentials for the VM.

**Why it's correct:**
- ✔️ "**gcloud compute reset-windows-password**" matches "**Windows VM on Compute Engine**": it's Google's built-in tool for creating a Windows login on a Compute Engine VM.
- ✔️ "**to retrieve the login credentials for the VM**" matches "**log in to the VM via RDP**": you get a username and password, which is exactly what RDP asks for.
- ✔️ "**After the VM has been created**": the command talks to the running VM's agent to set the password.

📌 **When to use it:** Use it when you need a username and password to log in to a Windows computer remotely.
🏢 **Office example:** IT creates your login on a company PC and hands you the password.

### ❌ C
> **C.** When creating the VM, add metadata to the instance using 'windows-password' as the key and a password as the value.

**Wrong words:**
- ❌ "**add metadata … using 'windows-password' as the key**": there's **no such metadata key**; Windows won't pick it up.
- ❌ "**a password as the value**": metadata is visible to anyone who can view the VM, so storing a password there is insecure.

📌 **When to use it:** **Never use this.** Use B to get a Windows password.
🏢 **Office example:** Writing the PC password on a sticky note on the monitor.

### ❌ D
> **D.** After the VM has been created, download the JSON private key for the default Compute Engine service account. Use the credentials in the JSON file to log in to the VM.

**Wrong words:**
- ❌ "**download the JSON private key for the default Compute Engine service account**": creates a risky key file for no reason.
- ❌ "**Use the credentials in the JSON file to log in to the VM**": a service account key is for **apps calling Google APIs**, not for logging in to a Windows desktop.

📌 **When to use it:** **Never use this** to log in to a VM. Use B.
🏢 **Office example:** Trying to log in to your PC with the office robot's badge.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow runs a Windows-only accounting export tool on `win-reports`.

```bash
gcloud compute instances create win-reports --zone=us-central1-a \
  --image-family=windows-2022 --image-project=windows-cloud --machine-type=e2-standard-2

gcloud compute reset-windows-password win-reports --zone=us-central1-a --user=ana
# → username: ana   password: x7#Kq9!mPz2L   ip_address: 34.123.45.67
```

Ana opens Remote Desktop, enters the IP, `ana` and the password, and sees the Windows desktop. *(A firewall rule must allow TCP 3389 from her office IP.)*

---

## 🧠 Key Takeaways / Memory Tips

- **Windows VM + RDP → `gcloud compute reset-windows-password`** (or console "Set Windows password").
- **Linux VM → SSH keys / OS Login.** Windows uses username + password.
- Google Account and service account keys **never** log you in to a Windows desktop.
  🧠 *"**Windows wants a password: ask gcloud to make one.**"*
- Related: **Q001** (OS Login for Linux SSH), **Q070** (service account keys are for APIs).

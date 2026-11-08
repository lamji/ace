# Q020: Connecting to a Windows (SQL Server) VM with RDP in the Fewest Steps

**Topic:** Compute Engine (Windows VMs, RDP, Windows password, firewall port 3389 vs 22)

## ❓ Question
> You created an instance of SQL Server 2017 on Compute Engine to test features in the new version. You want to connect to this instance using the fewest number of steps. What should you do?
>
> **A.** Install a RDP client on your desktop. Verify that a firewall rule for port 3389 exists.
>
> **B.** Install a RDP client in your desktop. Set a Windows username and password in the GCP Console. Use the credentials to log in to the instance.
>
> **C.** Set a Windows password in the GCP Console. Verify that a firewall rule for port 22 exists. Click the RDP button in the GCP Console and supply the credentials to log in.
>
> **D.** Set a Windows username and password in the GCP Console. Verify that a firewall rule for port 3389 exists. Click the RDP button in the GCP Console, and supply the credentials to log in.

**My answer:** A
**Correct answer:** D
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You created a VM running SQL Server 2017 (a Microsoft database on Windows) to try new features.
- **What you must achieve:** Log in to that VM.
- **The limits:** Use the fewest steps.
- **What they're really asking:** What is the quickest way to log in to this Windows VM?

To log in to **any** Windows VM with RDP, you need **all 3** of these:
1. 🔑 **A username and password.** A new Windows VM on Google Cloud **has none for you yet**, so you must **set/generate** one.
2. 🚪 **An open network door.** A firewall rule allowing **port 3389** (the RDP port).
3. 🖥️ **A way to start RDP.** The Console's **RDP button**, or an RDP client app.

| Keyword | What it hints at |
|---|---|
| "**SQL Server 2017 on Compute Engine**" | A **Windows** VM, so you connect with **RDP** (not SSH) |
| "**connect**" | You need **credentials + port 3389 + an RDP connection** |
| "**fewest number of steps**" | The fewest steps that **still work**. Skipping a required step doesn't count |

**Exam topic:** Compute Engine, specifically **connecting to Windows VMs**.

---

## 📚 Key Terms Explained

### 1️⃣ SQL Server 2017 on Compute Engine
- **What it is:** Microsoft's database running on a **Windows Server VM**. Google offers ready-made public images with SQL Server already installed.
- **Analogy:** 🏢 A **branch office computer** that already has the accounting software installed.
- **In the online store:** A test VM where ShopNow tries a new SQL Server version for its accounting system.

### 2️⃣ RDP (Remote Desktop Protocol)
- **What it is:** Microsoft's way to **see and control a Windows desktop remotely**, as if you were sitting in front of it.
- **Analogy:** 🖥️ A **video call where you also control the other computer's mouse and keyboard**.

### 3️⃣ RDP Client
- **What it is:** An app on **your** computer that makes the RDP connection (e.g., Microsoft Remote Desktop).
- **Analogy:** 📞 The **phone app** you use to make the video call.

### 4️⃣ Port 3389 vs Port 22
- **Port:** A numbered "door" on a server, where each service uses its own.
  | Port | Used for | Typical OS |
  |---|---|---|
  | **3389** | **RDP** (remote desktop) | **Windows** ✅ |
  | **22** | **SSH** (command-line login) | **Linux** |
- **Analogy:** 🚪 An office building with numbered doors. **Door 3389** = visitors for the Windows desktop. **Door 22** = the Linux command-line entrance.

### 5️⃣ Firewall Rule
- **What it is:** A rule in your VPC that **allows or blocks traffic** to VMs on certain ports. Without an "allow tcp:3389" rule, RDP is blocked.
- The **default** network comes with a `default-allow-rdp` rule, but **custom networks don't**. That's why you **verify** it exists.
- **Analogy:** 🛡️ The **security guard's list** of which doors are open to visitors.

### 6️⃣ Windows Username and Password ("Set Windows password")
- **What it is:** Google Cloud **doesn't give you a ready password** for a new Windows VM. You click **"Set Windows password"** in the Console (or run `gcloud compute reset-windows-password`), and Google **creates the user and generates a password** for you.
- **Without this step, you can't log in**, even if everything else is ready.
- **Analogy:** 🪪 **Getting your login from IT** before you can sign in to a new office computer.

### 7️⃣ The Console's "RDP" Button
- **What it is:** A button next to the Windows VM in the Cloud Console that **starts the RDP connection for you** (through a browser RDP extension or a ready-made `.rdp` file), so you don't have to set up a connection by hand.
- **Analogy:** 🔘 A **"Connect" button at reception** that opens the meeting room link for you.

### 🔗 How They Fit Together
```
👩‍💻 You
 │ ① 🔑 "Set Windows password" in Console → username: maria / password: generated
 │ ② 🛡️ Firewall rule: allow tcp:3389 → VM   (RDP door open)
 │ ③ 🔘 Click "RDP" in Console → enter username + password
 ▼
🖥️ Windows Server VM (SQL Server 2017)  ✅ desktop appears

❌ Missing ① → "The credentials did not work" (you can't log in)
❌ Port 22 instead of 3389 → RDP blocked (22 is SSH for Linux)
```

---

## 🌍 Real-World Scenario

A database admin spins up a **Windows VM with SQL Server** to test a new version. Windows servers are managed through a **remote desktop**, so the admin needs to **log in** to the desktop. On Google Cloud, the usual checklist is:

**get a Windows password → make sure port 3389 is open → connect with RDP**.

Missing any one of these means the connection fails.

---

## 🔍 Option-by-Option Breakdown

### ❌ A (your answer)
> **A.** Install a RDP client on your desktop. Verify that a firewall rule for port 3389 exists.

**Why it's wrong:**
- ✔️ Port **3389** is the right port, and an RDP client can connect.
- ❌ **No username or password!** A new Windows VM on Google Cloud **doesn't have login details for you** until you **set a Windows password**. You'd reach the login screen and **get stuck**.
- ⚠️ **Trap option:** it *looks* like the fewest steps because it's the **shortest**. But "fewest steps" means the fewest steps **that actually work**. A plan that can't log in isn't a plan. 🙂

**📌 When to use it:** Use it when you **already have login details** and only need to connect.
🏢 **Office example:** Driving to the branch office when you **already have your keycard**. You just check that the front door is unlocked.

### ❌ B
> **B.** Install a RDP client in your desktop. Set a Windows username and password in the GCP Console. Use the credentials to log in to the instance.

**Why it's wrong:**
- ✔️ It includes the **credentials** step, which is what A was missing.
- ❌ It **doesn't check the firewall rule for port 3389**. On a custom network without that rule, RDP is **blocked**.
- ❌ **Installing your own RDP client** is an extra setup step compared with clicking the Console's **RDP button**.

**📌 When to use it:** Use it when you **prefer your own remote desktop app** and the **network door is already open**.
🏢 **Office example:** Getting your **login from IT** and using **your own laptop's remote app**. That's fine if the building's door is already open.

### ❌ C
> **C.** Set a Windows password in the GCP Console. Verify that a firewall rule for port 22 exists. Click the RDP button in the GCP Console and supply the credentials to log in.

**Why it's wrong:**
- ✔️ It sets credentials and uses the RDP button.
- ❌ **Port 22 is SSH**, used for **Linux** command-line login. **RDP uses port 3389.** With only port 22 open, the RDP connection is **blocked**.

**📌 When to use it:** **Never use this** for Windows remote desktop. Port 22 is the wrong door. Use option D (port 3389).
🏢 **Office example:** Checking that the **loading dock door** is open when visitors actually come in through the **front entrance**.

### ✅ D
> **D.** Set a Windows username and password in the GCP Console. Verify that a firewall rule for port 3389 exists. Click the RDP button in the GCP Console, and supply the credentials to log in.

**Why it's correct:**
- ✔️ **Credentials:** "Set Windows password" creates the user and password. ✅
- ✔️ **Network:** a firewall rule for **port 3389** (RDP) lets the connection through. ✅
- ✔️ **Connection:** the Console's **RDP button** starts the session for you, so there's no separate client setup. ✅
- ✔️ It covers **everything required** with the **fewest steps**.

**📌 When to use it:** Use it when you want to **log in to a Windows server quickly** from the Cloud Console.
🏢 **Office example:** Getting your **login from IT**, checking the **front door is open**, then pressing the **"Connect" button at reception** that takes you straight to the computer.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **finance team** uses an accounting system that runs on **SQL Server**. Before upgrading, database admin Maria creates a test VM, `sql2017-test`, with a **SQL Server 2017 on Windows Server** image.

```
👩‍💻 Maria (laptop) ──RDP, port 3389──► 🖥️ sql2017-test (Windows Server + SQL Server 2017)
                                           └─ tests the accounting reports on the new version
```

**① Set a Windows username and password:**
- Console: **Compute Engine → VM instances → sql2017-test → Set Windows password** → username `maria` → copy the generated password
- Or with gcloud:
```bash
gcloud compute reset-windows-password sql2017-test \
  --zone=asia-southeast1-a \
  --user=maria
# → prints the username + a generated password
```

**② Verify or create the RDP firewall rule (port 3389):**
```bash
gcloud compute firewall-rules list --filter="allowed[].ports:3389"

# If missing, create one. Safer: only allow Maria's office IP
gcloud compute firewall-rules create allow-rdp-office \
  --network=shopnow-vpc \
  --allow=tcp:3389 \
  --source-ranges=203.0.113.10/32 \
  --target-tags=rdp
```

**③ Click RDP in the Console** → enter `maria` + the password → the Windows desktop opens → Maria opens SQL Server Management Studio and tests the reports. ✅

**🎬 With the other options:**
- **A:** Maria reaches the Windows login screen but **has no password**: "Your credentials did not work." ❌
- **C:** Only port 22 is open, so the RDP connection **times out**. ❌

**🔒 Security tip:** Don't leave port 3389 open to the whole internet (`0.0.0.0/0`). Limit it to your office IP, or use **IAP TCP forwarding** so the VM doesn't need a public IP at all:
```bash
gcloud compute start-iap-tunnel sql2017-test 3389 \
  --local-host-port=localhost:3389 \
  --zone=asia-southeast1-a
# then RDP to localhost:3389
```

---

## 🧠 Key Takeaways / Memory Tips

- **Windows VM login = 🔑 credentials + 🚪 port 3389 + 🖥️ RDP.** All three are required.
- **A new Windows VM has no password for you.** "Set Windows password" (or `gcloud compute reset-windows-password`) first.
- **Port 3389 = RDP (Windows). Port 22 = SSH (Linux).**
  🧠 *"**Windows** has more letters, so it gets the bigger number (**3389**). **SSH** is short, so it gets **22**."*
- **"Fewest steps" = fewest steps that WORK.** Don't pick an option that skips a required step.
- **Console RDP button** = start the session without separately setting up a client.

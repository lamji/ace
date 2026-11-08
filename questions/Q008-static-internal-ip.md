# Q008: Reserving a Specific Static Internal IP for a Server

**Topic:** VPC networking / Compute Engine (internal vs external IPs, static vs ephemeral IPs)

## ❓ Question
> You have an application that looks for its licensing server on the IP 10.0.3.21. You need to deploy the licensing server on Compute Engine. You do not want to change the configuration of the application and want the application to be able to reach the licensing server. What should you do?
>
> **A.** Reserve the IP 10.0.3.21 as a static internal IP address using gcloud and assign it to the licensing server.
>
> **B.** Reserve the IP 10.0.3.21 as a static public IP address using gcloud and assign it to the licensing server.
>
> **C.** Use the IP 10.0.3.21 as a custom ephemeral IP address and assign it to the licensing server.
>
> **D.** Start the licensing server with an automatic ephemeral IP address, and then promote it to a static internal IP address.

**My answer:** A
**Correct answer:** A
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** An application is set up to look for its licensing server (a server that confirms the app is allowed to run) at the private IP address 10.0.3.21.
- **What you must achieve:** Run that licensing server on a Compute Engine VM so the app can reach it.
- **The limits:** You can't change the app's settings, so the server must answer at exactly 10.0.3.21.
- **What they're really asking:** How do you create the VM so it gets that exact private address?

| Keyword | What it hints at |
|---|---|
| "**IP 10.0.3.21**" | A **private (internal)** address (in the 10.x.x.x range) |
| "**do not want to change the configuration**" | The server **must** have exactly this IP |
| "**be able to reach**" (long term) | The IP must **never change**, so it must be **static** |
| "**using gcloud**" | Reserve the address with `gcloud compute addresses create` |

**Exam topic:** VPC networking, specifically **static internal IP addresses**.

---

## 📚 Key Terms Explained

### 1️⃣ Licensing Server
- **What it is:** A server that checks whether software is **paid for and allowed to run**. The app asks it, "Do I have a valid license?" before starting.
- **Analogy:** 🎫 The **ticket checker** at the door. No valid ticket, no entry.
- **In the online store:** ShopNow's warehouse software (bought from a vendor) asks the license server at `10.0.3.21` for permission every time it starts.

### 2️⃣ Internal (Private) IP vs External (Public) IP
- **Internal IP:** An address used **inside your VPC** only (e.g., `10.0.3.21`). It comes from your **subnet's range** and can't be reached from the internet.
- **External IP:** An address that can be reached **from the internet** (e.g., `34.87.12.5`). Google assigns it from **Google's own pool**. You **can't choose** a number like `10.0.3.21`.
- **Analogy:** 📞 Internal IP = an **office extension number** (ext. 321) that only works inside the building. External IP = the company's **public phone number** that anyone in the world can call.
- **In the online store:** The license server only needs to be reached by the warehouse app inside the VPC, so an **internal** IP is enough (and safer).

### 3️⃣ Ephemeral vs Static IP
- **Ephemeral IP:** A **temporary** IP. It stays with the VM while the VM exists, but it's **released when the VM is deleted**. Next time, you may get a different number.
- **Static IP:** A **reserved** IP that **belongs to your project** until you release it. You can attach it to a new VM anytime, and the number never changes.
- **Analogy:** 🪑 Ephemeral = a **hot desk**. You sit there today, but once you leave, anyone can take it. Static = a desk with **your nameplate on it**, kept for you even if you're away.
- **In the online store:** If the license server VM gets deleted and recreated (e.g., during an upgrade), a static IP guarantees it comes back at `10.0.3.21`.

### 4️⃣ Reserving an IP Address
- **What it is:** Telling Google Cloud, *"Set aside this exact address for me."* For internal IPs, you choose the **subnet** and the **exact address** (it must be inside that subnet's range).
- **Command:** `gcloud compute addresses create ... --subnet=... --addresses=10.0.3.21`
- **Analogy:** 📝 Booking **meeting room 21** in the office system so nobody else can take it.

### 5️⃣ "Promoting" an Ephemeral IP to Static
- **What it is:** Taking the IP a VM **already has** and making it **permanent**. You keep **the same number**; you **can't change it** to a different one.
- **Analogy:** 🪑 You were given a random hot desk (say desk 7), liked it, and asked facilities to make desk 7 permanently yours. You still don't get desk 21.

### 6️⃣ Subnet Range (review from Q002)
- The internal IP **must be inside the subnet's range**. `10.0.3.21` fits in a subnet like `10.0.3.0/24` (addresses 10.0.3.0 to 10.0.3.255).
- Google reserves a few addresses in every subnet (for a /24: `.0`, `.1`, `.254`, `.255`), so `.21` is fine.

### 🔗 How They Fit Together
```
🏘️ VPC: shopnow-vpc
└── 🛣️ Subnet: shopnow-backend   10.0.3.0/24   (asia-southeast1)
      │
      ├── 📌 Reserved STATIC INTERNAL IP: license-ip = 10.0.3.21  (belongs to the project)
      │         │ assigned to
      │         ▼
      ├── 🖥️ VM: license-server   (internal IP 10.0.3.21) ✅
      │
      └── 🖥️ VM: warehouse-app ──"is my license valid?"──► 10.0.3.21  (hard-coded, never changes)

🌐 Internet ──X──► 10.0.3.21   (internal IPs are not reachable from the internet)
```

---

## 🌍 Real-World Scenario

Companies often move **old software** to the cloud ("lift and shift"). That software often has an **IP address written into its config** that nobody wants to touch: the vendor is gone, the config is locked, or changing it breaks the license.

So the cloud engineer builds the cloud network to **match the old address**: create a subnet that includes `10.0.3.21`, **reserve** that exact internal IP, and attach it to the new server. The app never knows it moved. 🎉

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Reserve the IP 10.0.3.21 as a static internal IP address using gcloud and assign it to the licensing server.

**Why it's correct:**
- ✔️ **Internal** is right, because `10.0.3.21` is a private address and the app talks to the server **inside the network**.
- ✔️ **Static (reserved)** means the IP **belongs to you**. Even if the VM is deleted and rebuilt, it gets `10.0.3.21` again.
- ✔️ The app's configuration **doesn't change**, exactly as required.

**📌 When to use it:** Use it when **other servers inside your network find a server by a fixed address** that must never change.
🏢 **Office example:** Reserving a **permanent extension number** (ext. 321) for the IT help desk. Even if the person at the desk changes, everyone dials the same number.

### ❌ B
> **B.** Reserve the IP 10.0.3.21 as a static public IP address using gcloud and assign it to the licensing server.

**Why it's wrong:**
- ❌ `10.0.3.21` is a **private** address (from the 10.x.x.x range). It **can't** be a public IP.
- ❌ You **can't choose** the number of a public IP. Google assigns it from its own pool (e.g., `34.87.12.5`).
- ❌ A license server doesn't need to be reachable from the internet, and exposing it would be a security risk.

**📌 When to use it:** Use it when **people outside the company (on the internet) need to reach your server** at an address that never changes.
🏢 **Office example:** The company's **public hotline number** printed on business cards. Customers always call the same number.

### ❌ C
> **C.** Use the IP 10.0.3.21 as a custom ephemeral IP address and assign it to the licensing server.

**Why it's wrong:**
- ⚠️ This might work **at first**: Google Cloud does let you pick a specific internal address for a VM without reserving it.
- ❌ But it's **ephemeral**: if the VM is **deleted** (upgrade, rebuild, mistake), the IP is **released**. Another VM could take `10.0.3.21`, and the app can't find its license server.
- ❌ It doesn't **guarantee** the address long-term, so it isn't Google's recommended approach.

**📌 When to use it:** Use it when you want a **specific address for now**, but it's fine if you lose it later (like a short test).
🏢 **Office example:** Sitting at **desk 21 without booking it**. It's fine today, but if you leave, someone else can sit there.

### ❌ D
> **D.** Start the licensing server with an automatic ephemeral IP address, and then promote it to a static internal IP address.

**Why it's wrong:**
- ❌ "Automatic" means Google picks a **random free address** in the subnet (e.g., `10.0.3.7`), **not** `10.0.3.21`.
- ❌ **Promoting** makes that random address permanent, but it's still `10.0.3.7`. The app keeps looking at `10.0.3.21` and finds nothing.

**📌 When to use it:** Use it when **you don't care which address the server gets at first**, but later decide to keep it forever.
🏢 **Office example:** You're given a **random temporary desk**, you like it, and you ask facilities to make **that same desk** permanently yours.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow bought **warehouse inventory software** from a vendor. Its config file is locked, and it **always** checks its license at `10.0.3.21`. ShopNow is moving it to Google Cloud.

```
🛍️ Shoppers ──► Next.js storefront ──► Orders API
                                          │ "reserve stock for order #1042"
                                          ▼
                              🏭 warehouse-app (vendor software)
                                          │ "is my license valid?"
                                          ▼
                              🎫 license-server  10.0.3.21 (static internal) ✅
```

**1. Make sure the subnet includes 10.0.3.21:**
```bash
gcloud compute networks subnets create shopnow-backend \
  --network=shopnow-vpc \
  --region=asia-southeast1 \
  --range=10.0.3.0/24
```

**2. Reserve the exact static internal IP (option A):**
```bash
gcloud compute addresses create license-ip \
  --region=asia-southeast1 \
  --subnet=shopnow-backend \
  --addresses=10.0.3.21
```

**3. Create the license server VM using that reserved IP (no public IP needed):**
```bash
gcloud compute instances create license-server \
  --zone=asia-southeast1-a \
  --subnet=shopnow-backend \
  --private-network-ip=license-ip \
  --no-address
```

**🎬 Six months later:** The license server needs an OS upgrade, so the team deletes and recreates the VM.
- **With A (static):** The new VM gets `10.0.3.21` again. The warehouse keeps working, and orders keep shipping. ✅
- **With C (custom ephemeral):** The IP was released when the VM was deleted. Meanwhile, autoscaling started a new Orders API VM that **took 10.0.3.21**. The warehouse app asks the wrong server for its license, fails to start, and **orders stop shipping**. ❌
- **With D (auto + promote):** The server was at `10.0.3.7` from day one, so the warehouse app **never** found it. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"App expects a specific private IP" → reserve a STATIC INTERNAL IP with that exact address.**
- **10.x / 172.16–31.x / 192.168.x = private, so always INTERNAL.** You can't pick a public IP's number.
- **Ephemeral = temporary (released when the VM is deleted). Static = reserved, it's yours until you release it.**
  🧠 *"Ephemeral = hot desk. Static = desk with your nameplate."*
- **Promoting keeps the SAME IP the VM already has.** It can't turn into a different number.
- Commands to remember:
  | Command | What it does |
  |---|---|
  | `gcloud compute addresses create NAME --region=R --subnet=S --addresses=IP` | Reserve a specific static **internal** IP |
  | `gcloud compute addresses create NAME --region=R` | Reserve a static **external** IP (Google picks the number) |
  | `gcloud compute instances create VM --private-network-ip=NAME_OR_IP` | Give a VM a specific internal IP |

# Q021: Using Two gcloud Configurations to Work in Two Accounts

**Topic:** Cloud SDK / gcloud CLI (named configurations: create, activate, list; account, project, region and zone per configuration)

## ❓ Question
> You have one GCP account running in your default region and zone and another account running in a non-default region and zone. You want to start a new Compute Engine instance in these two Google Cloud Platform accounts using the command line interface. What should you do?
>
> **A.** Create two configurations using gcloud config configurations create [NAME]. Run gcloud config configurations activate [NAME] to switch between accounts when running the commands to start the Compute Engine instances.
>
> **B.** Create two configurations using gcloud config configurations create [NAME]. Run gcloud configurations list to start the Compute Engine instances.
>
> **C.** Activate two configurations using gcloud configurations activate [NAME]. Run gcloud config list to start the Compute Engine instances.
>
> **D.** Activate two configurations using gcloud configurations activate [NAME]. Run gcloud configurations list to start the Compute Engine instances.

*(The end of option A was cut off in the screenshot ("accounts w…"). It reads "accounts when running the commands".)*

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know (learned it now)

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You use two Google Cloud accounts. One uses your default region and zone (location settings); the other uses a different region and zone.
- **What you must achieve:** Create a new VM in each account from the command line.
- **The limits:** Each VM must be created in the right account and the right location.
- **What they're really asking:** How do you set up the command-line tool so it can work with both accounts and their different locations?

| Keyword | What it hints at |
|---|---|
| "**one GCP account** … **another account**" | Two sets of login details, so **two gcloud configurations** |
| "**default** region and zone" / "**non-default** region and zone" | Each configuration stores its **own region and zone** |
| "**start a new Compute Engine instance**" | You need a real create command (`gcloud compute instances create`), not a "list" command |
| "**command line interface**" | The `gcloud` tool |

**Exam topic:** Cloud SDK / gcloud CLI, specifically **named configurations**. (This is the sister question of Q005, which used `describe`.)

---

## 📚 Key Terms Explained

### 1️⃣ gcloud CLI (Cloud SDK)
- **What it is:** The command-line tool for Google Cloud. You type commands like `gcloud compute instances create` instead of clicking in the Console.
- **Analogy:** 📞 Calling the office's service desk and **giving instructions by phone** instead of walking to each department.
- **In the online store:** The ShopNow DevOps engineer uses `gcloud` to create VMs, buckets and databases from a laptop.

### 2️⃣ GCP Account
- **What it is:** The **identity** you log in with (for example `maria@shopnow.com` or `maria.consulting@gmail.com`). Each account can see different projects.
- **Analogy:** 🪪 Your **staff ID card**. Different cards open different buildings.
- **In the online store:** Maria has a **work account** for ShopNow and a **second account** for a client project.

### 3️⃣ Region and Zone (review)
- **Region:** A **geographic area** with Google data centers (e.g., `us-central1`, `asia-southeast1`).
- **Zone:** One **data center area inside a region** (e.g., `asia-southeast1-a`). A VM always lives in **one zone**.
- **Default region/zone:** The value gcloud uses **when you don't type `--zone`**.
- **Analogy:** 🏙️ Region = the **city**. Zone = **one office building** in that city.

### 4️⃣ gcloud Configuration (named configuration) 🔑
- **What it is:** A **saved profile** of gcloud settings: **account, project, region, zone** (and more). You can have many. **Only ONE is active at a time**, and every command uses the active one.
- **Analogy:** 💼 **Work profiles on an office computer**: "ShopNow profile" and "Client profile". Each has its own login, own default printer, own office location. You **switch profiles** to change all of them at once.
- **In the online store:** Configuration `shopnow` = Maria's work account in `us-central1-a`. Configuration `client` = her other account in `asia-southeast1-b`.

### 5️⃣ The Configuration Commands
| Command | What it does |
|---|---|
| `gcloud config configurations create NAME` | Makes a **new profile** (and makes it active) |
| `gcloud config configurations activate NAME` | **Switches** to that profile |
| `gcloud config configurations list` | **Shows** all profiles and which one is active |
| `gcloud config configurations describe NAME` | **Shows** one profile's settings without switching (Q005) |
| `gcloud config list` | **Shows** the active profile's settings |
| `gcloud config set PROPERTY VALUE` | **Changes** a setting in the active profile (e.g., `compute/zone`) |

⚠️ Note: every one of these starts with **`gcloud config`**. There is **no `gcloud configurations …` command**. Options B, C and D use that broken form.

### 🔗 How They Fit Together
```
💻 Your laptop (gcloud CLI)
 ├── ⚙️ Configuration "shopnow"   ← account: maria@shopnow.com
 │                                   project: shopnow-prod
 │                                   region/zone: us-central1 / us-central1-a   (default)
 │
 └── ⚙️ Configuration "client"    ← account: maria.consulting@gmail.com
                                     project: client-app
                                     region/zone: asia-southeast1 / asia-southeast1-b  (non-default)

 Only ONE is active at a time:
   activate shopnow → gcloud compute instances create vm-1   → created in shopnow-prod, us-central1-a
   activate client  → gcloud compute instances create vm-2   → created in client-app, asia-southeast1-b
```

---

## 🌍 Real-World Scenario

Cloud engineers often work in **more than one place**: a company account and a client account, or **dev** and **prod** environments with different regions. Typing `--account`, `--project` and `--zone` on every command is slow and easy to get wrong. Creating a VM in the **wrong account or wrong region** can cost money or break rules about where data lives.

**Named configurations** fix this: set each profile up once, then **switch with one command** before you work.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create two configurations using gcloud config configurations create [NAME]. Run gcloud config configurations activate [NAME] to switch between accounts when running the commands to start the Compute Engine instances.

**Why it's correct:**
- ✔️ **`gcloud config configurations create`** makes **one profile per account**, each with its own account, project, region and zone.
- ✔️ **`gcloud config configurations activate`** **switches** between them. Only one profile can be active at a time.
- ✔️ After switching, you run the real create command (`gcloud compute instances create`) and the VM lands in the **right account and zone**.
- ✔️ Both commands use the **correct syntax** (`gcloud config configurations …`).

**📌 When to use it:** Use it when you work for two places and need to switch between them often.
🏢 **Office example:** Logging out of the "Head Office" profile and into the "Branch Office" profile on the shared computer before doing that branch's work.

### ❌ B
> **B.** Create two configurations using gcloud config configurations create [NAME]. Run gcloud configurations list to start the Compute Engine instances.

**Why it's wrong:**
- ✔️ Creating two configurations is a good start.
- ❌ **`gcloud configurations list` isn't a real command.** The correct form is `gcloud config configurations list`.
- ❌ Even the correct `list` only **shows** your configurations. It **doesn't start any VM** and **doesn't switch** accounts.

**📌 When to use it:** Use the correct `gcloud config configurations list` when you want to see all your profiles and which one is active.
🏢 **Office example:** Looking at the list of profiles on the shared computer. Reading the list doesn't do any work.

### ❌ C
> **C.** Activate two configurations using gcloud configurations activate [NAME]. Run gcloud config list to start the Compute Engine instances.

**Why it's wrong:**
- ❌ You **can't activate two configurations at once**. Only one is active at a time.
- ❌ You can't activate configurations that were **never created**.
- ❌ **`gcloud configurations activate`** is the wrong syntax (it needs `config`).
- ❌ **`gcloud config list`** only **shows** the active settings. It **doesn't create a VM**.

**📌 When to use it:** Use the correct `gcloud config list` when you want to check which account, project and zone you're using right now.
🏢 **Office example:** Glancing at your ID badge to check which office you're signed in to. It doesn't do any work.

### ❌ D
> **D.** Activate two configurations using gcloud configurations activate [NAME]. Run gcloud configurations list to start the Compute Engine instances.

**Why it's wrong:**
- ❌ Same problems as C: **you can't have two active at once**, they were **never created**, and the syntax is **missing `config`**.
- ❌ A **list** command **never starts VMs**.

**📌 When to use it:** **Never use this.** Create the profiles, then switch between them one at a time (option A).
🏢 **Office example:** Trying to sign in to two offices on the same computer at once, then expecting a printed staff list to do the work.

---

## 🛒 E-Commerce Full-Stack Example

Maria runs DevOps for **ShopNow** (work account) and also helps a **partner warehouse** company (second account) whose systems run in Asia.

**1. Set up the two profiles once:**
```bash
# Profile 1: ShopNow (the default region and zone)
gcloud config configurations create shopnow
gcloud config set account maria@shopnow.com
gcloud config set project shopnow-prod
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a

# Profile 2: partner warehouse (non-default region and zone)
gcloud config configurations create warehouse
gcloud config set account maria.consulting@gmail.com
gcloud config set project warehouse-tracking
gcloud config set compute/region asia-southeast1
gcloud config set compute/zone asia-southeast1-b
```
(`create` also makes the new profile active, so each `set` applies to the profile just created. Run `gcloud auth login` once per account.)

**2. Start one VM in each account:**
```bash
gcloud config configurations activate shopnow
gcloud compute instances create checkout-api-04 --machine-type=e2-medium
# → created in shopnow-prod, us-central1-a ✅

gcloud config configurations activate warehouse
gcloud compute instances create stock-sync-01 --machine-type=e2-small
# → created in warehouse-tracking, asia-southeast1-b ✅
```

**3. Check where you are before running anything risky:**
```bash
gcloud config configurations list
# NAME       IS_ACTIVE  ACCOUNT                     PROJECT             COMPUTE_DEFAULT_ZONE
# shopnow    False      maria@shopnow.com           shopnow-prod        us-central1-a
# warehouse  True       maria.consulting@gmail.com  warehouse-tracking  asia-southeast1-b
```

💡 **Bonus:** For a one-off command, you can skip switching with the `--configuration` flag:
```bash
gcloud compute instances list --configuration=shopnow
```

**🎬 Without configurations:** Maria forgets to change the project and creates the partner's VM inside **ShopNow's** project in the US. ShopNow pays for it, and the partner's data sits in the wrong region. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Many accounts / projects / regions → one named configuration each.** `create` once, then **`activate`** to switch.
- **Only ONE configuration is active at a time.** "Activate two" is always wrong.
- **`list`, `describe` and `config list` only SHOW information.** They never create or start anything.
- **All the commands start with `gcloud config configurations …`**. If you see `gcloud configurations …`, it's a fake command.
- 🧠 *"**Create** the profiles, **activate** to switch, then **run** the command."*
- Pair with Q005: **`activate` = switch to it**, **`describe` = peek at it without switching**.

---

## 🤔 Follow-up: "The question doesn't say switch"

True. The **question** never says "switch". Only **option A** does. The need to switch is **hidden in the situation**:

1. You have **two accounts**, and each has a **different region and zone**.
2. gcloud can only use **one active configuration at a time**, which means one account and one zone.
3. You want a VM in **both** accounts.
4. So you **must** go from setup 1 to setup 2 at some point. That move *is* switching (`activate`).

```
Create VM #1 → needs account 1 + default zone       ┐
                                                    ├─ only one can be active → you must change it in between
Create VM #2 → needs account 2 + non-default zone   ┘
```

🧠 **Exam tip:** Questions describe the **situation**, and the options describe the **action**. Ask yourself, *"What has to happen for this to work?"* Two accounts plus one active profile means you have to switch.

**Elimination works too:**
- **B and D:** `gcloud configurations list` is a fake command, and listing never starts a VM.
- **C and D:** you can't "activate two" at once, and they were never created.
- **C:** `gcloud config list` only shows settings.
- **A** is the only option where every command is real **and** a VM can actually get created.

*(Another real-world way, not offered as an option: skip switching with `--configuration=NAME` on each command.)*

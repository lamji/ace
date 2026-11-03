# Q122: Isolated Cassandra Dev Environments, Fast and Low Effort (Cloud Marketplace)

**Topic:** Cloud Marketplace (pre-built solutions), Compute Engine

## ❓ Question
> Your company is moving from an on-premises environment to Google Cloud. You have multiple development teams that use Cassandra environments as backend databases. They all need a development environment that is isolated from other Cassandra instances. You want to move to Google Cloud quickly and with minimal support effort. What should you do?
>
> **A.** 1. Build an instruction guide to install Cassandra on Google Cloud. 2. Make the instruction guide accessible to your developers.
>
> **B.** 1. Advise your developers to go to Cloud Marketplace. 2. Ask the developers to launch a Cassandra image for their development work.
>
> **C.** 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Use the snapshot to create instances for your developers.
>
> **D.** 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Upload the snapshot to Cloud Storage and make it accessible to your developers. 3. Build instructions to create a Compute Engine instance from the snapshot so that developers can do it themselves.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Many teams each need **their own Cassandra** for development. You want it **fast** and with **little support work** from you.

**Clues in the question:**
- "**quickly**" + "**minimal support effort**": use something **ready-made**. Cloud Marketplace has one-click Cassandra deployments.
- "**isolated from other Cassandra instances**": each team launches **its own** deployment.

**Exam topic:** Compute Engine / Marketplace.

---

## 📚 Key Terms Explained

### 1. Cloud Marketplace 🔑
- **What it is:** Google's **catalog of ready-to-deploy software** (databases, tools, OS images). A few clicks create VMs that are already installed and configured.
- **Looks like:** Console → Marketplace → "Cassandra" → Launch → pick zone/machine → Deploy
- **Not to be confused with:** a store for buying Google services.
- **Analogy:** 🏪 The **office supply catalog**: order a pre-assembled desk instead of building one.
- **In the online store:** A dev spins up Redis or Cassandra in minutes.

### 2. Apache Cassandra
- **What it is:** An open-source **NoSQL database** built for huge write volumes across many servers.
- **Looks like:** `cqlsh> SELECT * FROM shop.carts;`
- **Not to be confused with:** Cloud SQL (relational).
- **Analogy:** 📇 A giant, fast card index spread across many cabinets.
- **In the online store:** Some teams store cart events in it.

### 3. Snapshot (review from Q112)
- **What it is:** A backup copy of a disk. You can create VMs from it, but you must build and maintain the original yourself.
- **Looks like:** `gcloud compute disks snapshot ...`
- **Not to be confused with:** a ready-made product.
- **Analogy:** 📸 A photocopy of a desk you set up yourself.
- **In the online store:** Backups of DB disks.

### 🔗 How they fit together
```
 Team A ── Marketplace → Cassandra deployment A (own VMs) ✅
 Team B ── Marketplace → Cassandra deployment B (own VMs) ✅   (isolated, no custom build)
```

---

## 🌍 Real-World Scenario

During a migration, five dev teams need Cassandra. Instead of building images and writing guides, the platform team tells them to deploy **Cassandra from Cloud Marketplace**. Each team has its own isolated cluster within minutes, and support uses the vendor's documentation.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. Build an instruction guide to install Cassandra on Google Cloud. 2. Make the instruction guide accessible to your developers.

**Wrong words:**
- ❌ "**Build an instruction guide to install Cassandra**": every team installs by hand. Slow, error-prone, and you'll field lots of support questions.

📌 **When to use it:** Use a guide when no ready-made option exists and the setup is unusual.
🏢 **Office example:** Handing everyone assembly instructions instead of ordering ready-made desks.

### ✅ B
> **B.** 1. Advise your developers to go to Cloud Marketplace. 2. Ask the developers to launch a Cassandra image for their development work.

**Why it's correct:**
- ✔️ "**go to Cloud Marketplace … launch a Cassandra image**" matches "**move to Google Cloud quickly**": a ready-made deployment in a few clicks.
- ✔️ "**Cloud Marketplace**" matches "**minimal support effort**": no image to build or maintain yourself.
- ✔️ "**developers … launch**" (each their own) matches "**isolated from other Cassandra instances**": each team gets its own deployment.

📌 **When to use it:** Use it when teams need standard software quickly and you don't want to build it yourself.
🏢 **Office example:** Ordering pre-assembled desks from the office supply catalog for each team.

### ❌ C
> **C.** 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Use the snapshot to create instances for your developers.

**Wrong words:**
- ❌ "**Build a Cassandra Compute Engine instance and take a snapshot**": you build and maintain a custom image. More effort than Marketplace, and you create everyone's instances yourself.

📌 **When to use it:** Use it when you need a custom-configured image that Marketplace doesn't offer.
🏢 **Office example:** Building one desk yourself and copying it for everyone.

### ❌ D
> **D.** 1. Build a Cassandra Compute Engine instance and take a snapshot of it. 2. Upload the snapshot to Cloud Storage and make it accessible to your developers. 3. Build instructions to create a Compute Engine instance from the snapshot so that developers can do it themselves.

**Wrong words:**
- ❌ "**Upload the snapshot to Cloud Storage**": snapshots aren't uploaded to buckets this way.
- ❌ "**Build instructions**": even more steps and support work.

📌 **When to use it:** **Never use this.** Use Marketplace (B).
🏢 **Office example:** Building a desk, shipping photos of it, and writing a manual so everyone rebuilds it.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's cart-events team and recommendations team each need Cassandra for development. Each team opens **Marketplace → Apache Cassandra → Launch** in its own dev project, and has a separate 3-node cluster in about 10 minutes.

---

## 🧠 Key Takeaways / Memory Tips

- **Standard software, fast, low effort → Cloud Marketplace.**
- Custom images and guides = more work.
  🧠 *"**Need it ready-made? Marketplace.**"*
- Related: **Q089** (VM sizing), **Q112** (snapshots).

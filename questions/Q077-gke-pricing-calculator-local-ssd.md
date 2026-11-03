# Q077: Pricing Calculator for GKE With High IOPS and Snapshots (Local SSD + Persistent Disk + Snapshots)

**Topic:** Billing / cost estimation (Google Cloud pricing calculator, local SSD, persistent disk, snapshot storage, GPUs)

## ❓ Question
> You need to provide a cost estimate for a Kubernetes cluster using the GCP pricing calculator for Kubernetes. Your workload requires high IOPs, and you will also be using disk snapshots. You start by entering the number of nodes, average hours, and average days. What should you do next?
>
> **A.** Fill in local SSD. Fill in persistent disk storage and snapshot storage.
>
> **B.** Fill in local SSD. Add estimated cost for cluster management.
>
> **C.** Select Add GPUs. Fill in persistent disk storage and snapshot storage.
>
> **D.** Select Add GPUs. Add estimated cost for cluster management.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You're estimating the price of a GKE cluster. The app needs **very fast disk reads/writes** and you'll take **disk snapshots** (backups). After entering nodes and hours, which fields do you fill in next?

**Clues in the question:**
- "**high IOPs**": fast disk operations → **local SSD**.
- "**disk snapshots**": snapshots are taken of **persistent disks** and stored as **snapshot storage** → fill in both.
- GPUs are for **heavy math (ML, graphics)**, not disk speed. The cluster management fee is **added by the calculator itself**, so it's not something you fill in.

**Exam topic:** Billing / planning.

---

## 📚 Key Terms Explained

### 1️⃣ IOPS
- **What it is:** **Input/Output Operations Per Second**: how many reads and writes a disk can do each second. High IOPS = very fast disk.
- **Looks like:** standard disk ≈ hundreds to thousands of IOPS; local SSD ≈ hundreds of thousands
- **Not to be confused with:** CPU speed or GPUs.
- **Analogy:** 🗄️ How many **files per second** a clerk can pull from the cabinet.
- **In the online store:** A search index that reads thousands of small records per second.

### 2️⃣ Local SSD 🔑
- **What it is:** A very fast SSD **physically attached** to the server running the node. Extremely high IOPS, but data is **temporary** (lost if the VM stops), and it **can't be snapshotted**.
- **Looks like:** `--local-ssd-count=1` (375 GB each)
- **Not to be confused with:** a persistent disk (network disk that survives restarts and can be snapshotted).
- **Analogy:** 📝 Papers **on your desk**: fastest to grab, but cleared away at night.
- **In the online store:** A cache or scratch space for the search engine.

### 3️⃣ Persistent disk
- **What it is:** A **network disk** attached to a VM. Data **survives** restarts, and you can take **snapshots** of it.
- **Looks like:** `pd-balanced`, 100 GB
- **Not to be confused with:** local SSD (faster, but temporary and no snapshots).
- **Analogy:** 🗄️ The **filing cabinet** in your office: a bit slower, but things stay.
- **In the online store:** The database pod's data volume.

### 4️⃣ Snapshot storage
- **What it is:** Where **backup copies of persistent disks** are kept. You pay per GB stored.
- **Looks like:** `gcloud compute disks snapshot orders-disk --snapshot-names=orders-2026-10-31`
- **Not to be confused with:** the disk itself. A snapshot is a **copy**, priced separately.
- **Analogy:** 📸 **Photocopies of the cabinet** kept in the storage room.

### 5️⃣ GPU
- **What it is:** A **graphics processor** that does massive parallel math: machine learning, video, 3D.
- **Not to be confused with:** disk speed. GPUs don't improve IOPS.
- **Analogy:** 🧮 A room full of **calculators**. Useless if the problem is slow filing.

### 6️⃣ Cluster management fee
- **What it is:** GKE's hourly fee per cluster for running the control plane. The pricing calculator **includes it automatically** for the cluster.
- **Not to be confused with:** a field you need to estimate yourself.

### 🔗 How they fit together
```
 Pricing calculator → GKE
   1. nodes, hours, days        (already done)
   2. local SSD                 ← "high IOPs"           ✅
   3. persistent disk storage   ← snapshots come from these disks ✅
   4. snapshot storage          ← "disk snapshots"      ✅
   (GPUs ← only for ML/graphics ❌; management fee ← calculator adds it)
```

---

## 🌍 Real-World Scenario

Before approving a new project, finance asks for a monthly cost estimate. The engineer opens the **Google Cloud pricing calculator**, picks GKE, and enters what the workload actually needs: nodes, **local SSD** for speed, **persistent disks** for data, and **snapshot storage** for backups. Adding things the workload doesn't need (like GPUs) would inflate the estimate.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Fill in local SSD. Fill in persistent disk storage and snapshot storage.

**Why it's correct:**
- ✔️ "**Fill in local SSD**" matches "**Your workload requires high IOPs**": local SSD is the fastest disk option.
- ✔️ "**Fill in persistent disk storage**" matches "**you will also be using disk snapshots**": snapshots are taken of persistent disks, so the disks must be priced.
- ✔️ "**and snapshot storage**" matches "**disk snapshots**": the stored backups have their own cost.

📌 **When to use it:** Use it when the job needs very fast workspace plus permanent files with backup copies.
🏢 **Office example:** Budgeting for a fast desk, filing cabinets, and storage-room space for photocopies.

### ❌ B
> **B.** Fill in local SSD. Add estimated cost for cluster management.

**Wrong words:**
- ✔️ "Fill in local SSD" covers high IOPS.
- ❌ "**Add estimated cost for cluster management**": the calculator already includes the cluster fee. And this option **skips the disks and snapshots** the question asks about.

📌 **When to use it:** Use local SSD alone when you only need fast temporary space and no backups.
🏢 **Office example:** Budgeting for fast desks but forgetting the filing cabinets and the photocopies.

### ❌ C
> **C.** Select Add GPUs. Fill in persistent disk storage and snapshot storage.

**Wrong words:**
- ✔️ "Fill in persistent disk storage and snapshot storage" covers the snapshots.
- ❌ "**Select Add GPUs**": GPUs speed up **math**, not **disk reads/writes**. They don't help "high IOPs" and would add a large, wrong cost.

📌 **When to use it:** Add GPUs when the workload does machine learning, video or 3D graphics.
🏢 **Office example:** Buying a room full of calculators when the real problem is slow filing.

### ❌ D
> **D.** Select Add GPUs. Add estimated cost for cluster management.

**Wrong words:**
- ❌ "**Select Add GPUs**": not related to IOPS.
- ❌ "**Add estimated cost for cluster management**": already included, and the option misses **both** local SSD and snapshots.

📌 **When to use it:** **Never use this** for a high-IOPS, snapshot workload. Use A.
🏢 **Office example:** Budgeting for calculators and the building fee, but no desks or cabinets.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow plans a GKE cluster for its **product search engine** (lots of fast disk reads) and its **orders database** (needs daily backups).

In the pricing calculator:
- Nodes: 4 × e2-standard-8, 730 hours/month.
- **Local SSD:** 1 × 375 GB per node (search index, high IOPS).
- **Persistent disk:** 500 GB `pd-ssd` (orders data).
- **Snapshot storage:** about 200 GB (daily backups, only changed blocks stored).
- GPUs: none (no ML here).

---

## 🧠 Key Takeaways / Memory Tips

- **High IOPS → local SSD.**
- **Snapshots → persistent disk + snapshot storage** (local SSD can't be snapshotted).
- **GPUs = math, not disk speed.** The cluster fee is added by the calculator.
  🧠 *"**Fast disk → local SSD. Backups → persistent disk + snapshots.**"*
- Related: **Q006** (storage classes), **Q049** (machine sizes).

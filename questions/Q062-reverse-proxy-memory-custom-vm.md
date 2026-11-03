# Q062: Running a Memory-Heavy Caching Reverse Proxy Cheaply (Memorystore vs Custom Machine Type)

**Topic:** Compute Engine (custom machine types, memory-to-vCPU ratio) vs Memorystore for Redis; choosing the cheapest fit

## ❓ Question
> You want to run a single caching HTTP reverse proxy on GCP for a latency-sensitive website. This specific reverse proxy consumes almost no CPU. You want to have a 30-GB in-memory cache, and need an additional 2 GB of memory for the rest of the processes. You want to minimize cost. How should you run this reverse proxy?
>
> **A.** Create a Cloud Memorystore for Redis instance with 32-GB capacity.
>
> **B.** Run it on Compute Engine, and choose a custom instance type with 6 vCPUs and 32 GB of memory.
>
> **C.** Package it in a container image, and run it on Kubernetes Engine, using n1-standard-32 instances as nodes.
>
> **D.** Run it on Compute Engine, choose the instance type n1-standard-1, and add an SSD persistent disk of 32 GB.

**My answer:** — (didn't know; asked "why A?")
**Correct answer:** A
**Result:** ❓ Didn't know

> ⚠️ **Honest note: this question is debated.**
> - The site's **community vote is A** (Memorystore), so A is recorded here as the "exam answer".
> - **Many experienced people argue B** is technically better: the question says "**run this reverse proxy**", and Memorystore is a Redis database. It **can't run** an HTTP reverse proxy program (like Varnish or Nginx); it can only store data. B's numbers are also carefully chosen (see below), and a 6 vCPU / 32 GB custom VM generally costs **less** than a 32 GB Memorystore instance.
> - **Why people pick A:** "in-memory cache" + "latency-sensitive" + "almost no CPU" sounds like Memorystore, a managed cache where you don't pay for CPUs.
> - **For the exam:** learn both reasons. If you see this exact wording, the community answer is A. If the question clearly asks where to **run a program**, choose a custom-memory VM (B).

---

## 📖 What the Question Is Asking

**In plain words:** You have a small program (a caching reverse proxy) that needs **lots of memory (32 GB)** but **almost no CPU**. It must respond fast. Where's the **cheapest** place to run it?

| Question words | What they point to |
|---|---|
| "**30-GB in-memory cache**" + "**additional 2 GB**" | Total **32 GB of RAM** needed |
| "**consumes almost no CPU**" | Don't pay for lots of vCPUs → avoid big standard machines (C) |
| "**in-memory**" | RAM, **not disk** → D is out |
| "**latency-sensitive**" | Fast memory access → RAM-based cache |
| "**minimize cost**" | Pay only for what you need: managed cache (A) or a custom machine shape (B) |
| "**single**" | One instance, no cluster → C is overkill |

**Exam topic:** Compute Engine machine types / Memorystore.

---

## 📚 Key Terms Explained

### 1️⃣ Caching HTTP reverse proxy
- **What it is:** A **program** that sits in front of your website, **keeps copies of pages in memory**, and serves them instantly instead of asking the web server every time. Examples: Varnish, Nginx.
- **Looks like:** Shopper → **proxy (cache hit: returns page from RAM)** → web server only on cache miss
- **Not to be confused with:** a database. The proxy is **software you run**; it answers HTTP requests itself.
- **Analogy:** 🗂️ A **receptionist with photocopies** of the most-asked forms, so nobody has to walk to the records room.
- **In the online store:** The homepage and product pages are served from the proxy's RAM in milliseconds.

### 2️⃣ Cloud Memorystore for Redis
- **What it is:** A **managed Redis** service: an in-memory **key-value store** that Google runs for you. You pick the size (GB), and your app reads and writes keys to it.
- **Looks like:** `gcloud redis instances create shop-cache --size=32 --region=us-central1` then `SET product:123 "<html>..."`
- **Not to be confused with:** a place to **run programs**. You can't install Varnish or Nginx on it; it only stores data your app puts there.
- **Analogy:** 🗄️ A **super-fast filing cabinet** that someone else maintains. It holds papers, but it can't greet visitors.
- **In the online store:** Shopping-cart sessions and cached product data that the API reads.

### 3️⃣ Custom machine type 🔑 (review from Q049)
- **What it is:** A Compute Engine VM where **you pick the exact number of vCPUs and amount of memory**, instead of a fixed size. Rules (N1): vCPUs must be **1 or an even number**, and memory can be **up to 6.5 GB per vCPU**.
- **Looks like:** `gcloud compute instances create proxy --custom-cpu=6 --custom-memory=32GB`
- **Why 6 vCPUs in B?** 32 GB ÷ 6.5 GB per vCPU = 4.9 → at least **5** vCPUs → must be even → **6**. So 6 vCPUs is the **smallest** CPU count allowed for 32 GB.
- **Not to be confused with:** predefined types like `n1-standard-8` (8 vCPUs, 30 GB) with a fixed ratio.
- **Analogy:** 🪑 **Ordering a custom desk**: lots of drawers (memory), small work surface (CPU).

### 4️⃣ n1-standard-32
- **What it is:** A predefined VM with **32 vCPUs and 120 GB of memory**.
- **Not to be confused with:** "32 GB". The 32 is **vCPUs**, and you'd pay for 32 CPUs you don't use.
- **Analogy:** 🏢 Renting a **whole office floor** for one person.

### 5️⃣ SSD persistent disk
- **What it is:** Fast **disk** storage attached to a VM. Faster than a normal disk, but still **much slower than RAM**.
- **Not to be confused with:** memory. A disk is not an "in-memory cache".
- **Analogy:** 📦 A **storage room down the hall** versus papers **on your desk** (RAM).

### 🔗 How they fit together
```
                need 32 GB RAM, almost no CPU, cheapest
   ┌────────────────────┬─────────────────────┬────────────────────┬──────────────────┐
   A Memorystore 32 GB   B custom 6 vCPU/32 GB  C n1-standard-32 GKE D n1-standard-1 + SSD
   managed cache,        runs the proxy,        32 vCPU / 120 GB    3.75 GB RAM,
   no CPUs to pay for    smallest legal CPUs    way too big ❌       cache on disk ❌
   (can't run software)  for 32 GB
```

---

## 🌍 Real-World Scenario

A website wants pages to load instantly, so the team puts a caching proxy in front of it. The proxy keeps 30 GB of pages in RAM and barely uses the CPU. Standard machine sizes give you CPU and memory in fixed proportions, so you'd pay for CPUs you don't need. The cloud engineer's job is to match the shape: a **managed in-memory cache** or a **custom VM with lots of memory and few CPUs**, never a giant cluster or a disk-based cache.

---

## 🔍 Option-by-Option Breakdown

### ✅ A (community answer)
> **A.** Create a Cloud Memorystore for Redis instance with 32-GB capacity.

**Why it's chosen:**

- ✔️ "**Cloud Memorystore for Redis**" matches "**in-memory cache**", "**latency-sensitive**": A managed RAM cache with sub-millisecond reads.
- ✔️ "**32-GB capacity**" matches "**30-GB … additional 2 GB**": Exactly the 32 GB of memory needed.
- ✔️ Managed, sized by GB only matches "**almost no CPU**", "**minimize cost**": You pay for memory, not for vCPUs, and Google runs it for you.

**⚠️ The weak point:** ❌ the question says "**run this reverse proxy**". Memorystore can't run the proxy program; it only stores data. You'd still need somewhere to run the proxy.

📌 **When to use it:** Use it when your app needs a fast shared place to keep data in memory, and you don't want to manage the server.
🏢 **Office example:** A fast filing cabinet that a service company keeps stocked and repaired for you.

### ❌ B (strong alternative)
> **B.** Run it on Compute Engine, and choose a custom instance type with 6 vCPUs and 32 GB of memory.

**Wrong words (by the community answer):**
- ✔️ "**Run it on Compute Engine**": a VM **can** run the proxy program.
- ✔️ "**32 GB of memory**": matches 30 + 2 GB.
- ❌ "**6 vCPUs**": the question says the proxy uses **almost no CPU**, so voters see 6 vCPUs as paying for unused CPU. *(Counter-point: 6 is the **minimum** N1 custom type allows for 32 GB, and it's usually cheaper than Memorystore 32 GB.)*

📌 **When to use it:** Use it when a program needs much more memory than CPU and a standard machine size would waste money.
🏢 **Office example:** Ordering a desk with lots of drawers and a small work surface, because that's what the job needs.

### ❌ C
> **C.** Package it in a container image, and run it on Kubernetes Engine, using n1-standard-32 instances as nodes.

**Wrong words:**
- ❌ "**run it on Kubernetes Engine**": a whole cluster for a **single** proxy adds cost and work.
- ❌ "**n1-standard-32 instances**": 32 vCPUs and 120 GB per node, far more than needed. The opposite of "almost no CPU" and "minimize cost".

📌 **When to use it:** Use it when you run many containers that need lots of CPU and memory together.
🏢 **Office example:** Renting a whole office floor for one employee who only needs a desk.

### ❌ D
> **D.** Run it on Compute Engine, choose the instance type n1-standard-1, and add an SSD persistent disk of 32 GB.

**Wrong words:**
- ✔️ "**n1-standard-1**" is cheap and has little CPU, which fits "almost no CPU".
- ❌ "**add an SSD persistent disk of 32 GB**": that's **disk**, not memory. The question needs an **in-memory** cache. n1-standard-1 has only **3.75 GB of RAM**, and a disk cache is slower, which hurts "latency-sensitive".

📌 **When to use it:** Use it when a small program needs extra space to save files, not extra memory.
🏢 **Office example:** Giving a clerk a storage room down the hall when they needed a bigger desk.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow wants its product pages to load instantly during sales.

```bash
# Option A: managed in-memory cache that the storefront API reads from
gcloud redis instances create shop-cache --size=32 --region=us-central1 --tier=basic

# Option B: run the Varnish proxy itself on a memory-heavy custom VM
gcloud compute instances create varnish-proxy --zone=us-central1-a \
  --custom-cpu=6 --custom-memory=32GB
```

| Option | RAM | vCPUs paid for | Runs the proxy program? | Fit |
|---|---|---|---|---|
| **A** Memorystore | 32 GB | none (managed) | ❌ stores data only | ✅ community answer |
| B custom VM | 32 GB | 6 (minimum allowed) | ✅ | ✅ strong alternative |
| C GKE n1-standard-32 | 120 GB/node | 32 per node | ✅ | ❌ huge waste |
| D n1-standard-1 + SSD | 3.75 GB | 1 | ✅ | ❌ cache on disk, not RAM |

---

## 🧠 Key Takeaways / Memory Tips

- **"In-memory cache" + "managed" / "minimize cost" → think Memorystore.**
- **"Needs lots of memory, little CPU, run a program" → custom machine type** (up to 6.5 GB per vCPU on N1; even vCPU counts).
- **Disk ≠ memory.** "In-memory" rules out any disk answer.
- **n1-standard-32 = 32 vCPUs**, not 32 GB.
  🧠 *"**Memory-heavy, CPU-light → shape it (custom VM) or rent it (Memorystore). Never buy the whole floor.**"*
- Related: **Q049** (custom machine type / increasing memory), **Q033** (another debated question).

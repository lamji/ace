# G012: Autopilot Bill Too High Because Pods Have No Resource Requests (Set Requests That Match Real Usage)

**Topic:** GKE (Autopilot Pod resource requests)
**Exam guide section:** 3.1 Managing compute: Managing GKE Autopilot Pod resource requests

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You run a small worker Deployment on a GKE Autopilot cluster. The containers do not specify resource requests. Monitoring shows that each Pod uses about 0.1 vCPU and 200 MiB of memory, but the cost is much higher than expected. You want to reduce cost without changing the cluster mode. What should you do?
>
> **A.** Change the machine type of the Autopilot cluster's node pool to a smaller machine type.
>
> **B.** Increase the number of replicas so the load is spread across more Pods.
>
> **C.** Set CPU and memory resource requests in the Pod specification that match the actual usage, within Autopilot's allowed minimums and ratios.
>
> **D.** Enable the cluster autoscaler on the Autopilot cluster.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You run a small background program (a worker) on GKE Autopilot (Google's fully managed Kubernetes mode, where you pay per Pod). Its settings don't say how much CPU and memory each Pod needs (no resource requests).
- **What you must achieve:** Lower the bill.
- **The limits:** Keep using Autopilot. Each Pod really uses only about 0.1 vCPU and 200 MiB of memory.
- **What they're really asking:** On Autopilot, what decides how much you pay for each Pod, and how do you fix it here?

**Clues in the question:**
- "**Autopilot**": you're billed for the CPU and memory your Pods **request**, not for nodes.
- "**do not specify resource requests**": Autopilot then applies **default requests**, which are much larger than 0.1 vCPU / 200 MiB.
- "**without changing the cluster mode**": fix it in the Pod spec, not by switching to Standard.

**Exam topic:** GKE operations (exam guide section 3.1).

---

## 📚 Key Terms Explained

### 1. Resource requests
- **What it is:** The CPU and memory a container asks Kubernetes to reserve for it. Set in the Pod spec.
- **Looks like:** `resources: {requests: {cpu: "250m", memory: "256Mi"}}`
- **Not to be confused with:** Limits, which are the most a container may use.
- **Analogy:** 🪑 Reserving 2 desks for a team that needs only 1.
- **In the online store:** `order-worker` requests 250m CPU.

### 2. GKE Autopilot billing 🔑
- **What it is:** In Autopilot, Google manages the nodes and you pay for the resources your **Pods request**. If you set no requests, Autopilot applies defaults (for general-purpose Pods, about 0.5 vCPU and 2 GiB of memory per Pod). There are also minimums and CPU-to-memory ratio rules.
- **Looks like:** No requests set → billed as 0.5 vCPU / 2 GiB per Pod
- **Not to be confused with:** GKE Standard, where you pay for the node VMs whatever the Pods request.
- **Analogy:** 🏨 A hotel that charges for the rooms you booked, not the ones you sleep in.
- **In the online store:** 10 workers × default requests = a surprise bill.

### 3. Node pool (Standard)
- **What it is:** A group of nodes with one machine type that you manage in GKE Standard. Autopilot manages nodes for you.
- **Looks like:** `gcloud container node-pools create small --machine-type=e2-small` (Standard only)
- **Not to be confused with:** Something you edit in Autopilot.
- **Analogy:** 🏢 Choosing office furniture yourself vs a serviced office.
- **In the online store:** Not used in Autopilot.

### 🔗 How they fit together
```
 No requests → Autopilot default ≈ 0.5 vCPU / 2 GiB per Pod 💸
 Set requests ≈ 250m / 256Mi (≥ Autopilot minimums) → pay for what you use ✅
```

---

## 🌍 Real-World Scenario

A team moves its email-sending worker to Autopilot and forgets resource requests. Each tiny Pod is billed at the default size. Adding `resources.requests` close to real usage cuts the worker's cost several times over.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Change the machine type of the Autopilot cluster's node pool to a smaller machine type.

**Wrong words:**
- ❌ "**Change the machine type of the Autopilot cluster's node pool**": in Autopilot, Google manages nodes, and you're billed by Pod requests anyway.

📌 **When to use it:** Use it in GKE Standard when you choose node sizes yourself.
🏢 **Office example:** Trying to pick furniture in a fully serviced office.

### ❌ B
> **B.** Increase the number of replicas so the load is spread across more Pods.

**Wrong words:**
- ❌ "**Increase the number of replicas**": more Pods, each still billed at the default size, so the cost goes **up**.

📌 **When to use it:** Use more replicas when you need more capacity or availability.
🏢 **Office example:** Hiring more staff to save on payroll.

### ✅ C
> **C.** Set CPU and memory resource requests in the Pod specification that match the actual usage, within Autopilot's allowed minimums and ratios.

**Why it's correct:**
- ✔️ "**Set CPU and memory resource requests in the Pod specification**" matches "**containers do not specify resource requests**": this replaces the large defaults.
- ✔️ "**match the actual usage**" matches "**about 0.1 vCPU and 200 MiB**" and "**reduce cost**".
- ✔️ "**within Autopilot's allowed minimums and ratios**": Autopilot rounds requests up to its minimums, so you stay valid while paying for much less than the default.

📌 **When to use it:** Use it when you pay for what you reserve, so you reserve only what you actually need.
🏢 **Office example:** Booking one desk instead of two because the person only needs one.

### ❌ D
> **D.** Enable the cluster autoscaler on the Autopilot cluster.

**Wrong words:**
- ❌ "**Enable the cluster autoscaler on the Autopilot cluster**": Autopilot already manages scaling, and this doesn't change what each Pod is billed for.

📌 **When to use it:** Use the cluster autoscaler on GKE Standard node pools.
🏢 **Office example:** Asking a serviced office to add a lift you can't control.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `email-worker` on Autopilot:
```yaml
resources:
  requests: {cpu: "250m", memory: "512Mi"}
```
Before: 10 Pods billed at the defaults. After: about a quarter of the CPU cost.

---

## 🧠 Key Takeaways / Memory Tips

- **Autopilot bills Pod requests. No requests → defaults (≈0.5 vCPU / 2 GiB). Too costly → set right-sized requests.**
  🧠 *"**Autopilot: pay what you request.**"*
- Related: **Q267**, **Q283**, **Q291**, **Q296** (Autopilot).

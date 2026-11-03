# Q331: Global Users, Low Latency, Growth Across Regions (Multi-Region VMs + Global External Application Load Balancer)

**Topic:** Networking (global load balancing)

## ❓ Question
> You host your website on Compute Engine. The number of global users visiting your website is rapidly expanding. You need to minimize latency and support user growth in multiple geographical regions. You also want to follow Google-recommended practices and minimize operational costs. Which two actions should you take? (Choose two.)
>
> **A.** Use an external Application Load Balancer in Regional mode.
>
> **B.** Deploy your VMs in multiple Google Cloud regions closest to your user’s geographical locations.
>
> **C.** Use a Network Load Balancer.
>
> **D.** Use an external Application Load Balancer in Global mode.
>
> **E.** Deploy all of your VMs in a single Google Cloud region with the largest available CIDR range.

**My answer:** — (didn't know)
**Correct answer:** B, D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Users worldwide; **low latency**; growth in **many regions**. Pick two.

**Clues in the question:**
- "**multiple geographical regions**" → **VMs in several regions** near users.
- One global anycast IP routing to the nearest healthy region → **global external Application Load Balancer**.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Global external Application Load Balancer 🔑
- **What it is:** One anycast IP worldwide; sends each user to the closest healthy backend region (HTTP/HTTPS).
- **Looks like:** `gcloud compute backend-services create web --global --load-balancing-scheme=EXTERNAL_MANAGED`
- **Not to be confused with:** regional ALB (one region).
- **Analogy:** 🌍 One phone number that rings the nearest branch.
- **In the online store:** ShopNow storefront.

### 🔗 How they fit together
```
 users → global ALB (1 IP) → nearest region MIG (US / EU / Asia) ✅
```

---

## 🌍 Real-World Scenario

A fast-growing site deploys MIGs in **US, EU and Asia** behind a **global external ALB**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use an external Application Load Balancer in Regional mode.

**Wrong words:**
- ❌ "**Regional mode**": serves one region only.

📌 **When to use it:** Use regional ALB when all users and backends are in one region.
🏢 **Office example:** A local phone number.

### ✅ B
> **B.** Deploy your VMs in multiple Google Cloud regions closest to your user’s geographical locations.

**Why it's correct:**
- ✔️ "**Deploy your VMs in multiple Google Cloud regions closest to your user's geographical locations**" matches "**minimize latency and support user growth in multiple geographical regions**".

📌 **When to use it:** Use it when customers are spread across continents.
🏢 **Office example:** Opening branch offices near each group of customers.

### ❌ C
> **C.** Use a Network Load Balancer.

**Wrong words:**
- ❌ "**Network Load Balancer**": layer 4, typically regional; lacks global HTTP routing.

📌 **When to use it:** Use it for TCP/UDP traffic in a region.
🏢 **Office example:** A switchboard for one city.

### ✅ D
> **D.** Use an external Application Load Balancer in Global mode.

**Why it's correct:**
- ✔️ "**external Application Load Balancer in Global mode**" matches "**global users**" + "**minimize latency**": routes each user to the nearest region.

📌 **When to use it:** Use it when one web address should send everyone to the closest branch.
🏢 **Office example:** One phone number that rings whichever branch is nearest the caller.

### ❌ E
> **E.** Deploy all of your VMs in a single Google Cloud region with the largest available CIDR range.

**Wrong words:**
- ❌ "**single Google Cloud region**": far users get high latency; CIDR size doesn't help.

📌 **When to use it:** Use one region when users are local.
🏢 **Office example:** One office for the whole world.

---

## 🛒 E-Commerce Full-Stack Example

MIGs `storefront-us`, `-eu`, `-asia` behind global ALB `shopnow-web`.

---

## 🧠 Key Takeaways / Memory Tips

- **Global users → VMs in multiple regions + global external Application Load Balancer.**
  🧠 *"**Many regions, one global door.**"*
- Related: **Q195**, **Q293**.

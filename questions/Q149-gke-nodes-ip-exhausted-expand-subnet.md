# Q149: GKE Nodes Out of IPs in a Shared Subnet (Expand the Subnet's CIDR Range)

**Topic:** VPC / GKE networking (VPC-native clusters, primary vs alias ranges, expand-ip-range)

## ❓ Question
> You are running multiple VPC-native Google Kubernetes Engine clusters in the same subnet. The IPs available for the nodes are exhausted, and you want to ensure that the clusters can grow in nodes when needed. What should you do?
>
> **A.** Create a new subnet in the same region as the subnet being used.
>
> **B.** Add an alias IP range to the subnet used by the GKE clusters.
>
> **C.** Create a new VPC, and set up VPC peering with the existing VPC.
>
> **D.** Expand the CIDR range of the relevant subnet for the cluster.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Node IPs come from the subnet's **primary range**, and it's full. How do the clusters get room to add nodes?

**Clues in the question:**
- "**IPs available for the nodes are exhausted**": **nodes** use the subnet's **primary** range.
- "**clusters can grow in nodes**": make that range bigger → **expand the subnet** (Q082, Q129). Existing clusters keep working.

**Exam topic:** VPC / GKE.

---

## 📚 Key Terms Explained

### 1. VPC-native cluster
- **What it is:** A GKE cluster where **nodes** use the subnet's **primary range** and **pods/services** use **secondary (alias) ranges**.
- **Looks like:** primary 10.0.0.0/24 (nodes), secondary pods 10.4.0.0/14
- **Not to be confused with:** routes-based clusters.
- **Analogy:** 🏢 Desks (nodes) from the main floor plan; seats (pods) from side rooms.
- **In the online store:** ShopNow's GKE clusters.

### 2. Expand subnet range 🔑
- **What it is:** Grow the primary range in place, with no downtime.
- **Looks like:** `gcloud compute networks subnets expand-ip-range gke-subnet --region=us-central1 --prefix-length=22`
- **Not to be confused with:** adding a secondary range.
- **Analogy:** 🔨 Knocking down a wall for more desks.
- **In the online store:** Room for 1000 nodes.

### 🔗 How they fit together
```
 gke-subnet primary 10.0.0.0/24 (nodes, full) → expand to /22 ✅ → more node IPs
 secondary ranges (pods/services) unchanged
```

---

## 🌍 Real-World Scenario

Three GKE clusters share one subnet, and new nodes fail with "IP space exhausted". The engineer runs **expand-ip-range** on the subnet, and the cluster autoscaler can add nodes again.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a new subnet in the same region as the subnet being used.

**Wrong words:**
- ❌ "**Create a new subnet**": existing clusters can't simply move their node pools to another subnet. Their nodes must come from their cluster's subnet.

📌 **When to use it:** Use a new subnet for new clusters or workloads.
🏢 **Office example:** Opening a new floor for a team that must sit on their current floor.

### ❌ B
> **B.** Add an alias IP range to the subnet used by the GKE clusters.

**Wrong words:**
- ❌ "**Add an alias IP range**": alias (secondary) ranges are for **pods and services**, not node IPs.

📌 **When to use it:** Use secondary ranges when pod or service IPs run out.
🏢 **Office example:** Adding visitor seats when you need more staff desks.

### ❌ C
> **C.** Create a new VPC, and set up VPC peering with the existing VPC.

**Wrong words:**
- ❌ "**new VPC … VPC peering**": it doesn't give the existing clusters more node IPs, and it adds complexity.

📌 **When to use it:** Use peering to connect separate networks.
🏢 **Office example:** Building a new building and a bridge to add desks to the old floor.

### ✅ D
> **D.** Expand the CIDR range of the relevant subnet for the cluster.

**Why it's correct:**
- ✔️ "**Expand the CIDR range of the relevant subnet**" matches "**IPs available for the nodes are exhausted**": nodes get addresses from the bigger primary range.
- ✔️ "**Expand**" (in place, no downtime) matches "**ensure that the clusters can grow in nodes**".

📌 **When to use it:** Use it when the space everyone shares is full and can be made bigger.
🏢 **Office example:** Knocking down a wall so the floor fits more desks.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud compute networks subnets expand-ip-range shop-gke-subnet --region=us-central1 --prefix-length=22
# /24 (256) → /22 (1024): Black Friday autoscaling can add nodes again
```

---

## 🧠 Key Takeaways / Memory Tips

- **Nodes out of IPs → expand the subnet's primary range.** Pods out of IPs → secondary ranges.
- Same fix as Q082 and Q129.
  🧠 *"**Node IPs full? Expand the subnet.**"*
- Related: **Q082**, **Q129** (expand-ip-range).

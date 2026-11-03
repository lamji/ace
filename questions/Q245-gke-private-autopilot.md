# Q245: GKE With Verifiable Node Integrity, No Internet Access to Nodes, Low Ops (Private Autopilot Cluster)

**Topic:** GKE (Autopilot, private clusters, Shielded Nodes)

## ❓ Question
> You want to set up a Google Kubernetes Engine cluster. Verifiable node identity and integrity are required for the cluster, and nodes cannot be accessed from the internet. You want to reduce the operational cost of managing your cluster, and you want to follow Google-recommended practices. What should you do?
>
> **A.** Deploy a private autopilot cluster.
>
> **B.** Deploy a public autopilot cluster.
>
> **C.** Deploy a standard public cluster and enable shielded nodes.
>
> **D.** Deploy a standard private cluster and enable shielded nodes.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Shielded nodes**, **no public node access**, **least management**.

**Clues in the question:**
- "**Verifiable node identity and integrity**" → Shielded GKE Nodes (**always on in Autopilot**).
- "**nodes cannot be accessed from the internet**" → **private** cluster.
- "**reduce the operational cost**" → **Autopilot**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. Shielded GKE Nodes 🔑
- **What it is:** Nodes with secure boot and verified identity, so they can't be impersonated. Enabled by default in Autopilot.
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🛡️ Tamper-proof ID cards for each node.
- **In the online store:** —

### 2. Private cluster
- **What it is:** Nodes get **only internal IPs**; not reachable from the internet.
- **Looks like:** `--enable-private-nodes`
- **Not to be confused with:** public cluster.
- **Analogy:** 🏢 Staff floors with no street door.
- **In the online store:** ShopNow prod.

### 🔗 How they fit together
```
 Autopilot (Google manages nodes, Shielded always on) + private nodes ✅
```

---

## 🌍 Real-World Scenario

A fintech needs tamper-proof nodes with no public IPs and a small ops team. They create a **private Autopilot** cluster.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy a private autopilot cluster.

**Why it's correct:**
- ✔️ "**private**" matches "**nodes cannot be accessed from the internet**".
- ✔️ "**autopilot**" matches "**reduce the operational cost**" and includes Shielded Nodes, which matches "**Verifiable node identity and integrity**".

📌 **When to use it:** Use it when you need a locked-down cluster but don't want to manage the machines.
🏢 **Office example:** A serviced office with tamper-proof ID cards and no street entrance to the work floors.

### ❌ B
> **B.** Deploy a public autopilot cluster.

**Wrong words:**
- ✔️ Autopilot is right.
- ❌ "**public**": nodes get public IPs.

📌 **When to use it:** Use public clusters for simple, non-sensitive tests.
🏢 **Office example:** A serviced office with a street door on every floor.

### ❌ C
> **C.** Deploy a standard public cluster and enable shielded nodes.

**Wrong words:**
- ✔️ Shielded nodes are right.
- ❌ "**standard**": more to manage. ❌ "**public**": nodes reachable.

📌 **When to use it:** Use Standard public for full control in non-sensitive cases.
🏢 **Office example:** Managing your own building with open doors.

### ❌ D
> **D.** Deploy a standard private cluster and enable shielded nodes.

**Wrong words:**
- ✔️ "private" + "shielded nodes" meet security.
- ❌ "**standard**": you manage nodes, against "**reduce the operational cost**".

📌 **When to use it:** Use Standard private when you need node-level control.
🏢 **Office example:** A secure building you have to run yourself.

---

## 🛒 E-Commerce Full-Stack Example

`gcloud container clusters create-auto shopnow-prod --region=us-central1 --enable-private-nodes --release-channel=stable`

---

## 🧠 Key Takeaways / Memory Tips

- **Secure + low ops GKE → private Autopilot** (Shielded Nodes built in).
  🧠 *"**Private for no internet, Autopilot for no toil.**"*
- Related: **Q238**.

# Q288: Database + Backend on GKE Standard: No Data Loss, Enough Nodes Automatically (StatefulSet + Cluster Autoscaling)

**Topic:** GKE (StatefulSets, cluster autoscaler)

## ❓ Question
> You are planning to migrate a database and a backend application to a Standard Google Kubernetes Engine (GKE) cluster. You need to prevent data loss and make sure there are enough nodes available for your backend application based on the demands of your workloads. You want to follow Google-recommended practices and minimize the amount of manual work required. What should you do?
>
> **A.** Run your database as a StatefulSet. Configure cluster autoscaling to handle changes in the demands of your workloads.
>
> **B.** Run your database as a single Pod. Run the resize command when you notice changes in the demands of your workloads.
>
> **C.** Run your database as a DaemonSet. Run the resize command when you notice changes in the demands of your workloads.
>
> **D.** Run your database as a Deployment. Configure cluster autoscaling to handle changes in the demands of your workloads.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You will move a database and a backend app to a Standard GKE cluster.
- **What you must achieve:** Prevent data loss and keep enough nodes for the backend as demand changes.
- **The limits:** Follow recommended practice with little manual work.
- **What they're really asking:** How do you store the database's data safely and size the nodes automatically?

**Clues in the question:**
- "**prevent data loss**" for a **database** → **StatefulSet** (stable identity + persistent volume per pod).
- "**enough nodes … minimize … manual work**" → **cluster autoscaling**.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. StatefulSet 🔑
- **What it is:** Kubernetes object for stateful apps: each pod has a stable name and its **own persistent disk** that survives restarts.
- **Looks like:** `kind: StatefulSet … volumeClaimTemplates:`
- **Not to be confused with:** Deployment.
- **Analogy:** 🗄️ Each clerk keeps their own filing cabinet even after a break.
- **In the online store:** Postgres on GKE.

### 2. DaemonSet
- **What it is:** Runs one pod **on every node** (agents, log collectors).
- **Looks like:** —
- **Not to be confused with:** —
- **Analogy:** 🧹 One cleaner per floor.
- **In the online store:** —

### 🔗 How they fit together
```
 db StatefulSet (pod db-0 + PVC) ✅   backend Deployment   cluster autoscaler adds nodes ✅
```

---

## 🌍 Real-World Scenario

A team runs PostgreSQL as a **StatefulSet** with persistent volumes, and enables **cluster autoscaling** so the backend always has room.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Run your database as a StatefulSet. Configure cluster autoscaling to handle changes in the demands of your workloads.

**Why it's correct:**
- ✔️ "**Run your database as a StatefulSet**" matches "**prevent data loss**": each pod keeps its persistent volume.
- ✔️ "**Configure cluster autoscaling**" matches "**enough nodes … based on the demands**" + "**minimize the amount of manual work**".

📌 **When to use it:** Use it when a program keeps important records and the number of machines should follow demand.
🏢 **Office example:** Each records clerk keeps their own locked cabinet, and the building adds floors automatically when busy.

### ❌ B
> **B.** Run your database as a single Pod. Run the resize command when you notice changes in the demands of your workloads.

**Wrong words:**
- ❌ "**single Pod**": not managed; if it dies, it isn't recreated with its identity.
- ❌ "**Run the resize command when you notice**": manual.

📌 **When to use it:** Use a bare pod only for quick tests.
🏢 **Office example:** One clerk with no replacement plan, and adding floors by hand.

### ❌ C
> **C.** Run your database as a DaemonSet. Run the resize command when you notice changes in the demands of your workloads.

**Wrong words:**
- ❌ "**DaemonSet**": one copy per node — wrong for a database.
- ❌ Manual resize.

📌 **When to use it:** Use DaemonSets for per-node agents.
🏢 **Office example:** Hiring a records clerk on every floor.

### ❌ D
> **D.** Run your database as a Deployment. Configure cluster autoscaling to handle changes in the demands of your workloads.

**Wrong words:**
- ✔️ Cluster autoscaling is right.
- ❌ "**Deployment**" for a database: pods are interchangeable without stable per-pod storage.

📌 **When to use it:** Use Deployments for stateless apps.
🏢 **Office example:** Clerks who swap cabinets randomly.

---

## 🛒 E-Commerce Full-Stack Example

`orders-db` StatefulSet (1 replica, PVC 200Gi pd-ssd) + `orders-api` Deployment; node pool autoscaling 3–15.

---

## 🧠 Key Takeaways / Memory Tips

- **Database on Kubernetes → StatefulSet. Enough nodes automatically → cluster autoscaler.**
  🧠 *"**Stateful data, StatefulSet.**"*
- Related: **Q175**, **Q182**.

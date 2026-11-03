# Q277: Stateless App That Must Run on VMs and Scale With Traffic (Managed Instance Group + Autoscaling)

**Topic:** Compute Engine (MIG autoscaling)

## ❓ Question
> Your team has developed a stateless application which requires it to be run directly on virtual machines. The application is expected to receive a fluctuating amount of traffic and needs to scale automatically. You need to deploy the application. What should you do?
>
> **A.** Deploy the application on a managed instance group and configure autoscaling.
>
> **B.** Deploy the application on a Kubernetes Engine cluster and configure node pool autoscaling.
>
> **C.** Deploy the application on Cloud Functions and configure the maximum number instances.
>
> **D.** Deploy the application on Cloud Run and configure autoscaling.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** **Must run on VMs**, stateless, scale automatically.

**Clues in the question:**
- "**run directly on virtual machines**" → Compute Engine.
- "**scale automatically**" + "**stateless**" → **MIG with autoscaling**.

**Exam topic:** Compute Engine.

---

## 📚 Key Terms Explained

### 1. Managed instance group 🔑 (review from Q224)
- **What it is:** Identical VMs from a template; autoscaling, autohealing, rolling updates.
- **Looks like:** `gcloud compute instance-groups managed set-autoscaling web-mig --max-num-replicas=20 --target-cpu-utilization=0.6`
- **Not to be confused with:** GKE, Cloud Run.
- **Analogy:** 👥 A team of identical workers.
- **In the online store:** Web tier.

### 🔗 How they fit together
```
 traffic ↑ → MIG adds VMs ✅   traffic ↓ → removes VMs
```

---

## 🌍 Real-World Scenario

A legacy app needs VMs. The team builds an instance template and a **MIG with autoscaling** behind a load balancer.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy the application on a managed instance group and configure autoscaling.

**Why it's correct:**
- ✔️ "**managed instance group**" matches "**run directly on virtual machines**".
- ✔️ "**configure autoscaling**" matches "**fluctuating amount of traffic and needs to scale automatically**".

📌 **When to use it:** Use it when your program has to run on its own machines and demand goes up and down.
🏢 **Office example:** A team of identical workers that grows when it's busy and shrinks when it's quiet.

### ❌ B
> **B.** Deploy the application on a Kubernetes Engine cluster and configure node pool autoscaling.

**Wrong words:**
- ❌ "**Kubernetes Engine cluster**": runs containers, not directly on VMs.

📌 **When to use it:** Use GKE for containerized apps.
🏢 **Office example:** Moving the workers into a shared co-working space.

### ❌ C
> **C.** Deploy the application on Cloud Functions and configure the maximum number instances.

**Wrong words:**
- ❌ "**Cloud Functions**": serverless functions, not VMs.

📌 **When to use it:** Use Functions for small event handlers.
🏢 **Office example:** Hiring freelancers when you need staff on site.

### ❌ D
> **D.** Deploy the application on Cloud Run and configure autoscaling.

**Wrong words:**
- ❌ "**Cloud Run**": serverless containers, not VMs.

📌 **When to use it:** Use Cloud Run for containerized web apps.
🏢 **Office example:** Taxis when you were told to own the cars.

---

## 🛒 E-Commerce Full-Stack Example

MIG `legacy-api` from template `legacy-api-v4`, autoscaling 2–20 on CPU 60%, behind the HTTPS LB.

---

## 🧠 Key Takeaways / Memory Tips

- **Must be VMs + autoscale → MIG with autoscaling.**
  🧠 *"**VMs that grow = MIG.**"*
- Related: **Q224**, **Q221**.

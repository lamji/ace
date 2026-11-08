# Q263: Secure Autoscaling Website With Static Content in Cloud Storage (External HTTPS LB, Managed Cert, URL Map to Bucket Backend)

**Topic:** Load balancing (HTTPS LB, backend buckets)

## ❓ Question
> Your customer wants you to create a secure website with autoscaling based on the compute instance CPU load. You want to enhance performance by storing static content in Cloud Storage. Which resources are needed to distribute the user traffic?
>
> **A.** An external HTTP(S) load balancer with a managed SSL certificate to distribute the load and a URL map to target the requests for the static content to the Cloud Storage backend.
>
> **B.** An external network load balancer pointing to the backend instances to distribute the load evenly. The web servers will forward the request to the Cloud Storage as needed.
>
> **C.** An internal HTTP(S) load balancer together with Identity-Aware Proxy to allow only HTTPS traffic.
>
> **D.** An external HTTP(S) load balancer to distribute the load and a URL map to target the requests for the static content to the Cloud Storage backend. Install the HTTPS certificates on the instance.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A customer wants a secure website that autoscales on VM CPU load, with static content (images, CSS) served from Cloud Storage.
- **What you must achieve:** Distribute user traffic correctly.
- **The limits:** Secure (HTTPS), and both VMs and Cloud Storage serve content.
- **What they're really asking:** Which load balancer pieces do you need to send traffic to both?

**Clues in the question:**
- "**secure website**" → HTTPS with a **Google-managed SSL certificate** on the LB.
- "**static content in Cloud Storage**" → **URL map** routes `/static/*` to a **backend bucket**.
- Public → **external** HTTP(S) LB.

**Exam topic:** Load balancing.

---

## 📚 Key Terms Explained

### 1. URL map + backend bucket 🔑
- **What it is:** The LB's routing rules: e.g. `/static/*` → Cloud Storage bucket, everything else → VM group.
- **Looks like:** path rule `/static/*` → `backend-bucket static-assets`
- **Not to be confused with:** —
- **Analogy:** 🧭 A receptionist sending visitors to different floors.
- **In the online store:** Product images from a bucket.

### 2. Google-managed SSL certificate
- **What it is:** A certificate Google issues and renews automatically, attached to the LB.
- **Looks like:** `gcloud compute ssl-certificates create web-cert --domains=shop.com`
- **Not to be confused with:** certificates on VMs.
- **Analogy:** 🪪 An ID badge renewed for you.
- **In the online store:** —

### 🔗 How they fit together
```
 users ─HTTPS─► External HTTPS LB (managed cert)
                 URL map: /static/* → bucket ✅ | /* → MIG (autoscaling) ✅
```

---

## 🌍 Real-World Scenario

A store puts an **external HTTPS LB** with a **managed certificate** in front: `/static/*` goes to a bucket, everything else to an autoscaling MIG.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** An external HTTP(S) load balancer with a managed SSL certificate to distribute the load and a URL map to target the requests for the static content to the Cloud Storage backend.

**Why it's correct:**
- ✔️ "**external HTTP(S) load balancer with a managed SSL certificate**" matches "**secure website**".
- ✔️ "**URL map to target the requests for the static content to the Cloud Storage backend**" matches "**storing static content in Cloud Storage**".
- ✔️ It distributes to the autoscaling instance group, which matches "**autoscaling based on the compute instance CPU load**".

📌 **When to use it:** Use it when a public website needs secure connections and should serve its pictures and files from cheap storage.
🏢 **Office example:** A receptionist with an official ID who sends visitors for brochures to the brochure rack and everyone else to the staff.

### ❌ B
> **B.** An external network load balancer pointing to the backend instances to distribute the load evenly. The web servers will forward the request to the Cloud Storage as needed.

**Wrong words:**
- ❌ "**external network load balancer**": no HTTPS termination or URL routing.
- ❌ "**web servers will forward the request to the Cloud Storage**": extra load on VMs.

📌 **When to use it:** Use a network LB for non-HTTP TCP/UDP.
🏢 **Office example:** Making staff fetch every brochure themselves.

### ❌ C
> **C.** An internal HTTP(S) load balancer together with Identity-Aware Proxy to allow only HTTPS traffic.

**Wrong words:**
- ❌ "**internal HTTP(S) load balancer**": not reachable by public users.

📌 **When to use it:** Use internal LBs for private apps.
🏢 **Office example:** A receptionist inside a locked floor.

### ❌ D
> **D.** An external HTTP(S) load balancer to distribute the load and a URL map to target the requests for the static content to the Cloud Storage backend. Install the HTTPS certificates on the instance.

**Wrong words:**
- ✔️ External HTTPS LB + URL map are right.
- ❌ "**Install the HTTPS certificates on the instance**": certificates belong on the LB; on every VM it's extra work.

📌 **When to use it:** Use self-managed certs only when required.
🏢 **Office example:** Giving every staff member their own ID instead of one at reception.

---

## 🛒 E-Commerce Full-Stack Example

HTTPS LB `shopnow-web`: cert `shopnow-managed-cert`; URL map `/static/*` → backend bucket `shopnow-static` (Cloud CDN on); default → backend service `web-mig`.

---

## 🧠 Key Takeaways / Memory Tips

- **Secure public site + static files → External HTTPS LB + managed cert + URL map to a backend bucket.**
  🧠 *"**One front desk: HTTPS badge, static to the bucket.**"*
- Related: **Q078**, **Q274**.

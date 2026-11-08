# Q051: Recreate Unhealthy VMs in an HTTPS Managed Instance Group (Health Check on Port 443)

**Topic:** Compute Engine (managed instance groups, health checks, autohealing)

## ❓ Question
> You need to create an autoscaling managed instance group for an HTTPS web application. You want to make sure that unhealthy VMs are recreated. What should you do?
>
> **A.** Create a health check on port 443 and use that when creating the Managed Instance Group.
>
> **B.** Select Multi-Zone instead of Single-Zone when creating the Managed Instance Group.
>
> **C.** In the Instance Template, add the label 'health-check'.
>
> **D.** In the Instance Template, add a startup script that sends a heartbeat to the metadata server.

**My answer:** — (didn't know)
**Correct answer:** A. Create a health check on port 443 and use that when creating the Managed Instance Group.
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are building an autoscaling managed instance group for an HTTPS web app.
- **What you must achieve:** Unhealthy VMs must be recreated automatically.
- **The limits:** None stated.
- **What they're really asking:** What do you configure so the group notices unhealthy VMs and replaces them?

**Clues in the question:**
- "**HTTPS web application**": HTTPS uses **port 443**, so the check should test that port.
- "**unhealthy VMs are recreated**": this is **autohealing**, which needs a **health check** attached to the managed instance group.
- "**managed instance group**": only a *managed* group can recreate VMs, because it has a template to rebuild them from.

**Exam topic:** Compute Engine (MIG autohealing). Same idea as **Q004**.

---

## 📚 Key Terms Explained

### 1. Managed Instance Group (MIG)
- **What it is:** A group of identical VMs that Google manages as one unit, all built from the same instance template. It can add VMs, remove VMs and replace broken ones.
- **Looks like:** `gcloud compute instance-groups managed create web-mig --template=web-tmpl --size=3 --zone=us-central1-a`
- **Not to be confused with:** an *unmanaged* instance group, which is just a list of different VMs. Google can't recreate those because there's no template.
- **Analogy:** 🏪 A franchise with a standard store blueprint. If one store burns down, head office rebuilds it from the same blueprint.
- **In the online store:** The storefront web servers run as `web-mig`, 3 to 10 identical VMs behind the load balancer.

### 2. Instance template
- **What it is:** A saved recipe for a VM: machine type, disk image, network, labels, startup script. The MIG uses it to create every VM.
- **Looks like:** `gcloud compute instance-templates create web-tmpl --machine-type=e2-medium --image-family=debian-12 --image-project=debian-cloud`
- **Not to be confused with:** a running VM. A template is just the recipe; it doesn't run anything.
- **Analogy:** 📋 The standard setup checklist IT uses for every new employee's laptop.
- **In the online store:** `web-tmpl` describes one storefront server, and the MIG stamps out copies of it.

### 3. Autoscaling
- **What it is:** A MIG setting that adds or removes VMs based on load (for example, keep CPU near 60%).
- **Looks like:** `gcloud compute instance-groups managed set-autoscaling web-mig --min-num-replicas=3 --max-num-replicas=10 --target-cpu-utilization=0.6`
- **Not to be confused with:** autohealing. Autoscaling changes **how many** VMs there are; it does **not** fix broken ones.
- **Analogy:** 👥 Calling in extra temp staff during the holiday rush.
- **In the online store:** More storefront VMs during a Black Friday sale, fewer at 3 a.m.

### 4. Health check 🔑
- **What it is:** A rule that tells Google to send a small test request to each VM on a set port and path every few seconds. A VM that keeps failing is marked unhealthy.
- **Looks like:** `gcloud compute health-checks create https web-hc --port=443 --request-path=/healthz --check-interval=10s --unhealthy-threshold=3`
- **Not to be confused with:** a label or a heartbeat that the VM sends out. In a health check, **Google** calls the VM, not the other way around.
- **Analogy:** 📞 A manager phoning each branch every 10 seconds: "Are you open?" Three missed calls and the branch is marked closed.
- **In the online store:** `web-hc` checks `https://<vm>:443/healthz` on every storefront VM.

### 5. Autohealing 🔑
- **What it is:** A MIG feature that **deletes and recreates** any VM that fails the health check attached to the MIG.
- **Looks like:** `gcloud compute instance-groups managed update web-mig --health-check=web-hc --initial-delay=300 --zone=us-central1-a`
- **Not to be confused with:** a VM restart after a crash. Autohealing also catches VMs that are running but whose app is frozen or broken.
- **Analogy:** 🔧 Facilities replaces any desk phone that fails the morning test, without anyone filing a ticket.
- **In the online store:** If a storefront VM's web server hangs, the MIG replaces that VM automatically.

### 6. Port 443 (HTTPS)
- **What it is:** The standard numbered "door" on a server for encrypted web traffic (HTTPS). Plain HTTP uses port 80.
- **Looks like:** `https://shopnow.com` = `https://shopnow.com:443`
- **Not to be confused with:** an IP address. The IP finds the server; the port picks the service on it.
- **Analogy:** 🚪 The building's address is the IP; door 443 is the one marked "Secure deliveries".
- **In the online store:** Shoppers' browsers connect to the storefront on port 443.

### 7. Label
- **What it is:** A key-value tag you attach to a resource to organize it or track costs, such as `env=prod`. Labels **don't make anything happen**.
- **Looks like:** `--labels=env=prod,team=storefront`
- **Not to be confused with:** a setting or feature switch. A label named "health-check" is just a sticker.
- **Analogy:** 🏷️ A colored sticker on a folder. It helps you sort folders but doesn't do any work.
- **In the online store:** `team=storefront` labels show up on the billing report so each team sees its costs.

### 8. Metadata server
- **What it is:** A built-in internal address (`169.254.169.254` / `metadata.google.internal`) that a VM **reads** to learn about itself: its name, project, service account token and startup script.
- **Looks like:** `curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/name`
- **Not to be confused with:** a monitoring service. It doesn't collect heartbeats or judge VM health.
- **Analogy:** 📖 The employee handbook at your desk. You read it; you don't report to it.
- **In the online store:** The storefront VM reads its service account token from the metadata server to talk to Cloud Storage.

### 🔗 How they fit together
```
Instance template (recipe)
        │ builds
        ▼
Managed Instance Group ──── autoscaler: how MANY VMs (load)
   │  VM1  VM2  VM3
   │
   └── autohealing ◄── health check (HTTPS :443 /healthz)
         VM2 fails 3 checks → MIG deletes VM2 → recreates it from the template ✅
```

---

## 🌍 Real-World Scenario

Your web servers run in a MIG. Every few weeks, one VM's web server freezes from a memory leak. The VM is still "running", so nothing restarts it, but users who land on it get errors. You attach an HTTPS health check on port 443 to the MIG. Now when a VM stops answering, the MIG deletes it and creates a fresh one from the template, with no phone call at 2 a.m.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a health check on port 443 and use that when creating the Managed Instance Group.

**Why it's correct:**
- ✔️ "**health check**" + "**use that when creating the Managed Instance Group**" matches "**unhealthy VMs are recreated**": a health check attached to a MIG turns on autohealing, which deletes and recreates failing VMs.
- ✔️ "**port 443**" matches "**HTTPS web application**": HTTPS listens on port 443, so the check tests the port the app actually serves.

Command version:
```
gcloud compute health-checks create https web-hc --port=443 --request-path=/healthz
gcloud compute instance-groups managed create web-mig --template=web-tmpl --size=3 \
    --zone=us-central1-a --health-check=web-hc --initial-delay=300
```
The first command creates the HTTPS check on port 443. The second creates the MIG with autohealing using that check. `--initial-delay=300` gives a new VM 5 minutes to boot before it can be judged unhealthy.

> ⚠️ Real-world note: also allow Google's health-checker IP ranges (`35.191.0.0/16`, `130.211.0.0/22`) through the firewall on port 443, or every VM will look unhealthy.

📌 **When to use it:** Use it when you want broken machines found and replaced automatically.
🏢 **Office example:** A manager calls each branch every few minutes, and any branch that stops answering gets reopened with fresh staff.

### ❌ B
> **B.** Select Multi-Zone instead of Single-Zone when creating the Managed Instance Group.

**Wrong words:**
- ❌ "**Select Multi-Zone instead of Single-Zone**": this spreads VMs across several zones so one zone outage doesn't take the whole site down. It does **not** detect or recreate an unhealthy VM; that still needs a health check.

📌 **When to use it:** Use it when you want the site to keep running even if one whole data center has a problem.
🏢 **Office example:** Opening branches in three different towns, so a storm in one town doesn't close the whole business.

### ❌ C
> **C.** In the Instance Template, add the label 'health-check'.

**Wrong words:**
- ❌ "**add the label 'health-check'**": a label is only a name tag for sorting and billing. It doesn't check anything or trigger any action.

📌 **When to use it:** Use labels when you want to sort things or split costs by team or environment.
🏢 **Office example:** Putting a "Sales" sticker on a folder so accounting can find it. The sticker does no work.

### ❌ D
> **D.** In the Instance Template, add a startup script that sends a heartbeat to the metadata server.

**Wrong words:**
- ✔️ "**add a startup script**" in an instance template is a real feature.
- ❌ "**sends a heartbeat to the metadata server**": the metadata server only answers a VM's questions about itself. It doesn't collect heartbeats or judge health, and a startup script runs only once at boot anyway.

📌 **When to use it:** Use a startup script when every new machine needs the same setup steps at boot (install software, start the web server).
🏢 **Office example:** The first-day checklist every new hire follows, not a daily attendance check.

---

## 🛒 E-Commerce Full-Stack Example

- The ShopNow storefront (Next.js server rendering) runs on `web-mig`, built from `web-tmpl`, behind the HTTPS load balancer.
- **Autoscaling:** 3–10 VMs, targeting 60% CPU, for sale days.
- **Autohealing:** health check `web-hc` hits `https://<vm>:443/healthz` every 10 seconds. The `/healthz` route returns `200 OK` only if the app can reach Cloud SQL.
- One night a VM's Node process hangs. After 3 failed checks, the MIG deletes it and builds a new one from `web-tmpl`. Shoppers never notice, because the load balancer had already stopped sending them to it.
- **Multi-zone** (option B) is still a good extra: the MIG runs across `us-central1-a/b/c`. But that protects against a zone outage, not a hung VM.

---

## 🧠 Key Takeaways / Memory Tips

- **Recreate unhealthy VMs = autohealing = a health check attached to the MIG.** Match the port to the app: HTTPS → **443**, HTTP → **80**.
- Autoscaling changes **how many** VMs; autohealing replaces **broken** ones. Multi-zone survives **zone outages**. Three different jobs.
- 🧠 *"**No health check, no healing.**"*
- If you see "MIG" + "unhealthy" / "recreated" / "automatically replaced" → think **health check + autohealing**. Related: **Q004**.

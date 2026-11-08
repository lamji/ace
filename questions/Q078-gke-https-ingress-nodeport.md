# Q078: Exposing a GKE App Publicly Over HTTPS (NodePort Service + Ingress)

**Topic:** GKE networking (Service types ClusterIP / NodePort / LoadBalancer, Ingress, HTTP(S) Cloud Load Balancer)

## ❓ Question
> You are using Google Kubernetes Engine with autoscaling enabled to host a new application. You want to expose this new application to the public, using HTTPS on a public IP address. What should you do?
>
> **A.** Create a Kubernetes Service of type NodePort for your application, and a Kubernetes Ingress to expose this Service via a Cloud Load Balancer.
>
> **B.** Create a Kubernetes Service of type ClusterIP for your application. Configure the public DNS name of your application using the IP of this Service.
>
> **C.** Create a Kubernetes Service of type NodePort to expose the application on port 443 of each node of the Kubernetes cluster. Configure the public DNS name of your application with the IP of every node of the cluster to achieve load-balancing.
>
> **D.** Create a HAProxy pod in the cluster to load-balance the traffic to all the pods of the application. Forward the public traffic to HAProxy with an iptable rule. Configure the DNS name of your application using the public IP of the node HAProxy is running on.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A new app runs on GKE with autoscaling.
- **What you must achieve:** Make it public over HTTPS on a public IP address.
- **The limits:** None stated.
- **What they're really asking:** Which Kubernetes objects should you create to expose it?

**Clues in the question:**
- "**expose this new application to the public**": needs a **public** IP, so internal-only options (ClusterIP) are out.
- "**using HTTPS**": HTTPS (with certificates) is handled by Google's **HTTP(S) load balancer**, which GKE creates from an **Ingress**.
- "**autoscaling enabled**": nodes change, so never point DNS at individual node IPs. Use a managed load balancer that updates itself.

**Exam topic:** GKE networking.

---

## 📚 Key Terms Explained

### 1️⃣ Service types
- **What it is:** A Kubernetes **Service** gives a group of pods one stable address. Types:
  - **ClusterIP**: an **internal** IP, reachable only inside the cluster.
  - **NodePort**: opens the same port (30000–32767) on **every node**.
  - **LoadBalancer**: creates a **TCP/UDP** network load balancer with a public IP (Q060).
- **Looks like:** `spec: type: NodePort, ports: [{port: 80, targetPort: 8080}]`
- **Not to be confused with:** an Ingress (HTTP/HTTPS rules in front of Services).
- **Analogy:** ☎️ ClusterIP = **internal extension**; NodePort = the **same side door on every floor**.
- **In the online store:** `storefront-svc` groups all storefront pods.

### 2️⃣ Ingress 🔑
- **What it is:** A Kubernetes object with **HTTP(S) rules** (hostnames, paths, TLS certificates). On GKE, creating an Ingress makes Google build an **external HTTP(S) Cloud Load Balancer** with **one public IP**, which sends traffic to your Service.
- **Looks like:**
  ```yaml
  kind: Ingress
  spec:
    tls: [{secretName: shopnow-tls}]
    rules: [{host: shop.example.com, http: {paths: [{path: /, pathType: Prefix,
             backend: {service: {name: storefront-svc, port: {number: 80}}}}]}}]
  ```
- **Not to be confused with:** a Service. The Ingress is the **front door with the address and the lock (HTTPS)**; the Service is the **hallway to the pods**.
- **Analogy:** 🏢 The building's **main entrance with security and a sign**, leading to the right department.
- **In the online store:** `https://shop.example.com` → Ingress → storefront pods.

### 3️⃣ Cloud HTTP(S) Load Balancer (review from Q040)
- **What it is:** Google's managed, global load balancer for web traffic. It holds the **public IP**, handles **HTTPS certificates**, checks pod health, and spreads traffic.
- **Not to be confused with:** DNS round-robin or a homemade proxy.
- **Analogy:** 🛎️ A **professional reception team** that greets every visitor and sends them to a free desk.

### 4️⃣ HAProxy / iptables
- **What it is:** HAProxy is load-balancer **software** you run yourself; iptables is Linux's **firewall/forwarding rules**.
- **Not to be confused with:** a managed load balancer. You'd run, patch and scale it yourself.
- **Analogy:** 🧍 **One volunteer** at the door directing everyone. If they go home, nobody gets in.

### 🔗 How they fit together
```
 Internet ──HTTPS──► 🌐 Cloud HTTP(S) Load Balancer (one public IP, TLS cert)   ← created by Ingress
                         │
                         ▼
                    Service storefront-svc (NodePort)
                         │
                 ┌───────┼───────┐
                pod     pod     pod   (nodes scale up/down; LB updates itself) ✅
```

---

## 🌍 Real-World Scenario

A team launches a public web app on GKE. They need a single HTTPS URL, a certificate, health checks, and something that keeps working as nodes are added and removed. The standard pattern is a **Service + Ingress**: GKE creates the Google HTTP(S) load balancer automatically, attaches the certificate, and updates the backends as the cluster scales.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a Kubernetes Service of type NodePort for your application, and a Kubernetes Ingress to expose this Service via a Cloud Load Balancer.

**Why it's correct:**
- ✔️ "**Kubernetes Ingress to expose this Service via a Cloud Load Balancer**" matches "**expose this new application to the public**": the Ingress creates an external load balancer with a public IP.
- ✔️ "**Ingress … Cloud Load Balancer**" matches "**using HTTPS on a public IP address**": the HTTP(S) load balancer handles HTTPS certificates on one public IP.
- ✔️ "**Service of type NodePort**" matches "**autoscaling enabled**": the Ingress load balancer sends traffic to the Service, and GKE keeps the backends updated as nodes change.

📌 **When to use it:** Use it when a public website needs one secure address that keeps working as servers come and go.
🏢 **Office example:** A main entrance with a reception team that greets every visitor and sends them to a free desk.

### ❌ B
> **B.** Create a Kubernetes Service of type ClusterIP for your application. Configure the public DNS name of your application using the IP of this Service.

**Wrong words:**
- ❌ "**Service of type ClusterIP**": a ClusterIP is **internal only**. It can't be reached from the internet.
- ❌ "**Configure the public DNS name … using the IP of this Service**": the public would get an IP they can't reach. And there's no HTTPS.

📌 **When to use it:** Use ClusterIP for services that only other pods in the cluster call, like an internal API.
🏢 **Office example:** Publishing an internal phone extension in the public directory. Outsiders can't dial it.

### ❌ C
> **C.** Create a Kubernetes Service of type NodePort to expose the application on port 443 of each node of the Kubernetes cluster. Configure the public DNS name of your application with the IP of every node of the cluster to achieve load-balancing.

**Wrong words:**
- ❌ "**expose the application on port 443 of each node**": NodePort only uses ports **30000–32767**, so 443 isn't allowed, and there's still no HTTPS certificate handling.
- ❌ "**Configure the public DNS name … with the IP of every node**": with **autoscaling**, nodes appear and disappear, so DNS would point at dead IPs. DNS doesn't check health either.

📌 **When to use it:** Use NodePort on its own only for testing, or behind a load balancer (as in A).
🏢 **Office example:** Listing every employee's desk phone in the public directory; when someone leaves, callers reach a dead line.

### ❌ D
> **D.** Create a HAProxy pod in the cluster to load-balance the traffic to all the pods of the application. Forward the public traffic to HAProxy with an iptable rule. Configure the DNS name of your application using the public IP of the node HAProxy is running on.

**Wrong words:**
- ❌ "**Create a HAProxy pod**" + "**iptable rule**": homemade load balancing you must build and maintain.
- ❌ "**using the public IP of the node HAProxy is running on**": if that one node is removed by **autoscaling** or fails, the whole site goes down.

📌 **When to use it:** Almost never on GKE. Only when you need a special feature that Google's load balancers don't offer.
🏢 **Office example:** One volunteer at the only door directing every visitor. If they leave, nobody gets in.

---

## 🛒 E-Commerce Full-Stack Example

```yaml
# storefront-svc.yaml
apiVersion: v1
kind: Service
metadata: {name: storefront-svc}
spec:
  type: NodePort
  selector: {app: storefront}
  ports: [{port: 80, targetPort: 3000}]
---
# storefront-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: storefront
  annotations: {networking.gke.io/managed-certificates: shopnow-cert}
spec:
  defaultBackend: {service: {name: storefront-svc, port: {number: 80}}}
```

`kubectl apply` → GKE builds the HTTPS load balancer → `https://shop.example.com` points to its single public IP. On Black Friday the cluster grows from 3 to 12 nodes, and the load balancer keeps up automatically.

---

## 🧠 Key Takeaways / Memory Tips

- **Public + HTTPS on GKE → Service + Ingress (HTTP(S) Cloud Load Balancer).**
- **ClusterIP = internal only.** NodePort = ports 30000–32767 on each node.
- **Never put node IPs in DNS** with autoscaling, and never rely on one homemade proxy.
  🧠 *"**HTTPS for the world → Ingress.**"*
- Related: **Q060** (Service type LoadBalancer, internal LB), **Q040** (HTTPS load balancer).

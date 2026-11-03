# Q060: VM in Another VPC Reaching a GKE App (Internal Load Balancer + VPC Peering)

**Topic:** GKE + Networking (Service type LoadBalancer, internal load balancer annotation, VPC Network Peering, Cloud Armor)

## ❓ Question
> You have an application running in Google Kubernetes Engine (GKE) with cluster autoscaling enabled. The application exposes a TCP endpoint. There are several replicas of this application. You have a Compute Engine instance in the same region, but in another Virtual Private Cloud (VPC), called gce-network, that has no overlapping IP ranges with the first VPC. This instance needs to connect to the application on GKE. You want to minimize effort. What should you do?
>
> **A.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Set the service's externalTrafficPolicy to Cluster. 3. Configure the Compute Engine instance to use the address of the load balancer that has been created.
>
> **B.** 1. In GKE, create a Service of type NodePort that uses the application's Pods as backend. 2. Create a Compute Engine instance called proxy with 2 network interfaces, one in each VPC. 3. Use iptables on this instance to forward traffic from gce-network to the GKE nodes. 4. Configure the Compute Engine instance to use the address of proxy in gce-network as endpoint.
>
> **C.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Add an annotation to this service: cloud.google.com/load-balancer-type: Internal 3. Peer the two VPCs together. 4. Configure the Compute Engine instance to use the address of the load balancer that has been created.
>
> **D.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Add a Cloud Armor Security Policy to the load balancer that whitelists the internal IPs of the MIG's instances. 3. Configure the Compute Engine instance to use the address of the load balancer that has been created.

**My answer:** D
**Correct answer:** C
**Result:** ❌ Incorrect

> Why D was tempting: it sounds secure ("whitelists the internal IPs"). But the two VPCs are still **not connected**, so internal IPs can't even reach the load balancer, and Cloud Armor doesn't work on this kind of load balancer.

---

## 📖 What the Question Is Asking

**In plain words:** Your app runs as several pods in GKE (VPC 1). A VM lives in a **different VPC** (`gce-network`, VPC 2), same region, no overlapping IP ranges. The VM must call the app. Do it with the **least effort**.

| Question words | What they point to |
|---|---|
| "**exposes a TCP endpoint**" + "**several replicas**" | Put **one load balancer address** in front of all pods → Service type **LoadBalancer** |
| "**another Virtual Private Cloud (VPC)**" | Two separate networks can't talk privately until you **connect** them → **VPC Peering** |
| "**no overlapping IP ranges**" | The condition peering needs → hint that peering is the answer |
| "**same region**" | An **internal** load balancer is regional, so it works |
| "**minimize effort**" | Built-in features (annotation + peering), not a hand-made proxy VM |

**Exam topic:** GKE + VPC networking.

---

## 📚 Key Terms Explained

### 1️⃣ Kubernetes Service type LoadBalancer
- **What it is:** A Kubernetes object that gives your pods **one stable address**. With type `LoadBalancer`, GKE **creates a Google Cloud load balancer** for you automatically. By default it's **external** (public IP).
- **Looks like:**
  ```yaml
  kind: Service
  spec:
    type: LoadBalancer
    selector: {app: inventory}
    ports: [{port: 8080, protocol: TCP}]
  ```
- **Not to be confused with:** NodePort, which only opens a port on each node; you'd have to route to the nodes yourself.
- **Analogy:** ☎️ A **main reception number** that forwards each call to any free agent (pod).
- **In the online store:** One address for all `inventory` API pods.

### 2️⃣ Internal load balancer annotation 🔑
- **What it is:** A label on the Service that says "make the load balancer **internal**", giving it a **private IP** (like `10.0.1.50`) reachable only from inside the network, not the internet.
- **Looks like:**
  ```yaml
  metadata:
    annotations:
      cloud.google.com/load-balancer-type: "Internal"
  ```
  *(Newer GKE versions use `networking.gke.io/load-balancer-type: "Internal"`, same idea.)*
- **Not to be confused with:** an external load balancer with a **public** IP.
- **Analogy:** ☎️ An **internal extension number**, only callable from inside the company phone system.
- **In the online store:** The inventory API is private; only internal servers can call it.

### 3️⃣ VPC Network Peering 🔑 (review from Q054)
- **What it is:** A link between **two separate VPCs** so their machines can reach each other's **private IPs**. Requires **non-overlapping** IP ranges.
- **Looks like:** `gke-vpc (10.0.0.0/16) ⇄ gce-network (10.1.0.0/16)`
- **Not to be confused with:** VPN (tunnel over the internet) or one VPC with two subnets (already connected).
- **Analogy:** 🔗 Connecting **two companies' phone systems** so they can dial each other's extensions.
- **In the online store:** The reporting VM in `gce-network` can call the GKE inventory API privately.

### 4️⃣ Cloud Armor
- **What it is:** A **web application firewall** that filters traffic (allow/deny IPs, block attacks) at **external HTTP(S) load balancers**.
- **Looks like:** `gcloud compute security-policies rules create 1000 --security-policy=allow-office --src-ip-ranges=203.0.113.0/24 --action=allow`
- **Not to be confused with:** a network connector. Cloud Armor **filters** traffic; it doesn't **connect** two VPCs. It also doesn't apply to the TCP load balancer a GKE Service creates.
- **Analogy:** 🛡️ A **security guard at the public front door**. Useless if the visitor's building has no road to yours.

### 5️⃣ externalTrafficPolicy
- **What it is:** A Service setting that controls how an **external** load balancer sends traffic to nodes (`Cluster` = any node, `Local` = only nodes with the pod). It doesn't change **public vs private**.
- **Looks like:** `spec.externalTrafficPolicy: Cluster`

### 🔗 How they fit together
```
 VPC 1 (GKE)                                   VPC 2 (gce-network)
 ┌─────────────────────────────┐   peering ✅  ┌────────────────────┐
 │ Internal LB 10.0.1.50 ◄──────┼──────────────┼── 🖥️ VM 10.1.0.5    │
 │   ├── pod 1                 │               └────────────────────┘
 │   ├── pod 2                 │
 │   └── pod 3                 │
 └─────────────────────────────┘
 Without peering, 10.1.0.5 can't reach 10.0.1.50 at all.
```

---

## 🌍 Real-World Scenario

A company's backend team runs services on GKE in its own VPC. Another team has VMs (reporting, batch jobs) in a separate VPC. They want the VMs to call the GKE service **privately**, without exposing it to the internet. The standard pattern: expose the GKE service with an **internal load balancer** and **peer** the two VPCs. Two small changes, everything managed by Google, and it follows the pods automatically as they scale.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Set the service's externalTrafficPolicy to Cluster. 3. Configure the Compute Engine instance to use the address of the load balancer that has been created.

**Wrong words:**
- ✔️ "create a Service of type LoadBalancer that uses the application's Pods as backend" is fine.
- ❌ "**Set the service's externalTrafficPolicy to Cluster**": this only changes how traffic spreads across nodes. The load balancer stays **external** with a **public IP**, so the app is exposed to the whole internet and the VM must go out to the internet to reach it.

📌 **When to use it:** Use it when the app should be reachable from the public internet.
🏢 **Office example:** Publishing the main phone number in the public directory so anyone can call.

### ❌ B
> **B.** 1. In GKE, create a Service of type NodePort that uses the application's Pods as backend. 2. Create a Compute Engine instance called proxy with 2 network interfaces, one in each VPC. 3. Use iptables on this instance to forward traffic from gce-network to the GKE nodes. 4. Configure the Compute Engine instance to use the address of proxy in gce-network as endpoint.

**Wrong words:**
- ❌ "**Create a Compute Engine instance called proxy with 2 network interfaces**": an extra VM you must build, patch and keep running. It's a single point of failure.
- ❌ "**Use iptables on this instance to forward traffic**": hand-written forwarding rules, and with **cluster autoscaling** the nodes change, so you'd keep updating them. This is the opposite of "minimize effort".

📌 **When to use it:** Almost never. Use it only when two networks can't be peered and you have no other option.
🏢 **Office example:** Hiring a person to sit between two buildings and pass every phone message across by hand.

### ✅ C
> **C.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Add an annotation to this service: cloud.google.com/load-balancer-type: Internal 3. Peer the two VPCs together. 4. Configure the Compute Engine instance to use the address of the load balancer that has been created.

**Why it's correct:**

- ✔️ "**Service of type LoadBalancer that uses the application's Pods as backend**" matches "**several replicas**", "**TCP endpoint**", "cluster autoscaling": One address in front of all pods; GKE keeps it updated as pods and nodes change.
- ✔️ "**cloud.google.com/load-balancer-type: Internal**" matches "**Compute Engine instance in the same region**": Gives a **private** IP. An internal LB is regional, and the VM is in the same region, so it fits. Not exposed to the internet.
- ✔️ "**Peer the two VPCs together**" matches "**another Virtual Private Cloud**", "**no overlapping IP ranges**": Peering connects the two networks, and it needs non-overlapping ranges, which the question guarantees.
- ✔️ "**use the address of the load balancer**" matches "**This instance needs to connect to the application**": The VM calls the LB's private IP through the peering.
- ✔️ All built-in, 2 small changes matches "**minimize effort**": No extra VMs, no manual rules.

📌 **When to use it:** Use it when servers in another private network must call your app privately, without putting it on the internet.
🏢 **Office example:** Connecting two companies' phone systems and giving the help desk an internal extension, so the partner's staff can dial it directly.

### ❌ D (your answer)
> **D.** 1. In GKE, create a Service of type LoadBalancer that uses the application's Pods as backend. 2. Add a Cloud Armor Security Policy to the load balancer that whitelists the internal IPs of the MIG's instances. 3. Configure the Compute Engine instance to use the address of the load balancer that has been created.

**Wrong words:**
- ✔️ "create a Service of type LoadBalancer that uses the application's Pods as backend" is fine.
- ❌ "**Add a Cloud Armor Security Policy to the load balancer**": a GKE `LoadBalancer` Service creates a **TCP network load balancer**, and Cloud Armor IP rules are for **HTTP(S)** load balancers. It doesn't fit here.
- ❌ "**whitelists the internal IPs**": the load balancer is **external** (public IP). Traffic from the VM to a public IP arrives from the VM's **public** address, not its internal IP, so an allowlist of internal IPs would block it. And nothing **connects** the two VPCs privately.
- ❌ "**the MIG's instances**": the question never mentions a MIG. It's a single Compute Engine instance.

📌 **When to use it:** Use Cloud Armor when a public website behind an HTTPS load balancer must block bad visitors or allow only certain IPs.
🏢 **Office example:** A guard at the public front door with a list of allowed visitors. It doesn't help if there's no road between the two buildings.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow runs its **inventory API** on GKE in `shop-vpc` (10.0.0.0/16). The **reporting VM** lives in `gce-network` (10.1.0.0/16) and needs stock levels every hour.

```yaml
# inventory-ilb.yaml
apiVersion: v1
kind: Service
metadata:
  name: inventory-ilb
  annotations:
    cloud.google.com/load-balancer-type: "Internal"
spec:
  type: LoadBalancer
  selector: {app: inventory}
  ports: [{port: 8080, protocol: TCP}]
```

```bash
kubectl apply -f inventory-ilb.yaml          # → private IP 10.0.1.50

# Peering must be created from BOTH sides
gcloud compute networks peerings create shop-to-gce --network=shop-vpc --peer-network=gce-network
gcloud compute networks peerings create gce-to-shop --network=gce-network --peer-network=shop-vpc

# On the reporting VM
curl http://10.0.1.50:8080/stock
```

| Option | Inventory API on the internet? | Extra things to run |
|---|---|---|
| **C** | ❌ private ✅ | none |
| A | ✅ public ❌ | none, but exposed |
| B | private | a proxy VM + iptables rules |
| D | ✅ public, and the allowlist doesn't work | — |

---

## 🧠 Key Takeaways / Memory Tips

- **App in GKE + caller in another VPC + private → internal load balancer + VPC peering.**
- **"No overlapping IP ranges" in a question = a hint for VPC peering.**
- `type: LoadBalancer` alone = **public**. Add the **Internal** annotation for a private IP.
- **Cloud Armor filters traffic; it never connects networks.**
  🧠 *"**Internal LB = private door. Peering = the road between the buildings.** You need both."*
- Related: **Q054** (VPN/peering only for separate VPCs), **Q040** (HTTP(S) vs TCP load balancers), **Q012** (GKE deploy).

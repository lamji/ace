# Q040: Terminating Client SSL Sessions for a Public Web App

**Topic:** Cloud Load Balancing (HTTPS, TLS termination, external vs internal load balancers)

## ❓ Question
> You have an instance group that you want to load balance. You want the load balancer to terminate the client SSL session. The instance group is used to serve a public web application over HTTPS. You want to follow Google-recommended practices. What should you do?
>
> **A.** Configure an HTTP(S) load balancer.
>
> **B.** Configure an internal TCP load balancer.
>
> **C.** Configure an external SSL proxy load balancer.
>
> **D.** Configure an external TCP proxy load balancer.

**My answer:** A
**Correct answer:** A — Configure an HTTP(S) load balancer.
**Result:** ✅ Correct

---

## 1. ✅ Verdict

**Correct — your answer is A.** An external HTTP(S) load balancer is designed for internet-facing web traffic. It accepts HTTPS from clients, terminates the encrypted client session, and distributes web requests to the instance group.

## 2. 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A group of VMs serves a public website over HTTPS (encrypted web traffic).
- **What you must achieve:** Put a load balancer in front, and have the load balancer handle (terminate) the encrypted connection from visitors.
- **The limits:** Follow Google's recommended practice.
- **What they're really asking:** Which load balancer type and setup do this?

- **“public web application over HTTPS”** means internet-facing web traffic.
- **“terminate the client SSL session”** means the encrypted client connection ends at the load balancer, which then sends a separate request to a backend.
- **“Google-recommended practices”** points to an Application Load Balancer for HTTP(S) application traffic.
- **Exam topic:** Cloud Load Balancing and TLS termination.

## 2.5 📚 Key Terms Explained

### Instance group
- **What it is:** A collection of Compute Engine virtual machines managed together and used as a backend for services such as load balancers.
- **Analogy:** A team of employees who can all answer the same kind of request.
- **In the online store:** An instance group could run several copies of the storefront or order API.

### Load balancer
- **What it is:** A service that distributes incoming connections or requests across backend machines.
- **Analogy:** A receptionist who directs visitors to available staff.
- **In the online store:** It directs shoppers' web requests to healthy frontend servers.

### Client
- **What it is:** The person or software requesting a service. Here, it is a shopper's browser.
- **Analogy:** A visitor contacting the office.
- **In the online store:** The browser that opens the storefront and sends checkout requests.

### SSL and TLS
- **What they are:** SSL is the older name still used in some product wording; TLS is the modern protocol that encrypts a connection between a client and a server.
- **Analogy:** A sealed envelope for information sent between the visitor and the office.
- **In the online store:** TLS protects shoppers' sign-in and payment traffic while it travels over the internet.

### SSL/TLS session
- **What it is:** The secure connection established between a client and a server. In this question, the connection is between the browser and load balancer.
- **Analogy:** A private phone call between the visitor and the receptionist.
- **In the online store:** It protects a shopper's HTTPS connection to the store's load balancer.

### Terminate the session (TLS termination)
- **What it is:** The load balancer decrypts the client's HTTPS connection and ends that secure session. It can then send a separate request to the backend, using HTTP or another configured protocol.
- **Analogy:** A receptionist opens a sealed envelope at the front desk and routes the contents to the right department.
- **In the online store:** The load balancer handles the browser's secure connection before sending the request to the store's backend.

### HTTPS and HTTP(S)
- **What they are:** HTTP is the common protocol for web requests. HTTPS is HTTP protected with TLS. “HTTP(S)” means the load balancer supports web traffic using either protocol.
- **Analogy:** HTTP is an ordinary note; HTTPS is the same note sealed for the trip.
- **In the online store:** The storefront uses HTTPS so customer traffic is encrypted in transit.

### Public web application
- **What it is:** A website or web service that people can reach over the internet.
- **Analogy:** A shop with a front door open to customers.
- **In the online store:** The product catalog, cart, and checkout pages are public web features.

### TCP
- **What it is:** A basic network protocol that establishes connections between machines. It does not understand web page paths or other web request details.
- **Analogy:** A phone line that carries a conversation but does not know which office department should handle it.
- **In the online store:** TCP carries web connections, but an HTTP(S) load balancer can also understand web requests.

### Proxy load balancer
- **What it is:** A load balancer that accepts a client's connection and opens a separate connection to the backend. The backend sees the proxy as its network peer unless client details are forwarded separately.
- **Analogy:** A receptionist who receives a call, then calls the correct staff member on a separate line.
- **In the online store:** The external HTTP(S) load balancer acts as a proxy between the shopper's browser and the store's server group.

### Internal and external load balancer
- **What they are:** An external load balancer accepts traffic from the internet. An internal load balancer is for clients within a private Google Cloud network or connected network.
- **Analogy:** An external entrance is for customers; an internal doorway is for staff inside the office.
- **In the online store:** The public storefront uses external access; an internal-only admin tool might use internal access.

### How the pieces fit together

```text
Shopper's browser
   │ HTTPS (encrypted client session)
   ▼
External HTTP(S) load balancer
   │ terminates client TLS, routes web requests
   ▼
Instance group (web application servers)
```

## 3. 🌍 Real-World Scenario

A company hosts its public website on multiple virtual machines. During busy periods, a load balancer spreads traffic across those machines. The company configures HTTPS on the load balancer so it can handle secure browser connections and forward requests to the web servers.

## 4. 🔍 Option-by-Option Breakdown

### ✅ A — Correct

> **A.** Configure an HTTP(S) load balancer.

An external HTTP(S) load balancer is built for public web traffic. It can terminate the client TLS session and distribute HTTP(S) requests across an instance group. The backend connection can use HTTP or be configured for HTTPS when encryption to the backend is required.

📌 When to use it: Use it when people outside the office need secure access to a website.  
🏢 Office example: The receptionist welcomes customers at the front entrance and directs them to available staff.

### ❌ B

> **B.** Configure an internal TCP load balancer.

An internal TCP load balancer is for traffic within a private network, not a public website for internet users. It also does not match the web application use case as directly as an HTTP(S) load balancer.

📌 When to use it: Use it when staff inside the office need to reach a shared service.  
🏢 Office example: Direct calls between departments through the company's internal phone system.

### ❌ C

> **C.** Configure an external SSL proxy load balancer.

An external SSL proxy load balancer can terminate SSL/TLS for external encrypted traffic, but it is a network (TCP/SSL) proxy choice for traffic that does not need HTTP-aware application features. For a public web application serving HTTPS, Google recommends an Application Load Balancer, represented here by HTTP(S).

📌 When to use it: Use it when outside callers need a secure connection to a service that does not handle website requests.  
🏢 Office example: The receptionist securely connects callers to a specialist phone service, without sorting website pages.

### ❌ D

> **D.** Configure an external TCP proxy load balancer.

An external TCP proxy load balancer handles external TCP connections. This option does not provide the HTTP-aware application load balancing intended for the public HTTPS web application described here. The SSL proxy option is the TCP proxy choice when SSL offload is specifically needed, but A is the recommended fit for web traffic.

📌 When to use it: Use it when outside callers need a service that communicates through a basic connection.  
🏢 Office example: Route incoming calls from customers to the available phone desk.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow serves its React storefront and checkout API from a group of web servers. A shopper's browser connects over HTTPS to an external HTTP(S) load balancer. The load balancer handles the secure browser session, then routes requests to healthy servers in the instance group. If ShopNow requires encrypted traffic between the load balancer and those servers too, it can configure HTTPS to the backends.

## 6. 🧠 Key Takeaway / Memory Tip

For a public website using HTTP or HTTPS, choose an **external HTTP(S) / Application Load Balancer**. Think: **web request → HTTP(S) load balancer; internal TCP → private network service; TLS termination → secure client session ends at the proxy.**

**Current documentation:** [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer), and [HTTPS load balancer setup](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).

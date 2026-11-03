# Q043: Matching a Managed Instance Group Health-Check Delay to Startup Time

**Topic:** Compute Engine (managed instance groups, autoscaling, health checks, VM startup)

## ❓ Question
> You are running an application on multiple virtual machines within a managed instance group and have autoscaling enabled. The autoscaling policy is configured so that additional instances are added to the group if the CPU utilization of instances goes above 80%. VMs are added until the instance group reaches its maximum limit of five VMs or until CPU utilization of instances lowers to 80%. The initial delay for HTTP health checks against the instances is set to 30 seconds. The virtual machine instances take around three minutes to become available for users. You observe that when the instance group autoscales, it adds more instances then necessary to support the levels of end-user traffic. You want to properly maintain instance group sizes when autoscaling. What should you do?
>
> **A.** Set the maximum number of instances to 1.
>
> **B.** Decrease the maximum number of instances to 3.
>
> **C.** Use a TCP health check instead of an HTTP health check.
>
> **D.** Increase the initial delay of the HTTP health check to 200 seconds.

**My answer:** C
**Correct answer:** D — Increase the initial delay of the HTTP health check to 200 seconds.
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **C** is incorrect, but the mix-up makes sense: both HTTP and TCP can be used for health checks. The issue in this question is not which protocol the check uses; the 30-second startup grace period is much shorter than the roughly three minutes the VM needs before it can serve users.

**Correct answer: D — Increase the initial delay of the HTTP health check to 200 seconds.** That gives a new VM roughly 3 minutes 20 seconds to start, so the managed instance group can ignore failed startup probes instead of treating a still-starting VM as broken and recreating it. The extra 20 seconds provides a small margin.

**Current configuration note:** Compute Engine has two related but separate timing settings: the autohealing health-check initial delay, and the autoscaler's initialization period for CPU decisions. The screenshot explicitly calls out the health-check initial delay, so D is the intended answer. In a real setup, also set the autoscaler's initialization period to match measured application startup time if startup CPU data is distorting scale-out decisions.

## 2. 📖 What the Question Is Asking

In simple terms: the group starts new VMs when CPU goes above 80%, but new VMs need about three minutes before people can use them. The health-check delay is only 30 seconds. How should you give starting VMs enough time before judging them?

- **“30 seconds” vs “three minutes”** is the main clue: the grace period is far shorter than startup time.
- **“adds more instances than necessary”** suggests the group may be repeatedly reacting while new VMs are still starting or being declared unhealthy too soon.
- **“initial delay”** points to allowing a new VM time to initialize before acting on failed health checks.
- **Exam topic:** Compute Engine managed instance group autoscaling and autohealing.

## 2.5 📚 Key Terms Explained

### Virtual machine (VM) / instance
- **What it is:** A software-based computer running in Google Cloud. “Instance” is another name for a VM in this question.
- **Analogy:** One employee's work computer.
- **In the online store:** A VM can run one copy of the store's web or API application.

### Managed instance group (MIG)
- **What it is:** A group of similar VMs that Compute Engine manages from a shared template. It can create or remove VMs as instructed.
- **Analogy:** A pool of identical workstations that facilities can add or remove as staffing changes.
- **In the online store:** The MIG can run several copies of the online store's web application.

### Autoscaling
- **What it is:** Automatically changing the number of VMs in a managed instance group based on a signal such as CPU use.
- **Analogy:** Bringing in extra staff when the office gets busy and sending some home when work slows.
- **In the online store:** Autoscaling can add web-server VMs during a shopping rush.

### CPU utilization and the 80% target
- **What it is:** CPU utilization indicates how busy a VM's processor is. An 80% target tells the autoscaler the desired average level, not a hard cap on every VM.
- **Analogy:** How busy a worker's desk is; 80% means the team is nearing its planned workload.
- **In the online store:** High CPU on the store's web servers can prompt the MIG to add capacity.

### HTTP
- **What it is:** A protocol used by web browsers and web applications to exchange requests and responses.
- **Analogy:** A complete customer request form that a service desk can read.
- **In the online store:** The storefront uses HTTP messages, typically protected by HTTPS, to request pages and API actions.

### TCP
- **What it is:** A basic connection protocol that can show whether a network port accepts a connection, without checking whether the web application returns a useful response.
- **Analogy:** Checking whether a phone line rings, without checking whether the right employee answers.
- **In the online store:** A TCP check might confirm a server port is open, while an HTTP check can test whether the web service responds at a URL.

### Health check
- **What it is:** A repeated probe used to see whether an application or VM is responding. HTTP checks test an HTTP endpoint; TCP checks test whether a connection can be made to a port.
- **Analogy:** A receptionist calling a workstation to check whether the employee is ready.
- **In the online store:** A health check can test whether a web server is ready to handle shoppers.

### Initial delay
- **What it is:** The grace period for a newly created VM to start up. For a MIG autohealing health check, unsuccessful checks are ignored during this period because the VM may still be initializing.
- **Analogy:** Giving a new employee time to set up their desk before judging whether they can take calls.
- **In the online store:** It gives a web-server VM time to install or start the app before failing health probes count against it.

### VM startup / initialization
- **What it is:** The time from creating a VM until its application is ready to serve users and provide representative usage data.
- **Analogy:** The time to turn on a computer, sign in, and open the work tools.
- **In the online store:** The three-minute start includes booting the VM and getting the web app ready.

### End-user traffic
- **What it is:** Requests made by real people using the application.
- **Analogy:** Customers arriving at a shop and asking for help.
- **In the online store:** Shoppers loading product pages, adding items to a cart, and checking out.

### Maximum instance limit
- **What it is:** The largest number of VMs the autoscaler is allowed to create in the group.
- **Analogy:** The maximum number of desks available in an office.
- **In the online store:** The maximum number of web-server VMs the store is allowed to run.

### How the pieces fit together

```text
CPU rises above target
        │
        ▼
Autoscaler creates a VM
        │
        ├── VM and application take about 180 seconds to start
        └── Health-check initial delay is only 30 seconds → too short
                         │
                         ▼
Increase delay to 200 seconds (3m 20s) to cover startup plus a margin
```

## 3. 🌍 Real-World Scenario

An online retailer sees more shoppers, so the autoscaler adds web-server VMs. Each new VM takes three minutes to boot and start the application. If a health check starts judging it after only 30 seconds, the new server can fail probes before it is ready. Giving it a 200-second initial delay lets it finish starting before failed checks can trigger premature repair.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A

> **A.** Set the maximum number of instances to 1.

This would prevent the group from growing beyond one VM, but it does not fix the too-short startup delay. It also prevents the group from adding the capacity needed during busy periods and removes much of the benefit of autoscaling. One VM could become overloaded or be a single point of failure.

📌 When to use it: Use it when the application must stay on exactly one work computer.  
🏢 Office example: Keep one dedicated desk for a job that must always be handled by one assigned clerk.

### ❌ B

> **B.** Decrease the maximum number of instances to 3.

Lowering the maximum only caps the group at three VMs. It does not make newly created VMs ready sooner or correct premature health-check failures. If traffic genuinely requires four or five VMs, the lower cap can leave users waiting while the servers are overloaded.

📌 When to use it: Use it when the office has a firm limit of three workstations.  
🏢 Office example: A small branch has room and budget for only three service desks.

### ❌ C — Your answer

> **C.** Use a TCP health check instead of an HTTP health check.

Changing the probe protocol does not increase the startup grace period. A TCP check only confirms that a port accepts a connection; it might pass before the application is actually ready to serve web requests. An HTTP check can test a web endpoint, so it can provide a more meaningful signal for this HTTP application. The mismatch to fix is 30 seconds versus approximately 180 seconds of startup time, which is why the delay should be increased.

📌 When to use it: Use it when you only need to know whether a service's connection point is open.  
🏢 Office example: Check whether the office phone line is connected, without testing whether the right person can answer the request.

### ✅ D — Correct

> **D.** Increase the initial delay of the HTTP health check to 200 seconds.

A new VM takes around 180 seconds to become usable, but its current delay is only 30 seconds. During the autohealing initial delay, the MIG ignores unsuccessful health checks because the VM may still be starting. Setting the delay to 200 seconds gives it 20 seconds beyond the stated startup time. If the HTTP health check succeeds sooner, the VM is recognized as ready earlier; the full delay is not necessarily imposed when the check passes.

This prevents a new VM from being treated as unhealthy merely because its application is still starting. It can reduce unnecessary recreation and churn, helping the group settle at a size that matches actual traffic rather than repeatedly reacting to unready instances.

📌 When to use it: Use it when a new work computer needs time to start its tools before it can take assignments.  
🏢 Office example: Give a new clerk time to log in and open the records system before judging whether they can serve visitors.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow's storefront runs on VMs in a managed instance group. When CPU utilization exceeds the 80% target, the autoscaler adds another VM. Starting the storefront takes about three minutes, so a 30-second health-check delay is too short. Increasing it to 200 seconds lets the new VM start before failed HTTP checks can trigger premature repair. In an actual configuration, the team should also measure startup time and set the autoscaler's separate initialization period so CPU data from a starting VM does not distort scaling decisions.

## 6. 🧠 Key Takeaway / Memory Tip

When a VM takes longer to start than the health-check grace period, increase the initial delay to cover startup time plus a small margin. **30 seconds < 3 minutes → raise the delay; changing the health-check protocol does not fix the timing mismatch.**

**Current documentation:** [MIG autohealing and health-check initial delay](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), [Autoscaler initialization period](https://docs.cloud.google.com/compute/docs/autoscaler), and [Autoscaler CPU scaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu).

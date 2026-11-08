# G050: Know Within Minutes if the Public Storefront Stops Responding, Checked From Several Locations (Uptime Check + Alert)

**Topic:** Monitoring (uptime checks)
**Exam guide section:** 3.4 Monitoring and logging: Creating Cloud Monitoring alerts based on resource metrics

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your public storefront at https://shop.example.com must be checked from multiple geographic locations every minute. If the site stops responding with HTTP 200 from multiple locations, the on-call engineer must be notified. You want a managed solution. What should you do?
>
> **A.** Create a Cloud Monitoring uptime check for the URL from multiple regions, and create an alerting policy on the uptime check that notifies the on-call channel.
>
> **B.** Write a script on one VM that calls the URL every minute and sends an email if it fails.
>
> **C.** Enable VPC Flow Logs on the web servers' subnet.
>
> **D.** Create a log-based metric that counts HTTP 200 responses in the web server logs.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your public online store runs at https://shop.example.com.
- **What you must achieve:** Check every minute, from several places around the world, that the site answers with HTTP 200 ("OK"), and alert the on-call engineer if it stops.
- **The limits:** It must be a managed service, and alert only when several locations see the failure (so one bad network path doesn't wake anyone up).
- **What they're really asking:** Which Cloud Monitoring feature checks a public URL from many locations?

**Clues in the question:**
- "**checked from multiple geographic locations every minute**": **uptime checks** run from several Google locations.
- "**notified**": an **alerting policy** on the uptime check.

**Exam topic:** Monitoring (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Uptime check 🔑
- **What it is:** A Cloud Monitoring check that calls a URL, IP or service from several Google locations on a schedule and records whether it answered correctly (for example HTTP 200, with optional content match).
- **Looks like:** Uptime check `storefront`: HTTPS GET shop.example.com/ every 1 min from USA, Europe, Asia-Pacific
- **Not to be confused with:** A health check for a load balancer (which decides where to send traffic).
- **Analogy:** 🛎️ Mystery shoppers in several cities checking that your shop is open every minute.
- **In the online store:** Watches the storefront home page.

### 2. Alerting policy
- **What it is:** A rule that sends notifications when a condition is met, for example when the uptime check fails from 2 or more locations.
- **Looks like:** Condition: check failing in ≥ 2 regions for 1 min → PagerDuty
- **Not to be confused with:** A dashboard.
- **Analogy:** 🚨 The alarm that calls the manager.
- **In the online store:** Pages on-call.

### 🔗 How they fit together
```
 Google locations (US, EU, APAC) ─every 1 min─► https://shop.example.com
       fail in ≥2 regions ─► alerting policy ─► on-call ✅
```

---

## 🌍 Real-World Scenario

One Friday the storefront went down and nobody noticed for 40 minutes. Now an **uptime check** from three continents with an **alerting policy** pages on-call within two minutes of a real outage.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a Cloud Monitoring uptime check for the URL from multiple regions, and create an alerting policy on the uptime check that notifies the on-call channel.

**Why it's correct:**
- ✔️ "**uptime check for the URL from multiple regions**" matches "**checked from multiple geographic locations every minute**".
- ✔️ "**alerting policy on the uptime check that notifies the on-call channel**" matches "**on-call engineer must be notified**".
- ✔️ It's a built-in Cloud Monitoring feature, matching "**managed solution**".

📌 **When to use it:** Use it when you want to know quickly if your public website stops answering.
🏢 **Office example:** Mystery shoppers in several cities who call the manager if the shop doesn't open.

### ❌ B
> **B.** Write a script on one VM that calls the URL every minute and sends an email if it fails.

**Wrong words:**
- ❌ "**script on one VM**": one location (not "multiple"), and it isn't managed. If the VM dies, monitoring dies with it.

📌 **When to use it:** Avoid it. Use built-in uptime checks.
🏢 **Office example:** One person peeking through the window from across the street.

### ❌ C
> **C.** Enable VPC Flow Logs on the web servers' subnet.

**Wrong words:**
- ❌ "**VPC Flow Logs**": record network flows. They don't test whether the site answers correctly.

📌 **When to use it:** Use flow logs for traffic analysis.
🏢 **Office example:** Counting cars in the car park instead of trying the shop door.

### ❌ D
> **D.** Create a log-based metric that counts HTTP 200 responses in the web server logs.

**Wrong words:**
- ❌ "**counts HTTP 200 responses in the web server logs**": if the site is down, there are no logs, and it doesn't check from outside locations.

📌 **When to use it:** Use log-based metrics to count events that appear in logs.
🏢 **Office example:** Counting receipts to tell if the shop is open.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: uptime check `storefront-home` (HTTPS, 60s, content match "Add to cart") + alerting policy "fails in ≥2 regions" → PagerDuty + #oncall.

---

## 🧠 Key Takeaways / Memory Tips

- **Is my public URL up, from many places? → uptime check + alerting policy.**
  🧠 *"**Uptime check = mystery shoppers worldwide.**"*
- Related: **Q123**, **Q239**, **G025**.

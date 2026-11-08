# G025: Get Notified Automatically When a Google Cloud Incident Affects Your Projects (Personalized Service Health)

**Topic:** Monitoring (Personalized Service Health)
**Exam guide section:** 3.4 Monitoring and logging: Viewing the Personalized Service Health dashboard

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Last month, a Google Cloud incident affected Cloud SQL in the region your application uses, and your team learned about it only from customer complaints. You want to be notified automatically about Google Cloud incidents that affect the services and locations your projects use. What should you do?
>
> **A.** Check the public Google Cloud status page every morning.
>
> **B.** Create an uptime check that monitors google.com.
>
> **C.** Open a support case every week to ask whether any incidents occurred.
>
> **D.** Use Personalized Service Health and configure an alerting policy for service health events that are relevant to your projects.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Google had a problem (an incident) with Cloud SQL in your region, and your team only found out when customers complained.
- **What you must achieve:** Get notified automatically when Google Cloud incidents affect the services and regions your projects actually use.
- **The limits:** It must be automatic and only about incidents that matter to your projects.
- **What they're really asking:** Which Google Cloud feature tells you about incidents that affect you, and can alert you?

**Clues in the question:**
- "**incidents that affect the services and locations your projects use**": **Personalized** Service Health, filtered to your projects.
- "**notified automatically**": configure an **alerting policy** on service health events.

**Exam topic:** Monitoring (exam guide section 3.4).

---

## 📚 Key Terms Explained

### 1. Personalized Service Health 🔑
- **What it is:** A Google Cloud dashboard and API that shows Google Cloud incidents relevant to **your** projects (by product and location). It can send alerts through Cloud Monitoring alerting policies, and the events can also go to logs.
- **Looks like:** Console → Personalized Service Health → "Cloud SQL – us-east1 – degraded performance – affects project shop-prod"
- **Not to be confused with:** The public Google Cloud status page, which lists all incidents for everyone and has no alerts set up for your projects.
- **Analogy:** 📣 A building manager who texts your office when your floor's power is affected.
- **In the online store:** Alerts #oncall when Cloud SQL in us-east1 is degraded.

### 2. Alerting policy
- **What it is:** A Cloud Monitoring rule that sends a notification when a condition is met.
- **Looks like:** Policy "Google incident affects shop-prod" → email + Slack
- **Not to be confused with:** A dashboard you have to check yourself.
- **Analogy:** 🚨 An automatic alarm.
- **In the online store:** Pages on-call.

### 🔗 How they fit together
```
 Google incident (Cloud SQL us-east1) ─► Personalized Service Health (filtered to your projects)
                                        └─► alerting policy ─► Slack / email ✅
```

---

## 🌍 Real-World Scenario

After learning about an outage from angry customers, an online store turns on **Personalized Service Health** alerts. Next time, on-call gets a message within minutes saying the Google incident affects `shop-prod`, and they post a status banner before support tickets pile up.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Check the public Google Cloud status page every morning.

**Wrong words:**
- ❌ "**Check the public … status page every morning**": manual, once a day, and not filtered to your projects.

📌 **When to use it:** Use it to read general Google Cloud status when you're curious.
🏢 **Office example:** Reading the city's public notice board each morning.

### ❌ B
> **B.** Create an uptime check that monitors google.com.

**Wrong words:**
- ❌ "**uptime check that monitors google.com**": google.com being up says nothing about Cloud SQL in your region.

📌 **When to use it:** Use uptime checks on your own endpoints.
🏢 **Office example:** Checking the mall entrance to learn if your shop's power is out.

### ❌ C
> **C.** Open a support case every week to ask whether any incidents occurred.

**Wrong words:**
- ❌ "**Open a support case every week**": slow, manual, and after the fact.

📌 **When to use it:** Use support cases for help with a specific problem.
🏢 **Office example:** Calling the landlord weekly to ask if anything broke.

### ✅ D
> **D.** Use Personalized Service Health and configure an alerting policy for service health events that are relevant to your projects.

**Why it's correct:**
- ✔️ "**Personalized Service Health**" matches "**incidents that affect the services and locations your projects use**".
- ✔️ "**configure an alerting policy for service health events**" matches "**notified automatically**".

📌 **When to use it:** Use it when you want to hear right away when the provider's problems affect your own systems.
🏢 **Office example:** The building manager texts your office when an outage hits your floor.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow**: alerting policy "PSH: incidents on shop-prod" → #oncall-shop + email. The status page banner is updated by the on-call engineer.

---

## 🧠 Key Takeaways / Memory Tips

- **Google Cloud incidents affecting *your* projects + automatic alerts → Personalized Service Health (+ alerting policy).**
  🧠 *"**Personalized = about you.**"*
- Related: **G022** (Cloud Hub).

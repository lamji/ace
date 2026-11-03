# Q293: Lowest Latency for Production, Lower Cost for Development (Premium Tier for Prod, Standard Tier for Dev)

**Topic:** Networking (network service tiers)

## ❓ Question
> You work for a financial services company that operates as a stock market broker. Your company is planning to migrate to Google Cloud. You need to plan the network design in Google Cloud. Your design must: • Minimize the latency between all production systems. • Minimize costs related to your development environment. What should you do?
>
> **A.** Create a VPC in the Standard Tier and one in the Premium Tier. Deploy production workloads in the Standard Tier and development workloads in the Premium Tier.
>
> **B.** Create a VPC in the Standard Tier and one in the Premium Tier. Deploy development workloads in the Standard Tier and production workloads in the Premium Tier.
>
> **C.** Create a VPC in the Premium Tier, and deploy both production and development workloads on this VPC.
>
> **D.** Create a VPC in the Standard Tier, and deploy both production and development workloads on this VPC.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Prod: **fastest** network. Dev: **cheapest**.

**Clues in the question:**
- **Premium Tier** = Google's global backbone, lowest latency → **production**.
- **Standard Tier** = public internet routing, cheaper → **development**.

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. Network Service Tiers 🔑
- **What it is:** **Premium** (default): traffic rides Google's private backbone end to end. **Standard**: traffic uses the public internet for longer; cheaper, regional only.
- **Looks like:** `gcloud compute addresses create dev-ip --network-tier=STANDARD --region=us-central1`
- **Not to be confused with:** —
- **Analogy:** 🛣️ Private toll highway vs public roads.
- **In the online store:** Prod LB on Premium.

### 🔗 How they fit together
```
 production → Premium Tier (lowest latency) ✅
 development → Standard Tier (lower cost) ✅
```

---

## 🌍 Real-World Scenario

A broker runs trading systems on **Premium Tier** for low latency, and dev on **Standard Tier** to save money.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a VPC in the Standard Tier and one in the Premium Tier. Deploy production workloads in the Standard Tier and development workloads in the Premium Tier.

**Wrong words:**
- ❌ Backwards: "**production workloads in the Standard Tier**" and "**development … in the Premium Tier**".

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Sending traders on public roads and interns on the private highway.

### ✅ B
> **B.** Create a VPC in the Standard Tier and one in the Premium Tier. Deploy development workloads in the Standard Tier and production workloads in the Premium Tier.

**Why it's correct:**
- ✔️ "**development workloads in the Standard Tier**" matches "**Minimize costs related to your development environment**".
- ✔️ "**production workloads in the Premium Tier**" matches "**Minimize the latency between all production systems**".

📌 **When to use it:** Use it when the important work needs the fastest route and test work just needs to be cheap.
🏢 **Office example:** Traders take the private express road; the training team takes public roads.

### ❌ C
> **C.** Create a VPC in the Premium Tier, and deploy both production and development workloads on this VPC.

**Wrong words:**
- ✔️ Prod on Premium is right.
- ❌ Dev on **Premium** doesn't minimize dev costs.

📌 **When to use it:** Use all Premium when cost doesn't matter.
🏢 **Office example:** Everyone on the toll highway.

### ❌ D
> **D.** Create a VPC in the Standard Tier, and deploy both production and development workloads on this VPC.

**Wrong words:**
- ❌ Prod on **Standard**: higher latency.

📌 **When to use it:** Use all Standard for cost-sensitive, latency-tolerant apps.
🏢 **Office example:** Everyone on public roads, including traders.

---

## 🛒 E-Commerce Full-Stack Example

Prod HTTPS LB IP (Premium); dev test IPs `--network-tier=STANDARD`.

---

## 🧠 Key Takeaways / Memory Tips

- **Latency-critical → Premium Tier. Save money → Standard Tier.**
  🧠 *"**Premium for prod, Standard for savings.**"*
- Related: **Q195**.

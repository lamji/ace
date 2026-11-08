# G029: Allow VMs Outbound Access Only to a Payment Provider's Domain Name (Cloud NGFW FQDN Egress Rule)

**Topic:** VPC firewall (Cloud NGFW FQDN objects)
**Exam guide section:** 2.3 Networking: Creating and applying VPC firewall rules and Cloud NGFW policies with ingress and egress rules

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your payment VMs must be able to send HTTPS requests only to api.payments-provider.com. The provider's IP addresses change frequently and are not published. All other outbound internet traffic from these VMs must be blocked. What should you do?
>
> **A.** Create a Cloud NGFW network firewall policy with an egress rule that allows TCP 443 to the FQDN api.payments-provider.com, plus a lower-priority egress rule that denies all other traffic.
>
> **B.** Create a VPC firewall egress rule that allows TCP 443 to the provider's current IP addresses, and update it by hand when they change.
>
> **C.** Allow all egress traffic, and ask developers to call only the provider's API.
>
> **D.** Create a Cloud DNS private zone for api.payments-provider.com.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Some VMs handle payments and must call one outside service: `api.payments-provider.com` over HTTPS (port 443).
- **What you must achieve:** Allow only that one destination and block every other outbound internet connection.
- **The limits:** The provider's IP addresses change often and aren't published, so you can't list them.
- **What they're really asking:** How can a firewall rule allow traffic by domain name instead of by IP address?

**Clues in the question:**
- "**IP addresses change frequently and are not published**": IP-based rules break. You need **domain-name (FQDN)** rules.
- "**only to api.payments-provider.com**" + "**all other … blocked**": allow the FQDN, then a lower-priority deny-all egress rule.
- FQDN objects are a **Cloud NGFW** (network firewall policy) feature.

**Exam topic:** Networking (exam guide sections 2.3 and 3.3).

---

## 📚 Key Terms Explained

### 1. FQDN
- **What it is:** Fully qualified domain name: the full name of a host.
- **Looks like:** `api.payments-provider.com`
- **Not to be confused with:** An IP address like `203.0.113.7`.
- **Analogy:** 🏷️ A company's name instead of its changing street address.
- **In the online store:** The payment provider's API.

### 2. Cloud NGFW FQDN object 🔑
- **What it is:** In a network firewall policy rule, you can use domain names as the destination of egress rules. Cloud NGFW resolves the name and keeps the IP addresses up to date. This is a Cloud NGFW Standard feature, alongside geolocation and threat-intelligence objects.
- **Looks like:** Rule 100: egress allow tcp:443 dest-fqdns `api.payments-provider.com`, target tag `pay`; rule 65000: egress deny all, target tag `pay`
- **Not to be confused with:** VPC firewall rules, which take IP ranges only.
- **Analogy:** 📇 A guard list that says "anyone from Acme Payments" instead of a list of license plates.
- **In the online store:** Only checkout VMs reach the provider.

### 🔗 How they fit together
```
 pay VMs ─tcp:443─► api.payments-provider.com ✅ (FQDN allow, prio 100)
 pay VMs ─anything else─► ✋ (deny all egress, prio 65000)
```

---

## 🌍 Real-World Scenario

A card-processing provider rotates its IPs behind a CDN. The team writes a **Cloud NGFW** egress rule using the provider's **FQDN**, plus a deny-all. Payments keep working when the IPs change, and nothing else can leave those VMs.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a Cloud NGFW network firewall policy with an egress rule that allows TCP 443 to the FQDN api.payments-provider.com, plus a lower-priority egress rule that denies all other traffic.

**Why it's correct:**
- ✔️ "**egress rule that allows TCP 443 to the FQDN api.payments-provider.com**" matches "**only to api.payments-provider.com**" and "**IP addresses change frequently**".
- ✔️ "**lower-priority egress rule that denies all other traffic**" matches "**All other outbound internet traffic … must be blocked**".
- ✔️ "**Cloud NGFW network firewall policy**" is where FQDN objects are supported.

📌 **When to use it:** Use it when you must allow outbound access to a named website whose addresses keep changing.
🏢 **Office example:** Telling the guard "only let them visit Acme Payments", whatever building Acme moves to.

### ❌ B
> **B.** Create a VPC firewall egress rule that allows TCP 443 to the provider's current IP addresses, and update it by hand when they change.

**Wrong words:**
- ✔️ Egress allow on TCP 443 is the right shape.
- ❌ "**current IP addresses … update it by hand**": the IPs change often and aren't published, so the rule will break.

📌 **When to use it:** Use IP-based rules when destinations have fixed, known addresses.
🏢 **Office example:** A guard list of license plates for a company that changes cars daily.

### ❌ C
> **C.** Allow all egress traffic, and ask developers to call only the provider's API.

**Wrong words:**
- ❌ "**Allow all egress … ask developers**": nothing is enforced, which breaks "**must be blocked**".

📌 **When to use it:** Never rely on asking people for a security rule. Enforce it.
🏢 **Office example:** Leaving every exit open and asking staff to behave.

### ❌ D
> **D.** Create a Cloud DNS private zone for api.payments-provider.com.

**Wrong words:**
- ❌ "**Cloud DNS private zone**": controls name lookups inside your VPC. It doesn't allow or block traffic, and overriding the provider's name would break it.

📌 **When to use it:** Use private zones for your own internal names.
🏢 **Office example:** Changing the phone book doesn't lock any doors.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** `pay` VMs: policy `shop-fw` rule 100 allows tcp:443 to FQDN `api.payments-provider.com`; rule 65000 denies all egress for target tag `pay`.

---

## 🧠 Key Takeaways / Memory Tips

- **Allow egress by domain name (IPs change) → Cloud NGFW FQDN objects in a network firewall policy.**
  🧠 *"**Names, not numbers: FQDN rule.**"*
- Related: **G002**, **G030**, **Q151**.

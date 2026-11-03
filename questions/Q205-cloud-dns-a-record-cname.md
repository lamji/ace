# Q205: Point mydomain.com, www and home to the Load Balancer (One A Record + Two CNAMEs)

**Topic:** Networking (Cloud DNS record types)

## ❓ Question
> You are configuring Cloud DNS. You want to create DNS records to point home.mydomain.com, mydomain.com, and www.mydomain.com to the IP address of your Google Cloud load balancer. What should you do?
>
> **A.** Create one CNAME record to point mydomain.com to the load balancer, and create two A records to point WWW and HOME to mydomain.com respectively.
>
> **B.** Create one CNAME record to point mydomain.com to the load balancer, and create two AAAA records to point WWW and HOME to mydomain.com respectively.
>
> **C.** Create one A record to point mydomain.com to the load balancer, and create two CNAME records to point WWW and HOME to mydomain.com respectively.
>
> **D.** Create one A record to point mydomain.com to the load balancer, and create two NS records to point WWW and HOME to mydomain.com respectively.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Three names, one **IP address**. Which record types?

**Clues in the question:**
- Name → **IP** = **A** record (so `mydomain.com A 34.x.x.x`).
- Name → **another name** = **CNAME** (`www` and `home` → `mydomain.com`).
- A CNAME can't be at the zone apex (`mydomain.com`).

**Exam topic:** Networking.

---

## 📚 Key Terms Explained

### 1. A record 🔑
- **What it is:** Maps a name to an **IPv4 address**.
- **Looks like:** `mydomain.com. A 34.120.1.1`
- **Not to be confused with:** AAAA (IPv6).
- **Analogy:** 📇 Name → phone number.
- **In the online store:** shopnow.com → LB IP.

### 2. CNAME record 🔑
- **What it is:** Makes a name an **alias of another name**.
- **Looks like:** `www.mydomain.com. CNAME mydomain.com.`
- **Not to be confused with:** A record.
- **Analogy:** 📇 "For Sales, see Front Desk."
- **In the online store:** www → apex.

### 3. AAAA / NS
- **What it is:** **AAAA** = name → IPv6 address. **NS** = which name servers are in charge of a zone.
- **Looks like:** `AAAA 2600:…` / `NS ns-cloud-a1.googledomains.com.`
- **Not to be confused with:** —
- **Analogy:** —
- **In the online store:** —

### 🔗 How they fit together
```
 mydomain.com       A     34.120.1.1  (LB) ✅
 www.mydomain.com   CNAME mydomain.com ✅
 home.mydomain.com  CNAME mydomain.com ✅
```

---

## 🌍 Real-World Scenario

A company points its main domain at the load balancer IP with an **A record**, and makes `www` and `home` **CNAME aliases**, so changing the IP later means editing one record.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create one CNAME record to point mydomain.com to the load balancer, and create two A records to point WWW and HOME to mydomain.com respectively.

**Wrong words:**
- ❌ "**CNAME record to point mydomain.com to the load balancer**": a CNAME points to a name, not an IP, and can't be at the apex.
- ❌ "**two A records to point WWW and HOME to mydomain.com**": A records point to IPs, not names.

📌 **When to use it:** Use CNAMEs for aliases and A records for IPs — the reverse of this.
🏢 **Office example:** Writing a person's name in the phone-number column.

### ❌ B
> **B.** Create one CNAME record to point mydomain.com to the load balancer, and create two AAAA records to point WWW and HOME to mydomain.com respectively.

**Wrong words:**
- ❌ "**CNAME … to the load balancer**" (same problem).
- ❌ "**AAAA records**": those hold IPv6 addresses, not names.

📌 **When to use it:** Use AAAA when you have an IPv6 address.
🏢 **Office example:** An overseas number format for an internal alias.

### ✅ C
> **C.** Create one A record to point mydomain.com to the load balancer, and create two CNAME records to point WWW and HOME to mydomain.com respectively.

**Why it's correct:**
- ✔️ "**one A record to point mydomain.com to the load balancer**" matches "**to the IP address of your Google Cloud load balancer**".
- ✔️ "**two CNAME records to point WWW and HOME to mydomain.com**" matches "**home.mydomain.com … and www.mydomain.com**": aliases of the main name.

📌 **When to use it:** Use it when several names should all reach the same place, with one main entry holding the real number.
🏢 **Office example:** One directory entry with the real phone number, and two "see the main entry" notes for the other names.

### ❌ D
> **D.** Create one A record to point mydomain.com to the load balancer, and create two NS records to point WWW and HOME to mydomain.com respectively.

**Wrong words:**
- ❌ "**NS records to point WWW and HOME**": NS records hand a subdomain to other name servers. They don't make aliases.

📌 **When to use it:** Use NS records to delegate a zone.
🏢 **Office example:** Handing a section of the directory to another company.

---

## 🛒 E-Commerce Full-Stack Example

```
shopnow.com.       A     34.120.10.5
www.shopnow.com.   CNAME shopnow.com.
blog.shopnow.com.  CNAME shopnow.com.
```

---

## 🧠 Key Takeaways / Memory Tips

- **Name → IP: A. Name → name: CNAME.** AAAA = IPv6, NS = delegation.
  🧠 *"**A for Address, CNAME for Copy-a-NAME.**"*
- Related: **Q162**.

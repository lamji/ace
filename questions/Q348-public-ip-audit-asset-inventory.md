# Q348: Audit All VMs With Public IPs Across the Org, Managed and Low-Maintenance (Cloud Asset Inventory)

**Topic:** Security (Cloud Asset Inventory)

## ❓ Question
> You are conducting an audit of your Google Cloud organization. You need to identify all Compute Engine instances that have a public IP address. You want to implement a solution that is easy to maintain and uses Google Cloud managed services. What should you do?
>
> **A.** Enable the compute.vmExternalIpAccess organization policy at the organization level.
>
> **B.** Use Cloud Shell and Gemini CLI to query the Compute Engine API for instances with a public IP address.
>
> **C.** Use Cloud Asset Inventory to query for all Compute Engine instances with a public IP address.
>
> **D.** Create a shell script using the gcloud CLI to find all instances with a public IP address.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Find **all VMs with a public IP** org-wide; managed, easy to maintain.

**Clues in the question:**
- Org-wide audit + managed → **Cloud Asset Inventory** query.

**Exam topic:** Security.

---

## 📚 Key Terms Explained

### 1. Cloud Asset Inventory 🔑 (review)
- **What it is:** Managed inventory of all resources and IAM policies, searchable org-wide.
- **Looks like:** `gcloud asset search-all-resources --scope=organizations/123 --asset-types=compute.googleapis.com/Instance --query="networkInterfaces.accessConfigs.natIP:*"`
- **Not to be confused with:** org policy (blocks, doesn't list).
- **Analogy:** 🗂️ Company-wide inventory.
- **In the online store:** —

### 🔗 How they fit together
```
 Asset Inventory → instances with external IP → report ✅
```

---

## 🌍 Real-World Scenario

Security queries **Cloud Asset Inventory** for instances with external IPs.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Enable the compute.vmExternalIpAccess organization policy at the organization level.

**Wrong words:**
- ❌ "**compute.vmExternalIpAccess**": restricts future external IPs; doesn't list existing ones.

📌 **When to use it:** Use it to prevent new public IPs.
🏢 **Office example:** A rule for the future, not an audit list.

### ❌ B
> **B.** Use Cloud Shell and Gemini CLI to query the Compute Engine API for instances with a public IP address.

**Wrong words:**
- ❌ "**Gemini CLI to query the Compute Engine API**": ad hoc, per project.

📌 **When to use it:** Use it for quick personal exploration.
🏢 **Office example:** Asking around office by office.

### ✅ C
> **C.** Use Cloud Asset Inventory to query for all Compute Engine instances with a public IP address.

**Why it's correct:**
- ✔️ "**Cloud Asset Inventory to query for all Compute Engine instances with a public IP**" matches "**identify all … instances that have a public IP**" + "**easy to maintain and uses Google Cloud managed services**".

📌 **When to use it:** Use it when you need a list of certain things across every part of the company.
🏢 **Office example:** The company-wide inventory system answering 'which desks have outside phone lines?'

### ❌ D
> **D.** Create a shell script using the gcloud CLI to find all instances with a public IP address.

**Wrong words:**
- ❌ "**shell script using the gcloud CLI**": custom, loops over projects; maintenance.

📌 **When to use it:** Use scripts for small one-offs.
🏢 **Office example:** Walking every floor with a clipboard.

---

## 🛒 E-Commerce Full-Stack Example

Weekly asset query → report of VMs with external IPs.

---

## 🧠 Key Takeaways / Memory Tips

- **Org-wide resource audit → Cloud Asset Inventory.**
  🧠 *"**Audit = Asset Inventory.**"*
- Related: **Q340**, **Q363**.

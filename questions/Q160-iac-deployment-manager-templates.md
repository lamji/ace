# Q160: Standardize Infrastructure as Code With Little Repetition (Deployment Manager Templates)

**Topic:** Infrastructure as Code (Deployment Manager templates, gcloud scripts, REST)

## ❓ Question
> Your company wants to standardize the creation and management of multiple Google Cloud resources using Infrastructure as Code. You want to minimize the amount of repetitive code needed to manage the environment. What should you do?
>
> **A.** Develop templates for the environment using Cloud Deployment Manager.
>
> **B.** Use curl in a terminal to send a REST request to the relevant Google API for each individual resource.
>
> **C.** Use the Cloud Console interface to provision and manage all related resources.
>
> **D.** Create a bash script that contains all requirement steps as gcloud commands.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your company wants to create and manage many Google Cloud resources using Infrastructure as Code (describing resources in code files instead of clicking).
- **What you must achieve:** Standardize how resources are created.
- **The limits:** Write as little repeated code as possible.
- **What they're really asking:** How do you structure the code so common pieces are written once and reused?

**Clues in the question:**
- "**Infrastructure as Code**" + "**minimize the amount of repetitive code**" → **templates** with parameters (Deployment Manager, or Terraform modules today).

**Exam topic:** Infrastructure as Code.

---

## 📚 Key Terms Explained

### 1. Deployment Manager template 🔑 (review from Q143)
- **What it is:** A **reusable, parameterized** description of resources (Jinja/Python). Write once, reuse with different values.
- **Looks like:** `{% for zone in properties.zones %} - name: web-{{zone}} …`
- **Not to be confused with:** a one-off script.
- **Analogy:** 📐 A **blueprint with blanks** to fill in.
- **In the online store:** One template for every ShopNow environment.

### 2. Declarative vs imperative
- **What it is:** Templates say **what you want** (declarative). Scripts say **each step to do** (imperative).
- **Looks like:** YAML/Jinja vs `gcloud … create` lines
- **Not to be confused with:** the same thing.
- **Analogy:** 📐 Blueprint vs a list of instructions for the builder.
- **In the online store:** Templates handle updates for you.

### 🔗 How they fit together
```
 template web-stack.jinja (params: env, size, zones)
   → dev (small)  → staging (medium)  → prod (large) ✅ same code, different values
```

---

## 🌍 Real-World Scenario

A company wants identical dev, staging and prod environments. They write one **Deployment Manager template** with parameters and deploy it three times with different values.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Develop templates for the environment using Cloud Deployment Manager.

**Why it's correct:**
- ✔️ "**templates … using Cloud Deployment Manager**" matches "**Infrastructure as Code**".
- ✔️ "**templates**" (reusable, parameterized) matches "**minimize the amount of repetitive code**".

📌 **When to use it:** Use it when you build the same kind of setup many times.
🏢 **Office example:** A blueprint with blanks, reused for every new office.

### ❌ B
> **B.** Use curl in a terminal to send a REST request to the relevant Google API for each individual resource.

**Wrong words:**
- ❌ "**curl … REST request … for each individual resource**": a separate request for every resource is very repetitive and not managed as code.

📌 **When to use it:** Use raw REST calls for debugging or features not in tools yet.
🏢 **Office example:** Phoning the builder for each brick.

### ❌ C
> **C.** Use the Cloud Console interface to provision and manage all related resources.

**Wrong words:**
- ❌ "**Cloud Console interface**": manual clicking, which isn't Infrastructure as Code.

📌 **When to use it:** Use the console for exploring and one-off changes.
🏢 **Office example:** Building each office by hand without blueprints.

### ❌ D
> **D.** Create a bash script that contains all requirement steps as gcloud commands.

**Wrong words:**
- ❌ "**bash script … gcloud commands**": step-by-step commands, repeated for each environment. It doesn't handle updates cleanly.

📌 **When to use it:** Use scripts for small automations.
🏢 **Office example:** A long list of builder instructions copied for every office.

---

## 🛒 E-Commerce Full-Stack Example

```yaml
# shop-env.yaml
imports: [{path: web-stack.jinja}]
resources:
- name: prod-stack
  type: web-stack.jinja
  properties: {env: prod, machineType: e2-standard-4, size: 6}
```

---

## 🧠 Key Takeaways / Memory Tips

- **IaC with less repetition → templates** (Deployment Manager / Terraform modules).
  🧠 *"**Blueprint once, build many.**"*
- Related: **Q143**, **Q069** (Deployment Manager).

# Q137: Install Jenkins as Quickly and Easily as Possible (Cloud Marketplace)

**Topic:** Cloud Marketplace, CI/CD

## ❓ Question
> You are developing a new application and are looking for a Jenkins installation to build and deploy your source code. You want to automate the installation as quickly and easily as possible. What should you do?
>
> **A.** Deploy Jenkins through the Google Cloud Marketplace.
>
> **B.** Create a new Compute Engine instance. Run the Jenkins executable.
>
> **C.** Create a new Kubernetes Engine cluster. Create a deployment for the Jenkins image.
>
> **D.** Create an instance template with the Jenkins executable. Create a managed instance group with this template.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You need **Jenkins** (a build server), installed **quickly and easily**.

**Clues in the question:**
- "**as quickly and easily as possible**" + "**automate the installation**": a **one-click** ready-made deployment → **Cloud Marketplace** (as in Q122).

**Exam topic:** Marketplace.

---

## 📚 Key Terms Explained

### 1. Cloud Marketplace (review from Q122) 🔑
- **What it is:** A catalog of **ready-to-deploy software**. A few clicks create configured VMs or GKE apps.
- **Looks like:** Console → Marketplace → "Jenkins" → Launch
- **Not to be confused with:** building it yourself.
- **Analogy:** 🏪 Ordering a pre-assembled desk.
- **In the online store:** A dev team's Jenkins in 5 minutes.

### 2. Jenkins
- **What it is:** An open-source **build and deploy server** (CI/CD): it compiles code, runs tests and deploys.
- **Looks like:** `http://jenkins-1:8080` pipeline: build → test → deploy
- **Not to be confused with:** a source code host.
- **Analogy:** 🏭 An automatic assembly line for your code.
- **In the online store:** Builds the ShopNow storefront on every commit.

### 🔗 How they fit together
```
 Marketplace → Jenkins → Deploy ✅ (VM + Jenkins pre-installed and configured)
 vs. manual VM / GKE / MIG setups ❌ (more steps)
```

---

## 🌍 Real-World Scenario

A new team needs a CI server today. Instead of installing Java and Jenkins by hand, they deploy **Jenkins from Cloud Marketplace**, open the URL, and create their first pipeline.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Deploy Jenkins through the Google Cloud Marketplace.

**Why it's correct:**
- ✔️ "**Deploy Jenkins through the Google Cloud Marketplace**" matches "**automate the installation as quickly and easily as possible**": a ready-made deployment in a few clicks.

📌 **When to use it:** Use it when you need standard software running fast.
🏢 **Office example:** Ordering a pre-assembled desk from the supply catalog.

### ❌ B
> **B.** Create a new Compute Engine instance. Run the Jenkins executable.

**Wrong words:**
- ❌ "**Create a new Compute Engine instance. Run the Jenkins executable**": manual installation (Java, service setup, firewall). Slower and not automated.

📌 **When to use it:** Use it when you need a fully custom setup.
🏢 **Office example:** Assembling the desk yourself from parts.

### ❌ C
> **C.** Create a new Kubernetes Engine cluster. Create a deployment for the Jenkins image.

**Wrong words:**
- ❌ "**Create a new Kubernetes Engine cluster … deployment**": a whole cluster plus storage and service setup. More work, not "quickly and easily".

📌 **When to use it:** Use it when you already run Jenkins at scale on Kubernetes.
🏢 **Office example:** Building a factory to make one desk.

### ❌ D
> **D.** Create an instance template with the Jenkins executable. Create a managed instance group with this template.

**Wrong words:**
- ❌ "**instance template … managed instance group**": more steps, and Jenkins isn't made to run as a group of identical stateless VMs.

📌 **When to use it:** Use MIGs for stateless, scalable apps.
🏢 **Office example:** Hiring a staffing agency for a single desk.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's platform team deploys **Jenkins from Marketplace** into `shopnow-cicd`. The storefront repo's pipeline builds the image, runs tests and deploys to GKE on every merge.

---

## 🧠 Key Takeaways / Memory Tips

- **Quick, easy, standard software → Cloud Marketplace.**
  🧠 *"**Fastest install? Marketplace.**"*
- Related: **Q122** (Cassandra from Marketplace), **Q177** (MongoDB Atlas).

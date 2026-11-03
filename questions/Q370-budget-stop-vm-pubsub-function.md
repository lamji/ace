# Q370: Automatically Stop Spending When Over Budget (Budget → Pub/Sub → Cloud Run Function That Stops the VM)

**Topic:** Billing (programmatic budget notifications)

## ❓ Question
> You are managing a new project for a web application on Google Cloud. The web application is running on a Compute Engine VM, and your team has a strict budget. You have already created a budget in Cloud Billing and set an alert rule to send an email when 90% of the budget is consumed. You must ensure that project spending automatically stops if it exceeds the budgeted amount. What should you do?
>
> **A.** Create a new Cloud Billing account, and associate the project with it to prevent new spending from affecting your project’s budget.
>
> **B.** Create a Pub/Sub topic, and connect it to the budget. Create a Cloud Run function that subscribes to the Pub/Sub topic and executes code to stop the VM.
>
> **C.** Use the Cloud Billing dashboard to identify the forecasted spend of your project, and then update the budget and alert to match the forecasted spend.
>
> **D.** Rely on the budget’s configuration to automatically disable billable resources when the spend reaches 100%.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Spending must **automatically stop** if over budget.

**Clues in the question:**
- Budgets **only notify**; they never stop spending.
- Automation → **Pub/Sub notification** + **function** that stops resources.

**Exam topic:** Billing.

---

## 📚 Key Terms Explained

### 1. Programmatic budget notifications 🔑
- **What it is:** A budget publishes JSON messages (cost vs budget) to a Pub/Sub topic; code can react.
- **Looks like:** Budget → Manage notifications → Pub/Sub topic `budget-alerts`
- **Not to be confused with:** email alerts.
- **Analogy:** 📟 An automatic signal that triggers a shutdown.
- **In the online store:** —

### 🔗 How they fit together
```
 budget → Pub/Sub → Cloud Run function → stop VM ✅
```

---

## 🌍 Real-World Scenario

When cost exceeds budget, a **function** triggered by the budget's **Pub/Sub** message stops the VM.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a new Cloud Billing account, and associate the project with it to prevent new spending from affecting your project’s budget.

**Wrong words:**
- ❌ "**new Cloud Billing account**": doesn't cap spending.

📌 **When to use it:** Use new accounts for separate invoices.
🏢 **Office example:** A new card doesn't stop shopping.

### ✅ B
> **B.** Create a Pub/Sub topic, and connect it to the budget. Create a Cloud Run function that subscribes to the Pub/Sub topic and executes code to stop the VM.

**Why it's correct:**
- ✔️ "**Pub/Sub topic … connect it to the budget**" matches "**budget in Cloud Billing**".
- ✔️ "**Cloud Run function … stop the VM**" matches "**spending automatically stops if it exceeds the budgeted amount**".

📌 **When to use it:** Use it when going over budget must switch things off without anyone stepping in.
🏢 **Office example:** A meter that automatically switches off the machine when the allowance runs out.

### ❌ C
> **C.** Use the Cloud Billing dashboard to identify the forecasted spend of your project, and then update the budget and alert to match the forecasted spend.

**Wrong words:**
- ❌ "**update the budget … forecasted spend**": raises the limit; doesn't stop spending.

📌 **When to use it:** Use forecasts for planning.
🏢 **Office example:** Moving the line instead of stopping.

### ❌ D
> **D.** Rely on the budget’s configuration to automatically disable billable resources when the spend reaches 100%.

**Wrong words:**
- ❌ "**Rely on the budget's configuration to automatically disable**": budgets don't disable resources.

📌 **When to use it:** **Never rely on this** — budgets only notify.
🏢 **Office example:** Expecting a warning bell to lock the doors.

---

## 🛒 E-Commerce Full-Stack Example

Budget `dev-project` → `budget-alerts` → function `stop-dev-vms`.

---

## 🧠 Key Takeaways / Memory Tips

- **Budgets notify only. Auto-stop → Pub/Sub + function.**
  🧠 *"**Budget rings; function acts.**"*
- Related: **Q374**, **Q316**.

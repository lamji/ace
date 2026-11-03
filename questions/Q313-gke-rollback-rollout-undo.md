# Q313: Roll Back a GKE Rolling Update (kubectl rollout undo)

**Topic:** GKE (Deployments, rollbacks)

## ❓ Question
> You recently discovered an issue with your rolling update in Google Kubernetes Engine (GKE). You now need to roll back a rolling update. What should you do?
>
> **A.** Delete the deployment.
>
> **B.** Use the kubectl rollout restart command to revert the deployment.
>
> **C.** Use the kubectl rollout undo command.
>
> **D.** Manually scale down the new Pods and scale up the old Pods.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Revert a bad rolling update.

**Clues in the question:**
- Rollback → **`kubectl rollout undo`** returns the Deployment to the previous revision.

**Exam topic:** GKE.

---

## 📚 Key Terms Explained

### 1. kubectl rollout undo 🔑
- **What it is:** Reverts a Deployment to the previous (or a chosen) revision.
- **Looks like:** `kubectl rollout undo deployment/web` or `--to-revision=3`
- **Not to be confused with:** `rollout restart` (restarts same version).
- **Analogy:** ⏪ Undo button.
- **In the online store:** ShopNow web rollback.

### 🔗 How they fit together
```
 v2 (bad) ── rollout undo ──► v1 ✅
```

---

## 🌍 Real-World Scenario

A bad release breaks checkout; the engineer runs `kubectl rollout undo deployment/checkout`.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Delete the deployment.

**Wrong words:**
- ❌ "**Delete the deployment**": causes downtime.

📌 **When to use it:** Use deletion only to retire an app.
🏢 **Office example:** Closing the store to fix a sign.

### ❌ B
> **B.** Use the kubectl rollout restart command to revert the deployment.

**Wrong words:**
- ❌ "**rollout restart**": restarts Pods on the same (bad) version.

📌 **When to use it:** Use restart to refresh Pods (e.g., reload config).
🏢 **Office example:** Restarting the broken machine.

### ✅ C
> **C.** Use the kubectl rollout undo command.

**Why it's correct:**
- ✔️ "**kubectl rollout undo**" matches "**roll back a rolling update**".

📌 **When to use it:** Use it when the new version is bad and you want the last good one back.
🏢 **Office example:** Pressing undo on the document.

### ❌ D
> **D.** Manually scale down the new Pods and scale up the old Pods.

**Wrong words:**
- ❌ "**Manually scale down … scale up**": manual and error-prone; Deployments don't keep old Pods that way.

📌 **When to use it:** **Avoid.**
🏢 **Office example:** Moving staff desk by desk by hand.

---

## 🛒 E-Commerce Full-Stack Example

`kubectl rollout history deployment/checkout` → `kubectl rollout undo deployment/checkout`.

---

## 🧠 Key Takeaways / Memory Tips

- **GKE rollback → kubectl rollout undo.**
  🧠 *"**Undo undoes; restart restarts.**"*
- Related: **Q220**.

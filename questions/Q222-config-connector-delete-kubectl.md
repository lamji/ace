# Q222: Permanently Delete a Pub/Sub Topic Managed by Config Connector (kubectl delete the Resource)

**Topic:** Config Connector (managing Google Cloud via Kubernetes)

## ❓ Question
> You want to permanently delete a Pub/Sub topic managed by Config Connector in your Google Cloud project. What should you do?
>
> **A.** Use kubectl to create the label deleted-by-cnrm and to change its value to true for the topic resource.
>
> **B.** Use kubectl to delete the topic resource.
>
> **C.** Use gcloud CLI to delete the topic.
>
> **D.** Use gcloud CLI to update the topic label managed-by-cnrm to false.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** The topic is **managed by Config Connector**. How do you delete it for good?

**Clues in the question:**
- Config Connector keeps Google Cloud matching the **Kubernetes resource**. Delete it with **`kubectl delete`**, and Config Connector deletes the topic.
- If you delete with gcloud, Config Connector **recreates** it.

**Exam topic:** Config Connector.

---

## 📚 Key Terms Explained

### 1. Config Connector 🔑
- **What it is:** A GKE add-on that lets you manage Google Cloud resources as **Kubernetes objects**. It keeps the real resource in sync with the YAML.
- **Looks like:** `kind: PubSubTopic` / `kubectl delete pubsubtopic orders`
- **Not to be confused with:** Terraform.
- **Analogy:** 🤖 A housekeeper who restores the room to match the plan every few minutes.
- **In the online store:** ShopNow topics as YAML.

### 🔗 How they fit together
```
 kubectl delete pubsubtopic orders ─► Config Connector ─► deletes topic in GCP ✅
 gcloud pubsub topics delete orders ─► Config Connector recreates it ✗
```

---

## 🌍 Real-World Scenario

A team manages Pub/Sub with Config Connector. To retire a topic, they run **`kubectl delete pubsubtopic legacy-events`**, and it's removed from Google Cloud too.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use kubectl to create the label deleted-by-cnrm and to change its value to true for the topic resource.

**Wrong words:**
- ❌ "**label deleted-by-cnrm**": no such label triggers deletion.

📌 **When to use it:** **Never use this** — it's made up.
🏢 **Office example:** Writing "please remove" on the furniture.

### ✅ B
> **B.** Use kubectl to delete the topic resource.

**Why it's correct:**
- ✔️ "**Use kubectl to delete the topic resource**" matches "**permanently delete a Pub/Sub topic managed by Config Connector**": the controller deletes the real topic and won't recreate it.

📌 **When to use it:** Use it whenever something is managed from a master plan: change the plan, not the thing.
🏢 **Office example:** Removing the item from the housekeeper's plan, so it's taken away and not put back.

### ❌ C
> **C.** Use gcloud CLI to delete the topic.

**Wrong words:**
- ❌ "**Use gcloud CLI to delete the topic**": Config Connector sees it missing and **recreates** it.

📌 **When to use it:** Use gcloud for resources not managed by Config Connector.
🏢 **Office example:** Throwing out a chair that the housekeeper puts right back.

### ❌ D
> **D.** Use gcloud CLI to update the topic label managed-by-cnrm to false.

**Wrong words:**
- ❌ "**update the topic label managed-by-cnrm to false**": doesn't delete anything.

📌 **When to use it:** **Never use this.**
🏢 **Office example:** Changing a sticker instead of removing the item.

---

## 🛒 E-Commerce Full-Stack Example

`kubectl delete pubsubtopic shop-legacy-events -n config-control`

---

## 🧠 Key Takeaways / Memory Tips

- **Config Connector resource → change/delete it with kubectl.** Direct gcloud changes get reverted.
  🧠 *"**Delete the YAML, delete the thing.**"*
- Related: **Q143**, **Q160**.

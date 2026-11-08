# Q268: Votes Arriving at Varying Rates From Many Users (Pub/Sub → Cloud Functions)

**Topic:** Serverless (Pub/Sub, Cloud Functions)

## ❓ Question
> Your team is building a website that handles votes from a large user population. The incoming votes will arrive at various rates. You want to optimize the storage and processing of the votes. What should you do?
>
> **A.** Save the incoming votes to Firestore. Use Cloud Scheduler to trigger a Cloud Functions instance to periodically process the votes.
>
> **B.** Use a dedicated instance to process the incoming votes. Send the votes directly to this instance.
>
> **C.** Save the incoming votes to a JSON file on Cloud Storage. Process the votes in a batch at the end of the day.
>
> **D.** Save the incoming votes to Pub/Sub. Use the Pub/Sub topic to trigger a Cloud Functions instance to process the votes.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Your team is building a website that receives votes from many users, arriving at changing rates.
- **What you must achieve:** Store and process the votes efficiently.
- **The limits:** Vote volume goes up and down unpredictably.
- **What they're really asking:** How should the votes be received and processed so bursts are handled smoothly?

**Clues in the question:**
- "**arrive at various rates**" → **Pub/Sub** buffers spikes.
- Process each as it arrives → **Pub/Sub-triggered Cloud Functions** that scale automatically.

**Exam topic:** Serverless.

---

## 📚 Key Terms Explained

### 1. Pub/Sub trigger 🔑
- **What it is:** A Cloud Function runs for each message published to a topic.
- **Looks like:** `gcloud functions deploy count-vote --trigger-topic=votes`
- **Not to be confused with:** Cloud Scheduler polling.
- **Analogy:** 📬 Each letter rings a bell for a clerk.
- **In the online store:** Order events.

### 🔗 How they fit together
```
 voters ─► Pub/Sub votes (buffer) ─► Cloud Function per message (auto-scales) ✅
```

---

## 🌍 Real-World Scenario

A TV show's voting site publishes each vote to **Pub/Sub**; a **Cloud Function** counts them, scaling up during the show and to zero after.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Save the incoming votes to Firestore. Use Cloud Scheduler to trigger a Cloud Functions instance to periodically process the votes.

**Wrong words:**
- ❌ "**Cloud Scheduler … periodically process**": batch delays and polling, not optimized for varying rates.

📌 **When to use it:** Use scheduled processing for daily summaries.
🏢 **Office example:** Collecting ballots once an hour.

### ❌ B
> **B.** Use a dedicated instance to process the incoming votes. Send the votes directly to this instance.

**Wrong words:**
- ❌ "**dedicated instance … Send the votes directly**": one VM can be overwhelmed or idle; no buffer.

📌 **When to use it:** Use a dedicated VM for steady, predictable loads.
🏢 **Office example:** One clerk handling every ballot during a rush.

### ❌ C
> **C.** Save the incoming votes to a JSON file on Cloud Storage. Process the votes in a batch at the end of the day.

**Wrong words:**
- ❌ "**JSON file on Cloud Storage … batch at the end of the day**": concurrent writes to one file clash; results delayed.

📌 **When to use it:** Use daily batches when delay is fine.
🏢 **Office example:** Everyone writing on one sheet of paper.

### ✅ D
> **D.** Save the incoming votes to Pub/Sub. Use the Pub/Sub topic to trigger a Cloud Functions instance to process the votes.

**Why it's correct:**
- ✔️ "**Save the incoming votes to Pub/Sub**" matches "**arrive at various rates**": it absorbs spikes.
- ✔️ "**trigger a Cloud Functions instance to process the votes**" matches "**optimize the storage and processing**": scales with load.

📌 **When to use it:** Use it when lots of small messages arrive in bursts and each needs quick handling.
🏢 **Office example:** A ballot box that rings a bell for a clerk each time a vote drops in, with more clerks during rushes.

---

## 🛒 E-Commerce Full-Stack Example

Product reviews: storefront → Pub/Sub `review-submitted` → Cloud Function `moderate-review`.

---

## 🧠 Key Takeaways / Memory Tips

- **Bursty events → Pub/Sub + triggered Cloud Functions.**
  🧠 *"**Buffer with Pub/Sub, react with Functions.**"*
- Related: **Q213**, **Q064**.

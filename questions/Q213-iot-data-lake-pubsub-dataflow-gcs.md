# Q213: Highly Available IoT Data Lake for Structured and Unstructured Data (Pub/Sub → Dataflow → Cloud Storage)

**Topic:** Data pipelines (Pub/Sub, Dataflow, Cloud Storage)

## ❓ Question
> You are building a data lake on Google Cloud for your Internet of Things (IoT) application. The IoT application has millions of sensors that are constantly streaming structured and unstructured data to your backend in the cloud. You want to build a highly available and resilient architecture based on Google-recommended practices. What should you do?
>
> **A.** Stream data to Pub/Sub, and use Dataflow to send data to Cloud Storage.
>
> **B.** Stream data to Pub/Sub, and use Storage Transfer Service to send data to BigQuery.
>
> **C.** Stream data to Dataflow, and use Dataprep by Trifacta to send data to Bigtable.
>
> **D.** Stream data to Dataflow, and use Storage Transfer Service to send data to BigQuery.

**My answer:** — (didn't know)
**Correct answer:** A
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You are building a data lake (a central store for raw data) for an IoT app with millions of sensors streaming structured and unstructured data.
- **What you must achieve:** A highly available, resilient design.
- **The limits:** Follow Google-recommended practices.
- **What they're really asking:** Which services should receive the stream and store the data?

**Clues in the question:**
- "**constantly streaming**" → ingest with **Pub/Sub** (buffer, scales, durable).
- "**data lake**" + "**structured and unstructured**" → **Cloud Storage**.
- **Dataflow** moves stream data from Pub/Sub to storage.

**Exam topic:** Data pipelines.

---

## 📚 Key Terms Explained

### 1. Pub/Sub 🔑
- **What it is:** A managed messaging service that **receives and buffers** streams of messages.
- **Looks like:** topic `sensor-events`
- **Not to be confused with:** Dataflow (processing).
- **Analogy:** 📬 A mail sorting center that never closes.
- **In the online store:** Order events.

### 2. Dataflow
- **What it is:** Managed stream/batch processing (Apache Beam).
- **Looks like:** template "Pub/Sub to Cloud Storage Text"
- **Not to be confused with:** Storage Transfer Service (bulk copy).
- **Analogy:** 🏭 A conveyor that sorts and packs.
- **In the online store:** —

### 3. Data lake
- **What it is:** A store for raw data of **any format**, usually Cloud Storage.
- **Looks like:** `gs://iot-lake/raw/2026/11/03/…`
- **Not to be confused with:** a data warehouse (structured).
- **Analogy:** 📦 A big warehouse for all kinds of boxes.
- **In the online store:** —

### 🔗 How they fit together
```
 sensors ─► Pub/Sub ─► Dataflow ─► Cloud Storage (data lake) ✅
```

---

## 🌍 Real-World Scenario

A smart-meter company streams readings and images from millions of devices into **Pub/Sub**, with **Dataflow** writing them into a **Cloud Storage** data lake.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Stream data to Pub/Sub, and use Dataflow to send data to Cloud Storage.

**Why it's correct:**
- ✔️ "**Stream data to Pub/Sub**" matches "**millions of sensors … constantly streaming**" + "**highly available and resilient**".
- ✔️ "**use Dataflow to send data to Cloud Storage**" matches "**data lake**" + "**structured and unstructured data**".

📌 **When to use it:** Use it when huge numbers of devices keep sending all sorts of data that you want to keep in one big store.
🏢 **Office example:** A sorting center that receives every parcel, and a conveyor that stacks them in the big warehouse.

### ❌ B
> **B.** Stream data to Pub/Sub, and use Storage Transfer Service to send data to BigQuery.

**Wrong words:**
- ✔️ "Pub/Sub" is right.
- ❌ "**Storage Transfer Service**": copies files in bulk; it doesn't read Pub/Sub streams.
- ❌ "**BigQuery**" isn't a lake for unstructured data.

📌 **When to use it:** Use Storage Transfer Service to move bulk files from other clouds or on-prem.
🏢 **Office example:** Sending a moving truck to collect individual letters.

### ❌ C
> **C.** Stream data to Dataflow, and use Dataprep by Trifacta to send data to Bigtable.

**Wrong words:**
- ❌ "**Stream data to Dataflow**": devices should send to Pub/Sub first.
- ❌ "**Dataprep … to Bigtable**": Dataprep is for interactive data cleaning, not streaming.

📌 **When to use it:** Use Dataprep to clean datasets visually.
🏢 **Office example:** Asking an editor to sort the mail as it arrives.

### ❌ D
> **D.** Stream data to Dataflow, and use Storage Transfer Service to send data to BigQuery.

**Wrong words:**
- ❌ "**Stream data to Dataflow**" and ❌ "**Storage Transfer Service**": wrong tools for streaming.

📌 **When to use it:** **Never use this** for streaming ingest.
🏢 **Office example:** Two wrong tools in a row.

---

## 🛒 E-Commerce Full-Stack Example

Clickstream from the storefront → Pub/Sub `clicks` → Dataflow template "Pub/Sub to Cloud Storage Text" → `gs://shopnow-lake/clicks/`.

---

## 🧠 Key Takeaways / Memory Tips

- **Streaming ingest → Pub/Sub. Process → Dataflow. Data lake → Cloud Storage.**
  🧠 *"**Pub/Sub catches, Dataflow carries, Storage keeps.**"*
- Related: **Q139**, **Q168**.

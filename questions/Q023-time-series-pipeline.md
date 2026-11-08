# Q023: Time-Series Data Pipeline (Pub/Sub → Dataflow → Bigtable + BigQuery)

**Topic:** Data pipelines (Pub/Sub ingest, Dataflow processing, Bigtable for time-series storage, BigQuery for analytics)

## ❓ Question
> You are building a pipeline to process time-series data. Which Google Cloud Platform services should you put in boxes 1,2,3, and 4?
>
> (Diagram: Constrained Devices (non-TCP, e.g. BLE) → Standard Devices (HTTPS) with a Gateway → inside Google Cloud Platform: box **1** → box **2** → which splits into **Storage** (box **3**) and **Analytics** (box **4**).)
>
> **A.** Cloud Pub/Sub, Cloud Dataflow, Cloud Datastore, BigQuery
>
> **B.** Firebase Messages, Cloud Pub/Sub, Cloud Spanner, BigQuery
>
> **C.** Cloud Pub/Sub, Cloud Storage, BigQuery, Cloud Bigtable
>
> **D.** Cloud Pub/Sub, Cloud Dataflow, Cloud Bigtable, BigQuery

**My answer:** C
**Correct answer:** D
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A diagram shows a pipeline for time-series data (readings with timestamps, like sensor values). Devices send data in, then box 1 receives it, box 2 processes it, box 3 stores it and box 4 analyzes it.
- **What you must achieve:** Put the right Google Cloud service in each box.
- **The limits:** It must handle lots of timestamped data.
- **What they're really asking:** Which Google Cloud services belong in boxes 1, 2, 3 and 4?

| Box | Job in the diagram | What it needs |
|---|---|---|
| **1** | First stop, where **messages arrive** | A service that **receives a flood of messages**: **Pub/Sub** |
| **2** | **Processes** the data, then **splits it into two paths** | A service that **cleans and transforms streams**: **Dataflow** |
| **3** | Under the **"Storage"** label | A database for **huge amounts of time-series data with fast reads**: **Bigtable** |
| **4** | Under the **"Analytics"** label | A **SQL analytics** warehouse: **BigQuery** |

| Keyword / clue | What it hints at |
|---|---|
| "**time-series data**" | Bigtable is Google's go-to for time series |
| "**pipeline to process**" | A processing step: **Dataflow** |
| Diagram label "**Storage**" over box 3 | A database goes in box 3, **not** an analytics tool |
| Diagram label "**Analytics**" over box 4 | **BigQuery** goes in box 4 |
| Devices + gateway sending messages | **Pub/Sub** first |

**Exam topic:** Data and analytics services: choosing the right service for **ingest → process → store → analyze**.

---

## 📚 Key Terms Explained

### 1️⃣ Time-Series Data
- **What it is:** Data where **every record has a time**, arriving **non-stop**: sensor readings, stock prices, website clicks, server CPU every second.
- **Analogy:** 🌡️ The office thermostat writing down the temperature **every minute**, all day, every day.
- **In the online store:** Every page view and "add to cart" click with its timestamp, plus warehouse sensors recording fridge temperature every 10 seconds.

### 2️⃣ Constrained Devices, Standard Devices and Gateway
- **Constrained devices:** Tiny gadgets (bulbs, sensors) that can't talk to the internet directly. They use short-range radio like **BLE (Bluetooth Low Energy)**.
- **Standard devices:** Laptops, phones and gateways that **can** send data over the internet (**HTTPS**).
- **Gateway:** A small box that **collects data from the tiny devices** and **forwards it to the cloud**.
- **Analogy:** 📬 Staff drop notes in the **floor's mailbox** (gateway), and the mail runner carries them to head office.

### 3️⃣ Cloud Pub/Sub (box 1)
- **What it is:** A **messaging service**. Senders **publish** messages to a **topic**, and receivers **subscribe** to get them. It absorbs **millions of messages per second** and holds them so nothing is lost if the next step is busy.
- **Analogy:** 📥 The **company mailroom**. All incoming mail lands there first, then gets delivered to the right departments.
- **In the online store:** Every order and click event is published to a `shop-events` topic.

### 4️⃣ Cloud Dataflow (box 2)
- **What it is:** A managed service that **processes data streams (and batches)**: cleans, filters, converts and combines records, then **sends them to several destinations at once**. Built on **Apache Beam**.
- **Analogy:** 🗂️ The **sorting desk** behind the mailroom. It opens every envelope, fixes mistakes, stamps it, and sends a copy to **Records** and a copy to **Finance**.
- **In the online store:** Removes duplicate clicks, adds the product category, then writes to Bigtable **and** BigQuery.

### 5️⃣ Cloud Bigtable (box 3, Storage)
- **What it is:** A **NoSQL** database for **huge** amounts of data (terabytes to petabytes) with **very fast reads and writes**, looked up by a **row key**. It's the classic choice for **time-series**, IoT and real-time dashboards.
- **Analogy:** 🗄️ A giant **filing wall** sorted by "sensor + time". You can pull "fridge-7, today 10:00–10:05" instantly.
- **In the online store:** Stores every sensor reading and click so the live dashboard can show "the last 5 minutes" instantly.

### 6️⃣ BigQuery (box 4, Analytics)
- **What it is:** A **data warehouse** for **SQL analytics** on huge datasets: reports, trends, and machine learning (review from Q015 and Q017).
- **Analogy:** 📊 The **analysts' office** that answers big questions: "How did fridge temperatures change over the last year?"
- **In the online store:** "Which products get the most views but the fewest purchases this quarter?"

### 7️⃣ The services in the wrong options
| Service | What it really is | Why it doesn't fit here |
|---|---|---|
| **Cloud Datastore** (now *Firestore in Datastore mode*) | NoSQL **document** database for app data (user profiles, carts) | Not built for massive streams of time-series writes |
| **Cloud Spanner** | Global **relational** (SQL) database with strong consistency | Expensive, and built for transactions (orders, banking), not sensor streams |
| **Firebase Cloud Messaging** | Sends **push notifications to phones and apps** | It sends messages **to** users. It doesn't ingest data **from** devices |
| **Cloud Storage** | **Object/file** storage (images, backups, CSV files) | It stores files. It **doesn't process** streams, so it can't be box 2 |

### 🔗 How They Fit Together
```
📡 Devices ──► 🚪 Gateway ──HTTPS──►  [1] Pub/Sub        (receive: the mailroom)
                                          │
                                          ▼
                                     [2] Dataflow        (process: the sorting desk)
                                       ┌──┴──────────────┐
                                       ▼                 ▼
                              [3] Bigtable          [4] BigQuery
                              STORAGE:              ANALYTICS:
                              fast reads of         SQL reports and
                              recent readings       long-term trends

 Mnemonic: "Pub → Flow → Table → Query"  (Receive → Process → Store → Analyze)
```

---

## 🌍 Real-World Scenario

A company has **thousands of sensors** (in factories, warehouses, smart buildings) sending a reading **every few seconds**. The engineers need to:
1. **Receive everything** without losing messages, even during spikes → **Pub/Sub**
2. **Clean and transform** the stream as it arrives → **Dataflow**
3. **Store it** so apps can read recent values **instantly** → **Bigtable**
4. **Analyze it** with SQL for reports and trends → **BigQuery**

This is Google's **reference architecture for IoT and time-series data**, and the diagram in this question comes from it. *(Note: the diagram is old. It used to include **Cloud IoT Core**, which Google retired in 2023. Today devices or gateways publish straight to Pub/Sub, or go through a partner IoT platform. Pub/Sub → Dataflow → Bigtable/BigQuery is still the standard pipeline.)*

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Cloud Pub/Sub, Cloud Dataflow, Cloud Datastore, BigQuery

**Why it's wrong:**
- ✔️ Boxes 1, 2 and 4 are correct (Pub/Sub, Dataflow, BigQuery).
- ❌ **Box 3 = Datastore** is the wrong database. Datastore is a document database for **app data** (users, carts, settings). It isn't built for **massive streams of time-series writes**. **Bigtable** is.

**📌 When to use it:** Use Datastore (Firestore) when an app needs to save and load records like user profiles or shopping carts.
🏢 **Office example:** The HR filing cabinet with one folder per employee.

### ❌ B
> **B.** Firebase Messages, Cloud Pub/Sub, Cloud Spanner, BigQuery

**Why it's wrong:**
- ❌ **Firebase Cloud Messaging** sends **push notifications to phones**. It doesn't **receive** data from devices.
- ❌ **Pub/Sub in box 2** is wrong. Pub/Sub **delivers** messages but doesn't **process or transform** them.
- ❌ **Spanner** is a costly global SQL database for **transactions**, not time-series storage.

**📌 When to use it:** Use Firebase Messaging when you want to send a pop-up alert to people's phones.
🏢 **Office example:** The office group text that tells everyone "the meeting moved to 3 PM."

### ❌ C (your answer)
> **C.** Cloud Pub/Sub, Cloud Storage, BigQuery, Cloud Bigtable

**Why it's wrong:**
- ✔️ Box 1 = Pub/Sub is right, and it **names the right services**: Bigtable and BigQuery are both in the correct answer.
- ❌ **Box 2 = Cloud Storage**: Storage only **holds files**. It **can't process** a stream or **split it into two outputs**. You need **Dataflow** there.
- ❌ **Boxes 3 and 4 are swapped.** The diagram labels box 3 **"Storage"** and box 4 **"Analytics"**. **BigQuery is the analytics** tool (box 4), and **Bigtable is the storage** database (box 3).
- 💡 **Likely mix-up:** The word "**Storage**" in "Cloud Storage" makes it feel like a storage box. But box 2 is a **processing** step, and the two "Big" names are easy to swap. See the memory tip below.

**📌 When to use it:** Use Cloud Storage when you need to keep files such as images, backups or exported reports.
🏢 **Office example:** The storage room where boxes of files are kept. Nobody in there reads or sorts them.

### ✅ D
> **D.** Cloud Pub/Sub, Cloud Dataflow, Cloud Bigtable, BigQuery

**Why it's correct:**
- ✔️ **1 = Pub/Sub:** receives the flood of device messages reliably.
- ✔️ **2 = Dataflow:** processes the stream and **sends it to both** destinations (the split in the diagram).
- ✔️ **3 = Bigtable (Storage):** the best fit for **huge time-series data** with **fast reads**.
- ✔️ **4 = BigQuery (Analytics):** **SQL analysis** of all the history.

**📌 When to use it:** Use it when nonstop readings must be received, cleaned, kept for quick lookups, and studied for reports.
🏢 **Office example:** Mailroom → sorting desk → a copy to the records wall for quick lookups and a copy to the analysts for monthly reports.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's **warehouse** has **500 fridge sensors** (for groceries) that send temperature over Bluetooth to a **gateway**. The website also sends every **click** as an event.

```
🌡️ Fridge sensors ─BLE─► 🚪 Gateway ─HTTPS─┐
🛒 Website clicks (Next.js) ───────────────┤
                                           ▼
[1] Pub/Sub topic: shop-events
                                           ▼
[2] Dataflow streaming job: clean, dedupe, add product/fridge info
            ├──► [3] Bigtable table: sensor_readings   (row key: fridge-7#2026-10-22T10:00:01)
            │        → live "Fridge health" dashboard: last 5 minutes, instantly
            └──► [4] BigQuery dataset: shop_analytics
                     → "Which fridges ran warm most often this quarter?"
                     → "Most viewed vs. least bought products"
```

**Setup sketch:**
```bash
# 1. Topic + subscription
gcloud pubsub topics create shop-events
gcloud pubsub subscriptions create shop-events-dataflow --topic=shop-events

# 3. Bigtable instance + table (column family "r" = readings)
gcloud bigtable instances create shop-iot --display-name="ShopNow IoT" \
  --cluster-config=id=shop-iot-c1,zone=us-central1-a,nodes=1
cbt -instance=shop-iot createtable sensor_readings families=r

# 4. BigQuery dataset
bq mk --dataset shopnow-prod:shop_analytics

# 2. Dataflow streaming job (a Google template, or your own Apache Beam pipeline)
#    reads from the subscription, then writes to Bigtable and BigQuery
```

**🎬 With option C:** Events land in **Cloud Storage** as files, but **nothing processes them**. The "live" dashboard waits for someone to load the files, and BigQuery sits in the **storage** spot while Bigtable sits in **analytics**, so the analysts are left without SQL. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Classic streaming pipeline: Pub/Sub → Dataflow → Bigtable / BigQuery.**
  🧠 *"**Pub → Flow → Table → Query**": Receive → Process → Store → Analyze.*
- **Pub/Sub = receive messages. Dataflow = process streams.** Cloud Storage only holds files, so it's never the "process" box.
- **"Time-series / IoT / huge, fast reads and writes" → Bigtable.**
- **"SQL analytics / reports / warehouse" → BigQuery.**
- 🧠 **Don't swap the two "Bigs":**
  - Big**table** = a giant **table** you **look things up** in fast (storage).
  - Big**Query** = you **query** it to **analyze** (analytics).
- **Datastore/Firestore** = app data. **Spanner** = global transactions. **Firebase Messaging** = push notifications to phones.
- **Read the diagram labels!** "Storage" and "Analytics" over the boxes give the answer away.

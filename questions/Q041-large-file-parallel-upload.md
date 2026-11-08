# Q041: Using Parallel Composite Uploads for a Large File

**Topic:** Cloud Storage (large-file uploads, network throughput, Nearline storage)

## ❓ Question
> You have 32 GB of data in a single file that you need to upload to a Nearline Storage bucket. The WAN connection you are using is rated at 1 Gbps, and you are the only one on the connection. You want to use as much of the rated 1 Gbps as possible to transfer the file rapidly. How should you upload the file?
>
> **A.** Use the GCP Console to transfer the file instead of gsutil.
>
> **B.** Enable parallel composite uploads using gsutil on the file transfer.
>
> **C.** Decrease the TCP window size on the machine initiating the transfer.
>
> **D.** Change the storage class of the bucket from Nearline to Multi-Regional.

**My answer:** — (Didn't know)
**Correct answer:** B — Enable parallel composite uploads using gsutil on the file transfer.
**Result:** ❓ Didn't know

---

## 1. ❓ Verdict

You marked this as **“didn't know.”** The exam's intended answer is **B. Enable parallel composite uploads using gsutil on the file transfer.** Parallel composite upload splits one large file into pieces, uploads those pieces at the same time, and combines them into one object. That can make better use of available network capacity.

**Important current-practice caveat:** the question specifies a Nearline bucket. Google warns against parallel composite uploads for Nearline, Coldline, or Archive because temporary component objects are deleted quickly and can incur early-deletion charges. The current `gcloud storage` compatibility check also only performs parallel composite uploads when the destination storage class is Standard. So B is the exam's speed-focused answer, but the question omits a material cost/practice issue: don't blindly enable this for a Nearline destination in production.

## 2. 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You must upload one 32 GB file to a Nearline Storage bucket over a 1 Gbps connection that only you are using.
- **What you must achieve:** Use as much of the connection speed as possible so the upload is fast.
- **The limits:** It is one single large file.
- **What they're really asking:** How do you upload it to make full use of the connection?

- **“32 GB”** and **“single file”** point to splitting a large file into parts.
- **“only one on the connection”** means other users are not consuming the stated bandwidth.
- **“use as much of the rated 1 Gbps as possible”** points to sending pieces in parallel.
- **Exam topic:** Cloud Storage upload performance and network throughput.

## 2.5 📚 Key Terms Explained

### Cloud Storage bucket
- **What it is:** A named container in Google Cloud for storing objects, such as files.
- **Analogy:** A labeled filing cabinet.
- **In the online store:** A bucket can hold product photos, downloadable invoices, and backups.

### Nearline Storage
- **What it is:** A Cloud Storage class intended for data that is accessed less often than Standard data. It has a minimum storage duration, so deleting objects early can result in early-deletion charges.
- **Analogy:** An off-site records room for files that are kept for a while and retrieved occasionally.
- **In the online store:** Nearline might hold older backup copies, rather than frequently requested product images.

### WAN and Gbps
- **What they are:** A WAN is a wide area network, such as an internet connection between your office and Google Cloud. Gbps means gigabits per second, a measure of the connection's rated data-carrying rate.
- **Analogy:** A road connecting the office to a distant warehouse; Gbps describes how many lanes the road is rated to carry.
- **In the online store:** The WAN is the path used to send a local backup file into the store's Cloud Storage bucket.

### Bandwidth and throughput
- **What they are:** Bandwidth is the network's possible carrying capacity; throughput is the data rate actually achieved during a transfer. A 1 Gbps rating is not a guarantee that one upload will achieve that exact rate.
- **Analogy:** A road may have many lanes, but traffic flow depends on how vehicles enter and use them.
- **In the online store:** Faster upload throughput helps move product catalogs or backup files into Cloud Storage sooner.

### `gsutil`
- **What it is:** A command-line tool for working with Cloud Storage. It can copy local files to buckets and supports parallel composite upload settings. Google now recommends `gcloud storage` for many command-line tasks, though this exam option specifically names `gsutil`.
- **Analogy:** A text-based filing clerk that sends files to the cloud cabinet.
- **In the online store:** An operator can use a command-line tool to upload a batch of product images or backups.

### Parallel composite upload
- **What it is:** An upload method that divides one file into temporary component objects, uploads them in parallel, then combines them into a single composite object and deletes the components.
- **Analogy:** Several office clerks send separate sections of a large binder at once; another clerk joins the sections into one binder.
- **In the online store:** It can speed up a large media or backup upload when the network and disk can handle parallel work.

### TCP and TCP window size
- **What they are:** TCP is a network protocol that delivers data reliably. The TCP window controls how much unacknowledged data can be in transit at once; reducing it can limit how much data flows over a fast connection.
- **Analogy:** TCP is a tracked delivery service; the window size is how many packages can be sent before waiting for delivery confirmations.
- **In the online store:** TCP carries uploads from a deployment or backup machine to Cloud Storage.

### Storage class
- **What it is:** A setting that describes the access and pricing model for stored objects, such as Standard or Nearline. It does not make the sender's WAN connection faster.
- **Analogy:** A filing policy that determines how records are stored and charged, rather than how fast the courier drives.
- **In the online store:** Frequently requested images can use Standard; older backups may use a colder class.

### Multi-Regional
- **What it is:** A legacy Cloud Storage location term for data stored redundantly across multiple geographic areas. Location and storage class are separate concepts in current Cloud Storage; the option's wording treats “Multi-Regional” as a storage class, which is outdated terminology. Changing a bucket's location is not a simple speed setting.
- **Analogy:** Keeping records in more than one regional office for availability, not adding lanes to the delivery road.
- **In the online store:** Geographic placement can affect availability and access patterns for objects, but does not increase the user's local WAN rating.

### How the terms fit together

```text
Local machine
    │ 1 Gbps WAN connection
    ▼
Cloud Storage bucket (Nearline)

Parallel composite upload: split one large file → upload parts concurrently → compose final object
```

## 3. 🌍 Real-World Scenario

A company needs to move a large database backup from its office to Cloud Storage. The network is available, so sending several chunks at once may finish sooner than sending the whole file as one stream. The engineer must also consider the target storage class: Nearline's minimum storage duration makes quickly deleted temporary chunks a cost concern.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A

> **A.** Use the GCP Console to transfer the file instead of gsutil.

**Why it is wrong for this goal:** The question asks how to push a single, very large file through an available 1 Gbps connection as rapidly as possible. The Cloud Console gives you a convenient point-and-click upload, but it does not perform parallel composite uploads. It therefore does not use the specific method that divides this one file into simultaneous component transfers. It may still complete an upload, but convenience is not the same as maximizing throughput for this large-file scenario.

**When it is useful:** The Console is convenient for a person uploading a small number of files manually, especially when they prefer a visual interface and do not need to script or tune a large transfer.

📌 When to use it: Use it when you want to upload a few files by clicking through a page.  
🏢 Office example: A receptionist uses a filing screen to place a few forms in the right cabinet.

### ✅ B — Exam-intended answer

> **B.** Enable parallel composite uploads using gsutil on the file transfer.

**Why it is correct for the exam's speed goal:** A normal single-stream upload sends the file as one stream. A parallel composite upload breaks a large source file into multiple temporary component objects, uploads those components at the same time, and then composes them into one final object. Several active transfers can keep more of the available network capacity busy, provided the sender's disk, processor, connection, and Cloud Storage can all supply or accept data quickly enough. A 1 Gbps rating is a ceiling, not a promise that the upload will reach exactly 1 Gbps; network overhead and transfer conditions reduce the real rate. This option is the only one that directly increases parallelism for the one large file.

`gsutil` is the tool named by the exam. Its parallel composite upload behavior is controlled through a configuration setting and applies to files above a size threshold. The final object is a composite object: it has CRC32C integrity information rather than an MD5 hash, which can matter for downstream tools that expect MD5 or for Python downloads that need an appropriate CRC32C implementation.

**Nearline caveat:** This question's destination makes B risky in real use. Parallel composite upload creates temporary component objects and deletes them after composing the final object. Nearline has a minimum storage duration, so early deletion of those temporary objects can cause early-deletion charges. Google's current guidance says not to use parallel composite uploads for Nearline, Coldline, or Archive, and the current `gcloud storage` compatibility check only runs parallel composite uploads when the object's class is Standard. So **B is the intended exam answer to the narrow speed question**, while the Nearline detail makes the question incomplete as a real-world recommendation. For an actual Nearline transfer, use an upload method that avoids this temporary-object early-deletion cost, or stage appropriately in Standard and plan the subsequent storage-class change.

📌 When to use it: Use it when a very large file can be split and sent in several parts at once without creating unwanted costs or compatibility problems.  
🏢 Office example: Several clerks send sections of a large binder at the same time, then a records clerk joins the sections into one binder.

### ❌ C

> **C.** Decrease the TCP window size on the machine initiating the transfer.

**Why it is wrong:** TCP's window controls how much data can be sent before the sender must wait for acknowledgments. A smaller window puts a tighter cap on in-flight data. On a fast connection, especially when the destination is far away and acknowledgments take time to return, the sender can spend more time waiting and less time transmitting. That reduces the amount of the 1 Gbps capacity the upload can use. The question asks to use more of the available rate, so reducing the window moves in the opposite direction. If TCP tuning were needed, an engineer would measure the network and size settings for the bandwidth-delay product rather than blindly decreasing the window.

**When it is useful:** A smaller window can be useful for limiting traffic or adapting a connection to a particular constrained network, but it is not a speed-up setting for this task.

📌 When to use it: Use it when you need to limit how much data is sent before the sender waits for confirmation.  
🏢 Office example: Ask the courier to carry one envelope, wait for its receipt, and only then take the next one.

### ❌ D

> **D.** Change the storage class of the bucket from Nearline to Multi-Regional.

**Why it is wrong:** The bottleneck described is the path from the machine to Cloud Storage: the WAN connection. A bucket's storage class or location does not add capacity to that connection or split the upload into parallel streams. “Multi-Regional” is also not a current storage class; it is legacy wording for a multi-region location. Storage class and location describe how Cloud Storage stores and prices data, while the WAN rating describes how quickly data can travel from the sender. Changing where or how the object is stored is not a direct upload-throughput tuning method.

**When it is useful:** Choosing a multi-region location can be appropriate when geographic placement and availability requirements call for data to be stored across regions. It is a placement decision, not a way to make an individual upload faster.

📌 When to use it: Use it when records should be available across more than one geographic area.  
🏢 Office example: Keep records in several regional offices so teams in different areas can access them.

### Quick comparison

| Option | What it changes | Why it misses or meets this goal |
|---|---|---|
| A: Console | Upload interface | Convenient, but doesn't parallelize this single large file. |
| B: Parallel composite upload | How the file is divided and sent | Directly uploads pieces concurrently; intended speed answer, with Nearline fee caveat. |
| C: Smaller TCP window | Amount of data in flight | Restricts the flow and can lower throughput. |
| D: Multi-Regional | Storage placement | Doesn't increase the sender's WAN rate; terminology is also outdated as a storage class. |

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow needs to upload a 32 GB product-video archive from its office to Cloud Storage. Parallel composite upload could send chunks at once and reassemble the archive, which helps with transfer speed. But if the destination is Nearline, temporary chunk deletion can create early-deletion charges. For a real production transfer, check the current upload tool's safeguards and storage-class guidance; the exam's B answer focuses on speed and leaves out this cost caveat.

## 6. 🧠 Key Takeaway / Memory Tip

For a **single huge file and a goal of maximizing throughput**, think **parallel chunks uploaded at once**. Then check the destination storage class: **Nearline and other colder classes can make temporary chunk deletion costly**, so the exam's speed answer needs a real-world caveat.

**Current documentation:** [Parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads), [Object uploads](https://docs.cloud.google.com/storage/docs/uploads), and [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/locations).

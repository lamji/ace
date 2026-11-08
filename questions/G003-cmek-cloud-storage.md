# G003: Encrypt a Bucket With a Key Your Company Controls and Can Disable (CMEK With Cloud KMS)

**Topic:** Cloud Storage (CMEK encryption)
**Exam guide section:** 3.2 Managing storage and data solutions: Configuring customer-managed encryption keys (CMEK)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> A compliance rule requires that objects in a Cloud Storage bucket containing customer invoices be encrypted with a key that your company creates, rotates, and can disable at any time. Encryption must still happen automatically when applications write objects. What should you do?
>
> **A.** Keep the default Google-managed encryption, because it already meets the requirement.
>
> **B.** Encrypt each file on an administrator's laptop with a password before uploading it.
>
> **C.** Create a key in Cloud KMS, grant the Cloud Storage service agent the Cloud KMS CryptoKey Encrypter/Decrypter role on the key, and set the key as the bucket's default encryption key.
>
> **D.** Use customer-supplied encryption keys, and include the raw key with every upload and download request.

**My answer:** — (not tried yet)
**Correct answer:** C
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A bucket (a storage folder in Cloud Storage) holds customer invoices. A compliance rule says what kind of encryption key must protect them.
- **What you must achieve:** Your company must own the key: create it, change it on a schedule (rotate), and be able to switch it off at any time.
- **The limits:** Apps write files normally, so encryption must happen automatically with no extra work per file.
- **What they're really asking:** Which encryption option gives your company control of the key while Google still encrypts every file automatically?

**Clues in the question:**
- "**key that your company creates, rotates, and can disable**": the default Google-owned keys don't give you this control. You need **customer-managed** keys.
- "**must still happen automatically**": the key should live in **Cloud KMS** and be used by the bucket on every write, without apps sending keys.

**Exam topic:** Storage and data security (exam guide section 3.2).

---

## 📚 Key Terms Explained

### 1. Default encryption (Google-managed keys)
- **What it is:** Google encrypts all data at rest automatically with keys that Google creates and manages. You can't see, rotate or disable them.
- **Looks like:** Every new bucket → "Google-managed encryption key"
- **Not to be confused with:** No encryption. Data is always encrypted. The question is who controls the key.
- **Analogy:** 🔒 The bank locks your safe-deposit box with the bank's own key.
- **In the online store:** ShopNow's product images use the default.

### 2. Cloud KMS
- **What it is:** Google Cloud's key management service. It stores encryption keys that **you** create in key rings, and it can rotate them on a schedule and disable or destroy them.
- **Looks like:** `gcloud kms keys create invoices-key --keyring=shop-ring --location=us --purpose=encryption --rotation-period=90d`
- **Not to be confused with:** Secret Manager, which stores passwords and API keys, not encryption keys for services.
- **Analogy:** 🗝️ Your own key cabinet, with a log of each use.
- **In the online store:** Key ring `shop-ring` in `us`.

### 3. CMEK (customer-managed encryption key) 🔑
- **What it is:** Using a Cloud KMS key that **you** manage to protect a Google service's data (a bucket, a disk, BigQuery, Cloud SQL). The service's **service agent** must be allowed to use the key.
- **Looks like:** `gcloud storage buckets update gs://shop-invoices --default-encryption-key=projects/p/locations/us/keyRings/shop-ring/cryptoKeys/invoices-key`
- **Not to be confused with:** CSEK (customer-**supplied** keys), where you send the raw key with every request and Google doesn't store it.
- **Analogy:** 🔐 The bank uses **your** key for your box, and you can take that key back.
- **In the online store:** The invoice bucket defaults to `invoices-key`.

### 4. Service agent
- **What it is:** A Google-managed service account that a Google service uses to act in your project, for example the Cloud Storage service agent.
- **Looks like:** `service-123456789@gs-project-accounts.iam.gserviceaccount.com`
- **Not to be confused with:** Your own app's service account.
- **Analogy:** 🧑‍🔧 The bank's vault clerk who needs permission to use your key.
- **In the online store:** Gets `roles/cloudkms.cryptoKeyEncrypterDecrypter` on `invoices-key`.

### 🔗 How they fit together
```
 App ──write──► gs://shop-invoices ──(default key)──► Cloud KMS invoices-key
                         ▲ Cloud Storage service agent has Encrypter/Decrypter
 Disable key in KMS → objects can't be read ✅ (company control)
```

---

## 🌍 Real-World Scenario

A finance regulator asks a retailer to prove it can make invoice data unreadable on demand. The engineer creates a Cloud KMS key with 90-day rotation, lets the Cloud Storage service agent use it, and sets it as the bucket default. Apps change nothing. If the company ever disables the key, the invoices can't be decrypted.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Keep the default Google-managed encryption, because it already meets the requirement.

**Wrong words:**
- ❌ "**default Google-managed encryption … already meets the requirement**": data is encrypted, but your company can't create, rotate or disable those keys, so the rule isn't met.

📌 **When to use it:** Use it when you have no rule about who controls the keys. That is most data.
🏢 **Office example:** Letting the bank use its own lock on your box.

### ❌ B
> **B.** Encrypt each file on an administrator's laptop with a password before uploading it.

**Wrong words:**
- ❌ "**on an administrator's laptop with a password**": manual, not automatic, and the password is hard to rotate or disable centrally.

📌 **When to use it:** Never use this for app data. Use CMEK in Cloud KMS.
🏢 **Office example:** Locking each invoice with a padlock by hand before filing it.

### ✅ C
> **C.** Create a key in Cloud KMS, grant the Cloud Storage service agent the Cloud KMS CryptoKey Encrypter/Decrypter role on the key, and set the key as the bucket's default encryption key.

**Why it's correct:**
- ✔️ "**Create a key in Cloud KMS**" matches "**key that your company creates, rotates, and can disable**": KMS keys are yours to rotate and disable.
- ✔️ "**grant the Cloud Storage service agent the … Encrypter/Decrypter role on the key**" is required so the bucket is allowed to use the key.
- ✔️ "**set the key as the bucket's default encryption key**" matches "**Encryption must still happen automatically**".

📌 **When to use it:** Use it when a rule says your company must own and be able to switch off the key that protects stored data.
🏢 **Office example:** The bank locks your box with your own key, and you can cancel that key whenever you like.

### ❌ D
> **D.** Use customer-supplied encryption keys, and include the raw key with every upload and download request.

**Wrong words:**
- ✔️ CSEK does let the customer own the key.
- ❌ "**include the raw key with every upload and download request**": every app must handle the raw key, which breaks "**automatically when applications write**". Google doesn't store the key, so losing it means losing the data.

📌 **When to use it:** Use it when policy says Google must never store your key at all, and you can supply it on every request.
🏢 **Office example:** Bringing your own key to the bank every single visit.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** invoices:
- `gs://shopnow-invoices` with a default CMEK `shop-ring/invoices-key` and 90-day rotation.
- The Cloud SQL `orders` instance can also use CMEK.
- If the key is disabled, invoice PDFs can't be read until it's enabled again.

---

## 🧠 Key Takeaways / Memory Tips

- **"Our own key, rotate, disable" → CMEK in Cloud KMS, and grant the service agent Encrypter/Decrypter.**
- CSEK = you **supply** the key on every call (rare). CMEK = you **manage** it in KMS (common).
  🧠 *"**CMEK = Managed by me in KMS.**"*
- Related: **Q061**, **Q107** (Cloud Storage).

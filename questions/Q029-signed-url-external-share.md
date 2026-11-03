# Q029: Sharing a Sensitive File for 4 Hours with a Company That Has No Google Account (Signed URL)

**Topic:** Cloud Storage security (signed URLs vs public objects, lifecycle management, static websites, temporary buckets)

## ❓ Question
> You have an object in a Cloud Storage bucket that you want to share with an external company. The object contains sensitive data. You want access to the content to be removed after four hours. The external company does not have a Google account to which you can grant specific user-based access privileges. You want to use the most secure method that requires the fewest steps. What should you do?
>
> **A.** Create a signed URL with a four-hour expiration and share the URL with the company.
>
> **B.** Set object access to 'public' and use object lifecycle management to remove the object after four hours.
>
> **C.** Configure the storage bucket as a static website and furnish the object's URL to the company. Delete the object from the storage bucket after four hours.
>
> **D.** Create a new Cloud Storage bucket specifically for the external company to access. Copy the object to that bucket. Delete the bucket after four hours have passed.

*(The `λ€˜ λ€™` characters in the screenshot are broken quote marks, shown here as `'`.)*

**My answer:** B
**Correct answer:** A
**Result:** ❌ Incorrect

---

## 📖 What the Question Is Asking

**In plain words:** You need to give an outside company **one sensitive file**. They **don't have a Google account**, so you can't add them in IAM. Their access must **stop after 4 hours**. What's the **safest** way with the **fewest steps**?

| Keyword | What it hints at |
|---|---|
| "**sensitive data**" | Never make it **public** |
| "**removed after four hours**" | Access must **expire automatically** at a set time |
| "**does not have a Google account**" | You can't use IAM roles. You need a link that **carries its own permission** |
| "**most secure**" + "**fewest steps**" | One command that makes an expiring link: a **signed URL** |

**Exam topic:** Cloud Storage access control (signed URLs).

---

## 📚 Key Terms Explained

### 1️⃣ Signed URL 🔑
- **What it is:** A **normal web link to one file**, with a **digital signature and an expiry time** added to the end. Anyone who has the link can download that file, **with no Google account needed**, until the time runs out. After that, the link returns "Access denied".
- **Looks like:**
  ```
  https://storage.googleapis.com/shopnow-contracts/supplier-pricing.pdf
    ?X-Goog-Algorithm=GOOG4-RSA-SHA256
    &X-Goog-Credential=signer@shopnow-prod.iam.gserviceaccount.com/...
    &X-Goog-Expires=14400          ← 4 hours, in seconds
    &X-Goog-Signature=8f3a9c...    ← proves you created it, so it can't be faked or edited
  ```
- **Not to be confused with:** making the file **public**. The file stays **private**. Only people holding **this exact link** can open it, and only **until it expires**. Change one character and it stops working.
- **Analogy:** 🎟️ A **visitor pass with an expiry time printed on it**: "Valid for room 3 until 4:00 PM". No employee ID needed, and after 4 PM the guard refuses it.
- **In the online store:** A customer clicks "Download invoice" and gets a signed URL valid for 15 minutes.

### 2️⃣ Public Object (`allUsers`)
- **What it is:** A file whose permission is set to **`allUsers` can read**, meaning **anyone on the internet** who finds or guesses its address can open it, forever, until you change it.
- **Looks like:** `https://storage.googleapis.com/shopnow-contracts/supplier-pricing.pdf` (no signature, no expiry)
- **Not to be confused with:** a signed URL. Public = **no lock at all**. Copies can also be cached by browsers and proxies.
- **Analogy:** 📌 Pinning the document to the **notice board in the street**.
- **In the online store:** Fine for product photos. Never for contracts or invoices.

### 3️⃣ Object Lifecycle Management (review from Q020)
- **What it is:** **Automatic rules** on a bucket, like "delete files older than **N days**" or "move to Coldline after 30 days". Google checks them in the background.
- **Looks like:** `{"action": {"type": "Delete"}, "condition": {"age": 1}}`. The **smallest age is 1 day**, so you **can't** say "4 hours".
- **Not to be confused with:** a timer. Rules are counted in **days** and run **asynchronously**, so the delete may happen hours later.
- **Analogy:** 🗄️ The office policy "shred files older than one year", done by the cleaners whenever they get round to it.

### 4️⃣ Static Website Hosting on a Bucket
- **What it is:** A bucket setting that serves its files as a **website** (`index.html`, images). The files must be **public** for visitors to see them.
- **Looks like:** `gcloud storage buckets update gs://www.shopnow-promo.com --web-main-page-suffix=index.html`
- **Not to be confused with:** a private file share. It's built for **public** content.
- **Analogy:** 🪧 Putting the document in the **shop window**.

### 🔗 How They Fit Together
```
🔒 gs://shopnow-contracts/supplier-pricing.pdf   (stays PRIVATE)
        │
        │  gcloud storage sign-url … --duration=4h
        ▼
🎟️ Signed URL (signature + expires in 4h)  ──email──►  🏢 External company (no Google account)
        │
        ├── 0–4h:  link works ✅
        └── after 4h: "Access denied" ✅  (automatic, nothing to delete)

❌ Public (B/C): anyone with the address can read it, and lifecycle can't do 4 hours
❌ New bucket (D): more steps, and it still needs public access or a signed URL
```

---

## 🌍 Real-World Scenario

Companies often send files to **partners, lawyers, auditors or suppliers** who **aren't** in their Google Workspace: a contract draft, a data export, a video file. Email attachments are too large or too permanent, and making the file public is a data leak waiting to happen. The standard answer is a **time-limited link**: the partner downloads it today, and tomorrow the link is dead even if the email gets forwarded.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Create a signed URL with a four-hour expiration and share the URL with the company.

**Why it's correct:**
- ✔️ **No Google account needed.** The permission is inside the link.
- ✔️ **The file stays private.** Only this link works.
- ✔️ **Expires automatically after 4 hours.** You don't have to remember to delete anything.
- ✔️ **One step**: create the link and send it.

**📌 When to use it:** Use it when someone outside the company needs one private file for a short time.
🏢 **Office example:** Giving a courier a visitor pass for the records room that says "valid until 4 PM today".

### ❌ B (your answer)
> **B.** Set object access to 'public' and use object lifecycle management to remove the object after four hours.

**Why it's wrong:**
- ❌ **Public = anyone on the internet** can read the **sensitive** file, not just the company. That's the least secure choice.
- ❌ **Lifecycle rules work in days, not hours.** The smallest Age is **1 day**, and deletion isn't instant.
- ❌ It **deletes your file**. You only wanted to remove **their access**.
- 💡 **Likely mix-up:** "remove after four hours" made you think of the automatic delete rule from Q020. Lifecycle cleans up **old files**. It doesn't control **who can open** a file.

**📌 When to use it:** Use public files for things everyone may see, and lifecycle rules to clean up old files after days or months.
🏢 **Office example:** The company brochure in the lobby (public), and the cleaners shredding old flyers once a month (lifecycle).

### ❌ C
> **C.** Configure the storage bucket as a static website and furnish the object's URL to the company. Delete the object from the storage bucket after four hours.

**Why it's wrong:**
- ❌ A static website needs **public** files, so it has the same leak as B.
- ❌ **Extra steps**: website setup, then remembering to **delete by hand** after 4 hours.

**📌 When to use it:** Use it when you want to put a simple public web page online, like a promo page.
🏢 **Office example:** Putting a poster in the shop window for everyone passing by.

### ❌ D
> **D.** Create a new Cloud Storage bucket specifically for the external company to access. Copy the object to that bucket. Delete the bucket after four hours have passed.

**Why it's wrong:**
- ❌ **Many steps**: create a bucket, copy, set access, then delete by hand.
- ❌ The company **has no Google account**, so you **can't grant them access** to the new bucket without making it **public** or using a **signed URL** anyway.

**📌 When to use it:** Use a separate bucket when a partner gets their own long-term shared space with proper accounts.
🏢 **Office example:** Renting a dedicated storage room for a long-term partner who has their own staff ID cards.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow must send `supplier-pricing.pdf` (secret discount prices) to a logistics company that **doesn't use Google**.

```bash
gcloud storage sign-url gs://shopnow-contracts/supplier-pricing.pdf \
  --duration=4h \
  --impersonate-service-account=url-signer@shopnow-prod.iam.gserviceaccount.com
```
→ Prints a long `https://storage.googleapis.com/...&X-Goog-Expires=14400&X-Goog-Signature=...` link. Email it.

| Time | Result |
|---|---|
| 10:00 | Logistics company opens the link → PDF downloads ✅ |
| 14:01 | Someone forwards the email and clicks the link → **"Access denied"** ✅ |
| Any time | `https://storage.googleapis.com/shopnow-contracts/supplier-pricing.pdf` without the signature → **denied** (file is private) ✅ |

**The same idea in the app:** The "Download my invoice" button calls the backend, which creates a **15-minute signed URL** for `gs://shopnow-invoices/inv-1043.pdf`. Invoices are never public.

**🎬 With option B:** The pricing PDF is public. A competitor guesses the address pattern and downloads it. The lifecycle rule can't run for at least a day, and when it does, it deletes ShopNow's own copy. ❌

---

## 🧠 Key Takeaways / Memory Tips

- **"No Google account" + "temporary access" + "one file" → Signed URL.**
  🧠 *"**Signed URL = a visitor pass with an expiry time.**"*
- **Sensitive data → never public.** Options with `public` or `allUsers` are traps when data is sensitive.
- **Lifecycle rules count in days**, so they can't do "4 hours", and they **delete files**, not **access**.
- Bonus: **signed URLs** can also let someone **upload** without an account (a PUT signed URL). Max expiry is **7 days**.
- Related: **Q020** (lifecycle Age counts from creation), **Q026/Q028** (IAM roles for people and machines that *do* have Google identities).

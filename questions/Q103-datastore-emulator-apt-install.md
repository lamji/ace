# Q103: Testing Datastore Locally When the SDK Came From apt (Install the Emulator With apt-get)

**Topic:** Cloud SDK (components, apt-installed SDK, Datastore emulator)

## ❓ Question
> You have a developer laptop with the Cloud SDK installed on Ubuntu. The Cloud SDK was installed from the Google Cloud Ubuntu package repository. You want to test your application locally on your laptop with Cloud Datastore. What should you do?
>
> **A.** Export Cloud Datastore data using gcloud datastore export.
>
> **B.** Create a Cloud Datastore index using gcloud datastore indexes create.
>
> **C.** Install the google-cloud-sdk-datastore-emulator component using the apt get install command.
>
> **D.** Install the cloud-datastore-emulator component using the gcloud components install command.

**My answer:** — (didn't know)
**Correct answer:** C
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** You want to run Datastore **on your laptop** for testing. Your gcloud was installed with **apt** (Ubuntu's package manager). How do you add the emulator?

**Clues in the question:**
- "**test your application locally**": you need the **Datastore emulator**, a local fake Datastore.
- "**installed from the Google Cloud Ubuntu package repository**": when gcloud comes from apt, `gcloud components install` is **disabled**. Extra pieces are installed with **apt-get** instead.

**Exam topic:** Cloud SDK.

---

## 📚 Key Terms Explained

### 1. Datastore emulator 🔑
- **What it is:** A **small program that runs a fake Datastore on your laptop**, so you can test without touching (or paying for) the real one.
- **Looks like:** `gcloud beta emulators datastore start` → `localhost:8081`
- **Not to be confused with:** the real Datastore. Data disappears when you stop it.
- **Analogy:** 🧪 A **practice cash register** for training new staff.
- **In the online store:** Developers test the cart code against a local Datastore.

### 2. apt / apt-get
- **What it is:** Ubuntu's **package manager**, the tool that installs and updates software from a repository.
- **Looks like:** `sudo apt-get install google-cloud-sdk-datastore-emulator`
- **Not to be confused with:** gcloud components, which is gcloud's own installer.
- **Analogy:** 📦 The company's IT software catalog.
- **In the online store:** The laptop's gcloud is kept updated by apt.

### 3. gcloud components install
- **What it is:** gcloud's **own installer** for extra pieces. It works only when gcloud was installed with Google's own installer, **not** with apt.
- **Looks like:** `gcloud components install cloud-datastore-emulator`
- **Not to be confused with:** apt-get. With an apt install it says: "component manager is disabled".
- **Analogy:** 🛠️ A self-service tool that's switched off when IT manages your PC.
- **In the online store:** Works on Mac laptops installed with the Google installer.

### 🔗 How they fit together
```
 gcloud installed by apt?  → add pieces with: sudo apt-get install google-cloud-sdk-<piece> ✅
 gcloud installed by Google installer? → gcloud components install <piece>
```

---

## 🌍 Real-World Scenario

A developer on Ubuntu wants to run tests against Datastore without a cloud project. They try `gcloud components install` and get "component manager is disabled for this installation". The fix is `sudo apt-get install google-cloud-sdk-datastore-emulator`, then they start the emulator.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Export Cloud Datastore data using gcloud datastore export.

**Wrong words:**
- ❌ "**Export Cloud Datastore data**": this copies real data to Cloud Storage. It doesn't give you a local Datastore.

📌 **When to use it:** Use export for backups or moving data.
🏢 **Office example:** Photocopying the real files when you needed a practice cash register.

### ❌ B
> **B.** Create a Cloud Datastore index using gcloud datastore indexes create.

**Wrong words:**
- ❌ "**Create a Cloud Datastore index**": indexes speed up queries in the real database. Nothing runs locally.

📌 **When to use it:** Use it when a real Datastore query needs a composite index.
🏢 **Office example:** Making a new index card for the real archive.

### ✅ C
> **C.** Install the google-cloud-sdk-datastore-emulator component using the apt get install command.

**Why it's correct:**
- ✔️ "**google-cloud-sdk-datastore-emulator**" matches "**test your application locally … with Cloud Datastore**": the emulator runs Datastore on the laptop.
- ✔️ "**using the apt get install command**" matches "**installed from the Google Cloud Ubuntu package repository**": an apt-installed SDK gets its pieces through apt.

📌 **When to use it:** Use it when your tools were installed by the system's software catalog and you need an add-on.
🏢 **Office example:** Asking IT's software catalog for the training register, because self-service is locked on your PC.

### ❌ D
> **D.** Install the cloud-datastore-emulator component using the gcloud components install command.

**Wrong words:**
- ✔️ "cloud-datastore-emulator" is the right tool.
- ❌ "**gcloud components install**": disabled when the SDK was installed with apt.

📌 **When to use it:** Use it when gcloud was installed with Google's own installer.
🏢 **Office example:** Using the self-service tool that IT has switched off on your PC.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's developer Ben uses Ubuntu with gcloud from apt.

```bash
sudo apt-get install google-cloud-sdk-datastore-emulator
gcloud beta emulators datastore start
$(gcloud beta emulators datastore env-init)   # sets DATASTORE_EMULATOR_HOST=localhost:8081
npm test   # cart service tests hit the local Datastore
```

---

## 🧠 Key Takeaways / Memory Tips

- **Local testing → emulator.**
- **SDK from apt → `apt-get install google-cloud-sdk-…`. SDK from Google's installer → `gcloud components install`.**
  🧠 *"**Installed with apt? Add with apt.**"*
- Related: **Q084** (gcloud configurations), **Q075** (gcloud services list).

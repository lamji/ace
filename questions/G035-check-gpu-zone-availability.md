# G035: Check Which Zones in a Region Offer a Specific GPU Type Before Deploying (gcloud compute accelerator-types list)

**Topic:** Compute Engine (regions and zones availability)
**Exam guide section:** 1.1 Verifying product availability across geographical locations (e.g., regions, zones)

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> You plan to deploy VMs with NVIDIA H100 GPUs in europe-west4. Not every zone offers every GPU type. Before you deploy, you want to confirm which zones in that region offer H100 GPUs. What should you do?
>
> **A.** Run gcloud projects list.
>
> **B.** Run gcloud compute regions list.
>
> **C.** Create a VM in each zone with an H100 GPU and see which ones succeed.
>
> **D.** Run gcloud compute accelerator-types list and filter the results by zones in europe-west4 and the H100 accelerator type.

**My answer:** — (not tried yet)
**Correct answer:** D
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You want VMs with H100 GPUs (powerful AI chips) in the europe-west4 region. Each region is split into zones (separate data centers), and not every zone has every GPU type.
- **What you must achieve:** Find out which zones in that region offer H100 GPUs before you deploy.
- **The limits:** Check first rather than by trial and error.
- **What they're really asking:** Which command lists GPU types available per zone?

**Clues in the question:**
- "**Not every zone offers every GPU type**" + "**confirm which zones**": list the **accelerator types** per zone.
- `gcloud compute accelerator-types list --filter="zone~europe-west4 AND name~h100"`.

**Exam topic:** Project setup / locations (exam guide sections 1.1 and 2.1).

---

## 📚 Key Terms Explained

### 1. Region / zone
- **What it is:** A region is a geographic area (like `europe-west4`, Netherlands). A zone is one data center area inside it (like `europe-west4-a`).
- **Looks like:** `europe-west4-a`, `europe-west4-b`, `europe-west4-c`
- **Not to be confused with:** A multi-region (like `EU`), which is used by storage.
- **Analogy:** 🏙️ A city (region) and its neighborhoods (zones).
- **In the online store:** ShopNow's EU training runs in `europe-west4`.

### 2. accelerator-types list 🔑
- **What it is:** A gcloud command that lists GPU and accelerator types offered in each zone. `machine-types list` does the same for machine types.
- **Looks like:** `gcloud compute accelerator-types list --filter="zone~europe-west4"` → `nvidia-h100-80gb  europe-west4-b`…
- **Not to be confused with:** `regions list`, which shows regions and quotas, not GPU types per zone.
- **Analogy:** 📋 The menu showing which dishes each branch kitchen serves.
- **In the online store:** Confirms where H100s exist.

### 🔗 How they fit together
```
 accelerator-types list (filter europe-west4, h100)
   → europe-west4-b ✅, europe-west4-c ✅ (a ✗) → deploy there
```

---

## 🌍 Real-World Scenario

An ML team almost scheduled a launch in a zone without H100s. A quick `accelerator-types list` shows the right zones, and the Terraform zone variable is set before deployment.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Run gcloud projects list.

**Wrong words:**
- ❌ "**gcloud projects list**": lists projects. Nothing about GPUs or zones.

📌 **When to use it:** Use it to find project IDs.
🏢 **Office example:** Listing departments when you asked about the menu.

### ❌ B
> **B.** Run gcloud compute regions list.

**Wrong words:**
- ❌ "**regions list**": shows regions and some regional quotas, not which zones offer H100s.

📌 **When to use it:** Use it to see the list of regions.
🏢 **Office example:** Listing cities without checking the menus.

### ❌ C
> **C.** Create a VM in each zone with an H100 GPU and see which ones succeed.

**Wrong words:**
- ❌ "**Create a VM in each zone … see which ones succeed**": trial and error that costs money and can fail for other reasons, like quota.

📌 **When to use it:** Avoid it. Check availability first.
🏢 **Office example:** Ordering the dish at every branch to see which serves it.

### ✅ D
> **D.** Run gcloud compute accelerator-types list and filter the results by zones in europe-west4 and the H100 accelerator type.

**Why it's correct:**
- ✔️ "**gcloud compute accelerator-types list**" matches "**confirm which zones … offer H100 GPUs**".
- ✔️ "**filter … by zones in europe-west4 and the H100 accelerator type**" matches "**in europe-west4**" and "**H100**".

📌 **When to use it:** Use it when you need to know where a certain special machine part is offered before you plan.
🏢 **Office example:** Checking which branch kitchens serve a dish before booking the event.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** ML: `gcloud compute accelerator-types list --filter="zone~europe-west4 AND name~h100"` → deploy training to `europe-west4-b`.

---

## 🧠 Key Takeaways / Memory Tips

- **Is GPU / machine type X offered in zone Y? → `gcloud compute accelerator-types list` / `machine-types list` with a filter.**
  🧠 *"**Check the menu before ordering.**"*
- Related: **G034**, **G036**, **Q089**.

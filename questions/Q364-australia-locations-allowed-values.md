# Q364: Restrict New Resources to Australian Regions With Minimal Config (gcp.resourceLocations allowed in:australia-locations)

**Topic:** Organization Policy (resource locations)

## ❓ Question
> You are a Google Cloud organization policy administrator for your company that operates in a regulated industry. You need to enforce a policy that restricts all new location-based Google Cloud resources to the australia-southeast1 and australia-southeast2 regions only. You want to ensure that this policy requires minimal configuration. What should you do?
>
> **A.** Create a custom organization policy that uses the resource.location == ‘australia-southeast1’ || resource.location == ‘australia-southeast2’ Common Expression Language (CEL) condition.
>
> **B.** Modify the gcp.resourceLocations list constraint by adding in:australia-locations to the allowed_values list.
>
> **C.** Modify the gcp.resourceLocations list constraint by adding in:australia-locations to the denied_values list.
>
> **D.** Create a custom organization policy that uses the resource.location.startsWith(‘australia’) Common Expression Language (CEL) condition.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Only `australia-southeast1` and `-southeast2`; **minimal configuration**.

**Clues in the question:**
- Built-in **`gcp.resourceLocations`** constraint + value group **`in:australia-locations`** in **allowed** values. No custom CEL needed.

**Exam topic:** Organization Policy.

---

## 📚 Key Terms Explained

### 1. Location value groups 🔑
- **What it is:** Predefined groups like `in:eu-locations`, `in:australia-locations` covering all regions/zones in an area.
- **Looks like:** `allowedValues: [in:australia-locations]`
- **Not to be confused with:** custom org policy (CEL).
- **Analogy:** 🗺️ 'Australia only' checkbox instead of listing cities.
- **In the online store:** —

### 🔗 How they fit together
```
 gcp.resourceLocations allowed: in:australia-locations ✅
```

---

## 🌍 Real-World Scenario

A regulated company sets **allowed `in:australia-locations`** at the org.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Create a custom organization policy that uses the resource.location == ‘australia-southeast1’ || resource.location == ‘australia-southeast2’ Common Expression Language (CEL) condition.

**Wrong words:**
- ❌ "**custom organization policy … CEL**": more work; custom constraints don't cover all services.

📌 **When to use it:** Use custom constraints for rules built-in ones can't express.
🏢 **Office example:** Writing a custom rulebook for a standard rule.

### ✅ B
> **B.** Modify the gcp.resourceLocations list constraint by adding in:australia-locations to the allowed_values list.

**Why it's correct:**
- ✔️ "**gcp.resourceLocations list constraint**" matches "**restricts all new location-based Google Cloud resources**".
- ✔️ "**in:australia-locations to the allowed_values list**" matches "**australia-southeast1 and australia-southeast2 regions only**" + "**minimal configuration**".

📌 **When to use it:** Use it when everything must stay in one country, using a ready-made rule.
🏢 **Office example:** Ticking the 'Australia only' box on HQ's rule sheet.

### ❌ C
> **C.** Modify the gcp.resourceLocations list constraint by adding in:australia-locations to the denied_values list.

**Wrong words:**
- ❌ "**denied_values**": blocks Australia — the opposite.

📌 **When to use it:** Use denied values to block a region.
🏢 **Office example:** Banning the only allowed country.

### ❌ D
> **D.** Create a custom organization policy that uses the resource.location.startsWith(‘australia’) Common Expression Language (CEL) condition.

**Wrong words:**
- ❌ "**custom organization policy … startsWith**": more config, limited coverage.

📌 **When to use it:** Use custom policies for special cases.
🏢 **Office example:** A homemade rule for a standard need.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow AU entity: allowed `in:australia-locations`.

---

## 🧠 Key Takeaways / Memory Tips

- **Region restriction → gcp.resourceLocations with `in:<area>-locations` in allowed values.**
  🧠 *"**Allow the group, not each region.**"*
- Related: **Q333**, **Q350**.

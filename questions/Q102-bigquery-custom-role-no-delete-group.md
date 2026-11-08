# Q102: Let Users Query BigQuery but Not Delete Datasets (Custom Role + Group)

**Topic:** IAM / BigQuery (custom roles, groups, predefined BigQuery roles)

## ❓ Question
> Your organization needs to grant users access to query datasets in BigQuery but prevent them from accidentally deleting the datasets. You want a solution that follows Google-recommended practices. What should you do?
>
> **A.** Add users to roles/bigquery user role only, instead of roles/bigquery dataOwner.
>
> **B.** Add users to roles/bigquery dataEditor role only, instead of roles/bigquery dataOwner.
>
> **C.** Create a custom role by removing delete permissions, and add users to that role only.
>
> **D.** Create a custom role by removing delete permissions. Add users to the group, and then add the group to the custom role.

**My answer:** — (didn't know)
**Correct answer:** D
**Result:** ❓ Didn't know

> ℹ️ **Note:** This is the site's accepted (most voted) answer. Some people argue for A, but `bigquery.user` lets users create datasets, and they become owner of (and can delete) those datasets.

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** Users need to query BigQuery datasets.
- **What you must achieve:** Let them run queries.
- **The limits:** They must not be able to delete datasets; follow Google's recommended practice.
- **What they're really asking:** Which roles let them query but not delete?

**Clues in the question:**
- "**query datasets**" + "**prevent … deleting**": you need a role with query permissions but **without `bigquery.datasets.delete`** → a **custom role**.
- "**Google-recommended practices**": grant roles to a **group**, not to each user.

**Exam topic:** IAM.

---

## 📚 Key Terms Explained

### 1. Custom role 🔑
- **What it is:** A role **you build** by picking permissions, for example a copy of a BigQuery role with the delete permissions removed.
- **Looks like:** `gcloud iam roles create bqQueryNoDelete --project=shopnow-data --permissions=bigquery.jobs.create,bigquery.tables.getData,...`
- **Not to be confused with:** a predefined role, which Google maintains and you can't edit.
- **Analogy:** ✂️ A hand-made pass that lists exactly which rooms you can enter.
- **In the online store:** Analysts can query `sales` but can't drop it.

### 2. Google group
- **What it is:** A **named list of email addresses**. Granting a role to the group gives it to everyone on the list.
- **Looks like:** `analysts@shopnow.com = [ana@…, ben@…]`
- **Not to be confused with:** a shared account. Nobody logs in as the group.
- **Analogy:** 📋 The team list at the front desk.
- **In the online store:** New analysts are added to the list, not to IAM.

### 3. BigQuery predefined roles
- **What it is:** `bigquery.user` = run queries, create datasets. `bigquery.dataEditor` = edit tables **and delete tables**. `bigquery.dataOwner` = full control of the data, including deleting datasets.
- **Looks like:** `roles/bigquery.dataEditor`
- **Not to be confused with:** each other: all three can delete something.
- **Analogy:** 🔑 Different key rings.
- **In the online store:** Engineers get dataEditor; analysts don't.

### 🔗 How they fit together
```
 analysts@shopnow.com (group) ── custom role "query, no delete" ✅
      ├── bigquery.jobs.create      (run queries)
      ├── bigquery.tables.getData   (read rows)
      └── ✗ bigquery.datasets.delete (removed)
```

---

## 🌍 Real-World Scenario

A data team wants business analysts to explore the warehouse freely, but last month someone deleted a dataset by mistake. The admin creates a **custom role** without delete permissions and grants it to the **analysts group**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Add users to roles/bigquery user role only, instead of roles/bigquery dataOwner.

**Wrong words:**
- ❌ "**roles/bigquery user role**": users can create datasets and become owner of them, so they can still delete datasets.
- ❌ "**Add users**" one by one: not the recommended practice.

📌 **When to use it:** Use bigquery.user when people should run queries and create their own datasets.
🏢 **Office example:** Letting staff open new folders in the archive, which they can also throw away.

### ❌ B
> **B.** Add users to roles/bigquery dataEditor role only, instead of roles/bigquery dataOwner.

**Wrong words:**
- ❌ "**roles/bigquery dataEditor**": it can delete tables and change data. Not safe from accidental deletion.
- ❌ "**Add users**" individually: not best practice.

📌 **When to use it:** Use dataEditor for engineers who load and change data.
🏢 **Office example:** Giving analysts the shredder key just so they can read files.

### ❌ C
> **C.** Create a custom role by removing delete permissions, and add users to that role only.

**Wrong words:**
- ✔️ "Create a custom role by removing delete permissions" is the right role.
- ❌ "**add users to that role only**": granting to individual users isn't Google's recommended practice. Use a group.

📌 **When to use it:** Use it when only one or two people need the role and there's no group.
🏢 **Office example:** Writing each analyst's name on the door list one by one.

### ✅ D
> **D.** Create a custom role by removing delete permissions. Add users to the group, and then add the group to the custom role.

**Why it's correct:**
- ✔️ "**Create a custom role by removing delete permissions**" matches "**query datasets … but prevent them from accidentally deleting**": they can query, but delete is not in the role.
- ✔️ "**Add users to the group, and then add the group to the custom role**" matches "**follows Google-recommended practices**": roles go to groups, not individuals.

📌 **When to use it:** Use it when a team needs almost all of a role, minus one dangerous action.
🏢 **Office example:** Giving the analyst team a pass to read the archive, but no key to the shredder room.

---

## 🛒 E-Commerce Full-Stack Example

```bash
gcloud iam roles create bqAnalyst --project=shopnow-data \
  --permissions=bigquery.jobs.create,bigquery.datasets.get,bigquery.tables.list,bigquery.tables.get,bigquery.tables.getData
gcloud projects add-iam-policy-binding shopnow-data \
  --member=group:analysts@shopnow.com --role=projects/shopnow-data/roles/bqAnalyst
```
Ana runs `SELECT * FROM sales.orders LIMIT 10` ✅. `bq rm -d sales` → Access Denied ✅.

---

## 🧠 Key Takeaways / Memory Tips

- **Need a role minus one dangerous permission → custom role.**
- **Best practice: grant roles to groups.**
- dataEditor and dataOwner can delete.
  🧠 *"**Remove the dangerous permission, then grant the role to a group.**"*
- Related: **Q080** (Viewer), **Q100** (group + role), **Q025** (auditors group).

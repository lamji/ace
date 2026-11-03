# Q038: Granting Cloud Spanner Data Access to Three Users

**Topic:** IAM + Cloud Spanner (database access role, groups, least privilege)

## ❓ Question
> You need to grant access for three users so that they can view and edit table data on a Cloud Spanner instance. What should you do?
>
> **A.** Run gcloud iam roles describe roles/spanner.databaseUser. Add the users to the role.
>
> **B.** Run gcloud iam roles describe roles/spanner.databaseUser. Add the users to a new group. Add the group to the role.
>
> **C.** Run gcloud iam roles describe roles/spanner.viewer --project my-project. Add the users to the role.
>
> **D.** Run gcloud iam roles describe roles/spanner.viewer --project my-project. Add the users to a new group. Add the group to the role.

**My answer:** B
**Correct answer:** B — Run gcloud iam roles describe roles/spanner.databaseUser. Add the users to a new group. Add the group to the role.
**Result:** ✅ Correct

---

## 1. ✅ Verdict

**Correct — your answer is B.** The intended role is `roles/spanner.databaseUser`, which allows reading and writing data. Putting the three people in one group makes the access easier to manage.

The command wording needs care: `gcloud iam roles describe` only displays role details. It does not add a group or grant access. In real use, an administrator grants the role to the group on the appropriate Spanner resource.

## 2. 📖 What the Question Is Asking

In plain words: three people need permission to both look at and change rows in a Cloud Spanner database. Which role and access-management approach fit?

- **“view and edit”** means read and write data; a view-only role is not enough.
- **“three users”** points toward giving the same role to a group, then managing people through the group.
- **Exam topic:** IAM and Cloud Spanner data access.

## 2.5 📚 Key Terms Explained

### Cloud Spanner
- **What it is:** Google Cloud's managed relational database service for storing structured data and running SQL queries.
- **Analogy:** A shared office records system with organized tables and rows.
- **In the online store:** It could hold orders and inventory records used by the store's backend.

### Instance
- **What it is:** A Cloud Spanner resource that contains databases and provides the capacity to run them.
- **Analogy:** An office building that contains one or more records rooms.
- **In the online store:** The Spanner instance is the managed database environment that holds the store's database.

### Table data
- **What it is:** The actual records stored in rows and columns of a database table. Viewing means reading those records; editing means changing them.
- **Analogy:** The entries inside a spreadsheet or filing ledger.
- **In the online store:** Rows such as orders, products, or inventory counts.

### IAM (Identity and Access Management)
- **What it is:** Google Cloud's system for deciding who can do what on a resource.
- **Analogy:** The office's system for issuing and checking access badges.
- **In the online store:** IAM can grant the store's operators access to database resources.

### IAM role
- **What it is:** A named bundle of permissions. An administrator grants a role to a person or group on a resource.
- **Analogy:** A badge type that opens specific office areas.
- **In the online store:** `roles/spanner.databaseUser` can allow a backend operator to read and write Spanner data.

### `roles/spanner.databaseUser`
- **What it is:** A predefined role that allows reading and writing Spanner database data, running SQL including data changes, and viewing or updating schema. It is broad for data work, so use it only when both read and write access are needed.
- **Analogy:** A records-room badge that allows reading and changing entries.
- **In the online store:** It could be granted to a trusted operations group that needs to correct order or inventory records.

### `roles/spanner.viewer`
- **What it is:** A predefined role for viewing Spanner resource information, such as instances and databases. It does not grant permission to read or edit database contents.
- **Analogy:** A visitor can see the room directory but cannot open the filing cabinets.
- **In the online store:** It could let support staff see which Spanner resources exist without viewing customer orders.

### Google group
- **What it is:** A managed list of individual user accounts. Granting a role to the group gives its members that access; each person still signs in as themselves.
- **Analogy:** An office team list used to issue the same badge to its current members.
- **In the online store:** A `spanner-operators@shopnow.example` group can hold the three staff members who need database access.

### `gcloud`
- **What it is:** Google's command-line tool for managing Cloud resources.
- **Analogy:** A text-based control desk for the cloud administrator.
- **In the online store:** An administrator could use it to inspect role details or change IAM policy.

### `gcloud iam roles describe`
- **What it is:** A command that shows metadata and permissions for an IAM role. It does not grant that role to anyone.
- **Analogy:** Looking up what an office badge permits; it does not issue the badge.
- **In the online store:** The administrator can inspect the Spanner role before deciding whether it fits the backend operators.

### Project and `--project my-project`
- **What it is:** A project is a Google Cloud container for resources and settings. The `--project` flag tells a command which project to use for a project-scoped operation or role lookup.
- **Analogy:** A project is a company department's labeled office space; the flag identifies which department to look in.
- **In the online store:** `shopnow-prod` could contain the production Spanner instance.

### How the terms fit together

```text
Google group (three people)
          │ receives a role binding
          ▼
Cloud Spanner instance / database
          │ contains
          ▼
Tables and their data

roles/spanner.databaseUser → read and write table data
roles/spanner.viewer       → view resource details, not table data
```

## 3. 🌍 Real-World Scenario

A company has three operations staff who need to correct order records in its Spanner database. The cloud administrator grants the database access role to one team group. When staff join or leave, the administrator updates the group membership instead of changing the resource policy for each person.

## 4. 🔍 Option-by-Option Breakdown

### ✅ B — Correct

> **B.** Run gcloud iam roles describe roles/spanner.databaseUser. Add the users to a new group. Add the group to the role.

`roles/spanner.databaseUser` fits the stated need to read and edit table data. A group is a manageable way to give the three users the same access. The `describe` command only inspects the role; the actual granting step is an IAM policy binding on the Spanner instance or database.

**📌 When to use it:** Use it when a team needs the same permission to read and change records.
**🏢 Office example:** Give the records team one shared team badge, then update the team list when staff change.

### ❌ A

> **A.** Run gcloud iam roles describe roles/spanner.databaseUser. Add the users to the role.

The role matches read-and-edit access, but assigning it separately to each person is harder to manage as the team changes. Also, a role is not a membership list: the administrator grants a role to users or groups through a resource's IAM policy. The `describe` command itself only shows role details.

**📌 When to use it:** Use it when one named person needs this access and there is no team to manage.
**🏢 Office example:** Give one records clerk their own badge when only that clerk needs to change entries.

### ❌ C

> **C.** Run gcloud iam roles describe roles/spanner.viewer --project my-project. Add the users to the role.

`roles/spanner.viewer` does not grant access to read or edit table data; it is for viewing Spanner resource information. The project flag scopes the role description lookup, but it does not change what the role permits. Direct user assignment also makes a changing team harder to maintain. The command only describes the role.

**📌 When to use it:** Use it when people only need to see which database rooms exist.
**🏢 Office example:** Let reception read the directory of records rooms without opening the cabinets.

### ❌ D

> **D.** Run gcloud iam roles describe roles/spanner.viewer --project my-project. Add the users to a new group. Add the group to the role.

Using a group is helpful, but the viewer role still cannot provide the requested table-data access. It does not let members read or edit the database contents. The `describe` command only displays the role's details.

**📌 When to use it:** Use it when a team needs to see the names and details of database resources only.
**🏢 Office example:** Give the reception team one directory badge so they can direct visitors to the right records room.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow's backend API uses a Cloud Spanner database for order and inventory records. Three operations engineers need to inspect and correct those records. The administrator puts them in `spanner-operators@shopnow.example` and grants `roles/spanner.databaseUser` to that group on the appropriate Spanner database or instance. When an engineer leaves, the administrator removes that person from the group.

The storefront frontend does not need this human operator role. Its backend should use its own carefully scoped identity. For production systems, consider whether fine-grained database access can limit which tables or actions a person may use; `roles/spanner.databaseUser` includes schema update access as well as data read/write access.

## 6. 🧠 Key Takeaway / Memory Tip

If the question says **read and edit Spanner data**, think `roles/spanner.databaseUser`; if it says **view resource details only**, think `roles/spanner.viewer`. For several people with the same access, grant the role to a group and manage membership there.

**Current documentation:** [Spanner IAM overview](https://docs.cloud.google.com/spanner/docs/iam), [Spanner roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner), and [gcloud iam roles describe](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe).

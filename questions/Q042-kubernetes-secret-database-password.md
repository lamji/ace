# Q042: Keeping a Database Password Out of a Kubernetes Deployment

**Topic:** GKE / Kubernetes (Secrets vs ConfigMaps, container images, persistent volumes)

## ❓ Question

The screenshot's question number is cropped. The following snippet shows the relevant part of the Deployment configuration:

```yaml
- name: main-container
  image: gcr.io/my-company-repo/myapp1:1.4
  env:
    - name: DB_PASSWORD
      value: "t0ugh2guess!"
  ports:
    - containerPort: 8080
```

> You need to refactor this configuration so that the database password is not stored in plain text. You want to follow Google-recommended practices. What should you do?
>
> **A.** Store the database password inside the Docker image of the container, not in the YAML file.
>
> **B.** Store the database password inside a Secret object. Modify the YAML file to populate the DB_PASSWORD environment variable from the Secret.
>
> **C.** Store the database password inside a ConfigMap object. Modify the YAML file to populate the DB_PASSWORD environment variable from the ConfigMap.
>
> **D.** Store the database password in a file inside a Kubernetes persistent volume, and use a persistent volume claim to mount the volume to the container.

**My answer:** B
**Correct answer:** B — Store the database password inside a Secret object. Modify the YAML file to populate the DB_PASSWORD environment variable from the Secret.
**Result:** ✅ Correct

---

## 1. ✅ Verdict

**Correct — your answer is B.** Kubernetes Secrets are designed to hold sensitive values such as passwords. The Deployment can reference the Secret key and provide its value to the container as `DB_PASSWORD`, rather than embedding the password directly in the Deployment YAML.

A Secret is safer and more manageable than putting the password in a Deployment or image, but it is not magic encryption: Kubernetes Secret values are base64-encoded in the API representation. In GKE, customer content stored at rest is encrypted by default, and access should still be restricted. For a production GKE application, Google's current guidance generally prefers an external secret manager such as Secret Manager when practical.

## 2. 📖 What the Question Is Asking

In plain words: the application needs a password to connect to its database, but the password is written directly into a Kubernetes Deployment configuration. Where should the password live, and how should the container receive it?

- **“database password”** is sensitive information.
- **“not stored in plain text”** means do not leave the literal password in an ordinary Deployment YAML file or image.
- **“Google-recommended practices”** points to separating credentials from application configuration and using a secret-handling feature.
- **Exam topic:** Kubernetes configuration and secrets in GKE.

## 2.5 📚 Key Terms Explained

### Google Kubernetes Engine (GKE)
- **What it is:** Google's managed Kubernetes service for running containerized applications.
- **Analogy:** A managed office building where your team's applications work in separate rooms.
- **In the online store:** GKE can run the store's order API and other backend services.

### Kubernetes
- **What it is:** A system for running and managing containerized applications across a cluster of machines.
- **Analogy:** An office coordinator that assigns work to machines and keeps the application running.
- **In the online store:** Kubernetes runs and replaces the store's backend containers as needed.

### YAML file
- **What it is:** A human-readable text format often used to describe Kubernetes resources and their settings.
- **Analogy:** A written instruction sheet for setting up a workstation.
- **In the online store:** The Deployment YAML describes how the store's API container should run.

### Deployment
- **What it is:** A Kubernetes resource that describes an application and maintains the requested number of running copies of it.
- **Analogy:** A staffing plan that says how many workers should be on shift.
- **In the online store:** This Deployment manages two copies of the `myapp1` service.

### Container image / Docker image
- **What it is:** A packaged application and its dependencies used to start a container. Image layers can persist and be copied to registries or machines.
- **Analogy:** A boxed workstation kit that can be copied many times.
- **In the online store:** The `myapp1:1.4` image contains the API application. It should not contain a database password.

### Container
- **What it is:** A running instance of an application created from an image.
- **Analogy:** A workstation assembled from the boxed kit.
- **In the online store:** The container runs the order API process.

### Database password
- **What it is:** A secret credential used to prove the application is allowed to connect to a database.
- **Analogy:** A key or passcode to a locked records room.
- **In the online store:** The order service may need a credential to connect to its database.

### Environment variable (`DB_PASSWORD`)
- **What it is:** A named value supplied to a running process. The application reads it at runtime. Environment variables can still be exposed to processes or tools with sufficient access, so permissions and logging matter.
- **Analogy:** A private note placed at a worker's station when the shift starts.
- **In the online store:** The API process can read `DB_PASSWORD` when it connects to the database.

### Kubernetes Secret object
- **What it is:** A Kubernetes API object intended to hold sensitive values such as passwords. A Pod can consume a Secret as an environment variable or mounted file.
- **Analogy:** A locked credential envelope issued only to staff who need it.
- **In the online store:** A Secret can provide the order service with its database password.

### ConfigMap object
- **What it is:** A Kubernetes API object for non-confidential configuration, such as a log level or service URL. It is not meant to protect passwords.
- **Analogy:** A public notice board for ordinary instructions, not a locked drawer.
- **In the online store:** A ConfigMap could hold the API's non-secret setting for the database hostname.

### Persistent volume (PV)
- **What it is:** Storage made available to workloads in a Kubernetes cluster, often backed by a disk or another storage system. A volume is not automatically a secure secret store.
- **Analogy:** A shared filing cabinet or disk kept for a long time.
- **In the online store:** A PV might hold application files that must persist when a container is replaced.

### Persistent volume claim (PVC)
- **What it is:** A request by a Kubernetes workload for storage from a persistent volume.
- **Analogy:** A requisition asking facilities for a particular cabinet or storage space.
- **In the online store:** A PVC can request storage for a service that needs files to remain after a Pod restarts.

### Plain text and base64 encoding
- **What they are:** Plain text is directly readable text. Base64 changes how text is represented but is not encryption and does not hide a password from someone who can decode it.
- **Analogy:** Base64 is like writing a note in a predictable code that anyone can translate; encryption is like locking the note with a key.
- **In the online store:** Never treat a base64-encoded password in a manifest as protected from readers of that manifest.

### How the pieces fit together

```text
Kubernetes Secret (DB_PASSWORD value)
              │ referenced by key
              ▼
Deployment YAML ── injects value as DB_PASSWORD ──> application container
                                                   │
                                                   ▼
                                              database login
```

## 3. 🌍 Real-World Scenario

A developer commits a Deployment YAML file to a shared source repository. If the database password is written directly in that file, everyone who can read the repository may learn it, and it can remain in the repository's history even after the file is changed. A Secret separates the sensitive value from the app's Deployment instructions and lets the cluster provide it to the workload.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A

> **A.** Store the database password inside the Docker image of the container, not in the YAML file.

**Why it is wrong:** A container image is a packaged artifact that can be copied, cached, pushed to a registry, scanned, and downloaded by users or systems with image access. A password baked into an image can remain in its layers and in old image versions even after the password is changed. This also ties credential rotation to rebuilding and redeploying the application image. Moving a secret from YAML into an image does not make it secret; it can make exposure broader and harder to clean up.

**When it is useful:** Container images are for application code and dependencies that can safely be shared wherever that app runs, not credentials.

📌 When to use it: Use it when you need to package application files that are safe to copy.  
🏢 Office example: Put standard forms and the office phone list in every staff handbook, but keep door codes out of it.

### ✅ B — Correct

> **B.** Store the database password inside a Secret object. Modify the YAML file to populate the DB_PASSWORD environment variable from the Secret.

**Why it is correct:** A Kubernetes Secret is the resource intended for sensitive values such as passwords. The Deployment YAML can refer to a Secret by name and key using `valueFrom.secretKeyRef`; the literal password no longer needs to appear in the Deployment's container `env.value` field. This separates credential management from the application image and from ordinary deployment settings. The application continues reading `DB_PASSWORD`, so the app can keep its existing environment-variable interface while Kubernetes supplies the value from the Secret.

A configuration example looks like this:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: myapp-db-credentials
        key: password
```

The Secret itself should be managed carefully. Kubernetes encodes Secret values as base64 in API/YAML representations; base64 is not encryption. Don't commit a manifest containing the actual password to a repository. Restrict Secret access with least-privilege permissions, and protect the password from application logs or debugging output. GKE encrypts customer content at rest by default. For stronger centralized management and rotation in production, Google recommends considering Secret Manager integration.

**When it is useful:** Use a Kubernetes Secret when a Pod needs a sensitive value and a suitable external secret-management integration is not being used.

📌 When to use it: Use it when a program needs a private password or key while it runs.  
🏢 Office example: Keep a door code in a locked envelope and give it only to the staff member who needs it.

### ❌ C

> **C.** Store the database password inside a ConfigMap object. Modify the YAML file to populate the DB_PASSWORD environment variable from the ConfigMap.

**Why it is wrong:** ConfigMaps hold ordinary, non-sensitive configuration. They do not provide the intended protection boundary for passwords. Referencing a ConfigMap instead of writing the value directly in the Deployment may tidy up the YAML, but it does not make the password appropriately protected. The prompt specifically asks how to handle a database password following recommended practice; use a Secret for that, not a ConfigMap.

**When it is useful:** Use a ConfigMap for settings that are not confidential, such as a display name, feature flag, or database hostname.

📌 When to use it: Use it when an application needs ordinary instructions that are safe for the team to read.  
🏢 Office example: Put the printer name and meeting-room hours on a shared notice board.

### ❌ D

> **D.** Store the database password in a file inside a Kubernetes persistent volume, and use a persistent volume claim to mount the volume to the container.

**Why it is wrong:** A persistent volume is durable storage, not a secrets-management feature. A file containing the password can still be read by anyone or any workload with access to that volume, may be copied into backups, and requires extra storage and mount configuration. A PVC only requests storage; it does not encrypt or control access to the password by itself. Kubernetes can mount a Secret as a file if the application needs file-based credentials, but the credential should still originate from a Secret or external secret manager, not an ordinary persistent volume.

**When it is useful:** Use persistent volumes for application data that must remain available after a Pod is replaced, not as the first choice for passwords.

📌 When to use it: Use it when an application must keep its own files after its work computer is replaced.  
🏢 Office example: Store an employee's ongoing project files in a managed cabinet that stays when their desk computer is swapped.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow's order API runs in a GKE container and needs a password to connect to its database. Put the credential in a Kubernetes Secret named `myapp-db-credentials`, then have the Deployment map its `password` key to the container's `DB_PASSWORD` variable. Keep the literal value out of the Deployment and out of the container image. Limit which workload and administrators can read the Secret, and avoid printing the value in logs. For production systems, consider storing the source credential in Secret Manager and exposing it to GKE using the Secret Manager integration.

## 6. 🧠 Key Takeaway / Memory Tip

**Password or key → Secret; ordinary setting → ConfigMap.** Never bake passwords into a container image or treat a persistent disk as a secret manager. Remember that base64 is encoding, not encryption.

**Current documentation:** [GKE security hardening practices](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster), [Use Secret Manager with GKE](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component), [Kubernetes Secret good practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/), and [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/).

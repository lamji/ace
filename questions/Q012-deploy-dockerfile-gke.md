# Q012: Deploying a Dockerfile to Kubernetes Engine (GKE)

**Topic:** GKE / containers (Dockerfile → image → registry → Deployment YAML → kubectl)

## ❓ Question
> You have a Dockerfile that you need to deploy on Kubernetes Engine. What should you do?
>
> **A.** Use kubectl app deploy <dockerfilename>.
>
> **B.** Use gcloud app deploy <dockerfilename>.
>
> **C.** Create a docker image from the Dockerfile and upload it to Container Registry. Create a Deployment YAML file to point to that image. Use kubectl to create the deployment with that file.
>
> **D.** Create a docker image from the Dockerfile and upload it to Cloud Storage. Create a Deployment YAML file to point to that image. Use kubectl to create the deployment with that file.

**My answer:** C
**Correct answer:** C
**Result:** ✅ Correct

---

## 📖 What the Question Is Asking

**In plain words:** You have a **Dockerfile** (a recipe for packaging your app). You want to run the app on **GKE (Kubernetes)**. What are the correct steps?

| Keyword | What it hints at |
|---|---|
| "**Dockerfile**" | It's only a **recipe**. You must **build an image** from it first |
| "**Kubernetes Engine**" | You deploy with **kubectl** + a **Deployment YAML** (not `gcloud app deploy`, which is App Engine) |
| (implied) | Kubernetes **pulls images from a container registry**, not from Cloud Storage |

**The 3-step pattern:** **Build** the image → **Push** it to a registry → **Deploy** with kubectl + YAML.

**Exam topic:** GKE, specifically **deploying containerized applications**.

⚠️ **Update:** **Container Registry** (`gcr.io`) is **deprecated and was shut down in 2025**. Its replacement is **Artifact Registry** (`*-docker.pkg.dev`). The steps are exactly the same. On a newer exam, choose the **Artifact Registry** option.

---

## 📚 Key Terms Explained

### 1️⃣ Container
- **What it is:** A **package** that holds your app **plus everything it needs** to run (code, libraries, runtime). It runs the same way on any machine.
- **Analogy:** 🍱 A **packed lunch box**: the food, utensils, and sauce all in one box. It's the same meal wherever you open it.
- **In the online store:** The ShopNow Orders API (Node.js + its libraries) packed into one container.

### 2️⃣ Docker and the Dockerfile
- **Docker:** The most popular tool for **building and running containers**.
- **Dockerfile:** A text file with **step-by-step instructions** for building a container image ("start from Node 20, copy my code, install libraries, start the server").
- **Analogy:** 📝 A **recipe card** for the lunch box. It's not food yet, just the instructions.
- **In the online store:**
  ```dockerfile
  FROM node:20-slim
  WORKDIR /app
  COPY package*.json ./
  RUN npm ci --omit=dev
  COPY . .
  EXPOSE 8080
  CMD ["node", "server.js"]
  ```

### 3️⃣ Docker Image
- **What it is:** The **built result** of a Dockerfile: a ready-to-run, read-only package. You build it once (`docker build`) and run it anywhere.
- **Analogy:** 🍱 The **finished, sealed lunch box**, cooked from the recipe and ready to hand out.
- **In the online store:** `orders-api:v1`, the built Orders API image.

### 4️⃣ Container Registry / Artifact Registry
- **What it is:** A **storage service made specifically for container images**. Kubernetes **pulls** images from here when it starts your app.
  - **Container Registry** (`gcr.io/...`): the **old** service (deprecated and shut down).
  - **Artifact Registry** (`asia-southeast1-docker.pkg.dev/...`): the **current** service.
- **Analogy:** 🏪 The company's **central pantry** for sealed lunch boxes. Every branch knows to pick up meals here.
- **In the online store:** `asia-southeast1-docker.pkg.dev/shopnow-prod/shopnow-repo/orders-api:v1`

### 5️⃣ Kubernetes and GKE
- **Kubernetes:** A system that **runs and manages containers** across many machines: it starts them, restarts crashed ones, and scales them.
- **GKE (Google Kubernetes Engine):** Google's **managed Kubernetes**. Google runs the control plane for you.
- **Analogy:** 🚢 A **cargo ship captain** deciding where each container goes and replacing broken ones.
- **In the online store:** The `shopnow-gke` cluster runs the storefront, Orders API, and Payments API containers.

### 6️⃣ Pod
- **What it is:** The **smallest unit** in Kubernetes: one (or a few tightly linked) running containers.
- **Analogy:** 🧑‍🍳 One **cook at a station**, preparing meals from the lunch box recipe.

### 7️⃣ Deployment and the Deployment YAML
- **Deployment:** A Kubernetes object that says, *"Run **N copies** (Pods) of **this image**, and keep them running."* It also handles rolling updates.
- **YAML file:** The text file where you write the Deployment's settings (which image, how many replicas, which ports).
- **Analogy:** 📋 An **order form** for the branch manager: "Serve **3** of lunch box **orders-api:v1**, and replace any that go bad."

### 8️⃣ kubectl
- **What it is:** The **command-line tool for Kubernetes** (review from Q005). `kubectl apply -f deployment.yaml` (or `kubectl create -f`) sends the YAML to the cluster.

### 9️⃣ `gcloud app deploy` and Cloud Storage (why they appear in the wrong options)
- **`gcloud app deploy`:** Deploys to **App Engine** (review from Q009), a **different product** from GKE.
- **Cloud Storage:** Stores **files** (images, backups, review from Q006). Kubernetes **can't pull container images from a bucket**.

### 🔗 How They Fit Together
```
📝 Dockerfile (recipe)
     │  ① docker build  (or: gcloud builds submit)
     ▼
🍱 Docker image: orders-api:v1 (sealed lunch box)
     │  ② docker push
     ▼
🏪 Artifact Registry (formerly Container Registry)   ← Kubernetes pulls from HERE
     ▲
     │  ④ GKE pulls the image
📋 deployment.yaml  "run 3 replicas of .../orders-api:v1"
     │  ③ kubectl apply -f deployment.yaml
     ▼
🚢 GKE cluster ──► 🧑‍🍳 Pod  🧑‍🍳 Pod  🧑‍🍳 Pod   (3 running copies)
```

---

## 🌍 Real-World Scenario

A developer finishes a new version of an app and gives you its **Dockerfile**. Your job as the cloud engineer is to run it on the company's **GKE cluster**. Kubernetes doesn't understand Dockerfiles directly. It runs **images** that it **pulls from a registry**, following the instructions in a **YAML file**.

So the standard pipeline (often automated in CI/CD with **Cloud Build**) is always: **build → push → deploy**.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** Use kubectl app deploy <dockerfilename>.

**Why it's wrong:**
- ❌ **`kubectl app deploy` doesn't exist.** kubectl has commands like `apply`, `create`, `get`, and `delete`, but no `app deploy`.
- ❌ Kubernetes can't run a **Dockerfile** directly anyway. It needs a **built image** from a registry.
- ⚠️ **Trap option:** it mixes up `kubectl` with `gcloud app deploy`.

**📌 When to use it:** **Never use this.** The command doesn't exist. Use option C (build → push → kubectl apply).
🏢 **Office example:** Like asking the receptionist to file a form that the company **doesn't have**. Nothing happens.

### ❌ B
> **B.** Use gcloud app deploy <dockerfilename>.

**Why it's wrong:**
- ❌ `gcloud app deploy` deploys to **App Engine**, **not** Kubernetes Engine. Wrong product.
- ❌ (App Engine *flexible* can use a Dockerfile, but the question says **Kubernetes Engine**.)

**📌 When to use it:** Use it when you want to put your app in **App Engine**, where Google handles everything for you.
🏢 **Office example:** Sending your work to a **fully serviced office building** that sets everything up for you. It's a different building from the one you were asked to use.

### ✅ C
> **C.** Create a docker image from the Dockerfile and upload it to Container Registry. Create a Deployment YAML file to point to that image. Use kubectl to create the deployment with that file.

**Why it's correct:**
- ✔️ **Build the image** from the Dockerfile, since Kubernetes runs images, not Dockerfiles.
- ✔️ **Push it to Container Registry**, a registry that Kubernetes can **pull** images from. (Today, **Artifact Registry**.)
- ✔️ **Write a Deployment YAML** that points to the image's address in the registry.
- ✔️ **Use kubectl** to create the Deployment, and GKE starts the Pods.

**📌 When to use it:** Use it when you want to **run your app on Kubernetes**: package it, store it in the official place, then give the instructions.
🏢 **Office example:** **Packing a ready-made kit**, storing it in the company's **official supply room**, then giving the branch manager an **order form** saying how many kits to set up.

### ❌ D
> **D.** Create a docker image from the Dockerfile and upload it to Cloud Storage. Create a Deployment YAML file to point to that image. Use kubectl to create the deployment with that file.

**Why it's wrong:**
- ❌ **Cloud Storage is not a container registry.** Kubernetes **can't pull** container images from a storage bucket.
- ❌ The Deployment would fail with an **image pull error** (`ErrImagePull` / `ImagePullBackOff`).
- ⚠️ **Trap option:** everything else is correct. Only the **storage location** is wrong.

**📌 When to use it:** Use Cloud Storage when you want to store **files** like documents, photos, or backups, **not** app packages for Kubernetes.
🏢 **Office example:** The **general storage room** for boxes and files. It's fine for documents, but the branch can't order kits from it.

---

## 🛒 E-Commerce Full-Stack Example

A ShopNow developer finished **Orders API v1** and handed you its Dockerfile. Deploy it to the `shopnow-gke` cluster.

```
👩‍💻 Developer ──Dockerfile──► 🛠️ docker build ──► 🏪 Artifact Registry
                                                        │ pull
                                                        ▼
🛍️ Shoppers ──► 🚦 Load Balancer ──► 🚢 GKE: orders-api Pods ×3 ──► 🗄️ Cloud SQL
```

**① Create a Docker repository in Artifact Registry (one time):**
```bash
gcloud artifacts repositories create shopnow-repo \
  --repository-format=docker \
  --location=asia-southeast1
gcloud auth configure-docker asia-southeast1-docker.pkg.dev
```

**② Build and push the image:**
```bash
docker build -t asia-southeast1-docker.pkg.dev/shopnow-prod/shopnow-repo/orders-api:v1 .
docker push asia-southeast1-docker.pkg.dev/shopnow-prod/shopnow-repo/orders-api:v1

# (Alternative: Cloud Build does both steps in Google Cloud)
# gcloud builds submit --tag asia-southeast1-docker.pkg.dev/shopnow-prod/shopnow-repo/orders-api:v1
```
*(In the old exam's Container Registry, the address looked like `gcr.io/shopnow-prod/orders-api:v1`.)*

**③ Write `deployment.yaml` pointing to that image:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: orders-api
  template:
    metadata:
      labels:
        app: orders-api
    spec:
      containers:
      - name: orders-api
        image: asia-southeast1-docker.pkg.dev/shopnow-prod/shopnow-repo/orders-api:v1
        ports:
        - containerPort: 8080
```

**④ Connect to the cluster and create the Deployment with kubectl:**
```bash
gcloud container clusters get-credentials shopnow-gke --region=asia-southeast1
kubectl apply -f deployment.yaml
kubectl get pods            # 3 orders-api Pods → Running ✅

# Let shoppers reach it through a load balancer
kubectl expose deployment orders-api --type=LoadBalancer --port=80 --target-port=8080
```

**🎬 With the wrong options:**
- **A:** `kubectl app deploy` → `error: unknown command`. ❌
- **B:** `gcloud app deploy` → the API ends up on **App Engine**, not in the GKE cluster where the team runs everything else. ❌
- **D:** The image is in a Cloud Storage bucket → Pods show `ImagePullBackOff`, and the Orders API never starts. **Checkout is down.** ❌

---

## 🧠 Key Takeaways / Memory Tips

- **Dockerfile → GKE = Build → Push (registry) → Deploy (YAML + kubectl).**
  🧠 *"**Recipe → Lunch box → Pantry → Order form.**"*
- **Kubernetes pulls images from a container registry**: **Artifact Registry** (current) / Container Registry (old, shut down). **Never from Cloud Storage.**
- **`gcloud app deploy` = App Engine. `kubectl apply` = Kubernetes.** Match the tool to the product.
- **`kubectl app deploy` doesn't exist.** Watch for made-up commands.
- Commands to remember:
  | Command | What it does |
  |---|---|
  | `docker build -t IMAGE .` | Build an image from the Dockerfile |
  | `docker push IMAGE` | Upload the image to a registry |
  | `gcloud builds submit --tag IMAGE` | Build **and** push using Cloud Build |
  | `gcloud container clusters get-credentials CLUSTER` | Connect kubectl to a GKE cluster |
  | `kubectl apply -f deployment.yaml` | Create/update the Deployment |
  | `kubectl expose deployment NAME --type=LoadBalancer` | Make it reachable from the internet |

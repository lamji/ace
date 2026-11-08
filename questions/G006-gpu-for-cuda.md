# G006: PyTorch Training That Depends on Custom CUDA Kernels (GPUs, Not TPUs)

**Topic:** Compute Engine (GPUs vs TPUs)
**Exam guide section:** 2.1 Planning compute resources: Identifying whether to use GPUs or TPUs

> 🧾 Practice question written from the official exam guide (not from the question site).

## ❓ Question
> Your data science team trains a PyTorch model that depends on custom CUDA kernels written by the team. They want to speed up training on Compute Engine. What should you do?
>
> **A.** Attach NVIDIA GPUs to the training VMs.
>
> **B.** Attach Cloud TPUs, because TPUs run every machine learning framework and custom kernel faster.
>
> **C.** Switch the VMs to a compute-optimized machine type with more vCPUs and no accelerators.
>
> **D.** Add Local SSDs to the VMs to speed up the model's math operations.

**My answer:** — (not tried yet)
**Correct answer:** A
**Result:** ⏳ Not tried yet

---

## 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A data science team trains an AI model in PyTorch (a popular AI coding library). Part of their code is custom CUDA (NVIDIA's programming system for running math on NVIDIA graphics chips).
- **What you must achieve:** Make training faster on Compute Engine VMs.
- **The limits:** The custom CUDA code must keep working.
- **What they're really asking:** Which kind of accelerator chip can actually run CUDA code?

**Clues in the question:**
- "**custom CUDA kernels**": CUDA runs only on **NVIDIA GPUs**. TPUs don't run CUDA.
- "**speed up training**": you need an accelerator, not just more CPUs or faster disks.

**Exam topic:** Compute choice: GPUs vs TPUs (exam guide sections 2.1 and 3.1).

---

## 📚 Key Terms Explained

### 1. GPU 🔑
- **What it is:** A graphics processing unit: a chip with thousands of small cores for parallel math. It's widely used for AI, and it supports CUDA and most frameworks.
- **Looks like:** `gcloud compute instances create trainer --machine-type=g2-standard-8 --accelerator=type=nvidia-l4,count=1 --maintenance-policy=TERMINATE`
- **Not to be confused with:** A TPU, which is Google's own AI chip, programmed through XLA, not CUDA.
- **Analogy:** 🧰 A general toolbox that fits most jobs.
- **In the online store:** Fine-tuning the product-description model.

### 2. TPU
- **What it is:** Tensor Processing Unit: Google-designed chips specialised for the large matrix math in neural networks. Best with JAX/TensorFlow (and PyTorch through XLA) at large scale.
- **Looks like:** TPU slice `v5e-16` in GKE or TPU VMs
- **Not to be confused with:** A GPU. TPUs can't run CUDA kernels.
- **Analogy:** 🏭 A factory line built for one product, very fast at it.
- **In the online store:** Training a huge language model from scratch.

### 3. CUDA kernel
- **What it is:** A small program written for NVIDIA GPUs using CUDA.
- **Looks like:** `__global__ void fused_attention(...)`
- **Not to be confused with:** Generic Python code.
- **Analogy:** 🔌 A plug that only fits one brand of socket.
- **In the online store:** The team's custom attention layer.

### 🔗 How they fit together
```
 PyTorch + custom CUDA kernels ──► needs NVIDIA GPU ✅
                               ╳──► TPU (no CUDA)
```

---

## 🌍 Real-World Scenario

A retailer's data team wrote a custom CUDA layer to speed up their search-ranking model. Training on CPUs takes days. Attaching **NVIDIA GPUs** cuts it to hours. TPUs would need a rewrite away from CUDA.

---

## 🔍 Option-by-Option Breakdown

### ✅ A
> **A.** Attach NVIDIA GPUs to the training VMs.

**Why it's correct:**
- ✔️ "**NVIDIA GPUs**" matches "**custom CUDA kernels**": CUDA runs on NVIDIA GPUs.
- ✔️ GPUs give large parallel speed-ups for PyTorch training, which matches "**speed up training**".

📌 **When to use it:** Use it when the AI code needs the common graphics chips that most tools are written for.
🏢 **Office example:** Renting the standard power tools that every contractor's attachments fit.

### ❌ B
> **B.** Attach Cloud TPUs, because TPUs run every machine learning framework and custom kernel faster.

**Wrong words:**
- ❌ "**TPUs run every machine learning framework and custom kernel faster**": false. TPUs don't run CUDA kernels, so the team's code wouldn't work without a rewrite.

📌 **When to use it:** Use TPUs when training very large models in frameworks built for them, without CUDA-specific code.
🏢 **Office example:** A specialised factory line that only builds one kind of product.

### ❌ C
> **C.** Switch the VMs to a compute-optimized machine type with more vCPUs and no accelerators.

**Wrong words:**
- ❌ "**more vCPUs and no accelerators**": CPUs are much slower than GPUs for this math, and the CUDA kernels can't run at all without a GPU.

📌 **When to use it:** Use it for CPU-heavy work like batch processing or game servers.
🏢 **Office example:** Hiring more office clerks to do a job that needs a machine.

### ❌ D
> **D.** Add Local SSDs to the VMs to speed up the model's math operations.

**Wrong words:**
- ❌ "**Local SSDs … speed up the model's math**": disks speed up reading data, not calculations.

📌 **When to use it:** Use it when the job waits on fast temporary disk access.
🏢 **Office example:** A faster filing cabinet doesn't make the accountant add faster.

---

## 🛒 E-Commerce Full-Stack Example

**ShopNow** search ranking:
- Training VM `g2-standard-24` with 2× NVIDIA L4 GPUs, run nightly as a Spot VM to save money.
- The model is then served on Cloud Run with GPU, or on GKE.

---

## 🧠 Key Takeaways / Memory Tips

- **CUDA or broad framework support → GPU. Huge matrix-heavy training in JAX/TF at scale → TPU.**
  🧠 *"**CUDA? GPU. Giant JAX? TPU.**"*
- Related: **Q081**, **Q312**, **G007**.

# Q048: Displaying Cloud Storage PDFs in a browser

**Topic:** Cloud Storage object metadata (`Content-Type`) and public access

## ❓ Question
> You host a static website on Cloud Storage. Recently, you began to include links to PDF files on this site. Currently, when users click on the links to these PDF files, their browsers prompt them to save the file onto their local system. Instead, you want the clicked PDF files to be displayed within the browser window directly, without prompting the user to save the file locally. What should you do?
>
> **A.** Enable Cloud CDN on the website frontend.
>
> **B.** Enable “Share publicly” on the PDF file objects.
>
> **C.** Set Content-Type metadata to application/pdf on the PDF file objects.
>
> **D.** Add a label to the storage bucket with a key of Content-Type and value of application/pdf.

**My answer:** B  
**Correct answer:** C — Set Content-Type metadata to application/pdf on the PDF file objects.  
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **B** is understandable: a website visitor needs permission to access a PDF. But the question says users can already click the link and receive the file. The issue is how the browser handles the response, not whether the object is publicly accessible.

**Correct answer: C — Set Content-Type metadata to application/pdf on the PDF file objects.** `Content-Type` tells the browser what kind of content it received. When the object is labeled as a PDF, browsers can recognize it and commonly display it in their built-in PDF viewer instead of treating it as an unknown file type. This assumes the object is accessible and no `Content-Disposition: attachment` response header is forcing a download. Google's documentation describes `Content-Type` as metadata that lets browsers render objects properly. [Cloud Storage object metadata](https://docs.cloud.google.com/storage/docs/metadata)

## 2. 📖 What the Question Is Asking

**In plain words:**
- **The situation:** A static website (fixed files, no server code) is hosted in Cloud Storage and links to PDF files. Clicking a PDF makes the browser download it instead of showing it.
- **What you must achieve:** Show the PDFs inside the browser window.
- **The limits:** None stated.
- **What they're really asking:** What setting on the PDF files tells the browser to display them?

Clues:
- **“users click on the links”**: they can reach the object.
- **“prompt them to save”**: the problem is the browser's handling of the response.
- **“displayed within the browser window”**: the browser needs the correct content type to identify the file as a PDF.

**Exam domain:** Cloud Storage static website hosting and object metadata.

## 2.5 📚 Key Terms Explained

### Static website
- **What it is:** A website served as prebuilt files, such as HTML, CSS, images, and PDFs, without generating each page through a server-side application.
- **Analogy:** A display board made from finished printed pages.
- **In the online store:** Static product information pages or help documents can be stored as website files.

### Cloud Storage bucket and object
- **What it is:** A bucket is a container for files in Cloud Storage. Each stored file is an object.
- **Analogy:** A filing cabinet is the bucket; each document in it is an object.
- **In the online store:** A bucket can contain product images, downloadable manuals, and static site files.

### PDF
- **What it is:** A Portable Document Format file, commonly used for documents that should keep the same layout across devices.
- **Analogy:** A digital version of a printed handout.
- **In the online store:** The store may provide a product manual or return form as a PDF.

### Browser
- **What it is:** An app such as Chrome or Firefox that requests and displays websites and files.
- **Analogy:** A window through which a person reads documents and views a website.
- **In the online store:** Shoppers use a browser to view product pages and PDF manuals.

### Metadata
- **What it is:** Information stored about an object that describes or affects how it is handled, in addition to the object's file contents.
- **Analogy:** A label attached to a folder describing what's inside and how to handle it.
- **In the online store:** Metadata on an image or PDF can tell the browser what kind of file it receives.

### `Content-Type` / media type
- **What it is:** An object's metadata value sent in the HTTP response to identify the kind of content, such as `application/pdf` for a PDF. Browsers use it to decide how to handle or render the response.
- **Analogy:** The document type written on a folder so the receptionist knows whether it is a form, picture, or report.
- **In the online store:** Setting a manual's content type to `application/pdf` helps a shopper's browser recognize it as a PDF.

### `application/pdf`
- **What it is:** The standard media type identifying PDF content.
- **Analogy:** A clearly marked “PDF document” tag.
- **In the online store:** Use this value on PDF manuals or forms so browsers identify them correctly.

### “Share publicly” / public access
- **What it is:** Permission that allows people on the internet to read an object without signing in, subject to bucket and organization settings.
- **Analogy:** Putting a document in a public reading room instead of a locked cabinet.
- **In the online store:** A public product manual can be read by shoppers without an account. This controls who can read it, not whether a browser displays or downloads it.

### Cloud CDN
- **What it is:** A content delivery network that caches and serves content closer to users to improve delivery speed.
- **Analogy:** Keeping copies of popular documents at nearby office branches instead of fetching every copy from headquarters.
- **In the online store:** Cloud CDN can speed up delivery of product images and other static assets, but it doesn't correct a PDF's content type.

### Bucket label
- **What it is:** A key-value tag on a cloud resource used to organize or filter resources. It is not the same as an object's fixed `Content-Type` metadata.
- **Analogy:** A colored sticker used to sort a filing cabinet, not instructions attached to each document.
- **In the online store:** A bucket label such as `department=web` can help organize resources; it won't tell a shopper's browser that a specific object is a PDF.

### How the pieces fit

```text
Browser requests PDF link
        ↓
Cloud Storage checks access permission
        ↓
Cloud Storage returns object plus Content-Type metadata
        ↓
Browser recognizes application/pdf and can render the PDF inline
```

Public access answers **“may this visitor read it?”** `Content-Type` answers **“what kind of content is this?”**

## 3. 🌍 Real-World Scenario

A communications team publishes a public website with PDF forms. Visitors can fetch the files, but their browsers download them rather than opening them in the tab. The cloud engineer checks the object metadata and sets each PDF's `Content-Type` to `application/pdf`. If public visitors could not access the file at all, that would be a separate permissions issue.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A

> **A.** Enable Cloud CDN on the website frontend.

**Why it is wrong:** Cloud CDN can cache website content and serve it from locations closer to users, which may improve delivery speed. It does not identify a PDF's media type and does not, by itself, change whether a browser renders the object inline or treats it as a download. The question asks to change the browser's handling, so changing delivery/caching is not the relevant fix.

📌 When to use it: Use it when people far away need website files delivered more quickly.  
🏢 Office example: Keep copies of frequently used office forms at nearby branches so staff can get them faster.

### ❌ B — Your answer

> **B.** Enable “Share publicly” on the PDF file objects.

**Why it is wrong:** Public sharing changes **who can read** an object: it permits unauthenticated visitors to access it, if public access is allowed by the bucket and organization. It does not tell the browser that the file is a PDF or instruct it to display the file inline. Since users are already clicking the links and receiving a save prompt, the question indicates that access is working; the missing piece is the object's content type. Making a file public unnecessarily can also expose it to everyone on the internet. [Google's public access instructions describe public sharing as granting public read access](https://docs.cloud.google.com/storage/docs/making-data-public).

📌 When to use it: Use it when anyone should be able to read a document without signing in.  
🏢 Office example: Put an approved public brochure in the lobby for every visitor to read.

### ✅ C — Correct

> **C.** Set Content-Type metadata to application/pdf on the PDF file objects.

**Why it is correct:** `Content-Type` is object metadata that Cloud Storage returns with the file. Setting it to `application/pdf` identifies the response as a PDF, allowing compatible browsers to display it in their built-in PDF viewer. Set the metadata on the **PDF objects**, because each file has its own content type. Google's documentation says the `Content-Type` value lets browsers render objects properly. [Cloud Storage object metadata](https://docs.cloud.google.com/storage/docs/metadata).

A practical caveat: if the response also has `Content-Disposition: attachment`, that header can still tell the browser to download the file. This exam question's intended fix is the PDF `Content-Type`; in a real troubleshooting case, inspect both response headers if it continues downloading.

📌 When to use it: Use it when a browser needs to recognize what kind of file it received.  
🏢 Office example: Mark a document folder “PDF” so the receptionist knows to open it with the PDF viewer.

### ❌ D

> **D.** Add a label to the storage bucket with a key of Content-Type and value of application/pdf.

**Why it is wrong:** A bucket label is an organizational tag attached to the bucket resource. It is not the fixed `Content-Type` metadata returned with each object. Even if the bucket is labeled `Content-Type=application/pdf`, the browser won't receive that label as the file's media type. The metadata must be set on each PDF object (or on objects as they are uploaded).

📌 When to use it: Use it when you need to sort or identify a storage cabinet for staff.  
🏢 Office example: Add a “Legal” sticker to a filing cabinet; it won't label every paper inside as a contract.

## 5. 🛒 E-Commerce Full-Stack Example

An online store keeps product manuals in a Cloud Storage bucket and links to them from product pages. Each manual object should have `Content-Type: application/pdf`, so shoppers' browsers can recognize the file and display it in a PDF viewer. The store must separately grant the intended audience access to those manuals; public access controls readership, while content type describes the file. Cloud CDN could help deliver popular manuals faster, but it is not the setting that identifies them as PDFs.

## 6. 🧠 Key Takeaway / Memory Tip

Remember: **permissions decide who can read; `Content-Type` tells the browser what it is reading.** If the link works but the browser handles the file incorrectly, check the object's metadata, especially `Content-Type` and, in real troubleshooting, `Content-Disposition`.

**Current Google Cloud documentation:** [Object metadata](https://docs.cloud.google.com/storage/docs/metadata), [Making data public](https://docs.cloud.google.com/storage/docs/making-data-public), and [Cloud CDN overview](https://docs.cloud.google.com/cdn/docs/overview).

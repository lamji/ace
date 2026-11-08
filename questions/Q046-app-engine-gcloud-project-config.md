# Q046: Finding the Project Used by an App Engine Deployment

**Topic:** App Engine + Google Cloud CLI (`gcloud` project configuration)

## ❓ Question
> You deployed an App Engine application using gcloud app deploy, but it did not deploy to the intended project. You want to find out why this happened and where the application deployed. What should you do?
>
> **A.** Check the app.yaml file for your application and check project settings.
>
> **B.** Check the web-application.xml file for your application and check project settings.
>
> **C.** Go to Deployment Manager and review settings for deployment of applications.
>
> **D.** Go to Cloud Shell and run gcloud config list to review the Google Cloud configuration used for deployment.

**My answer:** A
**Correct answer:** D — Go to Cloud Shell and run gcloud config list to review the Google Cloud configuration used for deployment.
**Result:** ❌ Incorrect

---

## 1. ❌ Verdict

Your answer **A** is understandable because `app.yaml` is an important App Engine file. It describes the application's service/runtime settings, though, rather than choosing the Google Cloud project to receive a deployment.

**Correct answer: D — Go to Cloud Shell and run `gcloud config list` to review the Google Cloud configuration used for deployment.** By default, `gcloud app deploy` targets the project set in the active Google Cloud CLI configuration. If that project differs from the intended project, the app can land in the wrong place. A command-line `--project` flag can override the configured default.

**Small accuracy note:** `gcloud config list` displays the active configuration now. If someone changed the active configuration after the deployment, its output may not prove which project that earlier deployment used. Check the deploy command for an explicit `--project` flag and verify the application or deployment audit records in the candidate projects.

## 2. 📖 What the Question Is Asking

**In plain words:**
- **The situation:** You ran gcloud app deploy, but the app went to the wrong project.
- **What you must achieve:** Find out why and where it actually went.
- **The limits:** None stated.
- **What they're really asking:** What should you check to see which project gcloud was using?

- **“did not deploy to the intended project”** points to the selected project, not the application's runtime settings.
- **“using gcloud app deploy”** points to the Google Cloud CLI's active project configuration or an explicit `--project` override.
- **“why this happened and where”** means inspect the configuration that selected the target project.
- **Exam topic:** App Engine deployment and Google Cloud CLI configurations.

## 2.5 📚 Key Terms Explained

### App Engine
- **What it is:** Google Cloud's managed platform for deploying applications without managing the underlying VMs directly.
- **Analogy:** Renting a managed office service where the building owner handles much of the infrastructure.
- **In the online store:** App Engine can host the storefront API or a small web service.

### `gcloud`
- **What it is:** Google's command-line tool for managing Google Cloud resources and deployments.
- **Analogy:** A control desk where an operator gives instructions to the cloud.
- **In the online store:** A developer uses it to deploy the store's App Engine service.

### `gcloud app deploy`
- **What it is:** A command that uploads and deploys an App Engine application or service configuration to a Google Cloud project.
- **Analogy:** Sending the completed office setup instructions to a particular branch for installation.
- **In the online store:** It publishes a version of a store service to App Engine.

### Google Cloud project
- **What it is:** A named container that owns Google Cloud resources and settings. App Engine applications belong to projects.
- **Analogy:** A labeled company branch or department where resources are kept.
- **In the online store:** `shop-prod` might contain the production App Engine application; `shop-test` might contain staging.

### Active configuration
- **What it is:** The currently selected named set of Google Cloud CLI settings, including account and default project.
- **Analogy:** The currently selected company profile on an operator's control desk.
- **In the online store:** A developer might activate the `production` configuration before deploying the live service.

### `gcloud config list`
- **What it is:** A command that displays properties in the active Google Cloud CLI configuration, including the current account and `core/project` when set.
- **Analogy:** Reading the currently selected branch and operator from the control desk.
- **In the online store:** It helps reveal whether the CLI is set to `shop-prod` or a different project.

### `--project` flag
- **What it is:** A command-line option that selects a project for one invocation and can override the configured default.
- **Analogy:** Writing a one-time delivery address on a package, even if the office's default address is different.
- **In the online store:** `gcloud app deploy --project=shop-prod` directs that deployment to `shop-prod`.

### `app.yaml`
- **What it is:** An App Engine configuration file for an application service, including settings such as runtime and handlers. It does not normally set the Google Cloud project targeted by `gcloud app deploy`.
- **Analogy:** An instruction sheet for how to arrange a room, not the branch address where it should be delivered.
- **In the online store:** It can describe how the store's App Engine service runs.

### `web-application.xml`
- **What it is:** The option refers to a Java web-application deployment descriptor, commonly named `web.xml` in Java web apps. It configures web-application behavior, not the Google Cloud project selected for `gcloud app deploy`.
- **Analogy:** A room's internal rules, not the address of the office receiving the shipment.
- **In the online store:** A Java-based store service might use a web descriptor for application behavior, but it won't choose `shop-prod` versus `shop-test`.

### Deployment Manager
- **What it is:** Google Cloud's infrastructure-as-code service for deploying and managing supported cloud resources from configuration files. It is not the normal tool for deploying App Engine application code with `gcloud app deploy`.
- **Analogy:** A facilities team that builds office infrastructure, not the staff member who publishes the website.
- **In the online store:** Infrastructure templates may provision supporting resources, while `gcloud app deploy` publishes the App Engine service.

### Cloud Shell
- **What it is:** A browser-based command-line environment in the Google Cloud console that includes Google Cloud CLI tools.
- **Analogy:** A cloud-accessible operator desk.
- **In the online store:** A developer can inspect CLI settings or deploy a service from Cloud Shell.

### How the pieces fit together

```text
Active gcloud configuration ── default project ──┐
                                                 ├──> gcloud app deploy target project
Optional --project flag ── overrides default ────┘

app.yaml → how the App Engine service is configured
```

## 3. 🌍 Real-World Scenario

A developer works on both test and production versions of a website. The active CLI configuration still points to the test project, so a plain `gcloud app deploy` sends the app there. Checking `gcloud config list` reveals the default project and account. The developer can then switch to the production configuration or specify `--project` for a one-time deployment.

## 4. 🔍 Option-by-Option Breakdown

### ❌ A — Your answer

> **A.** Check the app.yaml file for your application and check project settings.

**Why it is wrong:** `app.yaml` is relevant to App Engine, which is why A looks plausible. It configures the service—such as runtime and request handlers—but generally does not select which Google Cloud project receives `gcloud app deploy`. Looking at it may help check what was deployed, but it doesn't directly reveal the CLI's active default project. The relevant setting is the active `gcloud` configuration's `core/project`, or an explicit `--project` flag on the deploy command.

**When it is useful:** Check `app.yaml` when the application is deploying to the right project but running with the wrong runtime or service settings.

📌 When to use it: Use it when you need to check how an application is set up to run.  
🏢 Office example: Check the room setup sheet when the right office received the delivery but the room was arranged incorrectly.

### ❌ B

> **B.** Check the web-application.xml file for your application and check project settings.

**Why it is wrong:** A Java web-application descriptor (usually named `web.xml`) configures behavior inside a Java web app. It is not the Google Cloud CLI setting that picks a project. It also might not exist for this application or runtime. The deployment target is selected by the active `gcloud` project setting or an explicit project flag.

**When it is useful:** Check a Java web descriptor when you need to inspect web-app behavior, such as servlet mappings or filters.

📌 When to use it: Use it when a Java website's internal rules need checking.  
🏢 Office example: Read a department's work instructions when the correct branch received the package but staff follow the wrong procedure.

### ❌ C

> **C.** Go to Deployment Manager and review settings for deployment of applications.

**Why it is wrong:** Deployment Manager is for managing cloud infrastructure from templates; it is not the setting that chooses the target project for `gcloud app deploy`. This option sends you to a different deployment tool and does not inspect the CLI configuration used by the command. The key is to see which project the active `gcloud` configuration selected, and whether the deployment command overrode it.

**When it is useful:** Use Deployment Manager when you need to define and manage supported cloud infrastructure from templates.

📌 When to use it: Use it when facilities need a written plan to build or change office infrastructure.  
🏢 Office example: Use the facilities plan to lay out new rooms, rather than to find out where a website was published.

### ✅ D — Correct

> **D.** Go to Cloud Shell and run gcloud config list to review the Google Cloud configuration used for deployment.

**Why it is correct:** `gcloud config list` displays the active CLI configuration, including the default project property when set. `gcloud app deploy` uses that configured project by default, so a wrong `core/project` explains how the app could deploy to the wrong project. A deploy command can also use `--project`, which overrides the configured default for that command. Thus, to determine the actual destination, inspect the active configuration and the original deploy command. Cloud Shell is convenient, but the same CLI command can be run in another terminal with the same active configuration.

Example checks:

```bash
gcloud config list
gcloud config configurations list
```

The first shows properties in the active configuration; the second shows named configurations and which one is active. If the active project is wrong, set it with `gcloud config set project PROJECT_ID`, activate the intended named configuration, or specify `--project=PROJECT_ID` on the deployment. If the configuration has changed since deployment, verify the destination in App Engine or the project's audit records.

**When it is useful:** Use it when you need to confirm which account and project the command line is currently using.

📌 When to use it: Use it when you need to check which office branch the control desk is set to.  
🏢 Office example: Read the selected branch on the operator's screen before sending the next package.

## 5. 🛒 E-Commerce Full-Stack Example

ShopNow has a test project, `shop-test`, and a production project, `shop-prod`. A developer runs `gcloud app deploy` while the active `gcloud` configuration still points to `shop-test`, so the new storefront version lands there. Running `gcloud config list` shows the active project's default. The developer should verify whether the original command included `--project`, then activate the production configuration or deploy with `--project=shop-prod`.

The `app.yaml` file still matters: it describes the App Engine service's runtime and behavior. But it doesn't usually choose between the test and production projects.

## 6. 🧠 Key Takeaway / Memory Tip

If `gcloud app deploy` targets the wrong project, check **the active `gcloud` project setting and any `--project` override**. Remember: **`app.yaml` describes the app; `gcloud` configuration selects the default project.**

**Current documentation:** [Deploying App Engine applications](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app), [Managing gcloud configurations](https://docs.cloud.google.com/sdk/docs/configurations), [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy), and [App Engine `app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

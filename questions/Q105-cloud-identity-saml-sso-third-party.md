# Q105: Users Sign In With the Company's SAML SSO (Third-Party IdP, Google as Service Provider)

**Topic:** Identity (Cloud Identity, SAML SSO, identity provider vs service provider, OAuth)

## ❓ Question
> Your company has a single sign-on (SSO) identity provider that supports Security Assertion Markup Language (SAML) integration with service providers. Your company has users in Cloud Identity. You would like users to authenticate using your company's SSO provider. What should you do?
>
> **A.** In Cloud Identity, set up SSO with Google as an identity provider to access custom SAML apps.
>
> **B.** In Cloud Identity, set up SSO with a third-party identity provider with Google as a service provider.
>
> **C.** Obtain OAuth 2.0 credentials, configure the user consent screen, and set up OAuth 2.0 for Mobile & Desktop Apps.
>
> **D.** Obtain OAuth 2.0 credentials, configure the user consent screen, and set up OAuth 2.0 for Web Server Applications.

**My answer:** — (didn't know)
**Correct answer:** B
**Result:** ❓ Didn't know

---

## 📖 What the Question Is Asking

**In plain words:** Your company already has a login system (SSO). You want users to sign in to Google with **that** system. How do you set it up?

**Clues in the question:**
- "**your company's SSO provider**" = the **identity provider (IdP)** that checks passwords.
- "**users in Cloud Identity**" + "**authenticate using your company's SSO**": Google must **trust** the company IdP. Google becomes the **service provider (SP)**.
- OAuth 2.0 is for **apps asking permission** to access data, not for company sign-in.

**Exam topic:** Identity / IAM.

---

## 📚 Key Terms Explained

### 1. Identity provider (IdP) vs service provider (SP) 🔑
- **What it is:** The **IdP** checks who you are (asks for the password). The **SP** is the app you want to use, and it trusts the IdP's answer.
- **Looks like:** IdP: Okta / Azure AD / ADFS. SP: Google Cloud console.
- **Not to be confused with:** each other. Here the company system is the IdP and Google is the SP.
- **Analogy:** 🪪 The **HR desk** issues and checks ID (IdP); the **building guard** trusts the HR badge (SP).
- **In the online store:** ShopNow staff sign in to Google with their Okta login.

### 2. SAML SSO
- **What it is:** A standard way for the IdP to send a **signed "this person is verified" message** to the SP, so users log in once.
- **Looks like:** Cloud Identity Admin → Security → SSO with third-party IdP → sign-in URL + certificate
- **Not to be confused with:** OAuth.
- **Analogy:** 📨 A signed note from HR saying "this is Ana".
- **In the online store:** One login for email, Google Cloud and the HR system.

### 3. OAuth 2.0
- **What it is:** A standard that lets an **app get permission to access a user's data** (the "Allow this app to see your Drive?" screen).
- **Looks like:** OAuth client ID + consent screen
- **Not to be confused with:** company-wide sign-in (SSO).
- **Analogy:** 🔑 Giving a valet a key that only starts the car.
- **In the online store:** A ShopNow app that reads a seller's Google Sheet.

### 🔗 How they fit together
```
 user → console.cloud.google.com (Google = SERVICE PROVIDER)
          └─► redirected to company SSO (IDENTITY PROVIDER: Okta/ADFS)
                 └─► password + MFA ✓ → SAML assertion → Google lets user in ✅
```

---

## 🌍 Real-World Scenario

A company uses Okta for all logins. After moving to Google Cloud, it doesn't want a second password. The admin configures **Cloud Identity → SSO with a third-party IdP**, entering Okta's sign-in URL and certificate. Now Google sends users to Okta to log in.

---

## 🔍 Option-by-Option Breakdown

### ❌ A
> **A.** In Cloud Identity, set up SSO with Google as an identity provider to access custom SAML apps.

**Wrong words:**
- ❌ "**Google as an identity provider**": that's the reverse direction. Google would check passwords for other apps, but the question wants the **company SSO** to check them.

📌 **When to use it:** Use it when Google accounts should log users in to other company apps.
🏢 **Office example:** Making the building guard issue badges for HR, when HR already issues them.

### ✅ B
> **B.** In Cloud Identity, set up SSO with a third-party identity provider with Google as a service provider.

**Why it's correct:**
- ✔️ "**a third-party identity provider**" matches "**your company's SSO provider**": the company system checks passwords.
- ✔️ "**Google as a service provider**" matches "**users in Cloud Identity**": Google trusts the company login for those users.
- ✔️ "**In Cloud Identity, set up SSO**" matches "**supports … SAML integration with service providers**": SAML SSO is set up in Cloud Identity.

📌 **When to use it:** Use it when the company already has one login system and Google should accept it.
🏢 **Office example:** The building guard accepts the badge that HR already issues.

### ❌ C
> **C.** Obtain OAuth 2.0 credentials, configure the user consent screen, and set up OAuth 2.0 for Mobile & Desktop Apps.

**Wrong words:**
- ❌ "**OAuth 2.0 for Mobile & Desktop Apps**": this lets an app ask for access to data. It doesn't make Google use your company login.

📌 **When to use it:** Use it when you build a phone or desktop app that needs a user's Google data.
🏢 **Office example:** Giving an app a valet key: nothing to do with the front-door badge.

### ❌ D
> **D.** Obtain OAuth 2.0 credentials, configure the user consent screen, and set up OAuth 2.0 for Web Server Applications.

**Wrong words:**
- ❌ "**OAuth 2.0 for Web Server Applications**": same problem as C, just for web apps.

📌 **When to use it:** Use it when your web app needs permission to access users' Google data.
🏢 **Office example:** A web app asking to read your calendar: still not company sign-in.

---

## 🛒 E-Commerce Full-Stack Example

ShopNow's staff use Okta. In **Cloud Identity Admin → Security → Authentication → SSO with third-party IdP**, the admin enters:
- Sign-in page URL: `https://shopnow.okta.com/app/google/sso/saml`
- Okta's signing certificate

Ana opens the Cloud console, types `ana@shopnow.com`, is sent to Okta, logs in with MFA, and lands back in Google Cloud.

---

## 🧠 Key Takeaways / Memory Tips

- **Company SSO checks passwords → third-party IdP; Google = service provider.**
- **OAuth = app permissions, not SSO.**
  🧠 *"**Company logs you in, Google trusts it.**"*
- Related: **Q109** (sync users from Active Directory), **Q083** (Workspace users).

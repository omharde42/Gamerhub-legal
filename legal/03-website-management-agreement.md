# GAMERHUB WEBSITE MANAGEMENT & HANDLING AGREEMENT

**Document Version:** 1.0
**Effective Date:** [DATE]
**Entity / Project Name:** GamerHub (`[LEGAL ENTITY NAME]`)
**Jurisdiction:** [GOVERNING LAW / JURISDICTION]

---

## ⚠️ LEGAL NOTICE & DISCLAIMER

**THIS DOCUMENT IS A PROJECT GOVERNANCE AND AGREEMENT DRAFT AND SHOULD BE REVIEWED BY A QUALIFIED LAWYER IN THE APPLICABLE JURISDICTION BEFORE BEING RELIED UPON AS A BINDING LEGAL AGREEMENT.**

---

## 1. PARTIES & SCOPE

This Website Management Agreement defines the operational duties, security boundaries, and approval workflows for **Purvesh Bhadale** in his role as **Website Handling & Management Lead** for GamerHub, under the executive oversight of **Yash** (Founder) and **Om Harde** (Co-Founder).

---

## 2. DUTIES & RESPONSIBILITIES

Purvesh Bhadale shall perform the following website handling and operational tasks:
* **Content Management:** Publishing, editing, updating, and maintaining text, imagery, banners, news articles, and promotional graphics on the GamerHub website.
* **Basic Administration:** Moderating user comments, managing routine CMS plug-ins/addons (subject to technical approval), and ensuring web pages display correctly.
* **UI Content Maintenance:** Ensuring marketing campaign banners, game announcements, and event schedules are accurate and up-to-date.
* **Issue Reporting:** Monitoring website availability, reporting broken links, performance slowdowns, UI glitches, or security anomalies immediately to the Founder (Yash) and Co-Founder (Om Harde).

---

## 3. ACCESS LEVEL & CREDENTIAL GRANTS

* **CMS Manager Access:** Purvesh Bhadale shall be granted content-manager level credentials to the GamerHub website CMS / Admin Dashboard.
* **Restricted Infrastructure Access:** Purvesh Bhadale shall **NOT** be granted direct root access to:
  - Production servers (SSH / AWS EC2 / VPS root keys).
  - Production databases (SQL / MongoDB database admin connection strings).
  - Primary Domain Registrar accounts (DNS / Nameserver controls).
  - Production payment gateways or financial accounts.
* All administrative access is conditional upon active role status and may be modified or revoked at any time by the Founder or Co-Founder.

---

## 4. IP NON-TRANSFER REQUIREMENT

Performing website management, publishing content, configuring pages, or administering web dashboards does **NOT** transfer any ownership of GamerHub, its source code, databases, trademarks, domain names, UI designs, or intellectual property to Purvesh Bhadale or any third party. All web assets remain exclusive GamerHub IP under `legal/02-ip-ownership-agreement.md`.

---

## 5. MANDATORY MAJOR CHANGE APPROVAL WORKFLOW

Purvesh Bhadale must receive explicit written approval (via documented pull request approval, official team messaging, or signed email) from the Founder (Yash) or Co-Founder (Om Harde) prior to making any of the following major changes:

1. **Branding & Logos:** Altering primary site logos, official color schemes, taglines, or legal disclaimers.
2. **Payment Integrations:** Modifying checkout flows, payment gateways, donation links, pricing schedules, or subscription settings.
3. **Authentication & User Data:** Modifying login/signup flows, privacy policy links, user registration forms, or database user fields.
4. **Security & System Configuration:** Modifying security headers, SSL/TLS settings, firewall rules, or admin user permissions.
5. **Database & API Structures:** Modifying backend API endpoints, script tags, database schemas, or embedding third-party tracking scripts.
6. **Infrastructure & Domain:** Modifying DNS records, domain redirects, hosting plans, or web server configurations.

---

## 6. WEBSITE SECURITY & COMPLIANCE RULES

Purvesh Bhadale agrees to adhere strictly to the following security mandates:
* **No Malicious Code:** Never intentionally introduce malicious code, backdoors, hidden redirect scripts, unauthorized tracking code, or unverified third-party plugins.
* **No Disabling Security Controls:** Never disable web application firewalls, SSL certificates, rate limiters, or authentication mechanisms.
* **Credential Protection:** Store administrative credentials exclusively in approved password managers; multi-factor authentication (2FA) is mandatory on all admin accounts.
* **Data Minimization:** Never export, scrape, copy, or share private user data, email lists, or site analytics with unauthorized third parties.
* **No Unauthorized Transfer:** Never transfer control, admin rights, or web access permissions to any external third party without written authorization.

---

## 7. SIGNATURE BLOCKS

**Founder**
Name: Yash
Role: Founder, GamerHub
Signature: _____________________________________  Date: __________________

**Co-Founder**
Name: Om Harde
Role: Co-Founder, GamerHub
Signature: _____________________________________  Date: __________________

**Website Management Lead**
Name: Purvesh Bhadale
Role: Marketing & Website Management
Signature: _____________________________________  Date: __________________

---

## 8. DOCUMENT VERSION CONTROL

* **Document Name:** GamerHub Website Management Agreement
* **Ref:** `legal/03-website-management-agreement.md` | **Version:** 1.0 | **Date:** [DATE]

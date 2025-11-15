# Security Policy

## 🔐 Reporting a Vulnerability
If you discover a security vulnerability in **Nexus-Flux**, please **DO NOT open a public issue**.

Instead, report it via our official security channel:

📩 **security@ikaffanan.com**

We take all security reports seriously and will respond as quickly as possible.

---

## 🛡 Supported Versions
Security updates will be provided for:

- The latest stable release (v1.x)
- The main branch (active development)

Older versions may not receive patches.

---

## 🧪 Responsible Disclosure Guidelines
When reporting a vulnerability, please include:

- A clear description of the issue
- Steps to reproduce (if applicable)
- Potential impact
- Suggested fixes (optional)

Please allow us **up to 72 hours** to investigate and respond before any public disclosure.

---

## 🔧 Security Hardening Recommendations
For users deploying Nexus-Flux:

### ✔ Run in isolated environments
Use containers or virtual environments to prevent cross-process access.

### ✔ Protect your API keys
Nexus-Flux relies on LLM API keys. Keep them secure and never commit them to Git.

### ✔ Configure Firewalls
If running the API, restrict inbound access to trusted networks.

### ✔ Monitor Logs
Use tools like Prometheus, Grafana, or Datadog to monitor timeline anomalies.

### ✔ Use HTTPS
Always expose the API behind HTTPS or a secure reverse proxy.

---

## 🧩 Ecosystem Security
Nexus-Flux includes:
- Multi-agent decision logic
- Vector-space computations
- Optional Redis backend

If you modify these components, make sure to:
- Validate input sizes
- Sanitize metadata
- Avoid unsafe execution in PragmaticAgent

---

## 🛡 Maintainers
Security policies and patches are managed by:

**YEO Kaffanan Issa** — Creator & Lead Architect  
**IKAFFANAN LTD (United Kingdom)** — Official maintainer and security sponsor

---

Thank you for helping keep **Nexus-Flux** safe, reliable, and trustworthy.
# Kubernetes Security Audit Tool
![Audit CI](https://github.com/Amir23156/k8s-security-audit-tool/actions/workflows/audit.yml/badge.svg)

# Kubernetes Security Audit Tool

A lightweight command-line tool that scans Kubernetes YAML manifests for **common security misconfigurations**.  
Inspired by tools like [MKAT](https://github.com/datadog/managed-kubernetes-auditing-tool), but built for **local audits**, **learning**, and easy integration into **DevSecOps pipelines**.

---

## Features

**Scans Kubernetes YAML or Helm manifests**  
**Detects common security issues**, including:

- **Privileged containers**
- **Missing CPU or memory resource limits**
- **Containers not configured to run as non-root**
- **Use of hostPath volumes**
- **Services of type NodePort**
- **hostNetwork enabled**

**CI/CD Ready**
- Fully integrated with **GitHub Actions** CI pipeline  
- Fails pipeline on **high severity** issues
- Generates audit reports in:
  -  **Markdown** (for readability)
  -  **HTML** (for GitHub Pages publishing)

 **GitHub Pages Deployment**
- Latest security audit reports are **automatically published** to [GitHub Pages](https://amir23156.github.io/k8s-security-audit-tool)

 **Fast & Extensible**
- Modular rule engine makes it easy to add more checks
- Works locally without external dependencies beyond `pyyaml` and `pandoc`

---

## Getting Started

```bash
git clone https://github.com/Amir23156/k8s-security-audit-tool.git
cd k8s-security-audit-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python audit.py --dir manifests/ --output text


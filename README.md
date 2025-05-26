# Kubernetes Security Audit Tool

A lightweight command-line tool that scans Kubernetes YAML manifests for common security misconfigurations.  
Built for local use, CI/CD pipelines, and educational DevSecOps workflows.

---

##  Features

-  Detects:
  - Privileged containers
  - Missing resource limits
  - Run-as-root containers
  - hostNetwork usage
  - NodePort services
  - hostPath volumes
-  Outputs: text, JSON, Markdown, and HTML
-  CI integrated (GitHub Actions)
-  Live audit report via [GitHub Pages](https://amir23156.github.io/k8s-security-audit-tool/)
-  [Dockerized version](https://hub.docker.com/r/amir23156/k8s-audit-tool) for easy use anywhere

---

## Run with Docker

```bash
docker run --rm -v $(pwd)/manifests:/app/manifests amir23156/k8s-audit-tool:latest --dir manifests/ --output markdown
```

---

## Example Report

![image](https://github.com/user-attachments/assets/8d40db02-337f-4b81-a72c-f9a87d1f2682)


---

## Local Setup

```bash
git clone https://github.com/Amir23156/k8s-security-audit-tool.git
cd k8s-security-audit-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python audit.py --dir manifests/ --output text
```

---

## GitHub Actions Workflow

- Automatically runs audit on push
- Builds report in Markdown and HTML
- Publishes latest audit to GitHub Pages
- Optionally deploys a Docker image

---

## Docker Build (for development)

```bash
docker build -t k8s-audit-tool .
```

```bash
docker run --rm -v $(pwd)/manifests:/app/manifests k8s-audit-tool --dir manifests/ --output markdown
```

---

## GitHub Badges

[![CI](https://github.com/Amir23156/k8s-security-audit-tool/actions/workflows/deploy.yml/badge.svg)](https://github.com/Amir23156/k8s-security-audit-tool/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/amir23156/k8s-audit-tool)](https://hub.docker.com/r/amir23156/k8s-audit-tool)
[![Live Report](https://img.shields.io/badge/report-live-blue)](https://amir23156.github.io/k8s-security-audit-tool/)

---

## Author

Made with Love by [Amir23156](https://github.com/Amir23156)

---

##  Topics

`kubernetes` • `security` • `devsecops` • `docker` • `ci-cd` • `yaml` • `cloud-native`

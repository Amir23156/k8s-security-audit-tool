# Kubernetes Security Audit Tool
![Audit CI](https://github.com/Amir23156/k8s-security-audit-tool/actions/workflows/audit.yml/badge.svg)

A command-line tool that scans Kubernetes YAML or Helm manifests for common security misconfigurations.   Inspired by tools like MKAT, but designed for fast local use and educational DevSecOps workflows.

## Features
- Detects:
  - Privileged containers
  - Missing resource limits
  - HostPath volumes
  - Run as root
  - NodePort services
- Outputs a list of risky resources
- Easy to integrate in CI/CD

# Kubernetes Security Audit Tool
A command-line tool that scans Kubernetes YAML or Helm manifests for common security misconfigurations.   Inspired by tools like Datadog MKAT, but designed for fast local use and educational DevSecOps workflows.

## Features
- Detects:
  - Privileged containers
  - Missing resource limits
  - HostPath volumes
  - Run as root
  - NodePort services
- Outputs a list of risky resources
- Easy to integrate in CI/CD

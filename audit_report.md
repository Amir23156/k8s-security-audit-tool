| Severity | Issue | File | Resource |
|----------|-------|------|----------|
| High | Privileged container is enabled | manifests/insecure.yaml | test-pod |
| Medium | Container is not configured to run as non-root | manifests/insecure.yaml | test-pod |
| Medium | Missing CPU or memory resource limits | manifests/insecure.yaml | test-pod |
| Medium | Container is not configured to run as non-root | manifests/insecure.yaml | test-deployment |
| Medium | Missing CPU or memory resource limits | manifests/insecure.yaml | test-deployment |
| Medium | Container is not configured to run as non-root | manifests/insecure.yaml | limitless-pod |
| Medium | Missing CPU or memory resource limits | manifests/insecure.yaml | limitless-pod |
| Medium | Container is not configured to run as non-root | manifests/insecure.yaml | host-network-pod |
| Medium | Missing CPU or memory resource limits | manifests/insecure.yaml | host-network-pod |
| High | hostNetwork is enabled (container shares host network stack) | manifests/insecure.yaml | host-network-pod |

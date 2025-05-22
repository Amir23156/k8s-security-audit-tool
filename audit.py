import yaml
import os

def scan_file(path):
    with open(path, 'r') as f:
        docs = list(yaml.safe_load_all(f))
        for doc in docs:
            if not doc or 'kind' not in doc:
                continue
            kind = doc.get("kind", "")
            metadata = doc.get("metadata", {})
            spec = doc.get("spec", {})

            if kind == "Pod" or kind == "Deployment":
                containers = spec.get("containers", []) if kind == "Pod" else spec.get("template", {}).get("spec", {}).get("containers", [])
                for container in containers:
                    security_context = container.get("securityContext", {})
                    if security_context.get("privileged", False):
                        print(f"[!] Privileged container found in {metadata.get('name')}")

if __name__ == "__main__":
    path = "manifests/insecure.yaml"
    scan_file(path)

def run_as_non_root_check(doc, file_path, resource_name):
    issues = []

    kind = doc.get("kind", "")
    spec = doc.get("spec", {})

    # Get containers based on resource kind
    containers = []
    if kind == "Pod":
        containers = spec.get("containers", [])
    elif kind in ["Deployment", "ReplicaSet", "StatefulSet", "DaemonSet", "Job", "CronJob"]:
        containers = (
            spec.get("template", {})
            .get("spec", {})
            .get("containers", [])
        )

    for container in containers:
        name = container.get("name", "<unnamed>")
        security_context = container.get("securityContext", {})

        if not security_context.get("runAsNonRoot", False):
            issues.append({
                "file": file_path,
                "resource": resource_name,
                "container": name,
                "issue": "Container is not configured to run as non-root",
                "severity": "Medium"
            })

    return issues

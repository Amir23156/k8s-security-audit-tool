def resources_limits_check(doc, file_path, resource_name):
    issues = []

    kind = doc.get("kind", "")
    spec = doc.get("spec", {})

    # Get containers based on kind
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
        resources = container.get("resources", {})
        limits = resources.get("limits", {})

        if not limits.get("cpu") or not limits.get("memory"):
            issues.append({
                "file": file_path,
                "resource": resource_name,
                "container": name,
                "issue": "Missing CPU or memory resource limits",
                "severity": "Medium"
            })

    return issues

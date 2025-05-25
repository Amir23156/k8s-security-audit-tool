def host_network_check(doc, file_path, resource_name):
    issues = []

    kind = doc.get("kind", "")
    spec = doc.get("spec", {})

    # Pod: hostNetwork is directly under spec
    # Controllers: hostNetwork is under template.spec
    host_network = False
    if kind == "Pod":
        host_network = spec.get("hostNetwork", False)
    elif kind in ["Deployment", "ReplicaSet", "StatefulSet", "DaemonSet", "Job", "CronJob"]:
        host_network = (
            spec.get("template", {})
            .get("spec", {})
            .get("hostNetwork", False)
        )

    if host_network:
        issues.append({
            "file": file_path,
            "resource": resource_name,
            "issue": "hostNetwork is enabled (container shares host network stack)",
            "severity": "High"
        })

    return issues

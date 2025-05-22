import os
import yaml
from audit.rules import privileged_check, run_as_non_root_check  # Add more rules as you implement them


def load_manifests_from_dir(directory):
    yaml_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                yaml_files.append(os.path.join(root, file))
    return yaml_files


def scan_file(file_path):
    issues = []
    try:
        with open(file_path, "r") as f:
            docs = list(yaml.safe_load_all(f))

        for doc in docs:
            if not isinstance(doc, dict):
                continue
            kind = doc.get("kind")
            metadata = doc.get("metadata", {})
            name = metadata.get("name", "Unnamed resource")

            # Apply rules
            issues += privileged_check(doc, file_path, name)
            issues += run_as_non_root_check(doc, file_path, name)

    except Exception as e:
        issues.append({"file": file_path, "issue": f"Failed to parse: {str(e)}", "severity": "Error"})

    return issues


def scan_directory(directory):
    results = []
    files = load_manifests_from_dir(directory)
    for file_path in files:
        results.extend(scan_file(file_path))
    return results


def print_report(issues):
    if not issues:
        print("No security issues found.")
    for issue in issues:
        print(f"[{issue['severity']}] {issue['issue']} in {issue['file']} (resource: {issue['resource']})")

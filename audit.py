import argparse
from audit.scanner import scan_directory, print_report
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kubernetes Security Audit Tool")
    parser.add_argument("--dir", default="manifests/", help="Directory containing YAML files")
    parser.add_argument("--output", default="text", choices=["text", "json"], help="Output format")
    args = parser.parse_args()

    results = scan_directory(args.dir)

    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print_report(results)


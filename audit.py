from audit.scanner import scan_directory, print_report

if __name__ == "__main__":
    directory = "manifests"
    results = scan_directory(directory)
    print_report(results)

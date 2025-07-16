from app.cloud_scanner import scan_terraform

issues = scan_terraform("sample_tf")

for file_path, warning in issues:
    print(f"{file_path}: {warning}")
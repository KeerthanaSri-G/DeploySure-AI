import argparse
import os

def start_scan(config_path):
    if not os.path.exists(config_path):
        print(f"❌ File '{config_path}' not found!")
        return

    print(f"🔍 Scan started for: {config_path}")

    with open(config_path, 'r') as file:
        content = file.read()

        # Basic pre-checks
        if "password" in content.lower():
            print("⚠️ Warning: Hardcoded password found.")

        if "0.0.0.0" in content:
            print("⚠️ Warning: Open access (0.0.0.0) detected.")

        if "admin" in content.lower():
            print("⚠️ Warning: 'admin' keyword found – potential risk.")

        print("✅ Basic scan completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DeploySure-AI: Cloud Config Scanner")
    parser.add_argument("config_path", type=str, help="Path to the cloud config file")
    args = parser.parse_args()
    start_scan(args.config_path)
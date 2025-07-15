```python
import os
from pathlib import Path

AWS_CRED_PATH = Path.home() / ".aws" / "credentials"
AWS_CONFIG_PATH = Path.home() / ".aws" / "config"

def check_file(path, name):
    if path.exists():
        print(f"[✓] Found {name} at {path}")
        if not os.access(path, os.R_OK):
            print(f"  ⚠️  Cannot read {name} — check permissions!")
    else:
        print(f"[x] {name} not found.")

def main():
    print("🔍 AWS Credential Check Tool")
    check_file(AWS_CRED_PATH, "credentials file")
    check_file(AWS_CONFIG_PATH, "config file")
    print("✅ Scan complete.")

if __name__ == "__main__":
    main()

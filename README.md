# aws-credential-checker
Scans local machine for insecure AWS credential storage
# AWS Credential Checker 🔐

This Python script scans a local machine for insecurely stored AWS credentials and configuration files.  
It helps identify common misconfigurations and warns the user of potential security risks.

## 🚀 Features
- Detects AWS CLI config/credential files
- Flags unprotected or exposed keys
- Generates a basic security report

## 📦 Requirements
- Python 3.7+
- `boto3` (optional for AWS integrations)
- `os`, `pathlib`, `colorama`

## 🔧 How to Use
```bash
python aws_check.py

Example Output:

🔍 AWS Credential Check Tool
[✓] Found credentials file at /Users/you/.aws/credentials
[✓] Found config file at /Users/you/.aws/config
✅ Scan complete.
🧠 Why This?
As part of my cloud security learning journey, I created this tool to explore how credentials are stored and to help others identify poor AWS practices.


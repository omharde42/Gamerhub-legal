#!/usr/bin/env python3
import os
import re
import sys

EXPECTED_FILES = [
    "README.md",
    "LICENSE",
    "legal/01-founder-cofounder-agreement.md",
    "legal/02-ip-ownership-agreement.md",
    "legal/03-website-management-agreement.md",
    "legal/04-marketing-agreement.md",
    "legal/05-confidentiality-agreement.md",
    "legal/06-contributor-agreement.md",
    "policies/privacy-policy.md",
    "policies/terms-of-service.md",
    "policies/cookie-policy.md",
    "policies/security-policy.md",
    "records/document-version-history.md"
]

REQUIRED_PARTIES = ["Yash", "Om Harde", "Purvesh Bhadale"]

LEGAL_FILES_NEEDING_PARTIES = [
    "legal/01-founder-cofounder-agreement.md",
    "legal/02-ip-ownership-agreement.md",
    "legal/03-website-management-agreement.md",
    "legal/04-marketing-agreement.md",
    "legal/05-confidentiality-agreement.md",
    "legal/06-contributor-agreement.md"
]

REQUIRED_PLACEHOLDERS = [
    "[LEGAL ENTITY NAME]",
    "[DATE]",
    "[GOVERNING LAW / JURISDICTION]"
]

def main():
    errors = []
    print("=== Starting GamerHub Legal Documentation Validation ===")

    # 1. File existence check
    for filepath in EXPECTED_FILES:
        if not os.path.exists(filepath):
            errors.append(f"Missing required file: {filepath}")
        else:
            print(f"✓ Found {filepath}")

    if errors:
        print("\n❌ File Existence Errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    # 2. Content Checks
    for filepath in EXPECTED_FILES:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check parties in key legal documents
        if filepath in LEGAL_FILES_NEEDING_PARTIES:
            for party in REQUIRED_PARTIES:
                if party not in content:
                    errors.append(f"{filepath}: Missing party name '{party}'")

        # Check standard placeholders in legal/policies docs
        if filepath.startswith("legal/") or filepath.startswith("policies/"):
            for ph in REQUIRED_PLACEHOLDERS:
                if ph not in content:
                    errors.append(f"{filepath}: Missing expected placeholder '{ph}'")

        # Check mandatory legal disclaimer note in agreements and policies
        if filepath.startswith("legal/") or filepath.startswith("policies/"):
            if "LEGAL NOTICE & DISCLAIMER" not in content and "DISCLAIMER" not in content:
                errors.append(f"{filepath}: Missing legal disclaimer section")

        # Check signature block in agreements
        if filepath.startswith("legal/"):
            if "SIGNATURE" not in content.upper():
                errors.append(f"{filepath}: Missing signature section")

        # Check document version control section
        if filepath.startswith("legal/") or filepath.startswith("policies/"):
            if "VERSION CONTROL" not in content.upper() and "VERSION" not in content.upper():
                errors.append(f"{filepath}: Missing version control section")

    if errors:
        print("\n❌ Validation Errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\n✅ All GamerHub Legal Documentation Checks Passed Successfully!")

if __name__ == "__main__":
    main()

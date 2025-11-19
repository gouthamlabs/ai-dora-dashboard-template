# Example script to lint prompts for risky patterns
import os
import re

def lint_prompts(directory):
    risky_patterns = [r"PII", r"secret", r"client_data"]
    for root, _, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                content = f.read()
                for pattern in risky_patterns:
                    if re.search(pattern, content):
                        print(f"Risky pattern '{pattern}' found in {file}")

if __name__ == "__main__":
    lint_prompts("prompts/")

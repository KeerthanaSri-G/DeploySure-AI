import os

def scan_terraform(directory):
    risky_patterns = {
        '0.0.0.0/0': '⚠️ Resource open to the world',
        'aws_access_key': '⚠️ Hardcoded AWS access key',
        'aws_secret_key': '⚠️ Hardcoded AWS secret key',
    }

    issues_found = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.tf'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    for pattern, warning in risky_patterns.items():
                        if pattern in content:
                            issues_found.append((path, warning))

    return issues_found
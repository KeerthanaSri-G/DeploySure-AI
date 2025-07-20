from app.cloud_scanner import scan_terraform

def mock_gpt_explanation(warning):
    explanations = {
        '⚠️ Resource open to the world': "This CIDR block exposes the resource to the internet. It's risky in production.",
        '⚠️ Hardcoded AWS access key': "Embedding AWS keys in code is insecure. Use environment variables or secret managers.",
        '⚠️ Hardcoded AWS secret key': "Hardcoding secrets can lead to credential leaks. Use a safer alternative.",
    }
    return explanations.get(warning, "⚠️ Please review this issue carefully.")

def run_scan():
    scan_results = scan_terraform('sample_tf')
    detailed_results = []

    for file_path, warning in scan_results:
        explanation = mock_gpt_explanation(warning)
        detailed_results.append({
            "file": file_path,
            "warning": warning,
            "explanation": explanation
        })

    return detailed_results

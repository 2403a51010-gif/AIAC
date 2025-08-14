import re

def extract_emails(text):
    # Simple regex pattern for email extraction
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

# Example usage
sample_text = "Contact us at support@example.com or sales@company.org for more info."
emails = extract_emails(sample_text)
print("Extracted emails:", emails)
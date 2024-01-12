import re

def obfuscate_pii(log_entry):
    # Define regex patterns for different PII fields
    patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
        'ssn': r'\b\d{3}[-.\s]?\d{2}[-.\s]?\d{4}\b',
        # Add more patterns for other PII fields
    }

    # Replace PII fields with asterisks in the log entry
    for field, pattern in patterns.items():
        log_entry = re.sub(pattern, '********', log_entry)

    return log_entry

# Example usage
if __name__ == "__main__":
    original_log_entry = "User john.doe@example.com logged in from 192.168.1.1"
    obfuscated_log_entry = obfuscate_pii(original_log_entry)

    print("Original log entry:", original_log_entry)
    print("Obfuscated log entry:", obfuscated_log_entry)

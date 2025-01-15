# Extract all email addresses from a string.
import re

text = "Please contact us at support@example.com or sales@company.org."
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)
print("Emails found:", emails)
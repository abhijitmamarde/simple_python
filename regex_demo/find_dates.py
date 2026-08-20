import re

text = "Meeting on 20-08-2026 and 25-08-2026"

pattern = r"\d{2}-\d{2}-\d{4}"

print(re.findall(pattern, text))

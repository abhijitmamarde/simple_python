import re

text = "My phone is 9812345678 or alternate is: 9812345611"

result = re.sub(r"\d{10}", "XXXXXXXXXX", text)

print(result)
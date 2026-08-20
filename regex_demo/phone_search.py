import re

text = "My phone number is 9812345678. Other numbers are 9812345611 and 9812345622"

result = re.search(r"\d{10}", text)
if result:
    print("Number found!")
    results = re.findall(r"\d{10}", text)
    print(results)
else:
    print("Number not found!")


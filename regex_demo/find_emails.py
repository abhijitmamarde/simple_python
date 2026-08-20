import re

text = """
Contact john@gmail.com
or alice@yahoo.com
"""

pattern = r"[\w.-]+@[\w.-]+\.\w+"

print(re.findall(pattern, text))

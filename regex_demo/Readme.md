# What is Regex?

- A regular expression (Regex) is a pattern used to find, extract, validate, or replace text.
- `import re`
- Basic operations:
    - `re.search()`     -> Find first match
    - `re.match()`      -> Match from beginning
    - `re.findall()`    -> Find all matches
    - `re.sub()`        -> Replace matches
- mini / subset language
- domain specifix
- uses expression

### Online tool

- https://regex101.com/
- set flavor to Python

# Basic usage

```python
import re
text = "My phone number is 9812345678"

result = re.search(r"\d{10}", text)
print(result)

results = re.findall(r"\d{10}", text)
print(results)

# \d{10} -> Find a 10-digit number
# Meaning:
# \d -> a digit
# {10} -> matching exactly 10 times
```

# Patterns

| Pattern | Meaning   |
| ------- | --------- |
| `*`     | 0 or more |
| `+`     | 1 or more |
| `?`     | 0 or 1    |
| `{3}`   | exactly 3 |
| `{2,5}` | 2 to 5    |
| `{2,}`  | 2 or more |
| `[abc]` | Match one character that is either a, b, or c. |
| `[0-9]` | Match digit 0 to 9 |
| `[A-Z]` | Match alphabet A to Z |
| `[a-z]` | Match alphabet a to z |
| `[^0-9]` | ^ inside [] means NOT, so this means anything except 0 to 9 |
| `abc` | literal string `abc` |
| `a.c` | . means any character, including letter, will match `aac,abc,a1c` etc |
| `\d` | a digit |
| `\w` | matches word, seprated with whitespace |
| `\s` | matches all whitespace |

quick reference way:

```
.          Any character
\d         Digit
\D         Not a digit
\w         Word character
\W         Not a word character
\s         Whitespace
\S         Not whitespace

[abc]      a, b or c
[a-z]      lowercase letters
[A-Z]      uppercase letters
[0-9]      digits
[^0-9]     not a digit

*          0 or more
+          1 or more
?          0 or 1
{3}        exactly 3
{2,5}      2 to 5

^          Start of string
$          End of string

()         Capture group
|          OR
```
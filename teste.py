import re

text = "ele é legal"

text = re.sub(r'\s', '+', text)

print(text)
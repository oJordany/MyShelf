import re
metadata = "['esse cara', 'aquele cara']"
pattern = re.compile(r"\[|\'|\'|\]")
metadata = re.sub(pattern, '', metadata)
print(metadata)
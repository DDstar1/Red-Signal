import re, sys

path = r"C:\Users\USER\Desktop\Projects\RED SIGNAL\code_scripts\generate_prompts.py"
lines = open(path, encoding="utf-8").read().split("\n")

for i, l in enumerate(lines, 1):
    s = l.strip()
    if not s:
        continue
    # Skip lines that are properly quoted strings or structural
    first_char = l.lstrip()[0]
    if first_char in ('"', "'", "#", "{", "[", "(", "}", "]", ")"):
        continue
    # Skip dict keys / assignments like '"note": "...'
    if re.match(r'^[\w"]+["\w\s]*":', l.lstrip()):
        continue
    # Skip lines that look like normal code (def, return, etc.)
    if re.match(r'^\s*(def|return|class|if|elif|else|for|in|import|from|with|while|try|except|finally|raise|pass|break|continue)\b', l):
        continue
    # Continuation lines inside string-concat lists that are missing opening quote
    if s.endswith(('.', ',', ')', '"', "'", ":", '}', ']')):
        print(f"{i}: {l}")

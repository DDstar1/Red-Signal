import re
path = r"C:\Users\USER\Desktop\Projects\RED SIGNAL\code_scripts/generate_prompts.py"
lines = open(path, encoding="utf-8").read().split("\n")
pat = re.compile(r'["\']\}\)\s*,\s*$')
for i, l in enumerate(lines, 1):
    s = l.rstrip()
    if pat.search(s):
        print(i, repr(s[-40:]))

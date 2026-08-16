import re
path = r"C:\Users\USER\Desktop\Projects\RED SIGNAL\code_scripts/generate_prompts.py"
lines = open(path, encoding="utf-8").read().split("\n")

# find video_prompt( lines and print until we hit a line ending with ')'
for i, l in enumerate(lines, 1):
    if "video_prompt(" in l and "def " not in l:
        print(f"=== {i}: {l.strip()[:60]}")
        j = i
        while j < len(lines):
            j += 1
            s = lines[j-1].rstrip()
            print(f"    {j}: {repr(s[:90])}")
            if s.endswith(")") or s.endswith("),"):
                break

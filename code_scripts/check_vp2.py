import re
path = r"C:\Users\USER\Desktop\Projects\RED SIGNAL\code_scripts/generate_prompts.py"
lines = open(path, encoding="utf-8").read().split("\n")

for i, l in enumerate(lines, 1):
    if "video_prompt(" in l and "def " not in l:
        # collect following indented string lines until line ending with ')'
        block = []
        j = i
        while j < len(lines):
            j += 1
            s = lines[j-1]
            if s.strip().startswith('"'):
                block.append(s.rstrip())
            if s.rstrip().endswith(")") or s.rstrip().endswith("),"):
                break
        last = block[-1][-25:] if block else ""
        print(f"line {i}: last_line_ending=...{last}")

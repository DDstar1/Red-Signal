import json
import os

with open("metadata.jsonl") as f:
    for line in f:
        entry = json.loads(line)
        img_name = entry["file_name"]
        caption = entry["prompt"]
        txt_name = img_name.rsplit(".", 1)[0] + ".txt"
        with open(txt_name, "w") as out:
            out.write(caption)

count = len([f for f in os.listdir(".") if f.endswith(".txt")])
print(f"done, wrote {count} caption files")

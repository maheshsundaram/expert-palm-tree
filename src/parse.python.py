import json
import re

with open("./emoji-test.txt", "r", encoding="utf-8") as file:
    data = file.read()

lines = data.split("\n")

match_version = re.compile(r"E\d+(\.\d+)?", re.IGNORECASE)

emoji_data_by_hex = {}

for line in lines:
    clean = line.strip()
    if not clean or clean.startswith("#"):
        continue

    # left, right = clean.split("#")
    # "0023 FE0F 20E3                                         ; fully-qualified     # #️⃣ E0.6 keycap: #"
    # "0023 20E3                                              ; unqualified         # #⃣ E0.6 keycap: #"

    left, right = clean.split("#", maxsplit=1)

    hex_code_points, qualified_status = left.split(";")
    version_test = match_version.search(right)

    if version_test:
        version = version_test.group(0)
        index = version_test.start()
        emoji = right[:index].strip()
        description = right[index + len(version) :].strip()
        name, *modifiers = description.split(":")
        modifiers = modifiers[0].strip() if modifiers else None

        row = {
            "hex_code_points": hex_code_points.strip(),
            "qualified_status": qualified_status.strip(),
            "emoji": emoji.strip(),
            "version": version.strip(),
            "name": name.strip(),
            **({"modifiers": modifiers.strip()} if modifiers else {}),
        }

        emoji_data_by_hex[row["hex_code_points"]] = row

data = json.dumps(emoji_data_by_hex, ensure_ascii=False, separators=(",", ":"))
pretty_data = json.dumps(emoji_data_by_hex, ensure_ascii=False, indent=2)

with open("./build/python/emoji_data_by_hex.json", "w", encoding="utf-8") as file:
    file.write(data)

with open(
    "./build/python/emoji_data_by_hex_pretty.json", "w", encoding="utf-8"
) as file:
    file.write(pretty_data)

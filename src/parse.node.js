import * as fs from "fs";

const file = fs.readFileSync("./emoji-test.txt");
const raw_data = file.toString();
const lines = raw_data.split("\n");

const match_version = /E\d+(\.\d+)?/i;

const emoji_data_by_hex = {};

for (const line of lines) {
  const clean = line.trim();
  if (!clean) continue;
  if (clean === "\n" || clean.startsWith("#")) continue;
  const [left, right] = clean.split("#");
  const [hex_code_points, qualified_status] = left.split(";");
  const version_test = right.match(match_version);
  if (version_test && version_test.index) {
    const [version] = version_test;
    const { index } = version_test;
    const emoji = right.slice(0, index);
    const description = right.slice(index + version.length);
    const [name, modifiers] = description.split(":");

    const row = {
      hex_code_points: hex_code_points.trim(),
      qualified_status: qualified_status.trim(),
      emoji: emoji.trim(),
      version: version.trim(),
      name: name.trim(),
      ...(modifiers && { modifiers: modifiers.trim() }),
    };

    emoji_data_by_hex[row.hex_code_points] = row;
  }
  const data = JSON.stringify(emoji_data_by_hex);
  const pretty_data = JSON.stringify(emoji_data_by_hex, null, "  ");
  fs.writeFileSync("./build/node/emoji_data_by_hex.json", data);
  fs.writeFileSync("./build/node/emoji_data_by_hex_pretty.json", pretty_data);
}

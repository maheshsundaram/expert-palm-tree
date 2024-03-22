const file = Bun.file("./build/bun/emoji_data_by_hex.json");
const data = await file.json();

import { render } from "../src/render.js";

describe("render", () => {
  Object.keys(data).forEach((key) =>
    it(key, () => {
      const rendered = render(data[key].hex_code_points);
      expect(data[key].emoji).toEqual(rendered);
    })
  );
});

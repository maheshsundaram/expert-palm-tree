import * as fs from "fs";
const data = fs.readFileSync("./build/node/emoji_data_by_hex.json");

import { render } from "../src/render.js";

describe("render", () => {
  Object.keys(data).forEach((key) =>
    it("should render the emoji", () => {
      const rendered = render(data[key].hex_code_points);
      expect(data[key].emoji).toEqual(rendered);
    })
  );
});

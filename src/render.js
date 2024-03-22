export const render = (hex_code_points) =>
  hex_code_points.split(" ").map((point) => String.fromCodePoint(parseInt(point, 16))).join("");

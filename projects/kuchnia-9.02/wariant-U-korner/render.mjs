// Eksport PNG: rysunki (technical/*.svg) i widoki modelu 3D (index.html → renders/*.png).
//   node render.mjs svg            — tylko rysunki
//   node render.mjs 3d             — tylko widoki 3D
//   THREE_URL=file:///…/three.min.js node render.mjs 3d   — lokalna kopia three.js r128 (offline)
import { createRequire } from "module";
import { readdirSync, mkdirSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const HERE = dirname(fileURLToPath(import.meta.url));
const what = process.argv[2] || "all";

const VIEWS = [  // [plik, widok, fronty, numery]
  ["01-widok-od-wejscia", "entry", true, false],
  ["02-widok-od-przejscia", "right", true, false],
  ["03-widok-z-gory", "top", true, false],
  ["04-korpusy-bez-frontow", "entry", false, false],
  ["05-okno-i-zlew", "window", true, false],
  ["06-makieta-z-numerami", "iso", true, true],
];

const browser = await chromium.launch({ args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
if (what === "all" || what === "svg") {
  const page = await browser.newPage({ deviceScaleFactor: 2 });
  const dir = join(HERE, "technical");
  for (const f of readdirSync(dir).filter((f) => f.endsWith(".svg"))) {
    await page.goto("file://" + join(dir, f));
    await (await page.$("svg")).screenshot({ path: join(dir, f.replace(".svg", ".png")) });
    console.log("png", f);
  }
  await page.close();
}
if (what === "all" || what === "3d") {
  mkdirSync(join(HERE, "renders"), { recursive: true });
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  page.on("console", (m) => m.type() === "error" && console.log("console:", m.text()));
  if (process.env.THREE_URL) {
    await page.route("**/three.min.js", (r) => r.fulfill({ path: fileURLToPath(process.env.THREE_URL) }));
  }
  await page.route(/fonts\.(googleapis|gstatic)\.com/, (r) => r.abort());
  await page.goto("file://" + join(HERE, "index.html") + "?capture=1");
  await page.waitForFunction(() => window.__ready === true, null, { timeout: 120000 });
  for (const [name, view, fronts, labels] of VIEWS) {
    await page.evaluate(([v, f, l]) => window.__shot(v, f, l), [view, fronts, labels]);
    await page.waitForTimeout(400);
    await (await page.$("#stage")).screenshot({ path: join(HERE, "renders", name + ".png") });
    console.log("render", name);
  }
  await page.close();
}
await browser.close();

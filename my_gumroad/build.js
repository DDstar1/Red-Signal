/**
 * build.js — compile landing.template.html → landing.html
 *
 * Placeholder syntax:
 *   {{ASSET:filename}}      — data URI for images, raw <svg> for .svg files
 *   {{ASSET_URI:filename}}  — always a data URI (use inside src="" or CSS url())
 *
 * Run: node build.js
 */

const fs = require("fs");
const path = require("path");

const ASSETS = path.join(__dirname, "assets");
const TEMPLATE = path.join(__dirname, "landing.template.html");
const OUTPUT = path.join(__dirname, "landing.html");

const MIME = {
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".gif": "image/gif",
  ".webp": "image/webp",
  ".svg": "image/svg+xml",
};

function dataUri(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const mime = MIME[ext] ?? "application/octet-stream";
  const b64 = fs.readFileSync(filePath).toString("base64");
  return `data:${mime};base64,${b64}`;
}

function inlineSvg(filePath) {
  return fs.readFileSync(filePath, "utf8").trim();
}

function resolve(_, kind, name) {
  const filePath = path.join(ASSETS, name.trim());

  if (!fs.existsSync(filePath)) {
    console.warn(`  WARNING: asset not found -> ${filePath}`);
    return `{{${kind}:${name}}}`;
  }

  const ext = path.extname(filePath).toLowerCase();

  if (kind === "ASSET" && ext === ".svg") {
    console.log(`  inline SVG  : ${name}`);
    return inlineSvg(filePath);
  }

  console.log(`  data URI    : ${name}`);
  return dataUri(filePath);
}

if (!fs.existsSync(TEMPLATE)) {
  console.error(`ERROR: ${TEMPLATE} not found`);
  process.exit(1);
}

const template = fs.readFileSync(TEMPLATE, "utf8");
const result = template.replace(/\{\{(ASSET(?:_URI)?):([^}]+)\}\}/g, resolve);

fs.writeFileSync(OUTPUT, result, "utf8");
console.log(`\nOK ${OUTPUT}  (${result.length.toLocaleString()} chars)`);

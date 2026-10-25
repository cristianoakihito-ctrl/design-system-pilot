#!/usr/bin/env python3
"""Verificação do design-system-pilot. Só usa a biblioteca padrão do Python.

Uso: python3 scripts/verify.py            (na raiz do repositório)
Sai com código 1 se encontrar qualquer erro.

Checagens:
  1. Tokens: JSON válido e aliases de cor que resolvem (sem ciclo).
  2. Ícones: nome em kebab-case, tela 24 x 24 e viewBox 24 x 24.
  3. Documentos e exemplos: arquivos citados existem e toda variável
     --pbcon-* usada ou declarada existe nos tokens.
  4. Exemplos: o valor de cada token declarado no :root é igual ao do repositório.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []


def err(where, msg):
    errors.append(f"{where}: {msg}")


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # JSON inválido ou arquivo ausente
        err(rel(path), f"JSON inválido ou ilegível ({e})")
        return {}


# ---------------------------------------------------------------- 1. tokens
colors_raw = {}
for name in ("global", "semantic", "component"):
    colors_raw.update(load(os.path.join(ROOT, "tokens", "colors", name + ".json")))
spacing = load(os.path.join(ROOT, "tokens", "spacing.json"))
typo = load(os.path.join(ROOT, "tokens", "typography.json"))
motion = load(os.path.join(ROOT, "tokens", "motion.json"))
load(os.path.join(ROOT, "tokens", "drop-shadow.json"))


def resolve(key, seen=()):
    value = colors_raw[key]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        target = value[1:-1]
        if target in seen or key in seen:
            err("tokens/colors", f"alias circular em {key}")
            return None
        if target not in colors_raw:
            err("tokens/colors", f"{key} aponta para {{{target}}}, que não existe")
            return None
        return resolve(target, seen + (key,))
    return value


expected = {}  # nome da variável CSS -> (valor esperado, alvo de alias ou None)
for key, value in colors_raw.items():
    resolved = resolve(key)
    alias = value[1:-1] if isinstance(value, str) and value.startswith("{") else None
    expected["--" + key] = (resolved, alias)

for key, value in spacing.items():
    if key != "unit" and isinstance(value, (int, float)):
        expected["--pbcon-" + key] = ("0" if value == 0 else f"{value}px", None)
for group in ("font-size", "line-height", "letter-spacing", "paragraph-spacing"):
    for key, value in typo.get(group, {}).get("values", {}).items():
        expected[f"--pbcon-{group}-{key.replace('.', '-')}"] = ("0" if value == 0 else f"{value}px", None)
for key in typo.get("font-weight", {}):
    expected[f"--pbcon-font-weight-{key}"] = (key, None)
for key, value in typo.get("font-family", {}).items():
    expected[f"--pbcon-font-family-{key}"] = (value, None)
for key, value in motion.get("duration", {}).get("values", {}).items():
    expected[f"--pbcon-motion-duration-{key}"] = (f"{value}ms", None)
for key, value in motion.get("distance", {}).get("values", {}).items():
    expected[f"--pbcon-motion-distance-{key}"] = (f"{value}px", None)
for key, value in motion.get("easing", {}).items():
    expected[f"--pbcon-motion-easing-{key}"] = (value, None)

# --------------------------------------------------------------- 2. ícones
icons_dir = os.path.join(ROOT, "assets", "icons")
icon_files = sorted(f for f in os.listdir(icons_dir) if f.endswith(".svg")) if os.path.isdir(icons_dir) else []
if not icon_files:
    err("assets/icons", "nenhum ícone encontrado")
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)+\.svg$")
for fname in icon_files:
    path = os.path.join(icons_dir, fname)
    where = f"assets/icons/{fname}"
    if not NAME.match(fname):
        err(where, "nome fora do padrão kebab-case (categoria-nome.svg)")
    if "direciton" in fname or re.search(r"-up(filled|outlined)\.svg$", fname):
        err(where, "nome com erro de digitação conhecido")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"\s*<svg\b[^>]*>", text)
    if not m:
        err(where, "não começa com <svg>")
        continue
    head = m.group(0)
    w = re.search(r'\swidth="([^"]+)"', head)
    h = re.search(r'\sheight="([^"]+)"', head)
    vb = re.search(r'viewBox="([^"]+)"', head)
    if not (w and h and vb):
        err(where, "falta width, height ou viewBox")
        continue
    vbv = vb.group(1).replace(",", " ").split()
    if (w.group(1), h.group(1)) != ("24", "24"):
        err(where, f'width/height {w.group(1)} x {h.group(1)}, esperado 24 x 24')
    if len(vbv) != 4 or (float(vbv[2]), float(vbv[3])) != (24.0, 24.0):
        err(where, f'viewBox "{vb.group(1)}" não tem tamanho 24 x 24')

# ------------------------------------------------- 3. documentos e exemplos
doc_files = (
    glob.glob(os.path.join(ROOT, "*.md"))
    + glob.glob(os.path.join(ROOT, "components", "*.md"))
    + glob.glob(os.path.join(ROOT, "foundations", "*.md"))
    + glob.glob(os.path.join(ROOT, "examples", "*.html"))
)
PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])/?((?:tokens|components|foundations|examples)/[A-Za-z0-9_./-]*\.(?:json|md|html))")
ICON_RE = re.compile(r"(?<![A-Za-z0-9_-])([a-z0-9]+(?:-[a-z0-9]+)+\.svg)\b")
for path in sorted(doc_files):
    where = rel(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    plain = re.sub(r"data:[^)\"']+", "", text)  # ignora fontes embutidas
    for p in sorted(set(PATH_RE.findall(plain))):
        if not os.path.exists(os.path.join(ROOT, p)):
            err(where, f"cita {p}, que não existe")
    for icon in sorted(set(ICON_RE.findall(plain))):
        if icon not in icon_files:
            err(where, f"cita o ícone {icon}, que não existe em assets/icons")
    for var in sorted(set(re.findall(r"var\((--pbcon-[A-Za-z0-9-]+)\)", plain))):
        if var not in expected and not (path.endswith(".html") and re.search(re.escape(var) + r"\s*:", plain)):
            err(where, f"usa {var}, que não existe nos tokens")

for path in sorted(glob.glob(os.path.join(ROOT, "components", "*.md"))):
    where = rel(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for var in sorted(set(re.findall(r"var\((--pbcon-[A-Za-z0-9-]+)\)", text))):
        if var not in expected:
            err(where, f"usa {var}, que não existe nos tokens")

def norm(value):
    """Compara valores CSS ignorando caixa e a diferença entre 0 e 0px."""
    value = str(value).strip().lower()
    return "0" if value in ("0", "0px") else value


# ---------------------------------------------- 4. valores dos exemplos
for path in sorted(glob.glob(os.path.join(ROOT, "examples", "*.html"))):
    where = rel(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    plain = re.sub(r"data:[^)\"']+", "", text)
    for var, value in re.findall(r"(--pbcon-[A-Za-z0-9-]+)\s*:\s*([^;]+);", plain):
        value = value.strip()
        if var not in expected:
            err(where, f"declara {var}, que não existe nos tokens")
            continue
        want, alias = expected[var]
        m = re.match(r"var\((--[\w-]+)\)$", value)
        if m:
            if alias is None or "--" + alias != m.group(1):
                err(where, f"{var} aponta para {m.group(1)}, o repositório aponta para {alias}")
        elif norm(want) != norm(value):
            err(where, f"{var} vale {value}, o repositório define {want}")

# ------------------------------------------------------------------ saída
if errors:
    print(f"FALHOU: {len(errors)} problema(s)\n")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"OK: {len(icon_files)} ícones, {len(expected)} tokens, {len(doc_files)} documentos e exemplos conferidos.")

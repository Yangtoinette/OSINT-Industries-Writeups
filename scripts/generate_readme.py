#!/usr/bin/env python3
"""
generate_readme.py — Repo Markdown
Scanne writeups/*.md, lit le frontmatter YAML (---),
génère README.md avec le tableau des write-ups.
Lancer manuellement : python3 scripts/generate_readme.py
"""
import re
from pathlib import Path
from datetime import datetime

# ── À modifier avant le premier push ─────────────────────────────────────────
README_TITLE       = "OSINT Write-ups"
README_DESCRIPTION = "Résolutions de challenges OSINT — format Markdown."
# ─────────────────────────────────────────────────────────────────────────────

WRITEUPS_DIR = Path("writeups")
README_PATH  = Path("README.md")


def extract_meta(filepath):
    """Lit le frontmatter YAML (---) en tête de fichier Markdown."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        print(f"  [!] Pas de frontmatter dans {filepath.name} — ignoré")
        return None
    meta = {}
    for line in match.group(1).strip().splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            # Supprimer les guillemets optionnels autour des valeurs
            meta[key.strip().lower()] = val.strip().strip('"')
    meta["_file"] = filepath.name
    return meta


def build_table(entries):
    if not entries:
        return "_Aucun write-up pour le moment._\n"
    rows = [
        "| Challenge | Plateforme | Catégorie | Difficulté | Date | Points |",
        "|:----------|:-----------|:----------|:-----------|:-----|-------:|",
    ]
    for e in sorted(entries, key=lambda x: x.get("date", ""), reverse=True):
        title = e.get("title", e["_file"].replace(".md", ""))
        # Lien relatif — GitHub rend le Markdown nativement
        url   = f"writeups/{e['_file']}"
        rows.append(
            f"| [{title}]({url}) "
            f"| {e.get('platform', '-')} "
            f"| {e.get('category', '-')} "
            f"| {e.get('difficulty', '-')} "
            f"| {e.get('date', '-')} "
            f"| {e.get('points', '-')} |"
        )
    return "\n".join(rows) + "\n"


def main():
    entries = []
    if WRITEUPS_DIR.exists():
        for f in sorted(WRITEUPS_DIR.glob("*.md")):
            if f.stem.upper() == "TEMPLATE":
                continue
            meta = extract_meta(f)
            if meta:
                entries.append(meta)
    print(f"{len(entries)} write-up(s) trouvé(s)")

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    readme = f"""# {README_TITLE}

{README_DESCRIPTION}

---

{build_table(entries)}
---

"""
    README_PATH.write_text(readme, encoding="utf-8")
    print("README.md mis à jour")


if __name__ == "__main__":
    main()

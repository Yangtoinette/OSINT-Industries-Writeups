#!/usr/bin/env python3
"""
generate_readme.py — Repo Markdown
Scanne writeups/*.md, lit le frontmatter YAML (---),
et met à jour uniquement les sections entre les balises
<!-- STATS:START --> / <!-- STATS:END --> et
<!-- WRITEUPS:START --> / <!-- WRITEUPS:END --> dans README.md.

Le reste du README (logo, présentation, informations complémentaires...)
est entièrement préservé.

Si les balises sont absentes, le README est créé depuis zéro avec un
header par défaut (à personnaliser ensuite à la main).

Lancer manuellement : python3 scripts/generate_readme.py
"""
import re
from pathlib import Path
from datetime import datetime

# ── À modifier avant le premier push ─────────────────────────────────────────
README_TITLE       = "OSINT Industries Write-ups"
README_DESCRIPTION = "Résolutions de challenges OSINT Industries — GEOINT, réseaux sociaux, stéganographie et enquêtes en source ouverte."
PLATFORM_LABEL     = "OSINT%20INDUSTRIES"   # texte du badge logo (encodé URL)
BADGE_COLOR        = "2ea043"               # vert — cohérent avec le thème des writeups
STATS_TITLE        = "🔎 OSINT Industries Stats"
STAT_1_LABEL       = "🧩 Writeups résolus"
STAT_2_LABEL       = "⭐ Points totaux"
# ─────────────────────────────────────────────────────────────────────────────

WRITEUPS_DIR        = Path("writeups")
README_PATH         = Path("README.md")
MARKER_STATS_START  = "<!-- STATS:START -->"
MARKER_STATS_END    = "<!-- STATS:END -->"
MARKER_WU_START     = "<!-- WRITEUPS:START -->"
MARKER_WU_END       = "<!-- WRITEUPS:END -->"


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


def build_stats(entries):
    """Calcule le nombre de writeups et la somme des points numériques."""
    count = len(entries)
    total_points = 0
    for e in entries:
        raw = str(e.get("points", "")).strip()
        if raw.isdigit():
            total_points += int(raw)

    badge_count  = f"https://img.shields.io/badge/{count}-writeups-{BADGE_COLOR}?style=for-the-badge"
    badge_points = f"https://img.shields.io/badge/{total_points}-points-58a6ff?style=for-the-badge"

    return (
        f'<div align="center">\n\n'
        f"## {STATS_TITLE}\n\n"
        f"<table>\n"
        f"  <tr>\n"
        f'    <td align="center" width="220">\n'
        f"      <strong>{STAT_1_LABEL}</strong><br/><br/>\n"
        f'      <img src="{badge_count}" alt="{count} writeups"/>\n'
        f"    </td>\n"
        f'    <td align="center" width="220">\n'
        f"      <strong>{STAT_2_LABEL}</strong><br/><br/>\n"
        f'      <img src="{badge_points}" alt="{total_points} points"/>\n'
        f"    </td>\n"
        f"  </tr>\n"
        f"</table>\n\n"
        f"</div>"
    )


def replace_between(content, start_marker, end_marker, new_inner):
    if start_marker in content and end_marker in content:
        return re.sub(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            f"{start_marker}\n{new_inner}\n{end_marker}",
            content,
            flags=re.DOTALL,
        )
    return None


def update_readme(stats_block, writeups_block):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    writeups_inner = f"<!-- Dernière mise à jour : {now} UTC -->\n\n{writeups_block}"

    if README_PATH.exists():
        content = README_PATH.read_text(encoding="utf-8")
        updated = replace_between(content, MARKER_STATS_START, MARKER_STATS_END, stats_block)
        if updated is not None:
            content = updated
            updated_wu = replace_between(content, MARKER_WU_START, MARKER_WU_END, writeups_inner)
            if updated_wu is not None:
                README_PATH.write_text(updated_wu, encoding="utf-8")
                print("README.md mis à jour (stats + writeups uniquement, header préservé)")
                return

    # Pas de balises ou pas de fichier → création depuis zéro avec un header par défaut
    logo = (
        f'<div align="center">\n'
        f'<img src="https://img.shields.io/badge/{PLATFORM_LABEL}-000000?'
        f'style=for-the-badge&logoColor=white" alt="{README_TITLE}" height="40">\n'
        f"</div>\n"
    )
    README_PATH.write_text(
        f"{logo}\n"
        f"<!-- STATS:START -->\n{stats_block}\n<!-- STATS:END -->\n\n"
        f"---\n\n"
        f"# {README_TITLE}\n\n"
        f"{README_DESCRIPTION}\n\n"
        f"---\n\n"
        f"{MARKER_WU_START}\n{writeups_inner}\n{MARKER_WU_END}\n",
        encoding="utf-8",
    )
    print("README.md créé depuis zéro (avec header par défaut à personnaliser)")


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

    update_readme(build_stats(entries), build_table(entries))


if __name__ == "__main__":
    main()

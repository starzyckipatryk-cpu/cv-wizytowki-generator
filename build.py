#!/usr/bin/env python3
import csv, json, shutil, sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import qrcode

ROOT = Path(__file__).parent
TEMPLATE_DIR = ROOT / "template"
DIST_DIR = ROOT / "dist"
CSV_FILE = ROOT / "clients.csv"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=select_autoescape(["html", "xml"]))
page_tpl = env.get_template("index.html")

def slugify(s: str) -> str:
    import re, unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def parse_bullets(text: str):
    """Rozdziela bullety po ' | ' lub nowej linii."""
    if not text: return []
    # najpierw po ' | ', jeśli nie ma – po nowej linii
    parts = [p.strip() for p in text.split(" | ") if p.strip()]
    if len(parts) == 1 and "\n" in text:
        parts = [p.strip() for p in text.split("\n") if p.strip()]
    return parts

def build_client(row: dict):
    name = f"{row.get('Imię','').strip()} {row.get('Nazwisko','').strip()}".strip()
    if not name: return
    slug = slugify(name)
    client_dir = DIST_DIR / slug
    client_dir.mkdir(parents=True, exist_ok=True)

    site_url = f"https://twojanazwa.github.io/cv-wizytowki/{slug}/"
    qr = qrcode.make(site_url, box_size=6, border=2)
    qr.save(client_dir / "qr.png")

    skills = [s.strip() for s in row.get("Umiejętności", "").split(",") if s.strip()]

    exp = []
    for i in range(1, 6):
        company = row.get(f"Doświadczenie {i} (nazwa firmy)", "").strip()
        if not company: continue
        bullets = parse_bullets(row.get(f"Doświadczenie {i} (bullety)", ""))
        exp.append({
            "company": company,
            "role": row.get(f"Doświadczenie {i} (stanowisko)", "").strip(),
            "period": row.get(f"Doświadczenie {i} (okres)", "").strip(),
            "bullets": bullets,
        })

    portfolio = []
    for i in range(1, 4):
        title = row.get(f"Projekt {i} (tytuł)", "").strip()
        if not title: continue
        portfolio.append({
            "title": title,
            "description": row.get(f"Projekt {i} (opis)", "").strip(),
            "image": row.get(f"Projekt {i} (obraz)", "").strip(),
            "link": row.get(f"Projekt {i} (link)", "").strip(),
        })

    ctx = {
        "name": name,
        "title": row.get("Stanowisko docelowe", "").strip(),
        "industry": row.get("Branża", "").strip(),
        "linkedin": row.get("Link do LinkedIn", "").strip(),
        "email": row.get("Email kontaktowy", "").strip(),
        "phone": row.get("Telefon", "").strip(),
        "about": row.get("O mnie", "").strip(),
        "skills": skills,
        "experience": exp,
        "portfolio": portfolio,
        "qr_path": "qr.png",
        "site_url": site_url,
        "meta_description": f"{name} – {row.get('Stanowisko docelowe','')}. Strona wizytówka CV.",
        "current_year": 2026,
    }

    html = page_tpl.render(**ctx)
    (client_dir / "index.html").write_text(html, encoding="utf-8")

    assets_src = TEMPLATE_DIR / "assets"
    assets_dst = client_dir / "assets"
    if assets_dst.exists(): shutil.rmtree(assets_dst)
    shutil.copytree(assets_src, assets_dst)

    print(f"✅ Built: {site_url}")

def main():
    if not CSV_FILE.exists():
        print(f"❌ Brak {CSV_FILE}")
        sys.exit(1)
    DIST_DIR.mkdir(exist_ok=True)
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("Status", "").strip().lower() == "gotowy":
                build_client(row)

if __name__ == "__main__":
    main()

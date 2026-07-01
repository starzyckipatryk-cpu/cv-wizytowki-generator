# CV Wizytówka – Generator & Operacyjne Pliki

Struktura projektu:
```
cv-wizytowki-generator/
├── build.py                    # Generator stron (Python + Jinja2)
├── clients.csv                 # Eksport z Tally (umieść tutaj przed budową)
├── template/
│   ├── index.html              # Szablon Jinja2 (mobile-first, accessible)
│   └── assets/
│       ├── style.css           # Pełne style (CSS custom props, clamp(), print)
│       └── script.js           # Vanilla JS (smooth scroll, animations, QR lazy, copy)
├── dist/                       # Wygenerowane strony klientów (git push → GitHub Pages)
│   └── jan-kowalski/
│       ├── index.html
│       ├── qr.png
│       └── assets/
├── docs/
│   ├── regulamin_i_polityka_prywatnosci.md  # Gotowy do wklejenia na Carrd + Tally
│   └── kpi_google_sheets_setup.md           # Instrukcja arkusza KPI + formuły
└── emails/
    └── sekwencja_mailowa.md    # 4 maile (HTML + plaintext) + zmienne
```

---

## 🚀��� SZYBKI START (po pobraniu)

### 1. Zależności Pythona
```bash
pip install jinja2 qrcode[pil]
```

### 2. Przygotuj `clients.csv`
Eksport z Tally → Responses → Export CSV → zmień nazwy kolumn na polskie (zgodne z `build.py`) lub dostosuj `build.py` do swoich nagłówków.

**Minimalne kolumny wymagane:**
```
Imię,Nazwisko,Stanowisko docelowe,Branża,Link do LinkedIn,Email kontaktowy,Telefon,O mnie,Umiejętności,Doświadczenie 1 (nazwa firmy),Doświadczenie 1 (stanowisko),Doświadczenie 1 (okres),Doświadczenie 1 (bullety),...,Doświadczenie 5 (...),Status
```
> `Status` = `gotowy` dla klientów do wygenerowania.

### 3. Dodaj zdjęcie profilowe
Umieść `assets/avatar.jpg` w `template/assets/` (kwadratowe, 400x400px, <200KB).

### 4. Generuj
```bash
python build.py
# Tworzy dist/<slug>/index.html + qr.png + kopiuje assets/
```

### 5. Deploy
```bash
git add dist/
git commit -m "clients: jan-kowalski, anna-nowak"
git push origin main
# GitHub Pages odświeża się w ~60 sekund
```

---

## 📋 CHECKLISTA WDROŻENIA (Tydzień 0-1)

| Zadanie | Plik / Narzędzie | Status |
|---------|------------------|--------|
| Profil LinkedIn (zdjęcie, headline, About, Featured) | – | ☐ |
| 500+ kontaktów LinkedIn | – | ☐ |
| Konto Tally.so + formularz briefu | `docs/regulamin...` (checkbox RODO) | ☐ |
| Domena landing page + Carrd | `docs/regulamin...` (linki w stopce) | ☐ |
| Repo GitHub `cv-wizytowki-generator` + Pages | `build.py`, `template/` | ☐ |
| Szablon HTML/CSS/JS | `template/` | ☐ |
| Generator `build.py` | `build.py` | ☐ |
| 3 strony testowe (znajomi) | `dist/` + testimonial | ☐ |
| Landing page na Carrd | `docs/regulamin...` (treść) | ☐ |
| Regulamin + Polityka prywatności | `docs/regulamin_i_polityka_prywatnosci.md` | ☐ |
| Arkusz KPI Google Sheets | `docs/kpi_google_sheets_setup.md` | ☐ |
| Szablony maili (Canned Responses) | `emails/sekwencja_mailowa.md` | ☐ |
| Cold outreach LinkedIn (dziennie 2h) | `Outreach_Stats` zakładka | ☐ |

---

## 🔧 DOSTOSOWANIE SZABLONU

### Zmiana kolorystyczna (CSS Variables w `style.css`):
```css
:root {
  --color-primary: #2563eb;      /* Twój brand blue */
  --color-accent: #f59e0b;       /* Akcent (badge, QR label) */
  --color-bg-dark: #1a1a2e;      /* Hero background */
  --font-family: 'Inter', ...;   /* Lub inna font z Google Fonts */
}
```

### Dodanie sekcji Portfolio:
W `index.html` sekcja `#portfolio` już gotowa – przekazuj w `clients.csv` kolumny:
`Projekt 1 (tytuł), Projekt 1 (opis), Projekt 1 (obraz), Projekt 1 (link), ...`

### Custom domena klienta (upsell 150 zł):
1. Klient kupuje domenę u rejestratora.
2. Ty w Cloudflare: `CNAME jan-kowalski.twojanazwa.github.io` + Proxy ON + SSL Full.
3. W GitHub Pages repo: Settings > Pages > Custom domain > wpisz domenę.
4. Gotowe – HTTPS, CDN, DDoS protection gratis.

---

## 📧 MAILE – JAK UŻYWAĆ

1. **Gmail / Outlook:** Utwórz **Canned Responses / Quick Parts** z treścią HTML (kopiuj z `emails/sekwencja_mailowa.md`).
2. **Zmienne** podmieniasz ręcznie (5 min/klient) – to daje ludzki touch.
3. **Mail 1** – automatyzuj przez Tally → Webhook → Make.com (free) → Gmail API.
4. **Mail 2, 3, 4** – wysyłaj ręcznie po sprawdzeniu plików.

---

## 📊 KPI – CO TYGODNIA (piątek 16:00)

Otwórz `Dashboard` w Google Sheets → sprawdź:
- Zaproszenia ≥ 150/tydz
- Acceptance rate ≥ 25%
- Reply rate ≥ 15%
- Demo ≥ 3/tydz
- Sprzedaże ≥ 1-2/tydz
- Czas produkcji ≤ 45 min

Jeśli coś nie pasuje → **zmień jedną rzecz** (zdjęcie, headline, szablon wiadomości) i testuj kolejny tydzień.

---

## 🛟 TROUBLESHOOTING

| Problem | Rozwiązanie |
|---------|-------------|
| `build.py` ModuleNotFoundError | `pip install jinja2 qrcode[pil]` |
| Strona nie odświeża na GitHub Pages | Sprawdz Actions tab, poczekaj 2 min, hard refresh (Ctrl+Shift+R) |
| QR kod nie skanuje | Sprawdź `site_url` w `build.py` (musi kończyć się `/`) |
| Mail ląduje w spamie | Ustaw DKIM/SPF/DMARC na domenie, unikaj słów "gratis", "promocja" |
| Acceptance rate < 15% | Popraw zdjęcie profilowe, headline, About na LinkedIn |
| Klient nie płaci po akceptacji | Mail 4 (przypomnienie) + wezwanie do zapłaty po 14 dniach |

---

## 📞 KONTAKT / ROZWOJ

- **Generator v2:** GitHub Action auto-deploy na push do `main` (`.github/workflows/deploy.yml`)
- **PDF CV auto:** Dodaj `weasyprint` lub `playwright` w `build.py` → generuj PDF z `cv.html` szablonu
- **Skalowanie:** Make.com / n8n dla automatyzacji maili, Notion CRM, Airtable pipeline

---

**Wersja:** 1.0 (Master Plan Run 1)  
**Data:** 2026-07-01  
**Autor:** Max AI + Ty 🤝
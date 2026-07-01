# Sekwencja maili do Klienta – CV Wizytówka

Wszystkie maile wysyłasz z adresu: **{{ sender_email }}** (np. kontakt@cvwizytowka.pl)  
Tematy: krótkie, konkretne, bez spamu-słów.  
Format: **HTML + plaintext** (dla dostarczalności).  
Zmienne w `{{ }}` – podmieniaj przed wysłaniem.

---

## 📧 MAIL 1: Potwierdzenie zamówienia + brief
**Kiedy:** Natychmiast po wypełnieniu formularza Tally (automatyzacja: Tally → webhook → email)  
**Cel:** Potwierdzić, ustalić oczekiwania, poprosić o brakujące materiały.

---

**Temat:** Potwierdzenie zamówienia CV Wizytówka – {{ name }} {{ surname }}

---

### Treść HTML:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Potwierdzenie zamówienia</title>
</head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#1a1a2e;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;padding:40px 20px;">
    <tr>
      <td style="background:#ffffff;border-radius:12px;padding:40px;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <!-- Header -->
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td style="text-align:center;padding-bottom:24px;border-bottom:1px solid #e2e8f0;">
              <p style="margin:0 0 8px;font-size:12px;font-weight:600;color:#2563eb;text-transform:uppercase;letter-spacing:0.1em;">CV Wizytówka</p>
              <h1 style="margin:0;font-size:24px;font-weight:700;color:#1a1a2e;">Dziękujemy za zamówienie, {{ name }}!</h1>
            </td>
          </tr>
        </table>

        <!-- Main content -->
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;">
          <tr>
            <td>
              <p style="margin:0 0 16px;font-size:16px;">Otrzymaliśmy Twój brief i materiały. Przystępujemy do pracy – Twoja strona i CV będą gotowe w ciągu <strong>5 dni roboczych</strong> (do {{ delivery_date }}).</p>
              
              <p style="margin:0 0 16px;font-size:16px;">Oto co prześlesz nam (lub już prześleś):</p>
              
              <ul style="margin:0 0 24px;padding-left:20px;font-size:15px;color:#374151;">
                <li style="margin-bottom:8px;"><strong>CV (PDF/DOCX):</strong> {{ cv_status }}</li>
                <li style="margin-bottom:8px;"><strong>Zdjęcie profilowe:</strong> {{ photo_status }}</li>
                <li style="margin-bottom:8px;"><strong>Zdjęcia do portfolio (opcjonalnie):</strong> {{ portfolio_status }}</li>
              </ul>

              {% if missing_materials %}
              <div style="background:#fef3c7;border:1px solid #f59e0b;border-radius:8px;padding:16px;margin-bottom:24px;">
                <p style="margin:0 0 8px;font-weight:600;color:#92400e;">⚠️ Brakujące materiały:</p>
                <p style="margin:0;font-size:15px;color:#92400e;">{{ missing_materials }}</p>
                <p style="margin:12px 0 0;font-size:14px;">Proszę o przesłanie ich odpowiedzią na ten mail lub przez WeTransfer/Dysk Google – to przyspieszy pracę.</p>
              </div>
              {% endif %}

              <h2 style="margin:0 0 16px;font-size:18px;font-weight:600;color:#1a1a2e;">Co się teraz dzieje?</h2>
              <ol style="margin:0 0 24px;padding-left:20px;font-size:15px;color:#374151;">
                <li style="margin-bottom:12px;">Budujemy stronę na podstawie szablonu + Twoje dane.</li>
                <li style="margin-bottom:12px;">Przerabiamy CV (PDF + DOCX) i wklejamy kod QR.</li>
                <li style="margin-bottom:12px;">Wysyłamy link do wersji live + pliki do akceptacji.</li>
                <li style="margin-bottom:12px;">Masz 48h na jedną rundę poprawek (max 3 zmiany).</li>
                <li>Po akceptacji – płacisz 899 zł i odbierasz gotowe pliki.</li>
              </ol>

              <p style="margin:0 0 16px;font-size:15px;">W razie pytań – odpowiadaj na ten mail. Odpisujemy w ciągu kilku godzin (godz. pracy 9–17).</p>

              <p style="margin:0;font-size:15px;">Pozdrawiamy,<br><strong>Zespół CV Wizytówka</strong><br><a href="https://cvwizytowka.pl" style="color:#2563eb;text-decoration:none;">cvwizytowka.pl</a> | <a href="mailto:{{ sender_email }}" style="color:#2563eb;text-decoration:none;">{{ sender_email }}</a></p>
            </td>
          </tr>
        </table>

        <!-- Footer -->
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #e2e8f0;padding-top:24px;">
          <tr>
            <td style="font-size:12px;color:#9ca3af;text-align:center;">
              <p style="margin:0 0 4px;">Otrzymałeś ten mail, bo zamówiłeś usługę na cvwizytowka.pl.</p>
              <p style="margin:0">{{ provider_name }}, NIP: {{ provider_nip }}, {{ provider_address }}</p>
              <p style="margin:8px 0 0;"><a href="https://cvwizytowka.pl/regulamin" style="color:#9ca3af;">Regulamin</a> | <a href="https://cvwizytowka.pl/polityka-prywatnosci" style="color:#9ca3af;">Polityka prywatności</a></p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

---

### Wersja plaintext (kopiuj do pola "text version" w systemie mailowym):

```
Dziękujemy za zamówienie, {{ name }}!

Otrzymaliśmy Twój brief i materiały. Przystępujemy do pracy – Twoja strona i CV będą gotowe w ciągu 5 dni roboczych (do {{ delivery_date }}).

Oto status materiałów:
- CV (PDF/DOCX): {{ cv_status }}
- Zdjęcie profilowe: {{ photo_status }}
- Zdjęcia do portfolio: {{ portfolio_status }}

{% if missing_materials %}
⚠️ Brakujące materiały: {{ missing_materials }}
Proszę o przesłanie odpowiedzią na ten mail lub przez WeTransfer/Dysk Google.
{% endif %}

Co się teraz dzieje?
1. Budujemy stronę na podstawie szablonu + Twoje dane.
2. Przerabiamy CV (PDF + DOCX) i wklejamy kod QR.
3. Wysyłamy link do wersji live + pliki do akceptacji.
4. Masz 48h na jedną rundę poprawek (max 3 zmiany).
5. Po akceptacji – płacisz 899 zł i odbierasz gotowe pliki.

W razie pytań – odpowiadaj na ten mail. Odpisujemy w ciągu kilku godzin.

Pozdrawiamy,
Zespół CV Wizytówka
cvwizytowka.pl | {{ sender_email }}

---
{{ provider_name }}, NIP: {{ provider_nip }}
Regulamin: https://cvwizytowka.pl/regulamin
Polityka prywatności: https://cvwizytowka.pl/polityka-prywatnosci
```

---

## 📧 MAIL 2: Dostarczenie do akceptacji (wersja live + pliki)
**Kiedy:** Po zakończeniu produkcji (cel: ≤5 dni roboczych)  
**Cel:** Pokazać efekt, zebrać akceptację lub poprawki, zainicjować płatność.

---

**Temat:** Twoja strona CV jest gotowa do podglądu – {{ name }} {{ surname }}

---

### Treść HTML:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Strona gotowa do akceptacji</title>
</head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#1a1a2e;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;padding:40px 20px;">
    <tr>
      <td style="background:#ffffff;border-radius:12px;padding:40px;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td style="text-align:center;padding-bottom:24px;border-bottom:1px solid #e2e8f0;">
              <p style="margin:0 0 8px;font-size:12px;font-weight:600;color:#10b981;text-transform:uppercase;letter-spacing:0.1em;">Gotowe do podglądu</p>
              <h1 style="margin:0;font-size:24px;font-weight:700;color:#1a1a2e;">Twoja strona i CV są gotowe, {{ name }}!</h1>
            </td>
          </tr>
        </table>

        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;">
          <tr>
            <td>
              <p style="margin:0 0 24px;font-size:16px;">Przygotowaliśmy wersję finalną. Sprawdź spokojnie – masz <strong>48 godzin</strong> na feedback.</p>

              <!-- CTA Buttons -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
                <tr>
                  <td style="text-align:center;padding-bottom:12px;">
                    <a href="{{ site_url }}" style="display:inline-block;background:#2563eb;color:#ffffff;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;">🔗 Zobacz stronę live</a>
                  </td>
                </tr>
                <tr>
                  <td style="text-align:center;">
                    <a href="{{ cv_pdf_url }}" style="display:inline-block;background:#ffffff;color:#2563eb;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;border:2px solid #2563eb;">📄 Pobierz CV (PDF)</a>
                  </td>
                </tr>
              </table>

              <p style="margin:0 0 16px;font-size:15px;color:#6b7280;">Link do wersji DOCX: <a href="{{ cv_docx_url }}" style="color:#2563eb;">{{ cv_docx_url }}</a></p>

              <div style="background:#f0fdf4;border:1px solid #10b981;border-radius:8px;padding:16px;margin-bottom:24px;">
                <p style="margin:0 0 8px;font-weight:600;color:#065f46;">✅ Co masz teraz zrobić?</p>
                <ol style="margin:0;padding-left:20px;font-size:15px;color:#065f46;">
                  <li style="margin-bottom:8px;">Kliknij link wyżej i przejrzyj stronę na telefonie i komputerze.</li>
                  <li style="margin-bottom:8px;">Otwórz PDF CV – sprawdź dane, ortografię, kod QR.</li>
                  <li style="margin-bottom:8px;">Jeśli wszystko OK – <strong>odpisz na ten mail z jednolinijkową akceptacją</strong> (np. „Akceptuję, płacę jutro”).</li>
                  <li>Jeśli chcesz poprawki – wpisz je w odpowiedzi (max 3 zmiany, np. „zmień zdjęcie, skróć 'O mnie', dodaj umiejętność X”).</li>
                </ol>
              </div>

              <h2 style="margin:0 0 16px;font-size:18px;font-weight:600;color:#1a1a2e;">Płatność</h2>
              <p style="margin:0 0 12px;font-size:15px;">Po Twojej akceptacji przelew <strong>899 zł brutto</strong> na konto:</p>
              <table role="presentation" cellpadding="0" cellspacing="0" style="font-size:15px;font-family:monospace;background:#f9fafb;border:1px solid #e2e8f0;border-radius:8px;">
                <tr><td style="padding:8px 12px;font-weight:600;color:#374151;">Nazwa:</td><td style="padding:8px 12px;">{{ provider_name }}</td></tr>
                <tr style="background:#ffffff;"><td style="padding:8px 12px;font-weight:600;color:#374151;">IBAN:</td><td style="padding:8px 12px;">{{ provider_iban }}</td></tr>
                <tr><td style="padding:8px 12px;font-weight:600;color:#374151;">Tytuł:</td><td style="padding:8px 12px;">CV Wizytówka – {{ name }} {{ surname }}</td></tr>
                <tr style="background:#ffffff;"><td style="padding:8px 12px;font-weight:600;color:#374151;">Kwota:</td><td style="padding:8px 12px;">899,00 PLN</td></tr>
              </table>

              <p style="margin:16px 0 0;font-size:14px;color:#6b7280;">Faktura VAT 23% wystawimy po zaksięgowaniu wpłaty (na dane z briefu).</p>

              <hr style="border:none;border-top:1px solid #e2e8f0;margin:24px 0;">

              <p style="margin:0 0 8px;font-size:15px;">Poprawki (1 runda, max 3 zmiany) są w cenie. Każda kolejna runda = 150 zł/h.</p>
              <p style="margin:0 0 8px;font-size:15px;">Brak odpowiedzi w ciągu 48h = akceptacja bezpoprawkowa.</p>

              <p style="margin:24px 0 0;font-size:15px;">Pozdrawiamy,<br><strong>Zespół CV Wizytówka</strong></p>
            </td>
          </tr>
        </table>

        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #e2e8f0;padding-top:24px;">
          <tr>
            <td style="font-size:12px;color:#9ca3af;text-align:center;">
              <p style="margin:0 0 4px;">{{ provider_name }}, NIP: {{ provider_nip }}</p>
              <p style="margin:0"><a href="https://cvwizytowka.pl/regulamin" style="color:#9ca3af;">Regulamin</a> | <a href="https://cvwizytowka.pl/polityka-prywatnosci" style="color:#9ca3af;">Polityka prywatności</a></p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

---

### Wersja plaintext:

```
Twoja strona i CV są gotowe, {{ name }}!

Przygotowaliśmy wersję finalną. Sprawdź spokojnie – masz 48 godzin na feedback.

🔗 Strona live: {{ site_url }}
📄 CV (PDF): {{ cv_pdf_url }}
📝 CV (DOCX): {{ cv_docx_url }}

✅ Co masz teraz zrobić?
1. Kliknij linki i przejrzyj stronę na telefonie i komputerze.
2. Otwórz PDF CV – sprawdź dane, ortografię, kod QR.
3. Jeśli wszystko OK – odpisz na ten mail z akceptacją (np. „Akceptuję, płacę jutro”).
4. Jeśli chcesz poprawki – wpisz je w odpowiedzi (max 3 zmiany).

💰 Płatność po akceptacji: 899 zł brutto
{{ provider_name }}
IBAN: {{ provider_iban }}
Tytuł: CV Wizytówka – {{ name }} {{ surname }}
Kwota: 899,00 PLN

Faktura VAT 23% po zaksięgowaniu.

Poprawki (1 runda, max 3 zmiany) w cenie. Kolejna runda = 150 zł/h.
Brak odpowiedzi w 48h = akceptacja.

Pozdrawiamy,
Zespół CV Wizytówka
cvwizytowka.pl | {{ sender_email }}
```

---

## 📧 MAIL 3: Finalizacja + dostarczenie plików + prośba o testimonial
**Kiedy:** Po zaksięgowaniu płatności (lub natychmiast po akceptacji, jeśli płaci BLIKiem/instant)  
**Cel:** Potwierdzić zakończenie, przesłać pliki końcowe, dać instrukcję LinkedIn, poprosić o testimonial.

---

**Temat:** Gotowe! Twoje pliki + instrukcja LinkedIn – {{ name }} {{ surname }}

---

### Treść HTML:

```html
<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Finalizacja zamówienia</title>
</head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6;color:#1a1a2e;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;margin:0 auto;padding:40px 20px;">
    <tr>
      <td style="background:#ffffff;border-radius:12px;padding:40px;box-shadow:0 2px 8px rgba(0,0,0,0.05);">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td style="text-align:center;padding-bottom:24px;border-bottom:1px solid #e2e8f0;">
              <p style="margin:0 0 8px;font-size:12px;font-weight:600;color:#10b981;text-transform:uppercase;letter-spacing:0.1em;">Zakończone ✅</p>
              <h1 style="margin:0;font-size:24px;font-weight:700;color:#1a1a2e;">Płatność zaksięgowana. Oto Twoje pliki, {{ name }}!</h1>
            </td>
          </tr>
        </table>

        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="padding:24px 0;">
          <tr>
            <td>
              <p style="margin:0 0 24px;font-size:16px;">Dziękujemy za zaufanie i współpracę. W załącznikach / linkach poniżej masz wszystko, co potrzebujesz.</p>

              <!-- Download links -->
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:24px;">
                <tr>
                  <td style="padding-bottom:12px;">
                    <a href="{{ cv_pdf_url }}" style="display:inline-block;background:#2563eb;color:#ffffff;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;">📄 Pobierz CV (PDF)</a>
                  </td>
                </tr>
                <tr>
                  <td style="padding-bottom:12px;">
                    <a href="{{ cv_docx_url }}" style="display:inline-block;background:#10b981;color:#ffffff;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;">📝 Pobierz CV (DOCX)</a>
                  </td>
                </tr>
                <tr>
                  <td style="padding-bottom:12px;">
                    <a href="{{ qr_png_url }}" style="display:inline-block;background:#f59e0b;color:#ffffff;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;">📱 Pobierz kod QR (PNG)</a>
                  </td>
                </tr>
                <tr>
                  <td>
                    <a href="{{ site_url }}" style="display:inline-block;background:#6366f1;color:#ffffff;font-weight:600;padding:14px 28px;border-radius:8px;text-decoration:none;font-size:16px;">🔗 Twoja strona: {{ site_url }}</a>
                  </td>
                </tr>
              </table>

              <p style="margin:0 0 24px;font-size:14px;color:#6b7280;">Strona jest już live i będzie działać bezpłatnie na zawsze (GitHub Pages). Faktura VAT dołączona w załączniku.</p>

              <!-- LinkedIn Instruction -->
              <div style="background:#f0f9ff;border:1px solid #0ea5e9;border-radius:8px;padding:20px;margin-bottom:24px;">
                <h2 style="margin:0 0 16px;font-size:18px;font-weight:600;color:#0369a1;">📌 Jak dodać link do strony w LinkedIn (2 minuty)</h2>
                <ol style="margin:0;padding-left:20px;font-size:15px;color:#0369a1;">
                  <li style="margin-bottom:10px;">Wejdź na <a href="https://linkedin.com" style="color:#0ea5e9;">LinkedIn</a> → Twój profil → ikona ołówka (Edytuj profil).</li>
                  <li style="margin-bottom:10px;">Sekcja <strong>„Wyróżnione” (Featured)</strong> → kliknij „+” → „Dodaj link”.</li>
                  <li style="margin-bottom:10px;">Wklej: <code style="background:#ffffff;padding:2px 6px;border-radius:4px;font-size:13px;">{{ site_url }}</code></li>
                  <li style="margin-bottom:10px;">Tytuł: <strong>Moja strona internetowa CV</strong></li>
                  <li style="margin-bottom:10px;">Opis: <em>Profesjonalna wizytówka z portfolio, umiejętnościami i historią kariery. Kod QR na CV prowadzi tutaj.</em></li>
                  <li>Zapisz. Przeciągnij na górę sekcji „Wyróżnione”, by była widoczna od razu.</li>
                </ol>
                <p style="margin:16px 0 0;font-size:14px;"><strong>Pro tip:</strong> Dodaj link też w sekcji „Kontakt” (ikona globe) i w nagłówku profilu (Headline) – np. „Sales Director | Moja strona: cvwizytowka.pl/jan-kowalski”.</p>
              </div>

              <!-- Testimonial Request -->
              <div style="background:#fafafa;border:1px dashed #d1d5db;border-radius:8px;padding:20px;text-align:center;margin-bottom:24px;">
                <p style="margin:0 0 12px;font-size:15px;color:#374151;">🙏 <strong>Mamy małą prośbę:</strong></p>
                <p style="margin:0 0 16px;font-size:15px;color:#6b7280;">Jeśli jesteś zadowolony/a – napisz 2-3 zdania, jak strona pomogła Ci w rekrutacji (lub jak wygląda). Użyjemy jako case study (anonimowo lub z imieniem – Twoja decyzja). To nam bardzo pomaga.</p>
                <a href="mailto:{{ sender_email }}?subject=Testimonial%20-%20{{ name }}%20{{ surname }}&body=Cze%C5%9B%C4%87%2C%0A%0AChc%C4%99%20podzieli%C4%87%20si%C4%99%20opini%C4%85%3A%0A%0A%5BTwoje%20s%C5%82owa%5D%0A%0AZgoda%20na%20case%20study%3A%20TAK%20%2F%20NIE%20(anonimowo)%0A%0APozdrawiam%2C%0A{{ name }}" style="display:inline-block;background:#1a1a2e;color:#ffffff;font-weight:600;padding:12px 24px;border-radius:8px;text-decoration:none;font-size:15px;">📝 Napisz testimonial</a>
              </div>

              <hr style="border:none;border-top:1px solid #e2e8f0;margin:24px 0;">

              <p style="margin:0 0 8px;font-size:15px;">W razie pytań technicznych (domena, hosting, zmiany w przyszłości) – pisz śmiało na ten mail.</p>
              <p style="margin:0 0 8px;font-size:15px;">Trzymamy kciuki za rekrutację! 🤞</p>
              <p style="margin:24px 0 0;font-size:15px;">Pozdrawiamy,<br><strong>Zespół CV Wizytówka</strong></p>
            </td>
          </tr>
        </table>

        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-top:1px solid #e2e8f0;padding-top:24px;">
          <tr>
            <td style="font-size:12px;color:#9ca3af;text-align:center;">
              <p style="margin:0 0 4px;">{{ provider_name }}, NIP: {{ provider_nip }}</p>
              <p style="margin:0"><a href="https://cvwizytowka.pl/regulamin" style="color:#9ca3af;">Regulamin</a> | <a href="https://cvwizytowka.pl/polityka-prywatnosci" style="color:#9ca3af;">Polityka prywatności</a></p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

---

### Wersja plaintext:

```
Płatność zaksięgowana. Oto Twoje pliki, {{ name }}!

Dziękujemy za zaufanie. W załącznikach / linkach masz wszystko:

📄 CV (PDF): {{ cv_pdf_url }}
📝 CV (DOCX): {{ cv_docx_url }}
📱 Kod QR (PNG): {{ qr_png_url }}
🔗 Twoja strona: {{ site_url }}

Strona jest live i będzie działać za darmo na zawsze (GitHub Pages). Faktura VAT w załączniku.

📌 JAK DODAĆ LINK W LINKEDIN (2 min):
1. LinkedIn → Twój profil → Edytuj (ołówek).
2. Sekcja „Wyróżnione” (Featured) → „+” → „Dodaj link”.
3. Wklej: {{ site_url }}
4. Tytuł: Moja strona internetowa CV
5. Opis: Profesjonalna wizytówka z portfolio, umiejętnościami i historią kariery. Kod QR na CV prowadzi tutaj.
6. Zapisz i przenieś na górę sekcji.

Pro tip: Dodaj link też w sekcji Kontakt i w Headline profilu.

🙏 PROŚBA O TESTIMONIAL:
Jeśli jesteś zadowolony/a – napisz 2-3 zdania, jak strona pomogła. Użyjemy jako case study (anonimowo lub z imieniem – Twoja decyzja).
Odpowiedz na ten mail lub kliknij: mailto:{{ sender_email }}?subject=Testimonial%20-%20{{ name }}%20{{ surname }}

W razie pytań – pisz śmiało. Trzymamy kciuki za rekrutację! 🤞

Pozdrawiamy,
Zespół CV Wizytówka
cvwizytowka.pl | {{ sender_email }}
```

---

## 📧 MAIL 4 (opcjonalny): Przypomnienie o płatności – D+7 po akceptacji
**Kiedy:** Jeśli klient zaakceptował, ale nie zapłacił w ciągu 7 dni  
**Tone:** Przyjazne, bez presji, ale jasne.

---

**Temat:** Przypomnienie o płatności 899 zł – CV Wizytówka {{ name }} {{ surname }}

```html
<p>Cześć {{ name }},</p>
<p>Przypominamy, że po akceptacji strony ({{ acceptance_date }}) oczekujemy wpłaty <strong>899 zł</strong> na konto:</p>
<p>{{ provider_name }}<br>IBAN: {{ provider_iban }}<br>Tytuł: CV Wizytówka – {{ name }} {{ surname }}</p>
<p>Po wpłacie wyślemy fakturę i pliki końcowe (jeśli jeszcze nie miały Państwo).</p>
<p>Jeśli zapłaciliście – ignoruj ten mail (system mógł nie nadążyć zaksięgować).</p>
<p>Pozdrawiamy,<br>Zespół CV Wizytówka</p>
```

---

## 🔧 ZMIENNE DO PODMIANY (checklista przed wysłaniem)

| Zmienna | Źródło | Przykład |
|---------|--------|----------|
| `{{ name }}` | Tally form | „Jan” |
| `{{ surname }}` | Tally form | „Kowalski” |
| `{{ site_url }}` | Generator | `https://twojanazwa.github.io/cv-wizytowki/jan-kowalski/` |
| `{{ cv_pdf_url }}` | Generator / GitHub release | `https://github.com/.../jan-kowalski-cv.pdf` |
| `{{ cv_docx_url }}` | Generator | `https://github.com/.../jan-kowalski-cv.docx` |
| `{{ qr_png_url }}` | Generator | `https://github.com/.../jan-kowalski/qr.png` |
| `{{ delivery_date }}` | Skrypt (data + 5 dni rob.) | „2026-07-10” |
| `{{ acceptance_date }}` | Data maila 2 | „2026-07-08” |
| `{{ missing_materials }}` | Sprawdzanie briefu | „Brak zdjęcia profilowego, brak CV” |
| `{{ cv_status }}` / `{{ photo_status }}` / `{{ portfolio_status }}` | „Otrzymano” / „Brak” |
| `{{ sender_email }}` | Konfiguracja | `kontakt@cvwizytowka.pl` |
| `{{ provider_name }}` | Firma | „Jan Kowalski Consulting” |
| `{{ provider_nip }}` | Firma | `123-456-78-90` |
| `{{ provider_iban }}` | Konto firmowe | `PL 1234 5678 9012 3456 7890 1234` |
| `{{ provider_address }}` | Firma | `ul. Przykładowa 1, 00-001 Warszawa` |

---

## 🛠 IMPLEMENTACJA (szybko, bez kodowania)

1. **Tally.so → Webhook → Make.com (free) / n8n / Zapier** → wysyła Mail 1 (HTML + text).
2. **Mail 2, 3, 4** – wysyłasz ręcznie z Gmaila / Outlooka (szablony w Canned Responses / Quick Parts) – to daje ludzki touch i kontrolę.
   - Dlaczego ręcznie? Bo chcesz sprawdzić pliki przed wysłaniem, dopisać osobistą notatkę („Fajne doświadczenie w X!”), a przy 5–10 klientach/mies to 15 min/dzień.
3. Gdy przeskalujesz (>20 zamówień/mies) – automatyzujesz Mail 2 i 3 przez Make.com + Gmail API.

---

## ✅ CHECKLISTA PRZED WYSŁANIEM KAŻDEGO MAILA

- [ ] Wszystkie `{{ zmienne }}` podmienione
- [ ] Linki działają (kliknij testowo)
- [ ] Załączniki (faktura, pliki) dodane
- [ ] Temat < 50 znaków, bez spamu-słów („Gratis”, „Promocja”, „!!!”)
- [ ] Adres nadawcy: `Kontakt CV Wizytówka <kontakt@cvwizytowka.pl>` (domena z DKIM/SPF/DMARC)
- [ ] Test na telefonie (Gmail App, iOS Mail) – czy przyciski nie uciekają
- [ ] Plaintext wersja poprawna (kopiuj z powyższych szablonów)
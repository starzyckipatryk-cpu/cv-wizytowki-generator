# Regulamin Usługi „CV Wizytówka”

**Wersja:** 1.0  
**Data wejścia w życie:** {{ current_date }}  
**Dostawca:** {{ provider_name }} (NIP: {{ provider_nip }}, REGON: {{ provider_regon }})  
**Adres do korespondencji:** {{ provider_address }}  
**E-mail:** {{ provider_email }}  
**Strona internetowa:** https://cvwizytowka.pl  

---

## § 1. Postanowienia wstępne

1. Niniejszy Regulamin określa zasady świadczenia usług przez Dostawcę na rzecz Klientów oraz prawa i obowiązki Stron.
2. Klientem w rozumieniu Regulaminu może być wyłącznie osoba fizyczna dokonująca zamówienia w celu realizacji usługi związanej z poszukiwaniem pracy (konsument w rozumieniu Kodeksu cywilnego).
3. Składanie zamówienia jest równoważne z akceptacją Regulaminu w całości.
4. W sprawach nieuregulowanych w Regulaminie mają zastosowanie przepisy Kodeksu cywilnego, ustawy o prawach konsumenta, ustawy o świadczeniu usług drogą elektroniczną oraz RODO.

---

## § 2. Przedmiot usługi

1. Usługa polega na przygotowaniu i dostarczeniu Klientowi:
   a) **Strony internetowej wizytówki (CV Website)** – statycznej strony HTML/CSS/JS hostowanej na GitHub Pages pod adresem `https://{{ github_username }}.github.io/cv-wizytowki/{{ slug }}/` (lub na custom domenie Klienta – zob. § 6 ust. 3), zawierającej sekcje: Hero (zdjęcie, imię, stanowisko), O mnie, Doświadczenie (timeline), Umiejętności, Portfolio (opcjonalnie), Kontakt, kod QR.
   b) **Plików CV** w formatach PDF oraz DOCX (Microsoft Word), zgodnych z ATS, z wklejonym kodem QR prowadzącym do strony internetowej.
   c) **Pliku graficznego kodu QR** (PNG, 300 DPI) do samodzielnego wykorzystania.

2. Usługa **nie obejmuje**: copywritingu treści „O mnie” ani opisów doświadczenia od zera (Klient dostarcza surowe materiały), sesji fotograficznej, zakupu custom domeny (opcjonalnie – zob. § 6 ust. 3), hostingow po stronie Klienta (hosting jest świadczony przez GitHub Pages bezpłatnie), wsparcia technicznego po upływie 12 miesięcy od dostarczenia.

---

## § 3. Proces zamawiania i realizacji

1. **Zamówienie:** Klient wypełnia formularz briefowy na stronie https://cvwizytowka.pl (Tally.so), przesyła CV (PDF/DOCX), zdjęcie profilowe oraz ewentualne zdjęcia do portfolio.
2. **Potwierdzenie:** W ciągu 24h roboczych Klient otrzymuje e-mail z potwierdzeniem przyjęcia zamówienia do realizacji oraz terminem planowanego dostarczenia.
3. **Realizacja:** Dostawca przygotowuje stronę i CV w terminie do **5 dni roboczych** odebrania kompletnych materiałów (briefer + CV + zdjęcia). Wariant Express (48h) dostępny za dopłatą 200 zł – należy o nim poinformować przed płatnością.
4. **Wersja do akceptacji:** Klient otrzymuje e-mail z:
   - linkiem do wersji live strony (GitHub Pages),
   - załącznikami CV (PDF + DOCX),
   - prośbą o feedback w ciągu 48h.
5. **Poprawki:** W cenie usługi zawarta jest **jedna runda poprawek** (maksymalnie 3 zmiany: tekst, zdjęcie, kolejność sekcji, drobne style). Każda kolejna runda lub zmiana przekraczająca 3 punkty = 150 zł/h.
6. **Akceptacja i płatność:** Po akceptacji (lub upływie 48h bez uwag – co jest równoznaczne z akceptacją) Klient przelewa kwotę **899 zł brutto** na konto bankowe podane w e-mailu. Tytuł przelewu: „CV Wizytówka – {{ name }} {{ surname }}”.
7. **Finalizacja:** Po zaksięgowaniu płatności Dostawca wysyła e-mail z:
   - potwierdzeniem zakończenia,
   - plikami CV (PDF + DOCX) do pobrania,
   - instrukcją „Jak dodać link do strony w LinkedIn”,
   - prośbą o testimonial (dobrowolne).

---

## § 4. Cena i płatności

1. Cena usługi: **899 zł brutto** (jednorazowo, VAT 23% – faktura VAT wystawiana po wpłacie).
2. Płatność **wyłącznie po akceptacji** gotowej pracy (brak zaliczki na etapie zamówienia).
3. Forma płatności: przelew bankowy na konto firmowe Dostawcy (BLIK możliwy po uzgodnieniu).
4. Termin płatności: 7 dni kalendarzowych od daty akceptacji / wysłania e-maila finalizującego.
5. W przypadku opóźnienia płatności Dostawca zastrzega sobie prawo do wstrzymania dostępu do plików źródłowych oraz wystawienia wezwania do zapłaty z odsetkami ustawowymi.

---

## § 5. Własność i prawa do plików

1. Po pełnej opłacie Klient otrzymuje **pełne, wyłączne, nieograniczone w czasie i terytorium prawa autorskie majątkowe** do przygotowanych plików: HTML/CSS/JS strony, PDF CV, DOCX CV, PNG QR.
2. Kod źródłowy strony jest hostowany w **publicznym repozytorium GitHub** (widoczny każdemu). Klient akceptuje ten fakt bezpłatnie. Na życzenie Klienta (za dopłatą 100 zł) Dostawca może przenieść repozytorium na prywatne (GitHub Private Pages) lub przekazać pliki do samodzielnego hostingu.
3. Dostawca zastrzega sobie prawo do wykorzystania zrzutów ekranu strony oraz anonimizowanych fragmentów CV jako **case study** w celach marketingowych (portfolio, landing page, LinkedIn), chyba że Klient w formularzu briefowym zaznaczy pole „Nie zgadzam się na case study”.

---

## § 6. Hosting, domena i dostępność

1. Strona jest hostowana na **GitHub Pages** (SLA GitHub, 99.9% uptime rocznie). Hosting jest **bezpłatny na zawsze** (brak opłat rocznych).
2. Dostawca nie ponosi odpowiedzialności za przestoje GitHub Pages, ataki DDoS, zmiany w warunkach usługi GitHub.
3. **Custom domena (opcjonalnie):** Klient może zakupić własną domenę (np. jan-kowalski.pl) u dowolnego rejestratora (~50–80 zł/rok). Dostawca konfiguruje DNS w Cloudflare (CNAME + proxy + SSL) za jednorazową opłatą **150 zł**. Opłaty odnowienia domeny pokrywa Klient bezpośrednio u rejestratora.
4. W przypadku braku płatności za odnowienie domeny przez Klienta, strona wciąż działa pod adresem GitHub Pages.

---

## § 7. Prawo odstąpienia od umowy (konsument)

1. Zgodnie z art. 38 ust. 13 ustawy o prawach konsumenta, w przypadku umów na świadczenie usług cyfrowych nie zapisanych na nośniku materialnym, konsument **traci prawo odstąpienia od umowy**, jeśli:
   - wykonawca rozpoczął realizację z wyrażoną zgodą konsumenta, oraz
   - konsument potwierdził, że jest świadomy, że po rozpoczęciu realizacji traci prawo odstąpienia.
2. **W formularzu briefowym Klient zaznacza pole:** „Wyrażam zgodę na rozpoczęcie realizacji usługi przed upływem 14 dni od zawarcia umowy i przyznaję, że po rozpoczęciu realizacji tracę prawo odstąpienia od umowy.”
3. Jeśli Klient **nie wyrazi takiej zgody**, Dostawca rozpocznie realizację po upływie 14 dni od zamówienia.

---

## § 8. Ochrona danych osobowych (RODO)

1. Administratorem danych osobowych jest Dostawca.
2. Dane (imię, nazwisko, e-mail, telefon, LinkedIn, CV, zdjęcia) przetwarzane są na podstawie:
   - art. 6 ust. 1 lit. b RODO (realizacja umowy),
   - art. 6 ust. 1 lit. a RODO (zgoda na case study, marketing – dobrowolne).
3. Dane przechowywane są **do 12 miesięcy** po zakończeniu usługi, po czym usuwane (z wyjątkiem danych fakturowych – 5 lat z uwzględnieniem przepisów podatkowych).
4. Klient ma prawo dostępu, sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia danych oraz wniesienia skargi do PUODO.
5. Kontakt w sprawach RODO: {{ provider_email }}.

---

## § 9. Odpowiedzialność i reklamacje

1. Dostawca odpowiada za wady usługi zgodnie z przepisami Kodeksu cywilnego o ręce miarowej (usługa) oraz odpowiedzialności za wady w towarze (pliki cyfrowe).
2. Reklamacje kieruje się na adres e-mail {{ provider_email }}. Czas rozpatrzenia: do 14 dni roboczych.
3. Dostawca nie odpowiada za:
   - błędy w treściach dostarczonych przez Klienta (ortografia, prawda merytoryczna),
   - niezgodność CV z wymaganiami konkretnego systemu ATS (usługa to optymalizacja ogólna, nie gwarancja przejścia),
   - decyzje rekruterów lub pracodawców.

---

## § 10. Postanowienia końcowe

1. Zmiany Regulaminu mogą nastąpić w dowolnym czasie; do zamówień złożonych przed zmianą stosuje się wersję obowiązującą w dniu zamówienia.
2. Sąd właściwy: sąd powszechny właściwy dla siedziby Dostawcy (dla konsumentów – również sąd miejsca zamieszkania).
3. Przepisy Regulaminu nie wykluczają ani nie ograniczają praw konsumenta wynikających z przepisów przymuszających prawa.

---

**Zaakceptowanie Regulaminu następuje poprzez zaznaczenie checkboxa w formularzu briefowym Tally.so.**

---

# Polityka Prywatności (RODO)

**Wersja:** 1.0  
**Data aktualizacji:** {{ current_date }}  
**Administrator:** {{ provider_name }}, NIP: {{ provider_nip_nip}}, e-mail: {{ provider_email }}

## 1. Kto jest Administratorem Twoich danych?

Administratorem Twoich danych osobowych jest **{{ provider_name }}** (dalej: „Administrator”), prowadzący działalność gospodarczą pod NIP {{ provider_nip }}, z siedzibą w {{ provider_address }}. Kontakt: {{ provider_email }}.

## 2. Jakie dane przetwarzamy i skąd je pobieramy?

Przetwarzamy dane, które **sam/a nam podajesz** w formularzu briefowym (Tally.so) oraz w przesyłanych plikach:
- Imię i nazwisko
- Adres e-mail
- Numer telefonu (opcjonalnie)
- Link do profilu LinkedIn
- Treść sekcji „O mnie”
- Historia zatrudnienia (nazwy firm, stanowiska, okresy, opis osiągnięć)
- Umiejętności
- Zdjęcie profilowe
- Zdjęcia do portfolio (opcjonalnie)
- Plik CV (PDF/DOCX)

**Nie pobieramy danych z innych źródeł.**

## 3. Na jakiej podstawie i do jakich celów przetwarzamy dane?

| Cel | Podstawa prawna (RODO) | Okres przechowywania |
|-----|------------------------|----------------------|
| Realizacja usługi (tworzenie strony, CV, QR) | Art. 6 ust. 1 lit. b – wykonanie umowy | Do zakończenia usługi + 12 miesięcy |
| Wystawianie faktury, ewidencja księgowa | Art. 6 ust. 1 lit. c – obowiązek prawny | 5 lat (przepisy podatkowe) |
| Komunikacja z Klientem (e-maile, telefon) | Art. 6 ust. 1 lit. b – wykonanie umowy | Do 12 mies. po zakończeniu |
| Case study / portfolio (jeśli wyraziłeś zgodę) | Art. 6 ust. 1 lit. a – zgoda | Do cofnięcia zgody (możesz cofnąć w każdej chwili) |
| Marketing bezpośredni / newsletter (jeśli wyraziłeś zgodę) | Art. 6 ust. 1 lit. a – zgoda | Do cofnięcia zgody |

## 4. Czy przekazujemy dane innym podmiotom?

Tak, w następujących przypadkach:
- **Tally.so** (formularz briefowy) – processor danych, zgodnie z DPA.
- **GitHub / Microsoft** (hosting strony w publicznym repozytorium) – dane widoczne publicznie na stronie (imię, nazwisko, stanowisko, LinkedIn, e-mail, zdjęcie, umiejętności, doświadczenie). Akceptujesz to w Regulaminie § 5 ust. 2.
- **Cloudflare** (DNS + SSL dla custom domeny) – tylko jeśli zamawiasz custom domenę.
- **System księgowy (inFakt / wFirma)** – dane na fakturze.
- **Urząd Skarbowy / ZUS** – w zakresie wynikającym z przepisów.

**Nie sprzedajemy danych. Nie przekazujemy ich do celów marketingowych firmom trzecim.**

## 5. Transfer danych poza EOG

GitHub (USA) i Cloudflare (USA) przetwarzają dane w USA. Transfer opiera się na **Standardowych Klauzulach Umownych (SCC)** oraz decyzji Angemessenheitsbeschluss UE-USA (Data Privacy Framework). Tally.so – serwery w UE.

## 6. Twoje prawa

Masz prawo:
1. **Dostępu** do swoich danych (kopia).
2. **Sprostowania** – jeśli dane są nieaktualne.
3. **Usunięcia** („być zapomnianym”) – po zakończeniu usługi i upływie obowiązków księgowych (możesz poprosić o usunięcie danych nietechnicznych wcześniej).
4. **Ograniczenia przetwarzania**.
5. **Przenoszenia danych** (w formacie CSV/JSON).
6. **Wniesienia sprzeciwu** wobec przetwarzania na podstawie art. 6 ust. 1 lit. f (uzasadniony interes) – nie stosujemy tej podstawy.
7. **Cofnięcia zgody** w dowolnym momencie (dotyczy case study / marketingu) – cofnięcie nie wpływa na legalność przetwarzania przed cofnięciem.
8. **Skargi do PUODO** (Prezes Urzędu Ochrony Danych Osobowych, ul. Stawki 2, 00-193 Warszawa).

Wydarzenie praw: napisz do {{ provider_email }}. Odpowiemy w ciągu 30 dni.

## 7. Automatyczne decyzyjne i profilowanie

**Nie stosujemy** automatycznych procesów decyzyjnych ani profilowania.

## 8. Pliki cookies i technologie śledzące

Na stronie Klienta (GitHub Pages) **nie używamy ciasteczek, pikseli, Google Analytics, Facebook Pixel ani żadnych skryptów trackingowych**. Strona jest w 100% statyczna.

Na landing page (cvwizytowka.pl, Carrd.co) mogą być pliki cookies niezbędne do działania formularza i Stripe (jeśli aktywny). Carrd ma własną politykę cookies.

## 9. Bezpieczeństwo danych

Stosujemy środki techniczne i organizacyjne: szyfrowanie SSL/TLS (HTTPS), dostęp do danych tylko uprawnionym osobom, kopie zapasowe, silne hasła, 2FA na kontach GitHub, Tally, e-mail, systemie księgowym.

## 10. Zmiany polityki

Polityka może zostać zaktualizowana. O zmianach poinformujemy e-mailem (jeśli masz konto/zamówienie) lub opublikujemy nową wersję na tej stronie z datą aktualizacji.

---

**Kontakt w sprawach RODO:** {{ provider_email }}  
**Data ostatniej aktualizacji:** {{ current_date }}
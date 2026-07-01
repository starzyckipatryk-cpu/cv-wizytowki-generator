# Arkusz KPI – CV Wizytówka (Google Sheets Setup)

**Link do gotowego arkusza:** [Utwórz kopię z szablonu](#) → *po utworzeniu plików poniżej, zaimportuj CSV do nowego arkusza*

---

## 📊 STRUKTURA ARKUSZA (zakładki)

| Zakładka | Cel |
|----------|-----|
| **`Pipeline`** | Główna tabela leadów – jeden wiersz = jeden kontakt |
| **`Dashboard`** | Podsumowania, wykresy, KPI tygodniowe/miesięczne |
| **`Outreach_Stats`** | Szczegółowe statystyki cold outreach (LinkedIn) |
| **`Settings`** | Konfiguracja: cele, progi, kolory, listy rozwijane |

---

## 🗂 ZAKŁADKA 1: `Pipeline` – Główna tabela

### Kolumny (A:AF) – kopiuj nagłówki do wiersza 1:

| Kol | Nagłówek | Typ | Walidacja / Uwagi |
|-----|----------|-----|-------------------|
| A | **Data dodania** | Date | `=TODAY()` default, format: `YYYY-MM-DD` |
| B | **Imię** | Text | |
| C | **Nazwisko** | Text | |
| D | **Stanowisko** | Text | np. "Sales Director", "IT Project Manager" |
| E | **Firma (aktualna)** | Text | |
| F | **LinkedIn URL** | URL | Walidacja: `=REGEXMATCH(F2,"linkedin\.com/in/")` |
| G | **Źródło leadu** | List | `LinkedIn Cold`, `LinkedIn InMail`, `Referral`, `Facebook Group`, `Organic`, `Inne` |
| H | **Segment** | List | `C-level`, `Director`, `Manager`, `Senior IC`, `Inne` |
| I | **Zaproszenie wysłane** | Checkbox | TRUE/FALSE |
| J | **Data zaproszenia** | Date | Jeśli I=TRUE → data, else puste |
| K | **Zaproszenie przyjęte** | Checkbox | |
| L | **Data przyjęcia** | Date | |
| M | **1. wiadomość wysłana** | Checkbox | |
| N | **Data 1. wiad.** | Date | |
| O | **Szablon wiadomości** | List | `A - Curiosity`, `B - Social Proof`, `C - Pain/Stat` |
| P | **Odpowiedź otrzymana** | Checkbox | |
| Q | **Data odpowiedzi** | Date | |
| R | **Demo / Link wysłany** | Checkbox | |
| S | **Data demo** | Date | |
| T | **Akceptacja (tak/nie)** | List | `Tak`, `Nie`, `Oczekuje`, `Zrezygnował` |
| U | **Data akceptacji** | Date | |
| V | **Płatność wpłacona** | Checkbox | |
| W | **Data płatności** | Date | |
| X | **Przychód (PLN)** | Number | `=IF(V2=TRUE,899,0)` |
| Y | **Czas produkcji (min)** | Number | Ręcznie wpisujesz po zrobieniu |
| Z | **Testimonial zebrany** | Checkbox | |
| AA | **Case study zgoda** | List | `Tak - z imieniem`, `Tak - anonimowo`, `Nie` |
| AB | **Uwagi** | Text | Długie notatki |
| AC | **Tydzień roku** | Formula | `=WEEKNUM(A2)` |
| AD | **Miesiąc** | Formula | `=TEXT(A2,"YYYY-MM")` |
| AE | **Status ogólny** | Formula | (patrz niżej) |
| AF | **Dni w pipeline** | Formula | `=IF(V2=TRUE, W2-A2, TODAY()-A2)` |

---

### Formuły w wierszu 2 (przeciągnij w dół na 1000 wierszy):

**AC2 (Tydzień roku):**
```excel
=IF(A2="","",WEEKNUM(A2))
```

**AD2 (Miesiąc):**
```excel
=IF(A2="","",TEXT(A2,"YYYY-MM"))
```

**AE2 (Status ogólny – automatyczny):**
```excel
=IFS(
  V2=TRUE, "💰 ZAMKNIETE",
  T2="Nie", "❌ ODRZUCONE",
  T2="Zrezygnował", "🚫 ZREZYGNOWAŁ",
  R2=TRUE, "🎯 DEMO WYSŁANE",
  P2=TRUE, "💬 ROZMOWA",
  K2=TRUE, "✅ POŁĄCZONY",
  I2=TRUE, "📤 ZAPROSZENIE",
  TRUE, "🆕 NOWY"
)
```

**AF2 (Dni w pipeline):**
```excel
=IF(A2="","",IF(V2=TRUE, W2-A2, TODAY()-A2))
```

**X2 (Przychód – auto):**
```excel
=IF(V2=TRUE, 899, 0)
```

---

### Formatowanie warunkowe (Pipeline – zaznacz A2:AF1000):

| Zasaka | Zakres | Format |
|--------|--------|--------|
| **Status = "💰 ZAMKNIETE"** | `$AE2:$AE1000` | Tło: `#d1fae5`, Czcionka: `#065f46`, Pogrubienie |
| **Status = "❌ ODRZUCONE"** | `$AE2:$AE1000` | Tło: `#fee2e2`, Czcionka: `#991b1b` |
| **Status = "🚫 ZREZYGNOWAŁ"** | `$AE2:$AE1000` | Tło: `#fef3c7`, Czcionka: `#92400e` |
| **Status = "🎯 DEMO WYSŁANE"** | `$AE2:$AE1000` | Tło: `#dbeafe`, Czcionka: `#1e40af` |
| **Status = "💬 ROZMOWA"** | `$AE2:$AE1000` | Tło: `#e0e7ff`, Czcionka: `#312e81` |
| **Status = "✅ POŁĄCZONY"** | `$AE2:$AE1000` | Tło: `#f3f4f6`, Czcionka: `#374151` |
| **Dni w pipeline > 30** | `$AF2:$AF1000` | Tekst: czerwony, pogrubiony (stare leady) |
| **Płatność = TRUE** | `$V2:$V1000` | Ikona ✅ (Format > Liczba > Format niestandardowy: `✅;;`) |

---

### Walidacja danych (Data > Data validation):

| Kolumna | Kryteria | Źródło / Lista |
|---------|----------|----------------|
| G (Źródło) | List from a range | `Settings!$B$2:$B$7` |
| H (Segment) | List from a range | `Settings!$C$2:$C$6` |
| O (Szablon) | List from a range | `Settings!$D$2:$D$4` |
| T (Akceptacja) | List from a range | `Settings!$E$2:$E$5` |
| AA (Case study) | List from a range | `Settings!$F$2:$F$4` |

---

## 📈 ZAKŁADKA 2: `Dashboard` – Podsumowania i wykresy

### Sekcja A: KPI Tygodniowe (wiersze 1-20)

| Komórka | Metryka | Formuła |
|---------|---------|---------|
| B3 | **Zaproszenia w tym tygodniu** | `=COUNTIFS(Pipeline!$J$2:$J,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$J$2:$J,"<="&TODAY())` |
| B4 | **Przyjęte zaproszenia** | `=COUNTIFS(Pipeline!$L$2:$L,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$L$2:$L,"<="&TODAY())` |
| B5 | **Acceptance rate (%)** | `=IF(B3=0,0,B4/B3)` → Format % |
| B6 | **Odpowiedzi** | `=COUNTIFS(Pipeline!$Q$2:$Q,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$Q$2:$Q,"<="&TODAY())` |
| B7 | **Reply rate (% od przyjętych)** | `=IF(B4=0,0,B6/B4)` → Format % |
| B8 | **Demo wysłane** | `=COUNTIFS(Pipeline!$S$2:$S,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$S$2:$S,"<="&TODAY())` |
| B9 | **Sprzedaże (zamknięte)** | `=COUNTIFS(Pipeline!$W$2:$W,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$W$2:$W,"<="&TODAY())` |
| B10 | **Konwersja Lead→Sale (%)** | `=IF(B3=0,0,B9/B3)` → Format % |
| B11 | **Przychód w tym tygodniu** | `=SUMIFS(Pipeline!$X$2:$X, Pipeline!$W$2:$W,">="&TODAY()-WEEKDAY(TODAY(),2)+1, Pipeline!$W$2:$W,"<="&TODAY())` |
| B12 | **Średni czas produkcji (min)** | `=AVERAGEIFS(Pipeline!$Y$2:$Y, Pipeline!$V$2:$V, TRUE, Pipeline!$W$2:$W,">="&TODAY()-WEEKDAY(TODAY(),2)+1)` |

### Sekcja B: KPI Miesięczne (wiersze 22-40) – analogicznie z `EOMONTH`

| Komórka | Metryka | Formuła |
|---------|---------|---------|
| B24 | **Zaproszenia w miesiącu** | `=COUNTIFS(Pipeline!$AD$2:$AD, TEXT(TODAY(),"YYYY-MM"))` |
| B25 | **Przyjęte** | `=COUNTIFS(Pipeline!$AD$2:$AD, TEXT(TODAY(),"YYYY-MM"), Pipeline!$K$2:$K, TRUE)` |
| B26 | **Acceptance rate** | `=IF(B24=0,0,B25/B24)` |
| B27 | **Sprzedaże** | `=COUNTIFS(Pipeline!$AD$2:$AD, TEXT(TODAY(),"YYYY-MM"), Pipeline!$V$2:$V, TRUE)` |
| B28 | **Przychód miesiąc** | `=SUMIFS(Pipeline!$X$2:$X, Pipeline!$AD$2:$AD, TEXT(TODAY(),"YYYY-MM"), Pipeline!$V$2:$V, TRUE)` |
| B29 | **Cel sprzedaży (8/mies)** | `8` (ręcznie) |
| B30 | **Realizacja celu (%)** | `=B27/B29` → Format % |

### Sekcja C: Analiza szablonów wiadomości (wiersze 42-55)

| Komórka | Metryka | Formuła |
|---------|---------|---------|
| B43 | **Szablon A - Wysłane** | `=COUNTIFS(Pipeline!$O$2:$O,"A - Curiosity", Pipeline!$M$2:$M, TRUE)` |
| C43 | **Szablon A - Odpowiedzi** | `=COUNTIFS(Pipeline!$O$2:$O,"A - Curiosity", Pipeline!$P$2:$P, TRUE)` |
| D43 | **Szablon A - Reply rate** | `=IF(B43=0,0,C43/B43)` |
| E43 | **Szablon A - Sprzedaże** | `=COUNTIFS(Pipeline!$O$2:$O,"A - Curiosity", Pipeline!$V$2:$V, TRUE)` |
| F43 | **Szablon A - Konwersja** | `=IF(B43=0,0,E43/B43)` |
| (B44:F44) | **Szablon B - Social Proof** | Analogicznie |
| (B45:F45) | **Szablon C - Pain/Stat** | Analogicznie |

### Sekcja D: Wykresy (Insert > Chart)

1. **Funnel tygodniowy:** Kolumnowy z B3, B4, B6, B8, B9 (Zaproszenia → Przyjęte → Odpowiedzi → Demo → Sale)
2. **Trend przychodów miesięczny:** Liniowy z `Dashboard!B28` (kopiuj wartości co tydzień do nowej kolumny lub użyj Tabela przestawna)
3. **Porównanie szablonów:** Słupkowy z D43:D45 (Reply rate per szablon)
4. **Pipeline status count:** Kołowy z `=QUERY(Pipeline!AE2:AE, "select AE, count(AE) where AE != '' group by AE label count(AE) 'Liczba'")`

---

## 📋 ZAKŁADKA 3: `Outreach_Stats` – Codzienny log outreachu

### Kolumny (A:J):

| Kol | Nagłówek | Typ |
|-----|----------|-----|
| A | Data | Date |
| B | Godzina rozpoczęcia | Time |
| C | Liczba zaproszeń wysłanych | Number |
| D | Liczba zaproszeń z wiadomością | Number |
| E | Szablon użyty (A/B/C/Mix) | List |
| F | Liczba odpowiedzi otrzymanych (w tym dniu) | Number |
| G | Liczba follow-upów wysłanych | Number |
| H | Czas poświęcony (min) | Number |
| I | Uwagi | Text |
| J | Tydzień | Formula `=WEEKNUM(A2)` |

### Formuły podsumowujące (wiersz 1 lub osobny zakres):

| Metryka | Formuła |
|---------|---------|
| **Śr. zaproszeń/dzień (tydzień)** | `=AVERAGEIFS(C:C, J:J, WEEKNUM(TODAY()))` |
| **Śr. czas/dzień** | `=AVERAGEIFS(H:H, J:J, WEEKNUM(TODAY()))` |
| **Łączne zaproszenia tydzień** | `=SUMIFS(C:C, J:J, WEEKNUM(TODAY()))` |
| **Łączne odpowiedzi tydzień** | `=SUMIFS(F:F, J:J, WEEKNUM(TODAY()))` |

---

## ⚙️ ZAKŁADKA 4: `Settings` – Konfiguracja (ukryta dla porządku)

### Wiersze 1-10 (nagłówki w wierszu 1):

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **Parametr** | **Źródła leadów** | **Segments** | **Szablony wiadomości** | **Statusy akceptacji** | **Case study zgody** |
| 1 | LinkedIn Cold | C-level | A - Curiosity | Tak | Tak - z imieniem |
| 2 | LinkedIn InMail | Director | B - Social Proof | Nie | Tak - anonimowo |
| 3 | Referral | Manager | C - Pain/Stat | Oczekuje | Nie |
| 4 | Facebook Group | Senior IC | | Zrezygnował | |
| 5 | Organic | Inne | | | |
| 6 | Inne | | | | |

### Cele (wiersze 12-20):

| A | B | C |
|---|---|---|
| **Cel** | **Wartość** | **Opis** |
| Zaproszenia / tydzień | 150 | Minimum do wysłania |
| Acceptance rate cel | 25% | Próg alarmowy <15% |
| Reply rate cel | 15% | Próg alarmowy <5% |
| Demo / tydzień | 5 | |
| Sprzedaże / tydzień | 2 | |
| Sprzedaże / miesiąc | 8 | Cel realny |
| Czas produkcji cel | 30 min | Po automatyzacji |
| Przychód / miesiąc | 7192 PLN | 8 × 899 |

---

## 📥 IMPORT GOTOWEGO ARKUSZA (CSV)

Skopiuj poniższy CSV do pliku `kpi_template.csv` i zaimportuj w Google Sheets: **File > Import > Upload > Replace spreadsheet**.

```csv
Data dodania,Imię,Nazwisko,Stanowisko,Firma (aktualna),LinkedIn URL,Źródło leadu,Segment,Zaproszenie wysłane,Data zaproszenia,Zaproszenie przyjęte,Data przyjęcia,1. wiadomość wysłana,Data 1. wiad.,Szablon wiadomości,Odpowiedź otrzymana,Data odpowiedzi,Demo / Link wysłany,Data demo,Akceptacja (tak/nie),Data akceptacji,Płatność wpłacona,Data płatności,Przychód (PLN),Czas produkcji (min),Testimonial zebrany,Case study zgoda,Uwagi,Tydzień roku,Miesiąc,Status ogólny,Dni w pipeline
,,,,,,,,FALSE,,FALSE,,FALSE,,FALSE,,FALSE,,,,FALSE,,0,,FALSE,,,,=WEEKNUM(A2),=TEXT(A2,"YYYY-MM"),=IFS(V2=TRUE,"💰 ZAMKNIETE",T2="Nie","❌ ODRZUCONE",T2="Zrezygnował","🚫 ZREZYGNOWAŁ",R2=TRUE,"🎯 DEMO WYSŁANE",P2=TRUE,"💬 ROZMOWA",K2=TRUE,"✅ POŁĄCZONY",I2=TRUE,"📤 ZAPROSZENIE",TRUE,"🆕 NOWY"),=IF(A2="","",IF(V2=TRUE,W2-A2,TODAY()-A2))
```

> **Uwaga:** Formuły w kolumnach AC, AD, AE, AF nie zaimportują się jako formuły – po imporcie wpisz je ręcznie w wierszu 2 i przeciągnij w dół.

---

## 🔄 AUTOMATYZACJA ODŚWIEŻANIA (Apps Script)

Dodaj w Google Sheets: **Extensions > Apps Script** → wklej:

```javascript
/**
 * CV Wizytówka KPI - Auto-refresh Dashboard
 * Uruchamia się co godzinę (triggers)
 */

function refreshDashboard() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var dashboard = ss.getSheetByName('Dashboard');
  var pipeline = ss.getSheetByName('Pipeline');
  
  if (!dashboard || !pipeline) return;
  
  // Wymuś przeliczenie formuł
  SpreadsheetApp.flush();
  
  // Opcjonalnie: zapisz snapshot tygodniowy do historii
  saveWeeklySnapshot();
}

function saveWeeklySnapshot() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var history = ss.getSheetByName('History') || ss.insertSheet('History');
  var dashboard = ss.getSheetByName('Dashboard');
  
  var week = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'YYYY-w');
  var revenue = dashboard.getRange('B11').getValue(); // Przychód tydzień
  var sales = dashboard.getRange('B9').getValue();    // Sprzedaże tydzień
  var invites = dashboard.getRange('B3').getValue();  // Zaproszenia tydzień
  var accepted = dashboard.getRange('B4').getValue(); // Przyjęte
  
  var lastRow = history.getLastRow() + 1;
  history.getRange(lastRow, 1, 1, 5).setValues([[week, invites, accepted, sales, revenue]]);
  
  // Nagłówki jeśli pierwszy raz
  if (lastRow === 2) {
    history.getRange(1, 1, 1, 5).setValues([['Tydzień', 'Zaproszenia', 'Przyjęte', 'Sprzedaże', 'Przychód (PLN)']])
      .setFontWeight('bold').setBackground('#1a1a2e').setFontColor('#ffffff');
  }
}

function createTriggers() {
  // Usuń stare
  ScriptApp.getProjectTriggers().forEach(function(t) { ScriptApp.deleteTrigger(t); });
  // Co godzinę w dni robocze 8-18
  ScriptApp.newTrigger('refreshDashboard')
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .onWeekDay(ScriptApp.WeekDay.TUESDAY)
    .onWeekDay(ScriptApp.WeekDay.WEDNESDAY)
    .onWeekDay(ScriptApp.WeekDay.THURSDAY)
    .onWeekDay(ScriptApp.WeekDay.FRIDAY)
    .atHour(8)
    .create();
  ScriptApp.newTrigger('refreshDashboard')
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .onWeekDay(ScriptApp.WeekDay.TUESDAY)
    .onWeekDay(ScriptApp.WeekDay.WEDNESDAY)
    .onWeekDay(ScriptApp.WeekDay.THURSDAY)
    .onWeekDay(ScriptApp.WeekDay.FRIDAY)
    .atHour(12)
    .create();
  ScriptApp.newTrigger('refreshDashboard')
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .onWeekDay(ScriptApp.WeekDay.TUESDAY)
    .onWeekDay(ScriptApp.WeekDay.WEDNESDAY)
    .onWeekDay(ScriptApp.WeekDay.THURSDAY)
    .onWeekDay(ScriptApp.WeekDay.FRIDAY)
    .atHour(16)
    .create();
}
```

**Uruchom raz:** `createTriggers()` → autoryzuj → gotowe.

---

## 📱 SZYBKI WPIS DANYCH (Mobile-friendly)

1. **Google Sheets App** na telefonie – edytujesz w tramwaju/przerwie.
2. **Skrót na pulpicie** do arkusza (Chrome > Menu > Add to Home Screen).
3. **Checkboxy** – tapnięcie zmienia TRUE/FALSE.
4. **Data** – kliknij komórkę > kalendarz.

---

## 🎯 CO TYGODNIA ROBISZ (5 minut w piątek 16:00)

1. Otwórz **Dashboard** – czy KPI się zgadzają?
2. Sprawdź **Outreach_Stats** – czy średnio 30 zaproszeń/dzień?
3. Filtruj **Pipeline** po `Status ogólny = "✅ POŁĄCZONY"` – هؤلاء to Twoje gorące leady, do których musisz napisać follow-up.
4. Filtruj `Status ogólny = "💬 ROZMOWA"` – przygotowuj demo / linki.
5. Jeśli `Acceptance rate < 15%` → zmień zdjęcie/nagłówek/tekst zaproszenia (zapisuj wersję w `Outreach_Stats` kolumna E).
6. Wpisz do `History` (Apps Script robi to auto, ale sprawdź).
7. Ustal priorytety na kolejny tydzień.

---

## 📊 GOTOWE WYKRESY (Insert > Chart – konfiguracja)

### 1. Funnel Sprzedażowy (Column Chart)
- **Data range:** `Dashboard!B3:B9` (transponuj: Switch rows/columns)
- **Series:** Zaproszenia, Przyjęte, Odpowiedzi, Demo, Sprzedaże
- **Customize:** Series > Zaproszenia (kolor #94a3b8), Przyjęte (#3b82f6), Odpowiedzi (#22c55e), Demo (#f59e0b), Sprzedaże (#10b981)

### 2. Przychód Miesięczny (Line Chart)
- **Data range:** `History!A:E` (po zebraniu 4+ tygodni)
- **X-axis:** Tydzień, **Series:** Przychód

### 3. Porównanie Szablonów (Bar Chart)
- **Data range:** `Dashboard!B43:F45`
- **X-axis:** Reply rate / Konwersja, **Series:** Szablony

### 4. Pipeline Status (Donut Chart)
- **Data range:** `=QUERY(Pipeline!AE2:AE, "select AE, count(AE) where AE != '' group by AE")`
- **Slice colors:** ZAMKNIETE (#10b981), DEMO (#3b82f6), ROZMOWA (#8b5cf6), POŁĄCZONY (#6b7280), ZAPROSZENIE (#94a3b8), NOWY (#d1d5db), ODRZUCONE (#ef4444)

---

## ✅ CHECKLISTA WDRÓŻENIA (zrób teraz, 15 min)

- [ ] Utwórz nowy Google Sheet: `CV Wizytówka - KPI`
- [ ] Dodaj 4 zakładki: `Pipeline`, `Dashboard`, `Outreach_Stats`, `Settings`
- [ ] Wklej nagłówki do `Pipeline` (A1:AF1) – **zamroź wiersz 1** (View > Freeze > 1 row)
- [ ] Wpisz formuły w wierszu 2 (AC:AF, X) – przeciągnij do wiersza 1000
- [ ] Zastosuj **Formatowanie warunkowe** (tabela wyżej)
- [ ] Ustaw **Walidację danych** dla kolumn G, H, O, T, AA (źródło: `Settings`)
- [ ] Wklej dane do `Settings` (tabela wyżej)
- [ ] Zbuduj **Dashboard** – wklej formuły do B3:B12, B24:B30, B43:F45
- [ ] Stwórz **4 wykresy** na Dashboard
- [ ] Dodaj **Apps Script** (Extensions > Apps Script) – wklej kod, uruchom `createTriggers()`
- [ ] Udostępnij arkusz sobie na telefonie (skrót na pulpicie)
- [ ] Wpisz **3 testowe leady** (znajomi) – przetestuj przepływ

---

## 🚀 PO WRZUCENIU PIERWSZYCH DANYCH – CO OGLĄDASZ

| Metryka | Cel (tydzień 3-4) | Cel (tydzień 6+) | Alarm |
|---------|-------------------|------------------|-------|
| Zaproszenia/tydzień | 150 | 200+ | < 100 |
| Acceptance rate | 25% | 30%+ | < 15% |
| Reply rate | 15% | 20%+ | < 5% |
| Demo/tydzień | 3-5 | 8+ | < 2 |
| Sprzedaże/tydzień | 1-2 | 2-3 | 0 przez 2 tygodnie |
| Czas produkcji | < 60 min | < 30 min | > 90 min |

---

**Gotowe.** Masz teraz kompletny system pomiarowy, który powie Ci prawdę o biznesie bez lania wody. 📈
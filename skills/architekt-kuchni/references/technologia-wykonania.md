# Technologia wykonania — od projektu do montażu

Uzupełnienie `../../architekt-wnetrz/references/standardy-meble.md` (wymiary modułów, AGD, tolerancje, mocowania — czytaj stamtąd, nie duplikuj). Tu: zasady technologiczne specyficzne dla realnych, niedoskonałych pomieszczeń.

---

## 1. Płyty i korpusy (skrót — szczegóły w korner-katalog.md)

- Korpus: płyta 18 mm (16 mm tylko ekonomiczne), plecy HDF 3 mm, wieniec górny/dolny pełny.
- Fronty: 19 mm (laminat HPL / MDF lakier / fornir — dobór wg katalogu Korner (płyty, korner.pl) i stylu projektu).
- Obrzeża ABS: 2 mm krawędzie widoczne i fronty, 1 mm ukryte; krawędź przy ścianie bez oklejania.
- Blat: laminowany 38 mm / spiek 12–20 mm na płycie / kamień — waga spieku i kamienia wymaga korpusów bez odchyłek poziomu.

## 2. Pomieszczenie nie jest idealne — obowiązkowe założenia

- **Nie zakładaj kątów prostych.** Ściany schodzą się w 88–92°; zabudowa narożna i blaty L wymagają pomiaru przekątnych.
- **Nie zakładaj, że ściana ma tę samą długość na każdej wysokości** — mierz na poziomie blatu (860) i na poziomie górnej krawędzi zabudowy; do formatek przyjmuj **najmniejszy** wymiar.
- **Krzywizny ścian**: odchyłka 5–15 mm na 2 m to norma w budownictwie — dlatego:
  - **szczelina montażowa** przy każdej ścianie: 20–50 mm zamykana **blendą** dociętą na miejscu (blendy zamawiaj z zapasem szerokości),
  - zabudowa „na styk" ściana–ściana: projektuj światło zabudowy = wymiar ściany − 40–60 mm łącznie na blendy,
  - do sufitu: fuga 10–30 mm + listwa/blenda maskująca (sufit też nie jest poziomy).
- **Poziomowanie**: nóżki regulowane 100–150 mm; spadek podłogi sprawdzić na długości zabudowy — przy >15 mm cokół docinany na miejscu.
- **Dylatacje**: blaty drewniane/laminowane 3–5 mm od ściany (praca materiału); spiek/kamień wg wytycznych producenta; styk blatu ze ścianą zamyka listwa przyblatowa lub silikon.

## 3. Instalacje za meblami

- Piony i podejścia wodne/odpływowe: wycięcia w plecach szafki zlewowej (szafka zlewowa często **bez pleców** lub z plecami serwisowymi na wkręty).
- Gniazda za AGD: zmywarka i lodówka — gniazdo w **sąsiedniej** szafce (dostęp bez wysuwania urządzenia); piekarnik/płyta — wypusty wg instalacje-elektryka.md.
- Gaz: podejście z zaworem musi zostać **dostępne** — zawór w szafce sąsiadującej, nigdy zabudowany na głucho.
- LED podszafkowe: trasa przewodu za wieńcem górnych szafek do transformatora w szafce wskazanej w projekcie.

## 4. Wentylacja i dostęp serwisowy — zakazy

- Kratka wentylacyjna: **nie wolno** zabudować na głucho. Opcje: odsunięcie zabudowy, kratka przeniesiona na front zabudowy (kanał), drzwiczki rewizyjne.
- Okap z wyrzutem: trasa kanału do kratki wentylacyjnej — zaplanuj obudowę/bok maskujący; recyrkulacja gdy kanał niemożliwy.
- Lodówka do zabudowy: wentylacja 50 mm tył + góra, kratka w cokole i w wieńcu górnym słupka.
- Piekarnik/zmywarka: nie blokować rewizji podejść; zawory odcinające dostępne.
- Bojler / piec / licznik / rewizja kanalizacji w strefie zabudowy: **zawsze** panel demontowalny lub drzwiczki — odnotuj w dokumentacji jako wymóg.

## 5. Mocowanie szafek wiszących

- Listwa montażowa + zawieszki (Camar lub odpowiednik); nośność wg standardy-meble.md.
- **Sprawdź materiał ściany**: beton/cegła pełna — kotwy standard; pustak/gazobeton — kotwy chemiczne; płyta GK — **tylko** w profile/wzmocnienia, inaczej zabudowa wisząca odpada lub wymaga rusztu. Jeśli materiał nieznany → pozycja na liście pomiarów kontrolnych.
- Płytki/spiek na ścianie: otwory wiertłem do gresu, krawędź płytki ≥50 mm od otworu.

## 6. Blendy, boki wykończeniowe, panele maskujące

| Element | Kiedy | Zasada |
|---|---|---|
| Blenda przyścienne (pion) | każdy styk zabudowy ze ścianą | 20–50 mm, docinana na miejscu z zapasu |
| Blenda przy gzymsie/słupie | zabudowa dochodzi do elementu konstrukcyjnego | zakończ zabudowę blendą 30–80 mm PRZED elementem; nie przycinaj korpusu wokół gzymsu, chyba że pomiar kontrolny potwierdzi geometrię |
| Bok wykończeniowy | widoczny bok skrajnej szafki | płyta frontowa (dekor frontu), nie surowy korpus |
| Panel maskujący | bok lodówki/słupka od strony przejścia, obudowa okapu | dekor frontów; głębokość = korpus + front |
| Cokół | obwód dolny | 100 mm standard, docinany; kratka wentylacyjna przy lodówce |
| Wieniec / blenda górna | zabudowa pod sufit | fuga 10–30 mm zamknięta blendą docinaną |

## 7. Lista pomiarów kontrolnych stolarza (szablon)

Zawsze zamykaj projekt tabelą — to pozycje, które stolarz **musi** zmierzyć na miejscu przed produkcją:

```
| # | Pomiar | Gdzie | Dlaczego krytyczny |
|---|--------|-------|--------------------|
| 1 | Długość każdej ściany zabudowy na wys. 0 / 860 / 2200 | ściany A/B | krzywizna → szerokość formatek i blend |
| 2 | Kąty narożników (przekątne) | róg AB | blat L i szafka narożna |
| 3 | Wysokość podłoga–sufit w 4+ punktach | cała strefa | wysoka zabudowa, blenda górna |
| 4 | Pion ścian (odchyłka łaty 2 m) | ściany zabudowy | blendy, szczeliny |
| 5 | Poziom podłogi na długości zabudowy | linia cokołu | nóżki, cokół |
| 6 | Pozycja + wymiar okna, parapetu, grubość ościeży | ściana z oknem | zabudowa przy oknie, zlew pod oknem |
| 7 | Pole wymachu drzwi | wejście | kolizja z frontami |
| 8 | Pozycje podejść wody, odpływu, gazu (+zawory) | strefa zmywania/gotowania | wycięcia, dostęp serwisowy |
| 9 | Pozycja i wymiar kratki wentylacyjnej | góra ściany | trasa okapu, zakaz zabudowy |
| 10 | Pozycje gniazd/wypustów elektrycznych | wszystkie ściany | ew. przeróbki przed montażem |
| 11 | Wymiary elementów konstrukcyjnych (gzyms/słup/uskok) | wg modelu | blendy, zakończenia zabudowy |
| 12 | Materiał ścian pod szafki wiszące | ściany górnych | dobór kotew / wykonalność |
```

Pozycje nieaktualne dla danego projektu usuń, specyficzne dodaj (np. „średnica i wysokość bojlera").

# Analiza pomieszczenia — protokół pracy ze zdjęciami i rzutami

Cel: z wielu zdjęć, szkiców i częściowych wymiarów zbudować **jeden spójny model pomieszczenia**, z jawnym rozdziałem faktów od założeń. To fundament — bez tego etapu nie wolno projektować układu ani generować wizualizacji.

---

## 1. Protokół analizy pojedynczego zdjęcia

Dla **każdego** zdjęcia wypełnij:

```
### Zdjęcie N
- Pozycja kamery (skąd robione, w którą stronę patrzy): np. "od drzwi wejściowych w stronę okna"
- Widoczne ściany (przypisz litery A/B/C/D zgodnie ze wspólną orientacją):
- Elementy stałe widoczne: okna (+parapet, kierunek otwierania), drzwi (+kierunek otwierania),
  wnęki, słupy, gzymsy/piony gzymsowe, kominy, uskoki ścian, grzejniki, skosy
- Instalacje widoczne: pion wodny, odpływ, zawory, gaz, kratka wentylacyjna,
  gniazdka, włączniki, wypusty elektryczne
- Wymiary możliwe do odczytania / oszacowania (z czego szacujesz — np. wysokość drzwi ~200 cm,
  płytka 60 cm, cegła, panel):
- Punkty wspólne z innymi zdjęciami (do sklejenia widoków): np. "to samo okno co na zdjęciu 2,
  widziane z prawej"
- Czego NIE widać (strefy zasłonięte / poza kadrem):
```

### Zasady odczytu zdjęć

- **Każde zdjęcie analizuj w odniesieniu do pozostałych** — szukaj wspólnych punktów (okno, drzwi, pion, gzyms, gniazdko) i na ich podstawie sklejaj widoki w jedno pomieszczenie. Nigdy nie traktuj zdjęcia jako osobnego pomieszczenia.
- **Nie wymyślaj elementów niewidocznych na zdjęciach.** Strefa poza kadrem = `[?] NIEZNANE — DO POTWIERDZENIA`, nie „pusta ściana".
- Szacunki z proporcji zdjęcia zawsze oznaczaj `[~]` i podawaj podstawę szacunku ("wysokość framugi ≈ 200 cm → ściana ≈ 320 cm").
- Zdjęcia szerokokątne (telefon) zniekształcają proporcje przy krawędziach kadru — wymiary z krawędzi traktuj jako mniej pewne.
- Kierunek otwierania okien/drzwi: jeśli nie widać zawiasów/klamki — `[?]`.

---

## 2. Model pomieszczenia (synteza)

Po analizie wszystkich zdjęć zbuduj:

### 2a. Rzut ASCII z orientacją

```
            ściana A (okno)
   ┌────────═══════════────────┐
   │ [~]120        [P]80  [?]  │
 ś │                           │ ś
 c │      KUCHNIA              │ c
 i │      ~3.2 × 2.6 m         │ i
 a │                           │ a
 n │ ▓gzyms                    │ n
 a │ 15×15                     │ a
 D │    kratka went.●          │ B
   └───────────┬─drzwi 90─────┘
            ściana C
```

Oznaczenia: `═` okno, `▓` element konstrukcyjny (gzyms/słup/komin), `●` instalacja, `┬` drzwi.

### 2b. Tabela wymiarów — trzy kategorie

| Wymiar | Wartość | Status | Źródło |
|---|---|---|---|
| Ściana A | 320 cm | `[P]` potwierdzony | podał użytkownik |
| Ściana B | ~260 cm | `[~]` orientacyjny | szacunek ze zdjęcia 2 (proporcja do drzwi) |
| Wysokość | ? | `[?]` do potwierdzenia | brak danych |

**Statusy:**
- `[P]` — potwierdzony (podany przez użytkownika lub odczytany z rzutu z wymiarami)
- `[~]` — orientacyjny (szacunek; podaj podstawę)
- `[?]` — nieznany / do potwierdzenia pomiarem

### 2c. Elementy stałe — rejestr

| Element | Ściana | Pozycja | Wymiary | Status | Konsekwencja projektowa |
|---|---|---|---|---|---|
| Okno | A | 60 cm od rogu AB | 120×140, parapet 85 | `[~]` | górne szafki nie zachodzą; zlew pod oknem możliwy |
| Gzyms pionowy | D | róg CD, podłoga→sufit | 15×15 | `[P]` (zdj. 1+3) | zabudowa kończy się blendą przed gzymsem |
| Kratka wentylacyjna | B | góra, ~30 cm od sufitu | 14×14 | `[P]` | zakaz zabudowy na głucho; kratka w zabudowie lub odsunięcie |
| Pion wodny + odpływ | B | 40 cm od rogu BC | — | `[~]` | strefa zmywania przy tej ścianie |

---

## 3. Wykrywanie sprzeczności

Porównaj systematycznie:

1. **Zdjęcie vs zdjęcie** — ten sam element ma inną pozycję/rozmiar na dwóch ujęciach? Wypisz obie wersje, oznacz `SPRZECZNE`.
2. **Zdjęcie vs podane wymiary** — proporcje ze zdjęcia nie zgadzają się z wymiarem podanym (np. na zdjęciu ściana wygląda na dłuższą niż deklarowane 240 cm)? Zapytaj / oznacz.
3. **Suma cząstkowych vs całość** — odcinki ściany (wnęka + filar + wnęka) nie sumują się do długości ściany.
4. **Rzut vs zdjęcia** — element na rzucie nieobecny na zdjęciach lub odwrotnie.

Format:

```
## Sprzeczności
| # | Co się nie zgadza | Wersja 1 (źródło) | Wersja 2 (źródło) | Co przyjmuję do dalszej pracy | Co potwierdzić |
```

Do dalszej pracy przyjmuj **wariant bezpieczniejszy** (mniejszy wymiar dla zabudowy, większy dla wymaganych odstępów) i jawnie to zaznacz.

---

## 4. Lista braków i pytań

Maksymalnie 3–5 pytań krytycznych naraz (wzorzec intake jak w architekt-wnetrz). Resztę braków wypisz jako listę pomiarów do wykonania — projekt kontynuuj na dostępnych danych z oznaczeniami `[~]`/`[?]`.

Priorytet pytań: (1) wymiary blokujące wybór układu (długości ścian, szerokość przejścia), (2) instalacje (gaz? pion? wentylacja?), (3) wysokość pomieszczenia, (4) kierunki otwierania, (5) preferencje.

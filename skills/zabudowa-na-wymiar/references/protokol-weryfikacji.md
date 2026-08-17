# Protokół weryfikacji — OBOWIĄZKOWY przed wysłaniem rysunku inwestorowi

Powstał po serii błędów w projekcie `kuchnia-wyspa` (2026-08-12/13), gdzie inwestor
wychwycił rzeczy, których nie sprawdziłem: okap nad szufladami zamiast nad płytą,
narożnik policzony dwa razy, drzwi piekarnika zasłonięte ramieniem, biała przerwa
w licu ciągu, uskok w linii frontów górnych.

**Zasada nadrzędna: rysunek nie wychodzi do inwestora, dopóki nie przejdzie wszystkich
punktów poniżej. Wolniej, ale bez wstydu.**

---

## 1. Jedno źródło prawdy

Wymiary modułów NIE mogą żyć równolegle w trzech miejscach (PLAN.md, generator schematu,
generator formatek) — zawsze się rozjadą. Trzymaj model w jednym pliku (`_kontrola.py`
albo `_model.py`) i po każdej zmianie sprawdź zgodność pozostałych plików z nim.

Kontrola ręczna, jeśli nie ma jeszcze wspólnego modelu: wypisz obok siebie sumy modułów
z PLAN.md i z generatora formatek. Muszą się zgadzać co do milimetra.

## 2. Kontrola automatyczna — `_kontrola.py`

Skopiuj do projektu i dopasuj model. Sprawdza:

| kod | co sprawdza | jaki błąd łapie |
|---|---|---|
| K1 | sumy modułów = długość ciągu | dziury i nadmiar w rozpisce |
| K2 | brak nakładek brył w rzucie | narożnik policzony dwa razy (blaty, korpusy) |
| K3 | każdy front ma zawias, przy którym się otworzy (ćwiartka wychyłu, tylko na zewnątrz lica) | drzwi piekarnika za ramieniem, drzwi obok słupka |
| K4 | okap obejmuje całą płytę | okap przesunięty nad szuflady |
| K5 | górne na ścianie mają wspólną płaszczyznę frontu | uskok po złej głębokości szafki przy pilastrze |
| K6 | przejścia ≥ próg zaakceptowany przez inwestora | ciche zejście z 60 na 59,6 |
| K7 | lico ciągu domknięte frontem albo blendą | biała przerwa na rzucie = brakująca blenda |
| K8 | okucia mieszczą się w otworze (cargo narożne ≥450, karuzela ≥450) | obiecane cargo, które fizycznie nie wejdzie |
| K9 | funkcje obowiązkowe nadal mają swój moduł (sztućce ≥250, kosz segregacji ≥450, przyprawy ≥100) | przebudowa modułu, która po cichu kasuje szuflady na sztućce |

`python3 _kontrola.py` → PASS/FAIL. `--regresja` odgrywa historyczne błędy i dowodzi,
że testy je łapią. **FAIL = nie wysyłasz rysunku.**

## 3. Obejrzyj wygenerowany PDF, nie tylko go wygeneruj

```bash
pip install pypdfium2
python3 -c "import pypdfium2 as p; p.PdfDocument('x.pdf')[0].render(scale=2).to_pil().save('x.png')"
```
Potem **przeczytaj obrazek narzędziem Read**. Połowa wpadek to rzeczy widoczne gołym
okiem: nachodzące napisy, ucięty tytuł, biała dziura, etykieta pod bryłą.
Generowanie PDF-a bez obejrzenia go = wysyłanie w ciemno.

## 4. Kontrole krzyżowe z wymiarów inwestora

Każdy wymiar musi domknąć się w co najmniej dwóch łańcuchach. Przykłady z tego projektu:
- `254,6 − 238,9 = 15,7 ≈ 15,5` → potwierdza pilaster
- `59,7 + 85,6 + 94,7 = 240 ≈ 238,9` → potwierdza pozycję okna
- `koniec ciągu 195 ≈ ścianka 188,5 + 9` → potwierdza linię południową
Jeśli łańcuch się nie domyka — **pytaj, nie zaokrąglaj**.

## 5. Zdjęcia: nie projektuj na interpretacji

Jedyny błąd z tej serii, którego skrypt nie złapie: odczytałem ze zdjęcia poziomą belkę
pod sufitem, a to był pionowy pilaster (zdjęcie było obrócone o 90°).

Reguły:
- sprawdź orientację zdjęcia (obróć i obejrzyj ponownie), zanim cokolwiek z niego wywnioskujesz;
- **zanim zbudujesz konstrukcję na elemencie ze zdjęcia, zdobądź od inwestora dwie liczby:**
  ile wystaje i jaki ma zasięg (długość/wysokość);
- element ze zdjęcia bez potwierdzonych liczb ma status `[?]`, nie `[P]`.

## 6. Zanim odpiszesz — sześć pytań

1. Czy każdy front ma się gdzie otworzyć?
2. Czy okap jest nad płytą, a zlew nie nad zmywarką?
3. Czy sumy modułów zgadzają się z wymiarem ściany?
4. Czy któraś przestrzeń jest liczona dwa razy?
5. **Czy po przebudowie modułu nie zniknęła funkcja, którą obiecywał plan funkcjonalny?**
   Przebudowa szafki szufladowej na narożną ślepą kasuje miejsce na sztućce. Sprawdź tabelę
   „co w której szafce" — czy nie opisuje modułów, których już nie ma.
6. Czy obejrzałem wygenerowany rysunek?

## 7. Gdy inwestor mówi „coś tu jest nie tak"

Nie poprawiaj grafiki od razu. **Najpierw sprawdź geometrię liczbowo** — w tym projekcie
dwa razy z „wizualizacja jest jakby zła" wyszedł realny błąd konstrukcyjny, a nie
kwestia rysunku. Uwaga inwestora to sygnał, że model może być zły, nie tylko obrazek.

## 8. Zwrot elewacji — sprawdzaj rachunkiem, nie okiem

Elewację wnętrzarską rysuje się **tak, jak ją widzi ktoś stojący w pomieszczeniu**.
Zwrot łatwo odwrócić, bo w rzucie ściana wygląda „tak samo z obu stron", a błąd jest
niewidoczny do momentu, w którym ktoś przyłoży rysunek do prawdziwej ściany.

Reguła (układ: x → wschód, y → południe, rzut z północą do góry):

| Patrzysz na ścianę | Kierunek patrzenia | Po LEWEJ | Po PRAWEJ |
|---|---|---|---|
| zachodnią | na zachód | **południe** | **północ** |
| wschodnią | na wschód | **północ** | **południe** |
| północną | na północ | **zachód** | **wschód** |
| południową | na południe | **wschód** | **zachód** |

Wynika to z jednej zasady: **stojąc twarzą do ściany, obracasz się względem północy
i twoja prawa ręka jedzie razem z tobą.** Patrzę na północ → prawo = wschód. Obrót
w lewo (na zachód) → prawo = północ. Obrót w prawo (na wschód) → prawo = południe.

**Procedura, nie intuicja:** przed wysłaniem elewacji wypisz dla każdej z nich, co ma
być po lewej, i porównaj z tym, co faktycznie rysuje kod. Trzy elewacje wymagają trzech
sprawdzeń — w tym projekcie dwie były dobrze, a trzecia (ściana zachodnia) była
odbita, mimo że jej własny podtytuł deklarował „widok z wnętrza".

**Podtytuł elewacji musi nazywać zwrot wprost** — „patrzysz na ZACHÓD → okno po PRAWEJ",
a nie samo „od lewej: pilaster". Wtedy rysunek sam się kontroluje: jeśli podtytuł kłóci
się z obrazkiem, widać to natychmiast.

Rzutu i aksonometrii to nie dotyczy — rzut ma sztywno północ do góry, a aksonometria
ma własną flagę lustra.

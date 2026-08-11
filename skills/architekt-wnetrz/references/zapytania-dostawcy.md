# Szablony Fazy 8 — harmonogram, listy zakupów, wiadomości do dostawców

Szablony wyjść Fazy 8. Mapa dostawców: `dostawcy.md`. Lista zakupów Korner (formatki/fronty/okucia): format w `../../zabudowa-na-wymiar/references/formatki.md`.

---

## Harmonogram robót (8a — Gantt-style ASCII)

```
TYDZ.  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |
─────────────────────────────────────────────────────────
Demontaż / przygotowanie     ████
Instalacje (woda/gaz/elektr.)     ████████
Tynki / gładzie                            ████
Posadzki (wylewki)                              ████
Sufity GK + malowanie                                ████████
Podłogi (deska/spiek)                                     ████
Drzwi + listwy                                                 ████
Łazienka (mikrocement + armatura)                              ████████
Meble na wymiar (montaż)                                              ████
Meble wolnostojące + dekoracje                                             ████
Sprzątanie + oddanie                                                            ██
```

---

## Lista zakupów per dostawca (struktura)

Osobna sekcja per sklep, tabele z kolumnami: Pozycja | Producent/SKU | Ilość | Cena/szt | Razem. Na końcu każdej sekcji suma "Razem <sklep>: ~XX zł".

```
## Leroy Merlin / Castorama (wykończenia masowe)
| Pozycja | Producent / SKU | Ilość | Cena/szt | Razem |
| ...     | ...             | ...   | ...      | ...   |

## IKEA (meble wolnostojące)
## Westwing / Bonami (designerskie tańsze)
## Specjalistyczne (oświetlenie hero, armatura — wg dostawcy.md)
## Allegro (drobnica — kable, kontakty, taśmy)
```

Zasady: ceny zawsze widełki orientacyjne; 2-3 opcje (ekonomia/standard/premium) przy pozycjach kosztotwórczych; pozycje `[DO WERYFIKACJI]` tam, gdzie SKU/cena niepotwierdzone.

## Szacunkowy koszt całości (struktura)

```
| Kategoria                       | Koszt netto (widełki) |
|---------------------------------|------------------------|
| Meble na wymiar (Korner płyty)  | od X do Y              |
| Wykończenia (podłogi/ściany)    | ...                    |
| Oświetlenie                     | ...                    |
| Meble wolnostojące              | ...                    |
| Instalacje + elektryka          | ...                    |
| Robocizna ekipy                 | ...                    |
| Dekoracje + tekstylia           | ...                    |
| **RAZEM (orientacyjnie)**       | **od X do Y zł**       |
```

Dolny zakres = wybory ekonomiczne, górny = premium. Zawsze dopisz: ostateczne ceny do potwierdzenia w sklepach; wycena ekipy budowlanej osobno.

## Wiadomości do dostawców (gotowe do skopiowania)

### Email do doradcy Korner (płyty, korner.pl — oddział Piekary Śląskie)

```
Temat: Wycena formatek + frontów — [projekt, np. kuchnia 3.2m]

Cześć,

proszę o wycenę zamówienia:

[tabela formatek / lista zakupów Korner wg formatki.md]

Termin pożądany: do <data>
Dostawa: <adres> / odbiór osobisty (Piekary Śląskie)

Pozdrawiam,
<imię>
```

Analogiczne wiadomości dla innych dostawców — tylko jeśli istnieje sensowny kanał kontaktu (dystrybutor armatury, salon oświetlenia). Do sklepów detalicznych (IKEA, Leroy) wiadomości nie piszesz — lista wystarcza.

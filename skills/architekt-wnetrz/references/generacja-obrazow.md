# Generacja obrazów (Gemini Nano Banana) — JEDYNE źródło logiki

Wspólne dla skilli architekt-wnetrz i zabudowa-na-wymiar. Nie kopiuj tej logiki do SKILL.md — odsyłaj tutaj. Konstrukcja promptów **kuchennych wiernych geometrii**: `../../zabudowa-na-wymiar/references/prompty-wizualizacyjne.md` (uzupełnia ten plik, nie zastępuje).

**Model:** `gemini-3.1-flash-image-preview` — to jest jedyne miejsce definicji nazwy modelu `[DO PRZEGLĄDU przy zmianach API]`. Przykład w `cloudflare-worker.md` używa tej wartości.

---

## 1. Detekcja środowiska — 4 ścieżki (w tej kolejności)

1. **MCP (preferowane):** `mcp__nanobanana-mcp__set_aspect_ratio` → `mcp__nanobanana-mcp__gemini_generate_image`; edycja istniejącego obrazu: `gemini_edit_image` z `imagePath`.
2. **Skrypt Python:** `generate.py` z pluginu banana-claude. **Nie zakładaj ścieżki** — ustal z konfiguracji użytkownika (zmienna środowiskowa `BANANA_GENERATE_PY` lub zapytaj raz i zapamiętaj w konwersacji). Wywołanie: `python3 "<ścieżka>/generate.py" --prompt "..." --aspect-ratio "16:9" --resolution "2K" --image-only`.
3. **Cloudflare Worker (mobile):** POST `/generate` — adres i secret to **konfiguracja użytkownika**, nie treść skilla; sposób wywołania i skąd wziąć wartości: `cloudflare-worker.md`.
4. **Manualny prompt:** gdy nic z powyższych nie działa — oddaj gotowy prompt EN użytkownikowi do ręcznego wklejenia.

## 2. Konstrukcja promptu — 5-component formula

Każdy prompt MUSI mieć: **Subject** (co projektujemy, z konkretami) → **Action/scene** (statyczne wnętrze, pora dnia) → **Location/context** (wymiary impression, charakter mieszkania) → **Composition** (kąt kamery, ogniskowa, perspektywa) → **Style** (materiały explicit, oświetlenie explicit, prestiżowa kotwica).

**ZAKAZANE słowa (degradują output):** `8K`, `masterpiece`, `ultra-realistic`, `high resolution`, `best quality`. Rozdzielczość przez parametr `imageSize: 2K`, nie przez tekst promptu.

**Kotwice stylistyczne:** "Architectural Digest editorial spread", "Dezeen feature photograph", "Wallpaper* magazine interior".

## 3. Aspect-ratio routing

| Co generujesz | Aspect ratio | Resolution |
|---|---|---|
| Kuchnia widok szeroki (1 ściana) | 16:9 | 2K |
| Kuchnia narożna / L-kształt | 4:3 | 2K |
| Szafa / garderoba (frontalnie) | 3:4 | 2K |
| Łazienka kompaktowa | 4:5 | 2K |
| Zbliżenie detalu (uchwyt, blat) | 1:1 | 2K |
| Full room render (cinematic) | 21:9 | 2K |
| Salon / pomieszczenie hero | 16:9 | 2K |
| Sypialnia | 4:3 | 2K |
| Hol / wejście | 3:4 | 2K |

## 4. Domyślne zestawy renderów

- **Pełny projekt mieszkania (Faza 7 architekt-wnetrz):** 5-8 obrazów — salon hero (16:9) + salon wieczór (16:9) + kuchnia (16:9) + sypialnia (4:3) + łazienka (4:5) + 1-2 detale (1:1) + hol (3:4, jeśli w scope).
- **Jedno pomieszczenie:** 3-4 obrazy — hero + alternatywny kąt + 1-2 detale.
- **Moodboard (Faza 1):** 2-3 obrazy — hero shot (16:9) + detail collage (1:1) + opcjonalny kąt alternatywny (16:9).
- **Zabudowa meblowa:** 2 obrazy — overview + detail close-up (macro, 100mm, f/2.8).

## 5. Szablon promptu — wnętrze (EN)

```
Architectural interior photograph of [room type] in a modern Polish apartment,
~[X] square meters. [Wall/finish descriptions with explicit materials and colors].
[Furniture with materials]. [Lighting: natural direction + artificial layers,
color temperature]. Captured with Sony A7R IV, 24mm lens at f/8, eye-level
perspective, three-point composition with depth. No people. Architectural
Digest editorial spread aesthetic, minimalist modern Polish apartment.
```

Detal: kamera "Canon EOS R5, 100mm macro lens at f/2.8", shallow depth of field, kotwica "Dezeen design feature photograph". Kuchnia wierna geometrii pomieszczenia: szablony i blok zakazów w `prompty-wizualizacyjne.md` (zabudowa-na-wymiar).

## 6. Obsługa błędów

| Błąd | Reakcja |
|---|---|
| `IMAGE_SAFETY` | przeformułuj — usuń triggery, dodaj "artistic editorial render" |
| HTTP 429 (rate limit) | czekaj 60s, retry; free tier ~5-15 RPM |
| `FAILED_PRECONDITION` (billing) | "Włącz billing w Google AI Studio: aistudio.google.com/apikey" |
| `API_KEY_INVALID` | "Klucz `GOOGLE_AI_API_KEY` nieprawidłowy lub niewczytany — sprawdź env var" |
| MCP niedostępne | fallback: skrypt Python (2) → Worker (3) → manualny prompt (4) |
| Brak `GOOGLE_AI_API_KEY` | poproś użytkownika o ustawienie zmiennej środowiskowej |

## 7. Po wygenerowaniu

1. Pokaż **ścieżki do plików**, 2. **prompty użyte** (educational), 3. **settings** (model, aspect ratio, resolution), 4. zapytaj: (a) regeneracja ze zmianą, (b) dodatkowy widok, (c) edycja tego obrazu (`gemini_edit_image` z `imagePath`), (d) dalej do następnej fazy.

**Iteracja:** zmiany w istniejącym obrazie ("zmień blat na biały marmur") — ZAWSZE `gemini_edit_image` z `imagePath` poprzedniego renderu, NIE generacja od zera. Edycja jest tańsza i zachowuje proporcje.

## 8. Kontrola zgodności renderu (obowiązkowa dla obu skilli)

Po każdej generacji porównaj render z projektem/modelem pomieszczenia:

| Sprawdzenie | OK/BŁĄD |
|---|---|
| Okna/drzwi w tej samej pozycji i rozmiarze | |
| Elementy konstrukcyjne zachowane (gzyms/słup/kratka) | |
| Meble/zabudowa zgodne z projektem (kolejność, liczba, pozycje) | |
| Proporcje pomieszczenia niezmienione | |
| Materiały/kolory zgodne z decyzjami | |

Błędy → iteruj przez `gemini_edit_image` ze wskazaniem konkretnej poprawki. Render niezgodny z geometrią **nie trafia do dokumentacji**. (Wersja rozszerzona dla kuchni: `prompty-wizualizacyjne.md` §5.)

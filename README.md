# Architekt Wnętrz — Claude Code Plugin

Pełen pipeline projektowania wnętrz mieszkaniowych A-Z dla rynku polskiego. Plugin Claude Code w formacie marketplace.

## Co robi (9 faz)

Wysyłasz zdjęcie pomieszczenia/szkic z wymiarami + opis → skill prowadzi cię przez:

1. **Intake** — analiza pomieszczenia, scope projektu, max 3 pytania krytyczne
2. **Koncept i moodboard** — styl, paleta, materiały + **2-3 wizualizacje** moodboardu (Gemini)
3. **Layout przestrzenny** — strefy funkcjonalne, rzut z góry z meblami i wymiarami
4. **Wykończenia** — podłogi, ściany, sufity, drzwi, listwy (z dostawcami i kosztorysem)
5. **Plan oświetlenia** — 3 warstwy świateł, lampy, LED, ściemniacze, smart, włączniki, gniazdka
6. **Meble** — wbudowane (Korner) + wolnostojące (IKEA / Westwing / Bonami / designerskie) + tekstylia
7. **Plan elektryczny + instalacje** — gniazdka, RJ45, włączniki, woda, kanalizacja, gaz, wentylacja
8. **Wizualizacje** — **5-8 fotorealistycznych renderów** całego projektu przez Gemini Nano Banana 2
9. **Plan budowy + harmonogram + lista zakupów** — gantt robót, lista per dostawca, gotowe wiadomości do Korner

## Domyślny styl

**Modern Polish Apartment** — Orzech Royal + kremowy + czarne listwowe uchwyty + ciepłe LED 3000K + spiek czarny mat. Stosowany domyślnie, chyba że poprosisz o inny styl (japandi, scandi, glamour, industrial, boho, wabi-sabi, mid-century, coastal — biblioteka 10 stylów w `references/style-aesthetics.md`).

## Struktura plugina

```
architekt-wnetrz/
├── .claude-plugin/
│   ├── plugin.json                            # manifest plugina
│   └── marketplace.json                       # katalog marketplace
├── skills/
│   └── architekt-wnetrz/
│       ├── SKILL.md                           # główny prompt (9 faz, ~31 KB)
│       └── references/                        # 9 plików referencyjnych
│           ├── korner-katalog.md
│           ├── standardy-meble.md
│           ├── workflow-zapytania.md
│           ├── oswietlenie-katalog.md
│           ├── podlogi-sciany-sufity.md
│           ├── dostawcy.md
│           ├── instalacje-elektryka.md
│           ├── style-aesthetics.md
│           └── cloudflare-worker.md
├── worker/                                    # Cloudflare Worker do telefonu
│   ├── src/index.ts
│   ├── wrangler.toml
│   ├── package.json
│   └── README.md
└── README.md
```

## Instalacja

### Opcja 1 — Marketplace via GitHub (rekomendowane — działa wszędzie)

Po wrzuceniu repo na GitHub:

**Claude Code (terminal):**
```
/plugin marketplace add <twoja-nazwa>/architekt-wnetrz
/plugin install architekt-wnetrz@architekt-wnetrz-marketplace
```

**Claude.ai (web + telefon):**

Settings → Skills → "Add from URL" → wklej `https://github.com/<twoja-nazwa>/architekt-wnetrz`

### Opcja 2 — Lokalna instalacja (Claude Code, bez GitHub)

```powershell
Copy-Item -Recurse "C:\Users\PC\architekt-wnetrz\skills\architekt-wnetrz" "C:\Users\PC\.claude\skills\architekt-wnetrz" -Force
```

Restart Claude Code → skill aktywny.

### Opcja 3 — Drag&drop folderu do Claude.ai

1. Wejdź na **claude.ai → Settings → Capabilities/Skills** (wymagany Pro/Team)
2. **"Create new skill"** → przeciągnij folder `skills/architekt-wnetrz/` z Eksploratora
3. Save → skill aktywny na wszystkich urządzeniach zalogowanych na to konto Claude (web + desktop + mobile)

## Test

W nowej sesji napisz:
> *"zaprojektuj mi salon 25m² w stylu japandi, okno panoramiczne z lewej"*

albo:
> *"urządź całe mieszkanie 60m², 2 pokoje + kuchnia + łazienka + hol, lecę na pełnej"*

albo realnym pomysłem z twojego mieszkania (zdjęcie + opis).

## Generacja obrazów (Gemini Nano Banana 2)

Skill wywołuje **Gemini Nano Banana 2** w 3 trybach (autodetekcja):

1. **MCP banana** (lokalnie na PC, najszybsze) — `mcp__nanobanana-mcp__gemini_generate_image`
2. **Python skrypt** (lokalny fallback) — `generate.py` z banana-claude plugin
3. **Cloudflare Worker** (z telefonu) — gdy claude.ai mobile

**Wymagania:**
- Klucz Gemini API w env `GOOGLE_AI_API_KEY` (z `aistudio.google.com/apikey`)
- Dla mobile dodatkowo: zdeployowany Cloudflare Worker (patrz `worker/README.md`, ~10 min, darmowy tier)

## GitHub push (raz)

```powershell
cd C:\Users\PC\architekt-wnetrz
git init
git add .
git commit -m "Initial: architekt-wnetrz v1.0 plugin"
git branch -M main
git remote add origin https://github.com/<twoja-nazwa>/architekt-wnetrz.git
git push -u origin main
```

Po zmianach:
```powershell
git add . ; git commit -m "Update: <opis>" ; git push
```

Po `git push` użytkownicy dostają update przez `/plugin update architekt-wnetrz`.

## Co skill **nie** robi

- ❌ Nie zamawia automatycznie u dostawców — generuje listy do skopiowania
- ❌ Nie liczy dokładnych cen — daje widełki do potwierdzenia
- ❌ Nie zastępuje pomiarów na miejscu — Twoje wymiary są szacunkiem
- ❌ Nie projektuje konstrukcji budowlanych — tylko wykończenia i meble
- ❌ Nie zna lokalnych cen wykonawców — robocizna zawsze osobno

## Relacja z innymi skillami

| Skill                  | Zakres                              | Kiedy uruchamiać                            |
|------------------------|-------------------------------------|----------------------------------------------|
| **architekt-wnetrz**   | Pełen projekt wnętrza (TEN SKILL)   | Wszystko o mieszkaniu / wnętrzu              |
| **banana-claude**      | Dowolny obraz, bez logiki projektowej| Szybkie koncepty, single image generations  |

## Aktualizacje

- **v1.0** (2026-05-25) — start: 9 faz, 9 plików referencyjnych, integracja z Banana / Gemini Nano Banana 2 + Cloudflare Worker dla mobile

## Autor

dpsolutionsbusiness@gmail.com
Dostawca mebli na wymiar: **Korner** (korner.eu, Żary)

## Licencja

MIT

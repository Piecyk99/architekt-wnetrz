# Skille — zasady utrzymania

## Źródło prawdy

**Jedynym źródłem prawdy dla skilli jest to repozytorium (`skills/`).**

- **Nie tworzyć kopii user-level** (`~/.claude/skills/`, upload pojedynczych folderów na konto claude.ai z ręcznie zmodyfikowaną treścią). Ręcznie utrzymywane kopie rozjeżdżają się z repo — dokładnie ten mechanizm wyprodukował rozjazd synced-vs-plugin wykryty w audycie 2026-08 (SKILLS_AUDIT.md).
- Dystrybucję ZIP-ów do uploadu na claude.ai zapewnia workflow `build-skills.yml` (spec: `docs/backlog-p1-build-skills-workflow.md`) — buduje paczki z repo automatycznie po każdym pushu na main.

## Pakowanie standalone — WYMÓG przepisywania ścieżek

Skille w tym repo współdzielą pliki referencyjne przez ścieżki względne
(`../architekt-wnetrz/references/...`). **Wewnątrz ZIP-a wgrywanego na claude.ai te ścieżki są martwe** — poza pluginem nie ma dostępu do `../`.

Ktokolwiek pakuje skill ręcznie (lub modyfikuje workflow), MUSI:

1. **Fizycznie skopiować** współdzielone pliki referencyjne do `references/` wewnątrz paczki skilla.
2. **Przepisać ścieżki w treści** — w `SKILL.md`: `../architekt-wnetrz/references/X.md` → `references/X.md`; w plikach wewnątrz `references/`: `../../architekt-wnetrz/references/X.md` → `X.md` (ten sam katalog).

**To jest wymóg, nie optymalizacja.** Samo skopiowanie plików bez przepisania ścieżek zostawia w treści martwe odwołania; samo przepisanie bez kopiowania zostawia odwołania do nieistniejących plików. Pominięcie któregokolwiek kroku odtwarza błąd klasy „meble-architekt deklaruje references, których nie ma" z audytu.

## Struktura ZIP-a na claude.ai

Korzeniem ZIP-a musi być katalog skilla (np. `zabudowa-na-wymiar/SKILL.md`) — nie folder-owijka repo, nie luźne pliki. Nazwa katalogu musi być zgodna z polem `name` we frontmatterze `SKILL.md`.

# P1 backlog: GitHub Actions — build ZIP-ów skilli do uploadu na claude.ai

**Status:** zaplanowane. **Wykonać w P1, PO przemianowaniu skilli** (workflow ma od razu budować właściwe nazwy). Nie implementować przed refactorem nazw/triggerów.

Plik docelowy: `.github/workflows/build-skills.yml`

## Wymagania

1. **Trigger:** push na `main` + `workflow_dispatch` (ręczne odpalenie z UI GitHuba, także z telefonu).
2. **Zakres:** dla każdego katalogu w `skills/` zawierającego `SKILL.md` — osobny ZIP.
3. **KRYTYCZNE — struktura ZIP-a:** korzeniem ZIP-a musi być katalog skilla (np. `zabudowa-na-wymiar/SKILL.md`), NIE folder-owijka repo i NIE luźne pliki. Weryfikacja w workflow przez `unzip -l`: build kończy się błędem, jeśli pierwsza ścieżka nie zaczyna się od nazwy skilla.
4. **Walidacja nazwy:** nazwa katalogu musi się zgadzać z polem `name` we frontmatterze `SKILL.md` — sprawdzić i przerwać build przy rozjeździe.
5. **Wykluczenia:** `.git`, `_deprecated/`, `node_modules`, pliki tymczasowe.
6. **Współdzielone references** (`../architekt-wnetrz/references/...`): pliki muszą trafić do ZIP-a **fizycznie** (poza pluginem `../` nie działa). Workflow rozwiązuje ścieżki względne, kopiuje pliki do ZIP-a i **wypisuje w logu, które pliki zdublowano i do którego ZIP-a**.
7. **Publikacja:** ZIP-y jako artifacts **ORAZ** GitHub Release z tagiem datowym `skills-YYYY-MM-DD` — do pobrania z telefonu bez logowania do Actions.
8. **Opis release'u:** lista skilli z rozmiarem + krótka nota co się zmieniło (z commit message).

## Notatki kontekstowe

- Rozwiązuje problem utrwalania `~/.claude/skills/synced/` — po każdym mergu do main gotowe ZIP-y do re-uploadu na konto claude.ai.
- Zastępuje ręczny mirror repo → synced wykonywany w P0.
- Punkt zaczepienia: istnieje już `worker/scripts/build-skill.mjs` (build skilla dla appki) — ocenić reuse logiki rozwiązywania references.

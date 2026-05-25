# Architekt Wnętrz — backend Worker

Cloudflare Worker: Claude API (chat ze streamingiem) + Gemini Nano Banana (wizualizacje) + D1 (projekty) + R2 (zdjęcia/rendery).

Endpoints: zobacz nagłówek `src/index.ts`.

## Pre-reqs

- Node 18+
- Konto Cloudflare (darmowy plan wystarcza)
- Klucz **Anthropic API** z https://console.anthropic.com/settings/keys
- Klucz **Google AI Studio** z https://aistudio.google.com/apikey

## Setup (raz)

```bash
cd worker
npm install
npx wrangler login
```

### 1. D1 — baza danych

```bash
npx wrangler d1 create architekt-wnetrz
```

Skopiuj `database_id` z outputu i wklej do `wrangler.toml` (linia z `REPLACE_AFTER_CREATE`).

Następnie odpal migracje:

```bash
npm run db:migrate:remote
```

### 2. R2 — bucket na obrazy

```bash
npx wrangler r2 bucket create architekt-wnetrz-media
```

### 3. Sekrety

Wygeneruj `SHARED_SECRET` (Linux/Mac):
```bash
openssl rand -base64 32
```
PowerShell:
```powershell
[Convert]::ToBase64String((1..32 | %{ Get-Random -Maximum 256 }))
```

Wprowadź sekrety do Cloudflare (każda komenda zapyta o wartość):
```bash
npm run secret:claude    # ANTHROPIC_API_KEY
npm run secret:gemini    # GEMINI_API_KEY
npm run secret:shared    # SHARED_SECRET
```

### 4. Deploy

```bash
npm run deploy
```

Wrangler zwróci URL typu `https://architekt-wnetrz.<twoja-subdomena>.workers.dev`. Zapisz — będziesz go potrzebował we frontendzie (`NEXT_PUBLIC_API_URL`).

### 5. Test

```bash
curl https://architekt-wnetrz.<twoja-subdomena>.workers.dev/health
# {"ok":true,"ts":...}

curl -X POST https://.../api/projects \
  -H "Authorization: Bearer <SHARED_SECRET>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","rooms":[{"name":"Salon","area":25}]}'
```

## Dev lokalnie

```bash
# Setup lokalnej bazy
npm run db:migrate:local

# Stwórz .dev.vars z sekretami (NIE commituj)
cat > .dev.vars <<EOF
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIza...
SHARED_SECRET=cokolwiek-do-dev
EOF

npm run dev   # http://localhost:8787
```

## Aktualizacja skilla

Skill (`../skills/architekt-wnetrz/SKILL.md` + `references/`) jest bundlowany do workera jako system prompt przy każdym build/deploy (script `scripts/build-skill.mjs` regeneruje `src/skill-content.generated.ts`). Po edycji skilla:

```bash
npm run deploy
```

## Logi

```bash
npm run tail
```

## Koszty (orientacyjnie)

| Usługa | Darmowy tier | Powyżej |
|---|---|---|
| Workers | 100k req/dzień | $5/mc za 10M |
| D1 | 5GB storage, 5M read/dzień | $0.75/GB |
| R2 | 10GB storage, 1M op/mc | $0.015/GB |
| Claude API | brak | ~$3-15/M tokens (Sonnet z cache) |
| Gemini Nano Banana | ~1500 obrazów/dzień | $0.039/obraz |

Realny koszt: **kilka groszy za pełen projekt mieszkania** (zakładając cache hit dla skill prompt 116KB).

## Bezpieczeństwo

- Aplikacja jest **dla jednego użytkownika** (Ciebie). `SHARED_SECRET` w `NEXT_PUBLIC_*` w aplikacji jest świadome — pełni rolę hasła do API.
- Nie udostępniaj URL aplikacji innym.
- Jeśli secret wycieknie: `npm run secret:shared` (nowy), zaktualizuj `NEXT_PUBLIC_SHARED_SECRET` w Cloudflare Pages, rebuild.

## Wstecz: stare endpointy `/generate` i `/edit` zachowane

Dalej działają — pozwala to równolegle używać plugina Claude Code (`architekt-wnetrz` w marketplace) z tym samym workerem.

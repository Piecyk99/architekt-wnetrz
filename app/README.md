# Architekt Wnętrz — frontend (Next.js)

Mobile-first PWA. Static export → Cloudflare Pages.

## Lokalnie

```bash
cd app
npm install
cp .env.local.example .env.local
# Edytuj .env.local — wpisz URL workera (np. http://localhost:8787 dla dev)
npm run dev
```

Otwórz http://localhost:3000

## Build & deploy do Cloudflare Pages

```bash
npm run build                       # generuje out/
npx wrangler pages deploy out --project-name=architekt-wnetrz
```

Po pierwszym deploy Cloudflare zapyta o utworzenie projektu Pages — potwierdź.

## Zmienne środowiskowe

Ustaw w **Cloudflare Pages → Settings → Environment Variables** (production):

| Zmienna | Wartość |
|---|---|
| `NEXT_PUBLIC_API_URL` | URL workera, np. `https://architekt-wnetrz.<subdomena>.workers.dev` |
| `NEXT_PUBLIC_SHARED_SECRET` | To samo co `wrangler secret put SHARED_SECRET` w workerze |

Po zmianie env zrób rebuild (`npm run pages:deploy`).

## PWA — instalacja na telefonie

1. Otwórz URL Pages w Safari (iOS) lub Chrome (Android)
2. iOS: Share → "Dodaj do ekranu początkowego"
3. Android: trzy kropki → "Zainstaluj aplikację"

Działa offline tylko jako shell — dane idą przez worker (wymaga sieci).

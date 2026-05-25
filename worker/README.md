# meble-banana-worker

Cloudflare Worker który proxuje Gemini Nano Banana API. Pozwala skillowi `meble-architekt` generować obrazy z **dowolnego urządzenia** (telefon, web, desktop) bez wystawiania klucza API klientowi.

## Co to robi

```
[Skill na telefonie / Claude.ai] -- POST /generate + Bearer SHARED_SECRET
       ↓
[Cloudflare Worker (ten kod)] -- dodaje GEMINI_API_KEY z secrets
       ↓
[Gemini API] -- zwraca PNG w base64
       ↓
[Worker zwraca base64 do Claude'a]
       ↓
[Claude pokazuje obraz user'owi]
```

**Po co to przez Workera, a nie bezpośrednio z telefonu?**
- Klucz API NIE może lądować w prompcie / kodzie skilla (= upubliczniony = Google unieważnia)
- Worker trzyma klucz jako secret na serwerze Cloudflare
- Skill autoryzuje się `SHARED_SECRET`'em (też trzymanym jako env var w Claude.ai lub w prompcie skilla — ale to mniejsze ryzyko niż klucz Gemini)
- Workers darmowy tier: **100 000 requestów dziennie** = wystarczy z zapasem

## Instalacja krok po kroku

### 1. Konto Cloudflare (darmowe)

Wejdź na **dash.cloudflare.com** → załóż konto (jeśli nie masz). Workers działają na darmowym planie do 100k req/dzień.

### 2. Zainstaluj wrangler CLI

```powershell
npm install -g wrangler
```

Wymaga Node.js 18+. Jeśli nie masz Node: pobierz z `nodejs.org` (LTS).

### 3. Zaloguj się

```powershell
cd C:\Users\PC\meble-architekt\worker
wrangler login
```

Otworzy przeglądarkę → zaloguj się do Cloudflare → autoryzuj wrangler.

### 4. Zainstaluj zależności

```powershell
npm install
```

### 5. Wygeneruj SHARED_SECRET (silny token)

W PowerShell:
```powershell
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
$secret = [Convert]::ToBase64String($bytes)
$secret  # ZAPISZ ten ciąg — będziesz go potrzebował na obu końcach
```

Skopiuj wartość. Wygląda mniej więcej tak: `kJ8sLp9Wq2nMrTvXyZ...` (44 znaki).

### 6. Ustaw sekrety w Cloudflare

```powershell
# Klucz Gemini z aistudio.google.com/apikey
wrangler secret put GEMINI_API_KEY
# (wklej AIza... + Enter)

# Shared secret z kroku 5
wrangler secret put SHARED_SECRET
# (wklej wygenerowany base64 + Enter)
```

### 7. Deploy

```powershell
wrangler deploy
```

Wrangler zwróci URL typu: `https://meble-banana.<twoj-subdomen>.workers.dev`

### 8. Test endpointu /health

```powershell
Invoke-RestMethod -Uri "https://meble-banana.<twoj-subdomen>.workers.dev/health"
# Powinno zwrócić: ok=True ts=<timestamp>
```

### 9. Test generacji

```powershell
$secret = "<twoj SHARED_SECRET z kroku 5>"
$body = @{
  prompt = "Architectural interior photograph of a modern kitchen with walnut royal smooth matte cabinet fronts, cream interior, thin black bar handles, 3000K LED under upper cabinets, dark stone worktop. Sony A7R IV 24mm lens, soft daylight, Architectural Digest editorial."
  aspectRatio = "16:9"
  resolution = "2K"
} | ConvertTo-Json

$response = Invoke-RestMethod `
  -Uri "https://meble-banana.<twoj-subdomen>.workers.dev/generate" `
  -Method Post `
  -Headers @{ "Authorization" = "Bearer $secret" } `
  -ContentType "application/json" `
  -Body $body

[System.IO.File]::WriteAllBytes("C:\Users\PC\test-worker.png", [Convert]::FromBase64String($response.imageBase64))
Start-Process "C:\Users\PC\test-worker.png"
```

Jeśli obraz się otworzy — **Worker działa** i obsługuje generację end-to-end.

## Podpięcie do skilla meble-architekt

W `meble-architekt/SKILL.md` Faza 3 (tryb fallback / mobile) wywołuje endpoint Workera. Klient (skill na Claude.ai) musi mieć dostęp do SHARED_SECRET.

**Bezpieczna opcja:** w skillu trzymaj placeholder `<<WORKER_URL>>` i `<<SHARED_SECRET>>`, a user wkleja je raz po deployowaniu. Patrz `references/cloudflare-worker.md` w katalogu skilla.

## Limity i koszty

| Komponent              | Darmowe                    | Płatne (po wyjściu)           |
|------------------------|----------------------------|-------------------------------|
| Cloudflare Workers     | 100k req/dzień             | $5/mc za 10M req              |
| Gemini Nano Banana 2   | ~1500 obrazów/dzień (free) | $0.039 / obraz (≈16 gr)       |

**Praktyczny scenariusz:** 10 projektów mebli dziennie × 2 obrazy/projekt = 20 generacji = pełnowymiarowo w darmowym tierze Gemini.

## Bezpieczeństwo

- **Nigdy** nie commituj `GEMINI_API_KEY` ani `SHARED_SECRET` do git
- `wrangler secret put` zapisuje wartości szyfrowane po stronie Cloudflare
- Worker waliduje Bearer token na każdym requeście — bez tokenu zwraca 401
- CORS ograniczony do `claude.ai` (zmień `ALLOWED_ORIGINS` w `wrangler.toml` jeśli potrzebujesz innych klientów)
- Jeśli SHARED_SECRET wycieknie: wygeneruj nowy, ustaw `wrangler secret put SHARED_SECRET`, zaktualizuj skill

## Tail logów (debug)

```powershell
wrangler tail
```

Pokazuje logi requestów w czasie rzeczywistym. Pomocne gdy coś nie działa.

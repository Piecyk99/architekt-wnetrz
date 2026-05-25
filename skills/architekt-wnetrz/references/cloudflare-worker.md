# Cloudflare Worker — instrukcja dla skilla

Ten plik jest **referencją dla skilla meble-architekt**, jak wywołać Cloudflare Worker w trybie fallback (telefon, claude.ai mobile).

## Konfiguracja po deployowaniu

Po deployowaniu Workera (instrukcja: `worker/README.md`) user wstawia tu dwie wartości:

- **WORKER_URL** = `https://meble-banana.<twoj-subdomen>.workers.dev`
- **SHARED_SECRET** = (44-znakowy base64 wygenerowany podczas instalacji)

**WAŻNE:** jeśli wgrywasz skill na Claude.ai mobile, NIE wpisuj SHARED_SECRET tutaj na sztywno (zostanie wgrany na konto Claude). Zamiast tego user przekazuje go w prompcie pierwszego użycia: *"mój worker to https://... a secret to ABC..."*, a skill zapamiętuje go w pamięci konwersacji.

## Endpoint: POST /generate

**Request:**
```json
POST https://meble-banana.<subdomen>.workers.dev/generate
Authorization: Bearer <SHARED_SECRET>
Content-Type: application/json

{
  "prompt": "Architectural interior photograph of a kitchen with...",
  "aspectRatio": "16:9",
  "resolution": "2K",
  "model": "gemini-3.1-flash-image-preview"
}
```

**Response (200):**
```json
{
  "imageBase64": "iVBORw0KGgoAAAANS...",
  "mimeType": "image/png",
  "text": "",
  "model": "gemini-3.1-flash-image-preview",
  "aspectRatio": "16:9",
  "resolution": "2K"
}
```

**Response (błąd):**
```json
{ "error": "Gemini API 429: Rate limit exceeded" }
```

## Endpoint: POST /edit

**Request:**
```json
POST https://meble-banana.<subdomen>.workers.dev/edit
Authorization: Bearer <SHARED_SECRET>
Content-Type: application/json

{
  "prompt": "Change the worktop to white marble",
  "imageBase64": "<base64 of previous image>",
  "imageMimeType": "image/png",
  "aspectRatio": "16:9",
  "resolution": "2K"
}
```

## Jak skill wywołuje Worker (tryb 3 fallback)

Jeśli MCP `nanobanana-mcp` niedostępne i nie ma dostępu do `scripts/generate.py`:

1. Pobierz `WORKER_URL` i `SHARED_SECRET` z kontekstu konwersacji (user wkleił je wcześniej)
2. Zbuduj prompt (5-component formula, patrz SKILL.md Faza 3b)
3. Wywołaj `POST /generate`:
   ```
   fetch(WORKER_URL + "/generate", {
     method: "POST",
     headers: {
       "Content-Type": "application/json",
       "Authorization": "Bearer " + SHARED_SECRET
     },
     body: JSON.stringify({ prompt, aspectRatio, resolution })
   })
   ```
4. Z response weź `imageBase64`
5. Pokaż user'owi: zdekoduj base64 i wyświetl jako obraz inline w konwersacji
6. (Opcjonalnie) zapytaj user'a czy zapisać lokalnie

## Aspect ratio routing

| Co projektujesz                  | aspectRatio  | resolution |
|----------------------------------|--------------|------------|
| Kuchnia widok szeroki            | `16:9`       | `2K`       |
| Kuchnia narożna / L-kształt      | `4:3`        | `2K`       |
| Szafa / garderoba (frontalnie)   | `3:4`        | `2K`       |
| Łazienka kompaktowa              | `4:5`        | `2K`       |
| Zbliżenie detalu                 | `1:1`        | `2K`       |
| Full room cinematic              | `21:9`       | `2K`       |

## Obsługa błędów

| Status / message               | Reakcja                                                    |
|--------------------------------|------------------------------------------------------------|
| 401 Unauthorized               | SHARED_SECRET zły — poproś user'a o aktualny token         |
| 400 Missing prompt             | bug w skillu — sprawdź body                                |
| 500 z `IMAGE_SAFETY`           | przeformułuj prompt, dodaj "artistic editorial"            |
| 500 z `FAILED_PRECONDITION`    | user musi włączyć billing w Google AI Studio               |
| 500 z `429`                    | czekaj 60s, retry                                          |
| Network error / timeout        | Worker padł lub przeciążony — fallback do manualnego promptu |

## Limity

- Worker free tier: **100k req/dzień** (z zapasem na lata projektów)
- Gemini free tier: **~1500 obrazów/dzień**, ~10 RPM
- Worker CPU limit: 50ms (Gemini call to wait time, nie CPU — bezpiecznie)
- Worker memory: 128MB (PNG 2K ≈ 2-4MB, base64 ≈ 5-8MB, OK)

import asyncio
from datetime import datetime
import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pro Uptime Monitor")

# --- DATABASE IN MEMORIA ---
# Simula un database con i siti da monitorare e lo storico delle risposte
SITI_DA_MONITORARE = [
    "https://www.google.com",
    "https://www.github.com",
    "https://un-sito-che-non-esiste-12345.com",
]

storico_monitoraggio = {
    url: {"status": "Sconosciuto", "ultimo_controllo": "-", "tempo_risposta": 0, "storico": []}
    for url in SITI_DA_MONITORARE
}


# --- MOTORE DI MONITORAGGIO ASINCRONO ---
async def controlla_sito(client: httpx.AsyncClient, url: str):
    """Invia una richiesta HTTP al sito e calcola il tempo di risposta."""
    orario = datetime.now().strftime("%H:%M:%S")
    try:
        inizio = asyncio.get_event_loop().time()
        risposta = await client.get(url, timeout=5.0)
        durata = round((asyncio.get_event_loop().time() - inizio) * 1000, 2)  # in millisecondi

        if risposta.status_code == 200:
            stato = "🟢 ONLINE"
        else:
            stato = f"🔴 ERRORE ({risposta.status_code})"
    except Exception:
        stato = "🔴 OFFLINE (Timeout/Errore Connessione)"
        durata = 0

    # Aggiorna lo stato nel nostro "database"
    storico_monitoraggio[url]["status"] = stato
    storico_monitoraggio[url]["ultimo_controllo"] = orario
    storico_monitoraggio[url]["tempo_risposta"] = durata
    
    # Tiene solo gli ultimi 5 controlli nello storico
    storico_monitoraggio[url]["storico"].append(f"[{orario}] {stato}")
    if len(storico_monitoraggio[url]["storico"]) > 5:
        storico_monitoraggio[url]["storico"].pop(0)


async def background_monitor_loop():
    """Loop infinito che gira in background ogni 30 secondi."""
    async with httpx.AsyncClient() as client:
        while True:
            # Controlla tutti i siti in parallelo grazie ad asyncio
            task = [controlla_sito(client, url) for url in SITI_DA_MONITORARE]
            await asyncio.gather(*task)
            await asyncio.sleep(30)  # Aspetta 30 secondi prima del prossimo controllo


@app.on_event("startup")
async def startup_event():
    """Avvia il monitoraggio in background all'avvio del server."""
    asyncio.create_task(background_monitor_loop())


# --- INTERFACCIA WEB (FRONTEND) ---
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Genera una dashboard HTML dinamica per mostrare i dati."""
    html_content = """
    <html>
        <head>
            <title>Dashboard Monitoraggio</title>
            <meta http-equiv="refresh" content="10"> <!-- Ricarica la pagina ogni 10s -->
            <style>
                body { font-family: Arial, sans-serif; background-color: #121212; color: #e0e0e0; padding: 40px; }
                h1 { color: #ffffff; }
                .card { background-color: #1e1e1e; border-radius: 8px; padding: 20px; margin-bottom: 15px; border-left: 5px solid #444; }
                .ONLINE { border-left-color: #4caf50; }
                .OFFLINE, .ERRORE { border-left-color: #f44336; }
                .url { font-size: 1.2em; font-weight: bold; }
                .info { margin-top: 8px; color: #aaaaaa; }
                .badge { padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <h1>🖥️ API & Website Uptime Monitor</h1>
            <p>La pagina si aggiorna automaticamente ogni 10 secondi. Controllo server ogni 30 secondi.</p>
    """
    
    for url, dati in storico_monitoraggio.items():
        classe_stato = "ONLINE" if "🟢" in dati["status"] else "OFFLINE"
        html_content += f"""
        <div class="card {classe_stato}">
            <div class="url">{url}</div>
            <div class="info">
                Stato: <span class="badge">{dati['status']}</span> | 
                Risposta: <strong>{dati['tempo_risposta']} ms</strong> | 
                Ultimo Controllo: {dati['ultimo_controllo']}
            </div>
            <div style="font-size: 0.85em; color: #777; margin-top: 8px;">
                Ultime verifiche: {", ".join(dati['storico'])}
            </div>
        </div>
        """
        
    html_content += "</body></html>"
    return html_content

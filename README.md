# 📈 Fastweb-Uptime-Monitor

Un servizio leggero, asincrono e performante per il monitoraggio in tempo reale dello stato (uptime) di siti web ed API. Sviluppato in Python sfruttando la potenza di **FastAPI** e **HTTPX**.

Questo progetto replica le funzionalità core di servizi commerciali come *Uptime Robot* o *Pingdom*, dimostrando l'implementazione di logiche asincrone concorrenti in background e la generazione di dashboard dinamiche.

---

## ✨ Funzionalità

* **Monitoraggio Asincrono Concorrente:** Grazie ad `asyncio` e `httpx`, il sistema è in grado di controllare centinaia di URL in parallelo senza bloccare il server, riducendo al minimo il consumo di CPU e RAM.
* **Dashboard Web Integrata:** Un'interfaccia web scura (Dark Mode), moderna e reattiva che si aggiorna automaticamente ogni 10 secondi per mostrare lo stato dei servizi in tempo reale.
* **Metriche di Performance:** Calcolo preciso dei tempi di risposta dei server espressi in millisecondi (ms).
* **Storico dei Controlli:** Conservazione in memoria degli ultimi stati del server per identificare anomalie o micro-interruzioni intermittenti.
* **Resilienza:** Gestione avanzata dei timeout e degli errori di rete (connessione fallita, domini inesistenti, errori 5xx).

---

## 🛠️ Stack Tecnologico

* **Linguaggio:** Python 3.9+
* **Framework Backend:** FastAPI
* **Client HTTP Asincrono:** HTTPX
* **Server ASGI:** Uvicorn

---

## ⚙️ Installazione e Utilizzo

1. **Clona la repository:**
   ```bash
   git clone [https://github.com/IlTuoUsername/Fastweb-Uptime-Monitor.git](https://github.com/IlTuoUsername/Fastweb-Uptime-Monitor.git)
   cd Fastweb-Uptime-Monitor

 Installa le dipendenze:

Bash
pip install -r requirements.txt
Configura i siti da monitorare:
Apri il file app.py e modifica la lista SITI_DA_MONITORARE inserendo gli URL che desideri tracciare:

Python
SITI_DA_MONITORARE = [
    "[https://www.google.com](https://www.google.com)",
    "[https://www.github.com](https://www.github.com)",
    "[https://tuo-sito-personale.com](https://tuo-sito-personale.com)"
]
Avvia il server:

Bash
uvicorn app:app --reload
Accedi alla dashboard:
Apri il tuo browser e naviga su http://127.0.0.1:8000

💼 Sviluppo su Commissione e Personalizzazioni
Sei un'azienda, un amministratore di rete o un privato e hai bisogno di una soluzione di monitoraggio professionale su misura per la tua infrastruttura?

Posso estendere e personalizzare questo software secondo le tue esigenze specifiche. Alcune delle funzionalità integrabili su richiesta:

Sistemi di Notifica Push: Avvisi istantanei in tempo reale su Telegram, Discord, Slack, WhatsApp o via Email (SendGrid/SMTP) non appena un servizio va offline.

Database Persistente: Integrazione con PostgreSQL, MySQL o MongoDB per salvare lo storico dei controlli nel lungo periodo ed esportare report mensili sull'affidabilità (SLA).

Grafici Avanzati: Pannelli statistici interattivi con grafici sull'andamento dei tempi di risposta e percentuali di uptime mensili.

Pannello Multi-Utente (SaaS): Sistema di autenticazione sicuro (OAuth2/JWT) con gestione dei ruoli, piani di abbonamento (Stripe) e dashboard private per i tuoi clienti.

📩 Sei interessato? Contattami in privato qui su GitHub o via email per richiedere un preventivo personalizzato!

📄 Licenza
Questo progetto è rilasciato sotto i termini della licenza MIT. Consulta il file LICENSE per ulteriori dettagli. Lo sviluppo è libero di essere modificato e integrato anche in progetti commerciali.

# 📈 FastPing

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
   git clone https://github.com/Fastweb/FastPing.git
   cd FastPing

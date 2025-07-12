# FormLog - Mini-app Fullstack

Una mini-applicazione fullstack per la gestione dei contatti con:
- **Frontend**: React con Vite
- **Backend**: FastAPI (Python)
- **Database**: MongoDB

## 🚀 Funzionalità

- Form di contatto responsive con validazione
- Invio dati tramite API REST
- Salvataggio in database MongoDB
- Messaggi di conferma e gestione errori
- Design moderno e user-friendly

## 📋 Prerequisiti

Assicurati di avere installato:
- **Node.js** (versione 18 o superiore)
- **Python** (versione 3.8 o superiore)
- **Docker** e **Docker Compose**

## 🛠️ Installazione e Avvio

### 1. Clona il repository
```bash
git clone <url-repository>
cd formlog
```

### 2. Avvia MongoDB con Docker
```bash
docker-compose up -d
```

### 3. Configura il Backend

#### Installa le dipendenze Python
```bash
cd backend
pip install -r requirements.txt
```

#### Configura le variabili d'ambiente
Crea un file `.env` nella cartella `backend` con il seguente contenuto:
```
MONGODB_URL=mongodb://admin:password@localhost:27017/formlog?authSource=admin
DATABASE_NAME=formlog
COLLECTION_NAME=contacts
```

#### Avvia il server FastAPI
```bash
# Dalla cartella backend
python main.py

# Oppure usando uvicorn direttamente
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Il backend sarà disponibile su: `http://localhost:8000`

### 4. Configura il Frontend

#### Installa le dipendenze Node.js
```bash
cd ../frontend
npm install
```

#### Avvia il server di sviluppo
```bash
npm run dev
```

Il frontend sarà disponibile su: `http://localhost:3000`

## 🎯 Utilizzo

1. Apri il browser e vai su `http://localhost:3000`
2. Compila il form con:
   - **Nome**: Il tuo nome
   - **Email**: La tua email (validata automaticamente)
   - **Messaggio**: Il tuo messaggio
3. Clicca su "Invia Messaggio"
4. Vedrai un messaggio di conferma se l'invio è andato a buon fine

## 📚 API Endpoints

### POST `/api/contacts`
Crea un nuovo contatto

**Request Body:**
```json
{
  "nome": "Mario Rossi",
  "email": "mario.rossi@example.com",
  "messaggio": "Ciao, questo è un messaggio di prova"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Messaggio inviato con successo!",
  "contact_id": "507f1f77bcf86cd799439011"
}
```

### GET `/api/contacts`
Recupera tutti i contatti (per debug)

### GET `/api/health`
Health check del server

## 🏗️ Struttura del Progetto

```
formlog/
├── backend/
│   ├── main.py                 # App FastAPI principale
│   ├── requirements.txt        # Dipendenze Python
│   └── .env.example           # Esempio variabili d'ambiente
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ContactForm.jsx    # Componente form
│   │   │   └── ContactForm.css    # Stili form
│   │   ├── App.jsx                # Componente principale
│   │   ├── App.css                # Stili app
│   │   ├── index.css              # Stili globali
│   │   └── main.jsx               # Entry point
│   ├── package.json               # Dipendenze Node.js
│   ├── vite.config.js             # Configurazione Vite
│   └── index.html                 # HTML principale
├── docker-compose.yml             # Configurazione MongoDB
└── README.md                      # Documentazione
```

## 🔧 Sviluppo

### Comandi Utili

**Backend:**
```bash
# Avvia con reload automatico
uvicorn main:app --reload

# Visualizza logs
python main.py
```

**Frontend:**
```bash
# Avvia sviluppo
npm run dev

# Build per produzione
npm run build

# Lint del codice
npm run lint
```

**MongoDB:**
```bash
# Avvia MongoDB
docker-compose up -d

# Ferma MongoDB
docker-compose down

# Visualizza logs
docker-compose logs -f mongodb
```

## 🐳 MongoDB

### Configurazione Database
- **Host**: localhost:27017
- **Database**: formlog
- **Collection**: contacts
- **Username**: admin
- **Password**: password

### Connessione diretta
```bash
# Con MongoDB Compass
mongodb://admin:password@localhost:27017/formlog?authSource=admin

# Con mongo shell
mongo mongodb://admin:password@localhost:27017/formlog?authSource=admin
```

## 🛡️ Sicurezza

- Validazione input lato client e server
- Validazione email con pydantic
- Gestione errori per evitare crash
- CORS configurato per localhost

## 📝 Note Tecniche

- **FastAPI**: Framework asincrono per API REST
- **Motor**: Driver MongoDB asincrono per Python
- **Vite**: Build tool veloce per React
- **Axios**: Client HTTP per le chiamate API
- **CSS moderno**: Flexbox, Grid, e animazioni smooth

## 🚨 Troubleshooting

### Errore connessione MongoDB
```bash
# Verifica che MongoDB sia in esecuzione
docker-compose ps

# Riavvia MongoDB
docker-compose restart mongodb
```

### Errore CORS
Assicurati che il frontend sia in esecuzione su `http://localhost:3000` e il backend su `http://localhost:8000`

### Errore dipendenze
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

## 📄 Licenza

Questo progetto è rilasciato sotto licenza MIT.

## 🤝 Contributi

I contributi sono benvenuti! Apri una issue o una pull request.

---

**Creato con ❤️ usando React, FastAPI e MongoDB** 
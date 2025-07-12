from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os
from typing import Optional

# Configurazione dell'app
app = FastAPI(title="FormLog API", version="1.0.0")

# Configurazione CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurazione Database
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://admin:password@localhost:27017/formlog?authSource=admin")
DATABASE_NAME = os.getenv("DATABASE_NAME", "formlog")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "contacts")

client: Optional[AsyncIOMotorClient] = None

# Modelli Pydantic
class ContactForm(BaseModel):
    nome: str
    email: EmailStr
    messaggio: str

class ContactResponse(BaseModel):
    id: str
    nome: str
    email: str
    messaggio: str
    data_creazione: datetime

# Eventi di avvio e chiusura
@app.on_event("startup")
async def startup_db_client():
    global client
    client = AsyncIOMotorClient(MONGODB_URL)
    try:
        # Test della connessione
        await client.admin.command('ping')
        print("✅ Connesso a MongoDB!")
    except Exception as e:
        print(f"❌ Errore connessione MongoDB: {e}")

@app.on_event("shutdown")
async def shutdown_db_client():
    global client
    if client:
        client.close()

# Endpoint per il form di contatto
@app.post("/api/contacts", response_model=dict)
async def create_contact(contact: ContactForm):
    try:
        # Prepara i dati per il database
        contact_data = {
            "nome": contact.nome,
            "email": contact.email,
            "messaggio": contact.messaggio,
            "data_creazione": datetime.now()
        }
        
        # Inserisce nel database
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        result = await collection.insert_one(contact_data)
        
        return {
            "success": True,
            "message": "Messaggio inviato con successo!",
            "contact_id": str(result.inserted_id)
        }
    
    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")
        raise HTTPException(status_code=500, detail="Errore interno del server")

# Endpoint per recuperare tutti i contatti (opzionale, per debug)
@app.get("/api/contacts")
async def get_contacts():
    try:
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        contacts = []
        
        async for contact in collection.find():
            contacts.append({
                "id": str(contact["_id"]),
                "nome": contact["nome"],
                "email": contact["email"],
                "messaggio": contact["messaggio"],
                "data_creazione": contact["data_creazione"]
            })
        
        return {"contacts": contacts}
    
    except Exception as e:
        print(f"Errore durante il recupero: {e}")
        raise HTTPException(status_code=500, detail="Errore interno del server")

# Endpoint di health check
@app.get("/api/health")
async def health_check():
    return {"status": "OK", "message": "API funzionante"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "FormLog API - Server running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
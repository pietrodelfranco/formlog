from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os
from typing import Optional

# App configuration
app = FastAPI(title="FormLog API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://admin:password@localhost:27017/formlog?authSource=admin")
DATABASE_NAME = os.getenv("DATABASE_NAME", "formlog")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "contacts")

client: Optional[AsyncIOMotorClient] = None

# Pydantic models
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    id: str
    name: str
    email: str
    message: str
    created_date: datetime

# Startup and shutdown events
@app.on_event("startup")
async def startup_db_client():
    global client
    client = AsyncIOMotorClient(MONGODB_URL)
    try:
        # Connection test
        await client.admin.command('ping')
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print(f"❌ MongoDB connection error: {e}")

@app.on_event("shutdown")
async def shutdown_db_client():
    global client
    if client:
        client.close()

# Contact form endpoint
@app.post("/api/contacts", response_model=dict)
async def create_contact(contact: ContactForm):
    try:
        # Prepare data for database
        contact_data = {
            "name": contact.name,
            "email": contact.email,
            "message": contact.message,
            "created_date": datetime.now()
        }
        
        # Insert into database
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        result = await collection.insert_one(contact_data)
        
        return {
            "success": True,
            "message": "Message sent successfully!",
            "contact_id": str(result.inserted_id)
        }
    
    except Exception as e:
        print(f"Error during insertion: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to retrieve all contacts (optional, for debug)
@app.get("/api/contacts")
async def get_contacts():
    try:
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        contacts = []
        
        async for contact in collection.find():
            contacts.append({
                "id": str(contact["_id"]),
                "name": contact["name"],
                "email": contact["email"],
                "message": contact["message"],
                "created_date": contact["created_date"]
            })
        
        return {"contacts": contacts}
    
    except Exception as e:
        print(f"Error during retrieval: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "OK", "message": "API working"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "FormLog API - Server running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 
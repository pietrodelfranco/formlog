#!/bin/bash

# Script di avvio per il backend FormLog

echo "🚀 Avvio del backend FormLog..."

# Verifica che il file .env esista
if [ ! -f ".env" ]; then
    echo "⚠️  File .env non trovato. Copiando da .env.example..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ File .env creato da .env.example"
    else
        echo "❌ File .env.example non trovato. Creando .env con configurazione predefinita..."
        cat > .env << EOF
MONGODB_URL=mongodb://admin:password@localhost:27017/formlog?authSource=admin
DATABASE_NAME=formlog
COLLECTION_NAME=contacts
EOF
        echo "✅ File .env creato con configurazione predefinita"
    fi
fi

# Installa le dipendenze se non già installate
if [ ! -d "venv" ]; then
    echo "📦 Creando ambiente virtuale..."
    python -m venv venv
fi

echo "🔧 Attivando ambiente virtuale..."
source venv/bin/activate

echo "📦 Installando dipendenze..."
pip install -r requirements.txt

echo "🌐 Avviando server FastAPI..."
python main.py 
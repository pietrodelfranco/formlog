#!/bin/bash

# Script per avviare l'intera applicazione FormLog

echo "🚀 Avvio completo di FormLog..."

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Funzione per stampare messaggi colorati
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verifica prerequisiti
print_status "Verifica prerequisiti..."

if ! command -v docker &> /dev/null; then
    print_error "Docker non è installato"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose non è installato"
    exit 1
fi

if ! command -v node &> /dev/null; then
    print_error "Node.js non è installato"
    exit 1
fi

if ! command -v python &> /dev/null; then
    print_error "Python non è installato"
    exit 1
fi

print_status "Tutti i prerequisiti sono soddisfatti ✅"

# Avvia MongoDB
print_status "Avvio MongoDB con Docker..."
docker-compose up -d
sleep 5

# Verifica che MongoDB sia in esecuzione
if ! docker-compose ps | grep -q "Up"; then
    print_error "Errore nell'avvio di MongoDB"
    exit 1
fi

print_status "MongoDB avviato con successo ✅"

# Avvia Backend
print_status "Preparazione backend..."
cd backend

# Crea file .env se non esiste
if [ ! -f ".env" ]; then
    print_warning "File .env non trovato. Creando configurazione predefinita..."
    cat > .env << EOF
MONGODB_URL=mongodb://admin:password@localhost:27017/formlog?authSource=admin
DATABASE_NAME=formlog
COLLECTION_NAME=contacts
EOF
    print_status "File .env creato ✅"
fi

# Installa dipendenze Python
print_status "Installazione dipendenze Python..."
pip install -r requirements.txt

# Avvia backend in background
print_status "Avvio backend FastAPI..."
python main.py &
BACKEND_PID=$!

cd ..

# Avvia Frontend
print_status "Preparazione frontend..."
cd frontend

# Installa dipendenze Node.js
print_status "Installazione dipendenze Node.js..."
npm install

# Avvia frontend in background
print_status "Avvio frontend React..."
npm run dev &
FRONTEND_PID=$!

cd ..

# Informazioni finali
print_status "🎉 FormLog avviato con successo!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend:  http://localhost:8000"
echo "🔍 API Docs: http://localhost:8000/docs"
echo "🍃 MongoDB:  mongodb://admin:password@localhost:27017/formlog"
echo ""
echo "Per fermare l'applicazione, premi Ctrl+C"
echo ""

# Gestione segnale di interruzione
trap 'print_status "Arresto dell'\''applicazione..."; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; docker-compose down; exit 0' INT

# Mantieni lo script in esecuzione
wait 
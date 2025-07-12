# FormLog - Fullstack Mini-app

A fullstack mini-application for contact management with:
- **Frontend**: React with Vite
- **Backend**: FastAPI (Python)
- **Database**: MongoDB

## 🚀 Features

- Responsive contact form with validation
- Data submission via REST API
- Data storage in MongoDB database
- Confirmation messages and error handling
- Modern and user-friendly design

## 📋 Prerequisites

Make sure you have installed:
- **Node.js** (version 18 or higher)
- **Python** (version 3.8 or higher)
- **Docker** and **Docker Compose**

## 🛠️ Installation and Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd formlog
```

### 2. Start MongoDB with Docker
```bash
docker-compose up -d
```

### 3. Configure Backend

#### Install Python dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Configure environment variables
Create a `.env` file in the `backend` folder with the following content:
```
MONGODB_URL=mongodb://admin:password@localhost:27017/formlog?authSource=admin
DATABASE_NAME=formlog
COLLECTION_NAME=contacts
```

#### Start FastAPI server
```bash
# From backend folder
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`

### 4. Configure Frontend

#### Install Node.js dependencies
```bash
cd ../frontend
npm install
```

#### Start development server
```bash
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## 🎯 Usage

1. Open browser and go to `http://localhost:3000`
2. Fill the form with:
   - **Name**: Your name
   - **Email**: Your email (automatically validated)
   - **Message**: Your message
3. Click "Send Message"
4. You'll see a confirmation message if submission is successful

## 📚 API Endpoints

### POST `/api/contacts`
Create a new contact

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "message": "Hello, this is a test message"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Message sent successfully!",
  "contact_id": "507f1f77bcf86cd799439011"
}
```

### GET `/api/contacts`
Retrieve all contacts (for debugging)

### GET `/api/health`
Server health check

## 🏗️ Project Structure

```
formlog/
├── backend/
│   ├── main.py                 # Main FastAPI app
│   ├── requirements.txt        # Python dependencies
│   └── .env.example           # Environment variables example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ContactForm.jsx    # Form component
│   │   │   └── ContactForm.css    # Form styles
│   │   ├── App.jsx                # Main component
│   │   ├── App.css                # App styles
│   │   ├── index.css              # Global styles
│   │   └── main.jsx               # Entry point
│   ├── package.json               # Node.js dependencies
│   ├── vite.config.js             # Vite configuration
│   └── index.html                 # Main HTML
├── docker-compose.yml             # MongoDB configuration
└── README.md                      # Documentation
```

## 🔧 Development

### Useful Commands

**Backend:**
```bash
# Start with auto-reload
uvicorn main:app --reload

# View logs
python main.py
```

**Frontend:**
```bash
# Start development
npm run dev

# Build for production
npm run build

# Lint code
npm run lint
```

**MongoDB:**
```bash
# Start MongoDB
docker-compose up -d

# Stop MongoDB
docker-compose down

# View logs
docker-compose logs -f mongodb
```

## 🐳 MongoDB

### Database Configuration
- **Host**: localhost:27017
- **Database**: formlog
- **Collection**: contacts
- **Username**: admin
- **Password**: password

### Direct connection
```bash
# With MongoDB Compass
mongodb://admin:password@localhost:27017/formlog?authSource=admin

# With mongo shell
mongo mongodb://admin:password@localhost:27017/formlog?authSource=admin
```

## 🛡️ Security

- Input validation on client and server side
- Email validation with pydantic
- Error handling to prevent crashes
- CORS configured for localhost

## 📝 Technical Notes

- **FastAPI**: Asynchronous framework for REST APIs
- **Motor**: Asynchronous MongoDB driver for Python
- **Vite**: Fast build tool for React
- **Axios**: HTTP client for API calls
- **Modern CSS**: Flexbox, Grid, and smooth animations

## 🚨 Troubleshooting

### MongoDB connection error
```bash
# Check if MongoDB is running
docker-compose ps

# Restart MongoDB
docker-compose restart mongodb
```

### CORS error
Make sure frontend is running on `http://localhost:3000` and backend on `http://localhost:8000`

### Dependencies error
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

## 📄 License

This project is released under MIT license.

## 🤝 Contributions

Contributions are welcome! Open an issue or a pull request.

---

**Created with ❤️ using React, FastAPI and MongoDB**

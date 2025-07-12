import React from 'react'
import ContactForm from './components/ContactForm'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>FormLog - Contatti</h1>
        <p>Invia un messaggio attraverso il form di contatto</p>
      </header>
      <main>
        <ContactForm />
      </main>
    </div>
  )
}

export default App 
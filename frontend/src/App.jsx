import React from 'react'
import ContactForm from './components/ContactForm'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>FormLog - Contacts</h1>
        <p>Send a message through the contact form</p>
      </header>
      <main>
        <ContactForm />
      </main>
    </div>
  )
}

export default App 
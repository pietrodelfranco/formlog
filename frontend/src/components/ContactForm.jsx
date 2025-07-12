import React, { useState } from 'react'
import axios from 'axios'
import './ContactForm.css'

const ContactForm = () => {
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    messaggio: ''
  })
  
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [submitStatus, setSubmitStatus] = useState(null) // 'success', 'error', null

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsSubmitting(true)
    setSubmitStatus(null)

    try {
      const response = await axios.post('/api/contacts', formData)
      
      if (response.data.success) {
        setSubmitStatus('success')
        setFormData({ nome: '', email: '', messaggio: '' }) // Reset form
      } else {
        setSubmitStatus('error')
      }
    } catch (error) {
      console.error('Errore durante l\'invio:', error)
      setSubmitStatus('error')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="contact-form-container">
      <form onSubmit={handleSubmit} className="contact-form">
        <h2>Contattaci</h2>
        
        <div className="form-group">
          <label htmlFor="nome">Nome *</label>
          <input
            type="text"
            id="nome"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            required
            placeholder="Inserisci il tuo nome"
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email *</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            placeholder="Inserisci la tua email"
          />
        </div>

        <div className="form-group">
          <label htmlFor="messaggio">Messaggio *</label>
          <textarea
            id="messaggio"
            name="messaggio"
            value={formData.messaggio}
            onChange={handleChange}
            required
            rows="5"
            placeholder="Scrivi il tuo messaggio..."
          />
        </div>

        <button 
          type="submit" 
          className="submit-btn"
          disabled={isSubmitting}
        >
          {isSubmitting ? 'Invio in corso...' : 'Invia Messaggio'}
        </button>

        {submitStatus === 'success' && (
          <div className="success-message">
            <p>✅ Messaggio inviato con successo!</p>
            <p>Ti risponderemo il prima possibile.</p>
          </div>
        )}

        {submitStatus === 'error' && (
          <div className="error-message">
            <p>❌ Errore nell'invio del messaggio.</p>
            <p>Riprova più tardi o contattaci direttamente.</p>
          </div>
        )}
      </form>
    </div>
  )
}

export default ContactForm 
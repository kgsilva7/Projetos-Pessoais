import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode> //testa a robustez do projeto para encontrar erros
    <App />
  </StrictMode>,
)

import React from 'react'
import ReactDOM from 'react-dom/client'
import Authentication from './Authentication'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
    <React.StrictMode>
        <Authentication />
    </React.StrictMode>,
)

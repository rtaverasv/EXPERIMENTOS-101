import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(page_title="Propuesta Especial", layout="wide")

# 2. Forzar el fondo blanco en la interfaz de Streamlit
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFFFF !important;
    }
    iframe {
        background-color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Todo el contenido interactivo y visual empaquetado de forma segura
componente_interactivo = """
<div class="main-container">
    <div class="titulo">¿QUIERES SER MI NOVIA?</div>
    
    <div class="contenedor-propuesta">
        <button id="botonNo" class="btn-no">NO</button>
        
        <img class="gatito-centro" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&auto=format&fit=crop&q=60" alt="Gatito Lindo">
        
        <button id="botonSi" class="btn-si" onclick="declaracionExitosa()">SÍ</button>
    </div>
    
    <h1 id="mensajeFinal" style="color: #FF4B4B; margin-top: 40px; display: none; font-family: sans-serif;">¡SABÍA QUE DIRÍAS QUE SÍ! 🐱❤️</h1>
</div>

<audio id="musicaGatito" autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>

<script>
    const botonNo = document.getElementById('botonNo');
    const mensajeFinal = document.getElementById('mensajeFinal');
    const musica = document.getElementById('musicaGatito');

    // Activar música con la primera interacción en la pantalla
    document.body.addEventListener('click', () => {
        musica.play().catch(() => {});
    }, { once: true });

    // Movimiento evasivo del botón NO
    botonNo.addEventListener('mouseover', function() {
        // Rango de movimiento aleatorio por toda la pantalla
        const x = Math.random() * (window.innerWidth - this.clientWidth - 100);
        const y = Math.random() * (window.innerHeight - this.clientHeight - 100);
        this.style.position = 'fixed';
        this.style.left = x + 'px';
        this.style.top = y + 'px';
        this.style.zIndex = '999'; // Mantenerlo siempre visible arriba de todo al moverse
    });

    function declaracionExitosa() {
        mensajeFinal.style.display = 'block';
        botonNo.style.display = 'none';
        alert('¡Viva! ¡Gracias por decir que SÍ! 😻🎉');
    }
</script>

<style>
    body {
        background-color: #FFFFFF !important;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    .main-container { 
        text-align: center; 
        font-family: 'Arial', sans-serif; 
        margin-top: 40px; 
        position: relative;
    }
    .titulo { 
        color: #FF4B4B; 
        font-size: 50px; 
        font-weight: bold; 
        margin-bottom: 40px; 
    }
    /* Contenedor flexible para alinear No - Gatito - Sí en una sola fila organizada */
    .contenedor-propuesta { 
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative; 
        width: 100%; 
        height: 350px; 
        gap: 40px;
    }
    /* Imagen fija y centrada del gatito */
    .gatito-centro {
        width: 260px;
        height: 260px;
        object-fit: cover;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        z-index: 5;
    }
    .btn-si { 
        background-color: #D2B4DE; /* Verde lila / Lavanda dulce */
        color: white; 
        border: none; 
        padding: 25px 80px; 
        font-size: 38px; 
        font-weight: bold; 
        border-radius: 15px; 
        cursor: pointer; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        z-index: 10;
        transition: transform 0.2s;
    }
    .btn-si:hover {
        transform: scale(1.05);
    }
    .btn-no { 
        background-color: #FF0000; /* Rojo */
        color: white; 
        border: none; 
        padding: 12px 35px; 
        font-size: 20px; 
        font-weight: bold; 
        border-radius: 8px; 
        cursor: pointer; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        z-index: 10;
        transition: top 0.1s ease, left 0.1s ease;
    }
</style>
"""

# 4. Renderizar el componente en la app con un tamaño generoso
components.html(componente_interactivo, height=750, scrolling=False)

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

# 3. Todo el contenido interactivo, visual y mensajes dinámicos
componente_interactivo = """
<div class="main-container">
    <div class="titulo">¿DIEGA LETICIA C. QUIERES SER MI NOVIA?</div>
    
    <div id="seccionPropuesta" class="contenedor-propuesta">
        <button id="botonNo" class="btn-no">NO</button>
        
        <img class="gatito-centro" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&auto=format&fit=crop&q=60" alt="Gatito Lindo Centro">
        
        <button id="botonSi" class="btn-si" onclick="declaracionExitosa()">SÍ</button>
    </div>
    
    <div id="contenedorVictoria" class="victoria-box">
        <h1 class="mensaje-final">¡SABÍA QUE DIRÍAS QUE SÍ! 🐱❤️</h1>
        <p class="mensaje-amor">Te mando besitos, tú sabrás dónde... 😏</p>
        <p class="mensaje-mua">MUAMUA 💋</p>
        <div class="firmas">👑 La mamá de Simba y papá de Michini 👑</div>
    </div>
</div>

<img class="gatito-lateral lateral-izq" src="https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400&auto=format&fit=crop&q=60" alt="Gatito Lindo Izquierda">
<img class="gatito-lateral lateral-der" src="https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=400&auto=format&fit=crop&q=60" alt="Gatito Lindo Derecha">

<audio id="musicaGatito" autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>

<script>
    const botonNo = document.getElementById('botonNo');
    const seccionPropuesta = document.getElementById('seccionPropuesta');
    const contenedorVictoria = document.getElementById('contenedorVictoria');
    const musica = document.getElementById('musicaGatito');

    // Activar música con la primera interacción en la pantalla
    document.body.addEventListener('click', () => {
        musica.play().catch(() => {});
    }, { once: true });

    // Movimiento evasivo del botón NO por toda la pantalla
    botonNo.addEventListener('mouseover', function() {
        const x = Math.random() * (window.innerWidth - this.clientWidth - 100);
        const y = Math.random() * (window.innerHeight - this.clientHeight - 100);
        this.style.position = 'fixed';
        this.style.left = x + 'px';
        this.style.top = y + 'px';
        this.style.zIndex = '999';
    });

    // Función cuando se hace clic en SÍ
    function declaracionExitosa() {
        // Ocultar los botones y el gatito central inicial
        seccionPropuesta.style.display = 'none';
        
        // Mostrar la hermosa caja de mensajes románticos
        contenedorVictoria.style.display = 'block';
        
        // Alerta opcional de celebración en pantalla
        alert('¡SÍII! 😻🎉 ¡Of

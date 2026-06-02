import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(page_title="Propuesta Especial", layout="wide")

# 2. Forzar el fondo blanco en la interfaz de Streamlit
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    iframe { background-color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Estilos visuales de la aplicación
estilos_css = """
<style>
    body { background-color: #FFFFFF !important; margin: 0; padding: 0; overflow-x: hidden; }
    .main-container { text-align: center; font-family: 'Arial', sans-serif; margin-top: 40px; position: relative; z-index: 10; }
    .titulo { color: #FF4B4B; font-size: 42px; font-weight: bold; margin-bottom: 40px; padding: 0 20px; }
    .contenedor-propuesta { display: flex; justify-content: center; align-items: center; position: relative; width: 100%; height: 350px; gap: 40px; }
    .gatito-centro { width: 260px; height: 260px; object-fit: cover; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); z-index: 5; }
    .btn-si { background-color: #D2B4DE; color: white; border: none; padding: 25px 80px; font-size: 38px; font-weight: bold; border-radius: 15px; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.15); z-index: 10; transition: transform 0.2s; }
    .btn-si:hover { transform: scale(1.05); }
    .btn-no { background-color: #FF0000; color: white; border: none; padding: 12px 35px; font-size: 20px; font-weight: bold; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.15); z-index: 10; transition: top 0.1s ease, left 0.1s ease; }
    .gatito-lateral { position: fixed; width: 180px; height: 180px; object-fit: cover; border-radius: 50%; box-shadow: 0 6px 12px rgba(0,0,0,0.1); z-index: 1; pointer-events: none; }
    .lateral-izq { bottom: 50px; left: 50px; }
    .lateral-der { bottom: 50px; right: 50px; }
    .victoria-box { margin-top: 20px; display: none; }
    .mensaje-final { color: #FF4B4B; font-size: 45px; margin-bottom: 15px; }
    .mensaje-amor { color: #5B2C6F; font-size: 28px; font-weight: bold; margin-bottom: 10px; }
    .mensaje-mua { color: #E60067; font-size: 35px; font-weight: bold; letter-spacing: 2px; margin-bottom: 25px; }
    .firmas { color: #555555; font-size: 22px; font-style: italic; background-color: #F4ECF7; display: inline-block; padding: 10px 25px; border-radius: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
</style>
"""

# 4. Estructura HTML de la página (Título, Fotos, Botones y Música)
estructura_html = """
<div class="main-container">
    <div class="titulo">¿DIEGA LETICIA C. QUIERES SER MI NOVIA?</div>
    
    <div id="seccionPropuesta" class="contenedor-propuesta">
        <button id="botonNo" class="btn-no">NO</button>
        <img class="gatito-centro" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&auto=format&fit=crop&q=60" alt="Gatito Centro">
        <button id="botonSi" class="btn-si" onclick="declaracionExitosa()">SÍ</button>
    </div>
    
    <div id="contenedorVictoria" class="victoria-box">
        <h1 class="mensaje-final">¡SABÍA QUE DIRÍAS QUE SÍ! 🐱❤️</h1>
        <p class="mensaje-amor">Te mando besitos, tú sabrás dónde... 😏</p>
        <p class="mensaje-mua">MUAMUA 💋</p>
        <div class="firmas">👑 La mamá de Simba y papá de Michini 👑</div>
    </div>
</div>

<img class="gatito-lateral lateral-izq" src="https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400&auto=format&fit=crop&q=60" alt="Gatito Izquierda">
<img class="gatito-lateral lateral-der" src="https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=400&auto=format&fit=crop&q=60" alt="Gatito Derecha">

<audio id="musicaGatito" autoplay loop>
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>
"""

# 5. Lógica JavaScript para el movimiento del botón y acción del SÍ
logica_js = """
<script>
    const botonNo = document.getElementById('botonNo');
    const seccionPropuesta = document.getElementById('seccionPropuesta');
    const contenedorVictoria = document.getElementById('contenedorVictoria');
    const musica = document.getElementById('musicaGatito');

    document.body.addEventListener('click', () => {
        musica.play().catch(() => {});
    }, { once: true });

    botonNo.addEventListener('mouseover', function() {
        const x = Math.random() * (window.innerWidth - this.clientWidth - 100);
        const y = Math.random() * (window.innerHeight - this.clientHeight - 100);
        this.style.position = 'fixed';
        this.style.left = x + 'px';
        this.style.top = y + 'px';
        this.style.zIndex = '999';
    });

    function declaracionExitosa() {
        seccionPropuesta.style.display = 'none';
        contenedorVictoria.style.display = 'block';
        alert('¡SÍII! 😻🎉 ¡Oficialmente Novios!');
    }
</script>
"""

# 6. Unir todas las partes y renderizar la aplicación web
componente_final = estilos_css + estructura_html + logica_js
components.html(componente_final, height=750, scrolling=False)

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Propuesta Especial", layout="wide")

# CSS Responsivo mejorado
estilos_css = """
<style>
    /* Meta viewport para móviles */
    @viewport { width: device-width; initial-scale: 1.0; }
    
    body { background-color: #FFFFFF !important; margin: 0; padding: 20px; overflow-x: hidden; }
    .main-container { text-align: center; font-family: 'Arial', sans-serif; margin-top: 20px; }
    
    .titulo { color: #FF4B4B; font-size: 30px; font-weight: bold; margin-bottom: 30px; }
    
    /* Contenedor adaptativo: en celular los elementos se ven mejor si están algo más compactos */
    .contenedor-propuesta { 
        display: flex; 
        flex-direction: column; /* Apila elementos en móvil */
        align-items: center; 
        gap: 20px; 
        margin-bottom: 50px;
    }
    
    .gatito-centro { width: 200px; height: 200px; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
    
    .btn-si { background-color: #D2B4DE; color: white; padding: 20px 50px; font-size: 24px; border-radius: 15px; border: none; cursor: pointer; }
    .btn-no { background-color: #FF0000; color: white; padding: 10px 25px; font-size: 16px; border-radius: 8px; border: none; cursor: pointer; }
    
    /* Ocultar laterales en pantallas muy pequeñas para no saturar */
    @media (max-width: 600px) {
        .gatito-lateral { display: none; }
        .titulo { font-size: 24px; }
    }
    
    .gatito-lateral { position: fixed; width: 100px; height: 100px; border-radius: 50%; opacity: 0.6; }
    .lateral-izq { bottom: 10px; left: 10px; }
    .lateral-der { bottom: 10px; right: 10px; }
    
    .victoria-box { display: none; padding: 20px; }
</style>
"""

# Estructura y lógica se mantienen igual, pero el CSS de arriba ya controla el tamaño
estructura_html = """
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<div class="main-container">
    <div class="titulo">¿DIEGA LETICIA C. QUIERES SER MI NOVIA?</div>
    <div id="seccionPropuesta" class="contenedor-propuesta">
        <button id="botonNo" class="btn-no">NO</button>
        <img class="gatito-centro" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500" alt="Gatito">
        <button id="botonSi" class="btn-si" onclick="declaracionExitosa()">SÍ</button>
    </div>
    <div id="contenedorVictoria" class="victoria-box">
        <h1 class="mensaje-final">¡SABÍA QUE DIRÍAS QUE SÍ! 🐱❤️</h1>
        <p class="mensaje-amor">Te mando besitos...</p>
        <div class="firmas">👑 La mamá de Simba y papá de Michini 👑</div>
    </div>
</div>
<img class="gatito-lateral lateral-izq" src="https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400">
<img class="gatito-lateral lateral-der" src="https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=400">
"""

# El script JS también debe ser cuidadoso con los límites en móvil
logica_js = """
<script>
    const botonNo = document.getElementById('botonNo');
    const seccionPropuesta = document.getElementById('seccionPropuesta');
    const contenedorVictoria = document.getElementById('contenedorVictoria');
    const musica = document.getElementById('musicaGatito');

    // Función para intentar reproducir la música con un "intento" repetido
    function intentarReproducirMusica() {
        musica.play().then(() => {
            console.log("Música iniciada correctamente");
        }).catch(error => {
            console.log("Esperando interacción del usuario para reproducir música");
        });
    }

    // Escuchamos cualquier clic en el cuerpo de la página para activar la música
    document.body.addEventListener('click', function() {
        intentarReproducirMusica();
    }, { once: true }); // { once: true } asegura que solo lo haga una vez

    // Movimiento evasivo del botón NO
    botonNo.addEventListener('mouseover', function() {
        // Al intentar interactuar con el botón, también activamos la música
        intentarReproducirMusica();
        
        const maxX = window.innerWidth - this.clientWidth - 20;
        const maxY = window.innerHeight - this.clientHeight - 20;
        this.style.position = 'fixed';
        this.style.left = Math.random() * maxX + 'px';
        this.style.top = Math.random() * maxY + 'px';
    });

    function declaracionExitosa() {
        intentarReproducirMusica(); // Aseguramos que suene al aceptar
        seccionPropuesta.style.display = 'none';
        contenedorVictoria.style.display = 'block';
        alert('¡SÍII! 😻🎉 ¡Oficialmente Novios!');
    }
</script>

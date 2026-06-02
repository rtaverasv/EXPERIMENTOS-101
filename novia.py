import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Propuesta Especial", layout="wide")

html_total = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background-color: #FFFFFF !important; font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 20px; }
        .titulo { color: #FF4B4B; font-size: 30px; font-weight: bold; margin-bottom: 30px; }
        .contenedor-propuesta { display: flex; flex-direction: column; align-items: center; gap: 20px; }
        .gatito-centro { width: 220px; height: 220px; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
        .gatito-lateral { width: 120px; height: 120px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin: 10px; }
        .laterales { display: flex; justify-content: center; gap: 20px; margin-top: 20px; }
        .btn-si { background-color: #D2B4DE; color: white; padding: 20px 50px; font-size: 24px; border-radius: 15px; border: none; cursor: pointer; }
        .btn-no { background-color: #FF0000; color: white; padding: 10px 25px; font-size: 16px; border-radius: 8px; border: none; cursor: pointer; position: absolute; }
        .victoria-box { display: none; margin-top: 20px; }
        .mensaje-final { color: #FF4B4B; font-size: 40px; }
    </style>
</head>
<body>
    <div class="titulo">¿DIEGA LETICIA C. QUIERES SER MI NOVIA?</div>
    
    <div id="seccionPropuesta" class="contenedor-propuesta">
        <button id="botonNo" class="btn-no">NO</button>
        <img class="gatito-centro" src="https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500" alt="Gatito Centro">
        
        <div class="laterales">
            <img class="gatito-lateral" src="https://images.unsplash.com/photo-1573865526739-10659fec78a5?w=400" alt="Gatito Izq">
            <img class="gatito-lateral" src="https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=400" alt="Gatito Der">
        </div>
        
        <button id="botonSi" class="btn-si" onclick="declaracionExitosa()">SÍ</button>
    </div>
    
    <div id="contenedorVictoria" class="victoria-box">
        <h1 class="mensaje-final">¡SABÍA QUE DIRÍAS QUE SÍ! 🐱❤️</h1>
        <p>Te mando besitos... MUAMUA 💋</p>
        <p>👑 La mamá de Simba y papá de Michini 👑</p>
    </div>

    <audio id="musicaGatito" loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
    </audio>

    <script>
        const botonNo = document.getElementById('botonNo');
        const musica = document.getElementById('musicaGatito');

        function reproducir() { musica.play().catch(()=>{}); }
        document.body.addEventListener('click', reproducir, {once: true});

        botonNo.addEventListener('mouseover', function() {
            reproducir();
            this.style.left = Math.random() * (window.innerWidth - 100) + 'px';
            this.style.top = Math.random() * (window.innerHeight - 100) + 'px';
        });

        function declaracionExitosa() {
            reproducir();
            document.getElementById('seccionPropuesta').style.display = 'none';
            document.getElementById('contenedorVictoria').style.display = 'block';
        }
    </script>
</body>
</html>
"""

components.html(html_total, height=900)

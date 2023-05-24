import streamlit as st
from PIL import Image

st.write("# Wired Warefare: A Battle of Bits and Bytes ✌️🤓")

# st.sidebar.success("Mamá Linda")

st.markdown(
    "<p style='text-align: justify;'>En un mundo apasionado por la tecnología, Marcos se enfrenta al emocionante desafío de su vida en 'El Desafío Tecnológico'. A través de tres etapas llenas de preguntas y retos, debe demostrar sus conocimientos en redes, programación y electrónica. Desde la complejidad de las redes informáticas hasta la destreza en la programación y el dominio de la electrónica, Marcos se sumerge en un juego que lo llevará al límite de sus habilidades. Con cada respuesta correcta, se acerca más a la victoria y al título de 'Maestro Tecnológico'. ¿Podrá superar los obstáculos y demostrar su talento en este desafío único? Acompaña a Marcos en esta apasionante aventura y descubre cómo el conocimiento y la pasión pueden abrir las puertas hacia un mundo lleno de posibilidades tecnológicas.</p>", unsafe_allow_html=True)
image = Image.open('maxresdefault.jpg')
st.image(image, caption='Game art')
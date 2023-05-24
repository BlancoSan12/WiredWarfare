import streamlit as st
import json
import requests
# from PIL import Image
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.write("# Wired Warefare (Origenes)📖")

col1, col2 = st.columns(2)

with col1:
    lottie_load2 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_2hmszkqu.json")
    
    st.markdown("<p style='text-align: justify;'>En esta emocionante etapa del juego, Marcos se enfrenta a desafíos en tres áreas clave: redes, programación y electrónica. Debe responder preguntas y superar desafíos relacionados con cada tema para avanzar en el juego. A medida que progresa, demuestra su habilidad y conocimiento en cada área, mostrando su dominio de conceptos como enrutamiento, protocolos de comunicación, lenguajes de programación, algoritmos, electrónica y diseño de circuitos.</p>", unsafe_allow_html=True)
    
    st_lottie(
        lottie_load2,
        reverse=False,
        loop=True,
        quality="low",
        height=250,
        width=300,
    )
    
    st.markdown("<p style='text-align: justify;'>Al finalizar la etapa del juego, Marcos ha demostrado ser un experto en redes, programación y electrónica. Ha adquirido un conocimiento profundo en cada área y se ha convertido en un jugador destacado en el campo tecnológico. Su dedicación, perseverancia y pasión por la tecnología lo han llevado al éxito en este desafiante juego.</p>", unsafe_allow_html=True)
    

with col2:
    lottie_load = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_lbn31mn4.json")
    
    lottie_load3 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_7WqJfHMicP.json")
    
    st_lottie(
        lottie_load,
        reverse=False,
        loop=True,
        quality="low",
        height=250,
        width=300,
    )
    st.markdown(
        "<p style='text-align: justify;'>El juego no solo pone a prueba sus habilidades técnicas, sino que también le brinda la oportunidad de aprender y crecer. A medida que Marcos responde correctamente a las preguntas, adquiere confianza en sus habilidades y se siente orgulloso de sus logros. Cada etapa es una aventura desafiante y emocionante donde Marcos demuestra su pasión por la tecnología y su capacidad para superar obstáculos en el mundo de las redes, la programación y la electrónica.</p>", unsafe_allow_html=True)
    
    st_lottie(
        lottie_load3,
        reverse=False,
        loop=True,
        quality="low",
        height=250,
        width=300,
    )   
import streamlit as st
from PIL import Image
import time
import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.write("# Jimmy 🛵")

col1, col2 = st.columns([1, 2])

Jimmy = Image.open('personajeprin.jpeg')

col1.image(Jimmy)


with st.spinner('Conoce a nuestro personaje pricipal'):
    time.sleep(2.5)
    with col2:
       st.write("<p style='text-align: justify;'>Jimmy es un apasionado de la tecnología que desde temprana edad ha mostrado un gran interés en las redes, la programación y la electrónica. Su curiosidad y dedicación lo llevaron a convertirse en un experto en el campo. A través del desafiante juego 'Wired Warefare: A Battle of Bits and Bytes', Marcos demostró su valía al superar las etapas de preguntas en redes, programación y electrónica, obteniendo el título de 'Maestro en Telecomunicaciones'. Hoy en día, trabaja como ingeniero de software y comparte sus conocimientos para inspirar a otros en el campo de la tecnología. Su historia es un testimonio del poder del conocimiento, la pasión y la perseverancia en el mundo tecnológico.</p>", unsafe_allow_html=True)
st.success('Vive una aventura junto a él!')

lottie_load = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_x5yfDN.json")
st_lottie(
    lottie_load,
    reverse=False,
    loop=True,
    quality="low",
    height=250,
    width=300,
)
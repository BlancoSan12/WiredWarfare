import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', 
         "https://www.googleapis.com/auth/drive"]

credenciales = ServiceAccountCredentials.from_json_keyfile_name("wiredwarfare-f1c0cacb8441.json", scope)
cliente = gspread.authorize(credenciales)

# # Crear un DataFrame para almacenar los comentarios y calificaciones
feedback_data = pd.DataFrame(columns=['Comentario', 'Calificación'])


def agregar_feedback(comentario, calificacion):
    global feedback_data
    feedback_data = {'Comentario': comentario, 'Calificación': calificacion}

def mostrar_feedback():
    st.header('Retroalimentación de los usuarios')
    if len(feedback_data) == 0:
        st.write('No hay comentarios aún.')
    else:
        st.dataframe(feedback_data)

def main():
    st.title('Aplicación de Retroalimentación')
    st.write('¡Bienvenido! Por favor, déjanos tus comentarios y calificaciones.')

    comentario = st.text_area('Comentario')
    calificacion = st.slider('Calificación', min_value=1, max_value=5, step=1)

    if st.button('Enviar'):
        agregar_feedback(comentario, calificacion)
        st.success('¡Comentario enviado con éxito!')
        sheet = cliente.open("CualquierNombre").sheet1
        sheet.append_row([comentario, calificacion])

    mostrar_feedback()

if __name__ == '__main__':
    main()
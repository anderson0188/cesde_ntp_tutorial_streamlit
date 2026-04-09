import streamlit as st
import pandas as pd
import numpy as np

# Configuro la página para que se vea a lo ancho y tenga un buen título en la pestaña
st.set_page_config(page_title="Mis Ejercicios", layout="wide")
st.title("Ejercicios de Streamlit - Mi Solución")

# --- RETO 1: SALUDO ---
# Un campo de texto simple. Si el usuario escribe algo, le mando un mensaje de éxito.
st.subheader("Ejercicio 1: Saludo Simple")
nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.success(f"¡Hola, {nombre}!")
st.divider()

# --- RETO 2: CALCULADORA ---
# Multiplicación básica. Agregué un aviso por si los números se pasan de 100.
st.subheader("Ejercicio 2: Calculadora de Producto")
n1 = st.number_input("Primer número", value=0)
n2 = st.number_input("Segundo número", value=0)
st.write(f"La multiplicación da: {n1 * n2}")

if n1 > 100 or n2 > 100:
    st.warning("¡Ojo! Estás usando números muy grandes")
st.divider()

# --- RETO 3: TEMPERATURA ---
# Aquí uso radio buttons para elegir la dirección de la conversión.
st.subheader("Ejercicio 3: Convertidor de Temperatura")
modo = st.radio("¿Qué quieres convertir?", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Ingresa los grados")

if modo == "Celsius a Fahrenheit":
    resultado = (valor * 9/5) + 32
    st.info(f"El resultado es: {resultado}°F")
else:
    resultado = (valor - 32) * 5/9
    st.info(f"El resultado es: {resultado}°C")
st.divider()

# --- RETO 4: MASCOTAS ---
# Organizo todo en pestañas (tabs) para que la galería se vea limpia.
st.subheader("Ejercicio 4: Galería de Mascotas")
t1, t2, t3 = st.tabs(["Gatos", "Perros", "Aves"])

with t1:
    st.image("https://placekitten.com/300/200")
    if st.button("Me gusta el Michi"): st.toast("Te gusta esta mascota")
with t2:
    st.image("https://placedog.net/300/200")
    if st.button("Me gusta el Firulais"): st.toast("Te gusta esta mascota")
with t3:
    st.image("https://picsum.photos/id/237/300/200") # Foto de perrito/ave de ejemplo
    if st.button("Me gusta el Ave"): st.toast("Te gusta esta mascota")
st.divider()

# --- RETO 5: FORMULARIO ---
# Encierro todo en un st.form para que no se envíe hasta dar click al botón.
st.subheader("Ejercicio 5: Caja de Comentarios")
with st.form("form_comentarios"):
    asunto = st.text_input("Asunto del mensaje")
    msg = st.text_area("Comentario")
    # Validación: si el mensaje está vacío, suelto un error.
    if st.form_submit_button("Enviar"):
        if msg:
            st.json({"Asunto": asunto, "Mensaje": msg})
        else:
            st.error("No puedes enviar un mensaje vacío")
st.divider()

# --- RETO 6: LOGIN (ESTADO DE SESIÓN) ---
# Uso session_state para que la página recuerde si el usuario ya se logueó.
st.subheader("Ejercicio 6: Login Simulado")
if 'auth' not in st.session_state: 
    st.session_state.auth = False

if not st.session_state.auth:
    u = st.text_input("Usuario")
    p = st.text_input("Clave", type="password")
    if st.button("Entrar"):
        if u == "admin" and p == "1234":
            st.session_state.auth = True
            st.rerun() # Refresco para mostrar el contenido de admin
        else: 
            st.error("Credenciales incorrectas")
else:
    st.write("Bienvenido al panel de Administrador")
    if st.button("Cerrar Sesión"):
        st.session_state.auth = False
        st.rerun()
st.divider()

# --- RETO 7: LISTA DE COMPRAS ---
# Aquí los productos se guardan en una lista dentro de session_state para que no se borren.
st.subheader("Ejercicio 7: Lista de Compras")
if 'compras' not in st.session_state: 
    st.session_state.compras = []

item = st.text_input("¿Qué quieres comprar?")
c1, c2 = st.columns(2)

if c1.button("Agregar a la lista") and item:
    st.session_state.compras.append(item)
if c2.button("Vaciar carrito"):
    st.session_state.compras = []

st.write("Tu lista de hoy:", st.session_state.compras)
st.divider()

# --- RETO 8: GRÁFICO ---
# Un slider controla cuántos datos aleatorios genero en el gráfico.
st.subheader("Ejercicio 8: Gráfico Interactivo")
n = st.slider("Ajusta la cantidad de puntos", 10, 100, 50)
if st.button("Generar nuevos datos"): 
    st.rerun()

# Genero números al azar con Numpy y los paso a un gráfico de líneas
datos = pd.DataFrame(np.random.randn(n), columns=["Valor Aleatorio"])
st.line_chart(datos)
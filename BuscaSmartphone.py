import pandas as pd
import streamlit as st

URL = "https://docs.google.com/spreadsheets/d/1KFurXiZi9HMB5F3Mtvgz822Uf0_hmOFjUrond-TBPNs/export?format=csv"

def consultar_dispositivo(nome_dispositivo):
    df = pd.read_csv(URL)

    col_dispositivo = "Qual celular você está tomando posse?"
    col_nome = "Qual o seu nome completo?"
    col_local = "Em qual localidade o dispositivo estará sendo utilizado? (ex: EAJ, LAIS, etc)"

    df_filtrado = df[df[col_dispositivo] == nome_dispositivo]

    if df_filtrado.empty:
        return None

    ultimo = df_filtrado.iloc[-1]
    return ultimo[col_nome], ultimo[col_local]

st.title("📱 Controle de Dispositivos")

dispositivo = st.selectbox(
    "Selecione o dispositivo:",
    ["Smartphone S1", "Smartphone S2", "Smartphone S3", "Smartphone S4"]
)

if st.button("Consultar"):
    resultado = consultar_dispositivo(dispositivo)

    if resultado:
        nome, local = resultado
        st.success(f"Responsável: {nome}")
        st.info(f"Local: {local}")
    else:
        st.warning("Nenhum registro encontrado.")

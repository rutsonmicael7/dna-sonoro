import streamlit as st
import pandas as pd
# Aqui depois vamos colocar a lógica da API do Spotify
# Por enquanto, é a estrutura da nossa interface

st.set_page_config(page_title="DNA Sonoro", page_icon="🎵")

st.title("🎵 DNA Sonoro: Recomendação por Vibe")
st.markdown("Chega de recomendações genéricas. Digite uma música e vamos achar o 'esqueleto' acústico dela.")

song_name = st.text_input("Qual música você tem na cabeça agora?", placeholder="Ex: My Dear - Chen")

if song_name:
    st.write(f"Analisando a estrutura de '{song_name}'...")
    # Aqui o código vai buscar os Audio Features e comparar
    st.info("Buscando B-sides e raridades com a mesma pegada acústica...")
    
    # Exemplo de como os resultados vão aparecer
    col1, col2 = st.columns(2)
    with col1:
        st.success("Recomendação 1: Focada em Timbre")
    with col2:
        st.success("Recomendação 2: Focada em Melancolia")

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Configuração da página
st.set_page_config(page_title="DNA Sonoro", page_icon="🎵")

st.title("🎵 DNA Sonoro: Recomendação por Vibe")
st.markdown("Chega de recomendações por marketing. Digite uma música e vamos achar o 'esqueleto' acústico dela.")

# Base de Dados Exemplo (DNA das Músicas)
# Em um projeto maior, carregaríamos um CSV com 100k músicas aqui.
@st.cache_data
def load_data():
    data = {
        'name': ['My Dear', 'Love Shot', 'Dynamite', 'Blue Hour', 'Growl', 'Seven', 'Ditto', 'Perfect Night'],
        'artist': ['Chen', 'EXO', 'BTS', 'TXT', 'EXO', 'Jungkook', 'NewJeans', 'LE SSERAFIM'],
        # DNA: [Danceability, Energy, Acousticness, Valence]
        'danceability': [0.4, 0.8, 0.7, 0.6, 0.7, 0.7, 0.6, 0.6],
        'energy': [0.3, 0.9, 0.8, 0.7, 0.8, 0.8, 0.5, 0.7],
        'acousticness': [0.8, 0.1, 0.0, 0.1, 0.1, 0.1, 0.7, 0.2],
        'valence': [0.3, 0.7, 0.9, 0.6, 0.7, 0.8, 0.4, 0.5]
    }
    return pd.DataFrame(data)

df = load_data()

# Preparação dos dados para a IA
features = ['danceability', 'energy', 'acousticness', 'valence']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# Treinando o modelo de vizinhos mais próximos
model = NearestNeighbors(n_neighbors=3, metric='euclidean')
model.fit(df_scaled)

# Interface de Busca
target_song = st.text_input("Qual música você tem na cabeça agora?", placeholder="Ex: My Dear - Chen")

if target_song:
    # Busca simples pelo nome
    match = df[df['name'].str.contains(target_song.split(' - ')[0], case=False, na=False)]
    
    if not match.empty:
        idx = match.index[0]
        st.write(f"🧬 **DNA Identificado:** {df.iloc[idx]['name']} ({df.iloc[idx]['artist']})")
        
        # Encontrando similares
        distances, indices = model.kneighbors([df_scaled[idx]])
        
        st.subheader("Sugestões com DNA próximo:")
        for i in indices[0]:
            if i != idx:
                st.write(f"✨ **{df.iloc[i]['name']}** — {df.iloc[i]['artist']}")
                st.caption(f"Vibe similar em {(1 - distances[0][1])*100:.1f}%")
    else:
        st.error("Ainda não tenho essa música no meu banco de dados. Tente uma das sugestões acima!")

st.info("💡 Este é o motor inicial. No próximo passo, vamos conectar uma base de dados com 1 milhão de músicas.")

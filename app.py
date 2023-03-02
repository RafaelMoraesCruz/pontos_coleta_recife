from utils import URL, mapa_recife_coleta_seletiva, RESUMO
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(
   page_title="Coleta_Seletiva_Recife",
   page_icon="🧊",
   layout="wide",
)

header = st.container()
resumo = st.container()
mapa = st.container()



with header:
    st.header('Pontos de coleta seletiva na Cidade do Recife')
    st.write(f'Estudo feito com o intuito de mostrar todos os pontos de coleta seletiva na cidade do Recife, com dados coletados diretamente do portal da prefeitura. Fonte: {URL}')
    
with resumo:
    st.subheader('Informções sobre os dados/planilha')
    st.dataframe(RESUMO)
    
with mapa:
    st.subheader('Mapa de pontos da coleta seletiva em Recife')
    st_folium(mapa_recife_coleta_seletiva, width='100%')
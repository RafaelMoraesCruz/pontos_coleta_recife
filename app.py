from utils import URL, mapa_recife_coleta_seletiva, RESUMO
import streamlit as st
from streamlit_folium import st_folium

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
    st.subheader('Mapa de dos pontos da coleta seletiva')
    st_folium(mapa_recife_coleta_seletiva, width='100%')
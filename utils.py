import pandas as pd
import folium
from folium.plugins import MarkerCluster
from bs4 import BeautifulSoup
from urllib.request import urlopen
import streamlit as st
from streamlit_folium import st_folium

fp = 'http://dados.recife.pe.gov.br/pt_BR/dataset/pontos-de-coleta-seletiva'
soup = BeautifulSoup(urlopen(fp))    
URL = soup.find_all('a', {'class': 'resource-url-analytics'})[0].get('href')

resumo = pd.read_html('http://dados.recife.pe.gov.br/pt_BR/dataset/pontos-de-coleta-seletiva')
RESUMO = resumo[0]

df = pd.read_csv(URL,sep=';')

mapa_recife_coleta_seletiva = folium.Map(width=1500,height=1000,location=df[["latitude", "longitude"]].mean().to_list(), zoom_start=12)
marker_cluster = MarkerCluster().add_to(mapa_recife_coleta_seletiva)
for i,r in df.iterrows():
    location = (r["latitude"], r["longitude"])
    folium.Marker(location=location,
                      popup = r['tiporesiduo'],
                      tooltip=r['endereco'])\
    .add_to(marker_cluster)
    
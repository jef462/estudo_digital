import os
import folium
from folium.plugins import HeatMap
import pandas as pd

# 1. Base de dados simulada com coordenadas da Grande SP e ABC
dados = {
    'local': [
        'SP - Centro',
        'São Bernardo do Campo',
        'Santo André',
        'Osasco',
        'Guarulhos',
    ],
    'lat': [-23.5505, -23.6939, -23.6639, -23.5325, -23.4628],
    'lon': [-46.6333, -46.5650, -46.5383, -46.7917, -46.5333],
    'peso': [1200, 850, 600, 450, 500],  # Volume de ocorrências
}

df = pd.DataFrame(dados)

# 2. Criando o mapa com tiles do Esri (Público, sem bloqueio e sem API Key)
mapa = folium.Map(
    location=[-23.5505, -46.6333],
    zoom_start=11,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
    attr='Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
)

# 3. Extraindo as coordenadas e os pesos
dados_calor = df[['lat', 'lon', 'peso']].values.tolist()

# 4. Adicionando o Mapa de Calor (HeatMap)
HeatMap(dados_calor, radius=25, blur=15).add_to(mapa)

# 5. Definindo o caminho para gravar na pasta 'slides'
if os.path.exists('escudo-digital'):
    caminho_saida = os.path.join('escudo-digital', 'slides', 'mapa_cibercrimes_sp.html')
else:
    caminho_saida = os.path.join('..', 'slides', 'mapa_cibercrimes_sp.html')

mapa.save(caminho_saida)
print(f'Sucesso! Mapa gerado em: {caminho_saida}')
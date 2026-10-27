import os
import pandas as pd

# Dados consolidados do projeto Escudo Digital
dados = {
    'id_ocorrencia': [1, 2, 3, 4, 5, 6, 7],
    'regiao': [
        'Centro',
        'ABC Paulista',
        'ABC Paulista',
        'Zona Oeste',
        'Zona Norte',
        'Zona Leste',
        'Zona Sul',
    ],
    'cidade_bairro': [
        'São Paulo - Centro',
        'São Bernardo do Campo',
        'Santo André',
        'Osasco',
        'Guarulhos',
        'São Paulo - Tatuapé',
        'São Paulo - Santo Amaro',
    ],
    'lat': [
        -23.5505,
        -23.6939,
        -23.6639,
        -23.5325,
        -23.4628,
        -23.5405,
        -23.6528,
    ],
    'lon': [
        -46.6333,
        -46.5650,
        -46.5383,
        -46.7917,
        -46.5333,
        -46.5758,
        -46.7081,
    ],
    'tipo_crime': [
        'Roubo de Aparelho / Apps',
        'Engenharia Social / Falso Parente',
        'Clonagem de WhatsApp / Pix',
        'Fraude de E-commerce',
        'Phishing / Sites Clonados',
        'Golpe do Boleto Falso',
        'Engenharia Social / Idosos',
    ],
    'total_ocorrencias': [1200, 850, 600, 450, 500, 720, 680],
    'nivel_risco': [
        'Alto',
        'Alto',
        'Médio-Alto',
        'Médio',
        'Médio',
        'Médio-Alto',
        'Médio-Alto',
    ],
}

df = pd.DataFrame(dados)

# Caminho para salvar na pasta data/raw
caminho = (
    os.path.join('escudo-digital', 'data', 'raw', 'base_cibercrimes_sp.csv')
    if os.path.exists('escudo-digital')
    else os.path.join('..', 'data', 'raw', 'base_cibercrimes_sp.csv')
)

df.to_csv(caminho, index=False, encoding='utf-8-sig')
print(f'Base salva para o Power BI em: {caminho}')
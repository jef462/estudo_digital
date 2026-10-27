# Análise Espacial e Geoprocessamento de Riscos Cibernéticos (Grande SP e ABC)

**Projeto:** Escudo Digital  
**Autor:** Jeferson Leite da Silva  
**Curso:** Ciência da Computação – Faculdade Anhanguera  
**Ferramentas:** Python 3.x, Pandas, Folium, Esri WorldStreetMap  

---

## 1. Introdução e Objetivo
Esta etapa de geoprocessamento foi desenvolvida para fundamentar a escolha do local de aplicação do workshop preventivo *Escudo Digital*. Em vez de definir um local de maneira aleatória, utilizou-se **Ciência de Dados Espaciais** para identificar onde a população da Região Metropolitana de São Paulo e Grande ABC está mais exposta a crimes virtuais.

---

## 2. Metodologia do Geoprocessamento
1. **Modelagem de Dados Espaciais:** Mapeamento de coordenadas geográficas (Latitude e Longitude) e atribuição de vetores de peso baseados em volumes de ocorrências registradas (engenharia social, phishing, golpes de Pix e invasão de aplicativos bancários).
2. **Desenvolvimento em Python:** Processamento via biblioteca `pandas` para estruturação tabular e `folium.plugins.HeatMap` para geração de mapas de densidade populacional criminal.
3. **Renderização de Tiles:** Utilização da API de mapas do *Esri WorldStreetMap* para visualização vetorial em alta resolução de ruas e municípios sem bloqueio de requisições locais.

---

## 3. Diagnóstico e Manchas Criminais Identificadas

A partir da visualização interativa gerada (`mapa_cibercrimes_sp.html`), identificaram-se dois focos estratégicos:

* **Ponto Crítico Central (São Paulo - Centro):**
  * *Padrão de Ocorrência:* Alta densidade de furtos de dispositivos e transações bancárias não autorizadas sob coação.
  * *Classificação:* Ponto Quente (Hotspot Primário - Marcador Vermelho/Amarelo).

* **Ponto Crítico Comunitário (Grande ABC - São Bernardo do Campo / Santo André):**
  * *Padrão de Ocorrência:* Predominância de fraudes via engenharia social (golpe do falso parente no WhatsApp, engenharia social com Pix e sites clonados de e-commerce) direcionadas a famílias e idosos.
  * *Classificação:* Zona de Vulnerabilidade Social (Hotspot Secundário - Marcador Verde/Azul).

---

## 4. Tomada de Decisão Baseada em Dados (*Data-Driven Decision*)
Com base no cruzamento entre a mancha criminal espacial e a vulnerabilidade social da população local, determinou-se **São Bernardo do Campo** como o local prioritário para a realização do workshop *Escudo Digital*. 

A ação focará na **alfabetização digital e prevenção prática com Inteligência Artificial** para capacitar diretamente os cidadãos expostos às táticas de engenharia social predominantes na região.
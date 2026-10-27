markdown_content = """# TERMO DE ABERTURA (TAP) E ESTRUTURA DE DECOMPOSIÇÃO DO TRABALHO (EAP)

**Projeto:** Escudo Digital — Análise de Dados de Fraudes e Capacitação com IA contra Golpes Virtuais  
**Componente Curricular:** Projeto de Extensão I — Ciência da Computação (Anhanguera)  
**Autor:** Jeferson Leite da Silva  
**Data:** Setembro de 2026  

---

## 1. INFORMAÇÕES GERAIS E IDENTIFICAÇÃO

| Campo | Detalhamento do Projeto |
| :--- | :--- |
| **Nome do Projeto** | **Projeto Escudo Digital:** Análise de Dados de Fraudes e Capacitação com IA contra Golpes Virtuais |
| **Instituição de Ensino** | Faculdade Anhanguera — Campus São Bernardo do Campo / SP |
| **Curso / Matriz** | Bacharelado em Ciência da Computação (CIC20261.SEME-100% ONLINE) |
| **Componente Curricular** | Projeto de Extensão I — Ciência da Computação |
| **Autor / Responsável** | Jeferson Leite da Silva |
| **Público-Alvo** | Moradores da comunidade local, idosos e membros de associações comunitárias / ONGs |
| **Versão / Emissão** | Versão 1.0 (Final) — Setembro de 2026 |

---

## 2. JUSTIFICATIVA SOCIAL E TECNOLÓGICA

A evolução das tecnologias bancárias e de comunicação, aliada à popularização do PIX e das redes sociais, trouxe grandes facilidades para a sociedade, mas também impulsionou um crescimento vertiginoso nas ocorrências de crimes cibernéticos e estelionatos virtuais. No Estado de São Paulo e na região do Grande ABC, milhares de cidadãos — em especial idosos e pessoas com menor letramento digital — tornam-se vítimas diárias de táticas de **engenharia social** (como o golpe do falso parente, falsa central bancária, links maliciosos via SMS/WhatsApp e fraudes em boletos).

Muitas vezes, a abordagem preventiva tradicional falha por ser excessivamente teórica ou abstrata. Este projeto de extensão justifica-se pela necessidade de unir o **rigor da Ciência de Dados** à **praticidade da Inteligência Artificial**, transformando estatísticas reais da Segurança Pública em alertas visuais e capacitando os cidadãos a utilizarem assistentes virtuais de IA no próprio celular como um "escudo" para identificar e bloquear tentativas de fraude em tempo real.

---

## 3. OBJETIVOS DO PROJETO

### 3.1 Objetivo Geral
Desenvolver um pipeline completo de análise de dados sobre fraudes e estelionatos no Estado de São Paulo para fundamentar uma ação prática de extensão universitária, promovendo oficinas comunitárias sobre segurança digital, visualização de dados via Power BI e uso de Inteligência Artificial para prevenção de golpes.

### 3.2 Objetivos Específicos
1. **Pipeline de Dados (Engenharia & Análise):** Coletar, tratar (Python/Pandas) e armazenar (SQL/Star Schema) microdados públicos de ocorrências de crimes cibernéticos da Polícia Federal (DCIBER).
2. **Modelagem e Visualização:** Construir o Modelo Estrela (*Star Schema*) no banco relacional e desenvolver um *Dashboard* interativo no Power BI mapeando as categorias de crimes, volume de operações e estados críticos (destacando São Paulo).
3. **Oficina Prática de Capacitação:** Planejar e executar uma palestra interativa para a comunidade, apresentando o panorama dos golpes e ensinando o passo a passo para utilizar a IA como filtro de mensagens suspeitas.
4. **Material Educativo e Metodologia:** Elaborar cartilhas orientativas impressas/digitais e roteiros de apresentação em slides guiados por imagens informativas sobre comportamento seguro diante de chamadas e mensagens suspeitas.
5. **Mensuração do Impacto Social:** Aplicar pesquisas de satisfação e formulários de retenção de aprendizado (pré e pós-oficina), consolidando os resultados para avaliação acadêmica.

---

## 4. DECLARAÇÃO DO ESCOPO DO PROJETO

| DENTRO DO ESCOPO (Incluso) | FORA DO ESCOPO (Excluso) |
| :--- | :--- |
| • Coleta e ETL em Python da base da Polícia Federal (DCIBER). | • Manutenção física de computadores ou smartphones dos participantes. |
| • Modelagem Dimensional de Banco de Dados SQL (Star Schema) e Views. | • Suporte para recuperação de valores perdidos em golpes anteriores. |
| • Criação do Dashboard no Power BI. | • Consultoria jurídica individual. |
| • Elaboração do roteiro de apresentação em slides ("IA como Escudo Digital"). | • Desenvolvimento de aplicativos do zero (foco no uso de IAs já existentes). |
| • Aplicação da oficina e distribuição do Guia Prático. | |
| • Coleta de feedbacks e emissão de lista de presença. | |
| • Elaboração da Redação / Relatório Final de Extensão. | |

---

## 5. METODOLOGIA, GOVERNANÇA E CICLO PDCA

O projeto adota o framework de gestão **PDCA** (*Plan-Do-Check-Act*), garantindo controle de qualidade tanto na estrutura técnica quanto na execução comunitária:

| Etapa PDCA | Atividades e Entregáveis |
| :---: | :--- |
| **PLAN** *(Planejamento)* | Mapeamento da base da Polícia Federal, formalização do TAP/EAP, modelagem DER e criação do script DDL e ETL Python. |
| **DO** *(Execução)* | Construção do Dashboard no Power BI, confecção dos slides de treinamento de IA, realização da oficina presencial e distribuição dos guias e cartões de feedback. |
| **CHECK** *(Verificação)* | Tabulação dos dados dos formulários de feedback, cálculo do índice de satisfação e análise comparativa do nível de aprendizado pré e pós-palestra. |
| **ACT** *(Padronização)* | Elaboração do Relatório Final de Extensão Universitária e consolidação do repositório público documentado no GitHub. |

---

## 6. ESTRUTURA DE DECOMPOSIÇÃO DO TRABALHO (EAP / WBS)

O diagrama abaixo apresenta a decomposição hierárquica das entregas do projeto:

```mermaid
graph TD
    A[1.0 PROJETO ESCUDO DIGITAL] --> B[1.1 Gestão e Governança]
    A --> C[1.2 Engenharia & Modelagem de Dados]
    A --> D[1.3 Business Intelligence & Analytics]
    A --> E[1.4 Materiais Didáticos & IA]
    A --> F[1.5 Ação Comunitária Presencial]
    A --> G[1.6 Consolidação do Portfólio]

    B --> B1[1.1.1 Termo de Abertura TAP]
    B --> B2[1.1.2 Estrutura da EAP]
    B --> B3[1.1.3 Documentação DER]
    B --> B4[1.1.4 Relatório Final de Extensão]

    C --> C1[1.2.1 Coleta dos Microdados DCIBER/PF]
    C --> C2[1.2.2 Script DDL Schema SQL]
    C --> C3[1.2.3 Script ETL Python]
    C --> C4[1.2.4 Banco SQLite e Views]

    D --> D1[1.3.1 Conexão Power BI ao SQLite/CSV]
    D --> D2[1.3.2 Criação do Dashboard Interativo]
    D --> D3[1.3.3 Análise de Insights em SP]

    E --> E1[1.4.1 Roteiro dos Slides da Palestra]
    E --> E2[1.4.2 Prompts de Análise de Golpes em IA]
    E --> E3[1.4.3 Guia Prático Impresso]
    E --> E4[1.4.4 Lista de Presença & Feedback]

    F --> F1[1.5.1 Alinhamento Logístico do Espaço]
    F --> F2[1.5.2 Apresentação da Palestra]
    F --> F3[1.5.3 Coleta de Assinaturas e Pesquisas]

    G --> G1[1.6.1 Arquitetura de Pastas no VS Code]
    G --> G2[1.6.2 Repositório Público no GitHub]
    G --> G3[1.6.3 Redação do README.md Profissional]
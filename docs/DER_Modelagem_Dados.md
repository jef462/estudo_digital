python -c "import os; md = '''# DOCUMENTAÇÃO DA MODELAGEM DE DADOS (DER)

**Projeto:** Escudo Digital — Análise de Crimes Cibernéticos  
**Componente Curricular:** Projeto de Extensão I — Ciência da Computação (Anhanguera)  
**Autor:** Jeferson Leite da Silva  
**Arquitetura:** Modelagem Dimensional em Modelo Estrela (*Star Schema*)  

---

## 1. DIAGRAMA DE ENTIDADE-RELACIONAMENTO (DER)

```mermaid
erDiagram
    DIM_LOCAL ||--o{ FATO_CRIMES_CIBERNETICOS : contem
    DIM_TEMPO ||--o{ FATO_CRIMES_CIBERNETICOS : registra
    DIM_CATEGORIA ||--o{ FATO_CRIMES_CIBERNETICOS : classifica

    DIM_LOCAL {
        int id_local PK
        string uf
        string pais
        string regiao_macro
    }

    DIM_TEMPO {
        int id_tempo PK
        int ano
        int mes_num
        string mes_nome
        string trimestre
    }

    DIM_CATEGORIA {
        int id_categoria PK
        string area_atribuicao
        string grupo_crime
    }

    FATO_CRIMES_CIBERNETICOS {
        int id_fato PK
        int id_local FK
        int id_tempo FK
        int id_categoria FK
        int qtd_operacoes
        int prisoes_flagrante
        int prisoes_preventivas
        int prisoes_temporarias
        int total_prisoes
        int mbas
        int vitimas_resgatadas
    }
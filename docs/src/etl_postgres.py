import pandas as pd
from sqlalchemy import create_engine, text
import os

def exportar_para_postgres():
    print("=" * 70)
    print("🐘 INICIANDO CARGA E ADMINISTRAÇÃO NO POSTGRESQL")
    print("=" * 70)

    # Configurações de Conexão com o PostgreSQL
    USUARIO = 'postgres'
    SENHA = '1991'
    HOST = 'localhost'
    PORTA = '5432'
    BANCO = 'db_escudo_digital'

    # Uso do driver psycopg2 explicitamente na URL de conexão
    string_conexao = f"postgresql+psycopg2://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{BANCO}"
    
    try:
        engine = create_engine(string_conexao)
        conn = engine.connect()
        print("✅ Conexão estabelecida com o PostgreSQL com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao PostgreSQL: {e}")
        print("💡 Certifica-te de que o banco de dados 'db_escudo_digital' foi criado no PostgreSQL/pgAdmin.")
        return

    caminho_csv = os.path.join('data', 'processed', 'crimes_ciberneticos_consolidados.csv')
    if not os.path.exists(caminho_csv):
        print(f"⚠️ Ficheiro {caminho_csv} não encontrado. Executa 'python src/etl.py' primeiro.")
        return

    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')

    # 1. Tabela Dimensão Local
    df_local = df[['uf', 'pais', 'regiao_macro']].drop_duplicates().reset_index(drop=True)
    df_local.index += 1
    df_local.index.name = 'id_local'
    df_local = df_local.reset_index()

    # 2. Tabela Dimensão Tempo
    df_tempo = df[['ano', 'mes_num', 'mes', 'trimestre']].drop_duplicates().reset_index(drop=True)
    df_tempo = df_tempo.rename(columns={'mes': 'mes_nome'})
    df_tempo.index += 1
    df_tempo.index.name = 'id_tempo'
    df_tempo = df_tempo.reset_index()

    # 3. Tabela Dimensão Categoria
    df_categoria = df[['area_atribuicao', 'grupo_crime']].drop_duplicates().reset_index(drop=True)
    df_categoria.index += 1
    df_categoria.index.name = 'id_categoria'
    df_categoria = df_categoria.reset_index()

    # 4. Tabela Fato
    df_fato = df.merge(df_local, on=['uf', 'pais', 'regiao_macro']) \
                .merge(df_tempo, left_on=['ano', 'mes_num', 'mes', 'trimestre'], right_on=['ano', 'mes_num', 'mes_nome', 'trimestre']) \
                .merge(df_categoria, on=['area_atribuicao', 'grupo_crime'])

    df_fato_final = df_fato[[
        'id_local', 'id_tempo', 'id_categoria', 'qtd_operacoes',
        'prisoes_flagrante', 'prisoes_preventivas', 'prisoes_temporarias',
        'total_prisoes', 'mbas', 'vitimas_resgatadas'
    ]].copy()
    
    df_fato_final.index += 1
    df_fato_final.index.name = 'id_fato'
    df_fato_final = df_fato_final.reset_index()

    print("🔄 Povoando tabelas no PostgreSQL...")
    df_local.to_sql('dim_local', engine, if_exists='replace', index=False)
    df_tempo.to_sql('dim_tempo', engine, if_exists='replace', index=False)
    df_categoria.to_sql('dim_categoria', engine, if_exists='replace', index=False)
    df_fato_final.to_sql('fato_crimes_ciberneticos', engine, if_exists='replace', index=False)

    # 5. Criando a View Analítica para o Power BI
    print("🛠️ Criando View Analítica 'vw_fato_completa'...")
    sql_view = """
    CREATE OR REPLACE VIEW vw_fato_completa AS
    SELECT 
        f.id_fato,
        l.uf,
        l.pais,
        l.regiao_macro,
        t.ano,
        t.mes_num,
        t.mes_nome AS mes,
        t.trimestre,
        c.area_atribuicao,
        c.grupo_crime,
        f.qtd_operacoes,
        f.prisoes_flagrante,
        f.prisoes_preventivas,
        f.prisoes_temporarias,
        f.total_prisoes,
        f.mbas,
        f.vitimas_resgatadas
    FROM fato_crimes_ciberneticos f
    JOIN dim_local l ON f.id_local = l.id_local
    JOIN dim_tempo t ON f.id_tempo = t.id_tempo
    JOIN dim_categoria c ON f.id_categoria = c.id_categoria;
    """
    with engine.connect() as con:
        con.execute(text(sql_view))
        con.commit()

    print("\n" + "=" * 70)
    print("✅ CARGA E CONFIGURAÇÃO NO POSTGRESQL CONCLUÍDAS COM SUCESSO!")
    print("=" * 70)
    print(f"📊 Registos carregados na Fato do PostgreSQL: {len(df_fato_final)}")

if __name__ == "__main__":
    exportar_para_postgres()
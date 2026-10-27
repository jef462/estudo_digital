import pandas as pd
import sqlite3
import os
import glob

def executar_etl():
    print("=" * 70)
    print("🚀 INICIANDO ETAPA 1 — PIPELINE DE ETL E TRATAMENTO EM PYTHON")
    print("=" * 70)

    # 1. Definição dos caminhos das pastas
    pasta_raw = 'data/raw'
    pasta_processed = 'data/processed'
    os.makedirs(pasta_processed, exist_ok=True)

    caminho_db = os.path.join(pasta_processed, 'escudo_digital.db')
    caminho_csv_final = os.path.join(pasta_processed, 'crimes_ciberneticos_consolidados.csv')

    # 2. Localização dos arquivos CSV da Polícia Federal
    arquivos = glob.glob(os.path.join(pasta_raw, '*.csv'))
    if not arquivos:
        print("⚠️ Nenhum arquivo .csv foi encontrado na pasta 'data/raw/'.")
        print(" Certifique-se de colá-los em data/raw/ antes de rodar.")
        return

    dfs = []
    
    # Mapeamento de colunas para padronizar o ano de 2023 (onde a coluna chama 'MBAS EXPEDIDOS')
    rename_2023 = {
        'PAÍS': 'pais', 'UF': 'uf', 'ANO': 'ano', 'MÊS': 'mes',
        'ÁREA DE ATRIBUIÇÃO': 'area_atribuicao',
        'QTD DE OPERAÇÕES': 'qtd_operacoes',
        'PRISÕES EM FLAGRANTE': 'prisoes_flagrante',
        'MBAS EXPEDIDOS': 'mbas',
        'PRISÕES PREVENTIVAS EXPEDIDAS': 'prisoes_preventivas',
        'PRISÕES TEMPORÁRIAS EXPEDIDAS': 'prisoes_temporarias'
    }

    # Mapeamento para 2025 e 2026 (onde a coluna chama 'MBAS CUMPRIDOS')
    rename_2025_2026 = {
        'PAÍS': 'pais', 'UF': 'uf', 'ANO': 'ano', 'MÊS': 'mes',
        'ÁREA DE ATRIBUIÇÃO': 'area_atribuicao',
        'QTD DE OPERAÇÕES': 'qtd_operacoes',
        'PRISÕES EM FLAGRANTE': 'prisoes_flagrante',
        'QTD DE VÍTIMAS DE ABUSO SEXUAL INFANTOJUVENIL RESGATADAS': 'vitimas_resgatadas',
        'MBAS CUMPRIDOS': 'mbas',
        'PRISÕES PREVENTIVAS CUMPRIDAS': 'prisoes_preventivas',
        'PRISÕES TEMPORÁRIAS CUMPRIDAS': 'prisoes_temporarias'
    }

    # 3. Leitura e Limpeza Inicial
    for arq in arquivos:
        nome_arq = os.path.basename(arq)
        print(f"📖 Lendo e tratando arquivo: {nome_arq}")
        
        try:
            df = pd.read_csv(arq, sep=';', encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(arq, sep=';', encoding='latin1')

        # Remove linhas totalmente vazias ou sem ano informado
        df = df.dropna(subset=['ANO'])

        if 'MBAS EXPEDIDOS' in df.columns:
            df = df.rename(columns=rename_2023)
            df['vitimas_resgatadas'] = 0
        else:
            df = df.rename(columns=rename_2025_2026)

        dfs.append(df)

    # 4. Consolidação dos DataFrames
    df_raw = pd.concat(dfs, ignore_index=True)

    # Tratamento de tipos numéricos e preenchimento de nulos com zero
    cols_numericas = ['ano', 'qtd_operacoes', 'prisoes_flagrante', 'mbas',
                      'prisoes_preventivas', 'prisoes_temporarias', 'vitimas_resgatadas']
    
    for col in cols_numericas:
        df_raw[col] = pd.to_numeric(df_raw[col], errors='coerce').fillna(0).astype(int)

    # Limpeza de espaços em branco nas colunas de texto
    cols_texto = ['pais', 'uf', 'mes', 'area_atribuicao']
    for col in cols_texto:
        df_raw[col] = df_raw[col].astype(str).str.strip()

    # 5. Conexão ao Banco SQLite
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    # Habilita suporte a chaves estrangeiras no SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 6. Aplicação da DDL / Schema (Criação das Tabelas)
    print("\n🛠️ Criando estrutura de tabelas Star Schema no SQLite...")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_local (
        id_local INTEGER PRIMARY KEY AUTOINCREMENT,
        uf TEXT NOT NULL UNIQUE,
        pais TEXT NOT NULL,
        regiao_macro TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_tempo (
        id_tempo INTEGER PRIMARY KEY AUTOINCREMENT,
        ano INTEGER NOT NULL,
        mes_num INTEGER NOT NULL,
        mes_nome TEXT NOT NULL,
        trimestre TEXT NOT NULL,
        UNIQUE(ano, mes_num)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        area_atribuicao TEXT NOT NULL UNIQUE,
        grupo_crime TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fato_crimes_ciberneticos (
        id_fato INTEGER PRIMARY KEY AUTOINCREMENT,
        id_local INTEGER NOT NULL,
        id_tempo INTEGER NOT NULL,
        id_categoria INTEGER NOT NULL,
        qtd_operacoes INTEGER DEFAULT 0,
        prisoes_flagrante INTEGER DEFAULT 0,
        prisoes_preventivas INTEGER DEFAULT 0,
        prisoes_temporarias INTEGER DEFAULT 0,
        total_prisoes INTEGER DEFAULT 0,
        mbas INTEGER DEFAULT 0,
        vitimas_resgatadas INTEGER DEFAULT 0,
        FOREIGN KEY (id_local) REFERENCES dim_local(id_local),
        FOREIGN KEY (id_tempo) REFERENCES dim_tempo(id_tempo),
        FOREIGN KEY (id_categoria) REFERENCES dim_categoria(id_categoria)
    );
    """)
    conn.commit()

    # Funções auxiliares para enriquecimento de dados
    def definir_regiao(uf):
        if uf in ['SP', 'RJ', 'MG', 'ES']: return 'Sudeste'
        elif uf in ['PR', 'SC', 'RS']: return 'Sul'
        elif uf in ['BA', 'PE', 'CE', 'MA', 'PB', 'AL', 'SE', 'PI', 'RN']: return 'Nordeste'
        elif uf in ['AM', 'PA', 'AP', 'TO', 'RO', 'RR', 'AC']: return 'Norte'
        elif uf in ['DF', 'GO', 'MT', 'MS']: return 'Centro-Oeste'
        else: return 'Âmbito Federal / Órgão Central'

    mapa_meses = {'Jan':1, 'Fev':2, 'Mar':3, 'Abr':4, 'Mai':5, 'Jun':6, 
                  'Jul':7, 'Ago':8, 'Set':9, 'Out':10, 'Nov':11, 'Dez':12}

    # 7. Carga das Tabelas Dimensão
    print("🔄 Povoando Tabelas Dimensão (dim_local, dim_tempo, dim_categoria)...")

    # dim_local
    for _, row in df_raw[['uf', 'pais']].drop_duplicates().iterrows():
        regiao = definir_regiao(row['uf'])
        cursor.execute("INSERT OR IGNORE INTO dim_local (uf, pais, regiao_macro) VALUES (?, ?, ?);",
                       (row['uf'], row['pais'], regiao))

    # dim_tempo
    for _, row in df_raw[['ano', 'mes']].drop_duplicates().iterrows():
        m_num = mapa_meses.get(row['mes'], 1)
        trimestre = f"T{(m_num - 1) // 3 + 1}"
        cursor.execute("INSERT OR IGNORE INTO dim_tempo (ano, mes_num, mes_nome, trimestre) VALUES (?, ?, ?, ?);",
                       (int(row['ano']), m_num, row['mes'], trimestre))

    # dim_categoria
    for cat in df_raw['area_atribuicao'].unique():
        grupo = 'Fraude Financeira / Estelionato' if 'Fraudes' in cat else 'Outros Crimes Cibernéticos'
        cursor.execute("INSERT OR IGNORE INTO dim_categoria (area_atribuicao, grupo_crime) VALUES (?, ?);",
                       (cat, grupo))

    conn.commit()

    # 8. Carga da Tabela Fato
    print("📊 Povoando Tabela Fato (fato_crimes_ciberneticos)...")
    
    # Limpa dados antigos da fato para evitar duplicidade na reexecução
    cursor.execute("DELETE FROM fato_crimes_ciberneticos;")

    for _, row in df_raw.iterrows():
        m_num = mapa_meses.get(row['mes'], 1)

        # Busca das chaves primárias nas dimensões
        cursor.execute("SELECT id_local FROM dim_local WHERE uf = ?;", (row['uf'],))
        id_local = cursor.fetchone()[0]

        cursor.execute("SELECT id_tempo FROM dim_tempo WHERE ano = ? AND mes_num = ?;", (int(row['ano']), m_num))
        id_tempo = cursor.fetchone()[0]

        cursor.execute("SELECT id_categoria FROM dim_categoria WHERE area_atribuicao = ?;", (row['area_atribuicao'],))
        id_categoria = cursor.fetchone()[0]

        tot_prisoes = row['prisoes_flagrante'] + row['prisoes_preventivas'] + row['prisoes_temporarias']

        cursor.execute("""
            INSERT INTO fato_crimes_ciberneticos (
                id_local, id_tempo, id_categoria, qtd_operacoes, 
                prisoes_flagrante, prisoes_preventivas, prisoes_temporarias, 
                total_prisoes, mbas, vitimas_resgatadas
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            id_local, id_tempo, id_categoria, int(row['qtd_operacoes']),
            int(row['prisoes_flagrante']), int(row['prisoes_preventivas']), int(row['prisoes_temporarias']),
            int(tot_prisoes), int(row['mbas']), int(row['vitimas_resgatadas'])
        ))

    conn.commit()

    # 9. Exportação do CSV Consolidado Limpo (para fácil uso no Power BI / Excel)
    df_export = pd.read_sql_query("""
        SELECT 
            f.id_fato, l.uf, l.pais, l.regiao_macro,
            t.ano, t.mes_num, t.mes_nome AS mes, t.trimestre,
            c.area_atribuicao, c.grupo_crime,
            f.qtd_operacoes, f.prisoes_flagrante, f.prisoes_preventivas,
            f.prisoes_temporarias, f.total_prisoes, f.mbas, f.vitimas_resgatadas
        FROM fato_crimes_ciberneticos f
        JOIN dim_local l ON f.id_local = l.id_local
        JOIN dim_tempo t ON f.id_tempo = t.id_tempo
        JOIN dim_categoria c ON f.id_categoria = c.id_categoria
        ORDER BY t.ano ASC, t.mes_num ASC, l.uf ASC;
    """, conn)

    df_export.to_csv(caminho_csv_final, index=False, sep=';', encoding='utf-8')
    conn.close()

    print("\n" + "=" * 70)
    print("✅ TRATAMENTO E CARGA CONCLUÍDOS COM SUCESSO!")
    print("=" * 70)
    print(f"🗄️ Banco de Dados Relacional SQLite: {caminho_db}")
    print(f"📄 Arquivo CSV Limpo e Consolidado: {caminho_csv_final}")
    print(f"📈 Total de registros carregados na Fato: {len(df_export)}")

if __name__ == "__main__":
    executar_etl()